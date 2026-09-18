# Batch report: h2h-b0ef1bf9-vs-3b1cb91f-1d0a6a

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v41_sellfirst | 3.615 | 2128 | 50 | 0 | 0 | 30481.3 |
| opp_salem2900 | -3.615 | 872 | 0 | 50 | 0 | -30481.3 |

## Per-opponent records

### v41_sellfirst
- vs opp_salem2900: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 30481.3

### opp_salem2900
- vs v41_sellfirst: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -30481.3

## Audit findings (ranked by severity)

- **preempted_sell**: 2409 occurrences
- **shed_overflow**: 378 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_salem2900 | preempted_sell | 1438 | 28.76 |
| opp_salem2900 | shed_overflow | 183 | 3.66 |
| v41_sellfirst | preempted_sell | 971 | 19.42 |
| v41_sellfirst | shed_overflow | 195 | 3.90 |

Top findings:

- [high] `shed_overflow` game=7ac423b545304631 step=432 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ac423b545304631 step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ac423b545304631 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ac423b545304631 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ac423b545304631 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ac423b545304631 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ac423b545304631 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ac423b545304631 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6f56635600fa4c0b step=432 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6f56635600fa4c0b step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6f56635600fa4c0b step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6f56635600fa4c0b step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6f56635600fa4c0b step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6f56635600fa4c0b step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6f56635600fa4c0b step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=762ac35e323a49ac step=432 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=762ac35e323a49ac step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=762ac35e323a49ac step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=762ac35e323a49ac step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=762ac35e323a49ac step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=762ac35e323a49ac step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=762ac35e323a49ac step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=762ac35e323a49ac step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8f08468f10a14f0c step=432 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8f08468f10a14f0c step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8f08468f10a14f0c step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8f08468f10a14f0c step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8f08468f10a14f0c step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8f08468f10a14f0c step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8f08468f10a14f0c step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8f08468f10a14f0c step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8f08468f10a14f0c step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3260475f3c1d4eb0 step=432 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3260475f3c1d4eb0 step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3260475f3c1d4eb0 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3260475f3c1d4eb0 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3260475f3c1d4eb0 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3260475f3c1d4eb0 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3260475f3c1d4eb0 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3260475f3c1d4eb0 step=624 player=1 — shed total=100 >= cap 100 at day boundary

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
