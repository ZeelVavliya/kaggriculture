# Batch report: h2h-b0ef1bf9-vs-7b0e5a7b-4f9441

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v41_sellfirst | 3.615 | 2128 | 50 | 0 | 0 | 35319.1 |
| c94 | -3.615 | 872 | 0 | 50 | 0 | -35319.1 |

## Per-opponent records

### v41_sellfirst
- vs c94: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 35319.1

### c94
- vs v41_sellfirst: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -35319.1

## Audit findings (ranked by severity)

- **preempted_sell**: 2681 occurrences
- **shed_overflow**: 188 occurrences
- **animal_escape**: 50 occurrences
- **melon_underyield**: 1 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| c94 | preempted_sell | 1381 | 27.62 |
| c94 | animal_escape | 50 | 1.00 |
| c94 | melon_underyield | 1 | 0.02 |
| v41_sellfirst | preempted_sell | 1300 | 26.00 |
| v41_sellfirst | shed_overflow | 188 | 3.76 |

Top findings:

- [high] `animal_escape` game=711b9447f199436b step=528 player=1 — COW escaped at (7,4)
- [high] `shed_overflow` game=711b9447f199436b step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=711b9447f199436b step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=711b9447f199436b step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=711b9447f199436b step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=4262dc0fba8a49fa step=528 player=0 — COW escaped at (7,4)
- [high] `shed_overflow` game=4262dc0fba8a49fa step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4262dc0fba8a49fa step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4262dc0fba8a49fa step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4262dc0fba8a49fa step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=e66f6e83094b46fb step=528 player=0 — COW escaped at (7,4)
- [high] `shed_overflow` game=e66f6e83094b46fb step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e66f6e83094b46fb step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e66f6e83094b46fb step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e66f6e83094b46fb step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=ce18395715e34ebc step=528 player=1 — COW escaped at (7,4)
- [high] `shed_overflow` game=ce18395715e34ebc step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ce18395715e34ebc step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ce18395715e34ebc step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ce18395715e34ebc step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=8d27644cbfc3464d step=528 player=1 — COW escaped at (7,4)
- [high] `shed_overflow` game=8d27644cbfc3464d step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d27644cbfc3464d step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d27644cbfc3464d step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d27644cbfc3464d step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8d27644cbfc3464d step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=c3945303c26e430a step=528 player=0 — COW escaped at (7,4)
- [high] `shed_overflow` game=c3945303c26e430a step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c3945303c26e430a step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c3945303c26e430a step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c3945303c26e430a step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c3945303c26e430a step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=d1c18a7162ce4f1e step=528 player=1 — COW escaped at (7,4)
- [high] `shed_overflow` game=d1c18a7162ce4f1e step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d1c18a7162ce4f1e step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d1c18a7162ce4f1e step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d1c18a7162ce4f1e step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=55130525841e434d step=528 player=0 — COW escaped at (7,4)
- [high] `shed_overflow` game=55130525841e434d step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=55130525841e434d step=576 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**VETO** — lost to incumbent in 46/50 games (seed_block=850000-850024)
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [VETO] vs_incumbent_paired: 0 games better than the incumbent mirror, 46 worse (raw losses 50)
- [VETO] vs_incumbent: raw W-L 0-50, paired regressions 46, over 850000-850024
- [VETO] vs_parent_paired: 0 games better than the parent mirror, 47 worse (raw losses 49)
- [VETO] vs_parent: raw W-L 1-49, paired regressions 47, over 860000-860024
- [INFO] vs_other:opp_soil: 50-0 over 870000-870024
- [INFO] vs_other:opp_salem2900: 50-0 over 870000-870024
- [INFO] vs_other:c94: 50-0 over 870000-870024
- [INFO] vs_other:v41_rl_1: 0-50 over 870000-870024
- [PASS] audit: 8875 findings, 0 critical
