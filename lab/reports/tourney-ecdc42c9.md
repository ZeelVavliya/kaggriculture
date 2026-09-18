# Batch report: tourney-ecdc42c9

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8_open20 | 3.183 | 2053 | 76 | 4 | 0 | 453.4 |
| v43_lead8_open43 | 1.452 | 1752 | 58 | 22 | 0 | -78.6 |
| v43_lead8_open50 | 0.000 | 1500 | 40 | 40 | 0 | -80.2 |
| v43_lead8_carrot | -1.452 | 1248 | 22 | 58 | 0 | -136.0 |
| v43_lead8 | -3.183 | 947 | 4 | 76 | 0 | -158.6 |

## Per-opponent records

### v43_lead8_open20
- vs v43_lead8: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 642.9
- vs v43_lead8_open50: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 629.9
- vs v43_lead8_open43: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin -59.0
- vs v43_lead8_carrot: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 600.0

### v43_lead8_open43
- vs v43_lead8: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin -62.0
- vs v43_lead8_open50: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin -231.7
- vs v43_lead8_open20: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin 59.0
- vs v43_lead8_carrot: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin -79.6

### v43_lead8_open50
- vs v43_lead8: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 43.7
- vs v43_lead8_open43: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin 231.7
- vs v43_lead8_open20: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -629.9
- vs v43_lead8_carrot: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 33.7

### v43_lead8_carrot
- vs v43_lead8: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 10.0
- vs v43_lead8_open50: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -33.7
- vs v43_lead8_open43: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin 79.6
- vs v43_lead8_open20: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -600.0

### v43_lead8
- vs v43_lead8_open50: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -43.7
- vs v43_lead8_open43: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin 62.0
- vs v43_lead8_open20: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -642.9
- vs v43_lead8_carrot: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -10.0

## Audit findings (ranked by severity)

- **shed_overflow**: 1894 occurrences
- **preempted_sell**: 24 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8 | shed_overflow | 375 | 4.69 |
| v43_lead8 | preempted_sell | 7 | 0.09 |
| v43_lead8_carrot | shed_overflow | 375 | 4.69 |
| v43_lead8_carrot | preempted_sell | 7 | 0.09 |
| v43_lead8_open20 | shed_overflow | 390 | 4.88 |
| v43_lead8_open43 | shed_overflow | 381 | 4.76 |
| v43_lead8_open43 | preempted_sell | 3 | 0.04 |
| v43_lead8_open50 | shed_overflow | 373 | 4.66 |
| v43_lead8_open50 | preempted_sell | 7 | 0.09 |

Top findings:

- [high] `shed_overflow` game=4644f75325524446 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4644f75325524446 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4644f75325524446 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4644f75325524446 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4644f75325524446 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4644f75325524446 step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4644f75325524446 step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4644f75325524446 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4644f75325524446 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b37c0f953b2e490c step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b37c0f953b2e490c step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b37c0f953b2e490c step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b37c0f953b2e490c step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b37c0f953b2e490c step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b37c0f953b2e490c step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b37c0f953b2e490c step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b37c0f953b2e490c step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b37c0f953b2e490c step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=594afa1c056e4299 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=354093075ede4daa step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=354093075ede4daa step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=354093075ede4daa step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=354093075ede4daa step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2afb963b220e433c step=456 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2afb963b220e433c step=456 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2afb963b220e433c step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2afb963b220e433c step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2afb963b220e433c step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2afb963b220e433c step=504 player=1 — shed total=100 >= cap 100 at day boundary
