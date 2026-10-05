"""add recent_5000 IVFFlat paragraph retrieval artifact

Revision ID: 0029_recent_5000_ivfflat
Revises: 0028_case_chunk_embedding_index
Create Date: 2026-10-02 00:00:00.000000
"""

from alembic import op


revision = "0029_recent_5000_ivfflat"
down_revision = "0028_case_chunk_embedding_index"
branch_labels = None
depends_on = None


_REFRESH_SQL = """
TRUNCATE TABLE recent_case_chunk_embeddings;

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


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS recent_case_chunk_embeddings (
            chunk_id INTEGER PRIMARY KEY REFERENCES case_chunks(id) ON DELETE CASCADE,
            case_id INTEGER NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
            chunk_index INTEGER NOT NULL,
            paragraph_start INTEGER NULL,
            paragraph_end INTEGER NULL,
            chunk_set VARCHAR(50) NOT NULL DEFAULT 'paragraph',
            text TEXT NOT NULL,
            embedding vector(1536) NOT NULL,
            embedding_model VARCHAR(100) NOT NULL,
            refreshed_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
        """
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_recent_case_chunk_embeddings_case_id "
        "ON recent_case_chunk_embeddings (case_id)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_recent_case_chunk_embeddings_embedding_model "
        "ON recent_case_chunk_embeddings (embedding_model)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_recent_case_chunk_embeddings_embedding_ivfflat "
        "ON recent_case_chunk_embeddings "
        "USING ivfflat (embedding vector_cosine_ops) WITH (lists = 200)"
    )
    op.execute(_REFRESH_SQL)


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS recent_case_chunk_embeddings")
