"""Add chunk storage for full-text embeddings.

Revision ID: 0004_case_chunks
Revises: 0003_backfill_processing_status
"""
from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector

revision = "0004_case_chunks"
down_revision = "0003_backfill_processing_status"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "case_chunks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("case_id", sa.Integer(), nullable=False),
        sa.Column("chunk_index", sa.Integer(), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("text_hash", sa.String(length=64), nullable=False),
        sa.Column("token_estimate", sa.Integer(), nullable=False),
        sa.Column("embedding", Vector(1536), nullable=True),
        sa.Column("embedding_model", sa.String(length=100), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_case_chunks_case_id", "case_chunks", ["case_id"])
    op.create_index("ix_case_chunks_text_hash", "case_chunks", ["text_hash"])


def downgrade() -> None:
    op.drop_index("ix_case_chunks_text_hash", table_name="case_chunks")
    op.drop_index("ix_case_chunks_case_id", table_name="case_chunks")
    op.drop_table("case_chunks")