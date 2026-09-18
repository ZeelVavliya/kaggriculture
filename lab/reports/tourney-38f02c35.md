# Batch report: tourney-38f02c35

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8_open7 | 2.826 | 1991 | 57 | 3 | 0 | 19.7 |
| v43_lead8_open12 | 0.868 | 1651 | 39 | 21 | 0 | 8.6 |
| v43_lead8_open15 | -0.868 | 1349 | 21 | 39 | 0 | -2.6 |
| v43_lead8_open20 | -2.826 | 1009 | 3 | 57 | 0 | -25.7 |

## Per-opponent records

### v43_lead8_open7
- vs v43_lead8_open20: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 27.7
- vs v43_lead8_open15: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 18.7
- vs v43_lead8_open12: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 12.7

### v43_lead8_open12
- vs v43_lead8_open20: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 26.7
- vs v43_lead8_open15: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 11.7
- vs v43_lead8_open7: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -12.7

### v43_lead8_open15
- vs v43_lead8_open20: W19-L1-T0 (win rate 95% CI 76%-99%, n=20), mean margin 22.7
- vs v43_lead8_open12: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -11.7
- vs v43_lead8_open7: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -18.7

### v43_lead8_open20
- vs v43_lead8_open15: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -22.7
- vs v43_lead8_open12: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -26.7
- vs v43_lead8_open7: W1-L19-T0 (win rate 95% CI 1%-24%, n=20), mean margin -27.7

## Audit findings (ranked by severity)

- **shed_overflow**: 1272 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8_open12 | shed_overflow | 318 | 5.30 |
| v43_lead8_open15 | shed_overflow | 318 | 5.30 |
| v43_lead8_open20 | shed_overflow | 318 | 5.30 |
| v43_lead8_open7 | shed_overflow | 318 | 5.30 |

Top findings:

- [high] `shed_overflow` game=27df9f8b7f734299 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=27df9f8b7f734299 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=27df9f8b7f734299 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=27df9f8b7f734299 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=27df9f8b7f734299 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=27df9f8b7f734299 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=27df9f8b7f734299 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=27df9f8b7f734299 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=95497cc29e0f4d34 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=95497cc29e0f4d34 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=95497cc29e0f4d34 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=95497cc29e0f4d34 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=95497cc29e0f4d34 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=95497cc29e0f4d34 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=95497cc29e0f4d34 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=95497cc29e0f4d34 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=456 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=456 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=64e02c5b10434e31 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0c2662ec45047fb step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0c2662ec45047fb step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0c2662ec45047fb step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0c2662ec45047fb step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0c2662ec45047fb step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0c2662ec45047fb step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0c2662ec45047fb step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c0c2662ec45047fb step=600 player=1 — shed total=100 >= cap 100 at day boundary
