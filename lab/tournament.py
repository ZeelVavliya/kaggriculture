"""Thin CLI alias: `python -m lab.tournament --artifacts all --seed-block <block>`
is the Phase 1 exit-criterion command named in the plan; the actual round-robin
implementation lives in lab.arena.tournament (shared with `lab.arena tournament`)."""
import argparse
from pathlib import Path

from lab import arena, ledger, rate, report


def resolve(name_or_path):
    if Path(name_or_path).exists():
        return name_or_path
    row = ledger.get_artifact_by_name(name_or_path)
    if row is None:
        raise SystemExit(f"not a path and not a registered artifact name: {name_or_path}")
    return ledger.artifact_path(row)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--artifacts", required=True, help="comma-separated artifact names, or 'all'")
    p.add_argument("--seed-block", required=True)
    p.add_argument("--workers", type=int, default=None)
    args = p.parse_args()

    if args.artifacts == "all":
        names = ["main", "main2", "c92", "c94", "c95"]
    else:
        names = args.artifacts.split(",")
    paths = [resolve(n) for n in names]

    batch_id, results = arena.tournament(paths, args.seed_block, workers=args.workers)
    rate.print_table(rate.compute_batch_ratings(batch_id))
    out = report.write_report(batch_id)
    print(f"\nreport written to {out}")


if __name__ == "__main__":
    main()
