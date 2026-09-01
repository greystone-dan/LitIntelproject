"""retain source HTML for formatted case reading

Revision ID: 0016_case_source_html
Revises: 0015_fc_activity_classifications
Create Date: 2026-09-01 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


revision = "0016_case_source_html"
down_revision = "0015_fc_activity_classifications"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("cases", sa.Column("source_html", sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column("cases", "source_html")
