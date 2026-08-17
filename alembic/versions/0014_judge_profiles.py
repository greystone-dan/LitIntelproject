"""add canonical judge profiles

Revision ID: 0014_judge_profiles
Revises: 0013_citation_kind
Create Date: 2026-08-12 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


revision = "0014_judge_profiles"
down_revision = "0013_citation_kind"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "judge_profiles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("display_name", sa.String(length=255), nullable=False),
        sa.Column("normalized_name", sa.String(length=255), nullable=False),
        sa.Column("primary_court", sa.String(length=255), nullable=True),
        sa.Column("aliases", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("normalized_name"),
        sa.UniqueConstraint("slug"),
    )
    op.create_index("ix_judge_profiles_primary_court", "judge_profiles", ["primary_court"])
    op.create_table(
        "case_judge_profiles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("case_id", sa.Integer(), nullable=False),
        sa.Column("judge_profile_id", sa.Integer(), nullable=False),
        sa.Column("raw_name", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["case_id"], ["cases.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["judge_profile_id"], ["judge_profiles.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("case_id", "judge_profile_id", name="uq_case_judge_profile"),
    )
    op.create_index("ix_case_judge_profiles_case_id", "case_judge_profiles", ["case_id"])
    op.create_index("ix_case_judge_profiles_judge_profile_id", "case_judge_profiles", ["judge_profile_id"])


def downgrade() -> None:
    op.drop_index("ix_case_judge_profiles_judge_profile_id", table_name="case_judge_profiles")
    op.drop_index("ix_case_judge_profiles_case_id", table_name="case_judge_profiles")
    op.drop_table("case_judge_profiles")
    op.drop_index("ix_judge_profiles_primary_court", table_name="judge_profiles")
    op.drop_table("judge_profiles")