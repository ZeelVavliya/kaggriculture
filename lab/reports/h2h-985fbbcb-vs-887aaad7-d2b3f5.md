# Batch report: h2h-985fbbcb-vs-887aaad7-d2b3f5

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8_carrot | 1.097 | 1691 | 41 | 1 | 8 | 15.4 |
| v43_lead8 | -1.097 | 1309 | 1 | 41 | 8 | -15.4 |

## Per-opponent records

### v43_lead8_carrot
- vs v43_lead8: W41-L1-T8 (win rate 95% CI 79%-96%, n=50), mean margin 15.4

### v43_lead8
- vs v43_lead8_carrot: W1-L41-T8 (win rate 95% CI 4%-21%, n=50), mean margin -15.4

## Audit findings (ranked by severity)

- **shed_overflow**: 452 occurrences
- **preempted_sell**: 2 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8 | shed_overflow | 226 | 4.52 |
| v43_lead8 | preempted_sell | 1 | 0.02 |
| v43_lead8_carrot | shed_overflow | 226 | 4.52 |
| v43_lead8_carrot | preempted_sell | 1 | 0.02 |

Top findings:

- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b15cbbe2944e4ca5 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7f9f8612e55c49ba step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=df697be25c634509 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b372d99dae9447be step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b372d99dae9447be step=504 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**PASS**
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [PASS] vs_incumbent_paired: 42 games better than the incumbent mirror, 0 worse (raw losses 4)
- [PASS] vs_incumbent: raw W-L 46-4, paired regressions 0, over 850000-850024
- [PASS] vs_parent_paired: 44 games better than the parent mirror, 0 worse (raw losses 2)
- [PASS] vs_parent: raw W-L 48-2, paired regressions 0, over 860000-860024
- [INFO] vs_other:v43_open55: 50-0 over 870000-870024
- [INFO] vs_other:opp_v43: 50-0 over 870000-870024
- [PASS] final_untouched: raw W-L 49-1, paired regressions 0, over 910000-910024
- [PASS] audit: 2986 findings, 0 critical
