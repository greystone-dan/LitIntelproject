"""Build the paragraph-level "cited by" tables from stored citation occurrences.

For every case that cites another library case by paragraph, store which paragraph it cites, how often,
and the signal phrase written next to the citation ("see also", "followed in", "distinguished", ...).
The reader's Markup view reads these rows.

Safe by default: with no flags it only reports what it would do. Nothing is written without --apply.
No AI. It is built so it cannot slow the live site down (lowest process priority, one database
connection, short time limits, rests between small batches, optional site health check, stop file).

  python scripts/build_paragraph_cited_by.py                                  # plan only
  python scripts/build_paragraph_cited_by.py --apply --max-minutes 30 --health-url http://127.0.0.1:8001/health/ready
  python scripts/build_paragraph_cited_by.py --report-cited 1292             # show what is stored for a case

Resumable: a citing case counts as done once its status row is written, so stopping (Ctrl+C, the stop file,
--max-minutes) and running the same command again carries on. To redo everything after changing the
classifier, raise ALGO_VERSION in backend/paragraph_cited_by.py. Read docs/PARAGRAPH_CITED_BY.md before running.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.paragraph_cited_by_runner import main, parse_args  # noqa: E402,F401

if __name__ == "__main__":
    raise SystemExit(main())
