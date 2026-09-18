"""SQLite run ledger: artifacts, games, batches. WAL mode so parallel game
workers writing through a single parent-process connection never lock."""
import json
import sqlite3
import time
from pathlib import Path

LAB = Path(__file__).resolve().parent
DB_PATH = LAB / "runs.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS artifacts (
    sha256 TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    path TEXT NOT NULL,
    bytes INTEGER NOT NULL,
    entry_point TEXT NOT NULL,
    parent_sha TEXT,
    created_at REAL NOT NULL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS batches (
    batch_id TEXT PRIMARY KEY,
    label TEXT,
    seed_block TEXT,
    created_at REAL NOT NULL,
    config_json TEXT,
    git_note TEXT
);

CREATE TABLE IF NOT EXISTS games (
    game_id TEXT PRIMARY KEY,
    batch_id TEXT NOT NULL,
    sha_p0 TEXT NOT NULL,
    sha_p1 TEXT NOT NULL,
    seed INTEGER NOT NULL,
    steps INTEGER,
    reward_p0 REAL,
    reward_p1 REAL,
    status_p0 TEXT,
    status_p1 TEXT,
    result TEXT,
    margin REAL,
    wall_ms REAL,
    replay_path TEXT
);
CREATE INDEX IF NOT EXISTS idx_games_batch ON games(batch_id);
CREATE INDEX IF NOT EXISTS idx_games_pair ON games(sha_p0, sha_p1);
"""


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript(SCHEMA)
    return conn


def add_artifact(sha256, name, path, nbytes, entry_point, parent_sha=None, notes=None, conn=None):
    own = conn is None
    conn = conn or connect()
    conn.execute(
        "INSERT OR REPLACE INTO artifacts (sha256,name,path,bytes,entry_point,parent_sha,created_at,notes) "
        "VALUES (?,?,?,?,?,?,?,?)",
        (sha256, name, str(path), nbytes, entry_point, parent_sha, time.time(), notes),
    )
    conn.commit()
    if own:
        conn.close()


def add_batch(batch_id, label, seed_block, config: dict, git_note=None, conn=None):
    own = conn is None
    conn = conn or connect()
    conn.execute(
        "INSERT INTO batches (batch_id,label,seed_block,created_at,config_json,git_note) "
        "VALUES (?,?,?,?,?,?)",
        (batch_id, label, seed_block, time.time(), json.dumps(config), git_note),
    )
    conn.commit()
    if own:
        conn.close()


def add_game(row: dict, conn=None):
    own = conn is None
    conn = conn or connect()
    cols = ("game_id", "batch_id", "sha_p0", "sha_p1", "seed", "steps", "reward_p0", "reward_p1",
            "status_p0", "status_p1", "result", "margin", "wall_ms", "replay_path")
    conn.execute(
        f"INSERT INTO games ({','.join(cols)}) VALUES ({','.join('?' * len(cols))})",
        tuple(row.get(c) for c in cols),
    )
    conn.commit()
    if own:
        conn.close()


def get_artifact_by_name(name, conn=None):
    own = conn is None
    conn = conn or connect()
    row = conn.execute("SELECT * FROM artifacts WHERE name=? ORDER BY created_at DESC LIMIT 1", (name,)).fetchone()
    if own:
        conn.close()
    return row


def games_for_batch(batch_id, conn=None):
    own = conn is None
    conn = conn or connect()
    rows = conn.execute("SELECT * FROM games WHERE batch_id=?", (batch_id,)).fetchall()
    if own:
        conn.close()
    return rows
