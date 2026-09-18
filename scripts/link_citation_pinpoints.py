"""Persist resolved case-citation paragraph links from stored paragraph chunks."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from sqlalchemy import text

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import SessionLocal

PINPOINT_RE = re.compile(
    r"(?:at\s+)?(?:para(?:s|graph(?:s)?)?\.?|paragraph(?:s)?)\s+(\d+)",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--apply", action="store_true", help="Write target paragraph links.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be at least 1")

    with SessionLocal() as session:
        limit_sql = "" if args.limit is None else "LIMIT :limit"
        eligible_sql = f"""
            SELECT c.id, c.target_case_id,
                   substring(c.citation_text FROM :pinpoint_pattern)::integer AS paragraph
            FROM citations AS c
            WHERE c.target_case_id IS NOT NULL
              AND c.target_paragraph IS NULL
              AND c.citation_text IS NOT NULL
              AND c.citation_text ~* :pinpoint_pattern
            ORDER BY c.id
            {limit_sql}
        """
        matches_sql = f"""
            WITH eligible AS ({eligible_sql}), match_counts AS (
                SELECT e.id, e.paragraph, COUNT(cc.id) AS match_count,
                       MIN(cc.id) AS target_chunk_id
                FROM eligible AS e
                LEFT JOIN case_chunks AS cc
                  ON cc.case_id = e.target_case_id
                 AND cc.chunk_set = 'paragraph'
                 AND cc.paragraph_start IS NOT NULL
                 AND cc.paragraph_end IS NOT NULL
                 AND cc.paragraph_start <= e.paragraph
                 AND cc.paragraph_end >= e.paragraph
                GROUP BY e.id, e.paragraph
            )
            SELECT COUNT(*) AS inspected,
                   COUNT(*) FILTER (WHERE match_count = 1) AS linked,
                   COUNT(*) FILTER (WHERE match_count <> 1) AS missing_chunk
            FROM match_counts
        """
        params = {"pinpoint_pattern": PINPOINT_RE.pattern}
        if args.limit is not None:
            params["limit"] = args.limit
        if not args.apply:
            summary = session.execute(text(matches_sql), params).mappings().one()
            print(
                f"inspected={summary['inspected']} linked={summary['linked']} "
                f"missing_chunk={summary['missing_chunk']} invalid=0 apply=False"
            )
            print("dry_run=true; no database rows changed")
            return

        update_sql = f"""
            WITH eligible AS ({eligible_sql}), match_counts AS (
                SELECT e.id, e.paragraph, COUNT(cc.id) AS match_count,
                       MIN(cc.id) AS target_chunk_id
                FROM eligible AS e
                LEFT JOIN case_chunks AS cc
                  ON cc.case_id = e.target_case_id
                 AND cc.chunk_set = 'paragraph'
                 AND cc.paragraph_start IS NOT NULL
                 AND cc.paragraph_end IS NOT NULL
                 AND cc.paragraph_start <= e.paragraph
                 AND cc.paragraph_end >= e.paragraph
                GROUP BY e.id, e.paragraph
            ), resolved AS (
                SELECT id, paragraph, target_chunk_id
                FROM match_counts
                WHERE match_count = 1
            )
            UPDATE citations AS c
            SET target_paragraph = r.paragraph,
                target_chunk_id = r.target_chunk_id
            FROM resolved AS r
            WHERE c.id = r.id
              AND c.target_paragraph IS NULL
            RETURNING c.id
        """
        updated = session.execute(text(update_sql), params).fetchall()
        session.commit()
        print(f"updated={len(updated)} apply=True")


if __name__ == "__main__":
    main()
