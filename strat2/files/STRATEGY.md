# Kaggriculture — Agent v3 "Portfolio"

**Competition:** [kaggriculture](https://www.kaggle.com/competitions/kaggriculture) · $50,000 · top 10 win $5,000 each
**Entry deadline:** 23 Sep 2026 · **Final submission:** 30 Sep 2026 · 5 submissions/day, latest 2 active

Built against the **updated** environment (`hinge` price curves, flat town-centre demand). Re-pull `kaggle-environments` before tuning — the older release has no `hinge`.

---

## Results

| Opponent | Record | Score |
|---|---|---|
| `starter` | **4/4** | 58,885 – 63,212 |
| `random` | **4/4** | ~60,000 |
| `pass` | **4/4** | ~60,000 |
| **v2 (goose rush)** | **4/4** | ~50,000 vs ~5,000 |
| **Mirror (v3 vs v3)** | — | **~44,000 each** |

~**17× the built-in baseline**, 0 errors, 0.12 ms/turn against a 1 s limit.

**The mirror number is the important one: v2 scored 12,791 in the mirror, v3 scores ~44,000.** Ladder rating comes from beating strong opponents, and strong opponents converge on similar strategies.

---

## Three findings that drove the rebuild

### 1. Melon is the best asset in the game

Water-only it reaches its 6-unit cap — **fertilizer adds nothing**. Its glut curve is `sq` with T=300, so it decays slowly:

| Melons sold | 25 | 50 | 100 |
|---|---|---|---|
| Price | $244 | $225 | $150 |

| Asset | Revenue/season | Actions | Cost |
|---|---|---|---|
| **Melon tile** | ~$2,400 (6 units × 2 cycles) | **~24** | $160 |
| Goose | ~$1,800 | ~150 | $300 |

More money for **a sixth of the actions**. Since actions are the binding constraint, this is decisive.

### 2. Every price curve is concave → a portfolio beats any monoculture

Each sale walks down its *own* curve, so spreading across goods harvests the top of each:

- 50 melon + 25 wool + 25 milk + 50 egg + 50 tomato ≈ **$27,000**
- 200 units of any single good ≈ far less

v2's egg monoculture was structurally capped no matter how well executed.

### 3. Counter-positioning decides mirrors

Replay 90643183 (v2 vs itself) showed the mechanism: two goose farms crushed eggs to **$39** while milk hit **$351** and strawberry **$318**, purely because nobody produced them. Worse, both bought feed wheat, driving it **$25 → $60** — margin per goose collapsed from $75/day to $18.

The opponent's farm is public in `obs["farms"][1-me]`. v3 reads their tile mix and steers away: if they flood melon it shifts to tomato; if they scale geese it adds sheep; if nobody farms wool/milk it adds both.

---

## Design

**Tile targets:** 16 melon · 4 tomato · 4 wheat · 6 geese · 2 sheep · 2 cow — adjusted live by counter-positioning.

**Grow feed wheat, don't buy it.** v2 bought wheat and inflated the price against itself.

**Trickle premium goods** while price holds above a fraction of base (`HOLD_FRAC`), then dump everything from day 28. Eggs sell freely — the `log` glut curve makes them near-immune.

**Labour:** hire cost is `fib(n)`, so 10 hands = 143 coins for 240 actions. Hire to workload, not to wallet.

### Carried over from v2 (each was worth thousands)

| Fix | Why |
|---|---|
| **Courier requires empty hands** | Otherwise the unit nearest the shed is re-picked forever; `PLACE` fired **zero** times and 23 geese rotted in the shed |
| **Stand-and-serve** | Units finish work underfoot before walking (movement was 4× productive actions) |
| **Morning bulk loadout** | Hands spawn on shed tiles — load them all with wheat at once. FEED 284 → 797; ended herd starvation |

---

## Submission

```bash
kaggle competitions submit kaggriculture -f main.py -m "Portfolio v3"
kaggle competitions submissions kaggriculture
kaggle competitions leaderboard kaggriculture -s
```

## Next steps

1. **Dynamic melon sizing** — 22 melon tiles scored *worse* than 16 (price craters past ~120 units). Size the melon block off the observed market inventory rather than a constant.
2. **Exploit `hinge` scarcity.** Tomato at 400 units below `I0` pays **$300**, at 600 below **$900**. If town shops drain tomato and neither player supplies it, a late tomato block is enormous.
3. **Tune on ladder replays** — `kaggle competitions replay <EPISODE_ID>`, plus the community dataset `georgymamarin/kaggriculture-episodes`.
