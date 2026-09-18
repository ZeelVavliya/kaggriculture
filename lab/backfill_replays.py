"""One-off: back-fill the loose pre-lab replay JSONs into the ledger so that
history is not lost. These replays predate the artifact/SHA bookkeeping, so
we don't know which exact agent source produced them -- sha is recorded as
"unknown" and a note explains why."""
import argparse
import json
import shutil
import uuid
from pathlib import Path

from lab import ledger

LAB = Path(__file__).resolve().parent
ROOT = LAB.parent
REPLAYS_DIR = LAB / "replays"
BACKFILL_BATCH = "backfill-loose-replays"

# (path, note) -- top-level combined replay only; the split -0/-1 files are
# duplicates of the same episode from each agent's own perspective and are
# not re-ingested as separate games.
LOOSE_REPLAYS = [
    (ROOT / "90643183.json", "pre-lab main.py replay; source agent unrecorded"),
    (ROOT / "strat2" / "Strat2_logs" / "95237733.json", "pre-lab main2.py replay; source agent unrecorded"),
]


def backfill():
    conn = ledger.connect()
    ledger.add_batch(BACKFILL_BATCH, "back-filled loose pre-lab replays", "unknown", {}, conn=conn)
    for src, note in LOOSE_REPLAYS:
        if not src.exists():
            print(f"SKIP (not found): {src}")
            continue
        d = json.loads(src.read_text(encoding="utf-8"))
        rewards = d.get("rewards") or [None, None]
        statuses = d.get("statuses") or [None, None]
        seed = (d.get("info") or {}).get("seed")
        episode_id = (d.get("info") or {}).get("EpisodeId", src.stem)

        dest_dir = REPLAYS_DIR / BACKFILL_BATCH
        dest_dir.mkdir(parents=True, exist_ok=True)
        game_id = f"backfill-{episode_id}"
        dest = dest_dir / f"{game_id}.json"
        shutil.copy2(src, dest)

        r0, r1 = rewards[0], rewards[1]
        margin = (r0 - r1) if (r0 is not None and r1 is not None) else None
        result = None
        if margin is not None:
            result = "W" if margin > 0 else ("L" if margin < 0 else "T")

        ledger.add_game({
            "game_id": game_id, "batch_id": BACKFILL_BATCH,
            "sha_p0": "unknown", "sha_p1": "unknown", "seed": seed if seed is not None else -1,
            "steps": len(d.get("steps", [])),
            "reward_p0": r0, "reward_p1": r1,
            "status_p0": statuses[0], "status_p1": statuses[1],
            "result": result, "margin": margin, "wall_ms": None,
            "replay_path": str(dest),
        }, conn=conn)
        print(f"backfilled {src.name}: episode={episode_id} seed={seed} rewards={rewards} note={note!r}")
    conn.close()


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    backfill()
