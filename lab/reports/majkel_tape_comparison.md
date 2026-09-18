# V43 agents vs. the Majkel1337 replay tape

**Caveat, read before any number below.** `opp_majkel_tape.py` is not Majkel1337's policy and
does not contain any of their decision-making. It is a fixed, step-indexed *recording* of the
actions Majkel1337 (rank 1, live LB rating 3,183.2 per the loop journal's gold-plan section)
happened to take in one specific public episode (Kaggle episode 109448978, seat 1, final bank
170003 vs DSM 160608). At step *n* it always returns the *n*-th action from that one game, no
matter who it is playing, what the weeds are doing, or what the shop offers — it cannot perceive
or react to anything, and orders that are invalid in the current game state simply no-op. Live
Kaggle access (leaderboard, episodes, replay download) is blocked in this environment, so this
tape is the only local signal we can get about the #1 ladder agent at all — but it is a weak,
indirect one. Nothing below should ever be read as "X beats Majkel1337." The only defensible
claim is "X's moves would have outscored this one frozen recording of one of Majkel1337's games,
N times out of M."

Tournament: `python -m lab.tournament --artifacts lab/candidates/opp_majkel_tape.py,v43_open55,v43_lead8,v43_open3_carrot,v43_lead8_open3 --seed-block 1040000-1040014 --workers 2`
— 5-agent round robin, 15 seeds, both seats, 10 pairs x 30 games = 300 games. Ledger batch
`tourney-dfcb9507`, `seed_block=1040000-1040014`, created 2026-09-18 09:08:45 UTC (matches the
run just requested; 300/300 game rows present, 0 `HARNESS_ERROR`). The tape has no registered
ledger name; its games were identified by matching `sha_p0`/`sha_p1` against
`sha256(lab/candidates/opp_majkel_tape.py)` = `d45c4da0fe81355b163a5d28e8f7c169ceb34da70e00d0faff70cc376cf8f2a5`
(shown as `d45c4da0` below, the tournament tool's own short label for it).

## Full Bradley-Terry ratings table (all 5 agents, from rr_vs_majkel.log)

| name | BT | elo | W | L | T | mean_margin |
|---|---|---|---|---|---|---|
| v43_open3_carrot | 3.553 | 2117 | 116 | 4 | 0 | 11150.1 |
| v43_lead8_open3 | 1.388 | 1741 | 86 | 34 | 0 | 11143.9 |
| v43_lead8 | -0.101 | 1482 | 60 | 60 | 0 | 36827.2 |
| v43_open55 | -1.749 | 1196 | 30 | 90 | 0 | 35183.9 |
| d45c4da0 (Majkel1337 tape) | -3.091 | 963 | 8 | 112 | 0 | -94305.0 |

`rr_vs_majkel.err` is empty — no errors were logged during the run.

## Head-to-head vs. the tape only

Computed from the read-only ledger (`games` table for batch `tourney-dfcb9507`), flipping
`result`/`margin` when the scored agent sat in the p1 seat. Sorted best-performing-vs-tape
first (win rate, then median margin, both descending).

| our agent | vs tape: W-L-T | win rate | median margin |
|---|---|---|---|
| v43_open55 | 30-0-0 | 100.0% | +148,505.0 |
| v43_lead8 | 30-0-0 | 100.0% | +148,383.0 |
| v43_lead8_open3 | 26-4-0 | 86.7% | +47,754.0 |
| v43_open3_carrot | 26-4-0 | 86.7% | +47,750.5 |

(These figures match the tournament tool's own per-opponent breakdown in
`lab/reports/tourney-dfcb9507.md` exactly, as a sanity cross-check.)

## Per-agent interpretation

- **v43_open55**: its moves would have beaten this one recorded Majkel1337 game 30 times out of
  30 in this seed block.
- **v43_lead8**: its moves would have beaten this one recorded Majkel1337 game 30 times out of
  30 in this seed block.
- **v43_lead8_open3**: its moves would have beaten this one recorded Majkel1337 game 26 times
  out of 30 in this seed block, losing the other 4.
- **v43_open3_carrot**: its moves would have beaten this one recorded Majkel1337 game 26 times
  out of 30 in this seed block, losing the other 4.

## Does this suggest a further avenue, or is it too thin to conclude anything?

Mostly the latter — and the tournament's own audit log tells us why. Every real agent clears the
tape by lopsided margins (tens to ~150k), far larger than the margins agents post against each
other (hundreds to low thousands in this same run, e.g. `v43_open3_carrot` vs `v43_open55` had a
median margin of 1,437). That gap is a strong sign of tape breakdown, not agent strength: the
batch's audit findings show `d45c4da0` (the tape) racking up `preempted_sell` at 59.12
occurrences per game, versus 12.81-14.28 per game for the four real agents — roughly 4-5x higher.
Because the tape is a fixed step-indexed sequence with no perception, its recorded orders become
invalid as the live game state (weed spawns, shop draws, the actual opponent's play) diverges
from the one original episode; those invalid orders no-op, and the tape agent effectively stalls
economically as the game goes on. That is consistent with a non-reactive tape falling apart
against *any* competent opponent, not with anything about the relative strength of the four V43
variants. On top of that, this is a single 30-seed-per-pair comparison against one recording of
one game — far too thin a sample, and too structurally different an opponent (deterministic,
non-adaptive, prone to no-ops), to support ranking the four V43 agents against each other by this
number, or to say anything at all about how they would fare against Majkel1337's actual reactive
policy. The one thing worth flagging for a possible follow-up, if it's ever wanted: a replay-level
look at *when* the tape's orders first start going invalid (which step, which order type) could
sanity-check that this preempted_sell spike really is a divergence artifact and not a bug in how
the tape was reconstructed — but this is a low-priority curiosity, not evidence about agent
quality, and does not change anything about the gate/submit loop.
