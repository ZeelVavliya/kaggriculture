"""Unpack the three embedded agent main.py blobs from the pulled kernel notebook.

Each candidate code cell holds `zlib.decompress(base64.b64decode("..."))` producing a
full agent main.py. We find every base64 literal in b64decode(...) calls, decode+inflate,
and match by SHA-256 against the known-good digests from the plan.
"""
import argparse
import base64
import json
import re
import sys
import zlib
from pathlib import Path

LAB = Path(__file__).resolve().parent
ROOT = LAB.parent
KERNEL_NB = ROOT / "kernel" / "kaggriculture-findings-from-zero-to-top-meta.ipynb"

# name -> (expected sha256 hex, expected byte length, entry point)
EXPECTED = {
    "c92": ("7b13e69371509fe53f1dbb7b769d73f6c82ff41db37df7a9a3a1879e82ed82f2", 70317, "kaggle_submission_agent"),
    "c94": ("7b0e5a7b9d18dc583f5789e50a54dca43561f6d08c1c616b4219bf50bcb8311f", 75078, "c94_submission_agent"),
    "c95": ("489f5d197527f107027626cce79d850fd2ca90edd43d94384b849b6511e27bdb", 75098, "c94_submission_agent"),
}

# Each candidate cell defines a list of adjacent base64-charset string literals
# (`_AGENT_B64_PARTS = [...]`) that are joined and fed to b64decode. Locate that
# list's `[...]` block specifically (literal length varies, last chunk can be
# short) and pull every quoted literal inside it, in order.
PARTS_BLOCK_RE = re.compile(r'_AGENT_B64_PARTS\s*=\s*\[(.*?)\]', re.DOTALL)
LITERAL_RE = re.compile(r'"([A-Za-z0-9+/=]+)"')


def _candidates_from_notebook(nb_path: Path):
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    out = []
    for i, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell["source"])
        if "b64decode" not in src:
            continue
        block_m = PARTS_BLOCK_RE.search(src)
        target = block_m.group(1) if block_m else src
        parts = LITERAL_RE.findall(target)
        if not parts:
            continue
        out.append((i, "".join(parts)))
    return out


def _decode(b64: str) -> bytes:
    return zlib.decompress(base64.b64decode(b64))


def extract():
    if not KERNEL_NB.exists():
        raise SystemExit(f"kernel notebook not found at {KERNEL_NB}; run step 1.1 kaggle kernels pull first")
    candidates = _candidates_from_notebook(KERNEL_NB)
    print(f"found {len(candidates)} b64decode(...) candidates across notebook cells")

    by_sha = {}
    for cell_idx, b64 in candidates:
        try:
            raw = _decode(b64)
        except Exception:
            continue
        import hashlib
        sha = hashlib.sha256(raw).hexdigest()
        by_sha[sha] = (cell_idx, raw)

    results = {}
    for name, (exp_sha, exp_len, entry) in EXPECTED.items():
        if exp_sha not in by_sha:
            raise SystemExit(f"HARD FAILURE: no candidate blob matched expected SHA-256 for {name} ({exp_sha})")
        cell_idx, raw = by_sha[exp_sha]
        assert len(raw) == exp_len, f"{name}: length mismatch {len(raw)} != {exp_len}"
        out_path = LAB / "agents" / f"{name}.py"
        out_path.write_bytes(raw)
        compile(raw, str(out_path), "exec")  # must be valid python
        assert b"def agent" in raw or entry.encode() in raw
        print(f"{name}: OK sha256={exp_sha[:12]}... bytes={len(raw)} cell={cell_idx} -> {out_path}")
        results[name] = {"sha256": exp_sha, "bytes": len(raw), "entry_point": entry, "path": str(out_path)}

    # Extract C95's _TRACE / _SUPPLY by importing the decoded module in isolation.
    _dump_c95_trace()
    return results


def _dump_c95_trace():
    import importlib.util
    c95_path = LAB / "agents" / "c95.py"
    spec = importlib.util.spec_from_file_location("c95_isolated", c95_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    trace = getattr(mod, "_TRACE", None)
    supply = getattr(mod, "_SUPPLY", None)
    if trace is None or supply is None:
        print(f"WARNING: c95 module missing _TRACE ({trace is None}) or _SUPPLY ({supply is None})")
        return
    (LAB / "agents" / "c95_trace.json").write_text(json.dumps(trace), encoding="utf-8")
    (LAB / "agents" / "c95_supply.json").write_text(json.dumps(supply), encoding="utf-8")
    print(f"c95: dumped _TRACE ({len(trace)} steps) -> lab/agents/c95_trace.json")
    print(f"c95: dumped _SUPPLY ({len(supply)} entries) -> lab/agents/c95_supply.json")


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    extract()
