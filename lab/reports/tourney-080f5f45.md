# Batch report: tourney-080f5f45

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| opp_v41 | 8.320 | 2945 | 80 | 0 | 0 | 33482.6 |
| opp_soil | 2.913 | 2006 | 60 | 20 | 0 | 25607.8 |
| opp_salem2900 | -2.651 | 1039 | 32 | 48 | 0 | -16370.2 |
| c94 | -3.350 | 918 | 24 | 56 | 0 | -21326.5 |
| c95 | -5.232 | 591 | 4 | 76 | 0 | -21393.7 |

## Per-opponent records

### opp_v41
- vs opp_soil: W20-L0-T0 (win rate 95% CI 84%-100%, n=20), mean margin 7061.1
- vs opp_salem2900: W20-L0-T0 (win rate 95% CI 84%-100%, n=20), mean margin 37716.2
- vs c94: W20-L0-T0 (win rate 95% CI 84%-100%, n=20), mean margin 44536.3
- vs c95: W20-L0-T0 (win rate 95% CI 84%-100%, n=20), mean margin 44616.8

### opp_soil
- vs opp_v41: W0-L20-T0 (win rate 95% CI 0%-16%, n=20), mean margin -7061.1
- vs opp_salem2900: W20-L0-T0 (win rate 95% CI 84%-100%, n=20), mean margin 30949.5
- vs c94: W20-L0-T0 (win rate 95% CI 84%-100%, n=20), mean margin 39230.9
- vs c95: W20-L0-T0 (win rate 95% CI 84%-100%, n=20), mean margin 39312.1

### opp_salem2900
- vs opp_v41: W0-L20-T0 (win rate 95% CI 0%-16%, n=20), mean margin -37716.2
- vs opp_soil: W0-L20-T0 (win rate 95% CI 0%-16%, n=20), mean margin -30949.5
- vs c94: W16-L4-T0 (win rate 95% CI 58%-92%, n=20), mean margin 1609.8
- vs c95: W16-L4-T0 (win rate 95% CI 58%-92%, n=20), mean margin 1574.9

### c94
- vs opp_v41: W0-L20-T0 (win rate 95% CI 0%-16%, n=20), mean margin -44536.3
- vs opp_soil: W0-L20-T0 (win rate 95% CI 0%-16%, n=20), mean margin -39230.9
- vs opp_salem2900: W4-L16-T0 (win rate 95% CI 8%-42%, n=20), mean margin -1609.8
- vs c95: W20-L0-T0 (win rate 95% CI 84%-100%, n=20), mean margin 70.9

### c95
- vs opp_v41: W0-L20-T0 (win rate 95% CI 0%-16%, n=20), mean margin -44616.8
- vs opp_soil: W0-L20-T0 (win rate 95% CI 0%-16%, n=20), mean margin -39312.1
- vs opp_salem2900: W4-L16-T0 (win rate 95% CI 8%-42%, n=20), mean margin -1574.9
- vs c94: W0-L20-T0 (win rate 95% CI 0%-16%, n=20), mean margin -70.9

## Audit findings (ranked by severity)

- **preempted_sell**: 8717 occurrences
- **shed_overflow**: 708 occurrences
- **animal_escape**: 160 occurrences
- **melon_underyield**: 28 occurrences
- **overage_time_consumed**: 6 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| c94 | preempted_sell | 1958 | 24.48 |
| c94 | animal_escape | 80 | 1.00 |
| c95 | preempted_sell | 1300 | 16.25 |
| c95 | animal_escape | 80 | 1.00 |
| opp_salem2900 | preempted_sell | 1966 | 24.57 |
| opp_salem2900 | shed_overflow | 186 | 2.33 |
| opp_salem2900 | melon_underyield | 28 | 0.35 |
| opp_soil | preempted_sell | 1608 | 20.10 |
| opp_soil | shed_overflow | 164 | 2.05 |
| opp_soil | overage_time_consumed | 6 | 0.07 |
| opp_v41 | preempted_sell | 1885 | 23.56 |
| opp_v41 | shed_overflow | 358 | 4.47 |

Top findings:

- [high] `shed_overflow` game=ad9dee3cb1684d9c step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ad9dee3cb1684d9c step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ad9dee3cb1684d9c step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ad9dee3cb1684d9c step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ad9dee3cb1684d9c step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ad9dee3cb1684d9c step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9bac41abb834695 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9bac41abb834695 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9bac41abb834695 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9bac41abb834695 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9bac41abb834695 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9bac41abb834695 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9bac41abb834695 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9bac41abb834695 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2e49c9a7c5994fc5 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2e49c9a7c5994fc5 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2e49c9a7c5994fc5 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2e49c9a7c5994fc5 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2e49c9a7c5994fc5 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2e49c9a7c5994fc5 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2e49c9a7c5994fc5 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2e49c9a7c5994fc5 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5bc87da7bf30499c step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5bc87da7bf30499c step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5bc87da7bf30499c step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e39ace0a64684509 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e39ace0a64684509 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e39ace0a64684509 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e39ace0a64684509 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e39ace0a64684509 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e39ace0a64684509 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=970065e6740343c8 step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=970065e6740343c8 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=970065e6740343c8 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6de47f8a8e7045ca step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6de47f8a8e7045ca step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6de47f8a8e7045ca step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6de47f8a8e7045ca step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6de47f8a8e7045ca step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6de47f8a8e7045ca step=624 player=0 — shed total=100 >= cap 100 at day boundary
