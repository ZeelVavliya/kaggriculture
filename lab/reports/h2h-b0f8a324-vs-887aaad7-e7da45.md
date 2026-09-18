# Batch report: h2h-b0f8a324-vs-887aaad7-e7da45

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8 | 3.615 | 2128 | 50 | 0 | 0 | 7432.4 |
| v43_open3_cash21b | -3.615 | 872 | 0 | 50 | 0 | -7432.4 |

## Per-opponent records

### v43_lead8
- vs v43_open3_cash21b: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 7432.4

### v43_open3_cash21b
- vs v43_lead8: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -7432.4

## Audit findings (ranked by severity)

- **shed_overflow**: 388 occurrences
- **preempted_sell**: 136 occurrences
- **animal_escape**: 50 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8 | shed_overflow | 193 | 3.86 |
| v43_lead8 | preempted_sell | 109 | 2.18 |
| v43_open3_cash21b | shed_overflow | 195 | 3.90 |
| v43_open3_cash21b | animal_escape | 50 | 1.00 |
| v43_open3_cash21b | preempted_sell | 27 | 0.54 |

Top findings:

- [high] `animal_escape` game=d75fd70d154b4adf step=48 player=1 — COW escaped at (4,4)
- [high] `shed_overflow` game=d75fd70d154b4adf step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d75fd70d154b4adf step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d75fd70d154b4adf step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d75fd70d154b4adf step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=d75fd70d154b4adf step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=996643c6fb334647 step=48 player=0 — COW escaped at (4,4)
- [high] `shed_overflow` game=996643c6fb334647 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=996643c6fb334647 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=a7ceb07e903d4a4c step=48 player=0 — COW escaped at (4,4)
- [high] `shed_overflow` game=a7ceb07e903d4a4c step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a7ceb07e903d4a4c step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a7ceb07e903d4a4c step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a7ceb07e903d4a4c step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a7ceb07e903d4a4c step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=a8d19e826c06409e step=48 player=1 — COW escaped at (4,4)
- [high] `shed_overflow` game=a8d19e826c06409e step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=a8d19e826c06409e step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `animal_escape` game=38987d1aee6f4703 step=48 player=1 — COW escaped at (4,4)
- [high] `shed_overflow` game=38987d1aee6f4703 step=528 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**VETO** — lost to incumbent in 46/50 games (seed_block=850000-850024)
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [VETO] vs_incumbent_paired: 0 games better than the incumbent mirror, 46 worse (raw losses 50)
- [VETO] vs_incumbent: raw W-L 0-50, paired regressions 46, over 850000-850024
- [VETO] vs_parent_paired: 0 games better than the parent mirror, 48 worse (raw losses 50)
- [VETO] vs_parent: raw W-L 0-50, paired regressions 48, over 860000-860024
- [INFO] vs_other:v43_lead8_open7: 0-50 over 870000-870024
- [INFO] vs_other:v43_lead8: 0-50 over 870000-870024
- [INFO] vs_other:opp_v43: 0-50 over 870000-870024
- [PASS] audit: 3352 findings, 0 critical
