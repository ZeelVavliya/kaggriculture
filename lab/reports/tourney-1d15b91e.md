# Batch report: tourney-1d15b91e

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| c94 | 8.789 | 3027 | 40 | 0 | 0 | 49854.5 |
| c95 | 4.201 | 2230 | 30 | 10 | 0 | 49796.6 |
| c92 | -0.000 | 1500 | 20 | 20 | 0 | 49653.9 |
| main2 | -4.201 | 770 | 10 | 30 | 0 | -56962.3 |
| main | -8.789 | -27 | 0 | 40 | 0 | -92342.6 |

## Per-opponent records

### c94
- vs main: W10-L0-T0, mean margin 108022.5
- vs main2: W10-L0-T0, mean margin 91065.0
- vs c92: W10-L0-T0, mean margin 235.2
- vs c95: W10-L0-T0, mean margin 95.4

### c95
- vs main: W10-L0-T0, mean margin 108020.1
- vs main2: W10-L0-T0, mean margin 91051.8
- vs c92: W10-L0-T0, mean margin 209.8
- vs c94: W0-L10-T0, mean margin -95.4

### c92
- vs main: W10-L0-T0, mean margin 108019.3
- vs main2: W10-L0-T0, mean margin 91041.2
- vs c94: W0-L10-T0, mean margin -235.2
- vs c95: W0-L10-T0, mean margin -209.8

### main2
- vs main: W10-L0-T0, mean margin 45308.7
- vs c92: W0-L10-T0, mean margin -91041.2
- vs c94: W0-L10-T0, mean margin -91065.0
- vs c95: W0-L10-T0, mean margin -91051.8

### main
- vs main2: W0-L10-T0, mean margin -45308.7
- vs c92: W0-L10-T0, mean margin -108019.3
- vs c94: W0-L10-T0, mean margin -108022.5
- vs c95: W0-L10-T0, mean margin -108020.1

## Audit findings (ranked by severity)

- **preempted_sell**: 2631 occurrences
- **animal_escape**: 363 occurrences
- **stuck_in_inventory**: 285 occurrences
- **shed_overflow**: 50 occurrences
- **melon_underyield**: 50 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| c92 | preempted_sell | 883 | 22.07 |
| c92 | animal_escape | 40 | 1.00 |
| c94 | preempted_sell | 473 | 11.82 |
| c94 | animal_escape | 40 | 1.00 |
| c95 | preempted_sell | 241 | 6.03 |
| c95 | animal_escape | 40 | 1.00 |
| main | preempted_sell | 268 | 6.70 |
| main | animal_escape | 228 | 5.70 |
| main | stuck_in_inventory | 160 | 4.00 |
| main | shed_overflow | 29 | 0.72 |
| main2 | preempted_sell | 766 | 19.15 |
| main2 | stuck_in_inventory | 125 | 3.12 |
| main2 | melon_underyield | 50 | 1.25 |
| main2 | shed_overflow | 21 | 0.53 |
| main2 | animal_escape | 15 | 0.38 |

Top findings:

- [high] `animal_escape` game=2824b416ad6c4dd1 step=48 player=0 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=2824b416ad6c4dd1 step=48 player=0 — GOOSE escaped at (4,2)
- [high] `animal_escape` game=2824b416ad6c4dd1 step=48 player=0 — GOOSE escaped at (3,3)
- [high] `animal_escape` game=2824b416ad6c4dd1 step=48 player=0 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=2824b416ad6c4dd1 step=48 player=0 — GOOSE escaped at (3,4)
- [high] `animal_escape` game=2824b416ad6c4dd1 step=264 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=2824b416ad6c4dd1 step=288 player=0 — GOOSE escaped at (2,1)
- [high] `animal_escape` game=2824b416ad6c4dd1 step=288 player=0 — GOOSE escaped at (2,4)
- [high] `shed_overflow` game=2824b416ad6c4dd1 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=2824b416ad6c4dd1 step=528 player=0 — GOOSE escaped at (3,0)
- [high] `shed_overflow` game=2824b416ad6c4dd1 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2824b416ad6c4dd1 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2824b416ad6c4dd1 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2824b416ad6c4dd1 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2824b416ad6c4dd1 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2824b416ad6c4dd1 step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2824b416ad6c4dd1 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2824b416ad6c4dd1 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=b908268fb85149d0 step=48 player=1 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=b908268fb85149d0 step=48 player=1 — GOOSE escaped at (4,2)
- [high] `animal_escape` game=b908268fb85149d0 step=48 player=1 — GOOSE escaped at (3,3)
- [high] `animal_escape` game=b908268fb85149d0 step=48 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=b908268fb85149d0 step=48 player=1 — GOOSE escaped at (3,4)
- [high] `animal_escape` game=b908268fb85149d0 step=264 player=0 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=b908268fb85149d0 step=288 player=1 — GOOSE escaped at (2,1)
- [high] `animal_escape` game=b908268fb85149d0 step=288 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=b908268fb85149d0 step=456 player=1 — GOOSE escaped at (2,4)
- [high] `shed_overflow` game=b908268fb85149d0 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=b908268fb85149d0 step=552 player=1 — GOOSE escaped at (3,0)
- [high] `shed_overflow` game=b908268fb85149d0 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b908268fb85149d0 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=b908268fb85149d0 step=600 player=1 — GOOSE escaped at (2,1)
- [high] `shed_overflow` game=b908268fb85149d0 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=36ca4f94ab564a2a step=48 player=1 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=36ca4f94ab564a2a step=48 player=1 — GOOSE escaped at (4,2)
- [high] `animal_escape` game=36ca4f94ab564a2a step=48 player=1 — GOOSE escaped at (3,3)
- [high] `animal_escape` game=36ca4f94ab564a2a step=48 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=36ca4f94ab564a2a step=48 player=1 — GOOSE escaped at (3,4)
- [high] `animal_escape` game=36ca4f94ab564a2a step=264 player=0 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=36ca4f94ab564a2a step=672 player=0 — COW escaped at (6,4)
