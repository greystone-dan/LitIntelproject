"""Add paragraph_positions for the whose-position reader tags. Additive only.

Undo: DROP TABLE paragraph_positions; (or alembic downgrade 0045_issue_maps).

Revision ID: 0046_paragraph_positions
Revises: 0045_issue_maps
Create Date: 2026-10-11
"""

import sqlalchemy as sa
from alembic import op


revision = "0046_paragraph_positions"
down_revision = "0045_issue_maps"
branch_labels = None
depends_on = None


def upgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    if "paragraph_positions" not in set(inspector.get_table_names()):
        op.create_table(
            "paragraph_positions",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
            sa.Column("tagger", sa.String(40), nullable=False),
            sa.Column("paragraph_count", sa.Integer(), nullable=False),
            sa.Column("paragraphs", sa.JSON(), nullable=False),
            sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
            sa.UniqueConstraint("case_id", name="uq_paragraph_positions_case_id"),
        )


def downgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    if "paragraph_positions" in set(inspector.get_table_names()):
        op.drop_table("paragraph_positions")
