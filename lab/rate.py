"""Bradley-Terry MLE over pairwise W/L (ties = half-wins) plus per-opponent
W-L-T and mean margin. select() ranks by win-based BT rating only -- margin
is reported, never used for ranking (the kernel's central lesson: BT and
margin diverge, e.g. C70 went 83-5 with +14196 mean margin and still stalled)."""
import argparse
import numpy as np

from lab import ledger

MAX_ITER = 2000
LR = 0.1


def bradley_terry_fit(players, wins: dict, l2: float = 0.01) -> dict:
    """players: list of ids. wins[(i,j)] = wins of i over j (ties already split as 0.5 each way).
    Returns {player: log-strength}, mean pinned to 0. Gradient ascent on the BT log-likelihood
    over every *unordered* pair (so a player with zero wins still gets pushed down), plus a
    small L2 prior so perfectly separated records (e.g. 40-0) stay finite."""
    n = len(players)
    idx = {p: k for k, p in enumerate(players)}
    pairs = {}
    for (i, j), w in wins.items():
        if i != j:
            a, b = sorted((idx[i], idx[j]))
            pairs.setdefault((a, b), [0.0, 0.0])[0 if idx[i] == a else 1] += w
    theta = np.zeros(n)
    for _ in range(MAX_ITER):
        grad = -l2 * theta
        for (a, b), (w_ab, w_ba) in pairs.items():
            p_ab = 1.0 / (1.0 + np.exp(theta[b] - theta[a]))
            g = w_ab - (w_ab + w_ba) * p_ab
            grad[a] += g
            grad[b] -= g
        theta += LR * grad / max(1, n)
        theta -= theta.mean()
    return {p: float(theta[idx[p]]) for p in players}


def wilson_ci(wins: float, games: int, z: float = 1.96):
    """95% Wilson interval for a win rate; ties count as half a win."""
    if games == 0:
        return (0.0, 0.0)
    ph = wins / games
    d = 1 + z * z / games
    c = (ph + z * z / (2 * games)) / d
    m = z * np.sqrt(ph * (1 - ph) / games + z * z / (4 * games * games)) / d
    return (max(0.0, c - m), min(1.0, c + m))


def elo(theta: float) -> float:
    """Log-strength on the kernel's familiar Elo-like scale (1500 = mean)."""
    return 1500.0 + 400.0 / np.log(10.0) * theta


def per_opponent_record(conn, sha: str, batch_id: str = None):
    if batch_id is not None:
        rows = conn.execute(
            "SELECT sha_p0,sha_p1,result,margin FROM games WHERE (sha_p0=? OR sha_p1=?) AND batch_id=? AND status_p0!='HARNESS_ERROR'",
            (sha, sha, batch_id),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT sha_p0,sha_p1,result,margin FROM games WHERE sha_p0=? OR sha_p1=?", (sha, sha)
        ).fetchall()
    rec = {}
    for r in rows:
        if r["sha_p0"] == sha:
            opp, result, margin = r["sha_p1"], r["result"], r["margin"]
        else:
            opp = r["sha_p0"]
            result = {"W": "L", "L": "W", "T": "T"}[r["result"]]
            margin = -r["margin"]
        d = rec.setdefault(opp, {"W": 0, "L": 0, "T": 0, "margins": []})
        d[result] += 1
        d["margins"].append(margin)
    return rec


def compute_batch_ratings(batch_id: str, conn=None):
    own = conn is None
    conn = conn or ledger.connect()
    games = conn.execute("SELECT sha_p0,sha_p1,result FROM games WHERE batch_id=? AND status_p0!='HARNESS_ERROR'", (batch_id,)).fetchall()
    players = sorted({g["sha_p0"] for g in games} | {g["sha_p1"] for g in games})
    wins = {}
    for g in games:
        p0, p1, result = g["sha_p0"], g["sha_p1"], g["result"]
        if p0 == p1:
            continue
        if result == "W":
            wins[(p0, p1)] = wins.get((p0, p1), 0) + 1
        elif result == "L":
            wins[(p1, p0)] = wins.get((p1, p0), 0) + 1
        else:
            wins[(p0, p1)] = wins.get((p0, p1), 0) + 0.5
            wins[(p1, p0)] = wins.get((p1, p0), 0) + 0.5
    ratings = bradley_terry_fit(players, wins) if len(players) > 1 else {p: 0.0 for p in players}

    name_by_sha = {}
    for sha in players:
        row = conn.execute("SELECT name FROM artifacts WHERE sha256=?", (sha,)).fetchone()
        name_by_sha[sha] = row["name"] if row else sha[:8]

    table = []
    for sha in sorted(players, key=lambda p: -ratings[p]):
        rec = per_opponent_record(conn, sha, batch_id=batch_id)
        w = sum(v["W"] for v in rec.values())
        l = sum(v["L"] for v in rec.values())
        t = sum(v["T"] for v in rec.values())
        margins = [m for v in rec.values() for m in v["margins"]]
        mean_margin = sum(margins) / len(margins) if margins else 0.0
        table.append({
            "sha": sha, "name": name_by_sha[sha], "bt_rating": ratings[sha],
            "W": w, "L": l, "T": t, "mean_margin": mean_margin,
            "per_opponent": {name_by_sha.get(o, o[:8]): v for o, v in rec.items()},
        })
    if own:
        conn.close()
    return table


def select(table):
    """Return the top artifact by BT rating. Refuses to be called with a margin sort."""
    return max(table, key=lambda r: r["bt_rating"])


def print_table(table):
    print(f"{'name':<10} {'BT':>8} {'elo':>6} {'W':>4} {'L':>4} {'T':>4} {'mean_margin':>12}")
    for r in table:
        print(f"{r['name']:<10} {r['bt_rating']:>8.3f} {elo(r['bt_rating']):>6.0f} {r['W']:>4} {r['L']:>4} {r['T']:>4} {r['mean_margin']:>12.1f}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--batch", required=True)
    args = p.parse_args()
    table = compute_batch_ratings(args.batch)
    print_table(table)
    best = select(table)
    print(f"\nselected by win-based BT rating: {best['name']} ({best['sha'][:8]})")


if __name__ == "__main__":
    main()
