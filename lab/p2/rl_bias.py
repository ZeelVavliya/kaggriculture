"""RL run 2: paired coordinate search over the residual policy's 14 head BIASES only
(per item: constant delta to sell fraction, constant delta to slot priority), weights
held at zero. Run 1 (full 3598-dim ES) diverged: noise-following updates, validation
14-26 vs v41 and 27-13 vs soil. This run is deliberately tiny and conservative.

- Base = zero residual (exactly v41). Base outcomes per (seed, seat, opp) are played once.
- A probe moves one coordinate by +/-step inside a trust region; its fitness is paired:
  sum over games of (result(probe) - result(base)), W=+1 L=-1 T=0.
- A move is accepted only if fitness >= MIN_GAIN; otherwise the center stays.
- Validation compares the final center against the base on held-out seeds.

ponytail: coordinate search, not ES/PPO. 14 knobs is enough to test "does any small
sell-timing shift beat v41"; widen to state-dependent weights only if this finds signal.
"""
import argparse, json, time
from pathlib import Path
import numpy as np
from lab import ledger
from lab.p2 import rl
from lab.p2.market_env import FREE_ITEMS

H, N = 256, len(FREE_ITEMS)
FB = slice(N * H, N * H + N)                       # frac_head.bias
PB = slice(2 * N * H + N, 2 * N * H + 2 * N)       # prio_head.bias
SCORE = {"W": 1, "L": -1, "T": 0}
OUT = Path(__file__).resolve().parent / "data" / "rl_bias"


def theta_from(bias):
    th = np.zeros(rl.theta_dim(), dtype=np.float32)
    th[FB] = bias[:N]; th[PB] = bias[N:]
    return th


def play(bias, games, opps, workers):
    tasks = [(theta_from(bias).tolist(), opps[o]["path"], s, seat, 58, H, N, False) for s, seat, o in games]
    res = rl._run_games(tasks, workers)
    return [r.get("cand_result", "T") if "error" not in r else "L" for r in res], res


def record(batch, games, res, cand_sha, opps, conn, label):
    rows = []
    for (s, seat, o), r in zip(games, res):
        if "error" in r:
            continue
        rows.append(dict(r, game_id=f"{batch}-{o}-{s}-{seat}", seat=seat, opp_sha=opps[o]["sha8"], sha_cand=cand_sha))
    rl._record_games(batch, label, f"{games[0][0]}-{games[-1][0]}", rows, opps, conn)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--train-seeds", default="630000-630005")
    ap.add_argument("--val-seeds", default="620000-620019")
    ap.add_argument("--frac-step", type=float, default=0.05)
    ap.add_argument("--prio-step", type=float, default=0.10)
    ap.add_argument("--frac-cap", type=float, default=0.10)
    ap.add_argument("--prio-cap", type=float, default=0.20)
    ap.add_argument("--min-gain", type=int, default=2)
    ap.add_argument("--sweeps", type=int, default=1)
    ap.add_argument("--workers", type=int, default=10)
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    opps = rl._resolve_opponents(["opp_v41", "opp_soil"])
    lo, hi = map(int, a.train_seeds.split("-"))
    train = [(s, seat, "opp_v41") for s in range(lo, hi + 1) for seat in (0, 1)] + [(lo, 0, "opp_soil"), (lo, 1, "opp_soil")]
    conn = ledger.connect()
    t0 = time.perf_counter()

    zero = np.zeros(2 * N, dtype=np.float32)
    base, bres = play(zero, train, opps, a.workers)
    record("p2-rlb-train-base", train, bres, "rl:zero", opps, conn, "p2-rlb train base (zero residual)")
    print("base train results:", dict(zip(*np.unique(base, return_counts=True))), flush=True)

    center = zero.copy(); log = []
    steps = [a.frac_step] * N + [a.prio_step] * N
    caps = [a.frac_cap] * N + [a.prio_cap] * N
    names = [f"frac:{i}" for i in FREE_ITEMS] + [f"prio:{i}" for i in FREE_ITEMS]
    for sweep in range(a.sweeps):
        for k in range(2 * N):
            for sign in (+1, -1):
                probe = center.copy()
                probe[k] = float(np.clip(probe[k] + sign * steps[k], -caps[k], caps[k]))
                if probe[k] == center[k]:
                    continue
                r, res = play(probe, train, opps, a.workers)
                gain = sum(SCORE[x] - SCORE[y] for x, y in zip(r, base))
                tag = f"{names[k]}{'+' if sign > 0 else '-'}"
                record(f"p2-rlb-train-s{sweep}-{tag}", train, res, f"rl:{tag}", opps, conn, f"p2-rlb probe {tag}")
                accepted = gain >= a.min_gain
                entry = dict(sweep=sweep, coord=names[k], sign=sign, value=float(probe[k]), gain=gain, accepted=accepted,
                             wall_s=round(time.perf_counter() - t0))
                log.append(entry); print(json.dumps(entry), flush=True)
                if accepted:
                    center, base = probe, r   # new center; its own results become the paired base
                    break
            (OUT / "log.jsonl").write_text("\n".join(json.dumps(e) for e in log), encoding="utf-8")
            (OUT / "center.json").write_text(json.dumps(dict(zip(names, map(float, center)))), encoding="utf-8")

    vlo, vhi = map(int, a.val_seeds.split("-"))
    val = [(s, seat, o) for o in ("opp_v41", "opp_soil") for s in range(vlo, vhi + 1) for seat in (0, 1)]
    summary = {}
    for label, vec in (("zero", zero), ("center", center)):
        if label == "center" and not center.any():
            summary["center"] = "identical to zero (no accepted move)"; break
        r, res = play(vec, val, opps, a.workers)
        record(f"p2-rlb-val-{label}", val, res, f"rl:{label}", opps, conn, f"p2-rlb validation {label}")
        summary[label] = {o: dict(zip(*np.unique([x for x, g in zip(r, val) if g[2] == o], return_counts=True))) for o in ("opp_v41", "opp_soil")}
    summary = json.loads(json.dumps(summary, default=int))
    summary["center_bias"] = dict(zip(names, map(float, center)))
    summary["wall_s"] = round(time.perf_counter() - t0)
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print("SUMMARY", json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
