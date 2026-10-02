"""Refresh the derived recent-5000 paragraph retrieval artifact."""

from __future__ import annotations

import argparse
import json
from typing import Any

from sqlalchemy import text

from backend.database import SessionLocal

_REFRESH_SQL = """
INSERT INTO recent_case_chunk_embeddings (
    chunk_id,
    case_id,
    chunk_index,
    paragraph_start,
    paragraph_end,
    chunk_set,
    text,
    embedding,
    embedding_model,
    refreshed_at
)
WITH recent_cases AS (
    SELECT id
    FROM cases
    ORDER BY date DESC, id DESC
    LIMIT 5000
)
SELECT
    cc.id,
    cc.case_id,
    cc.chunk_index,
    cc.paragraph_start,
    cc.paragraph_end,
    cc.chunk_set,
    cc.text,
    cc.embedding,
    cc.embedding_model,
    NOW()
FROM case_chunks cc
JOIN recent_cases rc ON rc.id = cc.case_id
WHERE cc.chunk_set = 'paragraph'
  AND cc.embedding IS NOT NULL
  AND cc.embedding_model = 'text-embedding-3-small';
"""

_PREVIEW_SQL = """
WITH recent_cases AS (
    SELECT id
    FROM cases
    ORDER BY date DESC, id DESC
    LIMIT 5000
)
SELECT COUNT(*) AS rows, COUNT(DISTINCT cc.case_id) AS cases
FROM case_chunks cc
JOIN recent_cases rc ON rc.id = cc.case_id
WHERE cc.chunk_set = 'paragraph'
  AND cc.embedding IS NOT NULL
  AND cc.embedding_model = 'text-embedding-3-small';
"""


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the refreshed derived artifact")
    parser.add_argument(
        "--confirm-recent-5000-refresh",
        action="store_true",
        help="confirm that only the derived recent-5000 artifact may be replaced",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    with SessionLocal() as database:
        table_name = database.scalar(text("SELECT to_regclass('public.recent_case_chunk_embeddings')"))
        if table_name is None:
            raise SystemExit("recent_case_chunk_embeddings is unavailable; apply migration 0029 first")
        preview = dict(database.execute(text(_PREVIEW_SQL)).mappings().one())
        if not args.apply:
            print(json.dumps({"mode": "dry_run", "qualifying": preview}, default=str))
            return 0
        if not args.confirm_recent_5000_refresh:
            raise SystemExit("--apply requires --confirm-recent-5000-refresh")
        database.rollback()
        with database.begin():
            database.execute(text("TRUNCATE TABLE recent_case_chunk_embeddings"))
            database.execute(text(_REFRESH_SQL))
        refreshed = dict(
            database.execute(
                text("SELECT COUNT(*) AS rows, COUNT(DISTINCT case_id) AS cases FROM recent_case_chunk_embeddings")
            ).mappings().one()
        )
        print(json.dumps({"mode": "applied", "qualifying": preview, "refreshed": refreshed}, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
