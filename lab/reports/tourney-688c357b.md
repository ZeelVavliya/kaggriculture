# Batch report: tourney-688c357b

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_open3_lead12 | 3.861 | 2171 | 116 | 4 | 0 | 967.3 |
| v43_open3_lead11 | 1.770 | 1808 | 88 | 32 | 0 | 488.7 |
| v43_open3_lead10 | -0.000 | 1500 | 60 | 60 | 0 | -17.4 |
| v43_open3_lead9 | -1.770 | 1192 | 32 | 88 | 0 | -560.8 |
| v43_open3_carrot | -3.861 | 829 | 4 | 116 | 0 | -877.8 |

## Per-opponent records

### v43_open3_lead12
- vs v43_open3_carrot: W29-L1-T0 (win rate 95% CI 83%-99%, n=30), mean margin 895.8
- vs v43_open3_lead9: W29-L1-T0 (win rate 95% CI 83%-99%, n=30), mean margin 1073.1
- vs v43_open3_lead10: W29-L1-T0 (win rate 95% CI 83%-99%, n=30), mean margin 970.2
- vs v43_open3_lead11: W29-L1-T0 (win rate 95% CI 83%-99%, n=30), mean margin 930.1

### v43_open3_lead11
- vs v43_open3_carrot: W29-L1-T0 (win rate 95% CI 83%-99%, n=30), mean margin 900.7
- vs v43_open3_lead9: W29-L1-T0 (win rate 95% CI 83%-99%, n=30), mean margin 1039.7
- vs v43_open3_lead10: W29-L1-T0 (win rate 95% CI 83%-99%, n=30), mean margin 944.6
- vs v43_open3_lead12: W1-L29-T0 (win rate 95% CI 1%-17%, n=30), mean margin -930.1

### v43_open3_lead10
- vs v43_open3_carrot: W29-L1-T0 (win rate 95% CI 83%-99%, n=30), mean margin 862.4
- vs v43_open3_lead9: W29-L1-T0 (win rate 95% CI 83%-99%, n=30), mean margin 982.8
- vs v43_open3_lead11: W1-L29-T0 (win rate 95% CI 1%-17%, n=30), mean margin -944.6
- vs v43_open3_lead12: W1-L29-T0 (win rate 95% CI 1%-17%, n=30), mean margin -970.2

### v43_open3_lead9
- vs v43_open3_carrot: W29-L1-T0 (win rate 95% CI 83%-99%, n=30), mean margin 852.4
- vs v43_open3_lead10: W1-L29-T0 (win rate 95% CI 1%-17%, n=30), mean margin -982.8
- vs v43_open3_lead11: W1-L29-T0 (win rate 95% CI 1%-17%, n=30), mean margin -1039.7
- vs v43_open3_lead12: W1-L29-T0 (win rate 95% CI 1%-17%, n=30), mean margin -1073.1

### v43_open3_carrot
- vs v43_open3_lead9: W1-L29-T0 (win rate 95% CI 1%-17%, n=30), mean margin -852.4
- vs v43_open3_lead10: W1-L29-T0 (win rate 95% CI 1%-17%, n=30), mean margin -862.4
- vs v43_open3_lead11: W1-L29-T0 (win rate 95% CI 1%-17%, n=30), mean margin -900.7
- vs v43_open3_lead12: W1-L29-T0 (win rate 95% CI 1%-17%, n=30), mean margin -895.8

## Audit findings (ranked by severity)

- **shed_overflow**: 3428 occurrences
- **preempted_sell**: 3350 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_open3_carrot | preempted_sell | 924 | 7.70 |
| v43_open3_carrot | shed_overflow | 692 | 5.77 |
| v43_open3_lead10 | preempted_sell | 740 | 6.17 |
| v43_open3_lead10 | shed_overflow | 684 | 5.70 |
| v43_open3_lead11 | preempted_sell | 738 | 6.15 |
| v43_open3_lead11 | shed_overflow | 680 | 5.67 |
| v43_open3_lead12 | shed_overflow | 680 | 5.67 |
| v43_open3_lead12 | preempted_sell | 214 | 1.78 |
| v43_open3_lead9 | preempted_sell | 734 | 6.12 |
| v43_open3_lead9 | shed_overflow | 692 | 5.77 |

Top findings:

- [high] `shed_overflow` game=1f1f12c597ec46de step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f1f12c597ec46de step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f1f12c597ec46de step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f1f12c597ec46de step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f1f12c597ec46de step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f1f12c597ec46de step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f1f12c597ec46de step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f1f12c597ec46de step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f1f12c597ec46de step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1f1f12c597ec46de step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=72a681273d1d43a8 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=72a681273d1d43a8 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=72a681273d1d43a8 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=72a681273d1d43a8 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=72a681273d1d43a8 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=72a681273d1d43a8 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=72a681273d1d43a8 step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=72a681273d1d43a8 step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=72a681273d1d43a8 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=72a681273d1d43a8 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6022a35d207843f3 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6022a35d207843f3 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6022a35d207843f3 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6022a35d207843f3 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6022a35d207843f3 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6022a35d207843f3 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6022a35d207843f3 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6022a35d207843f3 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6022a35d207843f3 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6022a35d207843f3 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=47dfb8ac8e1d4507 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=47dfb8ac8e1d4507 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=47dfb8ac8e1d4507 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=47dfb8ac8e1d4507 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=47dfb8ac8e1d4507 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=47dfb8ac8e1d4507 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=47dfb8ac8e1d4507 step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=47dfb8ac8e1d4507 step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=47dfb8ac8e1d4507 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=47dfb8ac8e1d4507 step=672 player=1 — shed total=100 >= cap 100 at day boundary
