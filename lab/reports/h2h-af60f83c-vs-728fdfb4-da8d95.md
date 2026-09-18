# Batch report: h2h-af60f83c-vs-728fdfb4-da8d95

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_carrot | 1.936 | 1836 | 49 | 1 | 0 | 89.7 |
| opp_v42 | -1.936 | 1164 | 1 | 49 | 0 | -89.7 |

## Per-opponent records

### v43_carrot
- vs opp_v42: W49-L1-T0 (win rate 95% CI 90%-100%, n=50), mean margin 89.7

### opp_v42
- vs v43_carrot: W1-L49-T0 (win rate 95% CI 0%-10%, n=50), mean margin -89.7

## Audit findings (ranked by severity)

- **shed_overflow**: 438 occurrences
- **preempted_sell**: 2 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_v42 | shed_overflow | 219 | 4.38 |
| opp_v42 | preempted_sell | 2 | 0.04 |
| v43_carrot | shed_overflow | 219 | 4.38 |

Top findings:

- [high] `shed_overflow` game=3d7b67424f2740de step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d7b67424f2740de step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d7b67424f2740de step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3d7b67424f2740de step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b826cc2e80854a44 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b826cc2e80854a44 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b826cc2e80854a44 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b826cc2e80854a44 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b826cc2e80854a44 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b826cc2e80854a44 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b826cc2e80854a44 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b826cc2e80854a44 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b826cc2e80854a44 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b826cc2e80854a44 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=62a9c23508b04ae9 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=62a9c23508b04ae9 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=62a9c23508b04ae9 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=62a9c23508b04ae9 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=62a9c23508b04ae9 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=62a9c23508b04ae9 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=62a9c23508b04ae9 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=62a9c23508b04ae9 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=62a9c23508b04ae9 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=62a9c23508b04ae9 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=22351e76067545c2 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=22351e76067545c2 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=22351e76067545c2 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=22351e76067545c2 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=22351e76067545c2 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=22351e76067545c2 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=51427514ddee46e2 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=51427514ddee46e2 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=51427514ddee46e2 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=51427514ddee46e2 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=51427514ddee46e2 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=51427514ddee46e2 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=506376bc205047e4 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=506376bc205047e4 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=506376bc205047e4 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=506376bc205047e4 step=672 player=1 — shed total=100 >= cap 100 at day boundary

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
