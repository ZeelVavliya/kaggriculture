# Batch report: tourney-369e8b5a

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_open3_carrot | 3.190 | 2054 | 75 | 3 | 2 | 456.2 |
| v43_lead8_open7_carrot | 1.220 | 1712 | 52 | 24 | 4 | 371.5 |
| v43_lead8_open3 | 0.550 | 1595 | 43 | 33 | 4 | 446.1 |
| v43_lead8_open7 | -1.256 | 1282 | 22 | 56 | 2 | 359.4 |
| v43_open55_carrot | -3.704 | 857 | 2 | 78 | 0 | -1633.2 |

## Per-opponent records

### v43_open3_carrot
- vs v43_lead8_open7_carrot: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 6.8
- vs v43_lead8_open3: W17-L1-T2 (win rate 95% CI 70%-97%, n=20), mean margin 8.6
- vs v43_lead8_open7: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 15.4
- vs v43_open55_carrot: W20-L0-T0 (win rate 95% CI 84%-100%, n=20), mean margin 1793.9

### v43_lead8_open7_carrot
- vs v43_open3_carrot: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -6.8
- vs v43_lead8_open3: W15-L3-T2 (win rate 95% CI 58%-92%, n=20), mean margin 1.8
- vs v43_lead8_open7: W17-L1-T2 (win rate 95% CI 70%-97%, n=20), mean margin 8.6
- vs v43_open55_carrot: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 1482.3

### v43_lead8_open3
- vs v43_lead8_open7_carrot: W3-L15-T2 (win rate 95% CI 8%-42%, n=20), mean margin -1.8
- vs v43_open3_carrot: W1-L17-T2 (win rate 95% CI 3%-30%, n=20), mean margin -8.6
- vs v43_lead8_open7: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 6.8
- vs v43_open55_carrot: W20-L0-T0 (win rate 95% CI 84%-100%, n=20), mean margin 1788.1

### v43_lead8_open7
- vs v43_lead8_open7_carrot: W1-L17-T2 (win rate 95% CI 3%-30%, n=20), mean margin -8.6
- vs v43_open3_carrot: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -15.4
- vs v43_lead8_open3: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -6.8
- vs v43_open55_carrot: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 1468.5

### v43_open55_carrot
- vs v43_lead8_open7_carrot: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -1482.3
- vs v43_open3_carrot: W0-L20-T0 (win rate 95% CI 0%-16%, n=20), mean margin -1793.9
- vs v43_lead8_open3: W0-L20-T0 (win rate 95% CI 0%-16%, n=20), mean margin -1788.1
- vs v43_lead8_open7: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -1468.5

## Audit findings (ranked by severity)

- **shed_overflow**: 2024 occurrences
- **preempted_sell**: 560 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8_open3 | shed_overflow | 396 | 4.95 |
| v43_lead8_open3 | preempted_sell | 62 | 0.78 |
| v43_lead8_open7 | shed_overflow | 410 | 5.12 |
| v43_lead8_open7 | preempted_sell | 58 | 0.72 |
| v43_lead8_open7_carrot | shed_overflow | 410 | 5.12 |
| v43_lead8_open7_carrot | preempted_sell | 58 | 0.72 |
| v43_open3_carrot | shed_overflow | 396 | 4.95 |
| v43_open3_carrot | preempted_sell | 62 | 0.78 |
| v43_open55_carrot | shed_overflow | 412 | 5.15 |
| v43_open55_carrot | preempted_sell | 320 | 4.00 |

Top findings:

- [high] `shed_overflow` game=00899cd5e5df48a9 step=456 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=456 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=00899cd5e5df48a9 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ead5d1ba73874d2f step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=54d55db2f4744e76 step=456 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=54d55db2f4744e76 step=456 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=54d55db2f4744e76 step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=54d55db2f4744e76 step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=54d55db2f4744e76 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=54d55db2f4744e76 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=54d55db2f4744e76 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=54d55db2f4744e76 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=54d55db2f4744e76 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=54d55db2f4744e76 step=552 player=1 — shed total=100 >= cap 100 at day boundary
