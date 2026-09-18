# Batch report: tourney-0c2f1843

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | W | L | T | mean margin |
|---|---|---|---|---|---|
| c94 | 6.818 | 158 | 2 | 0 | 55327.8 |
| c95 | 4.200 | 122 | 38 | 0 | 55299.9 |
| c92 | 0.927 | 80 | 80 | 0 | 55132.2 |
| main2 | -3.442 | 40 | 120 | 0 | -57168.5 |
| main | -8.503 | 0 | 160 | 0 | -108591.3 |

## Per-opponent records

### c94
- vs main: W40-L0-T0, mean margin 130606.8
- vs main2: W40-L0-T0, mean margin 90418.2
- vs c92: W40-L0-T0, mean margin 225.8
- vs c95: W38-L2-T0, mean margin 60.3

### c95
- vs main: W40-L0-T0, mean margin 130603.8
- vs main2: W40-L0-T0, mean margin 90406.3
- vs c92: W40-L0-T0, mean margin 249.9
- vs c94: W2-L38-T0, mean margin -60.3

### c92
- vs main: W40-L0-T0, mean margin 130603.6
- vs main2: W40-L0-T0, mean margin 90400.7
- vs c94: W0-L40-T0, mean margin -225.8
- vs c95: W0-L40-T0, mean margin -249.9

### main2
- vs main: W40-L0-T0, mean margin 42551.1
- vs c92: W0-L40-T0, mean margin -90400.7
- vs c94: W0-L40-T0, mean margin -90418.2
- vs c95: W0-L40-T0, mean margin -90406.3

### main
- vs main2: W0-L40-T0, mean margin -42551.1
- vs c92: W0-L40-T0, mean margin -130603.6
- vs c94: W0-L40-T0, mean margin -130606.8
- vs c95: W0-L40-T0, mean margin -130603.8

## Audit findings (ranked by severity)

- **premium_preempt**: 8398 occurrences
- **animal_escape**: 1486 occurrences
- **stuck_in_inventory**: 1147 occurrences
- **shed_overflow**: 150 occurrences

Top findings:

- [high] `animal_escape` game=4cb3890777cd452c step=48 player=1 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=4cb3890777cd452c step=48 player=1 — GOOSE escaped at (4,2)
- [high] `animal_escape` game=4cb3890777cd452c step=48 player=1 — GOOSE escaped at (3,3)
- [high] `animal_escape` game=4cb3890777cd452c step=48 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=4cb3890777cd452c step=48 player=1 — GOOSE escaped at (3,4)
- [high] `animal_escape` game=4cb3890777cd452c step=288 player=1 — GOOSE escaped at (2,1)
- [high] `animal_escape` game=4cb3890777cd452c step=288 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=4cb3890777cd452c step=456 player=0 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=4cb3890777cd452c step=456 player=1 — GOOSE escaped at (3,0)
- [high] `animal_escape` game=4cb3890777cd452c step=456 player=1 — GOOSE escaped at (2,1)
- [high] `animal_escape` game=4cb3890777cd452c step=456 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=4cb3890777cd452c step=480 player=0 — COW escaped at (5,3)
- [high] `premium_preempt` game=4cb3890777cd452c step=193 player=0 — player 1 sold FERTILIZER at step 192, player 0 sold same item 1 turn later at step 193
- [high] `premium_preempt` game=4cb3890777cd452c step=217 player=0 — player 1 sold FERTILIZER at step 216, player 0 sold same item 1 turn later at step 217
- [high] `premium_preempt` game=4cb3890777cd452c step=242 player=0 — player 1 sold FERTILIZER at step 241, player 0 sold same item 1 turn later at step 242
- [high] `premium_preempt` game=4cb3890777cd452c step=266 player=0 — player 1 sold FERTILIZER at step 265, player 0 sold same item 1 turn later at step 266
- [high] `premium_preempt` game=4cb3890777cd452c step=290 player=0 — player 1 sold FERTILIZER at step 289, player 0 sold same item 1 turn later at step 290
- [high] `premium_preempt` game=4cb3890777cd452c step=314 player=0 — player 1 sold FERTILIZER at step 313, player 0 sold same item 1 turn later at step 314
- [high] `premium_preempt` game=4cb3890777cd452c step=338 player=0 — player 1 sold FERTILIZER at step 337, player 0 sold same item 1 turn later at step 338
- [high] `premium_preempt` game=4cb3890777cd452c step=697 player=0 — player 1 sold FERTILIZER at step 696, player 0 sold same item 1 turn later at step 697
- [high] `animal_escape` game=1ae35fcff02f4f6d step=48 player=1 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=1ae35fcff02f4f6d step=48 player=1 — GOOSE escaped at (4,2)
- [high] `animal_escape` game=1ae35fcff02f4f6d step=48 player=1 — GOOSE escaped at (3,3)
- [high] `animal_escape` game=1ae35fcff02f4f6d step=48 player=1 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=1ae35fcff02f4f6d step=48 player=1 — GOOSE escaped at (3,4)
- [high] `animal_escape` game=1ae35fcff02f4f6d step=264 player=0 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=1ae35fcff02f4f6d step=288 player=1 — GOOSE escaped at (2,1)
- [high] `animal_escape` game=1ae35fcff02f4f6d step=288 player=1 — GOOSE escaped at (2,4)
- [high] `premium_preempt` game=1ae35fcff02f4f6d step=193 player=0 — player 1 sold FERTILIZER at step 192, player 0 sold same item 1 turn later at step 193
- [high] `premium_preempt` game=1ae35fcff02f4f6d step=217 player=0 — player 1 sold FERTILIZER at step 216, player 0 sold same item 1 turn later at step 217
- [high] `premium_preempt` game=1ae35fcff02f4f6d step=266 player=0 — player 1 sold FERTILIZER at step 265, player 0 sold same item 1 turn later at step 266
- [high] `premium_preempt` game=1ae35fcff02f4f6d step=289 player=1 — player 0 sold FERTILIZER at step 288, player 1 sold same item 1 turn later at step 289
- [high] `premium_preempt` game=1ae35fcff02f4f6d step=290 player=0 — player 1 sold FERTILIZER at step 289, player 0 sold same item 1 turn later at step 290
- [high] `premium_preempt` game=1ae35fcff02f4f6d step=314 player=0 — player 1 sold FERTILIZER at step 313, player 0 sold same item 1 turn later at step 314
- [high] `premium_preempt` game=1ae35fcff02f4f6d step=338 player=0 — player 1 sold FERTILIZER at step 337, player 0 sold same item 1 turn later at step 338
- [high] `premium_preempt` game=1ae35fcff02f4f6d step=696 player=1 — player 0 sold FERTILIZER at step 695, player 1 sold same item 1 turn later at step 696
- [high] `premium_preempt` game=1ae35fcff02f4f6d step=697 player=0 — player 1 sold FERTILIZER at step 696, player 0 sold same item 1 turn later at step 697
- [high] `animal_escape` game=95184f4ba2284731 step=48 player=0 — GOOSE escaped at (3,2)
- [high] `animal_escape` game=95184f4ba2284731 step=48 player=0 — GOOSE escaped at (4,2)
- [high] `animal_escape` game=95184f4ba2284731 step=48 player=0 — GOOSE escaped at (3,3)
