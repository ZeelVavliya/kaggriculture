# Batch report: h2h-887aaad7-vs-919fc1d6-cc4e21

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8 | 3.615 | 2128 | 50 | 0 | 0 | 3215.6 |
| opp_v43 | -3.615 | 872 | 0 | 50 | 0 | -3215.6 |

## Per-opponent records

### v43_lead8
- vs opp_v43: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 3215.6

### opp_v43
- vs v43_lead8: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -3215.6

## Audit findings (ranked by severity)

- **shed_overflow**: 490 occurrences
- **preempted_sell**: 320 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_v43 | shed_overflow | 244 | 4.88 |
| opp_v43 | preempted_sell | 188 | 3.76 |
| v43_lead8 | shed_overflow | 246 | 4.92 |
| v43_lead8 | preempted_sell | 132 | 2.64 |

Top findings:

- [high] `shed_overflow` game=1619049d70634e0e step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1619049d70634e0e step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=680ccca4b45040f8 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=680ccca4b45040f8 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=680ccca4b45040f8 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=680ccca4b45040f8 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=680ccca4b45040f8 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=680ccca4b45040f8 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e0024be25b54cb9 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e0024be25b54cb9 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e0024be25b54cb9 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e0024be25b54cb9 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e0024be25b54cb9 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e0024be25b54cb9 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e0024be25b54cb9 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e0024be25b54cb9 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=474ef6fdbd5c493f step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=24cea04847d64ad8 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=24cea04847d64ad8 step=576 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**PASS**
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [PASS] vs_incumbent_paired: 45 games better than the incumbent mirror, 0 worse (raw losses 1)
- [PASS] vs_incumbent: raw W-L 49-1, paired regressions 0, over 850000-850024
- [PASS] vs_parent_paired: 46 games better than the parent mirror, 0 worse (raw losses 2)
- [PASS] vs_parent: raw W-L 48-2, paired regressions 0, over 860000-860024
- [INFO] vs_other:v43_lead6: 50-0 over 870000-870024
- [INFO] vs_other:opp_v43: 50-0 over 870000-870024
- [PASS] final_untouched: raw W-L 50-0, paired regressions 0, over 910000-910024
- [PASS] audit: 3900 findings, 0 critical
