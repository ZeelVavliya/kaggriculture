# Batch report: h2h-a86e80f9-vs-919fc1d6-c4d2db

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_open55 | 3.615 | 2128 | 50 | 0 | 0 | 1335.6 |
| opp_v43 | -3.615 | 872 | 0 | 50 | 0 | -1335.6 |

## Per-opponent records

### v43_open55
- vs opp_v43: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 1335.6

### opp_v43
- vs v43_open55: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -1335.6

## Audit findings (ranked by severity)

- **shed_overflow**: 504 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_v43 | shed_overflow | 252 | 5.04 |
| v43_open55 | shed_overflow | 252 | 5.04 |

Top findings:

- [high] `shed_overflow` game=b608f640b11c4e51 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b608f640b11c4e51 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=039abf41f06b4a46 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8e27b64c72894c3f step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10e16e8b51814c31 step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10e16e8b51814c31 step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10e16e8b51814c31 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10e16e8b51814c31 step=528 player=1 — shed total=100 >= cap 100 at day boundary

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
