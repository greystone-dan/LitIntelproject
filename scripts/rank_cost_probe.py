"""Read-only timing probe: which part of the relevance ranking costs the time?

Takes the cases tagged with a topic (the biggest part of a broad topic search), then times each ranking building
block on exactly those rows, one SELECT each. Only SELECT statements run. It does not read keys.

    python scripts/rank_cost_probe.py --query reasonableness --out probe_reasonableness.txt
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STYLE = "c.metadata_json->'reader_extracted'->>'style of cause'"
BETWEEN = "c.metadata_json->'reader_extracted'->>'between'"
NORMALIZE = "TRIM(REGEXP_REPLACE(LOWER(COALESCE({e}, '')), '[^[:alnum:]]+', ' ', 'g'))"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--query", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    from sqlalchemy import text as sql_text

    from backend.analytics_service import ACTIVE_TAG_TAXONOMY_VERSION, _topic_tag_values
    from backend.database import SessionLocal
    from backend.search_matching import identity_sql

    citation, party, params = identity_sql(args.query)
    guard = f"LOWER(COALESCE(c.title, '')) LIKE :match_guard OR LOWER(COALESCE({STYLE}, '')) LIKE :match_guard OR LOWER(COALESCE({BETWEEN}, '')) LIKE :match_guard"
    params.setdefault("match_guard", f"%{max(args.query.lower().split(), key=len)}%")
    probes = [
        ("rows only (count)", "count(*)"),
        ("stored size of metadata_json, average bytes", "avg(pg_column_size(c.metadata_json))"),
        ("1 read of style of cause (one jsonb read)", f"count({STYLE})"),
        ("5 reads (3 style + 2 between, as the ranking does)", f"count({STYLE}) + count({STYLE}) + count({STYLE}) + count({BETWEEN}) + count({BETWEEN})"),
        ("normalize the title only (regexp_replace)", f"count({NORMALIZE.format(e='c.title')})"),
        ("normalize title + style + between", f"count({NORMALIZE.format(e='c.title')}) + count({NORMALIZE.format(e=STYLE)}) + count({NORMALIZE.format(e=BETWEEN)})"),
        ("cheap guard only (3 LIKEs)", f"sum(CASE WHEN {guard} THEN 1 ELSE 0 END)"),
        ("citation tier only", f"sum(CASE WHEN {citation} THEN 1 ELSE 0 END)"),
        ("party tier only (today's expression)", f"sum(CASE WHEN {party} THEN 1 ELSE 0 END)"),
        ("whole identity order key (today)", f"sum(CASE WHEN {citation} THEN 2 WHEN {party} THEN 1 ELSE 0 END)"),
        ("guard first, then party (PR 607 shape)", f"sum(CASE WHEN ({guard}) AND {party} THEN 1 ELSE 0 END)"),
    ]
    lines = []
    db = SessionLocal()
    try:
        values = _topic_tag_values(args.query)
        if not values:
            raise SystemExit("this query has no topic tag; use a topic word such as reasonableness")
        names = {f"tag_{index}": value for index, value in enumerate(values)}
        listed = ", ".join(f":{name}" for name in names)
        id_rows = db.execute(
            sql_text(f"SELECT DISTINCT case_id FROM case_tags WHERE taxonomy_version = :version AND value IN ({listed})"),
            {"version": ACTIVE_TAG_TAXONOMY_VERSION, **names},
        ).all()
        ids = [int(row[0]) for row in id_rows]
        lines.append(f"query={args.query!r} tagged cases={len(ids)}")
        for label, expression in probes:
            used = {key: value for key, value in params.items() if f":{key}" in expression or key == "match_guard" and ":match_guard" in expression}
            started = time.perf_counter()
            value = db.execute(
                sql_text(f"SELECT {expression} FROM cases c WHERE c.id = ANY(CAST(:probe_ids AS integer[]))"),
                {**used, "probe_ids": ids},
            ).scalar()
            lines.append(f"{time.perf_counter() - started:7.2f} s  {label}  -> {value}")
            print(lines[-1])
    finally:
        db.close()
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
