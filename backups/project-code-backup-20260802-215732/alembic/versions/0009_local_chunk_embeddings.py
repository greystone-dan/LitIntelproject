"""Add model-versioned BGE-M3 chunk embeddings alongside OpenAI vectors."""

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector

revision = "0009_local_chunk_embeddings"
down_revision = "0008_case_provenance_tables"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "case_chunk_embeddings",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("chunk_id", sa.Integer(), nullable=False),
        sa.Column("model_name", sa.String(length=255), nullable=False),
        sa.Column("dimensions", sa.Integer(), nullable=False),
        sa.Column("embedding", Vector(1024), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.ForeignKeyConstraint(["chunk_id"], ["case_chunks.id"], ondelete="CASCADE"),
        sa.UniqueConstraint("chunk_id", "model_name", name="uq_chunk_embedding_model"),
    )
    op.create_index(
        "ix_case_chunk_embeddings_chunk_id",
        "case_chunk_embeddings",
        ["chunk_id"],
    )
    op.create_index(
        "ix_case_chunk_embeddings_model_name",
        "case_chunk_embeddings",
        ["model_name"],
    )
    op.execute(
        "CREATE INDEX ix_case_chunk_embeddings_cosine "
        "ON case_chunk_embeddings USING hnsw (embedding vector_cosine_ops)"
    )


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_case_chunk_embeddings_cosine")
    op.drop_index("ix_case_chunk_embeddings_model_name", table_name="case_chunk_embeddings")
    op.drop_index("ix_case_chunk_embeddings_chunk_id", table_name="case_chunk_embeddings")
    op.drop_table("case_chunk_embeddings")
