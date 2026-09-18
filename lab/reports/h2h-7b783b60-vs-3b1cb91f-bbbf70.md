# Batch report: h2h-7b783b60-vs-3b1cb91f-bbbf70

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v41_rl_1 | 3.615 | 2128 | 50 | 0 | 0 | 34925.4 |
| opp_salem2900 | -3.615 | 872 | 0 | 50 | 0 | -34925.4 |

## Per-opponent records

### v41_rl_1
- vs opp_salem2900: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 34925.4

### opp_salem2900
- vs v41_rl_1: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -34925.4

## Audit findings (ranked by severity)

- **preempted_sell**: 2475 occurrences
- **shed_overflow**: 394 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_salem2900 | preempted_sell | 1456 | 29.12 |
| opp_salem2900 | shed_overflow | 194 | 3.88 |
| v41_rl_1 | preempted_sell | 1019 | 20.38 |
| v41_rl_1 | shed_overflow | 200 | 4.00 |

Top findings:

- [high] `shed_overflow` game=13237636cad244c9 step=432 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13237636cad244c9 step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13237636cad244c9 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13237636cad244c9 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13237636cad244c9 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13237636cad244c9 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13237636cad244c9 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13237636cad244c9 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=13237636cad244c9 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18bd9ab5def34dc5 step=432 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18bd9ab5def34dc5 step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18bd9ab5def34dc5 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18bd9ab5def34dc5 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=18bd9ab5def34dc5 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=82231aee0fc84df8 step=432 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=82231aee0fc84df8 step=480 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=82231aee0fc84df8 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=82231aee0fc84df8 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=82231aee0fc84df8 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=82231aee0fc84df8 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=82231aee0fc84df8 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=82231aee0fc84df8 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=82231aee0fc84df8 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58b3c98b78cd4c91 step=432 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58b3c98b78cd4c91 step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58b3c98b78cd4c91 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58b3c98b78cd4c91 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58b3c98b78cd4c91 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58b3c98b78cd4c91 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58b3c98b78cd4c91 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58b3c98b78cd4c91 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58b3c98b78cd4c91 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0ba9396061964321 step=432 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0ba9396061964321 step=480 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0ba9396061964321 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0ba9396061964321 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0ba9396061964321 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0ba9396061964321 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0ba9396061964321 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0ba9396061964321 step=624 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**PASS**
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [PASS] vs_incumbent_paired: 42 games better than the incumbent mirror, 0 worse (raw losses 4)
- [PASS] vs_incumbent: 50-0 over 850000-850024
- [PASS] vs_parent_paired: 45 games better than the parent mirror, 0 worse (raw losses 1)
- [PASS] vs_parent: 50-0 over 860000-860024
- [INFO] vs_other:opp_soil: 50-0 over 870000-870024
- [INFO] vs_other:opp_salem2900: 50-0 over 870000-870024
- [INFO] vs_other:c94: 50-0 over 870000-870024
- [PASS] final_untouched: 50-0 over 910000-910024
- [PASS] audit: 8997 findings, 0 critical
