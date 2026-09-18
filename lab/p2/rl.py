"""Phase 2 RL fine-tune: antithetic (mirrored-sampling) evolution strategy on
the residual policy's OUTPUT HEADS ONLY (frac_head, prio_head -- 3598 floats),
warm-started from lab/p2/data/bc_model_resid.pt (body frozen; heads exactly
zero there, so theta=0 == raw v41 exactly, see market_env.apply_policy).

Why ES over PPO here (goal.md Phase 2 step 2 names PPO but leaves the choice
open, "You may choose PPO or antithetic evolution strategies... justify"):
  - Reward is terminal win/loss/tie only (project rule) against a mostly
    DETERMINISTIC opponent (v41 mirror) -- there is no per-step reward to
    bootstrap a value function from, so PPO's main advantage (credit
    assignment via a learned critic) buys nothing here.
  - The searchable parameter space is tiny by construction (2 zero-init
    linear heads) -- ES scales fine to ~3.6k parameters with no backprop
    through the (non-differentiable) game engine.
  - Paired evaluation with common random numbers: v41 (theta=0) is
    deterministic given (seed, seat, opponent), so its result on every tuple
    is computed ONCE, cached to disk, and reused forever. Every candidate's
    fitness is then result(candidate) - result(base) on the SAME tuples, in
    {-2,-1,0,1,2} per game -- a perturbation that changes no outcome scores
    0, not noise. This is a much lower-variance signal than raw win/loss
    (run 1's mistake, see lab/p2/data/rl_run1: raw wins-losses fitness let
    the population's random opponent/seed draw dominate the gradient, drove
    ||theta|| to its cap in 6 iterations, and produced a checkpoint that lost
    to v41 26-14 and to soil 13-27 on validation -- worse than doing nothing).

RUN 1 POST-MORTEM (kept at lab/p2/data/rl_run1, not deleted): raw
wins-losses fitness plus a loose trust region (||theta|| <= 3.0, sigma=0.03,
lr=0.02) let the center drift to the cap within 6 iterations and stay
pinned there while validation record vs v41 fell to 14-26 (worse than the
zero residual, which is exactly 20-20 by seat symmetry) and vs soil fell to
27-13 (worse than v41's clean 20-0). Root cause: fitness that isn't paired
against the base measures opponent-mix/seed luck as much as policy quality,
and a soft L2 penalty alone didn't stop a bad gradient direction from being
reinforced every iteration. Fix, per audit: (1) paired-vs-base fitness, (2)
a ~10x tighter trust region (max ||theta||=0.3, sigma/lr ~10x smaller), (3)
an explicit accept/reject gate so the center only ever moves when a fixed
held-out probe block says the new center is at least as good as the old one
-- otherwise the step shrinks (sigma halved) and the center holds.

Body is NEVER updated (zero BC gradient by construction, see bc.py). Every
saved checkpoint is a complete, valid MarketMLP checkpoint (body + current
heads) -- directly loadable by fidelity.load_policy and export.export.

Usage (resumable: re-running with the same --run-dir continues from the
highest ckpt_iter*.pt found there):
    python -m lab.p2.rl --iterations 20 --workers 10 --pairs 4 --seeds-per-iter 2
"""
import argparse
import hashlib
import io
import json
import time
from contextlib import redirect_stdout
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import torch

from lab import ledger
from lab.p2.bc import MarketMLP
from lab.p2 import market_env
from lab.p2.market_env import FREE_ITEMS

DATA_DIR = Path(__file__).resolve().parent / "data"
BODY_CKPT = DATA_DIR / "bc_model_resid.pt"          # frozen body + zero heads warm start
DEFAULT_RUN_DIR = DATA_DIR / "rl"

N_ITEMS = len(FREE_ITEMS)
HEAD_KEYS = ("frac_head.weight", "frac_head.bias", "prio_head.weight", "prio_head.bias")

TRAIN_SEED_BASE = 600000     # disjoint from gate blocks (850k/860k/870k/910k) and our own val (620k+)
TRUST_SEED_BASE = 615000     # fixed accept/reject probe block, disjoint from training and validation seeds
WEAK_POOL = ["opp_soil", "opp_salem2900", "c94"]   # low-rate regression guard, per goal.md Phase 2 design
SCORE = {"W": 1, "L": -1, "T": 0}

_BODY_CACHE = {}


