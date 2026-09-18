"""Artifact validation before any game is played: SHA, last-callable check,
smoke game vs starter, then insert into the ledger and copy to lab/artifacts/<sha8>/main.py.
"""
import argparse
import hashlib
import io
import shutil
import sys
from contextlib import redirect_stdout
from pathlib import Path

from lab import ledger

LAB = Path(__file__).resolve().parent
ROOT = LAB.parent
ARTIFACTS_DIR = LAB / "artifacts"

# name -> (source path relative to project root, declared entry point, parent artifact name or None)
CANDIDATES = {
    "main": ("main.py", None, None),
    "main2": ("strat2/files/main2.py", None, None),
    "c92": ("lab/agents/c92.py", "kaggle_submission_agent", None),
    "c94": ("lab/agents/c94.py", "c94_submission_agent", "c92"),
    "c95": ("lab/agents/c95.py", "c94_submission_agent", "c94"),
}


def _quiet_import(fn, *a, **kw):
    """kaggle_environments spams OpenSpiel noise on import; swallow it."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        return fn(*a, **kw)


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def last_callable_name(path: Path) -> str:
    from kaggle_environments.agent import get_last_callable
    raw = path.read_text(encoding="utf-8")
    fn = get_last_callable(raw, path=str(path))
    return getattr(fn, "__name__", repr(fn))


def register(name: str, conn=None, path: str = None, entry: str = None, parent: str = None, notes: str = None) -> dict:
    """Register a known candidate by name, or any new file via path/entry/parent
    (how every future version -- yours or a Phase 2 export -- enters the ledger)."""
    if path:
        rel_path, declared_entry, parent_name = path, entry, parent
    else:
        rel_path, declared_entry, parent_name = CANDIDATES[name]
    src = Path(rel_path) if Path(rel_path).is_absolute() else ROOT / rel_path
    if not src.exists():
        raise SystemExit(f"{name}: source not found at {src}")

    raw = src.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    nbytes = len(raw)

    compile(raw, str(src), "exec")
    assert b"def agent" in raw, f"{name}: no 'def agent' found in source"

    actual_entry = last_callable_name(src)
    expected_entry = declared_entry or "agent"
    assert actual_entry == expected_entry, (
        f"{name}: last-callable trap! kaggle-environments would run "
        f"'{actual_entry}', not the declared entry point '{expected_entry}'"
    )

    # smoke game vs starter, full episode
    import kaggle_environments as ke
    env = _quiet_import(ke.make, "kaggriculture", configuration={"episodeSteps": 720, "seed": 1}, debug=False)
    _quiet_import(env.run, [str(src), "starter"])
    last = env.steps[-1]
    status_p0, reward_p0 = last[0].status, last[0].reward
    status_p1, reward_p1 = last[1].status, last[1].reward
    assert status_p0 == "DONE" and status_p1 == "DONE", (
        f"{name}: smoke game did not finish DONE/DONE (got {status_p0}/{status_p1})"
    )
    assert reward_p0 is not None and reward_p0 > 3000, (
        f"{name}: smoke game reward_p0={reward_p0} did not clear 3000 vs starter"
    )

    parent_sha = None
    if parent_name:
        prow = ledger.get_artifact_by_name(parent_name, conn=conn)
        if prow is None:
            raise SystemExit(f"{name}: parent '{parent_name}' is not registered")
        parent_sha = prow["sha256"]

    dest_dir = ARTIFACTS_DIR / sha[:8]
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "main.py"
    shutil.copy2(src, dest)

    ledger.add_artifact(
        sha256=sha, name=name, path=str(dest), nbytes=nbytes,
        entry_point=expected_entry, parent_sha=parent_sha,
        notes=(notes + " | " if notes else "") + f"smoke: reward_p0={reward_p0} vs starter, last_callable={actual_entry}",
        conn=conn,
    )
    print(f"{name}: OK sha256={sha[:12]}... entry={expected_entry} smoke_reward={reward_p0:.0f} -> {dest}")
    return {"name": name, "sha256": sha, "reward_p0": reward_p0}


def check_package(package: Path, entry: str = "agent", seed: int = 1) -> dict:
    """Unpack exactly what will be uploaded (main.py or a tar.gz) into a temp dir and play
    a smoke game from there. Catches files missing from the archive (Colosseum's 876)."""
    import tarfile, tempfile
    package = Path(package)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        if package.suffixes[-2:] == [".tar", ".gz"]:
            with tarfile.open(package, "r:gz") as tar:
                names = tar.getnames()
                tar.extractall(tmp, filter="data")
        else:
            names = [package.name]
            shutil.copy2(package, tmp / "main.py")
        main_py = tmp / "main.py"
        assert main_py.exists(), f"no main.py at archive root: {names}"
        actual = last_callable_name(main_py)
        assert actual == entry, f"last-callable is '{actual}', expected '{entry}'"
        import kaggle_environments as ke, os
        cwd = os.getcwd()
        os.chdir(tmp)  # an agent reading sibling files must find them next to main.py, not in the repo
        try:
            env = _quiet_import(ke.make, "kaggriculture", configuration={"episodeSteps": 720, "seed": seed}, debug=False)
            _quiet_import(env.run, [str(main_py), "starter"])
        finally:
            os.chdir(cwd)
        last = env.steps[-1]
        assert last[0].status == "DONE" and (last[0].reward or 0) > 3000, (
            f"packaged smoke failed: status={last[0].status} reward={last[0].reward}")
        print(f"package OK: {package.name} members={names} entry={actual} reward={last[0].reward:.0f}")
        return {"members": names, "entry": actual, "reward": last[0].reward}


def register_all():
    conn = ledger.connect()
    results = []
    # register in dependency order so parent_sha lookups succeed
    for name in ("main", "main2", "c92", "c94", "c95"):
        results.append(register(name, conn=conn))
    conn.close()
    return results


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--register-all", action="store_true")
    p.add_argument("--name", help="artifact name (a known candidate, or a new name with --path)")
    p.add_argument("--path", help="source file for a new artifact (absolute, or relative to kaggleagriculture/)")
    p.add_argument("--entry", help="expected last-callable name (default: agent)")
    p.add_argument("--parent", help="parent artifact name, enables the gate's veto-vs-parent")
    p.add_argument("--notes", help="what changed vs the parent")
    p.add_argument("--check-package", help="main.py or submission.tar.gz exactly as it will be uploaded")
    args = p.parse_args()
    if args.check_package:
        check_package(Path(args.check_package), entry=args.entry or "agent")
    elif args.register_all:
        register_all()
    elif args.name:
        register(args.name, conn=ledger.connect(), path=args.path, entry=args.entry,
                 parent=args.parent, notes=args.notes)
    else:
        p.error("pass --register-all or --name <candidate>")


if __name__ == "__main__":
    main()
