# Matrix analysis: turn-0 opening size x carrot overlay

Read-only analysis of two local round robins in `lab/runs.db`. Nothing was launched for
this report and the ledger was opened read-only; no row was written.

- **Tournament B** (main matrix): `tourney-75ceebf3`, seed block 1010000-1010001, 31 agents, 1860 games scored, 0 harness-error rows excluded.
- **Tournament A** (5-agent probe): `tourney-369e8b5a`, seed block 1000000-1000009, 5 agents, 200 games scored, 0 harness-error rows excluded.

## How to read these numbers

Tournament B runs **2 seeds per pair**, i.e. 4 games per pair (both seats on both seeds).
A 4-game pairwise record carries almost no information on its own - 3-1 and 1-3 are both
ordinary noise, and a single 4-0 is roughly a coin landing heads twice. The Bradley-Terry
rating pools every game an agent played against all 30 opponents (up to 120 games per
agent), so **the BT rating is the number to rank on**; the pairwise cells below are
context, not evidence. Tournament A, with 10 seeds and 20 games per pair, is the one
place in this report where a single pairwise record stands on its own.

Margins are from the named agent's point of view (reward_agent - reward_opponent),
flipped when that agent sat in the p1 seat. Medians and counts are exact as computed.
Mean margin is reported for completeness only: tournament B contains two very weak
agents (c94, c95) that lose by tens of thousands of coins, so any mean that includes
games against them says more about the field than about the agent. Read the median.

The "opening" column is parsed from each artifact's source: the last
`BUY_PRODUCT WHEAT n` / `SELL WHEAT n` turn-0 override in the file. `base` means the
agent has no wash override at all and keeps V43's default BUY 5 / BUY 10 / SELL 60.
Carrot is the literal presence of `_CARROT_PARENT` in the source.

## 1. Tournament B ranking

