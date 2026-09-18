"""Packages a trained BC checkpoint as a single main.py: v41's source verbatim,
followed by an embedded (base85+zlib) numpy state dict, a pure-numpy forward
pass (no torch at runtime), a self-contained copy of the market_env seam
logic, and a freshly bound final `agent`.

Mirrors v41's own "agent = globals().pop('agent')" convention at the very end:
get_last_callable() (kaggle_environments.agent) picks the *last-inserted*
callable in the exec namespace by dict order, not by name -- assigning to an
existing 'agent' key updates it in place without moving it to the end, so any
helper `def` after the last pop/reassign would silently become the selected
entry point. Every helper this module adds is defined *before* the wrapper
`def agent`, and the final line pops+reassigns 'agent' one more time so it is
provably the last-inserted callable regardless of what got embedded above it.

Usage: python -m lab.p2.export --checkpoint lab/p2/data/bc_model.pt --out lab/p2/data/v41_bc_main.py
"""
import argparse
import base64
import io
import textwrap
import zlib
from pathlib import Path

import numpy as np
import torch

from lab import ledger
from lab.p2.bc import MarketMLP
from lab.p2.market_env import FREE_ITEMS, V41_PRODUCTS, MAX_ORDERS


def _weights_blob(checkpoint_path):
    ckpt = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    model = MarketMLP(ckpt["in_dim"], hidden=ckpt["hidden"])
    model.load_state_dict(ckpt["state_dict"])
    arrays = {k: v.detach().numpy().astype(np.float32) for k, v in model.state_dict().items()}
    buf = io.BytesIO()
    np.savez(buf, **arrays)
    blob = base64.b85encode(zlib.compress(buf.getvalue(), 9)).decode("ascii")
    return blob, ckpt["in_dim"], ckpt["hidden"]


