"""
Kaggriculture agent - "Portfolio" v3

Rebuilt against the UPDATED environment (hinge price curves, flat town-centre
demand). Three findings drive the design:

  1. MELON is the best asset in the game. Water-only it reaches its 6-unit cap
     (fertilizer adds nothing), so a tile yields 6 units per ~10-day cycle for
     an $80 seed and ~12 actions. Its glut curve is `sq` with T=300, so it
     still pays $171/unit at 90 units sold. That is ~$2,400/tile/season for a
     sixth of the actions a goose costs.

  2. EVERY price curve is concave, so a diversified basket beats any
     monoculture. Selling 50 melon + 25 wool + 25 milk + 50 egg + 50 tomato
     banks far more than 200 units of any single good, because each sale walks
     down its own curve independently.

  3. Mirror matches are decided by counter-positioning. Replay 90643183 showed
     two goose farms crushing the egg price to $39 while milk hit $351 and
     strawberry $318 purely because nobody produced them. The opponent's farm
     is public, so we read their tile mix and steer away from it.

Also fixed from v2: grow feed wheat instead of buying it (buying drove wheat
25 -> 60 and ate the entire goose margin), and unlock land instead of letting
cash idle.
"""

CROPS = {
    "MELON":  {"seed": 80,  "first": 10, "max_day": 12, "cap_age": 10, "units": 6},
    "TOMATO": {"seed": 50,  "first": 8,  "max_day": 8,  "cap_age": 8,  "units": 4},
    "WHEAT":  {"seed": 10,  "first": 2,  "max_day": 4,  "cap_age": 4,  "units": 4},
    "CARROT": {"seed": 20,  "first": 2,  "max_day": 3,  "cap_age": 3,  "units": 3},
    "STRAWBERRY": {"seed": 100, "first": 10, "max_day": 10, "cap_age": 10, "units": 4},
}
ONGOING = ("TOMATO", "STRAWBERRY")
ANIMAL_OF = {"COOP": "GOOSE", "PASTURE": "SHEEP"}
ANIMAL_COST = {"GOOSE": 300, "COW": 400, "SHEEP": 500}
BASE = {"WHEAT": 25, "CARROT": 35, "TOMATO": 60, "STRAWBERRY": 120,
        "MELON": 250, "EGG": 50, "MILK": 160, "WOOL": 200, "FERTILIZER": 100}

SHED_TILES = [(4, 4), (5, 4), (4, 5), (5, 5)]
LAND_PRICES = [0, 1000, 2000, 4000]

# --- tunables -------------------------------------------------------------
MAX_HANDS = 11
SHED_CAP = 100
CASH_FLOOR = 120

# Target tile counts once land allows. Melon is the engine; wheat feeds the
# animals; geese supply eggs + free fertilizer; sheep/cow are premium trickle.
TARGET_MELON = 16
TARGET_TOMATO = 4
TARGET_WHEAT = 4
TARGET_GEESE = 6
TARGET_SHEEP = 2
TARGET_COW = 2

LAST_PLANT_DAY = {"MELON": 19, "TOMATO": 20, "WHEAT": 26, "CARROT": 26,
                  "STRAWBERRY": 16}
LAST_ANIMAL_DAY = 20
DUMP_DAY = 28              # final liquidation: price no longer matters

# Sell a premium good only while its price holds above frac*base. This walks
# each concave curve down to the point where the next unit is no longer worth
# more than the alternatives, instead of dumping the whole stack at once.
HOLD_FRAC = {"MELON": 0.55, "WOOL": 0.40, "MILK": 0.40, "STRAWBERRY": 0.35,
             "TOMATO": 0.45}
TRICKLE = {"MELON": 8, "WOOL": 5, "MILK": 5, "STRAWBERRY": 5, "TOMATO": 8}


def _dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _step_toward(pos, target):
    dx, dy = target[0] - pos[0], target[1] - pos[1]
    if dx == 0 and dy == 0:
        return None
    if abs(dx) >= abs(dy) and dx != 0:
        return "EAST" if dx > 0 else "WEST"
    return "SOUTH" if dy > 0 else "NORTH"


def _nearest_shed(pos):
    return min(SHED_TILES, key=lambda t: _dist(pos, t))


