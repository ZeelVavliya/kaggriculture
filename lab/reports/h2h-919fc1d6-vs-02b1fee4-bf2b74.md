# Batch report: h2h-919fc1d6-vs-02b1fee4-bf2b74

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| opp_v43 | 3.615 | 2128 | 50 | 0 | 0 | 7205.2 |
| opp_soil | -3.615 | 872 | 0 | 50 | 0 | -7205.2 |

## Per-opponent records

### opp_v43
- vs opp_soil: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 7205.2

### opp_soil
- vs opp_v43: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -7205.2

## Audit findings (ranked by severity)

- **preempted_sell**: 1619 occurrences
- **shed_overflow**: 287 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| opp_soil | preempted_sell | 623 | 12.46 |
| opp_soil | shed_overflow | 70 | 1.40 |
| opp_v43 | preempted_sell | 996 | 19.92 |
| opp_v43 | shed_overflow | 217 | 4.34 |

Top findings:

- [high] `shed_overflow` game=27306e9a6f364338 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=27306e9a6f364338 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=27306e9a6f364338 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6d9e1dcdfa6e4ffb step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6d9e1dcdfa6e4ffb step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6d9e1dcdfa6e4ffb step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6d9e1dcdfa6e4ffb step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6d9e1dcdfa6e4ffb step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6d9e1dcdfa6e4ffb step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=6d9e1dcdfa6e4ffb step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=733e8fb531d14c5e step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=733e8fb531d14c5e step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=733e8fb531d14c5e step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=733e8fb531d14c5e step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=733e8fb531d14c5e step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=733e8fb531d14c5e step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=39df22f0ac1c42d0 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=39df22f0ac1c42d0 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=39df22f0ac1c42d0 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=97405223b6d04319 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=97405223b6d04319 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=97405223b6d04319 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=97405223b6d04319 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=97405223b6d04319 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8a3d77aef6f4af9 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8a3d77aef6f4af9 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8a3d77aef6f4af9 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8a3d77aef6f4af9 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8a3d77aef6f4af9 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8a3d77aef6f4af9 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a3db99185b9940ec step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a3db99185b9940ec step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a3db99185b9940ec step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a3db99185b9940ec step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a3db99185b9940ec step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58ef980177cf4479 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58ef980177cf4479 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58ef980177cf4479 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58ef980177cf4479 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=58ef980177cf4479 step=672 player=0 — shed total=100 >= cap 100 at day boundary

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
