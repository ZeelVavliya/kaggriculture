# Batch report: h2h-d070da79-vs-a86e80f9-bcbffb

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8_open7 | 3.615 | 2128 | 50 | 0 | 0 | 1876.9 |
| v43_open55 | -3.615 | 872 | 0 | 50 | 0 | -1876.9 |

## Per-opponent records

### v43_lead8_open7
- vs v43_open55: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 1876.9

### v43_open55
- vs v43_lead8_open7: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -1876.9

## Audit findings (ranked by severity)

- **shed_overflow**: 538 occurrences
- **preempted_sell**: 330 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8_open7 | shed_overflow | 269 | 5.38 |
| v43_lead8_open7 | preempted_sell | 132 | 2.64 |
| v43_open55 | shed_overflow | 269 | 5.38 |
| v43_open55 | preempted_sell | 198 | 3.96 |

Top findings:

- [high] `shed_overflow` game=c0e71a89e1954dfa step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0e71a89e1954dfa step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0e71a89e1954dfa step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0e71a89e1954dfa step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0e71a89e1954dfa step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0e71a89e1954dfa step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ef0270df6c6f4fae step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ef0270df6c6f4fae step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ef0270df6c6f4fae step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ef0270df6c6f4fae step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ef0270df6c6f4fae step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ef0270df6c6f4fae step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ef0270df6c6f4fae step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ef0270df6c6f4fae step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d715702873146af step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d715702873146af step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d715702873146af step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d715702873146af step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d715702873146af step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d715702873146af step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f930303079141ce step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=dc10a26023e0420d step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=dc10a26023e0420d step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=dc10a26023e0420d step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=dc10a26023e0420d step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=dc10a26023e0420d step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=dc10a26023e0420d step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2656000173f74a8b step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2656000173f74a8b step=576 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**VETO** — lost to incumbent in 1/50 games (seed_block=850000-850024)
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [VETO] vs_incumbent_paired: 44 games better than the incumbent mirror, 1 worse (raw losses 2)
- [VETO] vs_incumbent: raw W-L 48-2, paired regressions 1, over 850000-850024
- [PASS] vs_parent_paired: 47 games better than the parent mirror, 0 worse (raw losses 1)
- [PASS] vs_parent: raw W-L 49-1, paired regressions 0, over 860000-860024
- [INFO] vs_other:v43_open55: 50-0 over 870000-870024
- [INFO] vs_other:opp_v43: 50-0 over 870000-870024
- [INFO] vs_other:v43_lead8_carrot: 45-5 over 870000-870024
- [PASS] audit: 3167 findings, 0 critical