# ---------------------------------------------------------------------------
# theta <-> state_dict plumbing
# ---------------------------------------------------------------------------

def _get_body(in_dim, hidden):
    key = (str(BODY_CKPT), in_dim, hidden)
    if key not in _BODY_CACHE:
        ckpt = torch.load(BODY_CKPT, map_location="cpu", weights_only=False)
        assert ckpt["in_dim"] == in_dim and ckpt["hidden"] == hidden
        sd = ckpt["state_dict"]
        _BODY_CACHE[key] = {k: sd[k].clone() for k in ("body.0.weight", "body.0.bias", "body.2.weight", "body.2.bias")}
    return _BODY_CACHE[key]


def theta_dim(hidden=256, n_items=N_ITEMS):
    return 2 * (n_items * hidden + n_items)  # frac_head + prio_head, weight+bias each


def unflatten_heads(theta, hidden, n_items):
    theta = np.asarray(theta, dtype=np.float32)
    i = 0
    fw = theta[i:i + n_items * hidden].reshape(n_items, hidden); i += n_items * hidden
    fb = theta[i:i + n_items]; i += n_items
    pw = theta[i:i + n_items * hidden].reshape(n_items, hidden); i += n_items * hidden
    pb = theta[i:i + n_items]; i += n_items
    assert i == len(theta)
    return {"frac_head.weight": fw, "frac_head.bias": fb, "prio_head.weight": pw, "prio_head.bias": pb}


def build_model(theta, in_dim=58, hidden=256, n_items=N_ITEMS):
    body = _get_body(in_dim, hidden)
    heads = unflatten_heads(theta, hidden, n_items)
    model = MarketMLP(in_dim, hidden, n_items)
    sd = model.state_dict()
    for k, v in body.items():
        sd[k] = v
    for k, v in heads.items():
        sd[k] = torch.from_numpy(v)
    model.load_state_dict(sd)
    model.eval()
    return model


def save_checkpoint(theta, path, in_dim=58, hidden=256, n_items=N_ITEMS):
    model = build_model(theta, in_dim, hidden, n_items)
    torch.save({"state_dict": model.state_dict(), "in_dim": in_dim, "hidden": hidden}, path)


def theta_sha(theta):
    return hashlib.sha256(np.asarray(theta, dtype=np.float32).tobytes()).hexdigest()[:16]


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# game playing (runs in worker processes -- no sqlite access here, mirrors
# lab.arena's convention of writing to the ledger only in the parent)
# ---------------------------------------------------------------------------

def _seat_result(s_c, s_o, r_c, r_o):
    ok_c = s_c == "DONE" and r_c is not None
    ok_o = s_o == "DONE" and r_o is not None
    if ok_c != ok_o:
        return "W" if ok_c else "L"
    if not ok_c:
        return "T"
    return "W" if r_c > r_o else ("L" if r_c < r_o else "T")


def _play_one(theta, opp_path, seed, seat, in_dim, hidden, n_items, collect_stats, steps=720):
    """Worker task. theta: list/np.ndarray of head params (all-zero = raw v41
    exactly). Returns a plain dict."""
    model = build_model(np.asarray(theta, dtype=np.float32), in_dim, hidden, n_items)
    policy = model.as_policy()
    v41 = market_env._load_v41_agent()  # fresh isolated namespace per game, see market_env docstring
    stats = {"turns": 0, "changed": 0, "abs_frac_sum": 0.0, "abs_prio_sum": 0.0}

    def stat_policy(feats):
        df, dp = policy(feats)
        if collect_stats:
            stats["turns"] += 1
            stats["abs_frac_sum"] += float(np.abs(df).sum())
            stats["abs_prio_sum"] += float(np.abs(dp).sum())
        return df, dp

    def cand_agent(observation, configuration=None):
        base_action = v41(observation, configuration)
        out = market_env.apply_policy(observation, base_action, stat_policy)
        if collect_stats and out["market"] != base_action["market"]:
            stats["changed"] += 1
        return out

    agents = [cand_agent, opp_path] if seat == 0 else [opp_path, cand_agent]
    buf = io.StringIO()
    t0 = time.perf_counter()
    with redirect_stdout(buf):
        import kaggle_environments as ke  # import here too: swallows its one-time OpenSpiel-list spam
        env = ke.make("kaggriculture", configuration={"episodeSteps": steps, "seed": seed}, debug=False)
        env.run(agents)
        last = env.steps[-1]
    wall_ms = (time.perf_counter() - t0) * 1000

    r0, r1 = last[0].reward, last[1].reward
    s0, s1 = last[0].status, last[1].status
    r_c, r_o = (r0, r1) if seat == 0 else (r1, r0)
    s_c, s_o = (s0, s1) if seat == 0 else (s1, s0)
    return {
        "seed": seed, "seat": seat, "opp_path": opp_path,
        "r0": r0, "r1": r1, "s0": s0, "s1": s1,
        "cand_result": _seat_result(s_c, s_o, r_c, r_o),
        "wall_ms": wall_ms, "stats": stats if collect_stats else None,
    }