| # | agent | sha8 | opening | carrot | BT rating | elo | W-L-T | games | win rate | median margin | mean margin |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | v43_open3_lead12 | `5b37959e` | 3 | yes | 10.120 | 3258 | 120-0-0 | 120 | 100.0% | 834.0 | 3098.4 |
| 2 | v43_open3_carrot | `1367897a` | 3 | yes | 6.322 | 2598 | 104-8-8 | 120 | 90.0% | 31.5 | 2654.1 |
| 3 | v43_open3_notopup | `df93494c` | 3 | yes | 6.322 | 2598 | 104-8-8 | 120 | 90.0% | 31.5 | 2654.1 |
| 4 | v43_lead12 | `0ff60be9` | 55 | no | 5.801 | 2508 | 104-16-0 | 120 | 86.7% | 809.5 | 3224.5 |
| 5 | v43_lead8_open7_carrot | `d4d64572` | 7 | yes | 5.569 | 2467 | 100-16-4 | 120 | 85.0% | 159.5 | 2762.5 |
| 6 | v43_lead8_open12_carrot | `862eb730` | 12 | yes | 4.836 | 2340 | 92-22-6 | 120 | 79.2% | 276.5 | 3057.2 |
| 7 | v43_lead8_open0_carrot | `775c1789` | 0 | yes | 4.737 | 2323 | 76-8-36 | 120 | 78.3% | 10.0 | 2636.8 |
| 8 | v43_lead8_open3 | `774a7f56` | 3 | no | 4.543 | 2289 | 90-26-4 | 120 | 76.7% | 20.5 | 2646.0 |
| 9 | v43_lead8_open7 | `d070da79` | 7 | no | 4.256 | 2239 | 86-28-6 | 120 | 74.2% | 148.5 | 2752.9 |
| 10 | v43_lead8_open15_carrot | `2ba8015a` | 15 | yes | 3.971 | 2190 | 84-32-4 | 120 | 71.7% | 333.0 | 3228.3 |
| 11 | v43_lead8_open12 | `f4253a13` | 12 | no | 3.591 | 2124 | 80-36-4 | 120 | 68.3% | 269.0 | 3048.4 |
| 12 | v43_lead8_open15 | `8a4268d2` | 15 | no | 3.011 | 2023 | 74-42-4 | 120 | 63.3% | 315.0 | 3220.0 |
| 13 | v43_lead8_open20_carrot | `f863d238` | 20 | yes | 3.011 | 2023 | 74-42-4 | 120 | 63.3% | 338.0 | 3228.7 |
| 14 | v43_lead8_open20 | `01004085` | 20 | no | 2.201 | 1882 | 66-50-4 | 120 | 56.7% | 320.0 | 3220.4 |
| 15 | v43_lead8_open43_carrot | `442c9244` | 43 | yes | 1.991 | 1846 | 64-52-4 | 120 | 55.0% | 11.0 | 2779.8 |
| 16 | v43_lead8_open50_carrot | `a3861fe7` | 50 | yes | 1.110 | 1693 | 56-60-4 | 120 | 48.3% | -10.0 | 2520.6 |
| 17 | v43_lead8_open43 | `f1d53ae7` | 43 | no | 1.110 | 1693 | 56-60-4 | 120 | 48.3% | -5.0 | 2769.1 |
| 18 | v43_lead8_open0 | `f9d9e585` | 0 | no | 0.875 | 1652 | 40-48-32 | 120 | 46.7% | 0.0 | 2628.7 |
| 19 | v43_lead8_carrot | `985fbbcb` | 55 | yes | 0.112 | 1519 | 48-68-4 | 120 | 41.7% | -33.5 | 2645.8 |
| 20 | v43_lead8_open50 | `a21b4d85` | 50 | no | 0.112 | 1519 | 48-68-4 | 120 | 41.7% | -22.0 | 2511.4 |
| 21 | v43_lead8 | `887aaad7` | 55 | no | -1.173 | 1296 | 40-76-4 | 120 | 35.0% | -44.0 | 2636.9 |
| 22 | v43_lead6 | `135bd368` | 55 | no | -2.446 | 1075 | 36-84-0 | 120 | 30.0% | -1219.0 | 1663.2 |
| 23 | v43_lead5 | `f52e507f` | 55 | no | -3.395 | 910 | 32-88-0 | 120 | 26.7% | -1112.5 | 1684.7 |
| 24 | v43_open55_carrot | `50ff2642` | 55 | yes | -4.375 | 740 | 28-92-0 | 120 | 23.3% | -1048.0 | 1384.5 |
| 25 | v43_open55 | `a86e80f9` | 55 | no | -5.380 | 565 | 24-96-0 | 120 | 20.0% | -1060.5 | 1372.1 |
| 26 | v43_carrot | `af60f83c` | base | yes | -6.415 | 386 | 20-100-0 | 120 | 16.7% | -1113.0 | 1012.2 |
| 27 | opp_v43 | `919fc1d6` | base | no | -7.745 | 155 | 14-104-2 | 120 | 12.5% | -1126.0 | 999.8 |
| 28 | opp_v42 | `728fdfb4` | base | no | -8.297 | 59 | 12-106-2 | 120 | 10.8% | -1126.0 | 960.8 |
| 29 | opp_v41 | `8951ff93` | base | no | -9.829 | -207 | 8-112-0 | 120 | 6.7% | -1992.0 | 96.3 |
| 30 | c94 | `7b0e5a7b` | base | no | -11.310 | -465 | 4-116-0 | 120 | 3.3% | -34160.0 | -34522.6 |
| 31 | c95 | `489f5d19` | base | no | -13.236 | -799 | 0-120-0 | 120 | 0.0% | -34230.0 | -34575.8 |

## 2. The opening-size curve

Restricted to the clean matrix: same `v43_lead8` base, one knob changed. Every agent in
both series played the same 30 opponents, so the two series are directly comparable.
(`v43_lead8` itself is the opening-55 cell - 55 is the base's own opening - and
`v43_open3_carrot` is the opening-3 + carrot cell.)

