"""
Kaggriculture agent - "Goose Rush" v2

Core thesis (derived from the market price curves):
  * Only EGG and WHEAT resist gluts. EGG holds ~$38 even after 800 units sold;
    MILK/WOOL/STRAWBERRY/MELON collapse to the $1 floor after ~100 units.
    => Sell eggs. Never scale cows/sheep/premium crops.
  * A fed+cared goose yields 2 eggs/day ~ $80/day for a one-off $300.
    A wheat tile yields ~$22/tile/day. => Every tile wants to be a coop;
    buy feed wheat from the market instead of growing it.
  * Farm hands cost fib(n): 10 hands = 143 coins for 240 extra actions/day.
    => Labour is nearly free. Hire to the action budget, not to the wallet.

Build order: carrots for opening cash -> coops+geese as fast as cash allows
-> buy NE land -> saturate with geese -> harvest/sell eggs every single day.
"""

CARROT_SEED = 20
GOOSE_COST = 300
SHED_TILES = [(4, 4), (5, 4), (4, 5), (5, 5)]
LAND_PRICES = [0, 1000, 2000, 4000]

# --- tunables -------------------------------------------------------------
MAX_HANDS = 12             # 376 coins/day for 288 actions - still trivial
GOOSE_TARGET = 36          # tile-bound in practice, not cash-bound late
LAST_GOOSE_BUY_DAY = 20    # 300 cost / ~80 per day => needs ~4 production days
LAST_CARROT_PLANT_DAY = 8  # carrots are opening cash only
CARROT_TILES = 6
FEED_DAYS_BUFFER = 2       # keep this many days of wheat on hand
CASH_FLOOR = 400           # must always be able to buy tomorrow's feed
SHED_CAP = 100


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