def _run_games(tasks, workers):
    results = [None] * len(tasks)
    if not tasks:
        return results
    with ProcessPoolExecutor(max_workers=min(workers, len(tasks))) as ex:
        futs = {ex.submit(_play_one, *t): i for i, t in enumerate(tasks)}
        for fut in as_completed(futs):
            i = futs[fut]
            try:
                results[i] = fut.result()
            except Exception as exc:
                print(f"HARNESS_ERROR task={i}: {exc!r}")
                results[i] = {"error": repr(exc)}
    return results


# ---------------------------------------------------------------------------
# base (theta=0 == raw v41) result cache -- deterministic per (seed, seat,
# opponent), computed once and reused for every iteration's paired fitness,
# every accept/reject probe, and every validation call.
# ---------------------------------------------------------------------------

def _cache_key(seed, seat, opp):
    return f"{seed}:{seat}:{opp}"


def _load_cache(run_dir):
    p = run_dir / "base_cache.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def _save_cache(run_dir, cache):
    (run_dir / "base_cache.json").write_text(json.dumps(cache), encoding="utf-8")


def ensure_base(tuples, cache, opps, workers, run_dir, conn=None, batch_id=None):
    """tuples: iterable of (seed, seat, opp_name). Fills `cache` in place with
    any missing base (theta=0) results and persists it. theta=0 reproduces
    v41 exactly regardless of the frozen body's random weights (tanh(0)=0),
    so this is genuinely "what v41 itself scores", playable once. Any newly
    played base game is also a real training game -- recorded in the ledger
    (if conn/batch_id given) under v41's own registered sha, since theta=0 IS
    v41 bit-for-bit, not a synthetic "rl:" marker."""
    tuples = list(dict.fromkeys(tuples))  # dedupe, keep order
    missing = [t for t in tuples if _cache_key(*t) not in cache]
    if not missing:
        return cache
    zeros = np.zeros(theta_dim(), dtype=np.float32).tolist()
    tasks = [(zeros, opps[opp]["path"], seed, seat, 58, 256, N_ITEMS, False) for (seed, seat, opp) in missing]
    results = _run_games(tasks, workers)
    rows = []
    for (seed, seat, opp), r in zip(missing, results):
        if "error" in r:
            continue
        cache[_cache_key(seed, seat, opp)] = r["cand_result"]
        rows.append({
            "game_id": f"rlbase-{opp}-{seed}-{seat}", "seed": seed, "seat": seat,
            "s0": r["s0"], "s1": r["s1"], "r0": r["r0"], "r1": r["r1"], "wall_ms": r["wall_ms"],
            "sha_cand": opps["opp_v41"]["sha8"], "opp_sha": opps[opp]["sha8"],
        })
    _save_cache(run_dir, cache)
    if conn is not None and batch_id is not None and rows:
        _record_games(batch_id, batch_id, f"base-fill {len(rows)} games", rows, opps, conn)
    return cache


def _record_games(batch_id, label, seed_block, rows, opp_paths_by_name, conn):
    from lab.arena import score as _p0_score
    ledger.add_batch(batch_id, label, seed_block, {"n_games": len(rows)}, conn=conn)
    for r in rows:
        p0_result, p0_margin = _p0_score(r["s0"], r["s1"], r["r0"], r["r1"])
        sha_cand, opp_sha = r["sha_cand"], r["opp_sha"]
        sha_p0, sha_p1 = (sha_cand, opp_sha) if r["seat"] == 0 else (opp_sha, sha_cand)
        ledger.add_game({
            "game_id": r["game_id"], "batch_id": batch_id, "sha_p0": sha_p0, "sha_p1": sha_p1,
            "seed": r["seed"], "steps": 720, "reward_p0": r["r0"], "reward_p1": r["r1"],
            "status_p0": r["s0"], "status_p1": r["s1"],
            "result": p0_result, "margin": p0_margin, "wall_ms": r["wall_ms"], "replay_path": None,
        }, conn=conn)


