"""add partial IVFFlat index for all hosted paragraph embeddings

Revision ID: 0030_full_paragraph_ivfflat
Revises: 0029_recent_5000_ivfflat
Create Date: 2026-10-02 00:00:00.000000
"""

from alembic import op


revision = "0030_full_paragraph_ivfflat"
down_revision = "0029_recent_5000_ivfflat"
branch_labels = None
depends_on = None


def upgrade() -> None:
	with op.get_context().autocommit_block():
		op.execute("SET maintenance_work_mem = '512MB'")
		op.execute(
			"CREATE INDEX CONCURRENTLY IF NOT EXISTS "
			"ix_case_chunks_paragraph_embedding_ivfflat "
			"ON case_chunks USING ivfflat (embedding vector_cosine_ops) "
			"WITH (lists = 1000) "
			"WHERE chunk_set = 'paragraph' "
			"AND embedding_model = 'text-embedding-3-small' "
			"AND embedding IS NOT NULL"
		)


def downgrade() -> None:
	with op.get_context().autocommit_block():
		op.execute(
			"DROP INDEX CONCURRENTLY IF EXISTS "
			"ix_case_chunks_paragraph_embedding_ivfflat"
		)