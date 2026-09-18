# Batch report: h2h-489f5d19-vs-0c2bffea-cbdc12

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| c95 | 2.917 | 2007 | 10 | 0 | 0 | 77888.9 |
| main2 | -2.917 | 993 | 0 | 10 | 0 | -77888.9 |

## Per-opponent records

### c95
- vs main2: W10-L0-T0, mean margin 77888.9

### main2
- vs c95: W0-L10-T0, mean margin -77888.9

## Audit findings (ranked by severity)

- **preempted_sell**: 251 occurrences
- **stuck_in_inventory**: 29 occurrences
- **melon_underyield**: 13 occurrences
- **animal_escape**: 11 occurrences
- **shed_overflow**: 5 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| c95 | preempted_sell | 32 | 3.20 |
| c95 | animal_escape | 10 | 1.00 |
| main2 | preempted_sell | 219 | 21.90 |
| main2 | stuck_in_inventory | 29 | 2.90 |
| main2 | melon_underyield | 13 | 1.30 |
| main2 | shed_overflow | 5 | 0.50 |
| main2 | animal_escape | 1 | 0.10 |

Top findings:

- [high] `animal_escape` game=e57d2f74bea54baf step=528 player=1 — COW escaped at (7,4)
- [high] `animal_escape` game=3a9467aebad04982 step=528 player=0 — COW escaped at (7,4)
- [high] `shed_overflow` game=3a9467aebad04982 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=9b563acfd29d4943 step=528 player=0 — COW escaped at (7,4)
- [high] `animal_escape` game=863da1fb68bd4b24 step=528 player=0 — COW escaped at (7,4)
- [high] `animal_escape` game=b424450b1bbd4cff step=480 player=0 — GOOSE escaped at (2,4)
- [high] `animal_escape` game=b424450b1bbd4cff step=528 player=1 — COW escaped at (7,4)
- [high] `animal_escape` game=0563e077266747fc step=528 player=1 — COW escaped at (7,4)
- [high] `animal_escape` game=eca676de073b4e9f step=528 player=0 — COW escaped at (7,4)
- [high] `shed_overflow` game=eca676de073b4e9f step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=05214a223b964e83 step=528 player=1 — COW escaped at (7,4)
- [high] `animal_escape` game=90e9e324b9854155 step=528 player=0 — COW escaped at (7,4)
- [high] `shed_overflow` game=90e9e324b9854155 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=427974a9cd89402a step=528 player=1 — COW escaped at (7,4)
- [high] `shed_overflow` game=427974a9cd89402a step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=427974a9cd89402a step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [medium] `melon_underyield` game=e57d2f74bea54baf step=216 player=0 — melon at (1, 4) left the field with yield 2 < 6
- [medium] `stuck_in_inventory` game=e57d2f74bea54baf step=719 player=0 — unit 0 holds 6x EGG at terminal, never DROPped
- [medium] `stuck_in_inventory` game=e57d2f74bea54baf step=719 player=0 — unit 0 holds 3x FERTILIZER at terminal, never DROPped
- [medium] `stuck_in_inventory` game=e57d2f74bea54baf step=719 player=0 — unit 0 holds 2x WHEAT at terminal, never DROPped
- [medium] `preempted_sell` game=e57d2f74bea54baf step=218 player=0 — opponent sold FERTILIZER at step 217, we started selling at 218
- [medium] `preempted_sell` game=e57d2f74bea54baf step=242 player=0 — opponent sold FERTILIZER at step 241, we started selling at 242
- [medium] `preempted_sell` game=e57d2f74bea54baf step=290 player=0 — opponent sold FERTILIZER at step 289, we started selling at 290
- [medium] `preempted_sell` game=e57d2f74bea54baf step=314 player=0 — opponent sold FERTILIZER at step 313, we started selling at 314
- [medium] `preempted_sell` game=e57d2f74bea54baf step=338 player=0 — opponent sold FERTILIZER at step 337, we started selling at 338
- [medium] `preempted_sell` game=e57d2f74bea54baf step=362 player=0 — opponent sold FERTILIZER at step 361, we started selling at 362
- [medium] `preempted_sell` game=e57d2f74bea54baf step=433 player=0 — opponent sold FERTILIZER at step 432, we started selling at 433
- [medium] `preempted_sell` game=e57d2f74bea54baf step=458 player=0 — opponent sold FERTILIZER at step 457, we started selling at 458
- [medium] `preempted_sell` game=e57d2f74bea54baf step=554 player=0 — opponent sold FERTILIZER at step 553, we started selling at 554
- [medium] `preempted_sell` game=e57d2f74bea54baf step=577 player=0 — opponent sold FERTILIZER at step 576, we started selling at 577
- [medium] `preempted_sell` game=e57d2f74bea54baf step=602 player=0 — opponent sold FERTILIZER at step 601, we started selling at 602
- [medium] `preempted_sell` game=e57d2f74bea54baf step=626 player=0 — opponent sold FERTILIZER at step 625, we started selling at 626
- [medium] `preempted_sell` game=e57d2f74bea54baf step=650 player=0 — opponent sold FERTILIZER at step 649, we started selling at 650
- [medium] `preempted_sell` game=e57d2f74bea54baf step=674 player=0 — opponent sold FERTILIZER at step 673, we started selling at 674
- [medium] `preempted_sell` game=e57d2f74bea54baf step=360 player=1 — opponent sold FERTILIZER at step 359, we started selling at 360
- [medium] `preempted_sell` game=e57d2f74bea54baf step=674 player=0 — opponent sold WHEAT at step 673, we started selling at 674
- [medium] `preempted_sell` game=e57d2f74bea54baf step=717 player=0 — opponent sold WHEAT at step 716, we started selling at 717
- [medium] `preempted_sell` game=e57d2f74bea54baf step=719 player=0 — opponent sold WHEAT at step 718, we started selling at 719
- [medium] `preempted_sell` game=e57d2f74bea54baf step=314 player=0 — opponent sold WOOL at step 313, we started selling at 314
- [medium] `preempted_sell` game=e57d2f74bea54baf step=674 player=0 — opponent sold WOOL at step 673, we started selling at 674

## Gate verdict

**VETO** — lost to incumbent in 10/10 games (seed_block=850000-850004)
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [VETO] vs_incumbent: 0-10 over 850000-850004
- [VETO] vs_parent: 0-10 over 860000-860004
- [INFO] vs_other:main2: 10-0 over 870000-870004
- [INFO] vs_other:c92: 10-0 over 870000-870004
- [PASS] audit: 1781 findings, 0 critical