def _centered_ranks(x):
    x = np.asarray(x, dtype=np.float64)
    if len(x) <= 1:
        return np.zeros_like(x)
    order = np.argsort(x)
    ranks = np.empty(len(x))
    ranks[order] = np.arange(len(x))
    return ranks / (len(x) - 1) - 0.5


# ---------------------------------------------------------------------------
# main training loop
# ---------------------------------------------------------------------------

def _resolve_opponents(names):
    out = {}
    for n in names:
        row = ledger.get_artifact_by_name(n)
        if row is None:
            raise SystemExit(f"artifact not registered: {n}")
        out[n] = {"path": row["path"], "sha8": row["sha256"][:16]}
    return out


def _latest_iter(run_dir):
    ckpts = sorted(run_dir.glob("ckpt_iter*.pt"))
    if not ckpts:
        return 0, None
    last = ckpts[-1]
    return int(last.stem.split("ckpt_iter")[1]), last


def _load_theta(ckpt_path):
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    sd = ckpt["state_dict"]
    return np.concatenate([sd[k].detach().cpu().numpy().reshape(-1) for k in HEAD_KEYS]).astype(np.float32)


def _paired_fitness(theta_rows, cache, weak_penalty=1.0):
    """theta_rows: list of (seed, seat, opp_name, cand_result). Returns total
    paired score = sum(score(cand) - score(base)) plus a flat -weak_penalty
    for every LOSS to a weak-pool opponent (regression guard), independent
    of what the base did there (base essentially always beats the weak pool,
    so this mostly reinforces the pairing signal rather than replacing it)."""
    total = 0.0
    for seed, seat, opp, cand_result in theta_rows:
        base_result = cache[_cache_key(seed, seat, opp)]
        total += SCORE[cand_result] - SCORE[base_result]
        if opp in WEAK_POOL and cand_result == "L":
            total -= weak_penalty
    return total


