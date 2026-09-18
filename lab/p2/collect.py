"""Roll the identity market_env wrapper (policy=None, so field ops + market
orders are byte-identical to raw v41) against a fixed opponent pool, logging
(features, base sell-fraction targets, base slot-priority targets) at every
turn where v41 has sellable free-item inventory or proposes a free-item
sell. This is the BC training set: "what would v41 itself have sold".

Usage: python -m lab.p2.collect --games 100 --seed0 700000 --workers 8
"""
import argparse
import io
import json
import time
from contextlib import redirect_stdout
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np

from lab import ledger
from lab.p2.market_env import make_agent, FREE_ITEMS

LAB = Path(__file__).resolve().parent.parent
DATA_DIR = Path(__file__).resolve().parent / "data"

POOL_NAMES = ["opp_soil", "opp_salem2900", "c94", "c95", "opp_v41"]


def _resolve_pool():
    pool = {}
    for name in POOL_NAMES:
        row = ledger.get_artifact_by_name(name)
        if row is None:
            raise SystemExit(f"artifact not registered: {name}")
        pool[name] = row["path"]
    return pool


def _play_and_log(opp_name, opp_path, seed, seat, steps):
    """seat: 0 -> wrapper is player0, 1 -> wrapper is player1. Runs in a
    worker process; loads v41 fresh via make_agent (isolated namespace)."""
    import kaggle_environments as ke  # imported in worker to avoid pickling issues

    log = []
    wrapped = make_agent(None, log=log)
    agents = [wrapped, opp_path] if seat == 0 else [opp_path, wrapped]

    buf = io.StringIO()
    t0 = time.perf_counter()
    with redirect_stdout(buf):
        env = ke.make("kaggriculture", configuration={"episodeSteps": steps, "seed": seed}, debug=False)
        env.run(agents)
        last = env.steps[-1]
    wall_s = time.perf_counter() - t0

    game_id = f"{opp_name}-seed{seed}-seat{seat}"
    rows = [(f.tolist(), fr.tolist(), pr.tolist()) for (f, fr, pr) in log]
    return {
        "game_id": game_id, "opponent": opp_name, "seed": seed, "seat": seat,
        "status": [last[0].status, last[1].status],
        "reward": [last[0].reward, last[1].reward],
        "wall_s": wall_s, "n_rows": len(rows), "rows": rows,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=100, help="total games; split evenly across the 5-opponent pool")
    ap.add_argument("--seed0", type=int, default=700000)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--steps", type=int, default=720)
    ap.add_argument("--out", default=str(DATA_DIR / "bc_data.npz"))
    args = ap.parse_args()

    pool = _resolve_pool()
    seeds_per_opp = max(1, args.games // (2 * len(pool)))  # x2 for both seats
    seeds = list(range(args.seed0, args.seed0 + seeds_per_opp))

    jobs = []
    for name, path in pool.items():
        for s in seeds:
            for seat in (0, 1):
                jobs.append((name, path, s, seat))

    print(f"pool={list(pool)} seeds_per_opp={seeds_per_opp} total_games={len(jobs)}")

    all_feats, all_frac, all_prio, game_ids, meta_games = [], [], [], [], []
    t0 = time.perf_counter()
    errors = 0
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(_play_and_log, n, p, s, seat, args.steps): (n, s, seat) for (n, p, s, seat) in jobs}
        for fut in as_completed(futs):
            name, s, seat = futs[fut]
            try:
                res = fut.result()
            except Exception as exc:
                errors += 1
                print(f"ERROR {name} seed={s} seat={seat}: {exc!r}")
                continue
            for (f, fr, pr) in res["rows"]:
                all_feats.append(f)
                all_frac.append(fr)
                all_prio.append(pr)
                game_ids.append(res["game_id"])
            meta_games.append({k: res[k] for k in ("game_id", "opponent", "seed", "seat", "status", "reward", "wall_s", "n_rows")})
            print(f"done {res['game_id']}: rows={res['n_rows']} reward={res['reward']} wall_s={res['wall_s']:.1f}")

    total_wall = time.perf_counter() - t0
    n_games = len(meta_games)
    n_rows = len(all_feats)
    print(f"\n{n_games} games ({errors} errors), {n_rows} rows, {total_wall:.1f}s total, "
          f"{total_wall / max(1, n_games):.2f}s/game")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.out,
        features=np.asarray(all_feats, dtype=np.float32),
        frac_targets=np.asarray(all_frac, dtype=np.float32),
        prio_targets=np.asarray(all_prio, dtype=np.float32),
        game_ids=np.asarray(game_ids),
    )
    manifest = {
        "artifact_shas": {n: ledger.get_artifact_by_name(n)["sha256"] for n in pool},
        "opponents": list(pool),
        "seed0": args.seed0, "seeds_per_opponent": seeds_per_opp,
        "steps": args.steps, "n_games": n_games, "n_rows": n_rows, "errors": errors,
        "wall_s_total": total_wall, "wall_s_per_game": total_wall / max(1, n_games),
        "free_items": list(FREE_ITEMS), "games": meta_games,
    }
    manifest_path = Path(args.out).with_suffix(".manifest.json")
    manifest_path.write_text(json.dumps(manifest, indent=2, default=str), encoding="utf-8")
    print(f"saved {args.out} and {manifest_path}")


if __name__ == "__main__":
    main()
