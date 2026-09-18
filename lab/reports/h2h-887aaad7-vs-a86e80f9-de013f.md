# Batch report: h2h-887aaad7-vs-a86e80f9-de013f

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8 | 1.936 | 1836 | 49 | 1 | 0 | 1127.3 |
| v43_open55 | -1.936 | 1164 | 1 | 49 | 0 | -1127.3 |

## Per-opponent records

### v43_lead8
- vs v43_open55: W49-L1-T0 (win rate 95% CI 90%-100%, n=50), mean margin 1127.3

### v43_open55
- vs v43_lead8: W1-L49-T0 (win rate 95% CI 0%-10%, n=50), mean margin -1127.3

## Audit findings (ranked by severity)

- **shed_overflow**: 498 occurrences
- **preempted_sell**: 312 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8 | shed_overflow | 249 | 4.98 |
| v43_lead8 | preempted_sell | 130 | 2.60 |
| v43_open55 | shed_overflow | 249 | 4.98 |
| v43_open55 | preempted_sell | 182 | 3.64 |

Top findings:

- [high] `shed_overflow` game=13b8ffb9df84433e step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13b8ffb9df84433e step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9607f28f505241b2 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d6e57014c094e03 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d1485a0873d14ac3 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d1485a0873d14ac3 step=504 player=1 — shed total=100 >= cap 100 at day boundary

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
