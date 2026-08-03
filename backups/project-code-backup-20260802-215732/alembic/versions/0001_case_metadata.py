"""Add case provenance and retrieval metadata.

Revision ID: 0001_case_metadata
Revises:
"""
from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector

revision = "0001_case_metadata"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing_columns = {column["name"] for column in inspector.get_columns("cases")}

    if "cases" not in inspector.get_table_names():
        op.create_table(
            "cases",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("title", sa.String(length=255), nullable=False),
            sa.Column("court", sa.String(length=255), nullable=False),
            sa.Column("jurisdiction", sa.String(length=100), nullable=True),
            sa.Column("date", sa.Date(), nullable=False),
            sa.Column("citation", sa.String(length=255), nullable=True),
            sa.Column("summary", sa.Text(), nullable=False),
            sa.Column("full_text", sa.Text(), nullable=True),
            sa.Column("issues", sa.JSON(), nullable=True),
            sa.Column("metadata_json", sa.JSON(), nullable=True),
            sa.Column("source_url", sa.String(length=2048), nullable=True),
            sa.Column("source_name", sa.String(length=255), nullable=True),
            sa.Column("embedding", Vector(1536), nullable=False),
            sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        )
        for column in ("title", "court", "jurisdiction", "date", "citation"):
            op.create_index(f"ix_cases_{column}", "cases", [column])
        return

    additions = {
        "jurisdiction": sa.Column("jurisdiction", sa.String(length=100), nullable=True),
        "citation": sa.Column("citation", sa.String(length=255), nullable=True),
        "full_text": sa.Column("full_text", sa.Text(), nullable=True),
        "issues": sa.Column("issues", sa.JSON(), nullable=True),
        "metadata_json": sa.Column("metadata_json", sa.JSON(), nullable=True),
        "source_url": sa.Column("source_url", sa.String(length=2048), nullable=True),
        "source_name": sa.Column("source_name", sa.String(length=255), nullable=True),
    }
    for name, column in additions.items():
        if name not in existing_columns:
            op.add_column("cases", column)

    for column in ("jurisdiction", "citation"):
        if column not in existing_columns:
            op.create_index(f"ix_cases_{column}", "cases", [column])

    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_cases_embedding_cosine "
        "ON cases USING hnsw (embedding vector_cosine_ops)"
    )


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "cases" not in inspector.get_table_names():
        return
    op.execute("DROP INDEX IF EXISTS ix_cases_embedding_cosine")
    for column in ("source_name", "source_url", "metadata_json", "issues", "full_text", "citation", "jurisdiction"):
        if column in {item["name"] for item in inspector.get_columns("cases")}:
            op.drop_column("cases", column)
