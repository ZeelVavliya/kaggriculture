# Batch report: h2h-af60f83c-vs-919fc1d6-39f1cf

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_carrot | 1.097 | 1691 | 41 | 1 | 8 | 17.2 |
| opp_v43 | -1.097 | 1309 | 1 | 41 | 8 | -17.2 |

## Per-opponent records

### v43_carrot
- vs opp_v43: W41-L1-T8 (win rate 95% CI 79%-96%, n=50), mean margin 17.2

### opp_v43
- vs v43_carrot: W1-L41-T8 (win rate 95% CI 4%-21%, n=50), mean margin -17.2

## Audit findings (ranked by severity)

- **shed_overflow**: 452 occurrences
- **preempted_sell**: 2 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_v43 | shed_overflow | 226 | 4.52 |
| opp_v43 | preempted_sell | 1 | 0.02 |
| v43_carrot | shed_overflow | 226 | 4.52 |
| v43_carrot | preempted_sell | 1 | 0.02 |

Top findings:

- [high] `shed_overflow` game=46c92e1eb9aa463c step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=46c92e1eb9aa463c step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=46c92e1eb9aa463c step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=46c92e1eb9aa463c step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=46c92e1eb9aa463c step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=46c92e1eb9aa463c step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d6c5a591f0634b27 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d6c5a591f0634b27 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d6c5a591f0634b27 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d6c5a591f0634b27 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d6c5a591f0634b27 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d6c5a591f0634b27 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d2aa277a32f4de3 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d8ef1b52b8b34118 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20267c8d77fa42e5 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20267c8d77fa42e5 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20267c8d77fa42e5 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=20267c8d77fa42e5 step=552 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**PASS**
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [PASS] vs_incumbent_paired: 42 games better than the incumbent mirror, 0 worse (raw losses 4)
- [PASS] vs_incumbent: raw W-L 46-4, paired regressions 0, over 850000-850024
- [PASS] vs_parent_paired: 44 games better than the parent mirror, 0 worse (raw losses 2)
- [PASS] vs_parent: raw W-L 48-2, paired regressions 0, over 860000-860024
- [INFO] vs_other:opp_v42: 49-1 over 870000-870024
- [INFO] vs_other:v41_rl_2: 42-8 over 870000-870024
- [PASS] final_untouched: raw W-L 49-1, paired regressions 0, over 910000-910024
- [PASS] audit: 2922 findings, 0 critical
