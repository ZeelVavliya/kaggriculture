# Batch report: h2h-af60f83c-vs-1d0bd51b-1f1d7b

## Bradley-Terry ranking (win-based; margin never used for selection)

| name | BT rating | elo | W | L | T | mean margin |
|---|---|---|---|---|---|---|
| v43_carrot | 0.828 | 1644 | 42 | 8 | 0 | 2193.6 |
| v41_rl_2 | -0.828 | 1356 | 8 | 42 | 0 | -2193.6 |

## Per-opponent records

### v43_carrot
- vs v41_rl_2: W42-L8-T0 (win rate 95% CI 71%-92%, n=50), mean margin 2193.6

### v41_rl_2
- vs v43_carrot: W8-L42-T0 (win rate 95% CI 8%-29%, n=50), mean margin -2193.6

## Audit findings (ranked by severity)

- **preempted_sell**: 596 occurrences
- **shed_overflow**: 442 occurrences

### What to improve, per agent (findings per game played)

| agent | check | count | per game |
|---|---|---|---|
| v41_rl_2 | preempted_sell | 390 | 7.80 |
| v41_rl_2 | shed_overflow | 227 | 4.54 |
| v43_carrot | shed_overflow | 215 | 4.30 |
| v43_carrot | preempted_sell | 206 | 4.12 |

Top findings:

- [high] `shed_overflow` game=b6fe7021820940bc step=552 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b6fe7021820940bc step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b6fe7021820940bc step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b6fe7021820940bc step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b6fe7021820940bc step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b6fe7021820940bc step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b6fe7021820940bc step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b6fe7021820940bc step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b6fe7021820940bc step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=b6fe7021820940bc step=696 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=982afbad65114282 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=982afbad65114282 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=982afbad65114282 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=982afbad65114282 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=982afbad65114282 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e9c7c839254438c step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e9c7c839254438c step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e9c7c839254438c step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e9c7c839254438c step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e9c7c839254438c step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e9c7c839254438c step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e9c7c839254438c step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=5e9c7c839254438c step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2da15d5f92d34c21 step=552 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2da15d5f92d34c21 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2da15d5f92d34c21 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2da15d5f92d34c21 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2da15d5f92d34c21 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2da15d5f92d34c21 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2da15d5f92d34c21 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2da15d5f92d34c21 step=672 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=2da15d5f92d34c21 step=696 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9028bacc2764ad3 step=576 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9028bacc2764ad3 step=576 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9028bacc2764ad3 step=600 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9028bacc2764ad3 step=600 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9028bacc2764ad3 step=624 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9028bacc2764ad3 step=624 player=1 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9028bacc2764ad3 step=672 player=0 — shed total=100 >= cap 100 at day boundary
- [high] `shed_overflow` game=c9028bacc2764ad3 step=672 player=1 — shed total=100 >= cap 100 at day boundary

## Gate verdict

**PASS**
- [PASS] compile_import: compiles and last-callable resolves
- [PASS] self_play_done: statuses=DONE/DONE
- [PASS] vs_incumbent_paired: 42 games better than the incumbent mirror, 0 worse (raw losses 4)
- [PASS] vs_incumbent: raw W-L 46-4, paired regressions 0, over 850000-850024
- [PASS] vs_parent_paired: 44 games better than the parent mirror, 0 worse (raw losses 2)
- [PASS] vs_parent: raw W-L 48-2, paired regressions 0, over 860000-860024
- [INFO] vs_other:opp_v42: 49-1 over 870000-870024
- [INFO] vs_other:v41_rl_2: 42-8 over 870000-870024
- [PASS] final_untouched: raw W-L 49-1, paired regressions 0, over 910000-910024
- [PASS] audit: 2922 findings, 0 critical