def run(args):
    run_dir = Path(args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    log_path = run_dir / "log.jsonl"
    state_path = run_dir / "state.json"

    opps = _resolve_opponents(["opp_v41"] + WEAK_POOL)
    val_lo, val_hi = (int(x) for x in args.val_seeds.split("-"))
    val_seeds = list(range(val_lo, val_hi + 1))
    trust_seeds = list(range(TRUST_SEED_BASE, TRUST_SEED_BASE + args.trust_block_seeds))
    trust_tuples = [(s, seat, "opp_v41") for s in trust_seeds for seat in (0, 1)]

    cache = _load_cache(run_dir)
    conn = ledger.connect()

    # One-time baseline: what the ZERO residual (raw v41) itself scores on
    # the validation block. This is the bar a checkpoint must clear -- not
    # "best so far", which run 1 got wrong by tracking best-vs-population
    # instead of best-vs-doing-nothing.
    baseline_tuples = [(s, seat, "opp_v41") for s in val_seeds for seat in (0, 1)] + \
                       [(s, seat, "opp_soil") for s in val_seeds for seat in (0, 1)]
    cache = ensure_base(baseline_tuples + trust_tuples, cache, opps, args.workers, run_dir,
                         conn=conn, batch_id="p2-rl-base-init")
    base_val_v41 = {"W": 0, "L": 0, "T": 0}
    base_val_soil = {"W": 0, "L": 0, "T": 0}
    for s in val_seeds:
        for seat in (0, 1):
            base_val_v41[cache[_cache_key(s, seat, "opp_v41")]] += 1
            base_val_soil[cache[_cache_key(s, seat, "opp_soil")]] += 1
    print(f"baseline (zero residual == raw v41) on val block {args.val_seeds}: "
          f"vs_v41(mirror)={base_val_v41} vs_soil={base_val_soil}")

    def _project_game_count():
        # Resume-safe grand total: a direct ledger count, not manually
        # accumulated (avoids double-counting cached base games across resumes).
        return conn.execute("SELECT COUNT(*) FROM games WHERE batch_id LIKE 'p2-rl-%'").fetchone()[0]

    start_iter, last_ckpt = _latest_iter(run_dir)
    theta = _load_theta(last_ckpt) if last_ckpt else np.zeros(theta_dim(), dtype=np.float32)
    print(f"resuming from iter={start_iter} ({'zero init' if last_ckpt is None else last_ckpt.name}), "
          f"theta_dim={len(theta)}, ||theta||={np.linalg.norm(theta):.4f}")

    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {
        "baseline_val_v41": base_val_v41, "baseline_val_soil": base_val_soil,
        "current_sigma": args.sigma, "best_ckpt": None, "best_iter": None, "best_val_wl_v41": None,
        "best_val_soil": None, "total_games": 0,
    }
    sigma = state.get("current_sigma", args.sigma)

    for step in range(1, args.iterations + 1):
        it = start_iter + step
        t_iter0 = time.perf_counter()

        # --- this iteration's population game batch (shared across all candidates: CRN) ---
        rng_games = np.random.RandomState(2000 + it)
        base_seed = TRAIN_SEED_BASE + (it - 1) * args.seeds_per_iter
        seeds = list(range(base_seed, base_seed + args.seeds_per_iter))
        opp_choice = ["opp_v41" if rng_games.random() >= args.weak_rate else rng_games.choice(WEAK_POOL) for _ in seeds]
        game_tuples = [(seed, seat, opp) for seed, opp in zip(seeds, opp_choice) for seat in (0, 1)]
        cache = ensure_base(game_tuples, cache, opps, args.workers, run_dir, conn=conn, batch_id=f"p2-rl-train-{it}")

        # --- sample antithetic perturbations at the CURRENT sigma ---
        rng_eps = np.random.RandomState(1000 + it)
        eps_list = [rng_eps.normal(0, 1, size=len(theta)).astype(np.float32) for _ in range(args.pairs)]
        candidates = []
        for k, eps in enumerate(eps_list):
            candidates.append((k, +1, theta + sigma * eps))
            candidates.append((k, -1, theta - sigma * eps))

        tasks, task_meta = [], []
        for ci, (k, sign, th) in enumerate(candidates):
            for (seed, seat, opp) in game_tuples:
                tasks.append((th.tolist(), opps[opp]["path"], seed, seat, 58, 256, N_ITEMS, False))
                task_meta.append((ci, seed, seat, opp))
        results = _run_games(tasks, args.workers)

        cand_rows = [[] for _ in candidates]
        opp_wl = {name: {"W": 0, "L": 0, "T": 0} for name in opps}
        train_rows = []
        for (ci, seed, seat, opp), r in zip(task_meta, results):
            if "error" in r:
                continue
            cand_rows[ci].append((seed, seat, opp, r["cand_result"]))
            opp_wl[opp][r["cand_result"]] += 1
            k, sign, th = candidates[ci]
            train_rows.append({
                "game_id": f"rl{it}-c{ci}-{seed}-{seat}", "seed": seed, "seat": seat,
                "s0": r["s0"], "s1": r["s1"], "r0": r["r0"], "r1": r["r1"], "wall_ms": r["wall_ms"],
                "sha_cand": "rl:" + theta_sha(th), "opp_sha": opps[opp]["sha8"],
            })

        l2 = np.array([np.sum(np.square(th)) for (_, _, th) in candidates])
        raw_fitness = np.array([_paired_fitness(cand_rows[i], cache) for i in range(len(candidates))]) - args.l2 * l2
        shaped = _centered_ranks(raw_fitness)

        grad = np.zeros_like(theta)
        for k in range(args.pairs):
            grad += (shaped[2 * k] - shaped[2 * k + 1]) * eps_list[k]
        grad /= max(1e-8, (2 * args.pairs * sigma))
        theta_proposed = theta + args.lr * grad
        pnorm = np.linalg.norm(theta_proposed)
        if pnorm > args.max_theta_norm:
            theta_proposed = theta_proposed * (args.max_theta_norm / pnorm)

        # --- accept/reject: proposed center must be >= old center on the fixed trust-block probe ---
        probe_tasks, probe_meta = [], []
        for label, th in (("old", theta), ("new", theta_proposed)):
            for (seed, seat, opp) in trust_tuples:
                probe_tasks.append((th.tolist(), opps[opp]["path"], seed, seat, 58, 256, N_ITEMS, label == "new"))
                probe_meta.append((label, seed, seat, opp))
        probe_results = _run_games(probe_tasks, args.workers)

        probe_rows = {"old": [], "new": []}
        turns = changed = 0
        abs_frac_sum = abs_prio_sum = 0.0
        probe_ledger_rows = []
        for (label, seed, seat, opp), r in zip(probe_meta, probe_results):
            if "error" in r:
                continue
            probe_rows[label].append((seed, seat, opp, r["cand_result"]))
            if label == "new":
                st = r["stats"]
                turns += st["turns"]; changed += st["changed"]
                abs_frac_sum += st["abs_frac_sum"]; abs_prio_sum += st["abs_prio_sum"]
            th = theta if label == "old" else theta_proposed
            probe_ledger_rows.append({
                "game_id": f"rl{it}-probe{label}-{seed}-{seat}", "seed": seed, "seat": seat,
                "s0": r["s0"], "s1": r["s1"], "r0": r["r0"], "r1": r["r1"], "wall_ms": r["wall_ms"],
                "sha_cand": "rl:" + theta_sha(th), "opp_sha": opps[opp]["sha8"],
            })
        old_score = _paired_fitness(probe_rows["old"], cache, weak_penalty=0.0)
        new_score = _paired_fitness(probe_rows["new"], cache, weak_penalty=0.0)
        accepted = new_score >= old_score

        if accepted:
            theta = theta_proposed
            sigma = args.sigma  # reset step size on acceptance
        else:
            sigma = max(args.sigma_min, sigma * 0.5)  # shrink and try again next iteration

        ckpt_path = run_dir / f"ckpt_iter{it:04d}.pt"
        save_checkpoint(theta, ckpt_path)
        ckpt_sha = file_sha(ckpt_path)

        batch_id = f"p2-rl-train-{it}"
        _record_games(batch_id, batch_id, f"{min(seeds)}-{max(seeds)}+probe{trust_seeds[0]}-{trust_seeds[-1]}",
                       train_rows + probe_ledger_rows, opps, conn)
        iter_games_logged = conn.execute("SELECT COUNT(*) FROM games WHERE batch_id=?", (batch_id,)).fetchone()[0]
        total_games = _project_game_count()

        mean_abs_frac = abs_frac_sum / (turns * N_ITEMS) if turns else 0.0
        mean_abs_prio = abs_prio_sum / (turns * N_ITEMS) if turns else 0.0
        pct_changed = 100.0 * changed / turns if turns else 0.0

        iter_wall = time.perf_counter() - t_iter0
        entry = {
            "iter": it, "games": iter_games_logged, "total_games": total_games,
            "wall_s": iter_wall, "fitness_mean": float(raw_fitness.mean()), "fitness_best": float(raw_fitness.max()),
            "wl_vs_v41_pop": opp_wl.get("opp_v41", {"W": 0, "L": 0, "T": 0}),
            "wl_vs_weak_pop": {n: opp_wl[n] for n in WEAK_POOL if opp_wl[n]["W"] + opp_wl[n]["L"] + opp_wl[n]["T"] > 0},
            "probe_old_score": old_score, "probe_new_score": new_score, "accepted": accepted,
            "sigma": sigma, "mean_abs_delta_frac": mean_abs_frac, "mean_abs_delta_prio": mean_abs_prio,
            "pct_turns_changed": pct_changed, "theta_norm": float(np.linalg.norm(theta)),
            "ckpt": ckpt_path.name, "ckpt_sha16": ckpt_sha,
        }
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"iter {it}: games={entry['games']} fitness_mean={entry['fitness_mean']:.2f} "
              f"wl_v41(pop)={entry['wl_vs_v41_pop']} probe old={old_score:.1f} new={new_score:.1f} "
              f"{'ACCEPT' if accepted else 'reject'} sigma={sigma:.5f} "
              f"|dfrac|={mean_abs_frac:.4f} |dprio|={mean_abs_prio:.4f} chg%={pct_changed:.1f} "
              f"||theta||={entry['theta_norm']:.4f} wall={iter_wall:.1f}s")

        if args.val_every > 0 and it % args.val_every == 0:
            val_result = validate(theta, val_seeds, opps, ckpt_sha, args.workers, conn, it, cache, run_dir)
            entry["validation"] = val_result
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps({"iter": it, "validation": val_result, "baseline_vs_v41": base_val_v41,
                                     "baseline_vs_soil": base_val_soil}) + "\n")
            print(f"  VALIDATION iter {it}: vs_v41={val_result['vs_v41']} (baseline {base_val_v41}) "
                  f"vs_soil={val_result['vs_soil']} (baseline {base_val_soil})")
            score = val_result["vs_v41"]["W"] - val_result["vs_v41"]["L"]
            base_score = base_val_v41["W"] - base_val_v41["L"]
            soil_ok = val_result["vs_soil"]["L"] == 0 and val_result["vs_soil"]["W"] == base_val_soil["W"]
            beats_baseline = score > base_score
            if soil_ok and beats_baseline:
                cur_best = state.get("best_val_wl_v41")
                if cur_best is None or score > cur_best:
                    state.update({
                        "best_iter": it, "best_val_wl_v41": score, "best_val_soil": val_result["vs_soil"],
                        "best_ckpt": str(ckpt_path), "best_val_detail": val_result,
                    })
            total_games = _project_game_count()

        state["current_sigma"] = sigma
        state["last_iter"] = it
        state["total_games"] = total_games
        state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")

    total_games = _project_game_count()
    conn.close()
    print(f"\ndone: ran {args.iterations} iteration(s), total_games={total_games}, last_iter={start_iter + args.iterations}")
    print(f"baseline: vs_v41={base_val_v41} vs_soil={base_val_soil}")
    print(f"state: {json.dumps(state, indent=2)}")


