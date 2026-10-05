"""Add reversible judge profile alias table.

Revision ID: 0040_judge_profile_aliases
Revises: 0039_citation_refinement
Create Date: 2026-10-05
"""

import sqlalchemy as sa
from alembic import op


revision = "0040_judge_profile_aliases"
down_revision = "0039_citation_refinement"
branch_labels = None
depends_on = None


def upgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    if "judge_profile_aliases" in set(inspector.get_table_names()):
        return
    op.create_table(
        "judge_profile_aliases",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("alias_profile_id", sa.Integer(), sa.ForeignKey("judge_profiles.id", ondelete="CASCADE"), nullable=False, unique=True),
        sa.Column("canonical_profile_id", sa.Integer(), sa.ForeignKey("judge_profiles.id", ondelete="CASCADE"), nullable=False),
        sa.Column("source", sa.String(30), nullable=False, server_default="rule"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_judge_profile_aliases_canonical", "judge_profile_aliases", ["canonical_profile_id"])


def downgrade() -> None:
    op.drop_index("ix_judge_profile_aliases_canonical", table_name="judge_profile_aliases")
    op.drop_table("judge_profile_aliases")
