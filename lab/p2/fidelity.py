"""Step 5 fidelity check: wrap a trained BC checkpoint with market_env.make_agent
and play it vs raw v41 and vs opp_soil. Success = within a few hundred coins of
v41 vs v41-mirror margins, and roughly v41's own record vs soil (20-0).

Games are recorded into lab/runs.db under batch_id "p2-bc-fidelity-<hex>" (the
BC policy has no file on disk, so sha_p0/sha_p1 for it is a synthetic marker
"bc:<checkpoint-sha256-prefix>" rather than a real artifact hash).

Usage: python -m lab.p2.fidelity --checkpoint lab/p2/data/bc_model.pt --seeds 880000-880009
"""
import argparse
import hashlib
import io
import time
import uuid
from contextlib import redirect_stdout
from pathlib import Path

import torch

from lab import ledger
from lab.arena import score as _p0_score
from lab.p2.bc import MarketMLP
from lab.p2.market_env import make_agent


def load_policy(checkpoint_path):
    ckpt = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    model = MarketMLP(ckpt["in_dim"], hidden=ckpt["hidden"])
    model.load_state_dict(ckpt["state_dict"])
    return model.as_policy()


def _run_one(agents, seed, steps=720):
    import kaggle_environments as ke
    buf = io.StringIO()
    with redirect_stdout(buf):
        env = ke.make("kaggriculture", configuration={"episodeSteps": steps, "seed": seed}, debug=False)
        env.run(agents)
        last = env.steps[-1]
    return last[0].reward, last[1].reward, last[0].status, last[1].status


def run_fidelity(checkpoint_path, seeds, opponents, batch_label="p2-bc-fidelity"):
    policy = load_policy(checkpoint_path)
    bc_marker = "bc:" + hashlib.sha256(Path(checkpoint_path).read_bytes()).hexdigest()[:16]
    batch_id = f"{batch_label}-{uuid.uuid4().hex[:8]}"
    conn = ledger.connect()
    ledger.add_batch(batch_id, batch_label, f"{min(seeds)}-{max(seeds)}", {"opponents": opponents}, conn=conn)

    results = {}
    for opp_name in opponents:
        opp_path = ledger.get_artifact_by_name(opp_name)["path"]
        opp_sha = hashlib.sha256(Path(opp_path).read_bytes()).hexdigest()
        rows = []
        for seed in seeds:
            for seat, (p0, p1, sha0, sha1) in enumerate([
                (make_agent(policy), opp_path, bc_marker, opp_sha),
                (opp_path, make_agent(policy), opp_sha, bc_marker),
            ]):
                t0 = time.perf_counter()
                r0, r1, s0, s1 = _run_one([p0, p1], seed)
                wall_ms = (time.perf_counter() - t0) * 1000
                bc_reward = r0 if seat == 0 else r1
                opp_reward = r1 if seat == 0 else r0
                bc_margin = (bc_reward - opp_reward) if bc_reward is not None and opp_reward is not None else None
                game_id = uuid.uuid4().hex[:16]
                # ledger convention (lab.arena.score): result/margin are always from
                # p0's view, regardless of which side is the BC agent this game.
                p0_result, p0_margin = _p0_score(s0, s1, r0, r1)
                ledger.add_game({
                    "game_id": game_id, "batch_id": batch_id, "sha_p0": sha0, "sha_p1": sha1,
                    "seed": seed, "steps": 720, "reward_p0": r0, "reward_p1": r1,
                    "status_p0": s0, "status_p1": s1,
                    "result": p0_result, "margin": p0_margin, "wall_ms": wall_ms, "replay_path": None,
                }, conn=conn)
                rows.append((seed, seat, bc_reward, opp_reward, bc_margin, s0, s1))
                print(f"{opp_name} seed={seed} seat_bc={seat} bc={bc_reward} opp={opp_reward} margin={bc_margin}")
        results[opp_name] = rows
    conn.close()

    print(f"\nbatch_id={batch_id}")
    for opp_name, rows in results.items():
        wins = sum(1 for r in rows if r[5] == "DONE" and r[6] == "DONE" and r[2] > r[3])
        losses = sum(1 for r in rows if r[5] == "DONE" and r[6] == "DONE" and r[2] < r[3])
        margins = [r[4] for r in rows if r[4] is not None]
        mean_margin = sum(margins) / len(margins) if margins else float("nan")
        print(f"  vs {opp_name}: {wins}-{losses} ({len(rows)} games), mean margin {mean_margin:+.0f}")
    return batch_id, results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--seeds", default="880000-880009")
    ap.add_argument("--opponents", default="opp_v41,opp_soil")
    args = ap.parse_args()
    lo, hi = args.seeds.split("-")
    seeds = list(range(int(lo), int(hi) + 1))
    run_fidelity(args.checkpoint, seeds, args.opponents.split(","))


if __name__ == "__main__":
    main()
