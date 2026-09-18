# Loop journal

## Iteration 1 — 2026-09-15 (local) / 2026-09-14 ~16:25 UTC

**Ladder before:** 56235192 `main` 504.4 (only a validation episode so far) · 55648629 `main2` 489.9 (1 public episode in 26 days) · 55317806 `main` 351.8 (inactive).
**Submissions used today (UTC day 2026-09-14):** 2 of 5 (`main` test upload, `c94` champion).

**Observation:** ladder episodes arrive very slowly for low-rated agents (main2 got 1 ranked game in a month). The goal.md "≥30 ladder episodes before promote/retire" rule may take days per submission. Local gating carries most of the decision weight.

**Action:** submitted `c94` (sha 7b0e5a7b) as champion — id **56235311**. Rationale: best local artifact by win-based BT (158-2 in tourney-0a651d40, both losses to c95 by 13 coins on seed 900013), package round-trip passed from temp dir (reward 127086 vs starter), SHA verified. Active slots are now {c94 champion, main test}. The next challenger submission will displace `main` (intended).

**Local state:** Phase 1 lab audited and fixed (BT gradient, incremental storage, error-scoring, melon check, preemption check, gate final block, Wilson CI, 25-seed gate blocks, package check). Gate exercised: c95 vs parent c94 → VETO 0-10 / 0-10.

**Finding chosen for next candidate:** C94's field tape starves a COW at (7,4) on day 21 (step 528) in every game, both seats (animal_escape 1.00/game for c92/c94/c95).
**Candidate in progress:** `c94_survival_guard` (parent c94), built by Sonnet subagent, plus opponent pool refresh (prvsiyan Soil/Moon, other current top public agents).
**Next:** gate `c94_survival_guard`; submit as challenger only on PASS.

### Iteration 1 (cont.) — candidate result

**Opponent pool refreshed** (registered, single self-contained files, last-callable `agent`):
- `opp_soil` 02b1fee4 — prvsiyan "Soil remembers rain". **Moon counts melons submits the byte-identical main.py** (both package yhay81 Shop Router 0909 unmodified; Moon's extra cells are research only and "do not change packaged main.py") → one opponent, not two.
- `opp_salem2900` 3b1cb91f · `opp_v41` 8951ff93 (Ahmed Berat Özer v41, 331 KB).

**C94 is behind the current public meta** (seed block 880000-880009, both seats):
| opponent vs c94 | record | mean margin |
|---|---|---|
| opp_soil | 20-0 | +29,431 |
| opp_v41 | 20-0 | +34,263 |
| opp_salem2900 | 19-1 | +2,531 |

**`c94_survival_guard` (8cc45e59, parent c94): VETO.**
- Builder diagnosis: a day-20 missed feed starts the (7,4) cow's fatal 2-day streak; the overlay feeds carried wheat into an unfed animal the unit stands on at hour ≥ 18, delaying the displaced PASS/move a turn. No later rescue window exists in the tape, so the escape is only *delayed* to day 23, not prevented.
- Gate: vs incumbent c94 **0-50** (mean −331), vs parent c94 **2-48** (−238), vs opp_soil 0-50 (−32,786). Pre-gate h2h 2-18 (−199). Diverting a unit off the position-dependent tape costs more than one milk cycle recovers.
- The gate process died when the builder agent stalled; the opp_salem2900 batch has 20 HARNESS_ERROR rows (now excluded from ratings/gate). Veto stands on the completed batches.
- Lesson: on tape agents, single-unit rescues desync the tape. Finding #1 is **blocked on c94** (1 veto); re-test only on a non-tape or better base.

**Lab fixes:** HARNESS_ERROR rows excluded from BT and gate loss counting.

**Next:** round robin {opp_v41, opp_soil, opp_salem2900, c94, c95} to choose the new champion base; submit the winner as the new champion (it displaces the `main` test slot).

### Iteration 1 (cont.) — new champion chosen

**Round robin tourney-080f5f45** (seeds 900000-900009, both seats, 200 games, 0 errors, ~15 s/game):
| agent | BT elo | W-L | mean margin |
|---|---|---|---|
| **opp_v41** | 2945 | **80-0** | +33,483 |
| opp_soil | 2006 | 60-20 | +25,608 |
| opp_salem2900 | 1039 | 32-48 | −16,370 |
| c94 | 918 | 24-56 | −21,327 |
| c95 | 591 | 4-76 | −21,394 |
v41 beats soil 20-0 (+7,061), c94 20-0 (+44,536). New champion base = **opp_v41** (Ahmed Berat Özer v41, Apache 2.0).

**Package:** rebuilt `lab/packages/v41/submission.tar.gz` exactly as the notebook does. main.py sha matches notebook `EXPECTED_MAIN_SHA256` (8951ff93) and archive sha matches `EXPECTED_ARCHIVE_SHA256` (38a7ee01…): byte-identical to the published upload. Package round-trip from temp dir: OK, reward 149,771 vs starter.
Note: v41's own manifest says `competitive_gate_status: FAILED_ELITE_POINT_CI` (its author's gate), but it is still the strongest agent in our pool by a wide margin.

**Submission BLOCKED:** `kaggle competitions submit` was denied by Claude Code's auto-mode permission classifier ("Real-World Transactions"). Not retried or worked around. **The loop cannot submit unattended until the user grants a permission rule** (see chat). Everything up to the submit step still runs.

**Phase 2 (IL+RL) started** on the v41 base, in parallel with the loop.

**User decision (2026-09-15):** once v41 is submitted and its ladder results are back, try IL+RL; if it doesn't work, fall back to the original one-change loop. Trigger and failure criteria written into goal.md → "Phase 2 decision". Prep work (BC, fidelity) continues in the meantime; RL waits for the trigger.

### Phase 2 prep — BC warm start on v41: PASS (audited)

- **Seam:** v41 = frozen 720-step field tape (`Chassis.step`) + 17 stacked overlay layers (`agent=globals().pop('agent')` rebinding). Overlay state (`_R12x_STATES`) is re-read from the live observation every turn, so rewriting SELL orders does not desync v41's bookkeeping. Policy rewrites only SELLs of the 7 free items (CARROT, TOMATO, STRAWBERRY, MELON, EGG, MILK, WOOL); WHEAT/FERTILIZER SELLs and all buys/hires/land keep their exact slot index.
- **First BC (absolute fractions): FAILED** 0-20 vs v41 (−17.5k), 0-20 vs soil. Causes found: (1) same-turn harvest means v41 sells more than the pre-turn shed shows, so `frac × shed` zeroed real orders (85/719 turns differed even with zero output); (2) v41's `sell_lead` can emit two SELLs for one item, which per-item merging collapsed. Also a ledger bug in `lab/p2/fidelity.py` (result stored from BC's view): fixed, 40 rows corrected in place.
- **Fix: residual policy.** Zero-initialised output heads add deltas to v41's own per-slot sell fraction/priority; capacity = max(pre-turn shed, v41's proposed qty). Zero output reproduces v41 exactly (0/719 turns differ). BC loss is 0 by construction: BC certifies the warm start, RL must create any improvement.
- **Fidelity (p2-bc-fidelity-9ca30f27, seeds 880000-880009, both seats):** vs v41 18 exact ties + seed 880002 ±117. **Auditor check:** raw v41 mirror on 880002 = 112,639 / 112,756, identical, so that ±117 is the seed's seat asymmetry, not "float rounding" as the builder reported. vs soil 20-0 (+5,945).
- **Data:** 500 games, 189,536 rows, 0 errors (`lab/p2/data/bc_data_500.npz`).
- **Export:** `v41_bc` (3b764ca5, parent opp_v41), 712 KB single file, 4.07 ms/turn, package check OK (reward 149,771 = raw v41).
- **Next:** RL fine-tune waits for the goal.md trigger (v41 live on the ladder + results back). v41 submission is waiting on the user's permission rule.

## Iteration 2 — 2026-09-15 (local)

**Ladder sync:** c94 56235311 **1006.9** (48 public episodes) · main 56235192 327.1 · main2 55648629 489.9 (inactive). Submissions today (UTC): 2 of 5.
**Champion v41 still NOT submitted:** `.claude/settings.json` still has no kaggle allow rule and the earlier submit was denied by auto mode. Not retried. Ready to submit: `lab/packages/v41/submission.tar.gz`, message `lab:opp_v41 sha:8951ff93 champion`. Kaggle token now at `~/.kaggle/access_token` (plain `kaggle` CLI authenticates).
**Diagnosis (local, v41 games in tourney-080f5f45):** only two v41 findings. `shed_overflow` 4.47/game, always exactly 100 on days 20-29. Estimated discard is ~72 items across 80 games (<1 item/game) → negligible, not worth a candidate. `preempted_sell` 23.6/game is the known-noisy heuristic. No recurring costly defect in v41 locally; next findings must come from v41's own ladder losses once it is live.
**No candidate built, no gate run.** RL waits for the Phase 2 trigger (v41 live + results back).

## Iteration 3 — 2026-09-15 (local)

**v41 champion is on the ladder:** submission **56242588** (`submission.tar.gz`, `lab:opp_v41 sha:8951ff93 champion`), submitted by the user at 01:40 UTC, status PENDING at sync. Recorded in the ledger.
**Active slots now:** {v41 56242588 champion, c94 56235311 at 1006.9}. The `main` test upload (327.1) has dropped out of the latest 2.
**Submissions today (UTC 2026-09-15):** 1 of 5.
**Permissions:** `.claude/settings.json` still has no kaggle allow rule, so future challengers still need a manual submit or the rule.
**Phase 2 trigger:** not met yet. Needs v41 COMPLETE plus ≥10 public episodes, or a score that moves <50 points across two syncs. RL not started.
**No candidate this iteration** (no v41 ladder losses to diagnose yet).

## Iteration 4 — 2026-09-15 (local)

