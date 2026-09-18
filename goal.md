# Goal: overnight improve → gate → submit → learn loop

**Competition:** kaggriculture · entry deadline 23 Sep 2026 · final submission 30 Sep 2026
**Ladder rules that shape this loop:** 5 submissions/day · only the **latest 2** submissions stay active · rating moves on **win/loss/tie only**, never coin margin.

## Objective

Raise our best active ladder score, one verified change at a time, with every step recorded in `lab/runs.db`.
Nothing is submitted that has not passed `lab.gate` locally. Nothing is kept because it "looks better". Losses get recorded too.

## Start the loop

```
/loop 2h Follow kaggleagriculture/goal.md: run exactly one iteration of the loop, then stop.
```

2 hours (at :07). Ladder episodes and gates are slow; a 30-minute cadence mostly re-synced unchanged state. Most iterations will only sync and check running jobs: new ladder episodes arrive slowly and 5 submissions/day allows at most ~1 submission every 5 hours. If a gate or Phase 2 job from an earlier iteration is still running, an iteration just checks it and ends.

## One iteration (do these in order, stop at the first step that says stop)

0. **Orient.** Read `lab/loop_journal.md` (create it if missing). Note the current champion, challenger and today's submission count. If a local tournament/gate is still running from the last iteration, check its output and skip to step 3 only when it has finished.
1. **Sync the ladder.** `python -m lab.submit sync`. For each active submission, `python -m lab.submit episodes --submission-id <id>`. Download replays of **new losses** (`kaggle competitions replay <EPISODE_ID> -p lab/ladder_replays/<sub_id>`, skipping episodes that already have `episode-<id>-replay.json` or `.json.gz`, then gzip new ones; read them with `lab.audit.load_replay`), and logs for any episode with an ERROR status. Record them in the ledger.
2. **Diagnose.** Run `lab.audit` over the new ladder replays and the last local batch. Pick the **single** most costly recurring finding. A finding counts only if it recurs (≥2 games) and is linked to losses. Write it into the journal with game ids and steps.
3. **Build one candidate.** Make exactly one targeted change that addresses that finding, as a new file, parented to the current champion. Register it: `python -m lab.registry --name <name> --path <file> --parent <champion> --notes "<what changed and why>"`. One change per candidate, so a pass or a veto says something about that change.
4. **Gate.** `python -m lab.gate --candidate <name> --parent <champion> --incumbent <champion> --others <current opponent pool>`. Opponent pool = opp_v41, opp_soil, opp_salem2900, c94, c95 (minus the candidate's own parent/incumbent). **VETO → stop.** Log the veto and its reason in the journal, revert, and next iteration pick the next finding. PASS → continue.
5. **Package check.** `python -m lab.registry --check-package <file or tar.gz> --entry <callable>`: unpacks exactly what will be uploaded into a temp dir, confirms the last-callable, plays one smoke game from there. Anything that fails → stop.
6. **Submit** (only if under **4** submissions today, UTC day — keep 1 in reserve for emergencies):
   `kaggle competitions submit kaggriculture -f <file> -m "lab:<name> sha:<sha8>"`, then `python -m lab.submit record` + `sync`.
   **Slot rule (corrected 2026-09-15):** Kaggle keeps only the latest 2 submissions active, and a new submission deactivates the **oldest** one. A resubmitted file restarts at 600, so resubmitting a displaced champion does not restore its rating. Therefore: only submit when the submission that would be deactivated is not carrying the team's best score, **or** the submission that stays active has climbed to within ~100 points of it. While the high-rated champion is the oldest active submission, a new gated candidate waits as `ready_to_submit` in the journal. **Exception:** submit anyway when the new candidate beats the displaced champion head to head locally with a Wilson 95% lower bound above 50% (≥20 both-seat games) and has passed the gate. A clearly stronger agent should start climbing immediately.
   **Claude submits (user rule, 2026-09-15):** every submission is made by Claude with the plain `kaggle competitions submit` command as soon as a candidate clears steps 4-5. Don't ask the user to submit, and don't wait for them. Record it with `python -m lab.submit record` and journal the submission id in the same iteration.
   **If the submit command is denied by permissions anyway:** do not work around it. Journal "ready to submit: <path>, <message>" and tell the user why it was blocked.
7. **Promote or retire.** Only when the challenger has **≥30 ladder episodes**: promote it to champion if its score beats the champion's; otherwise retire it. Identical files can score differently on the ladder (the reference kernel saw 2182 vs 1210 for one SHA), so never decide on a handful of episodes.
8. **Journal.** Append to `lab/loop_journal.md`: time, ladder scores, finding chosen, candidate sha8, gate verdict with per-opponent records, submission id or reason for not submitting, and the next finding to try. Then end the iteration.

## Phase 2 decision (user, 2026-09-15): try IL+RL after v41 is live, fall back if it fails

**Trigger to start RL:** the v41 champion submission is on the ladder (status COMPLETE) **and** its results are back: at least 10 public ladder episodes, or a public score that has moved less than 50 points across two syncs. Until then, Phase 2 may only do prep work that doesn't need the ladder: find the market decision point in v41, build the environment, collect data, train the imitation (BC) model, check fidelity, export.

**Try, in order** (each step must pass before the next):
1. **BC fidelity:** the imitated v41 plays raw v41 at about 50/50 (within a few hundred coins) and still beats opp_soil like v41 does, on seeds 880000-880009, both seats.
2. **RL fine-tune:** PPO from the BC weights, terminal win/loss reward, KL penalty to the BC policy, opponent pool = opp_v41, opp_soil, opp_salem2900, c94, c95 + frozen snapshots of the policy itself.
3. **Gate:** `lab.gate --candidate <v41_rl_x> --parent opp_v41 --incumbent opp_v41 --others opp_soil,opp_salem2900,c94`, then the package check, then submit as challenger.

**It "doesn't work" if any of these happen:**
- BC fidelity fails after one round of diagnosis and fixes.
- 3 RL candidates in a row are vetoed by the gate.
- An RL candidate passes the gate but, after 30 or more ladder episodes, scores below the v41 champion.
- The per-turn runtime or file size can't fit the submission limits (1 s per turn).

**Fallback (the original plan):** stop Phase 2, write the reason in the journal, and go back to the one-change-per-candidate loop above, with opp_v41 as the champion base: pull the next recurring loss pattern out of ladder replays → build a targeted overlay → gate → submit.

## Phase 2 outcome (user decision, 2026-09-16): fallback, option 1

The IL+RL fallback criterion was met: `v41_rl_1` passed the gate but sits below the v41 champion after ≥30 ladder episodes (2,154.7 vs 2,447.4). The market-only design also cannot learn production choices, where V42/V43's ~2.5k edge comes from. **Strategy from now on:** V43 is the champion base. Improve it with the one-change loop (ladder replay forensics, public-agent adoption, targeted overlays) through the gate. RL stays a tool, e.g. re-running the paired 14-knob search on V43, not the strategy. Re-opening full IL+RL (with production choices in the action space) needs the user's say-so.

## Submission freeze (user rule, 2026-09-16)

**No new submissions until BOTH active submissions have played at least 150 ranked (public) episodes.** Active now: v43 `56266006` and v43_open55 `56267455`. Gated candidates keep being built, gated and packaged, and wait in the journal as `ready_to_submit`. A background watcher (`lab/wait_150.sh`) checks the episode counts every 3 hours and notifies when both reach 150; at that point the normal submit rules (Claude submits, slot rule + exception, 4/day cap) resume.

## Gold plan (2026-09-17)

**Target:** a live score of **≥ 2,950 by 28 Sep** (gold is top 28 of 9,232 = 2,923.7 today and drifts up ~5-10/day). Current: v43_lead8 2,626 (falling), v43_lead8_open3 2,011 (climbing, 76% wins). Gap ≈ 300 points ≈ 3-5 percentage points of win rate in a field where 70-88% of games are same-farm mirrors decided on the market layer. Deadline: final submission 30 Sep.

**What we have learned (each item measured, not guessed):**
1. The farm is converged. Every loss at 2,600+ but one was to an identical farm. Gains come from market decisions, in this order of size: production routing to observed shops (V42/V43, +2.5k/game), turn-0 wheat size (55 → 3: +1.3k, win rate vs small openers 29% → 70%), sell-ahead horizon (4 → 8: +1.2-1.4k), then tie-breaks (carrot +10-17).
2. Small local edges transfer to the ladder to the coin (lead8 vs open50: −43 locally, −43 vs c_fxy live).
3. Ladder scores decay as an agent climbs into stronger company (lead8 87% → 55%); judge an agent by its win rate in the 2,600+ band, not its peak.
4. Dead ends, do not retry: reordering wheat/fertilizer sells (2 vetoes), single-unit field rescues on tapes, full-head RL, horizons 5/6/12 (regress on a few seeds), lead264 on v41.
5. The gate's "one paired regression = veto" has rejected agents that were better on 44/50 seeds (open7). Rule change below.
6. Rank 1 (Majkel1337, 3,183) runs a different farm: turn-0 cow, zero sheep, 3-13 cows, 10 hands. 165 of their replays are in `lab/top_replays/majkel1337/`.

**Phase A — consolidate on the open3 base (17-19 Sep), expected +50-100:**
- `v43_open3_carrot`: carrot tie-break on open3 (already PASS on two other bases). Gate, submit, replaces v43_lead8 when open3's score passes it.
- Re-test horizon 12 on open3 (it beat horizon 8 48-2 but regressed on 2 seeds while the opening was still 55).
- Add small-opener agents (open3/open7) to the gate's `--others` pool: that is the field now.

**Phase B — market-layer mining (every loop iteration, 17-26 Sep), expected +100-200:**
- For each new ladder loss to a same-farm opponent, diff market orders turn by turn (`lab/loop_journal.md` iterations 20-26 show the method). Known unexplored contested turns: step-21 wheat-seed buy (we buy 0, winners buy 2), steps 171/195 wheat buys (we buy 2, winners don't), milk/egg sold 3-6 steps early (Shun), terminal liquidation order.
- One change per candidate, parent = current champion, gate, submit on PASS.

**Phase C — structural test from the rank-1 farm (20-24 Sep), high variance:**
- Two single changes from Majkel's replays: (1) turn-0 `BUY_ANIMAL COW 1` opening; (2) no sheep — steer V43's plan router to a cow-heavy plan. Gate each against the full pool. Keep only if it wins the 2,600+ mirror band, not just the average.

**Gate rule change (from item 5):** a candidate passes a block if paired regressions ≤ 1 **and** games-better ≥ 40 of 50 **and** the final untouched block has 0 regressions. Anything else stays a veto. Record which rule a PASS used.

**Endgame (27-30 Sep):** by 28 Sep freeze the two active slots as {champion, best challenger}; in the last 48 h resubmit only if a live score decays by >100 and the replacement has ≥30 ranked games' worth of local evidence; never leave two unproven entries live at the deadline.

## Hard rules

- All submissions are made by Claude (user rule). Never submit an artifact that is not registered, gated and package-checked. The submission message always carries `sha:<sha8>`.
- Never edit `lab/*.py` while a background tournament or gate is running.
- Never delete ledger rows, replays or journal entries, including losses.
- Select on win-based rating and gate verdicts, never on mean margin.
- If the same finding gets vetoed 3 times, mark it "blocked" in the journal and move on.
- If Kaggle returns a submission ERROR, stop the loop's submission step until the logs are read and the cause is recorded.
- When editing any text file from Python on this machine, pass `encoding="utf-8"` (the default cp1252 truncated goal.md once).
- Stop the loop if: the daily limit is reached and nothing else is useful, auth fails twice, or the deadline passes.

## Findings queue (highest value first)

1. **Champion is opp_v41** (80-0 local round robin, tourney-080f5f45). Package ready: `lab/packages/v41/submission.tar.gz` (byte-identical to the published archive). Awaiting submission (auto-mode blocked the submit command).
2. **Blocked on c94:** animal starvation overlay (`c94_survival_guard` vetoed 0-50; one-unit rescues desync the recording). Re-test only on a base that isn't a recording, or with a different mechanism.
3. **Conflicting claim to settle:** SE quadrant (Rayk: every four-quadrant variant lost 450 games; Nathan Jacob: prvsiyan earns +$8–22K from it).
4. Phase 2 IL+RL on the v41 base, per the Phase 2 decision above.
