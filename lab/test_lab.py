"""One small runnable self-check: BT fit orders a dominant synthetic player first;
ledger round-trip; veto fires on a synthetic loss. No framework, just asserts."""
import tempfile
from pathlib import Path

from lab import ledger, rate, gate


def test_bt_orders_dominant_player_first():
    players = ["A", "B", "C"]
    # Sparse dict, the way compute_batch_ratings builds it: no (loser, winner) keys when the
    # loser never won. The first BT version gave a zero-win player no gradient at all.
    wins = {("A", "B"): 8, ("A", "C"): 8, ("B", "C"): 6, ("C", "B"): 2}
    ratings = rate.bradley_terry_fit(players, wins)
    ordered = sorted(players, key=lambda p: -ratings[p])
    assert ordered == ["A", "B", "C"], f"expected A>B>C, got {ordered} ({ratings})"
    assert all(abs(v) < 20 for v in ratings.values()), f"perfect separation diverged: {ratings}"
    assert ratings["C"] < ratings["B"] - 0.5, f"zero-win-vs-A player not pushed down: {ratings}"
    print("test_bt_orders_dominant_player_first: OK", ratings)


def test_ledger_round_trip():
    import os
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.unlink(path)  # ledger.connect creates it fresh
    orig_db = ledger.DB_PATH
    ledger.DB_PATH = Path(path)
    try:
        conn = ledger.connect()
        ledger.add_artifact("deadbeef" * 8, "test_artifact", "some/path.py", 123, "agent", conn=conn)
        ledger.add_batch("batch1", "test batch", "1-1", {"x": 1}, conn=conn)
        ledger.add_game({
            "game_id": "g1", "batch_id": "batch1", "sha_p0": "a", "sha_p1": "b", "seed": 1, "steps": 720,
            "reward_p0": 100.0, "reward_p1": 50.0, "status_p0": "DONE", "status_p1": "DONE",
            "result": "W", "margin": 50.0, "wall_ms": 12.0, "replay_path": "some/replay.json",
        }, conn=conn)
        row = ledger.get_artifact_by_name("test_artifact", conn=conn)
        assert row["sha256"] == "deadbeef" * 8
        games = ledger.games_for_batch("batch1", conn=conn)
        assert len(games) == 1 and games[0]["result"] == "W"
        conn.close()
        print("test_ledger_round_trip: OK")
    finally:
        ledger.DB_PATH = orig_db
        Path(path).unlink(missing_ok=True)
        for ext in ("-wal", "-shm"):
            Path(str(path) + ext).unlink(missing_ok=True)


def test_veto_and_scoring():
    from lab import arena
    # candidate "c" loses once from seat 1 (opponent as p0 won) among wins: gate must see exactly that loss
    results = [{"path_p0": "c", "path_p1": "o", "result": "W"},
               {"path_p0": "o", "path_p1": "c", "result": "W"},
               {"path_p0": "o", "path_p1": "c", "result": "L"}]
    assert len(gate.candidate_losses(results, "c")) == 1
    # an agent that errors loses even with a higher reward; both erroring is a tie
    assert arena.score("ERROR", "DONE", 9e9, 1.0)[0] == "L"
    assert arena.score("DONE", "DONE", 5.0, 7.0) == ("L", -2.0)
    assert arena.score("ERROR", "ERROR", None, None)[0] == "T"
    print("test_veto_and_scoring: OK")


if __name__ == "__main__":
    test_bt_orders_dominant_player_first()
    test_ledger_round_trip()
    test_veto_and_scoring()
    print("ALL PASS")
