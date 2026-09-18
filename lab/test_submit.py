"""Smoke test for lab/submit.py parsing logic. Run: python -m lab.test_submit
No local file edits, no kaggle CLI calls, no local games -- safe to run
alongside the running tournament."""
from lab.submit import SHA_MSG_RE, _parse_submissions_csv

CSV_SAMPLE = (
    "Warning: Looks like you're using an outdated `kaggle` version, please upgrade\n"
    "ref,fileName,date,description,status,publicScore,privateScore\n"
    "\n"
    "56235192,main.py,2026-09-14 16:18:41.303000,lab:main sha:551da854,SubmissionStatus.PENDING,,\n"
    "\n"
    "55648629,main2.py,2026-08-20 14:48:59.537000,,SubmissionStatus.COMPLETE,489.9,\n"
)


def demo():
    rows = _parse_submissions_csv(CSV_SAMPLE)
    assert len(rows) == 2
    assert rows[0]["ref"] == "56235192"
    assert rows[0]["status"] == "SubmissionStatus.PENDING"
    assert rows[1]["publicScore"] == "489.9"

    m = SHA_MSG_RE.search("lab:main sha:551da854")
    assert m and m.group("name") == "main" and m.group("sha8") == "551da854"
    assert SHA_MSG_RE.search("first trial") is None
    print("ok")


if __name__ == "__main__":
    demo()
