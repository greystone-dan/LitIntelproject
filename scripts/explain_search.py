"""Read-only EXPLAIN (ANALYZE, BUFFERS) of every case-search statement for one query.

Runs the site's own search function with a session wrapper that, for each statement that reads the cases table,
first runs it under EXPLAIN (ANALYZE, BUFFERS) and prints the plan with its total time. Only SELECT statements run
(EXPLAIN ANALYZE executes them but changes nothing). It does not read keys.

    python scripts/explain_search.py --query reasonableness --out explain_reasonableness.txt
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


class ExplainingSession:
    def __init__(self, db, lines):
        self._db, self._lines = db, lines

    def __getattr__(self, name):
        return getattr(self._db, name)

    def execute(self, statement, params=None, *args, **kwargs):
        from sqlalchemy import text as sql_text

        sql = str(statement)
        if sql.lstrip().upper().startswith(("SELECT", "(SELECT", "WITH")) and "FROM cases" in sql:
            try:
                plan_statement = sql_text("EXPLAIN (ANALYZE, BUFFERS) " + sql)
                # Keep expanding bind parameters (IN :ids) working.
                for key, bind in getattr(statement, "_bindparams", {}).items():
                    if getattr(bind, "expanding", False):
                        plan_statement = plan_statement.bindparams(bind)
                started = time.perf_counter()
                rows = self._db.execute(plan_statement, params or {}).all()
                self._lines.append(f"\n=== {time.perf_counter() - started:.2f} s ===\n{' '.join(sql.split())[:600]}")
                self._lines.extend(str(row[0]) for row in rows)
            except Exception as error:  # a statement that cannot be explained still runs below
                self._db.rollback()
                self._lines.append(f"\n=== could not EXPLAIN: {str(error)[:200]} ===\n{' '.join(sql.split())[:300]}")
        return self._db.execute(statement, params, *args, **kwargs)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--query", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    from backend.analytics_service import fetch_analytics_search_cases
    from backend.database import SessionLocal

    lines: list[str] = []
    db = SessionLocal()
    try:
        started = time.perf_counter()
        fetch_analytics_search_cases(ExplainingSession(db, lines), query=args.query, limit=10)
        lines.insert(0, f"query={args.query!r} total with EXPLAIN overhead {time.perf_counter() - started:.1f} s")
    finally:
        db.close()
    args.out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
