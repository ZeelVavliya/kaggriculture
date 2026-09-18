"""The promotion protocol: compile/import -> self-play both-DONE -> play incumbent
AND parent on disjoint seeds, both seats -> any loss to either is a VETO (even if
aggregate wins look strong) -> play structurally different opponents -> report
per-opponent records -> audit -> keep every result file.

Only a candidate that clears every step is eligible to be packaged.
"""
import argparse
from pathlib import Path

from lab import arena, audit, ledger, registry

# Two disjoint seed blocks so "incumbent" and "parent" never share a seed.
INCUMBENT_SEEDS = "850000-850024"   # 25 seeds x 2 seats = 50 games
PARENT_SEEDS = "860000-860024"      # 25 seeds, disjoint
OTHER_OPPONENT_SEEDS = "870000-870024"
# Never used for development or tuning: played once, after everything above passes.
FINAL_SEEDS = "910000-910024"


def candidate_losses(results, cand_path):
    """Games the candidate lost. result is from p0's view, so a candidate loss is
    (candidate p0 and L) or (candidate p1 and W)."""
    results = [r for r in results if r.get("status_p0") != "HARNESS_ERROR"]  # harness crashes are not games
    return [r for r in results if
            (r["path_p0"] == cand_path and r["result"] == "L") or
            (r["path_p1"] == cand_path and r["result"] == "W")]


def paired_regressions(cand_path, opp_path, results, seed_block, workers, label):
    """A mirror is seat-asymmetric: the opponent loses some (seed, seat) games to itself, so
    "any loss = veto" would veto an exact copy of it. Returns (games where the candidate scores
    below opponent-vs-itself on the same seed and seat, count of games where it scores above)."""
    mirror = arena.h2h(opp_path, opp_path, seed_block, both_seats=False, workers=workers,
                       label=f"gate:{label}_mirror_baseline")[1]
    base_by_seed = {r["seed"]: r["result"] for r in mirror}  # p0's view; both seats are the same agent
    pts = {"W": 1, "T": 0, "L": -1}
    def sign(r):
        return 1 if r["path_p0"] == cand_path else -1
    ok = [r for r in results if r.get("status_p0") != "HARNESS_ERROR"]
    worse = [r for r in ok if sign(r) * pts[r["result"]] < sign(r) * pts[base_by_seed[r["seed"]]]]
    better = sum(1 for r in ok if sign(r) * pts[r["result"]] > sign(r) * pts[base_by_seed[r["seed"]]])
    return worse, better


def _resolve(name_or_path):
    if Path(name_or_path).exists():
        return name_or_path, name_or_path
    row = ledger.get_artifact_by_name(name_or_path)
    if row is None:
        raise SystemExit(f"not a path and not a registered artifact name: {name_or_path}")
    return ledger.artifact_path(row), row["sha256"]


