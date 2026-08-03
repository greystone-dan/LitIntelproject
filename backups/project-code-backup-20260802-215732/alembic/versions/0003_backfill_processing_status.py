"""Backfill processing status for existing embedded records.

Revision ID: 0003_backfill_processing_status
Revises: 0002_raw_ingestion
"""
from alembic import op

revision = "0003_backfill_processing_status"
down_revision = "0002_raw_ingestion"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        "UPDATE cases SET processing_status = 'embedded' "
        "WHERE embedding IS NOT NULL AND processing_status = 'raw'"
    )


def downgrade() -> None:
    op.execute(
        "UPDATE cases SET processing_status = 'raw' "
        "WHERE embedding IS NOT NULL AND processing_status = 'embedded'"
    )