| opening | plain: agent | BT | W-L-T | win rate | median margin | carrot: agent | BT | W-L-T | win rate | median margin | carrot BT delta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | v43_lead8_open0 | 0.875 | 40-48-32 | 46.7% | 0.0 | v43_lead8_open0_carrot | 4.737 | 76-8-36 | 78.3% | 10.0 | 3.862 |
| 3 | v43_lead8_open3 | 4.543 | 90-26-4 | 76.7% | 20.5 | v43_open3_carrot | 6.322 | 104-8-8 | 90.0% | 31.5 | 1.780 |
| 7 | v43_lead8_open7 | 4.256 | 86-28-6 | 74.2% | 148.5 | v43_lead8_open7_carrot | 5.569 | 100-16-4 | 85.0% | 159.5 | 1.313 |
| 12 | v43_lead8_open12 | 3.591 | 80-36-4 | 68.3% | 269.0 | v43_lead8_open12_carrot | 4.836 | 92-22-6 | 79.2% | 276.5 | 1.244 |
| 15 | v43_lead8_open15 | 3.011 | 74-42-4 | 63.3% | 315.0 | v43_lead8_open15_carrot | 3.971 | 84-32-4 | 71.7% | 333.0 | 0.961 |
| 20 | v43_lead8_open20 | 2.201 | 66-50-4 | 56.7% | 320.0 | v43_lead8_open20_carrot | 3.011 | 74-42-4 | 63.3% | 338.0 | 0.809 |
| 43 | v43_lead8_open43 | 1.110 | 56-60-4 | 48.3% | -5.0 | v43_lead8_open43_carrot | 1.991 | 64-52-4 | 55.0% | 11.0 | 0.881 |
| 50 | v43_lead8_open50 | 0.112 | 48-68-4 | 41.7% | -22.0 | v43_lead8_open50_carrot | 1.110 | 56-60-4 | 48.3% | -10.0 | 0.998 |
| 55 | v43_lead8 | -1.173 | 40-76-4 | 35.0% | -44.0 | v43_lead8_carrot | 0.112 | 48-68-4 | 41.7% | -33.5 | 1.285 |

**Does "smaller opening is better" still hold?** Yes, exactly, and in both series.
Ordering the plain series by BT rating gives 3 > 7 > 12 > 15 > 20 >> 43 > 50 > 55, which
is the prior ordering character for character. The carrot series gives the same ordering.
Every adjacent pair also meets head to head and every one of those meetings went 4-0 the
way the ordering predicts (3 beats 7, 7 beats 12, 12 beats 15, 15 beats 20, 20 beats 43,
43 beats 50, 50 beats 55) - 7 of 7 adjacent steps agree with the rating order.
(Opening 0 is left out of this chain; see the anomaly below.)

**Where it flattens.** In per-game coins the small end is nearly flat and the big end is
a cliff. Median margin of each plain agent over the next size up, head to head:

| step | median margin | 
|---|---|
| open3 over open7 | 6.5 |
| open7 over open12 | 12.5 |
| open12 over open15 | 11.5 |
| open15 over open20 | 22.5 |
| open20 over open43 | 325.0 |
| open43 over open50 | 150.5 |
| open50 over open55 (v43_lead8) | 42.5 |

The step from 20 to 43 is worth 325 coins, roughly fifty times the step from 3 to 7.

Margins here are not additive, so the end-to-end size of the knob has to be measured
directly rather than summed. From `v43_lead8_open3`'s own seat the whole range is small:
it beats open7 by 6.5, open12 by 11.5, open15 by 14.5, open20 by 17.5, open43 by 30.5,
open50 by 32.5 and `v43_lead8` (opening 55) by 34.5 - a total spread of 34.5 coins per
game across the entire 3..55 range. The 300-1300 coin gaps show up only *between*
mid-sized openings (e.g. open20 over open50 by 1290.0), never between the best opening
and anything else. The practical content of the knob is therefore: stay small, and
below ~20 it barely matters which small value you pick.

**One anomaly worth naming: opening 0 is a null, not a winner.** `v43_lead8_open0` drew
all 32 of its games against the other eight plain matrix agents - result T, margin
exactly 0.0, identical rewards, full 720 steps, every single game. Its 40-48-32 record
comes entirely from the non-matrix part of the field. Its BT rating (0.875) therefore
says nothing about opening size; it is the rating of an agent that cannot lose or win
inside its own family. The carrot version behaves the same way against the carrot
family. Practical reading: size 0 (`BUY_PRODUCT WHEAT 0` / `SELL WHEAT 0`, i.e. no
market move at all on turn 0) gives up the small-opening edge rather than maximising
it - opening 3 is the smallest size that still converts into wins. Why a non-washing
opponent produces exactly equal rewards for both seats is not explained by this data and
is worth a replay-level look before anyone builds on opening 0.

## 3. The carrot delta, opening by opening

Head-to-head only: `open<N>_carrot` against plain `open<N>`. These pairs meet directly in
the round robin, so this is the paired measurement of the overlay at each opening. Each
row is 4 games. Records are from the carrot agent's point of view.