**Ladder:** v41 56242588 **COMPLETE, 1122.9** after 6 public episodes · c94 56235311 1006.9 · main 327.1 (inactive).
**v41 ladder record: 6-0**, all DONE (replays in `lab/ladder_replays/56242588/`):
| episode | opponent | seat | v41 | opp |
|---|---|---|---|---|
| 109114396 | Ahmed Bootaan | p1 | 63,745 | 24,628 |
| 109115456 | Balwinder Singh1235 | p0 | 159,826 | 80,268 |
| 109116653 | feng222666888 | p0 | 142,450 | 74,079 |
| 109117769 | sawasawasawa | p0 | 124,367 | 71,975 |
| 109118878 | black hole sun | p1 | 100,869 | 59,346 |
| 109119954 | Tai Tien Ta | p1 | 128,561 | 93,668 |
It is still climbing through low-rated opponents, so no losses to diagnose yet.
**Phase 2 trigger:** not met (6 < 10 episodes; this is the first sync with a score, so no stability reading yet).
**Permissions:** still no kaggle allow rule in `.claude/settings.json`.
**No candidate this iteration.**

## Iteration 5 — 2026-09-15 (local)

**Ladder:** v41 56242588 **1703.5**, **12-0** in 12 public episodes (new: boominginging, zjukop1, Ryo Hasegawa, SZU蓝心, DASH村, Snipine; all won, margins 6.5k-25k) · c94 1006.9.
**Phase 2 trigger MET** (≥10 public episodes, v41 COMPLETE). **RL started**: Sonnet builder launched on the residual policy (`v41_bc` 3b764ca5 as init). Fallback criteria per goal.md.
**No losses to diagnose.** Submissions today: 1 of 5. Permissions: still no kaggle allow rule.

### Phase 2 RL — run 1 (full-head ES): diverged, no candidate

- Sonnet builder wrote `lab/p2/rl.py`: antithetic ES on both linear heads (3,598 params), sigma 0.03, lr 0.02, theta-norm cap 3.0, 4 pairs × 2 seeds × 2 seats per iteration, 20% weak-opponent guard. 8 iterations, 352 games (batches p2-rl-train-1..8, p2-rl-val-8).
- **Diverged:** theta_norm 0.92 → 3.0 (pinned at the cap from iter 6); applied |delta_frac| ≈ 0.48, 16-22% of turns changed; perturbations lost to v41 nearly every time (iters 3-4: 0-32).
- **Validation (620000-620019, both seats):** 14-26 vs opp_v41, **27-13 vs opp_soil** (raw v41 is 20-0). Clearly worse than the zero residual. The builder's state.json wrongly marked iter 8 as "best"; the real baseline is the zero residual.
- Builder then stalled (watchdog) before starting run 2. **Not a gate veto** (no candidate produced).

### Phase 2 RL — run 2 (auditor-run): paired 14-knob search

- `lab/p2/rl_bias.py`: head weights fixed at 0, search only the 14 biases (per item: constant delta sell-fraction, constant delta slot-priority). Trust region frac ±0.30, prio ±1.5. Steps 0.15 / 1.0, chosen because base priorities are integer slot ranks (a 0.1 nudge never reorders) and small frac nudges round away on small stacks.
- Fitness strictly paired: result(probe) − result(base) on the same (seed, seat, opponent); train block 630000-630005 both seats vs v41 + 1 soil seed; accept a move only if gain ≥ +2 flipped outcomes. Validation of zero vs final center on 620000-620019 both seats vs v41 and soil. Running.
- **Ledger data loss (recorded, not hidden):** the builder's restart smoke test (rl_smoke2, killed after 1 iteration) reused batch id `p2-rl-train-1`, and `INSERT OR REPLACE` overwrote 4 of run 1's 352 game rows (seed 600000, candidates 0-1, both seats) plus that batch's metadata. Run 1's curve stays authoritative in `lab/p2/data/rl_run1/log.jsonl` (moved intact). Fix pending once rl_bias finishes: scope `lab/p2/rl.py` batch/game ids by run dir, and make `ledger.add_game`/`add_batch` refuse to overwrite an existing id. `rl_bias` ids are prefixed `p2-rlb-…` and unaffected.
- Builder's restart edits to rl.py (not used by run 2): cached paired base, fitness = Σ(result − base) + weak-loss penalty − l2·‖θ‖², theta cap 0.3, sigma 0.003, accept-if-probe-score ≥ old else halve sigma, best checkpoint compared against the zero residual's own validation.
- **Run 2 result:** 28 probes (1,617 s). Base train block: 4W-2L-8T vs v41 mirror. **Accepted exactly one move: frac:CARROT +0.15** (paired gain +8). Every other probe gave 0 or negative gain: lowering any premium sell fraction cost −8 to −16, and slot-priority shifts changed nothing.
- **Validation 620000-620019 (both seats):**
  | policy | vs opp_v41 | vs opp_soil | median margin vs v41 | bank mean |
  |---|---|---|---|---|
  | zero residual (= v41) | 3W-3L-34T | 40-0 (+6,713) | 0 | 96,195 |
  | +15% carrot sells | **37W-3L** | 40-0 (+6,698) | **+17** | 96,193 |
  Interpretation: same money, but selling a little more carrot each turn beats an exact v41 clone by ~17 coins, turning mirror ties into wins. The ladder ranks on W/L and v41 is public, so clone tiebreaks are a real edge; against non-clones it changes nothing.
