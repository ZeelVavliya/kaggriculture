# Batch report: h2h-985fbbcb-vs-887aaad7-7ef310

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8_carrot | 1.220 | 1712 | 46 | 4 | 0 | 26.0 |
| v43_lead8 | -1.220 | 1288 | 4 | 46 | 0 | -26.0 |

## Per-opponent records

### v43_lead8_carrot
- vs v43_lead8: W46-L4-T0 (win rate 95% CI 81%-97%, n=50), mean margin 26.0

### v43_lead8
- vs v43_lead8_carrot: W4-L46-T0 (win rate 95% CI 3%-19%, n=50), mean margin -26.0

## Audit findings (ranked by severity)

- **shed_overflow**: 498 occurrences
- **preempted_sell**: 2 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8 | shed_overflow | 249 | 4.98 |
| v43_lead8 | preempted_sell | 1 | 0.02 |
| v43_lead8_carrot | shed_overflow | 249 | 4.98 |
| v43_lead8_carrot | preempted_sell | 1 | 0.02 |

Top findings:

- [high] `shed_overflow` game=938e8ca6116d4989 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=938e8ca6116d4989 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18cb486d22694ea4 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c443daff36ec4ce2 step=672 player=1 — shed total=100 >= cap 100 at day boundary

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