| opening | carrot agent vs plain agent | W-L-T | games | median margin | mean margin |
|---|---|---|---|---|---|
| 0 | v43_lead8_open0_carrot vs v43_lead8_open0 | 4-0-0 | 4 | 11.0 | 11.0 |
| 3 | v43_open3_carrot vs v43_lead8_open3 | 4-0-0 | 4 | 11.0 | 11.0 |
| 7 | v43_lead8_open7_carrot vs v43_lead8_open7 | 4-0-0 | 4 | 11.0 | 11.0 |
| 12 | v43_lead8_open12_carrot vs v43_lead8_open12 | 4-0-0 | 4 | 11.0 | 11.0 |
| 15 | v43_lead8_open15_carrot vs v43_lead8_open15 | 4-0-0 | 4 | 11.0 | 11.0 |
| 20 | v43_lead8_open20_carrot vs v43_lead8_open20 | 4-0-0 | 4 | 11.0 | 11.0 |
| 43 | v43_lead8_open43_carrot vs v43_lead8_open43 | 4-0-0 | 4 | 11.0 | 11.0 |
| 50 | v43_lead8_open50_carrot vs v43_lead8_open50 | 4-0-0 | 4 | 11.0 | 11.0 |
| 55 | v43_lead8_carrot vs v43_lead8 | 4-0-0 | 4 | 11.0 | 11.0 |

**Is the carrot gain consistent across openings?** It is as consistent as a measurement
can be: 4-0-0 at every one of the nine openings, with a median margin of exactly 11.0
coins in all nine cells and a mean of exactly 11.0 in all nine. The overlay does not
depend on the opening at all in direct play - it is a flat, deterministic tie-break
worth 11 coins in the mirror, which is what a tie-break that sells a little more CARROT
should look like. Nine independent 4-0 sweeps is 36 paired games with zero regressions.

Pooled over the whole field the carrot is also always positive but not flat: the BT
delta in section 2 ranges from +0.809 (opening 20) to +1.780 (opening 3) across the
genuine cells, and +3.862 at opening 0, which is inflated by the all-tie anomaly above.
The pooled deltas are larger where the base is stronger, which is the expected shape
when a fixed 11-coin edge is applied to an agent that is already near the top of the
field: the same coins buy more rating where more matches are close.

## 4. Everything against v43_open3_carrot (`1367897a`)

Records are from the **challenger's** point of view, 4 games each (2 seeds x 2 seats).
Sorted by the challenger's BT rating in the full tournament.

| challenger | opening | carrot | W-L-T vs champ | median margin | mean margin | result |
|---|---|---|---|---|---|---|
| v43_open3_lead12 | 3 | yes | 4-0-0 | 832.0 | 832.0 | AHEAD |
| v43_open3_notopup | 3 | yes | 0-0-4 | 0.0 | 0.0 | level |
| v43_lead12 | 55 | no | 4-0-0 | 794.5 | 794.5 | AHEAD |
| v43_lead8_open7_carrot | 7 | yes | 0-4-0 | -6.5 | -6.5 | behind |
| v43_lead8_open12_carrot | 12 | yes | 0-4-0 | -11.5 | -11.5 | behind |
| v43_lead8_open0_carrot | 0 | yes | 0-0-4 | 0.0 | 0.0 | level |
| v43_lead8_open3 | 3 | no | 0-4-0 | -11.0 | -11.0 | behind |
| v43_lead8_open7 | 7 | no | 0-4-0 | -17.5 | -17.5 | behind |
| v43_lead8_open15_carrot | 15 | yes | 0-4-0 | -14.5 | -14.5 | behind |
| v43_lead8_open12 | 12 | no | 0-4-0 | -22.5 | -22.5 | behind |
| v43_lead8_open15 | 15 | no | 0-4-0 | -25.5 | -25.5 | behind |
| v43_lead8_open20_carrot | 20 | yes | 0-4-0 | -17.5 | -17.5 | behind |
| v43_lead8_open20 | 20 | no | 0-4-0 | -28.5 | -28.5 | behind |
| v43_lead8_open43_carrot | 43 | yes | 0-4-0 | -30.5 | -30.5 | behind |
| v43_lead8_open50_carrot | 50 | yes | 0-4-0 | -32.5 | -32.5 | behind |
| v43_lead8_open43 | 43 | no | 0-4-0 | -41.5 | -41.5 | behind |
| v43_lead8_open0 | 0 | no | 0-4-0 | -11.0 | -11.0 | behind |
| v43_lead8_carrot | 55 | yes | 0-4-0 | -34.5 | -34.5 | behind |
| v43_lead8_open50 | 50 | no | 0-4-0 | -43.5 | -43.5 | behind |
| v43_lead8 | 55 | no | 0-4-0 | -45.5 | -45.5 | behind |
| v43_lead6 | 55 | no | 0-4-0 | -1295.0 | -1295.0 | behind |
| v43_lead5 | 55 | no | 0-4-0 | -1245.5 | -1245.5 | behind |
| v43_open55_carrot | 55 | yes | 0-4-0 | -1093.5 | -1093.5 | behind |
| v43_open55 | 55 | no | 0-4-0 | -1102.0 | -1102.0 | behind |
| v43_carrot | base | yes | 0-4-0 | -1067.5 | -1067.5 | behind |
| opp_v43 | base | no | 0-4-0 | -1076.0 | -1076.0 | behind |
| opp_v42 | base | no | 0-4-0 | -1096.5 | -1096.5 | behind |
| opp_v41 | base | no | 0-4-0 | -1472.5 | -1472.5 | behind |
| c94 | base | no | 0-4-0 | -35680.0 | -35680.0 | behind |
| c95 | base | no | 0-4-0 | -35727.5 | -35727.5 | behind |