def validate(theta, val_seeds, opps, ckpt_sha, workers, conn, it, cache, run_dir):
    """40+40 games (both seats) vs opp_v41 and opp_soil on a fixed validation
    block. Base (zero-residual) results on this exact block are already
    cached from run() startup, so only the candidate's own games are played."""
    tasks, meta = [], []
    for opp_name in ("opp_v41", "opp_soil"):
        for seed in val_seeds:
            for seat in (0, 1):
                tasks.append((theta.tolist(), opps[opp_name]["path"], seed, seat, 58, 256, N_ITEMS, False))
                meta.append((opp_name, seed, seat))
    results = _run_games(tasks, workers)
    wl = {"opp_v41": {"W": 0, "L": 0, "T": 0}, "opp_soil": {"W": 0, "L": 0, "T": 0}}
    rows = []
    for (opp_name, seed, seat), r in zip(meta, results):
        if "error" in r:
            continue
        wl[opp_name][r["cand_result"]] += 1
        rows.append({
            "game_id": f"rlval{it}-{opp_name}-{seed}-{seat}", "seed": seed, "seat": seat,
            "s0": r["s0"], "s1": r["s1"], "r0": r["r0"], "r1": r["r1"], "wall_ms": r["wall_ms"],
            "sha_cand": "rl:" + ckpt_sha, "opp_sha": opps[opp_name]["sha8"],
        })
    batch_id = f"p2-rl-val-{it}"
    _record_games(batch_id, batch_id, f"{min(val_seeds)}-{max(val_seeds)}", rows, opps, conn)
    return {"vs_v41": wl["opp_v41"], "vs_soil": wl["opp_soil"], "batch_id": batch_id}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", default=str(DEFAULT_RUN_DIR))
    ap.add_argument("--iterations", type=int, default=10, help="NEW iterations to run this invocation")
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--pairs", type=int, default=4, help="antithetic pairs per iteration (2x candidates)")
    ap.add_argument("--seeds-per-iter", type=int, default=2, help="seeds per candidate eval (x2 seats)")
    ap.add_argument("--trust-block-seeds", type=int, default=2, help="seeds in the fixed accept/reject probe (x2 seats)")
    ap.add_argument("--sigma", type=float, default=0.003)
    ap.add_argument("--sigma-min", type=float, default=0.0003)
    ap.add_argument("--lr", type=float, default=0.002)
    ap.add_argument("--l2", type=float, default=5.0)
    ap.add_argument("--max-theta-norm", type=float, default=0.3,
                     help="hard cap on ||theta|| after each update -- the KL/L2 drift guardrail")
    ap.add_argument("--weak-rate", type=float, default=0.2)
    ap.add_argument("--val-every", type=int, default=6)
    ap.add_argument("--val-seeds", default="620000-620019")
    args = ap.parse_args()
    run(args)


if __name__ == "__main__":
    main()