def _agent(obs):
    player = obs["player"]
    day = obs.get("day", 0)
    hour = obs.get("hour", 0)
    me = obs["farms"][player]
    priv = obs["private"]
    prices = obs["market"]["prices"]
    tiles = me["tiles"]
    money = me["money"]
    shed = dict(priv.get("shed", {}) or {})
    seeds = dict(priv.get("seeds", {}) or {})
    invs = [dict(i or {}) for i in priv.get("inventories", [{}])]

    units = [tuple(me["farmer"])] + [tuple(h) for h in me.get("hands", [])]
    n_units = len(units)
    while len(invs) < n_units:
        invs.append({})

    # ---- survey ----------------------------------------------------------
    plants, animals, empty_coops, weeds, empties = [], [], [], [], []
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
                elif t["kind"] == "COOP":
                    empty_coops.append((x, y))

    n_animals = len(animals)
    in_transit = shed.get("GOOSE", 0) + sum(i.get("GOOSE", 0) for i in invs)
    geese_pipeline = n_animals + in_transit

    # keep coops tight around the shed to minimise walking
    empties.sort(key=lambda p: min(_dist(p, s) for s in SHED_TILES))
    empty_coops.sort(key=lambda p: min(_dist(p, s) for s in SHED_TILES))

    wheat_all = shed.get("WHEAT", 0) + sum(i.get("WHEAT", 0) for i in invs)

    # ======================================================================
    # MARKET  (10 orders/turn max, processed in order)
    # ======================================================================
    orders = []

    # -- hour 0: labour. Cheap, so scale to the work actually available.
    if hour == 0 and day < 29:
        work = n_animals * 4 + len(plants) + len(empty_coops) * 2 + in_transit * 2
        target = min(MAX_HANDS, max(4, (work + 9) // 10))
        for _ in range(min(10, max(0, target - len(me.get("hands", []))))):
            orders.append(["HIRE"])

    # -- sell eggs every turn: shed cap is 100 and eggs are the whole economy
    if shed.get("EGG", 0) > 0 and len(orders) < 10:
        orders.append(["SELL", "EGG", shed["EGG"]])

    # -- feed supply: never let an animal starve (2 missed days = escape)
    if n_animals > 0 and len(orders) < 10:
        need = n_animals * (FEED_DAYS_BUFFER + 1) - wheat_all
        if need > 0:
            unit_cost = max(1, prices.get("WHEAT", 25))
            room = SHED_CAP - sum(shed.values())
            afford = int(max(0, money - CASH_FLOOR) // unit_cost)
            n = max(0, min(need, afford, room, 40))
            if n > 0:
                orders.append(["BUY_PRODUCT", "WHEAT", n])
                money -= n * unit_cost

    # -- geese: the compounding engine. Buy as many as cash allows.
    if day <= LAST_GOOSE_BUY_DAY and geese_pipeline < GOOSE_TARGET and len(orders) < 10:
        housing = len(empty_coops) + len(empties)
        budget = int(max(0, money - CASH_FLOOR) // GOOSE_COST)
        n = max(0, min(budget, housing - in_transit,
                       GOOSE_TARGET - geese_pipeline,
                       SHED_CAP - sum(shed.values()), 6))
        if n > 0:
            orders.append(["BUY_ANIMAL", "GOOSE", n])
            money -= n * GOOSE_COST

    # -- land: more tiles = more coops. Cheap next to 300/goose.
    n_quads = len(me.get("unlocked_quadrants", ["NW"]))
    if n_quads < 4 and day <= 22 and len(orders) < 10:
        price_land = LAND_PRICES[min(n_quads, 3)]
        if len(empties) <= 3 and money >= price_land + GOOSE_COST * 2:
            orders.append(["BUY_LAND"])
            money -= price_land

    # -- opening cash: a few carrot tiles, only while geese are ramping
    if day <= LAST_CARROT_PLANT_DAY and len(orders) < 10:
        n_carrot = sum(1 for *_, t in plants if t["crop"] == "CARROT")
        if (n_carrot + seeds.get("CARROT", 0) < CARROT_TILES
                and money >= CARROT_SEED * 3 + GOOSE_COST):
            orders.append(["BUY_SEED", "CARROT", 3])
            money -= CARROT_SEED * 3

    # -- dump everything else that accumulates
    for item in ("CARROT", "FERTILIZER", "WHEAT"):
        if len(orders) >= 10:
            break
        cnt = shed.get(item, 0)
        if item == "WHEAT":
            reserve = 0 if day >= 29 else n_animals * (FEED_DAYS_BUFFER + 1)
            cnt = max(0, cnt - reserve)
        elif item == "FERTILIZER" and day < 29:
            cnt = max(0, cnt - 2)
        if cnt > 0:
            orders.append(["SELL", item, cnt])

    orders = orders[:10]

    # ======================================================================
    # UNIT JOBS  (priority -> greedy nearest-unit assignment)
    # ======================================================================
    jobs = []  # (prio, x, y, op, required_item)

    # P0 FEED unfed animals - starvation is unrecoverable
    for x, y, t in animals:
        if not t.get("fed_today"):
            jobs.append((0, x, y, ["FEED"], "WHEAT"))
    # P1 HARVEST eggs - max_held caps at 4, so drain daily
    for x, y, t in animals:
        if t.get("yield_units", 0) > 0:
            jobs.append((1, x, y, ["HARVEST"], None))
    # P2 PLACE geese onto empty coops
    for (x, y) in empty_coops[:in_transit]:
        jobs.append((2, x, y, ["PLACE", "GOOSE"], "GOOSE"))
    # P3 CARE - doubles egg yield, worth ~$40/animal/day
    for x, y, t in animals:
        if not t.get("cared_today"):
            jobs.append((3, x, y, ["CARE"], None))
    # P4 BUILD_COOP ahead of demand so geese never wait on housing
    want_coops = max(in_transit, 3 if geese_pipeline < GOOSE_TARGET else 0)
    spare = list(empties)
    for _ in range(max(0, want_coops - len(empty_coops))):
        if spare:
            x, y = spare.pop(0)
            jobs.append((4, x, y, ["BUILD_COOP"], None))
    # P5 water crops
    for x, y, t in plants:
        if not t.get("watered_today"):
            jobs.append((5, x, y, ["WATER"], None))
    # P6 harvest ripe crops
    for x, y, t in plants:
        age = day - t["planted_day"]
        if t.get("yield_units", 0) > 0 and age >= 3:
            jobs.append((6, x, y, ["HARVEST"], None))
    # P7 plant carrots on leftover tiles (early only)
    if day <= LAST_CARROT_PLANT_DAY:
        c = seeds.get("CARROT", 0)
        for (x, y) in spare:
            if c <= 0:
                break
            jobs.append((7, x, y, ["PLANT", "CARROT"], None))
            c -= 1
    # P8 fertilizer is free money but lowest value
    for x, y, t in animals:
        if t.get("fertilizer_available"):
            jobs.append((8, x, y, ["COLLECT_FERTILIZER"], None))
    # P9 clear weeds to free tiles
    for (x, y) in weeds:
        jobs.append((9, x, y, ["DIG"], None))

    jobs.sort(key=lambda j: j[0])

    unit_ops = [None] * n_units

    # ---- stand-and-serve: never walk away from unfinished work underfoot ---
    # Walking dominated earlier versions (4x more move ops than useful ones),
    # which starved animals. A unit already on a tile services it for free.
    def _tile_at(p):
        x, y = p
        if 0 <= y < len(tiles) and 0 <= x < len(tiles[0]):
            return tiles[y][x]
        return None

    for ui in range(n_units):
        t = _tile_at(units[ui])
        if not isinstance(t, dict):
            continue
        if t.get("animal"):
            if not t.get("fed_today") and invs[ui].get("WHEAT", 0) > 0:
                unit_ops[ui] = ["FEED"]
                invs[ui]["WHEAT"] -= 1
            elif t.get("yield_units", 0) > 0:
                unit_ops[ui] = ["HARVEST"]
            elif not t.get("cared_today"):
                unit_ops[ui] = ["CARE"]
            elif t.get("fertilizer_available"):
                unit_ops[ui] = ["COLLECT_FERTILIZER"]
        elif t.get("kind") == "COOP" and not t.get("animal") and invs[ui].get("GOOSE", 0) > 0:
            unit_ops[ui] = ["PLACE", "GOOSE"]
            invs[ui]["GOOSE"] -= 1
        elif t.get("kind") == "PLANT":
            if not t.get("watered_today"):
                unit_ops[ui] = ["WATER"]
            elif t.get("yield_units", 0) > 0 and day - t["planted_day"] >= 3:
                unit_ops[ui] = ["HARVEST"]

    # ---- logistics: couriers fetch wheat / geese from the shed -----------
    # A courier must be EMPTY-HANDED for the item it is fetching, otherwise the
    # unit nearest the shed is re-picked forever and never delivers its load.
    def _send_courier(item, want_total, per_trip):
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
        else:
            mv = _step_toward(units[ui], _nearest_shed(units[ui]))
            unit_ops[ui] = [mv] if mv else ["PASS"]

    unfed = sum(1 for _, _, t in animals if not t.get("fed_today"))

    # Morning bulk loadout: hands spawn on shed tiles, so every unit standing
    # there grabs a wheat stack at once. Starvation (2 missed days = permanent
    # escape) was the single largest source of lost value in earlier versions.
    if unfed > 0 and shed.get("WHEAT", 0) > 0:
        share = max(2, -(-unfed // max(1, n_units)) + 1)
        for ui in range(n_units):
            if unit_ops[ui] is not None or invs[ui].get("WHEAT", 0) > 0:
                continue
            if tuple(units[ui]) in SHED_TILES and shed.get("WHEAT", 0) > 0:
                take = min(shed["WHEAT"], share, 10)
                unit_ops[ui] = ["PICKUP", "WHEAT", take]
                invs[ui]["WHEAT"] = invs[ui].get("WHEAT", 0) + take
                shed["WHEAT"] -= take
        # anyone still empty while animals go hungry walks to the shed
        if sum(i.get("WHEAT", 0) for i in invs) < unfed:
            for _ in range(2):
                _send_courier("WHEAT", unfed, 8)

    if empty_coops:
        for _ in range(2):
            _send_courier("GOOSE", min(shed.get("GOOSE", 0), len(empty_coops)), 3)

    # ---- end of day: bank carried produce before it is lost -------------
    for ui in range(n_units):
        if unit_ops[ui] is not None:
            continue
        load = sum(v for k, v in invs[ui].items() if k not in ("WHEAT", "GOOSE"))
        if load >= 12 or (hour >= 22 and load > 0):
            st = _nearest_shed(units[ui])
            if tuple(units[ui]) in SHED_TILES:
                unit_ops[ui] = ["DROP"]
            else:
                mv = _step_toward(units[ui], st)
                unit_ops[ui] = [mv] if mv else ["DROP"]

    # ---- greedy nearest assignment --------------------------------------
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