_TEMPLATE = '''

# ==== lab/p2/export.py: BC market policy (numpy-only, no torch at runtime) ====
import base64 as _p2b64, zlib as _p2zlib, io as _p2io
import numpy as _p2np

_V41_AGENT = agent  # capture v41's final callable before we ever touch the 'agent' name again
del agent

_P2_FREE_ITEMS = {free_items!r}
_P2_PRODUCTS = {products!r}
_P2_MAX_ORDERS = {max_orders!r}
_P2_CROP_KINDS = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON")
_P2_DRIVER_KINDS = ("COW", "SHEEP", "GOOSE") + _P2_CROP_KINDS

_P2_BLOB = {blob!r}
_p2_npz = _p2np.load(_p2io.BytesIO(_p2zlib.decompress(_p2b64.b85decode(_P2_BLOB))))
_P2_W = {{k: _p2_npz[k] for k in _p2_npz.files}}


def _p2_forward(x):
    """Returns (delta_frac, delta_prio) -- a residual on v41's own decision,
    see market_env.apply_policy. Zero-initialised heads at training start
    mean an untrained/undertrained checkpoint still reproduces v41 exactly;
    only a checkpoint that has actually learned useful nonzero deltas (via
    BC-on-non-mirror-data or RL) should differ from raw v41 in practice."""
    h = _p2np.maximum(0.0, x @ _P2_W["body.0.weight"].T + _P2_W["body.0.bias"])
    h = _p2np.maximum(0.0, h @ _P2_W["body.2.weight"].T + _P2_W["body.2.bias"])
    delta_frac = _p2np.tanh(h @ _P2_W["frac_head.weight"].T + _P2_W["frac_head.bias"])
    delta_prio = h @ _P2_W["prio_head.weight"].T + _P2_W["prio_head.bias"]
    return delta_frac, delta_prio


def _p2_tile_counts(tiles):
    counts = {{k: 0 for k in _P2_DRIVER_KINDS}}
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


def _p2_extract_features(obs, base_action):
    player = obs["player"]; opp = 1 - player
    me = obs["farms"][player]; opp_farm = obs["farms"][opp]
    private = obs["private"]; shed = private.get("shed", {{}}) or {{}}
    seeds = private.get("seeds", {{}}) or {{}}
    market = obs.get("market", {{}}) or {{}}
    inventory = market.get("inventory", {{}}) or {{}}
    prices = market.get("prices", {{}}) or {{}}
    step = int(obs["step"]); day = int(obs.get("day", step // 24)); hour = int(obs.get("hour", step % 24))
    base_sell_qty = {{}}
    for o in (base_action.get("market") or []):
        if o and o[0] == "SELL" and len(o) >= 3:
            base_sell_qty[o[1]] = base_sell_qty.get(o[1], 0) + max(0, int(o[2]))
    opp_counts = _p2_tile_counts(opp_farm["tiles"])
    feats = [
        step / 720.0, day / 30.0, hour / 24.0,
        me["money"] / 1e5, opp_farm["money"] / 1e5,
        sum(shed.values()) / 100.0,
        len(base_action.get("market") or []) / float(_P2_MAX_ORDERS),
        me.get("hires_today", 0) / 10.0,
        len(me.get("unlocked_quadrants", [])) / 4.0,
    ]
    feats += [shed.get(p, 0) / 100.0 for p in _P2_PRODUCTS]
    feats += [inventory.get(p, 0) / 1000.0 for p in _P2_PRODUCTS]
    feats += [prices.get(p, 0) / 200.0 for p in _P2_PRODUCTS]
    feats += [base_sell_qty.get(p, 0) / 100.0 for p in _P2_PRODUCTS]
    feats += [opp_counts[k] / 25.0 for k in _P2_DRIVER_KINDS]
    feats += [seeds.get(c, 0) / 50.0 for c in _P2_CROP_KINDS]
    return _p2np.asarray(feats, dtype=_p2np.float32)


def _p2_apply_free_sells(market, chosen):
    market = list(market)
    free_positions = [i for i, o in enumerate(market) if o and o[0] == "SELL" and len(o) >= 3 and o[1] in _P2_FREE_ITEMS]
    non_free_count = len(market) - len(free_positions)
    capacity = max(0, _P2_MAX_ORDERS - non_free_count)
    chosen = chosen[:capacity]
    orig_items_at = {{i: market[i][1] for i in free_positions}}
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


def _p2_sellable_capacity(base_action, shed):
    # obs['private']['shed'] predates this turn's field ops (HARVEST/etc.),
    # so v41's own SELL qty can exceed it -- capacity is whichever is larger,
    # per item, exactly mirroring lab/p2/market_env._sellable_capacity.
    totals = {{}}
    for o in (base_action.get("market") or []):
        if o and o[0] == "SELL" and len(o) >= 3 and o[1] in _P2_FREE_ITEMS:
            totals[o[1]] = totals.get(o[1], 0) + max(0, int(o[2]))
    return {{it: max(int(shed.get(it, 0)), totals.get(it, 0)) for it in _P2_FREE_ITEMS}}


def _p2_base_frac_prio_slots(base_action, shed):
    sell_slots = [o for o in (base_action.get("market") or [])
                  if o and o[0] == "SELL" and len(o) >= 3 and o[1] in _P2_FREE_ITEMS]
    remaining = _p2_sellable_capacity(base_action, shed)
    n = len(sell_slots)
    slots = []
    for rank, o in enumerate(sell_slots):
        item = o[1]
        qty = max(0, int(o[2]))
        held_before = remaining[item]
        frac = min(1.0, (qty / held_before)) if held_before > 0 else 1.0
        remaining[item] = max(0, held_before - qty)
        slots.append((item, frac, float(n - rank)))
    idle_items = [it for it in _P2_FREE_ITEMS if it not in {{s[0] for s in slots}}]
    return slots, idle_items


def _p2_apply_policy(obs, base_action):
    market = list(base_action.get("market") or [])
    shed = obs["private"].get("shed", {{}}) or {{}}
    slots, idle_items = _p2_base_frac_prio_slots(base_action, shed)
    feats = _p2_extract_features(obs, base_action)
    delta_frac, delta_prio = _p2_forward(feats[None, :])
    delta_frac, delta_prio = delta_frac[0], delta_prio[0]
    delta_by_item = {{item: (float(delta_frac[j]), float(delta_prio[j])) for j, item in enumerate(_P2_FREE_ITEMS)}}

    candidates = []
    remaining = _p2_sellable_capacity(base_action, shed)
    for item, base_frac, base_prio in slots:
        df, dp = delta_by_item[item]
        f = max(0.0, min(1.0, base_frac + df))
        held_before = remaining[item]
        qty = min(held_before, int(round(f * held_before)))
        remaining[item] -= qty
        if qty > 0:
            candidates.append((base_prio + dp, ["SELL", item, qty]))
    for item in idle_items:
        df, dp = delta_by_item[item]
        held = remaining[item]
        f = max(0.0, min(1.0, df))
        qty = min(held, int(round(f * held)))
        if qty > 0:
            candidates.append((dp, ["SELL", item, qty]))
    candidates.sort(key=lambda t: -t[0])
    chosen = [c[1] for c in candidates]
    new_market = _p2_apply_free_sells(market, chosen)
    out = dict(base_action)
    out["market"] = new_market
    return out


def agent(observation, configuration=None):
    base_action = _V41_AGENT(observation, configuration)
    try:
        return _p2_apply_policy(observation, base_action)
    except Exception:
        return base_action  # fail-safe: never worse than raw v41


agent = globals().pop("agent")  # re-tail 'agent' so get_last_callable() selects it, not a helper above
'''


def export(checkpoint_path, out_path, v41_path=None):
    v41_path = v41_path or ledger.get_artifact_by_name("opp_v41")["path"]
    v41_src = Path(v41_path).read_text(encoding="utf-8")
    blob, in_dim, hidden = _weights_blob(checkpoint_path)
    tail = _TEMPLATE.format(
        free_items=tuple(FREE_ITEMS), products=tuple(V41_PRODUCTS), max_orders=MAX_ORDERS, blob=blob,
    )
    full = v41_src + tail
    Path(out_path).write_text(full, encoding="utf-8")
    print(f"wrote {out_path} ({len(full)} bytes, weights blob {len(blob)} chars, in_dim={in_dim} hidden={hidden})")
    return out_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    export(args.checkpoint, args.out)


if __name__ == "__main__":
    main()
