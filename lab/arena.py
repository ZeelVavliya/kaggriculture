"""Reproducible play: run_pair / h2h / tournament, thin over kaggle_environments.make.

Both seats always played in h2h/tournament (the market is shared and not seat-symmetric).
Games are sharded across processes by seed; sqlite writes happen only in the parent process
(worker returns a plain dict, parent inserts the ledger row) so WAL contention is avoided.
"""
import argparse
import io
import time
import uuid
from contextlib import redirect_stdout
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from lab import ledger

LAB = Path(__file__).resolve().parent
ROOT = LAB.parent
REPLAYS_DIR = LAB / "replays"

# Named, re-runnable seed blocks (kernel's convention).
SEED_BLOCKS = {
    "850000-850009": list(range(850000, 850010)),
    "850000-850004": list(range(850000, 850005)),
    "860000-860004": list(range(860000, 860005)),
    "900000-900019": list(range(900000, 900020)),
}


def parse_seed_block(spec: str):
    if spec in SEED_BLOCKS:
        return SEED_BLOCKS[spec]
    lo, hi = spec.split("-")
    return list(range(int(lo), int(hi) + 1))


def _play_one(path_p0: str, path_p1: str, seed: int, steps: int, batch_id: str, replay_dir: str):
    """Runs in a worker process. No sqlite access here. Loads agents fresh
    (by file path, per game/process) so module-global state (e.g. C95's
    _LAST_STEP / _CLONE_CONFIDENCE) can never leak between games."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        import kaggle_environments as ke
        env = ke.make("kaggriculture", configuration={"episodeSteps": steps, "seed": seed}, debug=False)
        t0 = time.perf_counter()
        env.run([path_p0, path_p1])
        wall_ms = (time.perf_counter() - t0) * 1000
        last = env.steps[-1]
        replay_json = env.toJSON()

    game_id = uuid.uuid4().hex[:16]
    # gzip: raw replays are ~10 MB each and filled the disk at ~2,700 games (compresses ~60x).
    import gzip, json
    replay_path = str(Path(replay_dir) / f"{game_id}.json.gz")
    Path(replay_path).parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(replay_path, "wt", encoding="utf-8", compresslevel=6) as fh:
        json.dump(replay_json, fh)

    r0, r1 = last[0].reward, last[1].reward
    result, margin = score(last[0].status, last[1].status, r0, r1)

    return {
        "game_id": game_id, "batch_id": batch_id,
        "path_p0": path_p0, "path_p1": path_p1, "seed": seed, "steps": steps,
        "reward_p0": r0, "reward_p1": r1,
        "status_p0": last[0].status, "status_p1": last[1].status,
        "result": result, "margin": margin, "wall_ms": wall_ms,
        "replay_path": replay_path,
    }


def score(status_p0, status_p1, r0, r1):
    """(result from p0's view, margin). A side that did not finish DONE loses, even if
    its reward happens to be larger -- an erroring agent must never count as a tie."""
    ok0, ok1 = status_p0 == "DONE" and r0 is not None, status_p1 == "DONE" and r1 is not None
    if ok0 != ok1:
        return ("W" if ok0 else "L"), 0.0
    if not ok0:
        return "T", 0.0
    margin = r0 - r1
    return ("W" if r0 > r1 else "L" if r0 < r1 else "T"), margin


def _error_row(path_p0, path_p1, seed, steps, batch_id, exc):
    return {"game_id": uuid.uuid4().hex[:16], "batch_id": batch_id, "path_p0": path_p0, "path_p1": path_p1,
            "seed": seed, "steps": steps, "reward_p0": None, "reward_p1": None,
            "status_p0": "HARNESS_ERROR", "status_p1": "HARNESS_ERROR", "result": "T", "margin": 0.0,
            "wall_ms": None, "replay_path": None, "error": repr(exc)}


def _sha_for_path(path: str, conn) -> str:
    import hashlib
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run_pair(a: str, b: str, seed: int, steps: int = 720, batch_id: str = None, conn=None):
    own = conn is None
    conn = conn or ledger.connect()
    batch_id = batch_id or f"pair-{uuid.uuid4().hex[:8]}"
    row = _play_one(a, b, seed, steps, batch_id, str(REPLAYS_DIR / batch_id))
    _finalize_and_store([row], conn)
    if own:
        conn.close()
    return row


def _finalize_and_store(raw_rows, conn):
    """Parent-process only: resolve sha256 for each path and write games rows."""
    for r in raw_rows:
        sha_p0 = _sha_for_path(r["path_p0"], conn)
        sha_p1 = _sha_for_path(r["path_p1"], conn)
        ledger.add_game({
            "game_id": r["game_id"], "batch_id": r["batch_id"],
            "sha_p0": sha_p0, "sha_p1": sha_p1, "seed": r["seed"], "steps": r["steps"],
            "reward_p0": r["reward_p0"], "reward_p1": r["reward_p1"],
            "status_p0": r["status_p0"], "status_p1": r["status_p1"],
            "result": r["result"], "margin": r["margin"], "wall_ms": r["wall_ms"],
            "replay_path": r["replay_path"],
        }, conn=conn)


def _run_many(pairs, batch_id: str, label: str, seed_block_spec: str, workers: int):
    """pairs: list of (path_p0, path_p1, seed) with both seats already expanded."""
    conn = ledger.connect()
    ledger.add_batch(batch_id, label, seed_block_spec, {"pairs": len(pairs)}, conn=conn)
    replay_dir = str(REPLAYS_DIR / batch_id)
    results = []
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(_play_one, p0, p1, seed, 720, batch_id, replay_dir): (p0, p1, seed) for (p0, p1, seed) in pairs}
        for fut in as_completed(futs):
            try:
                row = fut.result()
            except Exception as exc:  # harness crash: record it, don't lose the rest of the batch
                p0, p1, seed = futs[fut]
                row = _error_row(p0, p1, seed, 720, batch_id, exc)
                print(f"HARNESS_ERROR seed={seed}: {exc!r}")
            _finalize_and_store([row], conn)  # stored as each game lands, so a killed run keeps its games
            results.append(row)
    conn.close()
    return results


def h2h(a: str, b: str, seed_block: str, both_seats: bool = True, workers: int = None, label: str = None):
    seeds = parse_seed_block(seed_block)
    pairs = []
    for s in seeds:
        pairs.append((a, b, s))
        if both_seats:
            pairs.append((b, a, s))
    batch_id = f"h2h-{_label(a)}-vs-{_label(b)}-{uuid.uuid4().hex[:6]}"
    results = _run_many(pairs, batch_id, label or f"h2h {a} vs {b}", seed_block, workers)
    _print_h2h_summary(a, b, results)
    return batch_id, results


def _label(path: str) -> str:
    p = Path(path)
    # lab/artifacts/<sha8>/main.py -> <sha8>; otherwise the stem
    return p.parent.name if p.stem == "main" and p.parent.name else p.stem


def _print_h2h_summary(a, b, results):
    a_name, b_name = _label(a), _label(b)
    wl = {"as_p0": [0, 0, 0], "as_p1": [0, 0, 0]}  # W,L,T
    for r in results:
        seat = "as_p0" if r["path_p0"] == a else "as_p1"
        res = r["result"] if seat == "as_p0" else {"W": "L", "L": "W", "T": "T"}[r["result"]]  # result is p0's view
        idx = {"W": 0, "L": 1, "T": 2}[res]
        wl[seat][idx] += 1
    print(f"{len(results)} games logged.")
    print(f"{a_name} as p0: W{wl['as_p0'][0]}-L{wl['as_p0'][1]}-T{wl['as_p0'][2]}")
    print(f"{a_name} as p1: W{wl['as_p1'][0]}-L{wl['as_p1'][1]}-T{wl['as_p1'][2]}")


def tournament(artifacts: list, seed_block: str, workers: int = None, label: str = None):
    seeds = parse_seed_block(seed_block)
    pairs = []
    for i, a in enumerate(artifacts):
        for b in artifacts[i + 1:]:
            for s in seeds:
                pairs.append((a, b, s))
                pairs.append((b, a, s))
    batch_id = f"tourney-{uuid.uuid4().hex[:8]}"
    results = _run_many(pairs, batch_id, label or "tournament", seed_block, workers)
    print(f"{len(results)} games logged under batch {batch_id}")
    return batch_id, results


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    ph = sub.add_parser("h2h")
    ph.add_argument("--a", required=True)
    ph.add_argument("--b", required=True)
    ph.add_argument("--seed-block", required=True)
    ph.add_argument("--workers", type=int, default=None)

    pt = sub.add_parser("tournament")
    pt.add_argument("--artifacts", required=True, help="comma-separated paths, or 'all'")
    pt.add_argument("--seed-block", required=True)
    pt.add_argument("--workers", type=int, default=None)

    args = p.parse_args()

    def resolve(name_or_path):
        if Path(name_or_path).exists():
            return name_or_path
        row = ledger.get_artifact_by_name(name_or_path)
        if row is None:
            raise SystemExit(f"not a path and not a registered artifact name: {name_or_path}")
        return row["path"]

    if args.cmd == "h2h":
        h2h(resolve(args.a), resolve(args.b), args.seed_block, workers=args.workers)
    elif args.cmd == "tournament":
        if args.artifacts == "all":
            names = ["main", "main2", "c92", "c94", "c95"]
            paths = [resolve(n) for n in names]
        else:
            paths = [resolve(x) for x in args.artifacts.split(",")]
        tournament(paths, args.seed_block, workers=args.workers)


if __name__ == "__main__":
    main()
