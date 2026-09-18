"""Wraps v41 (opp_v41, sha8 8951ff93) so a learned policy can rewrite the SELL
portion of its market list, leaving field ops, BUY/HIRE/BUY_LAND orders, and
v41's own WHEAT/FERTILIZER sells untouched.

Seam (see Phase 2 Step 1 report for the full trace): v41 is treated as a
black box. Each turn we call its full ``agent(obs)`` (all ~30 stacked layers,
ending in the module's final ``agent = globals().pop("agent")`` rebind) to
get its complete proposed action, then only rewrite entries in
``action["market"]`` that are ``SELL`` orders for the 7 "free" items. WHEAT
and FERTILIZER SELLs, and every non-SELL order (BUY_SEED/BUY_PRODUCT/
BUY_ANIMAL/HIRE/BUY_LAND), are left at their exact original list index -- so
v41's own cross-turn bookkeeping (its R124/R127/R128 layers, which predict
next-turn shed/wheat state and log telemetry against the live observation,
never against a value they mutate themselves) cannot desync: those layers
read the live `observation` fresh every call, they don't carry forward a
simulated farm state that our sell rewrite could invalidate. The only value
they use that we ever touch is total money spent this turn on BUY_* orders,
which we never change (v1 keeps all buys/hire/land as v41 proposed).
"""
import base64
import zlib
from pathlib import Path

import numpy as np

from lab import ledger

LAB = Path(__file__).resolve().parent.parent
V41_PRODUCTS = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER")
LOCKED_ITEMS = ("WHEAT", "FERTILIZER")
FREE_ITEMS = tuple(p for p in V41_PRODUCTS if p not in LOCKED_ITEMS)  # 7 items policy may rewrite
MAX_ORDERS = 10

_CROP_KINDS = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON")
_ANIMAL_KINDS = ("COW", "SHEEP", "GOOSE")
_DRIVER_KINDS = _ANIMAL_KINDS + _CROP_KINDS  # 8 supply-driver counts


def _v41_path() -> str:
    row = ledger.get_artifact_by_name("opp_v41")
    if row is not None:
        return row["path"]
    return str(LAB / "artifacts" / "8951ff93" / "main.py")


def _load_v41_agent():
    """exec()s the artifact source into a *fresh* namespace so module-global
    state (the _R*_STATES dicts, _IMPL, etc.) never leaks between games --
    mirrors how kaggle_environments loads a fresh module per env.run() when
    given a file path, and how lab.arena re-imports per worker process."""
    path = _v41_path()
    src = Path(path).read_text(encoding="utf-8")
    ns = {"__name__": "v41_isolated_" + Path(path).parent.name, "__builtins__": __builtins__}
    exec(compile(src, path, "exec"), ns)
    fn = ns.get("agent")
    if not callable(fn):
        raise RuntimeError(f"v41 artifact at {path} did not bind a final callable 'agent'")
    return fn


def _tile_counts(tiles):
    counts = {k: 0 for k in _DRIVER_KINDS}
    for row in tiles:
        for tile in row:
            if not isinstance(tile, dict):
                continue
            kind = tile.get("kind")
            if kind == "PLANT" and tile.get("crop") in counts:
                counts[tile["crop"]] += 1
            elif kind in ("COOP", "PASTURE") and tile.get("animal") in counts:
                counts[tile["animal"]] += 1
    return counts


