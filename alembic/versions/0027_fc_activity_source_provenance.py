"""add nullable FC Activity source provenance

Revision ID: 0027_fc_activity_provenance
Revises: 0026_contextual_authority_p0
Create Date: 2026-09-29 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


revision = "0027_fc_activity_provenance"
down_revision = "0026_contextual_authority_p0"
branch_labels = None
depends_on = None


def upgrade() -> None:
    for table in ("fc_activity_cases", "fc_activity_classifications"):
        op.add_column(table, sa.Column("source_type", sa.String(length=100), nullable=True))
        op.add_column(table, sa.Column("source_name", sa.String(length=255), nullable=True))
        op.add_column(table, sa.Column("source_id", sa.String(length=255), nullable=True))
        for column in ("source_type", "source_name", "source_id"):
            op.create_index(f"ix_{table}_{column}", table, [column])


def downgrade() -> None:
    for table in ("fc_activity_cases", "fc_activity_classifications"):
        for column in ("source_type", "source_name", "source_id"):
            op.drop_index(f"ix_{table}_{column}", table_name=table)
    for table in ("fc_activity_classifications", "fc_activity_cases"):
        for column in ("source_id", "source_name", "source_type"):
            op.drop_column(table, column)