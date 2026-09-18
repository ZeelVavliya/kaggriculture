# Batch report: h2h-af60f83c-vs-919fc1d6-671aed

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_carrot | 1.373 | 1739 | 46 | 2 | 2 | 28.4 |
| opp_v43 | -1.373 | 1261 | 2 | 46 | 2 | -28.4 |

## Per-opponent records

### v43_carrot
- vs opp_v43: W46-L2-T2 (win rate 95% CI 84%-98%, n=50), mean margin 28.4

### opp_v43
- vs v43_carrot: W2-L46-T2 (win rate 95% CI 2%-16%, n=50), mean margin -28.4

## Audit findings (ranked by severity)

- **shed_overflow**: 492 occurrences
- **preempted_sell**: 2 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_v43 | shed_overflow | 246 | 4.92 |
| opp_v43 | preempted_sell | 1 | 0.02 |
| v43_carrot | shed_overflow | 246 | 4.92 |
| v43_carrot | preempted_sell | 1 | 0.02 |

Top findings:

- [high] `shed_overflow` game=8399b31a5cce44ab step=456 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=456 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8399b31a5cce44ab step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=beb22293eb4342e8 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=beb22293eb4342e8 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=beb22293eb4342e8 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=beb22293eb4342e8 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=beb22293eb4342e8 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=beb22293eb4342e8 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=beb22293eb4342e8 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=beb22293eb4342e8 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=456 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=456 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=bce0f74b60e4479c step=672 player=1 — shed total=100 >= cap 100 at day boundary

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
