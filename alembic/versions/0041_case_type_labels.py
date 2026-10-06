"""Add case_type_labels (deterministic case-type labels).

Revision ID: 0041_case_type_labels
Revises: 0040_judge_profile_aliases
Create Date: 2026-10-06
"""

import sqlalchemy as sa
from alembic import op


revision = "0041_case_type_labels"
down_revision = "0040_judge_profile_aliases"
branch_labels = None
depends_on = None


def upgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    if "case_type_labels" in set(inspector.get_table_names()):
        return
    op.create_table(
        "case_type_labels",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
        sa.Column("taxonomy_version", sa.String(50), nullable=False),
        sa.Column("status", sa.String(30), nullable=False),
        sa.Column("primary_type", sa.String(80), nullable=True),
        sa.Column("primary_detail", sa.String(80), nullable=True),
        sa.Column("secondary_types", sa.JSON(), nullable=True),
        sa.Column("proceeding", sa.String(60), nullable=True),
        sa.Column("confidence", sa.Float(), nullable=False, server_default="0"),
        sa.Column("scores", sa.JSON(), nullable=True),
        sa.Column("evidence", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("case_id", "taxonomy_version", name="uq_case_type_label_version"),
    )
    for column in ("case_id", "taxonomy_version", "status", "primary_type"):
        op.create_index(f"ix_case_type_labels_{column}", "case_type_labels", [column])


def downgrade() -> None:
    for column in ("primary_type", "status", "taxonomy_version", "case_id"):
        op.drop_index(f"ix_case_type_labels_{column}", table_name="case_type_labels")
    op.drop_table("case_type_labels")
