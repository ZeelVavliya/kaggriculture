# Batch report: h2h-985fbbcb-vs-887aaad7-097f30

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8_carrot | 1.373 | 1739 | 46 | 2 | 2 | 32.6 |
| v43_lead8 | -1.373 | 1261 | 2 | 46 | 2 | -32.6 |

## Per-opponent records

### v43_lead8_carrot
- vs v43_lead8: W46-L2-T2 (win rate 95% CI 84%-98%, n=50), mean margin 32.6

### v43_lead8
- vs v43_lead8_carrot: W2-L46-T2 (win rate 95% CI 2%-16%, n=50), mean margin -32.6

## Audit findings (ranked by severity)

- **shed_overflow**: 478 occurrences
- **preempted_sell**: 2 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8 | shed_overflow | 239 | 4.78 |
| v43_lead8 | preempted_sell | 1 | 0.02 |
| v43_lead8_carrot | shed_overflow | 239 | 4.78 |
| v43_lead8_carrot | preempted_sell | 1 | 0.02 |

Top findings:

- [high] `shed_overflow` game=c1e5f9bf95274a07 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c1e5f9bf95274a07 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ccb6abb55b6f4d11 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9d2b944706da4fa2 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9d2b944706da4fa2 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9d2b944706da4fa2 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9d2b944706da4fa2 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9d2b944706da4fa2 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9d2b944706da4fa2 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9d2b944706da4fa2 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9d2b944706da4fa2 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c5defbbefdb9471f step=456 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c5defbbefdb9471f step=456 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c5defbbefdb9471f step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c5defbbefdb9471f step=480 player=1 — shed total=100 >= cap 100 at day boundary

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
