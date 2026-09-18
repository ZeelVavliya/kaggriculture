# Batch report: h2h-0ff60be9-vs-887aaad7-fb5887

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead12 | 1.585 | 1775 | 48 | 2 | 0 | 1350.9 |
| v43_lead8 | -1.585 | 1225 | 2 | 48 | 0 | -1350.9 |

## Per-opponent records

### v43_lead12
- vs v43_lead8: W48-L2-T0 (win rate 95% CI 87%-99%, n=50), mean margin 1350.9

### v43_lead8
- vs v43_lead12: W2-L48-T0 (win rate 95% CI 1%-13%, n=50), mean margin -1350.9

## Audit findings (ranked by severity)

- **shed_overflow**: 444 occurrences
- **preempted_sell**: 172 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead12 | shed_overflow | 221 | 4.42 |
| v43_lead12 | preempted_sell | 56 | 1.12 |
| v43_lead8 | shed_overflow | 223 | 4.46 |
| v43_lead8 | preempted_sell | 116 | 2.32 |

Top findings:

- [high] `shed_overflow` game=e2a47d15757d44d2 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e2a47d15757d44d2 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e2a47d15757d44d2 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e2a47d15757d44d2 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e2a47d15757d44d2 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e2a47d15757d44d2 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e2a47d15757d44d2 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e2a47d15757d44d2 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e2a47d15757d44d2 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=e2a47d15757d44d2 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=277e939a5e864060 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=277e939a5e864060 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=277e939a5e864060 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=277e939a5e864060 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=277e939a5e864060 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=277e939a5e864060 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10d5ea100c1c4c65 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10d5ea100c1c4c65 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10d5ea100c1c4c65 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10d5ea100c1c4c65 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10d5ea100c1c4c65 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=10d5ea100c1c4c65 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ced24074202c4e7b step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ced24074202c4e7b step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ced24074202c4e7b step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ced24074202c4e7b step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ced24074202c4e7b step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ced24074202c4e7b step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ced24074202c4e7b step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ced24074202c4e7b step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ced24074202c4e7b step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=ced24074202c4e7b step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0fdf883f09854aee step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0fdf883f09854aee step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0fdf883f09854aee step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0fdf883f09854aee step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c3932891296945b9 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c3932891296945b9 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c3932891296945b9 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c3932891296945b9 step=672 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**VETO** — lost to incumbent in 2/50 games (seed_block=850000-850024)
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [VETO] vs_incumbent_paired: 42 games better than the incumbent mirror, 2 worse (raw losses 4)
- [VETO] vs_incumbent: raw W-L 46-4, paired regressions 2, over 850000-850024
- [VETO] vs_parent_paired: 44 games better than the parent mirror, 2 worse (raw losses 4)
- [VETO] vs_parent: raw W-L 46-4, paired regressions 2, over 860000-860024
- [INFO] vs_other:v43_lead8: 48-2 over 870000-870024
- [INFO] vs_other:opp_v43: 50-0 over 870000-870024
- [PASS] audit: 2887 findings, 0 critical