def extract_features(obs, base_action) -> np.ndarray:
    """58 floats. Order is fixed and documented here; downstream code
    (bc.py, collect.py) must import FEATURE_NAMES rather than re-derive it."""
    player = obs["player"]
    opp = 1 - player
    me = obs["farms"][player]
    opp_farm = obs["farms"][opp]
    private = obs["private"]
    shed = private.get("shed", {}) or {}
    seeds = private.get("seeds", {}) or {}
    market = obs.get("market", {}) or {}
    inventory = market.get("inventory", {}) or {}
    prices = market.get("prices", {}) or {}
    step = int(obs["step"])
    day = int(obs.get("day", step // 24))
    hour = int(obs.get("hour", step % 24))

    base_sell_qty = {}
    for o in (base_action.get("market") or []):
        if o and o[0] == "SELL" and len(o) >= 3:
            base_sell_qty[o[1]] = base_sell_qty.get(o[1], 0) + max(0, int(o[2]))

    opp_counts = _tile_counts(opp_farm["tiles"])

    feats = [
        step / 720.0,
        day / 30.0,
        hour / 24.0,
        me["money"] / 1e5,
        opp_farm["money"] / 1e5,
        sum(shed.values()) / 100.0,  # shed load fraction
        len(base_action.get("market") or []) / float(MAX_ORDERS),  # orders already used
        me.get("hires_today", 0) / 10.0,
        len(me.get("unlocked_quadrants", [])) / 4.0,
    ]
    feats += [shed.get(p, 0) / 100.0 for p in V41_PRODUCTS]          # 9: my shed counts
    feats += [inventory.get(p, 0) / 1000.0 for p in V41_PRODUCTS]    # 9: market inventory
    feats += [prices.get(p, 0) / 200.0 for p in V41_PRODUCTS]        # 9: prices
    feats += [base_sell_qty.get(p, 0) / 100.0 for p in V41_PRODUCTS]  # 9: v41's proposed sells
    feats += [opp_counts[k] / 25.0 for k in _DRIVER_KINDS]           # 8: opp supply drivers
    feats += [seeds.get(c, 0) / 50.0 for c in _CROP_KINDS]           # 5: my seed stock
    return np.asarray(feats, dtype=np.float32)


def base_frac_prio(base_action, shed):
    """v41's own decision, restated in the policy's (frac, priority) action
    space over FREE_ITEMS -- used ONLY for the BC target log (bc.py), which
    trains a per-item delta toward zero regardless of the fine-grained slot
    structure below. NOTE: this MERGES multiple SELL orders for the same
    item into one (e.g. v41's sell_lead layer can emit two separate SELL
    orders for the same item with merge=False, see artifact main.py line
    ~629), which loses information -- apply_policy below does NOT use this;
    it uses base_frac_prio_slots, which preserves duplicates and is what
    actually has to reproduce v41 exactly at delta=0."""
    base_sell_qty = {}
    for o in (base_action.get("market") or []):
        if o and o[0] == "SELL" and len(o) >= 3 and o[1] in FREE_ITEMS:
            base_sell_qty[o[1]] = base_sell_qty.get(o[1], 0) + max(0, int(o[2]))
    frac = np.zeros(len(FREE_ITEMS), dtype=np.float32)
    prio = np.zeros(len(FREE_ITEMS), dtype=np.float32)
    sell_order = [o for o in (base_action.get("market") or [])
                  if o and o[0] == "SELL" and len(o) >= 3 and o[1] in FREE_ITEMS]
    for rank, o in enumerate(sell_order):
        j = FREE_ITEMS.index(o[1])
        held = int(shed.get(o[1], 0))
        # v41's proposed qty can exceed the pre-turn shed snapshot when this
        # turn's own harvest/collection adds stock before the market runs --
        # clip to 1.0 ("sell everything you'll have") rather than overshoot
        # what apply_policy can ever emit (its own frac is clamped to [0,1]).
        frac[j] = min(1.0, (max(0, int(o[2])) / held) if held > 0 else 1.0)
        prio[j] = len(FREE_ITEMS) - rank  # earlier slot = higher priority
    return frac, prio, base_sell_qty


def _sellable_capacity(base_action, shed):
    """obs['private']['shed'] is a snapshot from *before* this turn's field
    ops (HARVEST/COLLECT_FERTILIZER/...) resolve, but v41's own SELL qty can
    exceed it when this turn's own harvest adds stock ahead of the market
    step (confirmed directly: seed 880000 step 149, shed WOOL=0 but v41
    proposes SELL WOOL 6 -- a real, not rare, case). We don't re-run v41's
    field simulation to get the true post-harvest count, so the capacity a
    frac of 1.0 must reconstruct back to is defined as
    max(pre-turn shed, total qty v41 itself proposes to sell) per item --
    exact whenever v41 sells everything it will hold (frac clips to 1.0
    there anyway), and only an approximation in the unlikely case v41 both
    undersells a same-turn harvest AND our own frac tries to sell more of it
    (candidate_qty would still be capped to this same capacity, never to a
    number smaller than v41 itself trusted)."""
    totals = {}
    for o in (base_action.get("market") or []):
        if o and o[0] == "SELL" and len(o) >= 3 and o[1] in FREE_ITEMS:
            totals[o[1]] = totals.get(o[1], 0) + max(0, int(o[2]))
    return {it: max(int(shed.get(it, 0)), totals.get(it, 0)) for it in FREE_ITEMS}


def base_frac_prio_slots(base_action, shed):
    """Per-SLOT (not per-item) restatement of v41's free-item SELLs, in
    original order, preserving duplicates. `frac` for each slot is against a
    *running* remaining-capacity balance (see _sellable_capacity) so that
    when the same item appears in two slots (v41's sell_lead pull-forward
    can add a second SELL for an item the tape already sells that turn), the
    two fracs partition the stock exactly the way v41 did -- this plus the
    capacity fix above is what makes delta=0 reproduce v41 bit-for-bit;
    base_frac_prio's per-item merge, and a naive raw-shed denominator,
    cannot (confirmed by fidelity batches p2-bc-fidelity-9011af92 and
    -1b51037e: a zero-output policy still lost 0-20 to v41's own mirror
    before these two fixes)."""
    sell_slots = [o for o in (base_action.get("market") or [])
                  if o and o[0] == "SELL" and len(o) >= 3 and o[1] in FREE_ITEMS]
    remaining = _sellable_capacity(base_action, shed)
    n = len(sell_slots)
    slots = []
    for rank, o in enumerate(sell_slots):
        item = o[1]
        qty = max(0, int(o[2]))
        held_before = remaining[item]
        frac = min(1.0, (qty / held_before)) if held_before > 0 else 1.0
        remaining[item] = max(0, held_before - qty)
        slots.append({"item": item, "frac": frac, "prio": float(n - rank)})
    idle_items = [it for it in FREE_ITEMS if it not in {s["item"] for s in slots}]
    return slots, idle_items


def _apply_free_sells(market, chosen):
    """chosen: list of ['SELL', item, qty] for FREE_ITEMS, best-priority first.
    Rewrites only indices that were already a free-item SELL in `market`
    (filled with a qty=0 placeholder if unused -- same convention v41 itself
    uses, see artifact main.py line ~612, "a zero-quantity order keeps later
    market race slots intact"), plus may append new orders at the end, all
    capped so total length never exceeds MAX_ORDERS. Every other index
    (non-SELL orders, and WHEAT/FERTILIZER SELLs) is left byte-identical at
    its original position -- this is what makes "never move WHEAT/FERTILIZER
    into an earlier slot" hold by construction rather than by a check."""
    market = list(market)
    free_positions = [i for i, o in enumerate(market) if o and o[0] == "SELL" and len(o) >= 3 and o[1] in FREE_ITEMS]
    non_free_count = len(market) - len(free_positions)
    capacity = max(0, MAX_ORDERS - non_free_count)
    chosen = chosen[:capacity]

    orig_items_at = {i: market[i][1] for i in free_positions}
    slots = list(free_positions)
    extra = capacity - len(free_positions)
    if extra > 0:
        slots += list(range(len(market), len(market) + extra))

    out = list(market)
    for i, idx in enumerate(slots):
        order = chosen[i] if i < len(chosen) else None
        if idx < len(out):
            out[idx] = order if order is not None else ["SELL", orig_items_at[idx], 0]
        elif order is not None:
            out.append(order)
    return out


def apply_policy(obs, base_action, policy):
    """policy(features: np.ndarray) -> (delta_frac[7], delta_prio[7]), a
    RESIDUAL on top of v41's own (frac, priority) restatement of its action
    (base_frac_prio, above). final = clip(base + delta). A policy that always
    outputs (0, 0) -- true of a freshly zero-initialised BC network before
    any training moves it -- reproduces v41's sells exactly: same items, same
    quantities, same relative slot order. This is what makes "warm start" a
    guarantee of the parameterisation rather than something merely learned:
    BC only has to keep the residual near zero on v41's own data (it starts
    there for free), and RL later is what pushes deltas away from zero to
    trade fidelity for win rate. policy=None skips all of this and returns
    v41's action untouched (still exact, but without the feature-extraction
    and rebuild round-trip -- used for the identity/no-policy case)."""
    if policy is None:
        return base_action
    market = list(base_action.get("market") or [])
    shed = obs["private"].get("shed", {}) or {}

    slots, idle_items = base_frac_prio_slots(base_action, shed)
    feats = extract_features(obs, base_action)
    delta_frac, delta_prio = policy(feats)
    delta_by_item = {item: (float(delta_frac[j]), float(delta_prio[j])) for j, item in enumerate(FREE_ITEMS)}

    candidates = []
    remaining = _sellable_capacity(base_action, shed)
    for s in slots:  # original slots first, same running-remaining order v41 itself used
        item = s["item"]
        df, dp = delta_by_item[item]
        f = max(0.0, min(1.0, s["frac"] + df))
        held_before = remaining[item]
        qty = min(held_before, int(round(f * held_before)))
        remaining[item] -= qty
        if qty > 0:
            candidates.append((s["prio"] + dp, ["SELL", item, qty]))
    for item in idle_items:  # items v41 didn't sell at all: a nonzero delta can still open a sell
        df, dp = delta_by_item[item]
        held = remaining[item]
        f = max(0.0, min(1.0, df))  # base frac is 0 for an idle item
        qty = min(held, int(round(f * held)))
        if qty > 0:
            candidates.append((dp, ["SELL", item, qty]))  # base prio is 0 for an idle item
    candidates.sort(key=lambda t: -t[0])
    chosen = [c[1] for c in candidates]

    new_market = _apply_free_sells(market, chosen)
    out = dict(base_action)
    out["market"] = new_market
    return out


def make_agent(policy, log=None):
    """Factory: call once per game (fresh v41 instance each time -- do not
    reuse the returned callable across env.run() calls). If `log` is a list,
    (features, base_sell_fractions_by_FREE_ITEMS) pairs are appended on every
    turn where v41 proposes/holds sellable inventory."""
    v41 = _load_v41_agent()

    def agent(observation, configuration=None):
        base_action = v41(observation, configuration)
        if log is not None:
            shed = observation["private"].get("shed", {}) or {}
            base_frac, base_prio, base_sell_qty = base_frac_prio(base_action, shed)
            has_signal = any(shed.get(it, 0) > 0 or base_sell_qty.get(it, 0) > 0 for it in FREE_ITEMS)
            if has_signal:
                feats = extract_features(observation, base_action)
                # Logged under the identity wrapper, so v41's own action *is* the
                # target -- these are also exactly this turn's residual base
                # (see apply_policy / base_frac_prio), i.e. the correct BC
                # target-delta is (target - base) == 0 on this dataset by
                # construction. bc.py trains toward that; see its docstring.
                log.append((feats, base_frac, base_prio))
        return apply_policy(observation, base_action, policy)

    return agent


if __name__ == "__main__":
    # ponytail self-check: identity wrapper must reproduce v41 bit-for-bit
    # actions on a handful of synthetic observations (no game engine needed).
    fake_obs = {
        "player": 0, "step": 100, "day": 4, "hour": 4,
        "farms": [
            {"money": 5000, "tiles": [[None] * 10 for _ in range(10)], "farmer": [0, 0], "hands": [],
             "unlocked_quadrants": ["NW"], "hires_today": 0},
            {"money": 4000, "tiles": [[None] * 10 for _ in range(10)], "farmer": [0, 0], "hands": [],
             "unlocked_quadrants": ["NW"], "hires_today": 0},
        ],
        "private": {"shed": {"WHEAT": 10, "STRAWBERRY": 3}, "seeds": {}, "inventories": [{}]},
        "market": {"inventory": {p: 100 for p in V41_PRODUCTS}, "prices": {p: 20 for p in V41_PRODUCTS}},
        "town": {"unlocked_shops": []},
    }
    base_action = {"market": [["SELL", "WHEAT", 5], ["SELL", "STRAWBERRY", 3], ["BUY_SEED", "WHEAT", 1]]}
    assert apply_policy(fake_obs, base_action, None) is base_action
    feats = extract_features(fake_obs, base_action)
    print("feature dim:", feats.shape[0])

    def zero_policy(f):  # simulates a freshly zero-initialised residual network
        return np.zeros(len(FREE_ITEMS), dtype=np.float32), np.zeros(len(FREE_ITEMS), dtype=np.float32)

    out = apply_policy(fake_obs, base_action, zero_policy)
    assert out["market"] == base_action["market"], "zero residual must reproduce v41's action exactly"
    print("zero-residual identity OK:", out["market"])

    def dumb_policy(f):  # a nonzero residual should still respect the invariants
        return np.ones(len(FREE_ITEMS), dtype=np.float32), np.arange(len(FREE_ITEMS), dtype=np.float32)

    out = apply_policy(fake_obs, base_action, dumb_policy)
    assert out["market"][0] == ["SELL", "WHEAT", 5], "WHEAT sell must stay untouched at its original index"
    assert out["market"][2] == ["BUY_SEED", "WHEAT", 1], "non-sell order must stay untouched at its original index"
    print("market_env self-check OK:", out["market"])
