# Batch report: h2h-985fbbcb-vs-a86e80f9-aeac68

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_lead8_carrot | 3.615 | 2128 | 50 | 0 | 0 | 1539.4 |
| v43_open55 | -3.615 | 872 | 0 | 50 | 0 | -1539.4 |

## Per-opponent records

### v43_lead8_carrot
- vs v43_open55: W50-L0-T0 (win rate 95% CI 93%-100%, n=50), mean margin 1539.4

### v43_open55
- vs v43_lead8_carrot: W0-L50-T0 (win rate 95% CI 0%-7%, n=50), mean margin -1539.4

## Audit findings (ranked by severity)

- **shed_overflow**: 442 occurrences
- **preempted_sell**: 300 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v43_lead8_carrot | shed_overflow | 221 | 4.42 |
| v43_lead8_carrot | preempted_sell | 116 | 2.32 |
| v43_open55 | shed_overflow | 221 | 4.42 |
| v43_open55 | preempted_sell | 184 | 3.68 |

Top findings:

- [high] `shed_overflow` game=0dc2c2d587544c7f step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0dc2c2d587544c7f step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0dc2c2d587544c7f step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0dc2c2d587544c7f step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0dc2c2d587544c7f step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0dc2c2d587544c7f step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0dc2c2d587544c7f step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0dc2c2d587544c7f step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0dc2c2d587544c7f step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=0dc2c2d587544c7f step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=7ffa811dbc684f51 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f7607b58ca6f47b8 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f7607b58ca6f47b8 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f7607b58ca6f47b8 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f7607b58ca6f47b8 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f7607b58ca6f47b8 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f7607b58ca6f47b8 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f7607b58ca6f47b8 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f7607b58ca6f47b8 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f7607b58ca6f47b8 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=f7607b58ca6f47b8 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b840af5ce6aa4858 step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b840af5ce6aa4858 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b840af5ce6aa4858 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b840af5ce6aa4858 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b840af5ce6aa4858 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b840af5ce6aa4858 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b840af5ce6aa4858 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b840af5ce6aa4858 step=624 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**PASS**
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [PASS] vs_incumbent_paired: 42 games better than the incumbent mirror, 0 worse (raw losses 4)
- [PASS] vs_incumbent: raw W-L 46-4, paired regressions 0, over 850000-850024
- [PASS] vs_parent_paired: 44 games better than the parent mirror, 0 worse (raw losses 2)
- [PASS] vs_parent: raw W-L 48-2, paired regressions 0, over 860000-860024
- [INFO] vs_other:v43_open55: 50-0 over 870000-870024
- [INFO] vs_other:opp_v43: 50-0 over 870000-870024
- [PASS] final_untouched: raw W-L 49-1, paired regressions 0, over 910000-910024
- [PASS] audit: 2986 findings, 0 critical
