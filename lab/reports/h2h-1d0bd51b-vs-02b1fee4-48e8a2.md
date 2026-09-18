# Batch report: h2h-1d0bd51b-vs-02b1fee4-48e8a2

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v41_rl_2 | 3.615 | 2128 | 50 | 0 | 0 | 6946.3 |
| opp_soil | -3.615 | 872 | 0 | 50 | 0 | -6946.3 |

## Per-opponent records

### v41_rl_2
- vs opp_soil: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 6946.3

### opp_soil
- vs v41_rl_2: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -6946.3

## Audit findings (ranked by severity)

- **preempted_sell**: 1407 occurrences
- **shed_overflow**: 309 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_soil | preempted_sell | 435 | 8.70 |
| opp_soil | shed_overflow | 70 | 1.40 |
| v41_rl_2 | preempted_sell | 972 | 19.44 |
| v41_rl_2 | shed_overflow | 239 | 4.78 |

Top findings:

- [high] `shed_overflow` game=a3d1b8cac3bd404d step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a3d1b8cac3bd404d step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a3d1b8cac3bd404d step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a3d1b8cac3bd404d step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a3d1b8cac3bd404d step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a3d1b8cac3bd404d step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=667a6df6049d4ed0 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=667a6df6049d4ed0 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=667a6df6049d4ed0 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=667a6df6049d4ed0 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=667a6df6049d4ed0 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=667a6df6049d4ed0 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=667a6df6049d4ed0 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=05b6c784b4d94eef step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=05b6c784b4d94eef step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=05b6c784b4d94eef step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=05b6c784b4d94eef step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=05b6c784b4d94eef step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=05b6c784b4d94eef step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=05b6c784b4d94eef step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10b80d87d412461f step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10b80d87d412461f step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10b80d87d412461f step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10b80d87d412461f step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10b80d87d412461f step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10b80d87d412461f step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10b80d87d412461f step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3b112b7fbacb444a step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3b112b7fbacb444a step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3b112b7fbacb444a step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3b112b7fbacb444a step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3b112b7fbacb444a step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3b112b7fbacb444a step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3b112b7fbacb444a step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=3b112b7fbacb444a step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6af5bff0e86b4585 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6af5bff0e86b4585 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6af5bff0e86b4585 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6af5bff0e86b4585 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6af5bff0e86b4585 step=624 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**PASS**
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [PASS] vs_incumbent_paired: 42 games better than the incumbent mirror, 0 worse (raw losses 4)
- [PASS] vs_incumbent: raw W-L 46-4, paired regressions 0, over 850000-850024
- [PASS] vs_parent_paired: 47 games better than the parent mirror, 0 worse (raw losses 1)
- [PASS] vs_parent: raw W-L 49-1, paired regressions 0, over 860000-860024
- [INFO] vs_other:opp_soil: 50-0 over 870000-870024
- [INFO] vs_other:v41_open20: 49-1 over 870000-870024
- [PASS] final_untouched: raw W-L 49-1, paired regressions 0, over 910000-910024
- [PASS] audit: 3626 findings, 0 critical