**Answer: two agents beat the incumbent, and both of them carry the same non-opening
knob.** `v43_open3_lead12` (`5b37959e`) went 4-0-0 with median margin +832.0, and
`v43_lead12` (`0ff60be9`) went 4-0-0 with median margin +794.5. Both wins are clean in
the sense that matters most for a 2-seed block: every one of the four games went the
same way in both seats on both seeds, and the per-game margins are ~800 coins, not the
10-40 coin edges that separate the rest of this field.

Two agents were exactly level: `v43_open3_notopup` (0-0-4, margin 0.0 in every game -
identical rewards to the champion, i.e. behaviourally a clone on these seeds) and
`v43_lead8_open0_carrot` (0-0-4, margin 0.0, the opening-0 null described above).
Every other agent in the field lost 0-4.

The shared knob is the sell-reservation horizon 12 instead of 8. `v43_lead12` carries it
on the *old* opening-55 base with no carrot, and still beats the champion by ~795 -
which says the horizon is worth far more than the entire opening-size knob (whose whole
3..55 range is worth about 45 coins per game at the small end). `v43_open3_lead12` is
the champion base plus that horizon, and it went 120-0-0 in the whole tournament,
including 4-0 (+41.5 median) over `v43_lead12` itself.

**How much to trust it.** 4 games is 4 games. What raises this above the usual 2-seed
noise is that `v43_open3_lead12` did not lose a single game to any of the 30 opponents
(120-0-0), the margins against the champion are two orders of magnitude larger than the
carrot-sized effects this lab usually chases, and both seats on both seeds agree. What
should still hold anyone back from calling it settled: 2 seeds cannot rule out a
seed-specific effect, and `v43_lead12` itself split 2-2 against six of the mid-opening
agents, which is what genuine seed sensitivity looks like. The horizon-12 result needs a
proper multi-seed head-to-head and a gate run before it goes near a submission slot;
this tournament is evidence, not a gate.

## 5. Tournament A (5-agent probe, 10 seeds per pair)

| # | agent | sha8 | opening | carrot | BT rating | elo | W-L-T | games | win rate | median margin | mean margin |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | v43_open3_carrot | `1367897a` | 3 | yes | 3.190 | 2054 | 75-3-2 | 80 | 95.0% | 12.0 | 456.2 |
| 2 | v43_lead8_open7_carrot | `d4d64572` | 7 | yes | 1.220 | 1712 | 52-24-4 | 80 | 67.5% | 4.5 | 371.5 |
| 3 | v43_lead8_open3 | `774a7f56` | 3 | no | 0.550 | 1595 | 43-33-4 | 80 | 56.2% | 6.0 | 446.1 |
| 4 | v43_lead8_open7 | `d070da79` | 7 | no | -1.256 | 1282 | 22-56-2 | 80 | 28.7% | -7.0 | 359.4 |
| 5 | v43_open55_carrot | `50ff2642` | 55 | yes | -3.704 | 857 | 2-78-0 | 80 | 2.5% | -1467.5 | -1633.2 |

