"""Add stored case fingerprints (not used by the live site yet).

Revision ID: 0042_case_fingerprints
Revises: 0041_case_type_labels
Create Date: 2026-10-06
"""

import sqlalchemy as sa
from alembic import op


revision = "0042_case_fingerprints"
down_revision = "0041_case_type_labels"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    if "case_fingerprints" in set(sa.inspect(bind).get_table_names()):
        return
    op.create_table(
        "case_fingerprints",
        sa.Column("case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), primary_key=True, nullable=False),
        sa.Column("version", sa.String(20), nullable=False),
        sa.Column("terms", sa.JSON(), nullable=False),
        sa.Column("authorities", sa.JSON(), nullable=False),
        sa.Column("role_chars", sa.JSON(), nullable=True),
        sa.Column("text_length", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("computed_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_case_fingerprints_version", "case_fingerprints", ["version"])


def downgrade() -> None:
    op.drop_index("ix_case_fingerprints_version", table_name="case_fingerprints")
    op.drop_table("case_fingerprints")
