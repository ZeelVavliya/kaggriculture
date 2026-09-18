# Batch report: h2h-887aaad7-vs-a86e80f9-b2fb0f

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8 | 1.585 | 1775 | 48 | 2 | 0 | 1580.5 |
| v43_open55 | -1.585 | 1225 | 2 | 48 | 0 | -1580.5 |

## Per-opponent records

### v43_lead8
- vs v43_open55: W48-L2-T0 (win rate 95% CI 87%-99%, n=50), mean margin 1580.5

### v43_open55
- vs v43_lead8: W2-L48-T0 (win rate 95% CI 1%-13%, n=50), mean margin -1580.5

## Audit findings (ranked by severity)

- **shed_overflow**: 486 occurrences
- **preempted_sell**: 296 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8 | shed_overflow | 243 | 4.86 |
| v43_lead8 | preempted_sell | 126 | 2.52 |
| v43_open55 | shed_overflow | 243 | 4.86 |
| v43_open55 | preempted_sell | 170 | 3.40 |

Top findings:

- [high] `shed_overflow` game=b41e527e14cb4eef step=456 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=456 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b41e527e14cb4eef step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8a71a03c135a46ac step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8a71a03c135a46ac step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8a71a03c135a46ac step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8a71a03c135a46ac step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8a71a03c135a46ac step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8a71a03c135a46ac step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8a71a03c135a46ac step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8a71a03c135a46ac step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4204cea4d6cc4476 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4204cea4d6cc4476 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4204cea4d6cc4476 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4204cea4d6cc4476 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4204cea4d6cc4476 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=4204cea4d6cc4476 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=25e292da00624ad4 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=25e292da00624ad4 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=25e292da00624ad4 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=25e292da00624ad4 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=25e292da00624ad4 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=25e292da00624ad4 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=25e292da00624ad4 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=25e292da00624ad4 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=25e292da00624ad4 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=25e292da00624ad4 step=600 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**PASS**
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [PASS] vs_incumbent_paired: 45 games better than the incumbent mirror, 0 worse (raw losses 1)
- [PASS] vs_incumbent: raw W-L 49-1, paired regressions 0, over 850000-850024
- [PASS] vs_parent_paired: 46 games better than the parent mirror, 0 worse (raw losses 2)
- [PASS] vs_parent: raw W-L 48-2, paired regressions 0, over 860000-860024
- [INFO] vs_other:v43_lead6: 50-0 over 870000-870024
- [INFO] vs_other:opp_v43: 50-0 over 870000-870024
- [PASS] final_untouched: raw W-L 50-0, paired regressions 0, over 910000-910024
- [PASS] audit: 3900 findings, 0 critical