Pairwise, 20 games per pair (both seats on 10 seeds). This is the only table here with
enough games per cell to read directly.

| agent | opponent | W-L-T | games | median margin | mean margin |
|---|---|---|---|---|---|
| v43_open3_carrot | v43_lead8_open7_carrot | 19-1-0 | 20 | 7.0 | 6.8 |
| v43_open3_carrot | v43_lead8_open3 | 17-1-2 | 20 | 10.0 | 8.6 |
| v43_open3_carrot | v43_lead8_open7 | 19-1-0 | 20 | 17.0 | 15.4 |
| v43_open3_carrot | v43_open55_carrot | 20-0-0 | 20 | 1645.0 | 1793.9 |
| v43_lead8_open7_carrot | v43_open3_carrot | 1-19-0 | 20 | -7.0 | -6.8 |
| v43_lead8_open7_carrot | v43_lead8_open3 | 15-3-2 | 20 | 3.0 | 1.8 |
| v43_lead8_open7_carrot | v43_lead8_open7 | 17-1-2 | 20 | 10.0 | 8.6 |
| v43_lead8_open7_carrot | v43_open55_carrot | 19-1-0 | 20 | 1038.0 | 1482.3 |
| v43_lead8_open3 | v43_open3_carrot | 1-17-2 | 20 | -10.0 | -8.6 |
| v43_lead8_open3 | v43_lead8_open7_carrot | 3-15-2 | 20 | -3.0 | -1.8 |
| v43_lead8_open3 | v43_lead8_open7 | 19-1-0 | 20 | 7.0 | 6.8 |
| v43_lead8_open3 | v43_open55_carrot | 20-0-0 | 20 | 1641.0 | 1788.1 |
| v43_lead8_open7 | v43_open3_carrot | 1-19-0 | 20 | -17.0 | -15.4 |
| v43_lead8_open7 | v43_lead8_open7_carrot | 1-17-2 | 20 | -10.0 | -8.6 |
| v43_lead8_open7 | v43_lead8_open3 | 1-19-0 | 20 | -7.0 | -6.8 |
| v43_lead8_open7 | v43_open55_carrot | 19-1-0 | 20 | 1009.0 | 1468.5 |
| v43_open55_carrot | v43_open3_carrot | 0-20-0 | 20 | -1645.0 | -1793.9 |
| v43_open55_carrot | v43_lead8_open7_carrot | 1-19-0 | 20 | -1038.0 | -1482.3 |
| v43_open55_carrot | v43_lead8_open3 | 0-20-0 | 20 | -1641.0 | -1788.1 |
| v43_open55_carrot | v43_lead8_open7 | 1-19-0 | 20 | -1009.0 | -1468.5 |

**What tournament A says.** With 20 games per cell this is the most solid block of
evidence in the report, and it agrees with tournament B on everything the two have in
common. `v43_open3_carrot` wins the probe outright (BT 3.190, 75-3-2). The carrot is
confirmed twice on 20-game samples: 17-1-2 (+10.0 median) for open3_carrot over plain
open3, and 17-1-2 (+10.0 median) for open7_carrot over plain open7 - the same +10 to +11
the matrix measures at every opening. Opening 3 over opening 7 is confirmed twice as
well: 19-1-0 (+7.0) with carrot on both sides, 19-1-0 (+7.0) with carrot on neither.

The two knobs can also be weighed against each other here: `v43_lead8_open7_carrot`
beats plain `v43_lead8_open3` 15-3-2 (+3.0 median). A carrot (+10) is worth more than
one step of opening size (+7), so the overlay matters more than the 3-vs-7 choice.

**Where `v43_open55_carrot` (`50ff2642`) lands: last, and not close.** BT -3.704
(elo 857), 2-78-0 over the probe, median margin -1467.5. It lost 0-20 to `v43_open3_carrot`
(median -1645.0) and 0-20 to plain `v43_lead8_open3` (median -1641.0); its only two wins
in 80 games were single games against the two opening-7 agents. That is the deliberate
measurement of the big-opening branch and it is unambiguous at 10 seeds: a carrot cannot
rescue opening 55. The +11 the overlay is worth is two orders of magnitude smaller than
the ~1600 coins the big opening gives away. The big-opening branch should be considered
closed unless something other than the opening changes - and note that `v43_lead12`,
which carries opening 55, is *not* a counterexample: it is winning on the horizon knob
in spite of its opening, not because of it.

