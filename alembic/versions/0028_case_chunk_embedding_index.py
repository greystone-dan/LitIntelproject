"""add HNSW index for hosted paragraph embeddings

Revision ID: 0028_case_chunk_embedding_index
Revises: 0027_fc_activity_provenance
Create Date: 2026-10-01 00:00:00.000000
"""

from alembic import op


revision = "0028_case_chunk_embedding_index"
down_revision = "0027_fc_activity_provenance"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.get_context().autocommit_block():
        op.execute(
            "CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_case_chunks_embedding_cosine "
            "ON case_chunks USING hnsw (embedding vector_cosine_ops)"
        )


def downgrade() -> None:
    with op.get_context().autocommit_block():
        op.execute("DROP INDEX CONCURRENTLY IF EXISTS ix_case_chunks_embedding_cosine")