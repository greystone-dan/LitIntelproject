"""Read-only check of search results and speed for a fixed query set.

Runs each query through the same function the site uses, with a timer, and saves the top-10 ids and the facet
counts to a JSON file. Run it before and after a search change and compare the two files with --compare.
Only SELECT statements run. It does not read keys.

    python scripts/search_speed_check.py --out before.json
    python scripts/search_speed_check.py --out after.json
    python scripts/search_speed_check.py --compare before.json after.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

QUERIES = [
    "Baker", "Doré", "Vavilov", "reasonableness", "pertinence de la décision", "2019 SCC 65",
    "Dunsmuir", "Khosa", "Suresh", "Ward", "Chieu", "Mugesera", "Baker v. Canada",
    "Canada (Minister of Citizenship and Immigration) v. Vavilov",
    "Minister of Citizenship and Immigration v. Khosa", "2009 SCC 12", "2008 SCC 9",
    "best interests of the child", "procedural fairness", "reasonable apprehension of bias", "Noël",
    "Canada", "Minister of Citizenship and Immigration", "Federal Court",
]


def run(out: Path) -> None:
    from backend.analytics_service import fetch_analytics_search_cases
    from backend.database import SessionLocal

    report = {}
    for query in QUERIES:
        timings = []
        for _ in range(2):
            db = SessionLocal()
            try:
                started = time.perf_counter()
                result = fetch_analytics_search_cases(db, query=query, limit=10)
                timings.append(round(time.perf_counter() - started, 2))
            finally:
                db.close()
        report[query] = {
            "top10": [row["case_id"] for row in result["results"]],
            "facets": result["facets"],
            "seconds_first_second_run": timings,
        }
        print(query, timings)
    out.write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")


def compare(before: Path, after: Path) -> int:
    old, new = (json.loads(path.read_text(encoding="utf-8")) for path in (before, after))
    moved = 0
    for query in old:
        same_ids = old[query]["top10"] == new[query]["top10"]
        same_set = set(old[query]["top10"]) == set(new[query]["top10"])
        same_facets = old[query]["facets"] == new[query]["facets"]
        moved += not (same_ids and same_facets)
        print(f"{query}: top10 {'same order' if same_ids else 'same set, order moved' if same_set else 'DIFFERENT'}; "
              f"facets {'identical' if same_facets else 'DIFFERENT'}; "
              f"seconds {old[query]['seconds_first_second_run']} -> {new[query]['seconds_first_second_run']}")
    return 1 if moved else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--compare", nargs=2, type=Path)
    args = parser.parse_args()
    if args.compare:
        raise SystemExit(compare(*args.compare))
    if not args.out:
        parser.error("give --out or --compare")
    run(args.out)
