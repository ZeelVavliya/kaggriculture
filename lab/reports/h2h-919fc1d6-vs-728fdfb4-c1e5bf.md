# Batch report: h2h-919fc1d6-vs-728fdfb4-c1e5bf

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| opp_v43 | 0.523 | 1591 | 25 | 1 | 24 | 70.6 |
| opp_v42 | -0.523 | 1409 | 1 | 25 | 24 | -70.6 |

## Per-opponent records

### opp_v43
- vs opp_v42: W25-L1-T24 (win rate 95% CI 60%-84%, n=50), mean margin 70.6

### opp_v42
- vs opp_v43: W1-L25-T24 (win rate 95% CI 16%-40%, n=50), mean margin -70.6

## Audit findings (ranked by severity)

- **shed_overflow**: 438 occurrences
- **preempted_sell**: 2 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_v42 | shed_overflow | 219 | 4.38 |
| opp_v42 | preempted_sell | 2 | 0.04 |
| opp_v43 | shed_overflow | 219 | 4.38 |

Top findings:

- [high] `shed_overflow` game=12f9b1823934403f step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=12f9b1823934403f step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=12f9b1823934403f step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=12f9b1823934403f step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=12f9b1823934403f step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=12f9b1823934403f step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6cb6c54d6c0442dd step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6cb6c54d6c0442dd step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6cb6c54d6c0442dd step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6cb6c54d6c0442dd step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6cb6c54d6c0442dd step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6cb6c54d6c0442dd step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6cb6c54d6c0442dd step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6cb6c54d6c0442dd step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6cb6c54d6c0442dd step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6cb6c54d6c0442dd step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=92548c25c66c45ab step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=92548c25c66c45ab step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=92548c25c66c45ab step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=92548c25c66c45ab step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=92548c25c66c45ab step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=92548c25c66c45ab step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=92548c25c66c45ab step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=92548c25c66c45ab step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=92548c25c66c45ab step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=92548c25c66c45ab step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1523afd5de40432e step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1523afd5de40432e step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1523afd5de40432e step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1523afd5de40432e step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1523afd5de40432e step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1523afd5de40432e step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e0a91c113c554b91 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e0a91c113c554b91 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e0a91c113c554b91 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e0a91c113c554b91 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e0a91c113c554b91 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e0a91c113c554b91 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e0a91c113c554b91 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e0a91c113c554b91 step=672 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**VETO** — lost to incumbent in 4/50 games (seed_block=850000-850024)
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [VETO] vs_incumbent_paired: 39 games better than the incumbent mirror, 4 worse (raw losses 5)
- [VETO] vs_incumbent: raw W-L 45-5, paired regressions 4, over 850000-850024
- [PASS] vs_parent_paired: 33 games better than the parent mirror, 0 worse (raw losses 1)
- [PASS] vs_parent: raw W-L 49-1, paired regressions 0, over 860000-860024
- [INFO] vs_other:v41_rl_2: 40-10 over 870000-870024
- [INFO] vs_other:opp_v42: 49-1 over 870000-870024
- [INFO] vs_other:opp_soil: 50-0 over 870000-870024
- [PASS] audit: 5712 findings, 0 critical