- **Lab fixes:** (1) `ledger.add_game`/`add_batch` now plain INSERT, so an id collision raises instead of silently overwriting. (2) **Gate veto made paired vs the mirror:** v41 loses ~3/40 seat-asymmetric games to itself, so "any loss = veto" would veto an exact copy. `gate.paired_regressions` vetoes only games where the candidate scores below parent-vs-parent on the same seed and seat (applied to incumbent, parent and final-block steps). Tests pass.
- **Candidate `v41_rl_1`** (7b783b60, parent opp_v41): package `lab/packages/v41_rl_1/submission.tar.gz` (460 KB), package check OK (reward 149,653). Full gate running (25 seeds × 2 seats per opponent).
- **GATE: PASS for `v41_rl_1`** (parent + incumbent opp_v41). True records from the ledger (the gate's one-line summary printed "50-0" for mirror steps: a display bug, now fixed to show raw W-L and paired regressions separately):
  | step | seeds | raw record | paired regressions vs v41 mirror | median margin |
  |---|---|---|---|---|
  | vs incumbent v41 | 850000-850024 | 46-4-0 | **0** (42 games better) | +13 |
  | vs parent v41 | 860000-860024 | 47-1-2 | **0** (45 games better) | +14 |
  | vs opp_soil | 870000-870024 | 50-0 | — | +6,231 |
  | vs opp_salem2900 | 870000-870024 | 50-0 | — | +29,098 |
  | vs c94 | 870000-870024 | 50-0 | — | +34,351 |
  | final untouched vs v41 | 910000-910024 | 41-1-8 | **0** | +11 |
  Every raw loss to v41 is a seat-asymmetric game that v41 also loses to itself; the candidate never does worse than the mirror. Audit: 0 critical.
- **Ready to submit as challenger** (Claude's submit still blocked, no allow rule): `lab/packages/v41_rl_1/submission.tar.gz`, message `lab:v41_rl_1 sha:7b783b60 challenger`. Slots after submit: {v41 56242588 champion, v41_rl_1 challenger}; c94 drops out. Submissions today: 1 of 5.
- **Phase 2 status:** RL produced a gated candidate on the first try, so no fallback. Promotion rule: after ≥30 ladder episodes, promote v41_rl_1 only if its score beats v41's.

## Iteration 6 — 2026-09-15 (local)

**Ladder:** v41 56242588 **2436.8** (83 public episodes) · c94 1008.6. `v41_rl_1` passed the gate but the user hasn't submitted it yet.
**v41 ladder record: 63W-15L-5T.** 19 of 83 games were decided within 1,500 coins. Comparing both players' actions in those replays shows **the ladder is full of v41 copies**:
- **Exact clones (all 5 ties):** David Wang, caintly, Khanh, Georgi Kanev, John Park. Farmer and market actions identical on 719/719 turns.
- **Clones with 1-2 market tweaks that beat us by 2-12 coins:** ShadowT_T (−12, market identical 717/719), pumpkin (−2, 718/719), Adam (−6, 717/719). **They already use the same tie-break idea as v41_rl_1.**
- **v41 field with a different market layer (~500-700/719 identical market turns):** neibyr −549, dodoshark −350, siren2345 −225, Himanshu Kumar −1,252, Levin −1,277, kunihiro −756, dddmd −1,087; plus our close wins vs tongmian1314 +1,009, NoMoreThan20Words +998, sam_the_rice_cake +940, "..." +426.
- **5 big losses (>1.5k) vs non-clone fields:** EthanL67 −5,603, Bantam −4,357 and −2,048, Nikita Biryukov −1,702, Exposed −1,661.

**Finding (highest value):** ~23% of ladder games are market-layer duels between v41 copies, exactly what Phase 2 optimises. `v41_rl_1` should turn the 5 ties and the 2-12 coin losses into wins (local median edge over an exact clone is +17). It doesn't reach the 225-1,277 coin market-variant losses.
**Next candidate idea (logged, not built):** turn the near-clone replays into opponents: v41 field + that player's recorded market orders by step (the fields are identical, so replaying their market tape is near-exact against v41-family play). Add them to the RL pool and gate, so the next RL run trains against the market variants actually beating us.
**No submission** (challenger awaiting user). Submissions today: 1 of 5.

## Iteration 7 — 2026-09-15 (local)

**Ladder:** v41 2435.3 (settled; was 2436.8). `v41_rl_1` still not submitted by the user.
**Replays have no seed** (`configuration.seed: None`), so ladder games can't be reproduced locally and tape-replay opponents would be unfaithful. Instead I diffed market orders turn by turn against the near-clones:
- **ShadowT_T (+12) and Adam (+6) vs us:** identical v41 except step 265, where they add `SELL MILK 3` at the end of the list and drop it from step 267. Selling milk two turns early front-runs a v41 clone.
- **pumpkin (+2):** one extra `SELL FERTILIZER 2` at step 530.
- **siren2345 (+225), Himanshu Kumar (+1,252), kunihiro (+756):** `SELL FERTILIZER` moved into slot 0 ahead of the HIREs (steps 97, 121). Openings differ too: a larger wheat buy/sell on step 1 (43 bought, 20+22 sold; or 13+30 bought, 30 sold).
- The aggregate quantity diffs include huge nominal "sell all" orders (e.g. 1000s), so they aren't meaningful as volumes.
**Candidate `v41_sellfirst`** (b0ef1bf9, parent opp_v41): one change, all SELL orders placed before non-SELL orders within each turn (relative orders kept). Smoke vs starter **159,879** (v41: 149,771). Full gate running, others = soil, salem, c94, **v41_rl_1**.
**Queued ideas (one change each):** (a) front-run milk/fertilizer 1-2 turns like ShadowT_T/Adam; (b) the larger step-1 wheat bridge opening.
- **GATE: VETO for `v41_sellfirst`.** True records:
  | opponent | seeds | record | median margin |
  |---|---|---|---|
  | v41 (incumbent) | 850000-850024 | 0-50 (46 paired regressions) | −1,187 |
  | v41 (parent) | 860000-860024 | 1-49 (47 paired regressions) | −1,188 |
  | v41_rl_1 | 870000-870024 | 0-50 | −1,195 |
  | soil / salem / c94 | 870000-870024 | 50-0 each | +5,787 / +24,410 / +33,199 |
- **Lesson:** a higher bank vs `starter` (159,879 vs 149,771) did not transfer. Head to head against v41-family agents, moving *all* sells ahead of hires loses ~1.2k every game. v41's slot order is deliberate. The gate caught what the smoke score would have hidden.
- **Refinement for next time (not built):** the variants that beat us moved only the *fertilizer* SELL to slot 0, not every sell. Next single-change candidate: fertilizer-only slot-0 (1 veto so far on the broader version).

## Iteration 8 — 2026-09-15 (local)

**Ladder:** v41 2432.4 · `v41_rl_1` still not submitted by the user.
**Candidate `v41_fertfirst`** (b1bad7f3, parent opp_v41): SELL FERTILIZER moved to slot 0 each turn, everything else in v41's order. Narrower follow-up to vetoed v41_sellfirst. Smoke vs starter 149,771, identical to v41, so the change doesn't alter play against starter. Gate running (others: soil, v41_rl_1).
- **GATE: VETO for `v41_fertfirst`.** vs v41 1-49 (median −2,200) and 1-49 (−2,037); vs v41_rl_1 0-50 (−1,951); vs soil 50-0 (+5,153). Paired regressions 45 and 47.
- **Lesson:** fertilizer in slot 0 alone costs ~2k per game against v41-family agents, *worse* than moving all sells (−1.2k). This matches the reference kernel's rule "never promote WHEAT or FERTILIZER": they're the only products an opponent can BUY_PRODUCT, so selling them first lifts the price the opponent's later slot sells into. The slot-0 fertilizer in siren2345/Himanshu/kunihiro is not what beats v41. Their edge must come from other differences (openings, other market turns).
- **Finding "slot reordering" marked blocked** (2 vetoes: all-sells-first, fertilizer-first). Don't pursue further reorderings of wheat/fertilizer.
- **Next queued idea:** ShadowT_T/Adam's milk front-run (sell 3 MILK two turns early, ends +6 to +12 vs v41). The RL knob search already tested milk sell-fraction and priority offsets with 0 gain, so a timing shift is the untested part.

## Iteration 9 — 2026-09-15 (local)

**Ladder:** v41 2445.4 · `v41_rl_1` still not submitted.
**How v41 leads sales today:** native `Chassis._sell_lead` pulls next-step premium SELLs forward (1 step, skipped on town-consumption steps). From step 288 to 695, the R36 reserve layer (`_r36_reserve`) sells up to `_R37_HORIZONS` (2) steps ahead within the 72-step block, with per-step debts subtracted later. ShadowT_T's/Adam's only change vs v41 (MILK at step 265 instead of 267) is that 2-step reserve applied before 288.
**Candidate `v41_lead264`** (1dbf8501, parent opp_v41): two literal edits, the R36 reserve window and the native-lead cutover both start at step 264 instead of 288. Real diff verified with `diff --strip-trailing-cr` (Python's write_text on Windows had converted line endings; semantics unchanged). Smoke vs starter 149,765 (v41 149,771). Gate running (others: soil, v41_rl_1).
- **DISK FULL incident.** The `v41_lead264` gate's final block hit `OSError(28, 'No space left on device')`: C: at 0 bytes free. Cause: `lab/replays` held 75 GB of raw ~10 MB JSON replays (2,761 files).
  - **Fix without deleting data:** gzip-compressed every replay, verifying each `.json.gz` loads before removing its `.json`. 2,724 compressed (~63x, 10.1 MB → 160 KB), **78.4 GB freed** (C: now 74 GB free). `games.replay_path` updated to `.json.gz` for all 2,725 rows; 0 rows point to a missing file.
  - 36 files failed: 0-byte replays written during the disk-full crash (batch h2h-1dbf8501-vs-8951ff93-d8bd60). Those games errored before their ledger rows were written, so no recorded game lost its replay. Files left in place.
  - `lab/arena.py` now writes replays as `.json.gz`; `lab/audit.py` gained `load_replay()` (reads .json or .json.gz). `lab/ladder_replays` (2.5 GB) not compressed yet.
- **`v41_lead264` partial gate (before the crash):** vs v41 28-4-18 (median +3) and 24-1-25 (median 0); vs soil 50-0; **vs v41_rl_1 1-47-2 (median −12)**; final block incomplete. Gate being rerun in full.
- **GATE (rerun, clean): VETO for `v41_lead264`.** vs incumbent v41: 0 paired regressions (24 better); vs parent v41: 0 regressions (23 better); vs soil 50-0; vs v41_rl_1 3-47; **final untouched block 910000-910024: 4 paired regressions** → veto. So the earlier sell lead helps on most seeds but does worse than the v41 mirror on some unseen ones, and it's dominated by v41_rl_1 either way. Finding "lead window" gets 1 veto.
- Gate display note: the "raw W-L" line counts ties as wins (results minus losses); the paired counts are exact. Minor, not fixed yet.
- Disk after the full rerun (~300 games): C: 73 GB free, lab/replays 1.5 GB. Gzip replays are working.

## Iteration 10 — 2026-09-15 (local)

**Ladder:** v41 2448.9 · c94 1010.1. `v41_rl_1` (gate PASS) still not submitted by the user. That's the current bottleneck.
**Housekeeping:** gzipped all 83 ladder replays (2.61 GB → 42 MB, each verified before its original was removed). goal.md step 1 now skips episodes that already have `.json` or `.json.gz` and says to gzip new downloads and read them with `lab.audit.load_replay`.
**No new candidate this iteration.** Blocked/vetoed so far: survival guard (c94), all-sells-first, fertilizer-first, lead264. Remaining queued ideas are thin: the step-1 wheat-bridge opening, and combining lead264's earlier lead with v41_rl_1's carrot tie-break (lead264 alone vetoed on 4 final-block regressions).

## Iteration 11 — 2026-09-15 (local)

**Ladder:** v41 2445.1, **94 episodes: 69W-19L-6T**. `v41_rl_1` still not submitted.
**11 new replays** (downloaded, gzipped): another exact-clone tie (Saifuddin, 719/719 identical); **ansheng jhang −13**, identical except the turn-0 wheat opening (`BUY 20, SELL 5, SELL 15` vs v41's `BUY 5, BUY 10, SELL 60`); Aleksey SCHUKIN +31 (wheat buy/sell tweaks); LS −635, Liu Classmate −1,709, 岸本湧士郎 −2,201 (market variants, ~500-570 identical market turns).
**Candidate `v41_open20`** (29765c51, parent opp_v41): turn-0 opening replaced with ansheng jhang's, only when v41 proposes its default. Verified in a live env that the override fires on turn 0 (smoke vs starter unchanged at 149,771 because starter doesn't contest wheat). Gate running (others: soil, v41_rl_1).

**Submitted `v41_rl_1`** as challenger at the user's explicit request: submission **56251547**, archive sha256 prefix 52f02cb8, message `lab:v41_rl_1 sha:7b783b60 challenger`. Active slots: {v41 56242588 champion, v41_rl_1 56251547 challenger}; c94 dropped out. Submissions today: 2 of 5. Promote/retire after ≥30 ladder episodes (score vs v41).
- **GATE: PASS for `v41_open20`.** vs v41 46-4 / 49-1 / final block 49-1, **0 paired regressions** everywhere (42, 47 games better than the mirror), median +13; vs soil 50-0; **vs v41_rl_1 19-25-6** (median −1).
- **Not submitted (decision):** the challenger slot already holds v41_rl_1, which beats open20 locally. Submitting open20 would push champion v41 out of the latest 2 and force a v41 resubmit: 4 of 5 daily submissions for a weaker challenger.
- **Next:** `v41_rl_2` = v41_rl_1 + open20's turn-0 opening (independent changes: turn-0 wheat vs carrot sell residual). Registered with parent v41_rl_1; gate running (incumbent v41, others soil + v41_open20). If it passes and beats v41_rl_1, it replaces v41_rl_1 as challenger per the Claude-submits rule.
- **GATE: PASS for `v41_rl_2`** (parent v41_rl_1, incumbent v41). vs v41 46-4 (median +26) and final block 49-1 (+24), 0 paired regressions; **vs parent v41_rl_1 49-1 (+13), 0 regressions**; vs v41_open20 49-1 (+14); vs soil 50-0. The strongest candidate so far.
- **Held, not submitted: `ready_to_submit: v41_rl_2`.** Kaggle deactivates the oldest active submission, which is champion v41 at 2449.8. Submitting now would leave active only v41_rl_1 (832.9, 2 ranked games) and a new 600 entry. Resubmitting v41 would restart it at 600. **Slot rule in goal.md corrected** accordingly.
- **Trigger to submit v41_rl_2:** v41_rl_1's ladder score within ~100 of v41's, at which point v41 can be dropped safely. Package it (`lab/packages/v41_rl_2/submission.tar.gz` + `lab.registry --check-package`) before submitting.
- **v41_rl_1 ladder so far:** 2-0 ranked (vs Oğuz Karabulut +37.7k, Abimael Firstana #2 +114k), score 832.9; validation self-play not ranked; logs show no Traceback/errors.

## Iteration 12 — 2026-09-15 (local)

**Ladder:** v41 56242588 **2459.8** · v41_rl_1 56251547 **1123.3**, 5-0 ranked (Oğuz Karabulut +37.7k, Abimael Firstana #2 +114.4k, JohnBlake +39.6k, Stcey Cong +36.8k, wangbin.dev +27.0k). Still climbing through low-rated opponents.
**v41_rl_2:** packaged `lab/packages/v41_rl_2/submission.tar.gz` (main.py sha8 1d0bd51b, verified against the ledger; 460 KB). Package check OK (reward 149,653). **Held:** the gap v41 − v41_rl_1 is 1,336, over the ~100 trigger.
**Submissions today:** 2 of 5.

## Iteration 13 — 2026-09-15 (local)

**Ladder:** v41 2455.8 · v41_rl_1 **1623.4** (12 ranked episodes). Gap 832, still over the ~100 trigger, so v41_rl_2 stays held (packaged, checked). Submissions today: 2 of 5.
**v41_rl_1 ranked record: 11-1.** Only loss: 109253338 vs "Một hai ba bốn 5 sáu bảy tám 9", −2,478 (we were seat 1). Opponent plays **v41's field** (farmer ops identical on 715/719 turns) with a **different market layer** (518/719 identical market turns). Same class as the neibyr/Levin/Himanshu market variants that beat v41. Our farm ended with 5 sheep vs their 3 plus 2 empty pastures, so the field outcome is similar; the gap is market-side. The carrot tie-break doesn't cover this class; it needs a stronger market policy (next RL target: train against market-variant behaviour).

## Iteration 14 — 2026-09-15 (local)

**Ladder:** v41 2455.3 · v41_rl_1 **1867.2**, **18-1** in 19 ranked episodes (the only loss is still the market variant, −2,478; no other close games yet). Gap 588, still over the ~100 trigger: v41_rl_2 stays held (packaged, checked). Submissions today: 2 of 5.

## Iteration 15 — 2026-09-15 (local)

**Ladder:** v41 2458.9 · v41_rl_1 **2057.6**, **37-6** in 43 ranked episodes. Gap 401, still over the ~100 trigger: v41_rl_2 stays held.
**v41_rl_1 losses (6):**
| episode | opponent | margin | farmer ops same as ours | market same |
|---|---|---|---|---|
| 109253338 | Một hai ba bốn… | −2,478 | 715/719 | 518 |
| 109274253 | GanadorPlusUltra | −2,501 | 695 | 554 |
| 109276597 | e0970145 | −2,124 | 304 | 339 |
| 109272378 | qq牧场 | −4,138 | 645 | — |
| 109279815 | Hamachi | −3,308 | 695 | — |
| 109281690 | Giulio Ravasio | −5,369 | 718 | — |
- 5 of 6 losses are to **v41-field variants** (farmer ops 645-718/719 identical) with different market layers; 1 (e0970145) is a genuinely different farm. Close wins vs the same class: joinus +809, tongmian1314 +517, Blue Rain +773, Aurora wy +2,084, Sean Peppers +1,260.
- **No exact-clone ties yet**, so the carrot tie-break is still untested on the ladder (clones sit near 2,400, and rl_1 hasn't reached them).
- **Pattern:** at this rating, losses are about **market strategy** against v41-field variants, decided by 2-5k coins. Tie-break tweaks can't address that. It needs a genuinely stronger market layer. **Next Phase 2 target:** a market-variant opponent pool. Candidate approach: extract each variant's market decisions from the ladder replays (their field matches v41, so state→market pairs are usable for behaviour cloning their market layer), build `opp_mv_*` agents = v41 field + cloned market policy, and use them in RL and the gate.
Submissions today: 2 of 5.

## Iteration 16 — 2026-09-15 (local)

**Ladder:** v41 2459.6 · v41_rl_1 **2086.3** (46 ranked). Gap 373: v41_rl_2 stays held.
**Opponent pool refresh from the newest public notebooks** (`kaggle kernels list --sort-by dateRun`): the v41 author has published **V42** and **V43**, a plausible source of the v41-field / different-market variants beating us on the ladder. Registered:
- `opp_v43` 919fc1d6: Ahmed Berat Özer V43 "Recovering Lost Harvests", bytes written by the notebook's own verified writer cell (sha matches its pin). Smoke 146,016.
- `opp_v42` 728fdfb4: V42 "Production That Fits the Market", `%%writefile` cell, sha matches its pin. Smoke 146,016.
- `opp_fsv5` d868d087: lynnsakurai Farming Score V5 "Timing Optimized". Smoke 149,771.
- `opp_s2710` 31ee22dc: lime0001 Score2710 t23 (kernel script used as the agent). Smoke 146,019.
**Round robin running:** {v41, v41_rl_1, v41_rl_2, v43, v42, fsv5, s2710} on 940000-940009 (fresh block), both seats, 420 games.

## Iteration 17 — 2026-09-16 (local)

**Ladder:** v41 2447.4 · v41_rl_1 **2154.7**.
**Round robin tourney-ec247f7b** (940000-940009, both seats, 420 games; it finished even though the previous session ended mid-wait):
| agent | BT elo | W-L-T |
|---|---|---|
| **opp_v43** | 1912 | 93-14-13 |
| opp_v42 | 1818 | 81-26-13 |
| opp_fsv5 | 1706 | 64-41-15 |
| v41_rl_2 | 1696 | 70-50-0 |
| v41_rl_1 | 1599 | 56-64-0 |
| opp_v41 | 1430 | 29-78-13 |
| opp_s2710 | 340 | 0-120 |
Key head-to-heads: **V43 vs v41 15-1-4 (+2,493), vs v41_rl_2 15-5 (+2,465), vs V42 14-2-4 (+143).** V42 vs v41 15-1-4 (+2,374). v41_rl_2 still beats v41 17-3 and v41_rl_1 17-3 (small margins). This explains the ladder: v41-field agents with V42/V43-style market layers beat the v41 family by ~2.5k.
**Decision: V43 becomes the champion base.** Package `lab/packages/v43/submission.tar.gz` is byte-identical to the notebook's pinned archive (sha f76baf85…); package check OK (reward 146,016). Gate running (parent/incumbent v41; others v41_rl_2, V42, soil).
**Slot question for the submit:** active = {v41 2447.4 (oldest), v41_rl_1 2154.7}. Submitting V43 deactivates v41 while rl_1 is 293 below it, which the current slot rule forbids. The rule's purpose is to not trade a proven score for a weaker entry; V43 locally dominates v41 with a 95% CI of 64-95% win rate. Adding an exception to the rule: allowed when the new submission beats the champion head to head with a Wilson 95% lower bound > 50% over ≥20 both-seat games, and it has passed the gate.

**User decision (2026-09-16): option 1, fall back to the one-change loop on the V43 base.** Recorded in goal.md ("Phase 2 outcome"). Full IL+RL with production choices is parked unless the user re-opens it.
- **GATE: VETO for `opp_v43`** (narrow): vs incumbent v41 on 850000-850024 raw 45-5 but **4 paired regressions** (39 games better); vs parent v41 on 860000-860024 49-1, **0 regressions**; vs v41_rl_2 40-10; vs V42 49-1; vs soil 50-0; audit 0 critical.
- **Submitted anyway on the user's explicit instruction ("no need to wait upload"): submission 56266006**, `lab:opp_v43 sha:919fc1d6 champion`, archive byte-identical to the notebook's pinned sha f76baf85. Active slots now {v43 56266006, v41_rl_1 56251547 2230.9}; **v41 (2385.1) deactivated** — it was the oldest.
- Note: v41's score has drifted down (2459 → 2385) while v41_rl_1 climbs (2230.9), so the cost of dropping v41 is smaller than when the slot rule was written.

## Iteration 18 — 2026-09-16 (local)

**Ladder:** v43 56266006 PENDING (0 ranked episodes yet) · v41_rl_1 2230.9. Submissions today (UTC 2026-09-16): 1 of 5.
**Candidate `v43_carrot`** (af60f83c, parent opp_v43): ports v41_rl_1's single learned knob (carrot sell fraction +0.15) onto V43 as a small deterministic overlay instead of the 710 KB weights file — the learned policy was a constant, so the network was dead weight. Extra carrot appended in the last slot; WHEAT/FERTILIZER untouched; no existing slot reordered. Smoke vs starter 145,938 (V43 146,016). Gate running (parent/incumbent V43; others V42, v41_rl_2).
- **GATE: PASS for `v43_carrot`.** vs V43: 46-4 / 46-2-2 / final block 41-1-8, **0 paired regressions** in all three (42, 44, and final better-than-mirror counts), median +13/+13/+10; vs V42 49-1 (+57); vs v41_rl_2 42-8 (+2,063, i.e. V43's own edge). Audit 0 critical.
- Packaged `lab/packages/v43_carrot/submission.tar.gz` (sha8 af60f83c), package check OK.
- **Held briefly:** active = {v43 56266006 (pending, 600), v41_rl_1 56251547 2230.9 (oldest)}. Submitting now would deactivate the only proven score and leave two unproven entries. **Submit as soon as v43's public score reaches ≥ v41_rl_1's** (or within ~100), which also satisfies the corrected slot rule.

## Iteration 19 — 2026-09-16 (local)

**Ladder:** v43 56266006 **1076.1**, **7-0** ranked (margins +25.6k to +118.5k, all vs non-v41-family farms — farmer ops match on only 61-92/719 turns) · v41_rl_1 2241.5.
**`v43_carrot` still held** (packaged, gate PASS): submitting deactivates v41_rl_1 (oldest, 2241.5) while v43 is only at 1076. Trigger unchanged: submit when v43 ≥ v41_rl_1 or within ~100.
**No new candidate this iteration** (v43 has no losses to diagnose yet).
Submissions today: 1 of 5.

## Iteration 20 — 2026-09-16 (local)

**Ladder:** v43 **1479.0**, **12-1** in 13 ranked · v41_rl_1 2250.9. `v43_carrot` still held (trigger: v43 ≥ v41_rl_1 or within ~100).
**V43's first loss — episode 109493975 vs "Shun", −1,928, identical field on all 719 turns**, 65 differing market turns:
- turn 0 opening: theirs `BUY_PRODUCT WHEAT 55 / SELL WHEAT 55` vs V43's `BUY 5 / BUY 10 / SELL 60`
- step 18: they buy 2 melon seeds, V43 buys 1 (production difference)
- they sell MILK at 299 vs our 302, EGG at 375 vs our 381 — **3-6 steps earlier**, a longer lead than V43's own 1-2 step window
**Candidate `v43_open55`** (parent opp_v43): the opening only, applied on turn 0 and only when V43 proposes its default. Gate running (others: v43_carrot, V42). The earlier-sell-lead and melon-seed differences stay queued as separate one-change candidates.
- **GATE: PASS for `v43_open55`, and it is a large gain, not a tie-break:** vs V43 **50-0 (median +1,280)**, 49-1 on the parent block, 50-0 on the final untouched block, **0 paired regressions** everywhere; vs `v43_carrot` 50-0 (+1,269); vs V42 50-0 (+1,300). Audit 0 critical.
- **Submitted: 56267455** `lab:v43_open55 sha:a86e80f9 challenger` (package sha8 a86e80f9, check OK). Slot-rule exception applied: it dominates everything we have with a 93% Wilson lower bound vs V43, so waiting made no sense. **v41_rl_1 (2255.1) deactivated**; active = {v43 56266006 1698.9, v43_open55 56267455}.
- So the wheat opening is worth ~1.3k per game on the V43 base, while the same idea on v41 (`v41_open20`, from ansheng jhang) was worth only ~13. **`v43_carrot` (+13) is now superseded**; next candidate: v43_open55 + carrot, then the 3-6 step early sell lead and the 2-melon-seed difference from Shun's replay.
- Submissions today: 2 of 5.

## Iteration 21 — 2026-09-16 (local)

**Ladder:** v43 1698.9 · v43_open55 56267455 at the 600 start, 0 ranked episodes yet.
**Reading V43's own lead logic:** `_R37_HORIZONS[player]` is 2 by default, 3 when the opponent's farm looks ≥90% similar for 6 straight turns in 336-647, 4 when a probe matches, and **hard-set to 4 for steps 288-695**. Shun sold MILK 3 and EGG 6 steps early, so their horizon is longer than 4.
**Candidate `v43_lead6`** (parent v43_open55): one literal, the 288-695 horizon 4 → 6. Built on top of open55 since that is now the strongest base. Gate running (incumbent/parent v43_open55; others V43, V42).
Submissions today: 2 of 5.
- **GATE: VETO for `v43_lead6`** (narrow): vs incumbent v43_open55 46-4 with **2 paired regressions** (42 better, median +1,114); vs parent v43_open55 48-2 with **0 regressions** (+1,390); vs V43 50-0 (**+3,161**); vs V42 50-0 (+3,337). So horizon 6 is worth ~1.2k on top of the opening but regresses on 2/50 seeds.
- **Next step, `v43_lead5`:** same literal set to 5 instead of 6 (smaller step). Gate running with others = V43 and v43_lead6, so the two horizons are compared directly.

**User rules (2026-09-16):** (1) **submission freeze** — no new submissions until both active submissions (v43 56266006, v43_open55 56267455) each have ≥150 ranked episodes; gated candidates wait as `ready_to_submit`. (2) Loop cadence 30 min → **2 h** (cron bb97acf5, at :07). (3) Watcher `lab/wait_150.sh` checks both counts every 3 h and exits when both reach 150, which notifies the session to resume goal.md submissions.
- **GATE: VETO for `v43_lead5`**, and it is *worse* than lead6: vs incumbent v43_open55 47-3 (2 paired regressions, +1,027); vs parent 44-6 (**4 regressions**, +1,346); vs V43 50-0 (+3,156); **vs v43_lead6 0-50 (−1,193)**.
- **Measured ordering on this base: horizon 6 > 5 > 4.** Longer lookahead is better, so the next test goes up, not down: `v43_lead8` (horizon 8), gated against v43_open55 with v43_lead6 in the pool for a direct comparison.
- **Leaderboard context (9,186 teams, pulled today):** gold = top 28 (score 2,919.6), silver = top 459 (2,643.0), bronze = top 918 (2,421.9). We are rank 1,803 at 1,847.6 (V43 still climbing); v41 peaked at ~2,460, about rank 850. Cutoffs drift as others improve.
- **GATE: PASS for `v43_lead8`** (horizon 4 -> 8 on the v43_open55 base): vs v43_open55 49-1 / 48-2 / final block 50-0, **0 paired regressions anywhere** (+1,153 / +1,407 / +1,122 median); **vs v43_lead6 50-0 (+1,421)**; vs V43 50-0 (+2,978). Audit 0 critical. Packaged at `lab/packages/v43_lead8/` and package-checked; **held by the submission freeze** as `ready_to_submit`.
- **Ordering now 8 > 6 > 5 > 4.** Interesting: the strict veto rejected the intermediate steps (5 and 6 regressed on 2-4 seeds) but the larger jump to 8 regresses on none. Testing `v43_lead12` next to find the ceiling.
- **GATE: VETO for `v43_lead12`** (horizon 12): vs v43_open55 46-4 with 2 paired regressions on both blocks, **but beats `v43_lead8` 48-2**. So raw strength keeps rising with the horizon while mirror-regressions reappear past 8. **`v43_lead8` is the best clean pass and stays the ready_to_submit candidate.** Horizon search closed: 4 (base) < 5 < 6 < 8 (PASS) < 12 (VETO).
- **Top-team replay pull (user request):** no games of ours vs Majkel1337 (rank 1, 3,183.2). Kaggle publishes daily episode dumps (`kaggle/kaggriculture-episodes-<date>`, ~634 MB zipped / ~21 GB raw, 652 episodes for 2026-09-15) plus a tiny index dataset. Extracting only the Majkel1337 episodes to `lab/top_replays/majkel1337/` as .json.gz, then deleting the dump (user: "make sure to clean everything").

## Iteration 22 — 2026-09-16 (local)

**Ladder:** v43_open55 56267455 **2543.3** (80 ranked, **69-11**) · v43 56266006 2146.6 (84 ranked). Today's medal cutoffs: bronze 2,421.9 / silver 2,643.0 / gold 2,919.6 — open55 is above bronze.
**v43_open55's 11 losses: 10 are identical-field mirrors** (farmer ops match on 694-719/719 turns), decided on the market layer alone: Canon −1, Max vrstpan1 −1, Pilea55 −22, 一路向北 −293 and −3,271, Ng −302, Superman king −397, Peng Wang −865, Justin Yang −1,440, Sam-wiz −2,394. Only "Ad Space Available" (−3,927) was a different farm (74/719).
**Two losses by a single coin** → the carrot tie-break (median +13 vs an identical clone) targets exactly this.
**Candidate `v43_open55_carrot`** (parent v43_open55): carrot sell fraction +0.15 on the open55 base. Gate running (others: v43_lead8, V43).
**Watcher restarted** (`lab/wait_150.sh`, 3 h interval) after the previous session ended: v43 84/150, v43_open55 80/150 ranked episodes.
- **Submitted `v43_lead8` (56274046)** on the user's instruction ("push the next best agent"), **overriding the 150-episode freeze** at v43 84 / v43_open55 80 episodes. Package check OK (reward 145,721). Active slots now {v43_open55 56267455 2545.0, v43_lead8 56274046}; **v43 (2146.6) deactivated** as the oldest. The freeze stays in goal.md for future candidates unless the user lifts it again.

## Iteration 23 — 2026-09-16 (local)

**Rank 246 of 9,232 teams, score 2,759.8 — inside silver.** Today's cutoffs: gold top 28 = 2,923.7, silver top 461 = 2,680.3, bronze top 923 = 2,440.9.
**Ladder:** v43_lead8 56274046 **2763.2** (62 ranked, **54-8**) · v43_open55 56267455 2605.7 (104 ranked, 69-11).
**Lab bug fixed:** `lab.audit.audit_batch` crashed on `Path(None)` for rows with no replay (harness-error rows and p2 batches); it now skips them. The `v43_open55_carrot` gate had died at its audit step and was rerun.
- **GATE: PASS for `v43_open55_carrot`** (46-4 / 48-2 / 49-1 vs v43_open55, 0 paired regressions) **but 0-50 vs v43_lead8** → superseded, not submitted.
- **v43_lead8's 8 ladder losses are all identical-field mirrors** (farmer ops 714-719/719), decided on the market layer: −43, −254, −1,138, −1,188, −1,306, −1,336, −1,534, −2,046. Two are small enough for a tie-break to flip.
**Candidate `v43_lead8_carrot`** (parent v43_lead8): carrot tie-break on the current champion. Gate running (others: v43_open55, V43).
- **GATE: PASS for `v43_lead8_carrot`.** vs parent v43_lead8: 46-4 / 48-2 / final block 49-1, **0 paired regressions** in all three (median +10 — a tie-break, as designed); vs v43_open55 50-0 (+1,240); vs V43 50-0 (+2,980). Audit 0 critical. Packaged (`lab/packages/v43_lead8_carrot/`, package check OK).
- **Held as `ready_to_submit`:** the 150-episode freeze is the standing rule and the earlier v43_lead8 push was an explicit one-off override. Submitting would displace v43_open55 (2,612.9, oldest) for an unproven entry whose local edge over v43_lead8 is only ~10 coins. Say the word to push it.

## Iteration 24 — 2026-09-16 (local)

**Ladder:** v43_lead8 2760.6 (81 ranked, **63-18**) · v43_open55 2612.4 (113 ranked). Watcher restarted after the session ended.
**19 new v43_lead8 replays. All 18 losses are identical-field mirrors** (farmer ops 706-719/719 except one at 573), decided on the market. Diffing the closest ones shows a single contested decision — **the turn-0 wheat opening size**:
| loss | opponent's opening | margin | differing market turns |
|---|---|---|---|
| 109659811 c_fxy | `BUY 50 / SELL 50` | −43 | **1** (only the opening) |
| 109667337 KongKongDe | `BUY 43 / SELL 38` | −240 | 5 |
| 109669964 Madiyar Khamzanov | `BUY 7 / SELL 7` | −243 | 4 |
| 109626675 Peng Wang | `BUY 20 / SELL 15` | −254 | 4 |
Ours is `BUY 55 / SELL 55`. In the c_fxy game that one turn is the *entire* difference between the two agents, and 50 beat 55. Knock-on effects in the others: at step 21 we buy 0 wheat seeds where they buy 2, and at steps 171/195 we buy 2 wheat they don't.
**Sweep built:** `v43_lead8_open50`, `_open43`, `_open20` (parent v43_lead8), round robin with v43_lead8 and v43_lead8_carrot on a fresh block 960000-960009, both seats.

## Iteration 25 — 2026-09-17 (local)

**Opening-size sweep (tourney-d0f7b9fa, 970000-970009, 156 of 200 games before the session died):**
| agent | BT elo | W-L |
|---|---|---|
| **v43_lead8_open20** | 2981 | 56-0 |
| v43_lead8_open43 | 2085 | 40-16 |
| v43_lead8_open50 | 1205 | 38-42 |
| v43_lead8_carrot (55) | 813 | 20-20 |
| v43_lead8 (55) | 416 | 2-78 |
Head-to-head medians: open20 beats open43 by +316 and open50 by +1,290; **lead8 (55) loses to open50 by −43, exactly the margin of the real ladder loss to c_fxy (−43)** — the diagnosis reproduces.
**Smaller is better across 55 → 20**, so `open7`, `open12`, `open15` were built and are in a round robin with open20 on 990000-990009.
**Background jobs now launched detached** (PowerShell Start-Process) so they survive a session restart; the earlier in-session jobs died three times. Logs: `lab/reports/open_sweep3.log`, `open_sweep_small.log`.
Ladder unchanged: v43_lead8 2760.6, v43_open55 2612.4; freeze holds (81 / 113 of 150).
- **Sweeps complete.** Full block 980000-980009 (200 games): open20 76-4 (elo 2053) > open43 58-22 > open50 40-40 > carrot(55) 22-58 > **v43_lead8 (55) 4-76**. Small block 990000-990009 (120 games): **open7 57-3 > open12 39-21 > open15 21-39 > open20 3-57**, but the head-to-head medians are only 13-28 coins, against 1,290 for 20-vs-50. **The curve is steep from 55 down to ~20 and nearly flat below that.**
- Built `open0` and `open3`; tiny-range sweep running on 991000-991014. **Gate started for `v43_lead8_open7`** (parent/incumbent v43_lead8; others v43_open55, V43, v43_lead8_carrot).
- Both launched detached via Start-Process so a session restart cannot kill them.

## Iteration 26 — 2026-09-17 (local)

**Ladder:** v43_lead8 **2723.4**, now **93-55 (62.8%)** over 148 ranked — the win rate fell from 87% as it climbed into stronger company. v43_open55 2558.4.
**Loss analysis by the opponent's turn-0 wheat buy (ours is 55):**
| their opening | our record | win rate | median margin |
|---|---|---|---|
| 0-9 | 9-22 | **29.0%** | −144 |
| 10-29 | 29-10 | 74.4% | +1,456 |
| 30-49 | 10-10 | 50.0% | +14 |
| 50+ | 45-13 | 77.6% | +1,294 |
We beat every big opener and lose to nearly every small one; a buy of 5 is the most common opening among agents that beat us (14 of our losses). This matches the local sweep from the other side.
**Tiny sweep (tourney-0fd80277, 991000-991014, 90 games):** open3 30-0 over open7 (median +7); **open0 ties every game against both** (a zero-size order appears to be dropped, so it is not a distinct strategy). Local optimum is ~3-7.
- **GATE: VETO for `v43_lead8_open7` by one game** — incumbent block 48-2 with **1 paired regression** (44 games better), parent block 49-1 with **0**; vs v43_open55 50-0, vs V43 50-0, vs v43_lead8_carrot 45-5.
- **Gate running for `v43_lead8_open3`** (others: open7, v43_open55, V43).

## Iteration 27 — 2026-09-17 (local)

- **GATE: PASS for `v43_lead8_open3`** — vs v43_lead8 46-4 / 48-2 / final block 49-1, **0 paired regressions anywhere**; vs v43_lead8_open7 49-1; vs v43_open55 50-0; vs V43 50-0. Audit 0 critical.
- **Freeze condition met** (v43_lead8 168 ranked, v43_open55 193, both ≥150), so the normal submit rules resumed. **Submitted 56298354** `lab:v43_lead8_open3 sha:774a7f56`. Active = {v43_lead8 56274046 2666.0, v43_lead8_open3 56298354}; **v43_open55 (2518.0) deactivated** as the oldest.
- Ladder trend to watch: both live agents are drifting down (v43_lead8 2763 → 2666, v43_open55 2612 → 2518) as they meet the stronger field. open3 targets the exact bucket behind that: opponents opening 0-9 wheat, where v43_lead8 wins only 29%.

## Iteration 28 — 2026-09-17 (local)

**Ladder:** v43_lead8_open3 56298354 **2044.9** after 29 ranked, **24-5 (82.8%)** — still climbing from 600. v43_lead8 56274046 2631.5 (181 ranked).
**The opening fix is confirmed on the ladder**, in the bucket it targeted:
| opponent's turn-0 wheat buy | v43_lead8 (opens 55) | v43_lead8_open3 (opens 3) |
|---|---|---|
| 0-9 | 29.0% (9-22), median −144 | **70.0% (7-3), median +15,042** |
| 10-29 | 74.4% | 81.8% (+7,030) |
| 30-49 | 50.0% | 100% (8-0, +3,560) |
| 50+ | 77.6% | no games yet |
Same farm, one number changed (55 → 3). Nothing else touched.
**Next:** let open3 accumulate games; when it passes v43_lead8's score it becomes champion. Queued candidates on the open3 base: the carrot tie-break (gated PASS on other bases, +10 median) and re-testing horizon 12, which lost only on paired regressions before the opening was fixed.

## Iteration 29 — 2026-09-17 (local) — subagent loss analysis across three agents

Full replay set pulled (194 + 183 + 40 episodes, 122 newly downloaded and gzipped; no raw .json left).
| agent | n | W-L | win rate | median margin | score |
|---|---|---|---|---|---|
| v43_open55 (deactivated) | 194 | 122-72 | 62.9% | +674 | 2513.9 |
| v43_lead8 (champion) | 183 | 101-82 | 55.2% | +393 | 2631.1 |
| v43_lead8_open3 (challenger) | 40 | 30-10 | **75.0%** | +4,236 | 2065.0 |
**>90% of all losses are same-farm mirrors** (70/72, 79/82, 9/10). Only 4 different-farm losses across 574 games.
**Catalogued ideas, re-tested at scale:**
- **Steps 171/195 wheat top-up — CONFIRMED and now precise.** In **26 of v43_lead8's 79 mirror losses** (34.2%) we place `BUY_PRODUCT WHEAT 1-2` at step 171 and again at 195 while the opponent places no wheat order; never the reverse. My own count: exactly steps 171 (26 games) and 195 (26 games), plus a 17-game tail of one-off steps. Examples: ep 109626675 (−254), 109667337 (−240), 109669964 (−243), 109540782 (−865), 109722634 (−1,703).
- **Step-21 wheat-seed buy — REFUTED.** Never exceeds 2 of 79 games; the earlier read came from a 4-game sample.
- **Milk/egg sold 3-6 steps early — REFUTED.** Rank-paired sell-step deltas have median 0 for both items on both agents; no directional bias.
- **Late-game sell-timing desync across many steps** looks big by frequency (40-60 of 70-79 games) but has no consistent lead/lag direction — trajectory divergence, not a fixable decision. Not pursued.
- **open3's small-opener fix holds but is smaller than the n=29 snapshot:** 0-9 bucket 58.3% vs v43_lead8's 23.3% (+35 points), down from the earlier 70% read.
- **No bugs:** all 164 loss replays end DONE/DONE, no errors, no unsold produce at terminal.
- **GATE: PASS for `v43_open3_carrot`** — vs incumbent/parent v43_lead8_open3 46-4 / 48-2 / final 49-1, **0 paired regressions anywhere**; vs v43_lead8 49-1; vs open7 49-1; vs V43 50-0.
- **Candidate `v43_open3_notopup`** (parent v43_open3_carrot): drops only the ≤2-wheat top-up buys at steps 171 and 195. Gate running.
- **Not submitted yet:** active slots are {v43_lead8 2631.1 (oldest), v43_lead8_open3 2065.0}. Submitting now would drop our best live score for two unproven entries. **Submit the best gated candidate once open3's score passes v43_lead8's**, then the displaced slot costs nothing.

## Iteration 30 — 2026-09-17 (local)

**Ladder:** v43_lead8 2627.4 (champion) · v43_lead8_open3 **2089.9**, climbing.
**`v43_open3_notopup` gate (final block still running):** vs its parent `v43_open3_carrot` **2-2 with 46 ties, median 0** — dropping the step-171/195 wheat top-ups changes the outcome in only 4 of 50 games. Its wins elsewhere (vs v43_lead8_open3 46-4 +10, vs v43_lead8 49-1 +45, vs V43 50-0 +1,249) are inherited from the carrot tweak, not from the change under test.
**Reinterpretation of the top-up finding:** it shows up in 34% of mirror losses, but the local test says removing it is ~neutral. Most likely the top-up is a **marker of which variant we face** (agents that skip it are the same ones opening small, which is what actually beats us) rather than a cause. Correlation, not causation — the loop's diff method can't separate the two without a controlled test, and this is the controlled test.
**Consequence:** `v43_open3_carrot` remains the best gated candidate; `v43_open3_notopup` adds nothing measurable and is not worth a submission slot on its own.
**Still holding submissions:** active {v43_lead8 2627.4 (oldest), v43_lead8_open3 2089.9}. Submit v43_open3_carrot once open3's score passes v43_lead8's.

## Iteration 31 — 2026-09-17 (local)

**Ladder:** v43_lead8 2630.3 (193 ranked) · v43_lead8_open3 **2156.0** (79 ranked), still climbing; submissions stay held until open3 passes the champion.
**`v43_open3_notopup` final verdict: PASS**, but neutral (46/50 ties vs its parent) — recorded as a no-op, not submitted.
**Candidate `v43_open3_lead12`** (parent v43_open3_carrot): sell-reservation horizon 8 → 12 on the fixed-opening base. On the old open55 base horizon 12 beat horizon 8 48-2 yet was vetoed on 2 paired regressions; the hypothesis is that those regressions came from the bad 55 opening interacting with the longer lead, not from the horizon itself. Gate running (incumbent v43_lead8_open3, others v43_lead8, V43).

## Iteration 32 — 2026-09-18 (local)

- **GATE: VETO for `v43_open3_lead12`** — 2 paired regressions on both the incumbent and parent blocks (46-4 each), vs v43_lead8 48-2, vs V43 48-2. Horizon 12 regresses on a couple of seeds on the fixed-opening base too, so the "bad opening caused the regressions" hypothesis is **refuted**. Horizon 8 stands; the horizon search is closed for good.
- **Submitted `v43_open3_carrot` (56318537)** on the user's instruction. Package sha8 1367897a, check OK. Active = {v43_lead8_open3 56298354 2217.1, v43_open3_carrot 56318537}; **v43_lead8 deactivated at 2474.3** — it had decayed from 2763 as it met the stronger field, so the displaced score cost less than it would have a day ago.
- Ladder at submit time: open3 2217.1 (climbing), v43_lead8 2474.3 (falling). Submissions today: 1 of 5.

## Iteration 33 — 2026-09-18 (local) — diagnosis only, no candidate built

No candidate this iteration. Three leads were examined against the full ladder-replay
population (529 games across 56274046 / 56298354 / 56267455) and **all three died**. Recording
them in full so a later session does not re-open them.

### Dead lead 1 — "buy 2 wheat seeds at step 21" (REFUTED, do not rebuild)

Cluster-C diffing (49 same-farm/near-same-market games) showed step 21 differing in 10/17 losses
vs 3/32 wins: we emit `BUY_SEED WHEAT 0` or `1`, winners emit `2`. Population check looked like a
confirmation:

```
we bought 0 seeds @21:   3W- 19L  (13.6%)
we bought 1 seed  @21:   2W- 25L  ( 7.4%)
we bought 2 seeds @21: 296W-152L  (66.1%)
```

**It is not causal.** `_r124_seed_budget` (`lab/candidates/v43_lead8_open3.py:2882`) shaves seed
orders down one unit at a time until they fit the money left after the HIRE reserve. We do not
*choose* 0 or 1 — we get shaved. Confirmed by joining money-at-step-21 onto the same games:

```
seed21=0: n= 22 win=13.6%  money21 median  7.5 (max 13)
seed21=1: n= 27 win= 7.4%  money21 median  6.0 (max 11)
seed21=2: n=480 win=66.5%  money21 median 39.0
```

Every single sub-2-seed game had ≤13 coins. Forcing the buy spends coins we do not have and
raids the labor reserve. **The seed count is a thermometer, not the fever.**

### Dead lead 2 — steps 171/195 wheat top-up (already closed, now explained)

Iteration 31 gated `v43_open3_notopup` and got 46/50 ties. That is consistent with the above: the
top-ups are the same thermometer further along the game. Removing them removes the symptom and
leaves the cash state untouched. Closed for good.

### Dead lead 3 — the subagent's turn-0 wheat-wash finding (CORRECT, but already shipped)

Subagent `a91f11d4978d77df7` classified all 183 replays of **56274046 = `v43_lead8`**, which is the
*old 55-wheat-opening agent*, and reported as its #1 fix: shrink the turn-0 55/55 wheat wash.
Its evidence is good — near-byte-identical 719-turn mirrors where the only diff is the opening,
with turn-1 money deltas of ±40-130 coins, and a clean monotone split (opponent opens <55 → we
lose 95%; opponent opens >55 → we win 91%). It independently reproduces the reason `open3` exists.

**That fix shipped three iterations ago** (`v43_lead8_open3`, gate PASS 0 regressions, submission
56298354). Its headline is stale because it was pointed at a superseded agent. Confirmed on the
current population: `open1 <10 → 66.4% win (n=152)` vs `open1 50+ → 59.2% (n=377)`.

**Lesson for spawning analysis subagents: name the submission id *and* which agent version it is,
or you get a confident report on an agent we already retired.**

### What survived: cash at step 21

The one monotone relationship left standing, and the largest single lever visible in the data:

```
money at step 21  ->  our win rate
  <20 :  n=108   17.6%
 20-40:  n=181   63.0%
 40-80:  n=119   71.4%
  80+ :  n=121   87.6%
```

20% of our games are in the `<20` bucket and we lose 82% of them. **This is not yet established as
causal either** — low cash may simply mark an unfavourable market draw rather than a fixable
decision, and that is exactly the distinction that killed leads 1-3. Diagnostic running
(`$TEMP/poor21.py`, background `bjkais8hv`) splits the poor games by opening size, hire count,
turn-0 wheat price and the opponent's cash, to separate "we overspent" from "the draw was bad".

**Next iteration starts here:** read `bjkais8hv`. If the poor games differ from the rich ones by
something we *choose* (hire count, opening size), that is the next single-change candidate, gated
against `v43_open3_carrot`. If they differ only by the market draw, cash-at-21 joins the dead leads
and Phase C (the rank-1 cow/no-sheep farm) becomes the next move.

### Phase C downgrade (standing)

Cross-agent classification of 176 losses: **only 3.4% come from a genuinely different farm**
(median −5,008). The subagent's independent pass agrees (3/82 = 4%). Re-architecting the farm
chases ~6 losses while risking the 96.6% of games we win on the mirror. Phase C stays parked until
the mirror well is dry.

### Ladder at end of iteration

| agent | submission | score | state |
|---|---|---|---|
| `v43_open3_carrot` | 56318537 | 960.3 | active, climbing from 600 |
| `v43_lead8_open3` | 56298354 | 2221.6 | active |
| `v43_lead8` | 56274046 | 2474.3 | deactivated |
| `v43_open55` | 56267455 | 2513.9 | deactivated |

Best recorded scores are still the two deactivated agents. Gold = 2,923.7 (top 28 of 9,232);
silver 2,680.3; bronze 2,440.9.

## Iteration 35 — 2026-09-18 (cloud agent, fresh checkout)

**Environment:** first iteration run from a cloud container instead of the Windows box.
No `KAGGLE_API_TOKEN` in the environment and no replay directories (all gitignored), so
**steps 1, 2, 6 and 7 of the loop could not run**: no ladder sync, no new-loss forensics,
no submission, no promote/retire. Ladder state below is unchanged from iteration 33.
Steps 3-5 ran normally. `lab/submit.py` already prefers `KAGGLE_API_TOKEN`, so setting it
as a secret is all that is needed to restore the full loop.

### Two infrastructure faults found and fixed (both silent, both fatal to the loop)

**1. Ledger artifact paths are Windows-absolute.** `artifacts.path` holds
`C:\Zeel Australia\...` strings, so `gate._resolve` / `arena.resolve` / `tournament`
returned a path that does not exist and every gate invoked by artifact name died before
playing a game. Added `ledger.artifact_path()`, which falls back to the tracked
content-addressed copy at `lab/artifacts/<sha8>/main.py`. No ledger rows rewritten.
Commit `aa11b51`.

**2. Every agent file had been silently re-hashed by git.** Each agent is a *mixed*
line-ending file: the V43 base (first 3329 lines) was written on Windows with CRLF, every
overlay was appended by Python with LF. Git normalised `lab/artifacts/` and
`lab/candidates/` to all-LF on commit, so in this checkout **29 of 40 artifacts and 25 of
26 candidate sources no longer hashed to their recorded sha256**:

| agent | ledger / submitted tarball | this checkout |
|---|---|---|
| `v43_open3_carrot` | `1367897a` | `164f53ee` |
| `v43_lead8_open3` | `774a7f56` | `f7131cd0` |
| `v43_open3_cash21` | `871a5888` | `3b5b7a67` |

That sha *is* an agent's identity here: it names the artifact directory, keys all 10,449
rows in `games`, and goes into the Kaggle message as `sha:<sha8>`. Left alone, every game
this loop records would be filed under a sha matching nothing in the ledger's history, and
any submission made off Windows would carry a sha8 the ladder has never seen.
`lab/packages/*/submission.tar.gz` is gzip, so git never touched it — those archives were
the ground truth that exposed it (their `main.py` has 3329 CR and hashes to the ledger sha).
Restored all 40 artifacts and 26 candidates, self-verifying (bytes written only when the
sha256 prefix equalled the directory name), and pinned the paths in `.gitattributes`.
Behaviour was never affected — Python ignores line endings — so all recorded results stand.
Commit `b918935`.

### `v43_open3_cash21` (871a5888): NO-OP, retired without a verdict

Iteration 34 registered it and opened a gate batch that logged **0 games** before the
session died. Re-ran it here, and the parent block settled it:

| block | n | result | games at margin exactly 0 |
|---|---|---|---|
| vs parent `v43_open3_carrot` | 50 | 46 T, 4 L | **46** |
| parent mirror (carrot vs itself) | 25 | 23 T, 2 L | 23 |

4 losses in 50 both-seat games against 2 in 25 one-seat mirror games is the gate's known
seat asymmetry, not the candidate. **It is behaviourally identical to its parent.**

**Root cause — a replay-index off-by-one.** Instrumenting the overlay shows the agent emits
the day-0 fill `['BUY_PRODUCT','WHEAT',5]` when its own clock reads `day*24+hour == 1`, and
its market list at `== 2` is **empty**. The candidate tested `== 2` because the fill is
recorded at index 2 of a replay: `steps[i]["action"]` is the action taken from the step
`i-1` observation, so the action slot sits one index after the observation the agent saw.
The overlay's loop matched nothing and returned the action untouched.

**Standing lesson:** a replay index is not the agent's clock. Any overlay keyed to a turn
must be verified firing — one instrumented game, ~20 s — before it is worth a gate.
Gate stopped early rather than spend 25 more minutes proving a no-op.

### `v43_open3_cash21b` (b0f8a324): the same change, one turn earlier

Parent `v43_open3_carrot`, single change: trim one unit off the day-0 `BUY_PRODUCT WHEAT`
fill at agent-clock `== 1`. Targets the one lever left standing in iteration 33's
population analysis — money at the seed-buy turn, where `_r124_seed_budget` shaves the
WHEAT seed order to fit the cash left after the HIRE reserve (`<20`: n=108, 17.6% wins;
`80+`: n=121, 87.6%).

Mechanism verified before gating, seed 850000, against the parent on the same seed:

| | carrot (parent) | cash21b |
|---|---|---|
| money after the day-0 fill | 1052 | **1080** |
| money at the seed-buy turn | 42 | **70** |
| after `BUY_SEED WHEAT 2` | 22 | **50** |

Exactly the +28 coins predicted. Gate running (parent `v43_open3_carrot`, incumbent
`v43_lead8_open3`, others `v43_lead8_open7`, `v43_lead8`, `opp_v43`).

### Ladder (unchanged — could not sync)

| agent | submission | score | state |
|---|---|---|---|
| `v43_open3_carrot` | 56318537 | 863.0 | active, climbing from 600 |
| `v43_lead8_open3` | 56298354 | 2221.6 | active |
| `v43_lead8` | 56274046 | 2474.3 | deactivated |
| `v43_open55` | 56267455 | 2513.9 | deactivated |

### `v43_open3_cash21b` (b0f8a324): VETO — and the cash-at-21 lead is dead

The corrected overlay fires, and the result is decisive in the wrong direction.

| block | candidate record | median margin | games at margin 0 |
|---|---|---|---|
| vs incumbent `v43_lead8_open3` | **0-50** | −7,926 | 0 |
| vs parent `v43_open3_carrot` | **0-50** | −7,014 | 0 |

Contrast with `871a5888`, which tied 46 of 50 at margin exactly 0: this one changes every
single game, so the no-op diagnosis above is confirmed from the other side too.

**Why it loses — wheat at day 0 is not slack cash, it is the seed capital of the animal
economy.** Animals must be fed wheat every day, and two consecutive missed feedings lose
them permanently. One unit trimmed from the day-0 fill starves the early herd, and the gap
compounds for the rest of the season. Same seed (860000), candidate vs parent, p0's herd:

| step | cash21b | carrot |
|---|---|---|
| 48 | 3 | 4 |
| 72 | 4 | 5 |
| 120 | 5 | 6 |
| 240 | **10** | **13** |

Three fewer producing animals across the last ~480 turns. Carrot against itself on that seed
ties exactly (93,164 vs 93,164), so this is the change, not variance.

**Consequence for the finding queue — "money at the seed-buy turn" is closed.** Iteration 33
found it monotone (`<20`: 17.6% wins, `80+`: 87.6%) and flagged it as not yet causal. It is
not causal: buying cash with wheat costs far more than the seed it buys. That makes four
leads from the same cluster that were all thermometers rather than fevers — the step-21 seed
count, the step-171/195 top-ups, and now cash at the seed turn. **They are all downstream of
the same thing: how much wheat the day-0 draw lets us hold.** Any future candidate that tries
to move cash early must add wheat, not spend less of it.

**Do not retry:** trimming the day-0 `BUY_PRODUCT WHEAT` fill, in any amount. The direction is
wrong, and the mechanism (herd starvation) says a smaller trim only scales the loss down.

**Next finding to try.** The mirror well is not dry, but this cluster is. The remaining
untested items from the gold plan's Phase B are the terminal liquidation order and the
contested late-game market turns; Phase C (the rank-1 cow-heavy farm) is still parked at 3.4%
of losses. Given that the herd size is what this iteration showed to drive the margin, the
most promising untried single change is on the other side of the same lever: **buy *more*
wheat on day 0 and see whether the herd compounds further ahead**, gated against
`v43_open3_carrot`. That is the natural next candidate and it is cheap to build.

**Formal gate line (tourney reports `h2h-b0f8a324-vs-*`):**

```
GATE VERDICT: VETO (lost to incumbent in 46/50 games (seed_block=850000-850024))
  [VETO ] vs_incumbent_paired: 0 games better than the incumbent mirror, 46 worse (raw losses 50)
  [VETO ] vs_parent_paired:    0 games better than the parent mirror,    48 worse (raw losses 50)
  [INFO ] vs_other:v43_lead8_open7: 0-50   [INFO ] vs_other:v43_lead8: 0-50
  [INFO ] vs_other:opp_v43:         0-50   [PASS ] audit: 3352 findings, 0 critical
```

**0-50 against every opponent in the pool, `opp_v43` included** — which the parent beats 50-0.
So this is an absolute degradation, not a matchup effect, exactly as the herd-starvation
mechanism predicts. Zero games better than the mirror in any block; the gate's relaxed gold-plan
rule (≤1 regression, ≥40/50 better) would not have changed this verdict either.

### Iteration 35 close-out

- Champion base unchanged: **`v43_open3_carrot` (1367897a)**, the best gated agent.
- Nothing was submittable this iteration, so the missing `KAGGLE_API_TOKEN` cost nothing yet.
- `lab/gate.py` still enforces the strict "any paired regression = VETO" rule; the gold plan's
  relaxed rule is still only plan text. Left unimplemented on purpose — changing the gate and
  testing a candidate in one iteration would confound both. Worth doing in an iteration of its
  own, since it is what vetoed `v43_lead8_open7` on a single regression back in iteration 26.

## Iteration 36 — 2026-09-18 (cloud agent) — opener x carrot cross, user-directed

Two things asked for: an `open7 + carrot` cross, and a measurement of the big-opening branch
(`open55_carrot`) against today's champion base. Still no `KAGGLE_API_TOKEN`, so nothing can be
submitted or synced; the nominated agent is packaged and held as `ready_to_submit`.

### `v43_lead8_open7_carrot` (d4d64572): VETO — but it proves the carrot knob a fourth time

Built as `v43_lead8_open7` + the carrot overlay verbatim, appended byte-exact (CRLF base kept,
LF overlay), so the only change vs the parent is the carrot tie-break.

```
GATE VERDICT: VETO (lost to incumbent in 42/50 games (seed_block=850000-850024))
  [PASS ] vs_parent (v43_lead8_open7):     raw 48-2,  44 better than mirror, 0 regressions
  [VETO ] vs_incumbent (v43_open3_carrot): raw 4-46,  0 better,             42 regressions
  [INFO ] vs_other:v43_lead8_open3: 47-3   [INFO ] vs_other:v43_lead8: 49-1
  [INFO ] vs_other:opp_v43:         50-0   [PASS ] audit: 2698 findings, 0 critical
```

Two clean readings:

1. **The carrot tie-break generalises again** — 48-2 with zero paired regressions on the open7
   base, its fourth passing base after open55, lead8 and open3. It is a base-independent knob.
2. **open3 > open7 survives adding carrot to both sides.** The cross beats *plain* `open3`
   47-3, which is just the carrot knob showing up; against `open3_carrot`, where both carry
   the knob, it loses 4-46. The opening advantage is what separates them, and 3 still wins.

So the cross is a genuine improvement on its own parent and still not worth a slot. Champion
base stays **`v43_open3_carrot` (1367897a)**.

### The adaptive opener the user asked for cannot be built — recorded so it is not retried

The request was an agent opening 55 by default that switches to open3 against opponents who
open low. **The opening cannot be conditioned on anything.** Verified from a replay: at step 0
both players see an identical observation — money 3000/3000, market inventory 10000 for every
product, WHEAT price 25, same farms — and it is the same on every seed. The turn-0 wash is a
constant decision, chosen before any opponent information exists. Only at step 1 does the
opponent's wash become visible (WHEAT inventory 9999, price 26 in the sample game), and by then
the opening is spent. There is also no "open3 behaviour" after step 0 to switch into: open3 and
open55 differ in exactly one line, the step-0 wash size.

User's call: skip the adaptive framing and measure the big-opening branch directly instead.
