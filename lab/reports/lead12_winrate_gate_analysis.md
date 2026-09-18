# Gate analysis: v43_open3_lead12, win-rate protocol (2026-09-18)

**Verdict: PASS.** All three decision blocks (vs_incumbent, vs_parent, final_untouched) clear the
Wilson 95% lower-bound > 0.50 threshold comfortably (worst case LB=0.812); the audit found 0
critical findings. Candidate `v43_open3_lead12` (sha 5b37959e) is now eligible for the
package-check step.

## Decision blocks

| block | seed_block | raw W-L-T (candidate) | Wilson 95% LB | passes 0.50? | paired regressions (diagnostic) |
|---|---|---|---|---|---|
| vs_incumbent (v43_lead8_open3) | 850000-850024 | 46-4-0 | 0.812 | yes | 42 better / 2 worse than incumbent-mirror baseline |
| vs_parent (v43_open3_carrot) | 860000-860024 | 46-4-0 | 0.812 | yes | 44 better / 2 worse than parent-mirror baseline |
| final_untouched (v43_lead8_open3) | 910000-910024 | 49-1-0 | 0.895 | yes | 48 better / 0 worse than final-mirror baseline |

All five numbers above (raw record, Wilson LB to 3 decimals, and both paired-regression counts)
were independently recomputed directly from `games` for each block's batch (read-only
`lab/runs.db` query, `sha_p0`/`sha_p1` resolved via `artifacts.sha256`, `HARNESS_ERROR` rows
excluded — there were none to exclude in any of these six batches) and match the gate's stdout
report in `lab/reports/gate_lead12_winrate.log` exactly, both for the win-rate LBs and for the
paired-regression diagnostic. `lab/reports/gate_lead12_winrate.err` is empty — nothing crashed.
No discrepancy was found, so there is no reason to suspect a bug in `lab/gate.py`'s arithmetic.

Relevant batch ids (all created 2026-09-18 09:07-09:41 UTC, cross-checked against
`lab/reports/gate_lead12_winrate.log`):

- vs_incumbent: `h2h-5b37959e-vs-774a7f56-db3716` (mirror baseline `h2h-774a7f56-vs-774a7f56-6448f2`)
- vs_parent: `h2h-5b37959e-vs-1367897a-eed6d3` (mirror baseline `h2h-1367897a-vs-1367897a-6220a4`)
- final_untouched: `h2h-5b37959e-vs-774a7f56-1f72ec` (mirror baseline `h2h-774a7f56-vs-774a7f56-e2fbc4`)

## Old rule vs. new rule on this same candidate

Iteration 32 vetoed this exact candidate under the old "any single paired-regression game = veto"
rule, on 2 paired-regression games on the parent block (860000-860024), despite a raw record of
46-4 there. That raw record is the same 46-4 confirmed above, and its Wilson 95% LB is 0.812 —
nowhere near the 0.50 threshold, so the new rule clears that block easily; the 2 "regression" games
the old rule vetoed on are exactly the 2 paired-regression losses recomputed above, now correctly
treated as diagnostic noise rather than an automatic veto.

The more interesting question is the untouched final block, since that's the one that caught the
same class of problem for a related candidate (v43_open3_lead9) in iteration 38, where a 47-3
record still only cleared LB≈0.84 — a "close" block by the old zero-tolerance standard, but one
that cleared the new 0.50 bar comfortably. That pattern holds here too, and even more strongly:
v43_open3_lead12's final_untouched record is 49-1 (better than lead9's 47-3), giving LB=0.895
versus lead9's ≈0.84. There is no close call anywhere in this run — every block is comfortably
above 0.80, well clear of the 0.50 bar the new rule actually tests.

## vs_other records (informational, not part of the verdict)

| opponent | record (candidate view) | seed_block |
|---|---|---|
| v43_lead8_open7 | 48-2-0 | 870000-870024 |
| v43_lead8 | 48-2-0 | 870000-870024 |
| opp_v43 | 48-2-0 | 870000-870024 |

## Audit findings

3827 total findings across all batches, **0 critical**. Spot-checking the vs_incumbent batch
report (`lab/reports/h2h-5b37959e-vs-774a7f56-db3716.md`) shows the findings are `shed_overflow`
(492 occurrences) and `preempted_sell` (135 occurrences) — both non-critical severities (high, not
critical) present on both agents (candidate and incumbent alike), consistent with the gate's
`0 critical` verdict and not a reason to withhold the PASS.

## Next step

Since the verdict is PASS, `v43_open3_lead12` is eligible for the package-check step
(`python -m lab.registry --check-package`) — not run as part of this analysis, per the task's
constraints. That step is for whoever picks this candidate up next.
