"""Add new paragraph chunks to the paragraph_search table (catch-up after imports; additive).

Dry run by default: prints how many paragraphs are waiting. Use --apply to add them, --prune to also drop
index rows whose chunk was deleted by re-chunking. Run after RAD/RLLR imports or any bulk chunking; the daily
intake does the same step automatically. Undo for one run: none needed (rows are derived from case_chunks);
to remove everything: DROP TABLE paragraph_search.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import SessionLocal  # noqa: E402
from backend.paragraph_search_sync import sync_paragraph_search  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="write rows (default is a dry run)")
    parser.add_argument("--prune", action="store_true", help="with --apply, delete rows whose chunk no longer exists")
    parser.add_argument("--max-rows", type=int, help="stop after adding this many rows")
    args = parser.parse_args()
    with SessionLocal() as db:
        report = sync_paragraph_search(db, apply=args.apply, prune=args.prune, max_rows=args.max_rows)
    print(json.dumps(report, indent=2))
    if not report["table_exists"]:
        print("paragraph_search does not exist; build it first with semantic-search/paragraph_index.sql")
        return 1
    if not args.apply:
        print("Dry run only; add --apply to write.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