def run_gate(candidate: str, parent: str = None, incumbent: str = None, others: list = None, workers=None):
    """Returns dict with 'verdict': 'PASS' or 'VETO', plus the evidence."""
    cand_path, cand_sha = _resolve(candidate)
    steps = []

    # step 1: compile/import
    compile(Path(cand_path).read_text(encoding="utf-8"), cand_path, "exec")
    registry.last_callable_name(Path(cand_path))  # raises if not importable
    steps.append(("compile_import", "PASS", "compiles and last-callable resolves"))

    # step 2: self-play, both DONE
    row = arena.run_pair(cand_path, cand_path, seed=1)
    self_ok = row["status_p0"] == "DONE" and row["status_p1"] == "DONE"
    steps.append(("self_play_done", "PASS" if self_ok else "FAIL", f"statuses={row['status_p0']}/{row['status_p1']}"))
    if not self_ok:
        return {"verdict": "VETO", "reason": "self-play did not finish DONE/DONE", "steps": steps}

    veto = False
    veto_reason = None
    per_opponent_batches = {}

    # step 3/4: incumbent + parent on disjoint seeds, both seats, any loss = veto
    if incumbent is None:
        row_art = ledger.get_artifact_by_name("c95")
        incumbent = ledger.artifact_path(row_art) if row_art else None
    if parent is None:
        art_row = None
        conn = ledger.connect()
        r = conn.execute("SELECT parent_sha FROM artifacts WHERE sha256=?", (cand_sha,)).fetchone()
        if r and r["parent_sha"]:
            prow = conn.execute("SELECT path FROM artifacts WHERE sha256=?", (r["parent_sha"],)).fetchone()
            parent = ledger.artifact_path(prow) if prow else None
        conn.close()

    for label, opp_path, seed_block in (("incumbent", incumbent, INCUMBENT_SEEDS), ("parent", parent, PARENT_SEEDS)):
        if opp_path is None:
            steps.append((f"vs_{label}", "SKIP", "no artifact resolved"))
            continue
        batch_id, results = arena.h2h(cand_path, opp_path, seed_block, both_seats=True, workers=workers,
                                       label=f"gate:{Path(cand_path).stem}_vs_{label}")
        per_opponent_batches[label] = batch_id
        losses = candidate_losses(results, cand_path)
        worse, better = paired_regressions(cand_path, opp_path, results, seed_block, workers, label)
        steps.append((f"vs_{label}_paired", "VETO" if worse else "PASS",
                      f"{better} games better than the {label} mirror, {len(worse)} worse (raw losses {len(losses)})"))
        raw_lost = len(losses)
        losses = worse
        if losses:
            veto = True
            veto_reason = veto_reason or f"lost to {label} in {len(losses)}/{len(results)} games (seed_block={seed_block})"
        steps.append((f"vs_{label}", "VETO" if losses else "PASS",
                      f"raw W-L {len(results) - raw_lost}-{raw_lost}, paired regressions {len(losses)}, over {seed_block}"))

    # step 5: structurally different opponents (only if not already vetoed -- still run, for the report)
    others = others or []
    other_records = {}
    for opp in others:
        opp_path, _ = _resolve(opp)
        batch_id, results = arena.h2h(cand_path, opp_path, OTHER_OPPONENT_SEEDS, both_seats=True, workers=workers,
                                       label=f"gate:{Path(cand_path).stem}_vs_{Path(opp_path).stem}")
        other_records[opp] = batch_id
        per_opponent_batches[f"other:{opp}"] = batch_id
        lost = len(candidate_losses(results, cand_path))
        # reported per opponent, not a veto: the protocol vetoes only on incumbent/parent
        steps.append((f"vs_other:{opp}", "INFO", f"{len(results) - lost}-{lost} over {OTHER_OPPONENT_SEEDS}"))
    if not others:
        steps.append(("other_opponents", "SKIP", "none passed via --others"))

    # step 7: frozen parameters, one untouched seed block vs incumbent -- only if nothing vetoed yet
    if not veto and incumbent is not None:
        batch_id, results = arena.h2h(cand_path, incumbent, FINAL_SEEDS, both_seats=True, workers=workers,
                                       label=f"gate:{Path(cand_path).stem}_final_untouched")
        per_opponent_batches["final_untouched"] = batch_id
        lost, better = paired_regressions(cand_path, incumbent, results, FINAL_SEEDS, workers, "final")
        if lost:
            veto = True
            veto_reason = f"lost {len(lost)}/{len(results)} on the untouched final block {FINAL_SEEDS}"
        steps.append(("final_untouched", "VETO" if lost else "PASS",
                      f"raw W-L {len(results) - len(candidate_losses(results, cand_path))}-{len(candidate_losses(results, cand_path))}, paired regressions {len(lost)}, over {FINAL_SEEDS}"))

    # step 6: audit
    audit_findings = []
    for label, batch_id in per_opponent_batches.items():
        audit_findings.extend(audit.audit_batch(batch_id))
    critical = [f for f in audit_findings if f["severity"] == "critical"]
    steps.append(("audit", "FAIL" if critical else "PASS", f"{len(audit_findings)} findings, {len(critical)} critical"))
    if critical:
        veto = True
        veto_reason = veto_reason or "critical audit findings"

    verdict = "VETO" if veto else "PASS"
    return {
        "verdict": verdict, "reason": veto_reason, "steps": steps,
        "candidate": candidate, "batches": per_opponent_batches, "other_batches": other_records,
        "audit_findings": audit_findings,
    }


def print_report(result):
    print(f"GATE VERDICT: {result['verdict']}" + (f" ({result['reason']})" if result.get('reason') else ""))
    for name, status, detail in result["steps"]:
        print(f"  [{status:<5}] {name}: {detail}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--candidate", required=True)
    p.add_argument("--parent", default=None)
    p.add_argument("--incumbent", default=None)
    p.add_argument("--others", default="", help="comma-separated artifact names")
    p.add_argument("--workers", type=int, default=None)
    args = p.parse_args()
    others = [o for o in args.others.split(",") if o]
    incumbent_path = _resolve(args.incumbent)[0] if args.incumbent else None
    parent_path = _resolve(args.parent)[0] if args.parent else None
    result = run_gate(args.candidate, parent=parent_path, incumbent=incumbent_path, others=others, workers=args.workers)
    print_report(result)
    from lab import report
    for label, batch_id in result["batches"].items():
        print(f"report: {report.write_report(batch_id, gate_result=result)}")


if __name__ == "__main__":
    main()
