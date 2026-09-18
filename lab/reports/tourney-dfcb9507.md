# Batch report: tourney-dfcb9507

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_open3_carrot | 3.553 | 2117 | 116 | 4 | 0 | 11150.1 |
| v43_lead8_open3 | 1.388 | 1741 | 86 | 34 | 0 | 11143.9 |
| v43_lead8 | -0.101 | 1482 | 60 | 60 | 0 | 36827.2 |
| v43_open55 | -1.749 | 1196 | 30 | 90 | 0 | 35183.9 |
| d45c4da0 | -3.091 | 963 | 8 | 112 | 0 | -94305.0 |

## Per-opponent records

### v43_open3_carrot
- vs d45c4da0: W26-L4-T0 (win rate 95% CI 70%-95%, n=30), mean margin 42789.2
- vs v43_open55: W30-L0-T0 (win rate 95% CI 89%-100%, n=30), mean margin 1749.4
- vs v43_lead8: W30-L0-T0 (win rate 95% CI 89%-100%, n=30), mean margin 48.2
- vs v43_lead8_open3: W30-L0-T0 (win rate 95% CI 89%-100%, n=30), mean margin 13.5

### v43_lead8_open3
- vs d45c4da0: W26-L4-T0 (win rate 95% CI 70%-95%, n=30), mean margin 42805.5
- vs v43_open55: W30-L0-T0 (win rate 95% CI 89%-100%, n=30), mean margin 1748.9
- vs v43_lead8: W30-L0-T0 (win rate 95% CI 89%-100%, n=30), mean margin 34.7
- vs v43_open3_carrot: W0-L30-T0 (win rate 95% CI 0%-11%, n=30), mean margin -13.5

### v43_lead8
- vs d45c4da0: W30-L0-T0 (win rate 95% CI 89%-100%, n=30), mean margin 145677.5
- vs v43_open55: W30-L0-T0 (win rate 95% CI 89%-100%, n=30), mean margin 1714.2
- vs v43_open3_carrot: W0-L30-T0 (win rate 95% CI 0%-11%, n=30), mean margin -48.2
- vs v43_lead8_open3: W0-L30-T0 (win rate 95% CI 0%-11%, n=30), mean margin -34.7

### v43_open55
- vs d45c4da0: W30-L0-T0 (win rate 95% CI 89%-100%, n=30), mean margin 145948.0
- vs v43_lead8: W0-L30-T0 (win rate 95% CI 0%-11%, n=30), mean margin -1714.2
- vs v43_open3_carrot: W0-L30-T0 (win rate 95% CI 0%-11%, n=30), mean margin -1749.4
- vs v43_lead8_open3: W0-L30-T0 (win rate 95% CI 0%-11%, n=30), mean margin -1748.9

### d45c4da0
- vs v43_open55: W0-L30-T0 (win rate 95% CI 0%-11%, n=30), mean margin -145948.0
- vs v43_lead8: W0-L30-T0 (win rate 95% CI 0%-11%, n=30), mean margin -145677.5
- vs v43_open3_carrot: W4-L26-T0 (win rate 95% CI 5%-30%, n=30), mean margin -42789.2
- vs v43_lead8_open3: W4-L26-T0 (win rate 95% CI 5%-30%, n=30), mean margin -42805.5

## Audit findings (ranked by severity)

- **preempted_sell**: 13470 occurrences
- **shed_overflow**: 2178 occurrences
- **animal_escape**: 628 occurrences
- **melon_underyield**: 360 occurrences
- **stuck_in_inventory**: 102 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| d45c4da0 | preempted_sell | 7094 | 59.12 |
| d45c4da0 | animal_escape | 628 | 5.23 |
| d45c4da0 | melon_underyield | 360 | 3.00 |
| d45c4da0 | stuck_in_inventory | 102 | 0.85 |
| d45c4da0 | shed_overflow | 70 | 0.58 |
| v43_lead8 | preempted_sell | 1537 | 12.81 |
| v43_lead8 | shed_overflow | 490 | 4.08 |
| v43_lead8_open3 | preempted_sell | 1563 | 13.03 |
| v43_lead8_open3 | shed_overflow | 563 | 4.69 |
| v43_open3_carrot | preempted_sell | 1563 | 13.03 |
| v43_open3_carrot | shed_overflow | 563 | 4.69 |
| v43_open55 | preempted_sell | 1713 | 14.28 |
| v43_open55 | shed_overflow | 492 | 4.10 |

