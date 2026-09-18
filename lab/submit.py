"""Kaggle submission ledger: record submissions, sync their status/score from
the Kaggle CLI, and fetch episode info. Stdlib only. New file -- does not
touch ledger.py or any other lab/*.py (a tournament may have them imported).

    python -m lab.submit record --submission-id 123 --message "lab:main sha:551da854"
    python -m lab.submit sync
    python -m lab.submit episodes --submission-id 123
"""
import argparse
import csv
import io
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

LAB = Path(__file__).resolve().parent
DB_PATH = LAB / "runs.db"
COMPETITION = "kaggriculture"
KAGGLE_JSON = Path(r"C:\Zeel Australia\kaggle_things\kaggle.json")

SCHEMA = """
CREATE TABLE IF NOT EXISTS submissions (
    submission_id TEXT PRIMARY KEY,
    sha256 TEXT,
    artifact_name TEXT,
    message TEXT,
    submitted_at REAL,
    status TEXT,
    public_score REAL,
    last_checked REAL,
    notes TEXT
);
"""

SHA_MSG_RE = re.compile(r"lab:(?P<name>\S+)\s+sha:(?P<sha8>[0-9a-f]{8})")


def _connect():
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA journal_mode=WAL")
    con.executescript(SCHEMA)
    return con


def _kaggle_env():
    # ponytail: reads the token fresh each call instead of caching a module
    # global -- a few extra ms per invocation, never prints the token.
    env = os.environ.copy()
    if KAGGLE_JSON.exists():
        key = json.loads(KAGGLE_JSON.read_text())["key"]
        env["KAGGLE_API_TOKEN"] = key
    return env


def _run_kaggle(args):
    result = subprocess.run(
        ["kaggle", *args], env=_kaggle_env(), cwd=LAB.parent,
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"kaggle {' '.join(args)} failed: {result.stderr}")
    return result.stdout


def _artifact_sha_by_name_prefix(con, name, sha8):
    """Best-effort lookup of the full sha256 for an artifact referenced by a
    submission message like 'lab:main sha:551da854'."""
    row = con.execute(
        "SELECT sha256 FROM artifacts WHERE name = ? AND sha256 LIKE ?",
        (name, sha8 + "%"),
    ).fetchone()
    return row[0] if row else None


def cmd_record(args):
    con = _connect()
    name, sha256 = None, args.sha256
    m = SHA_MSG_RE.search(args.message or "")
    if m:
        name = m.group("name")
        if not sha256:
            sha256 = _artifact_sha_by_name_prefix(con, name, m.group("sha8"))
    con.execute(
        """INSERT INTO submissions
           (submission_id, sha256, artifact_name, message, submitted_at, status, public_score, last_checked, notes)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(submission_id) DO UPDATE SET
             sha256=excluded.sha256, artifact_name=excluded.artifact_name,
             message=excluded.message, submitted_at=excluded.submitted_at,
             status=excluded.status, notes=excluded.notes""",
        (args.submission_id, sha256, args.artifact_name or name, args.message,
         args.submitted_at or time.time(), args.status or "PENDING", None,
         None, args.notes),
    )
    con.commit()
    print(f"recorded submission {args.submission_id} (sha256={sha256}, artifact={name})")


def _csv_lines(text):
    # kaggle CLI 2.2.1 prepends an "outdated version" Warning line (and blank
    # lines between data rows) before the real CSV -- strip both.
    return [ln for ln in text.splitlines() if ln.strip() and not ln.startswith("Warning:")]


def _parse_submissions_csv(text):
    # header: ref,fileName,date,description,status,publicScore,privateScore
    return list(csv.DictReader(_csv_lines(text)))


def cmd_sync(args):
    con = _connect()
    out = _run_kaggle(["competitions", "submissions", COMPETITION, "-v"])
    rows = _parse_submissions_csv(out)
    now = time.time()
    updated = 0
    for row in rows:
        sub_id = row.get("ref", "").strip()
        if not sub_id:
            continue
        existing = con.execute(
            "SELECT sha256, message FROM submissions WHERE submission_id = ?",
            (sub_id,),
        ).fetchone()
        if existing is None:
            continue  # only track submissions we explicitly recorded
        sha256 = existing[0]
        if not sha256:
            m = SHA_MSG_RE.search(row.get("description", "") or "")
            if m:
                sha256 = _artifact_sha_by_name_prefix(con, m.group("name"), m.group("sha8"))
        status = row.get("status", "") or None
        score_raw = (row.get("publicScore") or "").strip()
        public_score = float(score_raw) if score_raw else None
        con.execute(
            """UPDATE submissions SET status=?, public_score=?, last_checked=?, sha256=?
               WHERE submission_id=?""",
            (status, public_score, now, sha256, sub_id),
        )
        updated += 1
    con.commit()
    print(f"synced {updated} tracked submission(s) from {len(rows)} row(s) on the ladder")
    for r in con.execute("SELECT submission_id, status, public_score, sha256 FROM submissions"):
        print(f"  {r[0]}  status={r[1]}  public_score={r[2]}  sha256={r[3]}")


def cmd_episodes(args):
    out = _run_kaggle(["competitions", "episodes", args.submission_id, "-v"])
    print(out)
    lines = _csv_lines(out)
    return list(csv.DictReader(lines)) if lines else []


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    p_record = sub.add_parser("record", help="insert/update a submission row")
    p_record.add_argument("--submission-id", required=True)
    p_record.add_argument("--message", default="")
    p_record.add_argument("--sha256")
    p_record.add_argument("--artifact-name")
    p_record.add_argument("--status", default="PENDING")
    p_record.add_argument("--submitted-at", type=float)
    p_record.add_argument("--notes")
    p_record.set_defaults(func=cmd_record)

    p_sync = sub.add_parser("sync", help="refresh status/score for tracked submissions")
    p_sync.set_defaults(func=cmd_sync)

    p_ep = sub.add_parser("episodes", help="fetch episodes for a submission")
    p_ep.add_argument("--submission-id", required=True)
    p_ep.set_defaults(func=cmd_episodes)

    args = p.parse_args(argv)
    args.func(args)  # subcommands print what matters; not used as an exit code
    return 0


if __name__ == "__main__":
    sys.exit(main())
