"""Write lab/reports/<batch_id>.md: BT table, per-opponent W-L-T with mean margin,
audit findings ranked, and gate verdict (if a gate was run against this batch)."""
import argparse
from pathlib import Path

from lab import audit, rate

LAB = Path(__file__).resolve().parent
REPORTS_DIR = LAB / "reports"


def build_report(batch_id: str, gate_result: dict = None) -> str:
    table = rate.compute_batch_ratings(batch_id)
    findings = audit.audit_batch(batch_id)

    lines = [f"# Batch report: {batch_id}", ""]

    lines.append("## Bradley-Terry ranking (win-based; margin never used for selection)")
    lines.append("")
    lines.append("| name | BT rating | elo | W | L | T | mean margin |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in table:
        lines.append(f"| {r['name']} | {r['bt_rating']:.3f} | {rate.elo(r['bt_rating']):.0f} | {r['W']} | {r['L']} | {r['T']} | {r['mean_margin']:.1f} |")
    lines.append("")

    lines.append("## Per-opponent records")
    lines.append("")
    for r in table:
        lines.append(f"### {r['name']}")
        for opp, rec in r["per_opponent"].items():
            mm = sum(rec["margins"]) / len(rec["margins"]) if rec["margins"] else 0.0
            n = rec["W"] + rec["L"] + rec["T"]
            lo, hi = rate.wilson_ci(rec["W"] + 0.5 * rec["T"], n)
            lines.append(f"- vs {opp}: W{rec['W']}-L{rec['L']}-T{rec['T']} (win rate 95% CI {lo:.0%}-{hi:.0%}, n={n}), mean margin {mm:.1f}")
        lines.append("")

    lines.append("## Audit findings (ranked by severity)")
    lines.append("")
    counts = {}
    for f in findings:
        counts[f["check"]] = counts.get(f["check"], 0) + 1
    for check, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        lines.append(f"- **{check}**: {n} occurrences")
    lines.append("")
    names = {r["sha"]: r["name"] for r in table}
    by_agent = {}
    for f in findings:
        key = (names.get(f.get("sha"), (f.get("sha") or "?")[:8]), f["check"])
        by_agent[key] = by_agent.get(key, 0) + 1
    lines.append("### What to improve, per agent (findings per game played)")
    lines.append("")
    lines.append("| agent | check | count | per game |")
    lines.append("|---|---|---|---|")
    games_per = {r["name"]: r["W"] + r["L"] + r["T"] for r in table}
    for (agent, check), n in sorted(by_agent.items(), key=lambda kv: (kv[0][0], -kv[1])):
        g = games_per.get(agent) or 1
        lines.append(f"| {agent} | {check} | {n} | {n / g:.2f} |")
    lines.append("")
    lines.append("Top findings:")
    lines.append("")
    for f in findings[:40]:
        lines.append(f"- [{f['severity']}] `{f['check']}` game={f['game_id']} step={f['step']} "
                      f"player={f.get('player')} — {f['detail']}")
    lines.append("")

    if gate_result:
        lines.append("## Gate verdict")
        lines.append("")
        lines.append(f"**{gate_result['verdict']}**" + (f" — {gate_result['reason']}" if gate_result.get('reason') else ""))
        for name, status, detail in gate_result["steps"]:
            lines.append(f"- [{status}] {name}: {detail}")
        lines.append("")

    return "\n".join(lines)


def write_report(batch_id: str, gate_result: dict = None) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORTS_DIR / f"{batch_id}.md"
    out.write_text(build_report(batch_id, gate_result), encoding="utf-8")
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--batch", required=True)
    args = p.parse_args()
    out = write_report(args.batch)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
