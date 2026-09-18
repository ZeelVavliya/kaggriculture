# Batch report: tourney-0a651d40

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| c94 | 9.011 | 3065 | 158 | 2 | 0 | 55327.8 |
| c95 | 6.112 | 2562 | 122 | 38 | 0 | 55299.9 |
| c92 | 0.552 | 1596 | 80 | 80 | 0 | 55132.2 |
| main2 | -4.916 | 646 | 40 | 120 | 0 | -57168.5 |
| main | -10.759 | -369 | 0 | 160 | 0 | -108591.3 |

## Per-opponent records

### c94
- vs main: W40-L0-T0 (win rate 95% CI 91%-100%, n=40), mean margin 130606.8
- vs main2: W40-L0-T0 (win rate 95% CI 91%-100%, n=40), mean margin 90418.2
- vs c92: W40-L0-T0 (win rate 95% CI 91%-100%, n=40), mean margin 225.8
- vs c95: W38-L2-T0 (win rate 95% CI 83%-99%, n=40), mean margin 60.3

### c95
- vs main: W40-L0-T0 (win rate 95% CI 91%-100%, n=40), mean margin 130603.8
- vs main2: W40-L0-T0 (win rate 95% CI 91%-100%, n=40), mean margin 90406.3
- vs c92: W40-L0-T0 (win rate 95% CI 91%-100%, n=40), mean margin 249.9
- vs c94: W2-L38-T0 (win rate 95% CI 1%-17%, n=40), mean margin -60.3

### c92
- vs main: W40-L0-T0 (win rate 95% CI 91%-100%, n=40), mean margin 130603.6
- vs main2: W40-L0-T0 (win rate 95% CI 91%-100%, n=40), mean margin 90400.7
- vs c94: W0-L40-T0 (win rate 95% CI 0%-9%, n=40), mean margin -225.8
- vs c95: W0-L40-T0 (win rate 95% CI 0%-9%, n=40), mean margin -249.9

### main2
- vs main: W40-L0-T0 (win rate 95% CI 91%-100%, n=40), mean margin 42551.1
- vs c92: W0-L40-T0 (win rate 95% CI 0%-9%, n=40), mean margin -90400.7
- vs c94: W0-L40-T0 (win rate 95% CI 0%-9%, n=40), mean margin -90418.2
- vs c95: W0-L40-T0 (win rate 95% CI 0%-9%, n=40), mean margin -90406.3

### main
- vs main2: W0-L40-T0 (win rate 95% CI 0%-9%, n=40), mean margin -42551.1
- vs c92: W0-L40-T0 (win rate 95% CI 0%-9%, n=40), mean margin -130603.6
- vs c94: W0-L40-T0 (win rate 95% CI 0%-9%, n=40), mean margin -130606.8
- vs c95: W0-L40-T0 (win rate 95% CI 0%-9%, n=40), mean margin -130603.8

## Audit findings (ranked by severity)

- **preempted_sell**: 10497 occurrences
- **animal_escape**: 1486 occurrences
- **stuck_in_inventory**: 1147 occurrences
- **melon_underyield**: 229 occurrences
- **shed_overflow**: 150 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| c92 | preempted_sell | 3488 | 21.80 |
| c92 | animal_escape | 160 | 1.00 |
| c94 | preempted_sell | 1844 | 11.53 |
| c94 | animal_escape | 160 | 1.00 |
| c95 | preempted_sell | 918 | 5.74 |
| c95 | animal_escape | 160 | 1.00 |
| main | preempted_sell | 1095 | 6.84 |
| main | animal_escape | 956 | 5.97 |
| main | stuck_in_inventory | 640 | 4.00 |
| main | shed_overflow | 57 | 0.36 |
| main2 | preempted_sell | 3152 | 19.70 |
| main2 | stuck_in_inventory | 507 | 3.17 |
| main2 | melon_underyield | 229 | 1.43 |
| main2 | shed_overflow | 93 | 0.58 |
| main2 | animal_escape | 50 | 0.31 |

Top findings:

- [high] `animal_escape` game=2195c0e7db66459a step=48 player=0 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=2195c0e7db66459a step=48 player=0 — GOOSE escaped at (4,2)
- [high] `animal_escape` game=2195c0e7db66459a step=48 player=0 — GOOSE escaped at (3,3)
- [high] `animal_escape` game=2195c0e7db66459a step=48 player=0 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=2195c0e7db66459a step=48 player=0 — GOOSE escaped at (3,4)
- [high] `animal_escape` game=2195c0e7db66459a step=264 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=280d06b46c2d442f step=48 player=1 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=280d06b46c2d442f step=48 player=1 — GOOSE escaped at (4,2)
- [high] `animal_escape` game=280d06b46c2d442f step=48 player=1 — GOOSE escaped at (3,3)
- [high] `animal_escape` game=280d06b46c2d442f step=48 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=280d06b46c2d442f step=48 player=1 — GOOSE escaped at (3,4)
- [high] `animal_escape` game=280d06b46c2d442f step=264 player=0 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=d31b139f58264191 step=48 player=1 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=d31b139f58264191 step=48 player=1 — GOOSE escaped at (4,2)
- [high] `animal_escape` game=d31b139f58264191 step=48 player=1 — GOOSE escaped at (3,3)
- [high] `animal_escape` game=d31b139f58264191 step=48 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=d31b139f58264191 step=48 player=1 — GOOSE escaped at (3,4)
- [high] `animal_escape` game=d31b139f58264191 step=264 player=0 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=d31b139f58264191 step=288 player=1 — GOOSE escaped at (2,1)
- [high] `animal_escape` game=d31b139f58264191 step=288 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=20d3a44d69be4ce6 step=48 player=1 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=20d3a44d69be4ce6 step=48 player=1 — GOOSE escaped at (4,2)
- [high] `animal_escape` game=20d3a44d69be4ce6 step=48 player=1 — GOOSE escaped at (3,3)
- [high] `animal_escape` game=20d3a44d69be4ce6 step=48 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=20d3a44d69be4ce6 step=48 player=1 — GOOSE escaped at (3,4)
- [high] `animal_escape` game=20d3a44d69be4ce6 step=288 player=1 — GOOSE escaped at (2,1)
- [high] `animal_escape` game=20d3a44d69be4ce6 step=288 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=20d3a44d69be4ce6 step=360 player=0 — GOOSE escaped at (2,4)
- [high] `shed_overflow` game=20d3a44d69be4ce6 step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20d3a44d69be4ce6 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20d3a44d69be4ce6 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20d3a44d69be4ce6 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20d3a44d69be4ce6 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20d3a44d69be4ce6 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20d3a44d69be4ce6 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20d3a44d69be4ce6 step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20d3a44d69be4ce6 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20d3a44d69be4ce6 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=26f15b7f50f64852 step=48 player=1 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=26f15b7f50f64852 step=48 player=1 — GOOSE escaped at (4,2)
