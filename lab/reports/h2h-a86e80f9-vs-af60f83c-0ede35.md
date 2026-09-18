# Batch report: h2h-a86e80f9-vs-af60f83c-0ede35

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_open55 | 3.615 | 2128 | 50 | 0 | 0 | 1268.3 |
| v43_carrot | -3.615 | 872 | 0 | 50 | 0 | -1268.3 |

## Per-opponent records

### v43_open55
- vs v43_carrot: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 1268.3

### v43_carrot
- vs v43_open55: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -1268.3

## Audit findings (ranked by severity)

- **shed_overflow**: 472 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_carrot | shed_overflow | 236 | 4.72 |
| v43_open55 | shed_overflow | 236 | 4.72 |

Top findings:

- [high] `shed_overflow` game=a8030304bd6e4a88 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8030304bd6e4a88 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8030304bd6e4a88 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8030304bd6e4a88 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8030304bd6e4a88 step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8030304bd6e4a88 step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8030304bd6e4a88 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8030304bd6e4a88 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13371e9bdff54440 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13371e9bdff54440 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13371e9bdff54440 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13371e9bdff54440 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13371e9bdff54440 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13371e9bdff54440 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13371e9bdff54440 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13371e9bdff54440 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13371e9bdff54440 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13371e9bdff54440 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bd09db20735a4eda step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bd09db20735a4eda step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bd09db20735a4eda step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bd09db20735a4eda step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bd09db20735a4eda step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bd09db20735a4eda step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bd09db20735a4eda step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bd09db20735a4eda step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d497e808ec4745cf step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d497e808ec4745cf step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d497e808ec4745cf step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d497e808ec4745cf step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d497e808ec4745cf step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d497e808ec4745cf step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=263c3849bba0430a step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=263c3849bba0430a step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=263c3849bba0430a step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=263c3849bba0430a step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=263c3849bba0430a step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=263c3849bba0430a step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=263c3849bba0430a step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=263c3849bba0430a step=672 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**PASS**
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [PASS] vs_incumbent_paired: 46 games better than the incumbent mirror, 0 worse (raw losses 0)
- [PASS] vs_incumbent: raw W-L 50-0, paired regressions 0, over 850000-850024
- [PASS] vs_parent_paired: 47 games better than the parent mirror, 0 worse (raw losses 1)
- [PASS] vs_parent: raw W-L 49-1, paired regressions 0, over 860000-860024
- [INFO] vs_other:v43_carrot: 50-0 over 870000-870024
- [INFO] vs_other:opp_v42: 50-0 over 870000-870024
- [PASS] final_untouched: raw W-L 50-0, paired regressions 0, over 910000-910024
- [PASS] audit: 2431 findings, 0 critical
