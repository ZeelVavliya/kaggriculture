# Batch report: h2h-985fbbcb-vs-919fc1d6-0b9dda

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8_carrot | 3.615 | 2128 | 50 | 0 | 0 | 3216.0 |
| opp_v43 | -3.615 | 872 | 0 | 50 | 0 | -3216.0 |

## Per-opponent records

### v43_lead8_carrot
- vs opp_v43: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 3216.0

### opp_v43
- vs v43_lead8_carrot: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -3216.0

## Audit findings (ranked by severity)

- **shed_overflow**: 490 occurrences
- **preempted_sell**: 320 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_v43 | shed_overflow | 244 | 4.88 |
| opp_v43 | preempted_sell | 188 | 3.76 |
| v43_lead8_carrot | shed_overflow | 246 | 4.92 |
| v43_lead8_carrot | preempted_sell | 132 | 2.64 |

Top findings:

- [high] `shed_overflow` game=0db4fdff5d2943ac step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0db4fdff5d2943ac step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0db4fdff5d2943ac step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0db4fdff5d2943ac step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0db4fdff5d2943ac step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0db4fdff5d2943ac step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0db4fdff5d2943ac step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0db4fdff5d2943ac step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e47b5fc6e32f4936 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e47b5fc6e32f4936 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e47b5fc6e32f4936 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e47b5fc6e32f4936 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e47b5fc6e32f4936 step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e47b5fc6e32f4936 step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e47b5fc6e32f4936 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e47b5fc6e32f4936 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e60f35ef49f04b9e step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e60f35ef49f04b9e step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e60f35ef49f04b9e step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e60f35ef49f04b9e step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e60f35ef49f04b9e step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e60f35ef49f04b9e step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e60f35ef49f04b9e step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e60f35ef49f04b9e step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20634df9219744e2 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20634df9219744e2 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20634df9219744e2 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20634df9219744e2 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20634df9219744e2 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20634df9219744e2 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d621b3b2ab6d453f step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d621b3b2ab6d453f step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d621b3b2ab6d453f step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d621b3b2ab6d453f step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d621b3b2ab6d453f step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d621b3b2ab6d453f step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e57596d331684e5b step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e57596d331684e5b step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e57596d331684e5b step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e57596d331684e5b step=552 player=1 — shed total=100 >= cap 100 at day boundary

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
