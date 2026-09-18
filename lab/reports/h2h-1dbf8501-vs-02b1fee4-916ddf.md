# Batch report: h2h-1dbf8501-vs-02b1fee4-916ddf

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v41_lead264 | 3.615 | 2128 | 50 | 0 | 0 | 6982.0 |
| opp_soil | -3.615 | 872 | 0 | 50 | 0 | -6982.0 |

## Per-opponent records

### v41_lead264
- vs opp_soil: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 6982.0

### opp_soil
- vs v41_lead264: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -6982.0

## Audit findings (ranked by severity)

- **preempted_sell**: 1409 occurrences
- **shed_overflow**: 309 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_soil | preempted_sell | 437 | 8.74 |
| opp_soil | shed_overflow | 70 | 1.40 |
| v41_lead264 | preempted_sell | 972 | 19.44 |
| v41_lead264 | shed_overflow | 239 | 4.78 |

Top findings:

- [high] `shed_overflow` game=fc81a8c011584dd5 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=fc81a8c011584dd5 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=fc81a8c011584dd5 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=fc81a8c011584dd5 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=fc81a8c011584dd5 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=fc81a8c011584dd5 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=fc81a8c011584dd5 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8028a0d558f84c3e step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8028a0d558f84c3e step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8028a0d558f84c3e step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8028a0d558f84c3e step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8028a0d558f84c3e step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8028a0d558f84c3e step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8028a0d558f84c3e step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d0d0e07a683e4cec step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d0d0e07a683e4cec step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d0d0e07a683e4cec step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d0d0e07a683e4cec step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d0d0e07a683e4cec step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d0d0e07a683e4cec step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d0d0e07a683e4cec step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=07a8a8b9436f4f95 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=07a8a8b9436f4f95 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=07a8a8b9436f4f95 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=07a8a8b9436f4f95 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=07a8a8b9436f4f95 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=07a8a8b9436f4f95 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=07a8a8b9436f4f95 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=063f91a5925f46f6 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=063f91a5925f46f6 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=063f91a5925f46f6 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=063f91a5925f46f6 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=063f91a5925f46f6 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=063f91a5925f46f6 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1afd1d4f294e4cc4 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1afd1d4f294e4cc4 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1afd1d4f294e4cc4 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1afd1d4f294e4cc4 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1afd1d4f294e4cc4 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1afd1d4f294e4cc4 step=672 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**VETO** — lost 4/50 on the untouched final block 910000-910024
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [PASS] vs_incumbent_paired: 24 games better than the incumbent mirror, 0 worse (raw losses 4)
- [PASS] vs_incumbent: raw W-L 46-4, paired regressions 0, over 850000-850024
- [PASS] vs_parent_paired: 23 games better than the parent mirror, 0 worse (raw losses 1)
- [PASS] vs_parent: raw W-L 49-1, paired regressions 0, over 860000-860024
- [INFO] vs_other:opp_soil: 50-0 over 870000-870024
- [INFO] vs_other:v41_rl_1: 3-47 over 870000-870024
- [VETO] final_untouched: raw W-L 45-5, paired regressions 4, over 910000-910024
- [PASS] audit: 3622 findings, 0 critical