Top findings:

- [high] `animal_escape` game=c74a3f4d2f804d95 step=48 player=0 — COW escaped at (4,2)
- [high] `animal_escape` game=c74a3f4d2f804d95 step=120 player=0 — SHEEP escaped at (2,4)
- [high] `animal_escape` game=c74a3f4d2f804d95 step=120 player=0 — COW escaped at (4,4)
- [high] `animal_escape` game=c74a3f4d2f804d95 step=240 player=0 — SHEEP escaped at (4,3)
- [high] `animal_escape` game=c74a3f4d2f804d95 step=312 player=0 — COW escaped at (5,3)
- [high] `animal_escape` game=c74a3f4d2f804d95 step=312 player=0 — SHEEP escaped at (3,4)
- [high] `shed_overflow` game=c74a3f4d2f804d95 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c74a3f4d2f804d95 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c74a3f4d2f804d95 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c74a3f4d2f804d95 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c74a3f4d2f804d95 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=af77f48e19fe48e9 step=48 player=1 — COW escaped at (4,2)
- [high] `animal_escape` game=af77f48e19fe48e9 step=120 player=1 — SHEEP escaped at (2,4)
- [high] `animal_escape` game=af77f48e19fe48e9 step=120 player=1 — COW escaped at (4,4)
- [high] `animal_escape` game=af77f48e19fe48e9 step=240 player=1 — SHEEP escaped at (4,3)
- [high] `animal_escape` game=af77f48e19fe48e9 step=312 player=1 — COW escaped at (5,3)
- [high] `animal_escape` game=af77f48e19fe48e9 step=312 player=1 — SHEEP escaped at (3,4)
- [high] `shed_overflow` game=af77f48e19fe48e9 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=af77f48e19fe48e9 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=af77f48e19fe48e9 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=af77f48e19fe48e9 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=af77f48e19fe48e9 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=9015c727c70c4282 step=48 player=0 — COW escaped at (4,2)
- [high] `animal_escape` game=9015c727c70c4282 step=120 player=0 — SHEEP escaped at (2,4)
- [high] `animal_escape` game=9015c727c70c4282 step=120 player=0 — COW escaped at (4,4)
- [high] `animal_escape` game=9015c727c70c4282 step=240 player=0 — SHEEP escaped at (4,3)
- [high] `animal_escape` game=9015c727c70c4282 step=312 player=0 — COW escaped at (5,3)
- [high] `animal_escape` game=9015c727c70c4282 step=312 player=0 — SHEEP escaped at (3,4)
- [high] `shed_overflow` game=9015c727c70c4282 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=80d4b58d18bf4e20 step=48 player=1 — COW escaped at (4,2)
- [high] `animal_escape` game=80d4b58d18bf4e20 step=120 player=1 — SHEEP escaped at (2,4)
- [high] `animal_escape` game=80d4b58d18bf4e20 step=120 player=1 — COW escaped at (4,4)
- [high] `animal_escape` game=80d4b58d18bf4e20 step=240 player=1 — SHEEP escaped at (4,3)
- [high] `animal_escape` game=80d4b58d18bf4e20 step=312 player=1 — COW escaped at (5,3)
- [high] `animal_escape` game=80d4b58d18bf4e20 step=312 player=1 — SHEEP escaped at (3,4)
- [high] `shed_overflow` game=80d4b58d18bf4e20 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=35586874f4e74830 step=48 player=0 — COW escaped at (4,2)
- [high] `animal_escape` game=35586874f4e74830 step=120 player=0 — SHEEP escaped at (2,4)
- [high] `animal_escape` game=35586874f4e74830 step=120 player=0 — COW escaped at (4,4)
- [high] `animal_escape` game=35586874f4e74830 step=216 player=0 — SHEEP escaped at (6,4)