## 6. What this means

**Single best agent by this evidence: `v43_open3_lead12` (`5b37959e`)** - the current
champion base plus sell-reservation horizon 12. BT 10.120 (elo 3258), 120-0-0 across the
whole 31-agent field, undefeated against every opening size, both carrot settings, both
older opponent generations and the champion itself.

**Does it beat the incumbent? Yes:** 4-0-0 over `v43_open3_carrot` with median margin
+832.0 (+795.0 and +869.0 on seed 1010000 and 1010001, the same result in both seats).
`v43_lead12` also beats the incumbent 4-0-0 (+794.5 median) from the old opening-55 base.

**Results that contradict the prior summary:**

1. *The opening size is not the important knob.* The prior reading treats opening size
   as the live lever and the carrot as the increment on top. This tournament says the
   champion's own direct margin over the worst opening in its family is 34.5 coins per
   game (and 6.5 over opening 7), and the carrot is worth exactly 11, while horizon 12
   is worth ~800 against the same opponents. An agent on the *worst* opening (55) with
   horizon 12 and no carrot outranks every opening-3 and opening-7 agent that lacks it.
   Opening size and carrot are real but small; they were being tuned on top of a base
   that had a much larger unexploited knob.
2. *Opening 0 does not extend the "smaller is better" line.* It is not the best small
   opening; it is a null that ties its whole family at exactly 0 margin. The ordering
   3 > 7 > 12 > ... is confirmed, but it does not continue downward past 3.
3. *`v43_open3_notopup` is not a separate agent on these seeds.* It tied the champion
   0-0-4 with identical rewards in all four games and its whole-tournament line is
   identical to the champion's (104-8-8, BT 6.322). Whatever the step-171/195 top-up
   buys do, they did not fire on seed block 1010000-1010001. Testing it here cost 120
   games and produced no information; it needs seeds where the top-up actually occurs.

**What is not contradicted:** the carrot overlay. Nine paired 4-0 sweeps, +11.0 median
in every one, zero paired regressions anywhere in the matrix. Added to the four earlier
gate passes, the overlay now has nine bases behind it and behaves like a deterministic
tie-break rather than a stochastic edge. It is small, it is free, and it is real.

**Suggested next step (not done here, and not a recommendation to submit):** a
multi-seed head-to-head of `v43_open3_lead12` against `v43_open3_carrot` on a fresh seed
block, then `python -m lab.gate`. Nothing in this report is a gate result, and the hard
rule stands - nothing is submitted that has not passed the gate.

## Appendix: the two horizon-12 agents against the full field

Each cell is 4 games, from the row agent's point of view.

