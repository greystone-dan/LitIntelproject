"""Build the full-text search column and index for cases (run once, in a quiet window).

Not part of the normal deploy migration because it rewrites a very large table.
Safe to stop and re-run: the backfill only touches rows still NULL, and the code
keeps using the slower ILIKE path until the index ix_cases_search_tsv exists.

    python scripts/build_fulltext_index.py [--batch 500]
"""

import argparse
import os
import time

from sqlalchemy import create_engine, text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=int, default=500)
    args = parser.parse_args()
    from backend.database import DATABASE_URL

    engine = create_engine(os.environ.get("DATABASE_URL", DATABASE_URL), isolation_level="AUTOCOMMIT")
    with engine.connect() as conn:
        conn.execute(text("ALTER TABLE cases ADD COLUMN IF NOT EXISTS search_tsv tsvector"))
        conn.execute(text(
            "CREATE OR REPLACE FUNCTION cases_search_tsv_update() RETURNS trigger AS $$ BEGIN "
            "NEW.search_tsv := to_tsvector('english', COALESCE(NEW.title,'') || ' ' || COALESCE(NEW.summary,'') || ' ' || COALESCE(NEW.full_text,'')); "
            "RETURN NEW; END $$ LANGUAGE plpgsql"
        ))
        conn.execute(text("DROP TRIGGER IF EXISTS cases_search_tsv_trg ON cases"))
        conn.execute(text(
            "CREATE TRIGGER cases_search_tsv_trg BEFORE INSERT OR UPDATE OF title, summary, full_text ON cases "
            "FOR EACH ROW EXECUTE FUNCTION cases_search_tsv_update()"
        ))
        done = 0
        while True:
            result = conn.execute(text(
                "UPDATE cases SET search_tsv = to_tsvector('english', COALESCE(title,'') || ' ' || COALESCE(summary,'') || ' ' || COALESCE(full_text,'')) "
                "WHERE id IN (SELECT id FROM cases WHERE search_tsv IS NULL ORDER BY id LIMIT :n)"
            ), {"n": args.batch})
            if not result.rowcount:
                break
            done += result.rowcount
            print(f"backfilled {done}", flush=True)
            time.sleep(0.05)
        print("building index (CONCURRENTLY)...", flush=True)
        conn.execute(text("CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_cases_search_tsv ON cases USING gin (search_tsv)"))
        print("done")


if __name__ == "__main__":
    main()
