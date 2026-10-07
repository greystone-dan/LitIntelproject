"""Add pinpoint columns to citations_refined. Additive only.

Revision ID: 0044_refined_pinpoints
Revises: 0043_workbench
Create Date: 2026-10-07
"""

import sqlalchemy as sa
from alembic import op


revision = "0044_refined_pinpoints"
down_revision = "0043_workbench"
branch_labels = None
depends_on = None

COLUMNS = (
    ("pinpoint", sa.String(100)),
    ("pinpoint_kind", sa.String(12)),
    ("pinpoint_values", sa.String(255)),
)


def upgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    if "citations_refined" not in inspector.get_table_names():
        return
    existing = {column["name"] for column in inspector.get_columns("citations_refined")}
    for name, kind in COLUMNS:
        if name not in existing:
            op.add_column("citations_refined", sa.Column(name, kind, nullable=True))


def downgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    if "citations_refined" not in inspector.get_table_names():
        return
    existing = {column["name"] for column in inspector.get_columns("citations_refined")}
    for name, _ in reversed(COLUMNS):
        if name in existing:
            op.drop_column("citations_refined", name)