| agent | opponent | W-L-T | median margin |
|---|---|---|---|
| v43_open3_lead12 | v43_open3_carrot | 4-0-0 | 832.0 |
| v43_open3_lead12 | v43_open3_notopup | 4-0-0 | 832.0 |
| v43_open3_lead12 | v43_lead12 | 4-0-0 | 41.5 |
| v43_open3_lead12 | v43_lead8_open7_carrot | 4-0-0 | 838.5 |
| v43_open3_lead12 | v43_lead8_open12_carrot | 4-0-0 | 843.5 |
| v43_open3_lead12 | v43_lead8_open0_carrot | 4-0-0 | 832.0 |
| v43_open3_lead12 | v43_lead8_open3 | 4-0-0 | 841.0 |
| v43_open3_lead12 | v43_lead8_open7 | 4-0-0 | 847.5 |
| v43_open3_lead12 | v43_lead8_open15_carrot | 4-0-0 | 846.5 |
| v43_open3_lead12 | v43_lead8_open12 | 4-0-0 | 852.5 |
| v43_open3_lead12 | v43_lead8_open15 | 4-0-0 | 855.5 |
| v43_open3_lead12 | v43_lead8_open20_carrot | 4-0-0 | 849.5 |
| v43_open3_lead12 | v43_lead8_open20 | 4-0-0 | 858.5 |
| v43_open3_lead12 | v43_lead8_open43_carrot | 4-0-0 | 862.5 |
| v43_open3_lead12 | v43_lead8_open50_carrot | 4-0-0 | 864.5 |
| v43_open3_lead12 | v43_lead8_open43 | 4-0-0 | 871.5 |
| v43_open3_lead12 | v43_lead8_open0 | 4-0-0 | 841.0 |
| v43_open3_lead12 | v43_lead8_carrot | 4-0-0 | 866.5 |
| v43_open3_lead12 | v43_lead8_open50 | 4-0-0 | 873.5 |
| v43_open3_lead12 | v43_lead8 | 4-0-0 | 875.5 |
| v43_open3_lead12 | v43_lead6 | 4-0-0 | 964.5 |
| v43_open3_lead12 | v43_lead5 | 4-0-0 | 803.0 |
| v43_open3_lead12 | v43_open55_carrot | 4-0-0 | 681.5 |
| v43_open3_lead12 | v43_open55 | 4-0-0 | 684.5 |
| v43_open3_lead12 | v43_carrot | 4-0-0 | 655.5 |
| v43_open3_lead12 | opp_v43 | 4-0-0 | 658.5 |
| v43_open3_lead12 | opp_v42 | 4-0-0 | 678.0 |
| v43_open3_lead12 | opp_v41 | 4-0-0 | 1030.5 |
| v43_open3_lead12 | c94 | 4-0-0 | 35262.0 |
| v43_open3_lead12 | c95 | 4-0-0 | 35310.0 |
| v43_lead12 | v43_open3_lead12 | 0-4-0 | -41.5 |
| v43_lead12 | v43_open3_carrot | 4-0-0 | 794.5 |
| v43_lead12 | v43_open3_notopup | 4-0-0 | 794.5 |
| v43_lead12 | v43_lead8_open7_carrot | 4-0-0 | 857.5 |
| v43_lead12 | v43_lead8_open12_carrot | 2-2-0 | 40.5 |
| v43_lead12 | v43_lead8_open0_carrot | 4-0-0 | 829.0 |
| v43_lead12 | v43_lead8_open3 | 4-0-0 | 805.0 |
| v43_lead12 | v43_lead8_open7 | 4-0-0 | 871.5 |
| v43_lead12 | v43_lead8_open15_carrot | 2-2-0 | 27.5 |
| v43_lead12 | v43_lead8_open12 | 2-2-0 | 49.5 |
| v43_lead12 | v43_lead8_open15 | 2-2-0 | 36.5 |
| v43_lead12 | v43_lead8_open20_carrot | 2-2-0 | 14.5 |
| v43_lead12 | v43_lead8_open20 | 2-2-0 | 23.5 |
| v43_lead12 | v43_lead8_open43_carrot | 4-0-0 | 789.0 |
| v43_lead12 | v43_lead8_open50_carrot | 4-0-0 | 786.5 |
| v43_lead12 | v43_lead8_open43 | 4-0-0 | 803.0 |
| v43_lead12 | v43_lead8_open0 | 4-0-0 | 839.5 |
| v43_lead12 | v43_lead8_carrot | 4-0-0 | 829.0 |
| v43_lead12 | v43_lead8_open50 | 4-0-0 | 797.0 |
| v43_lead12 | v43_lead8 | 4-0-0 | 839.5 |
| v43_lead12 | v43_lead6 | 4-0-0 | 930.0 |
| v43_lead12 | v43_lead5 | 4-0-0 | 768.5 |
| v43_lead12 | v43_open55_carrot | 4-0-0 | 646.0 |
| v43_lead12 | v43_open55 | 4-0-0 | 650.0 |
| v43_lead12 | v43_carrot | 4-0-0 | 2779.5 |
| v43_lead12 | opp_v43 | 4-0-0 | 2781.5 |
| v43_lead12 | opp_v42 | 4-0-0 | 2864.0 |
| v43_lead12 | opp_v41 | 4-0-0 | 3957.5 |
| v43_lead12 | c94 | 4-0-0 | 35262.0 |
| v43_lead12 | c95 | 4-0-0 | 35310.0 |

---

Generated read-only from `lab/runs.db` (batches `tourney-75ceebf3` and `tourney-369e8b5a`). No games were run, no
ledger rows were written, and no gate, tournament or registry command was invoked.

