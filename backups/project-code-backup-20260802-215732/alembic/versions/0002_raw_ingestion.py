"""Support raw ingestion without summaries or embeddings.

Revision ID: 0002_raw_ingestion
Revises: 0001_case_metadata
"""
from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector

revision = "0002_raw_ingestion"
down_revision = "0001_case_metadata"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing_columns = {column["name"] for column in inspector.get_columns("cases")}

    additions = {
        "secondary_citation": sa.Column("secondary_citation", sa.String(length=255), nullable=True),
        "source_id": sa.Column("source_id", sa.String(length=255), nullable=True),
        "source_type": sa.Column("source_type", sa.String(length=100), nullable=True),
        "dataset_version": sa.Column("dataset_version", sa.String(length=100), nullable=True),
        "upstream_license": sa.Column("upstream_license", sa.Text(), nullable=True),
        "scraped_at": sa.Column("scraped_at", sa.DateTime(timezone=True), nullable=True),
        "language": sa.Column("language", sa.String(length=10), nullable=True),
        "full_text_hash": sa.Column("full_text_hash", sa.String(length=64), nullable=True),
        "processing_status": sa.Column("processing_status", sa.String(length=30), nullable=False, server_default="raw"),
        "cases_cited": sa.Column("cases_cited", sa.JSON(), nullable=True),
        "cases_citing": sa.Column("cases_citing", sa.JSON(), nullable=True),
        "citing_cases_count": sa.Column("citing_cases_count", sa.Integer(), nullable=True),
    }
    for name, column in additions.items():
        if name not in existing_columns:
            op.add_column("cases", column)

    op.alter_column("cases", "summary", existing_type=sa.Text(), nullable=True)
    op.alter_column("cases", "embedding", existing_type=Vector(1536), nullable=True)

    for column in ("source_id", "full_text_hash", "processing_status"):
        op.create_index(f"ix_cases_{column}", "cases", [column], if_not_exists=True)


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing_columns = {column["name"] for column in inspector.get_columns("cases")}

    for column in ("full_text_hash", "source_id", "processing_status"):
        op.drop_index(f"ix_cases_{column}", table_name="cases")
    for column in (
        "citing_cases_count", "cases_citing", "cases_cited", "processing_status",
        "full_text_hash", "language", "scraped_at", "upstream_license",
        "dataset_version", "source_type", "source_id", "secondary_citation",
    ):
        if column in existing_columns:
            op.drop_column("cases", column)

    op.alter_column("cases", "summary", existing_type=sa.Text(), nullable=False)
    op.alter_column("cases", "embedding", existing_type=Vector(1536), nullable=False)
