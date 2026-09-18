# Batch report: h2h-b1bad7f3-vs-02b1fee4-ee4f75

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v41_fertfirst | 3.615 | 2128 | 50 | 0 | 0 | 5724.1 |
| opp_soil | -3.615 | 872 | 0 | 50 | 0 | -5724.1 |

## Per-opponent records

### v41_fertfirst
- vs opp_soil: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 5724.1

### opp_soil
- vs v41_fertfirst: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -5724.1

## Audit findings (ranked by severity)

- **preempted_sell**: 1409 occurrences
- **shed_overflow**: 309 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_soil | preempted_sell | 437 | 8.74 |
| opp_soil | shed_overflow | 70 | 1.40 |
| v41_fertfirst | preempted_sell | 972 | 19.44 |
| v41_fertfirst | shed_overflow | 239 | 4.78 |

Top findings:

- [high] `shed_overflow` game=5e3763565eaa4aad step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e3763565eaa4aad step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e3763565eaa4aad step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e3763565eaa4aad step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e3763565eaa4aad step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e3763565eaa4aad step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e3763565eaa4aad step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e98b4167e0004ae2 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e98b4167e0004ae2 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e98b4167e0004ae2 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e98b4167e0004ae2 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e98b4167e0004ae2 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e98b4167e0004ae2 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e98b4167e0004ae2 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e98b4167e0004ae2 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5c2f0507326d417b step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5c2f0507326d417b step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5c2f0507326d417b step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5c2f0507326d417b step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5c2f0507326d417b step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5c2f0507326d417b step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5c2f0507326d417b step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1a9e5b82599e44ee step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1a9e5b82599e44ee step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1a9e5b82599e44ee step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1a9e5b82599e44ee step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1a9e5b82599e44ee step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1a9e5b82599e44ee step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1a9e5b82599e44ee step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a02a237e051a4531 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a02a237e051a4531 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a02a237e051a4531 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a02a237e051a4531 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a02a237e051a4531 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a02a237e051a4531 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f637cb976cfd4072 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f637cb976cfd4072 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f637cb976cfd4072 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f637cb976cfd4072 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f637cb976cfd4072 step=624 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**VETO** — lost to incumbent in 45/50 games (seed_block=850000-850024)
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [VETO] vs_incumbent_paired: 0 games better than the incumbent mirror, 45 worse (raw losses 49)
- [VETO] vs_incumbent: raw W-L 1-49, paired regressions 45, over 850000-850024
- [VETO] vs_parent_paired: 0 games better than the parent mirror, 47 worse (raw losses 49)
- [VETO] vs_parent: raw W-L 1-49, paired regressions 47, over 860000-860024
- [INFO] vs_other:opp_soil: 50-0 over 870000-870024
- [INFO] vs_other:v41_rl_1: 0-50 over 870000-870024
- [PASS] audit: 3136 findings, 0 critical
