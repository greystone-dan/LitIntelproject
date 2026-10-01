"""Report PostgreSQL progress for the hosted paragraph vector index build."""

from sqlalchemy import text

from backend.database import SessionLocal


QUERY = text(
    """
    SELECT
        p.pid,
        p.phase,
        p.blocks_total,
        p.blocks_done,
        p.tuples_total,
        p.tuples_done,
        EXISTS (
            SELECT 1
            FROM pg_indexes
            WHERE tablename = 'case_chunks'
              AND indexname = 'ix_case_chunks_embedding_cosine'
        ) AS index_exists
    FROM pg_stat_progress_create_index AS p
    WHERE p.relid = 'case_chunks'::regclass
    ORDER BY p.pid
    """
)


with SessionLocal() as database:
    database.execute(text("SET TRANSACTION READ ONLY"))
    rows = [dict(row) for row in database.execute(QUERY).mappings()]
    if rows:
        for row in rows:
            print(row)
    else:
        exists = database.scalar(
            text(
                """
                SELECT EXISTS (
                    SELECT 1 FROM pg_indexes
                    WHERE tablename = 'case_chunks'
                      AND indexname = 'ix_case_chunks_embedding_cosine'
                )
                """
            )
        )
        print({"running": False, "index_exists": bool(exists)})