def _survey(tiles):
    plants, animals, empty_struct, weeds, empties = [], [], [], [], []
    for y, row in enumerate(tiles):
        for x, t in enumerate(row):
            if t is None:
                empties.append((x, y))
            elif t == "LOCKED" or not isinstance(t, dict):
                continue
            elif t.get("kind") == "PLANT":
                plants.append((x, y, t))
            elif t.get("kind") == "WEED":
                weeds.append((x, y))
            elif t.get("kind") in ("COOP", "PASTURE"):
                if t.get("animal"):
                    animals.append((x, y, t))
                else:
                    empty_struct.append((x, y, t["kind"]))
    return plants, animals, empty_struct, weeds, empties


def _agent(obs):
    me_id = obs["player"]
    opp_id = 1 - me_id
    day = obs.get("day", 0)
    hour = obs.get("hour", 0)
    me = obs["farms"][me_id]
    priv = obs["private"]
    prices = obs["market"]["prices"]
    money = me["money"]
    shed = dict(priv.get("shed", {}) or {})
    seeds = dict(priv.get("seeds", {}) or {})
    invs = [dict(i or {}) for i in priv.get("inventories", [{}])]

    units = [tuple(me["farmer"])] + [tuple(h) for h in me.get("hands", [])]
    n_units = len(units)
    while len(invs) < n_units:
        invs.append({})

    plants, animals, empty_struct, weeds, empties = _survey(me["tiles"])
    empties.sort(key=lambda p: min(_dist(p, s) for s in SHED_TILES))
    empty_struct.sort(key=lambda p: min(_dist((p[0], p[1]), s) for s in SHED_TILES))

    crop_counts = {}
    for _, _, t in plants:
        crop_counts[t["crop"]] = crop_counts.get(t["crop"], 0) + 1
    animal_counts = {}
    for _, _, t in animals:
        animal_counts[t["animal"]] = animal_counts.get(t["animal"], 0) + 1
    pending = {a: shed.get(a, 0) + sum(i.get(a, 0) for i in invs)
               for a in ("GOOSE", "COW", "SHEEP")}
    n_animals = len(animals)
    wheat_all = shed.get("WHEAT", 0) + sum(i.get("WHEAT", 0) for i in invs)

    # ---- counter-positioning ---------------------------------------------
    # The opponent's tiles are public. If they are scaling a product hard, its
    # price will be depressed by their sales, so we tilt away from it and
    # toward whatever they are neglecting.
    opp = obs["farms"][opp_id]
    o_plants, o_animals, _, _, _ = _survey(opp["tiles"])
    opp_mix = {}
    for _, _, t in o_plants:
        opp_mix[t["crop"]] = opp_mix.get(t["crop"], 0) + 1
    for _, _, t in o_animals:
        opp_mix[t["animal"]] = opp_mix.get(t["animal"], 0) + 1

    def contested(key, heavy):
        return opp_mix.get(key, 0) >= heavy

    t_melon = TARGET_MELON
    t_goose = TARGET_GEESE
    t_tomato = TARGET_TOMATO
    t_sheep, t_cow = TARGET_SHEEP, TARGET_COW
    if contested("MELON", 6):          # they are flooding melon
        t_melon = max(4, TARGET_MELON - 4)
        t_tomato += 2
    if contested("GOOSE", 8):          # egg glut incoming
        t_goose = max(2, TARGET_GEESE - 3)
        t_sheep += 1
    if opp_mix.get("SHEEP", 0) + opp_mix.get("COW", 0) == 0:
        # nobody is supplying wool/milk: town demand will spike them
        t_sheep += 1
        t_cow += 1

    # ======================================================================
    # MARKET
    # ======================================================================
    orders = []

    if hour == 0 and day < 29:
        work = n_animals * 4 + len(plants) * 2 + len(empty_struct) * 2 + len(empties)
        target = min(MAX_HANDS, max(4, (work + 9) // 10))
        for _ in range(min(10, max(0, target - len(me.get("hands", []))))):
            orders.append(["HIRE"])

    dump = day >= DUMP_DAY

    # -- eggs are glut-proof (log curve): always liquidate
    if shed.get("EGG", 0) > 0 and len(orders) < 10:
        orders.append(["SELL", "EGG", shed["EGG"]])

    # -- premium goods: trickle while the price holds, dump at the end
    for item, frac in HOLD_FRAC.items():
        if len(orders) >= 10:
            break
        cnt = shed.get(item, 0)
        if cnt <= 0:
            continue
        if dump:
            orders.append(["SELL", item, cnt])
        elif prices.get(item, 0) >= BASE[item] * frac:
            orders.append(["SELL", item, min(cnt, TRICKLE[item])])

    # -- carrot / fertilizer: no reason to hold
    for item in ("CARROT", "FERTILIZER"):
        if len(orders) >= 10:
            break
        keep = 0 if dump else (0 if item == "CARROT" else 2)
        if shed.get(item, 0) > keep:
            orders.append(["SELL", item, shed[item] - keep])

    # -- wheat: feed reserve first, sell only genuine surplus. We GROW this;
    #    v2 bought it and drove the price 25 -> 60 against itself.
    reserve = 0 if dump else n_animals * 3
    if shed.get("WHEAT", 0) > reserve and len(orders) < 10:
        orders.append(["SELL", "WHEAT", shed["WHEAT"] - reserve])

    # -- emergency feed only: buying wheat is a last resort, not a plan
    if n_animals > 0 and wheat_all < n_animals and len(orders) < 10:
        n = min(n_animals * 2 - wheat_all, 12,
                int(max(0, money - CASH_FLOOR) // max(1, prices.get("WHEAT", 25))))
        if n > 0:
            orders.append(["BUY_PRODUCT", "WHEAT", n])
            money -= n * prices.get("WHEAT", 25)

    # -- seeds: keep a planting float for each crop we still want
    want_seeds = []
    if day <= LAST_PLANT_DAY["MELON"]:
        need = t_melon - crop_counts.get("MELON", 0) - seeds.get("MELON", 0)
        if need > 0:
            want_seeds.append(("MELON", min(need, 4)))
    if day <= LAST_PLANT_DAY["WHEAT"]:
        need = TARGET_WHEAT - crop_counts.get("WHEAT", 0) - seeds.get("WHEAT", 0)
        if need > 0:
            want_seeds.append(("WHEAT", min(need, 4)))
    if day <= LAST_PLANT_DAY["TOMATO"]:
        need = t_tomato - crop_counts.get("TOMATO", 0) - seeds.get("TOMATO", 0)
        if need > 0:
            want_seeds.append(("TOMATO", min(need, 3)))
    for crop, n in want_seeds:
        if len(orders) >= 10:
            break
        cost = CROPS[crop]["seed"] * n
        if money >= cost + CASH_FLOOR:
            orders.append(["BUY_SEED", crop, n])
            money -= cost

    # -- animals: geese for eggs+fertilizer, sheep/cow as premium trickle
    if day <= LAST_ANIMAL_DAY and len(orders) < 10:
        housing = len(empty_struct) + len(empties)
        for kind, tgt in (("GOOSE", t_goose), ("SHEEP", t_sheep), ("COW", t_cow)):
            have = animal_counts.get(kind, 0) + pending[kind]
            if have >= tgt or housing <= 0:
                continue
            cost = ANIMAL_COST[kind]
            n = min(tgt - have, int(max(0, money - CASH_FLOOR) // cost),
                    housing, 3, SHED_CAP - sum(shed.values()))
            if n > 0:
                orders.append(["BUY_ANIMAL", kind, n])
                money -= n * cost
                housing -= n
                break

    # -- land: idle cash is wasted cash (v2 finished with $10k unspent)
    n_quads = len(me.get("unlocked_quadrants", ["NW"]))
    if n_quads < 4 and day <= 21 and len(orders) < 10:
        cost = LAND_PRICES[min(n_quads, 3)]
        if len(empties) <= 12 and money >= cost + 700:
            orders.append(["BUY_LAND"])
            money -= cost

    orders = orders[:10]

    # ======================================================================
    # UNIT JOBS
    # ======================================================================
    jobs = []

    for x, y, t in animals:
        if not t.get("fed_today"):
            jobs.append((0, x, y, ["FEED"], "WHEAT"))
    # water anything at risk of becoming a weed, or inside its bonus window
    for x, y, t in plants:
        if not t.get("watered_today"):
            jobs.append((1, x, y, ["WATER"], None))
    for x, y, t in animals:
        if t.get("yield_units", 0) > 0:
            jobs.append((2, x, y, ["HARVEST"], None))
    # harvest crops at their yield cap
    for x, y, t in plants:
        crop = t["crop"]
        age = day - t["planted_day"]
        c = CROPS.get(crop)
        if not c or t.get("yield_units", 0) <= 0:
            continue
        if crop in ONGOING:
            if age >= c["first"]:
                jobs.append((2, x, y, ["HARVEST"], None))
        elif age >= c["cap_age"]:
            jobs.append((2, x, y, ["HARVEST"], None))
    for (x, y, kind) in empty_struct:
        want = ANIMAL_OF.get(kind)
        if kind == "PASTURE":
            want = "SHEEP" if pending["SHEEP"] > 0 else ("COW" if pending["COW"] > 0 else None)
        if want and pending.get(want, 0) > 0:
            jobs.append((3, x, y, ["PLACE", want], want))
    for x, y, t in animals:
        if not t.get("cared_today"):
            jobs.append((4, x, y, ["CARE"], None))

    # build housing ahead of the animals we intend to own
    spare = list(empties)
    need_coop = max(0, min(pending["GOOSE"], t_goose - animal_counts.get("GOOSE", 0))
                    - sum(1 for e in empty_struct if e[2] == "COOP"))
    need_past = max(0, min(pending["SHEEP"] + pending["COW"],
                           t_sheep + t_cow - animal_counts.get("SHEEP", 0)
                           - animal_counts.get("COW", 0))
                    - sum(1 for e in empty_struct if e[2] == "PASTURE"))
    for _ in range(need_coop):
        if spare:
            x, y = spare.pop(0)
            jobs.append((5, x, y, ["BUILD_COOP"], None))
    for _ in range(need_past):
        if spare:
            x, y = spare.pop(0)
            jobs.append((5, x, y, ["BUILD_PASTURE"], None))

    # plant: melon first (highest value per action), then wheat, then tomato
    plan = []
    for crop, tgt in (("MELON", t_melon), ("WHEAT", TARGET_WHEAT), ("TOMATO", t_tomato)):
        if day > LAST_PLANT_DAY[crop]:
            continue
        n = min(seeds.get(crop, 0), max(0, tgt - crop_counts.get(crop, 0)))
        plan += [crop] * n
    for crop in plan:
        if not spare:
            break
        x, y = spare.pop(0)
        jobs.append((6, x, y, ["PLANT", crop], None))

    for x, y, t in animals:
        if t.get("fertilizer_available"):
            jobs.append((7, x, y, ["COLLECT_FERTILIZER"], None))
    for (x, y) in weeds:
        jobs.append((8, x, y, ["DIG"], None))
    # clear dead/decayed plants so the tile can be replanted
    for x, y, t in plants:
        c = CROPS.get(t["crop"])
        if not c:
            continue
        age = day - t["planted_day"]
        if t.get("yield_units", 0) <= 0 and age > c["max_day"]:
            jobs.append((8, x, y, ["DIG"], None))

    jobs.sort(key=lambda j: j[0])

    unit_ops = [None] * n_units

    # ---- stand-and-serve: never walk away from work underfoot -------------
    tiles = me["tiles"]

    def tile_at(p):
        x, y = p
        if 0 <= y < len(tiles) and 0 <= x < len(tiles[0]):
            return tiles[y][x]
        return None

    for ui in range(n_units):
        t = tile_at(units[ui])
        if not isinstance(t, dict):
            continue
        if t.get("animal"):
            if not t.get("fed_today") and invs[ui].get("WHEAT", 0) > 0:
                unit_ops[ui] = ["FEED"]; invs[ui]["WHEAT"] -= 1
            elif t.get("yield_units", 0) > 0:
                unit_ops[ui] = ["HARVEST"]
            elif not t.get("cared_today"):
                unit_ops[ui] = ["CARE"]
            elif t.get("fertilizer_available"):
                unit_ops[ui] = ["COLLECT_FERTILIZER"]
        elif t.get("kind") in ("COOP", "PASTURE") and not t.get("animal"):
            want = "GOOSE" if t["kind"] == "COOP" else (
                "SHEEP" if invs[ui].get("SHEEP", 0) > 0 else "COW")
            if invs[ui].get(want, 0) > 0:
                unit_ops[ui] = ["PLACE", want]; invs[ui][want] -= 1
        elif t.get("kind") == "PLANT":
            c = CROPS.get(t["crop"])
            age = day - t["planted_day"]
            if not t.get("watered_today"):
                unit_ops[ui] = ["WATER"]
            elif c and t.get("yield_units", 0) > 0 and age >= (
                    c["first"] if t["crop"] in ONGOING else c["cap_age"]):
                unit_ops[ui] = ["HARVEST"]

    # ---- morning bulk loadout: hands spawn on shed tiles ------------------
    unfed = sum(1 for _, _, t in animals if not t.get("fed_today"))
    if unfed > 0 and shed.get("WHEAT", 0) > 0:
        share = max(2, -(-unfed // max(1, n_units)) + 1)
        for ui in range(n_units):
            if unit_ops[ui] is not None or invs[ui].get("WHEAT", 0) > 0:
                continue
            if tuple(units[ui]) in SHED_TILES and shed.get("WHEAT", 0) > 0:
                take = min(shed["WHEAT"], share, 8)
                unit_ops[ui] = ["PICKUP", "WHEAT", take]
                invs[ui]["WHEAT"] = invs[ui].get("WHEAT", 0) + take
                shed["WHEAT"] -= take

    def send_courier(item, want_total, per_trip):
        carried = sum(i.get(item, 0) for i in invs)
        if shed.get(item, 0) <= 0 or carried >= want_total:
            return
        free = [i for i in range(n_units)
                if unit_ops[i] is None and invs[i].get(item, 0) == 0]
        if not free:
            return
        ui = min(free, key=lambda i: _dist(units[i], _nearest_shed(units[i])))
        if tuple(units[ui]) in SHED_TILES:
            take = min(shed[item], want_total - carried, per_trip)
            if take > 0:
                unit_ops[ui] = ["PICKUP", item, take]
                invs[ui][item] = invs[ui].get(item, 0) + take
                shed[item] -= take
        else:
            mv = _step_toward(units[ui], _nearest_shed(units[ui]))
            unit_ops[ui] = [mv] if mv else ["PASS"]

    if unfed > sum(i.get("WHEAT", 0) for i in invs):
        send_courier("WHEAT", unfed, 8)
    for kind in ("GOOSE", "SHEEP", "COW"):
        if pending.get(kind, 0) > 0 and any(e[2] == ("COOP" if kind == "GOOSE" else "PASTURE")
                                            for e in empty_struct):
            send_courier(kind, min(shed.get(kind, 0), 3), 3)

    # ---- bank produce before end of day ----------------------------------
    for ui in range(n_units):
        if unit_ops[ui] is not None:
            continue
        load = sum(v for k, v in invs[ui].items()
                   if k not in ("WHEAT", "GOOSE", "SHEEP", "COW"))
        if load >= 10 or (hour >= 21 and load > 0):
            if tuple(units[ui]) in SHED_TILES:
                unit_ops[ui] = ["DROP"]
            else:
                mv = _step_toward(units[ui], _nearest_shed(units[ui]))
                unit_ops[ui] = [mv] if mv else ["DROP"]

    # ---- greedy nearest assignment ---------------------------------------
    for (prio, x, y, op, req) in jobs:
        cands = []
        for ui in range(n_units):
            if unit_ops[ui] is not None:
                continue
            if req and invs[ui].get(req, 0) <= 0:
                continue
            cands.append((_dist(units[ui], (x, y)), ui))
        if not cands:
            continue
        _, ui = min(cands)
        if units[ui] == (x, y):
            unit_ops[ui] = op
            if req:
                invs[ui][req] = invs[ui].get(req, 0) - 1
        else:
            mv = _step_toward(units[ui], (x, y))
            unit_ops[ui] = [mv] if mv else op

    for ui in range(n_units):
        if unit_ops[ui] is None:
            unit_ops[ui] = ["PASS"]

    return {"farmer": unit_ops[0], "hands": unit_ops[1:], "market": orders}


def agent(obs):
    try:
        return _agent(obs)
    except Exception:
        return {"farmer": ["PASS"], "hands": [], "market": []}
