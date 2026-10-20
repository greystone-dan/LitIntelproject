"""Read-only check for migration 0051 (covering index on case_tags): sizes, build estimate and the tag lookup plan.

Run it BEFORE the migration (to size it and record the plan) and AFTER (to prove the index is used and valid).
Only SELECT / EXPLAIN statements run. It does not read keys.

    python scripts/tag_index_check.py --out tag_index_before.txt
    python scripts/tag_index_check.py --out tag_index_after.txt
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

VALUES = ["reasonableness", "procedural_fairness", "duty_of_fairness"]
INDEX = "ix_case_tags_value_version_covering"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    from sqlalchemy import text as sql_text

    from backend.analytics_service import ACTIVE_TAG_TAXONOMY_VERSION
    from backend.database import SessionLocal

    lines: list[str] = []
    db = SessionLocal()
    try:
        def one(sql, **params):
            return db.execute(sql_text(sql), params).scalar()

        rows = one("SELECT count(*) FROM case_tags")
        lines.append(f"case_tags rows: {rows}")
        table_size = one("SELECT pg_size_pretty(pg_table_size('case_tags'))")
        lines.append(f"case_tags table size: {table_size}")
        for name, size in db.execute(sql_text(
            "SELECT indexrelname, pg_size_pretty(pg_relation_size(indexrelid)) FROM pg_stat_user_indexes "
            "WHERE relname = 'case_tags' ORDER BY pg_relation_size(indexrelid) DESC"
        )).all():
            lines.append(f"existing index {name}: {size}")
        valid = db.execute(sql_text(
            "SELECT i.indisvalid, i.indisready, pg_size_pretty(pg_relation_size(i.indexrelid)) FROM pg_index i "
            "JOIN pg_class c ON c.oid = i.indexrelid WHERE c.relname = :n"
        ), {"n": INDEX}).all()
        lines.append(f"{INDEX}: {valid if valid else 'not built yet'}")
        lines.append("free disk is not visible from SQL; build needs about the index size plus a sort copy of it")
        for value in VALUES:
            for attempt in (1, 2):
                started = time.perf_counter()
                plan = db.execute(sql_text(
                    "EXPLAIN (ANALYZE, BUFFERS) SELECT tq.case_id FROM case_tags tq "
                    "WHERE tq.taxonomy_version = :version AND tq.value IN (:value)"
                ), {"version": ACTIVE_TAG_TAXONOMY_VERSION, "value": value}).all()
                lines.append(f"\n=== tag lookup {value!r}, run {attempt}, {time.perf_counter() - started:.2f} s ===")
                lines.extend(str(row[0]) for row in plan)
    finally:
        db.close()
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:8]))


if __name__ == "__main__":
    main()
