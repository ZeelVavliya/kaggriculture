# Batch report: tourney-0fd80277

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8_open3 | 0.756 | 1631 | 30 | 0 | 30 | 153.5 |
| v43_lead8_open0 | -0.000 | 1500 | 0 | 0 | 60 | 0.0 |
| v43_lead8_open7 | -0.756 | 1369 | 0 | 30 | 30 | -153.5 |

## Per-opponent records

### v43_lead8_open3
- vs v43_lead8_open7: W30-L0-T0 (win rate 95% CI 89%-100%, n=30), mean margin 307.1
- vs v43_lead8_open0: W0-L0-T30 (win rate 95% CI 33%-67%, n=30), mean margin 0.0

### v43_lead8_open0
- vs v43_lead8_open7: W0-L0-T30 (win rate 95% CI 33%-67%, n=30), mean margin 0.0
- vs v43_lead8_open3: W0-L0-T30 (win rate 95% CI 33%-67%, n=30), mean margin 0.0

### v43_lead8_open7
- vs v43_lead8_open3: W0-L30-T0 (win rate 95% CI 0%-11%, n=30), mean margin -307.1
- vs v43_lead8_open0: W0-L0-T30 (win rate 95% CI 33%-67%, n=30), mean margin 0.0

## Audit findings (ranked by severity)

- **shed_overflow**: 820 occurrences
- **preempted_sell**: 2 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8_open0 | shed_overflow | 272 | 4.53 |
| v43_lead8_open3 | shed_overflow | 274 | 4.57 |
| v43_lead8_open7 | shed_overflow | 274 | 4.57 |
| v43_lead8_open7 | preempted_sell | 2 | 0.03 |

Top findings:

- [high] `shed_overflow` game=922e67e68a40429b step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=922e67e68a40429b step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=741bba98397e43de step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=741bba98397e43de step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=741bba98397e43de step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=741bba98397e43de step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=741bba98397e43de step=648 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=741bba98397e43de step=648 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=741bba98397e43de step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=741bba98397e43de step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=504 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=504 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=528 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=528 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=9bab589156e945e0 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f81e8d4936e94335 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f81e8d4936e94335 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f81e8d4936e94335 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f81e8d4936e94335 step=624 player=1 — shed total=100 >= cap 100 at day boundary
