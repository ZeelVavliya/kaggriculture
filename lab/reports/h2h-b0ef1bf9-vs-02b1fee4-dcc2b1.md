# Batch report: h2h-b0ef1bf9-vs-02b1fee4-dcc2b1

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v41_sellfirst | 3.615 | 2128 | 50 | 0 | 0 | 6003.6 |
| opp_soil | -3.615 | 872 | 0 | 50 | 0 | -6003.6 |

## Per-opponent records

### v41_sellfirst
- vs opp_soil: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 6003.6

### opp_soil
- vs v41_sellfirst: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -6003.6

## Audit findings (ranked by severity)

- **preempted_sell**: 1462 occurrences
- **shed_overflow**: 323 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_soil | preempted_sell | 465 | 9.30 |
| opp_soil | shed_overflow | 84 | 1.68 |
| v41_sellfirst | preempted_sell | 997 | 19.94 |
| v41_sellfirst | shed_overflow | 239 | 4.78 |

Top findings:

- [high] `shed_overflow` game=1384988431f64ce6 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1384988431f64ce6 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1384988431f64ce6 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1384988431f64ce6 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1384988431f64ce6 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1384988431f64ce6 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=1384988431f64ce6 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5af1b330e8364de7 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5af1b330e8364de7 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5af1b330e8364de7 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5af1b330e8364de7 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5af1b330e8364de7 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5af1b330e8364de7 step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5af1b330e8364de7 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5af1b330e8364de7 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5af1b330e8364de7 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d37ffe026d44694 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d37ffe026d44694 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d37ffe026d44694 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d37ffe026d44694 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d37ffe026d44694 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5d37ffe026d44694 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ed66a632ff304eae step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ed66a632ff304eae step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ed66a632ff304eae step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ed66a632ff304eae step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ed66a632ff304eae step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ed66a632ff304eae step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ed66a632ff304eae step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5f9c6df4fd334f08 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5f9c6df4fd334f08 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5f9c6df4fd334f08 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5f9c6df4fd334f08 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5f9c6df4fd334f08 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5f9c6df4fd334f08 step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5f9c6df4fd334f08 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5f9c6df4fd334f08 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5f9c6df4fd334f08 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8b334cb45bc74cb7 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=8b334cb45bc74cb7 step=624 player=0 — shed total=100 >= cap 100 at day boundary

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
