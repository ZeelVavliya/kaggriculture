"""Replay a batch's games and emit ranked findings keyed to game_id and step.

Each check below exists because it is a documented defect class in the kernel's
own bug table / loss analysis (see plan sec 1.7). Reads env.toJSON()-shaped
replay files (steps: list of [p0_step, p1_step], each a dict with
action/reward/info/observation/status).
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

from lab import ledger

MELON_CAP = 6
SHED_CAP = 100
MAX_MARKET_ORDERS = 10
ACT_TIMEOUT_S = 1.0


def load_replay(path):
    """Reads a replay written as .json or .json.gz."""
    path = Path(path)
    if path.suffix == ".gz":
        import gzip
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            return json.load(fh)
    return json.loads(path.read_text(encoding="utf-8"))


def _tiles(step_obs):
    return step_obs["farms"][step_obs["player"]]["tiles"]


def _iter_tile_cells(tiles):
    for y, row in enumerate(tiles):
        for x, cell in enumerate(row):
            yield (x, y), cell


def audit_replay(replay: dict, game_id: str):
    findings = []
    steps = replay["steps"]

    # per-player running state trackers
    prev_tiles = [None, None]
    prev_overage = [None, None]
    melons = [{}, {}]  # player -> {(x,y): last seen melon yield}
    sell_events = defaultdict(list)  # (item) -> list of (player, step)

    for step_idx, pair in enumerate(steps):
        for pid in (0, 1):
            st = pair[pid]
            obs = st.get("observation")
            if not obs or "farms" not in obs:
                continue

            # 6. non-DONE status / exceptions (only meaningful once episode should be finishing;
            #    always flag an "ERROR" status, and flag non-DONE at the very last step)
            status = st.get("status")
            if status not in ("ACTIVE", "DONE", "INACTIVE", None):
                findings.append({"severity": "high", "check": "non_done_status", "game_id": game_id,
                                  "step": step_idx, "player": pid, "detail": f"status={status}"})

            farm = obs["farms"][pid] if pid < len(obs.get("farms", [])) else None
            private = obs.get("private")
            tiles = farm["tiles"] if farm else None

            # 1. animal escapes: an animal-bearing tile loses its "animal" key
            #    between consecutive observations of this player (consecutive_unfed>=2 rule).
            if tiles and prev_tiles[pid]:
                for (x, y), cell in _iter_tile_cells(tiles):
                    prev_cell = prev_tiles[pid][y][x] if y < len(prev_tiles[pid]) and x < len(prev_tiles[pid][y]) else None
                    if (isinstance(prev_cell, dict) and "animal" in prev_cell
                            and isinstance(cell, dict) and "animal" not in cell
                            and cell.get("kind") == prev_cell.get("kind")):
                        findings.append({"severity": "high", "check": "animal_escape", "game_id": game_id,
                                          "step": step_idx, "player": pid,
                                          "detail": f"{prev_cell.get('animal')} escaped at ({x},{y})"})
            if tiles:
                prev_tiles[pid] = tiles

            # 2. melon leak: a melon tile that stops being a melon (harvested, decayed, dug)
            #    while its last seen yield was under the 6-unit ceiling -- the CARE-above-WATER bug.
            if tiles:
                seen = {}
                for (x, y), cell in _iter_tile_cells(tiles):
                    if isinstance(cell, dict) and cell.get("kind") == "PLANT" and cell.get("crop") == "MELON":
                        seen[(x, y)] = cell.get("yield_units", 0)
                for pos, yu in melons[pid].items():
                    if pos not in seen and yu < MELON_CAP:
                        findings.append({"severity": "medium", "check": "melon_underyield", "game_id": game_id,
                                          "step": step_idx, "player": pid,
                                          "detail": f"melon at {pos} left the field with yield {yu} < {MELON_CAP}"})
                melons[pid] = seen

            # 3. shed load >= 100 at end-of-day (hour wraps to 0 signals a fresh day boundary
            #    just occurred, i.e. this observation is post end-of-day drop)
            if private and "shed" in private:
                shed_total = sum(private["shed"].values())
                if obs.get("hour") == 0 and shed_total >= SHED_CAP:
                    findings.append({"severity": "high", "check": "shed_overflow", "game_id": game_id,
                                      "step": step_idx, "player": pid,
                                      "detail": f"shed total={shed_total} >= cap {SHED_CAP} at day boundary"})

            # 4. produce stuck in unit inventory at terminal step
            if step_idx == len(steps) - 1 and private and "inventories" in private:
                for ui, inv in enumerate(private["inventories"]):
                    for item, n in inv.items():
                        if n > 0:
                            findings.append({"severity": "medium", "check": "stuck_in_inventory", "game_id": game_id,
                                              "step": step_idx, "player": pid,
                                              "detail": f"unit {ui} holds {n}x {item} at terminal, never DROPped"})

            # 5. market orders per turn vs the 10 cap
            action = st.get("action") or {}
            orders = action.get("market") or []
            if len(orders) > MAX_MARKET_ORDERS:
                findings.append({"severity": "medium", "check": "market_orders_over_cap", "game_id": game_id,
                                  "step": step_idx, "player": pid,
                                  "detail": f"{len(orders)} market orders > cap {MAX_MARKET_ORDERS} (silently dropped)"})

            # record SELL events for the premium-preemption check (#8)
            for order in orders:
                if isinstance(order, (list, tuple)) and len(order) >= 2 and order[0] == "SELL":
                    sell_events[order[1]].append((pid, step_idx))

            # 6b. wall time per turn, proxy via remainingOverageTime decreasing turn-to-turn
            overage = obs.get("remainingOverageTime")
            if overage is not None and prev_overage[pid] is not None and overage < prev_overage[pid]:
                findings.append({"severity": "low", "check": "overage_time_consumed", "game_id": game_id,
                                  "step": step_idx, "player": pid,
                                  "detail": f"remainingOverageTime dropped {prev_overage[pid]}->{overage} "
                                            f"(turn exceeded {ACT_TIMEOUT_S}s actTimeout)"})
            if overage is not None:
                prev_overage[pid] = overage

        # non-DONE at the very last recorded step is a hard failure
        if step_idx == len(steps) - 1:
            for pid in (0, 1):
                st = steps[step_idx][pid]
                if st.get("status") != "DONE":
                    findings.append({"severity": "critical", "check": "not_done_at_terminal", "game_id": game_id,
                                      "step": step_idx, "player": pid, "detail": f"status={st.get('status')}"})

    # 8. pre-emption: the opponent sold an item exactly one turn before we START a sell run of it.
    #    Counting every adjacent sell (the first version) flagged routine back-and-forth trading;
    #    the kernel's documented loss is specifically the opponent getting in first. WHEAT and
    #    FERTILIZER are included because that is the exact case that reversed 11 C92 losses.
    contested = {"MELON", "STRAWBERRY", "WOOL", "MILK", "FERTILIZER", "WHEAT"}
    for item, events in sell_events.items():
        if item not in contested:
            continue
        sold = [set(), set()]
        for p_, s_ in events:
            sold[p_].add(s_)
        for pid in (0, 1):
            for s_ in sorted(sold[pid]):
                if (s_ - 1) in sold[1 - pid] and (s_ - 1) not in sold[pid] and (s_ - 1) >= 0:
                    findings.append({"severity": "medium", "check": "preempted_sell", "game_id": game_id,
                                      "step": s_, "player": pid,
                                      "detail": f"opponent sold {item} at step {s_ - 1}, we started selling at {s_}"})

    return findings


SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def audit_batch(batch_id: str, conn=None):
    own = conn is None
    conn = conn or ledger.connect()
    games = conn.execute("SELECT game_id, replay_path, sha_p0, sha_p1 FROM games WHERE batch_id=?", (batch_id,)).fetchall()
    all_findings = []
    for g in games:
        if not g["replay_path"]:
            continue  # harness-error rows and p2 batches have no replay
        path = Path(g["replay_path"])
        if not path.exists():
            continue
        replay = load_replay(path)
        for f in audit_replay(replay, g["game_id"]):
            if f.get("player") in (0, 1):
                f["sha"] = g["sha_p0"] if f["player"] == 0 else g["sha_p1"]
            all_findings.append(f)
    all_findings.sort(key=lambda f: SEVERITY_ORDER.get(f["severity"], 9))
    if own:
        conn.close()
    return all_findings


def print_findings(findings, limit=40):
    counts = defaultdict(int)
    for f in findings:
        counts[f["check"]] += 1
    print("finding counts by check:")
    for check, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {check}: {n}")
    print(f"\ntop {min(limit, len(findings))} findings:")
    for f in findings[:limit]:
        print(f"  [{f['severity']:<8}] {f['check']:<22} game={f['game_id']} step={f['step']} "
              f"player={f.get('player')} - {f['detail']}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--batch", required=True)
    p.add_argument("--limit", type=int, default=40)
    args = p.parse_args()
    findings = audit_batch(args.batch)
    print_findings(findings, args.limit)


if __name__ == "__main__":
    main()
