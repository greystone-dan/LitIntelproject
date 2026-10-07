"""Add Workbench tables (demo analyst case list and pinned decisions). Additive only.

Revision ID: 0043_workbench
Revises: 0042_case_fingerprints
Create Date: 2026-10-07
"""

import sqlalchemy as sa
from alembic import op


revision = "0043_workbench"
down_revision = "0042_case_fingerprints"
branch_labels = None
depends_on = None


def upgrade() -> None:
    existing = set(sa.inspect(op.get_bind()).get_table_names())
    if "workbench_cases" not in existing:
        op.create_table(
            "workbench_cases",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("owner", sa.String(80), nullable=False),
            sa.Column("imm_number", sa.String(50), nullable=False),
            sa.Column("label", sa.String(255), nullable=True),
            sa.Column("notes", sa.Text(), nullable=True),
            sa.Column("tags", sa.JSON(), nullable=True),
            sa.Column("folder", sa.String(80), nullable=True),
            sa.Column("deadline", sa.Date(), nullable=True),
            sa.Column("deadline_label", sa.String(120), nullable=True),
            sa.Column("last_seen_entries", sa.Integer(), nullable=False, server_default="0"),
            sa.Column("last_seen_activity_date", sa.Date(), nullable=True),
            sa.Column("last_seen_status", sa.String(80), nullable=True),
            sa.Column("last_viewed_at", sa.DateTime(timezone=True), nullable=True),
            sa.Column("added_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
            sa.UniqueConstraint("owner", "imm_number", name="uq_workbench_case_owner_imm"),
        )
        op.create_index("ix_workbench_cases_owner", "workbench_cases", ["owner"])
    if "workbench_pins" not in existing:
        op.create_table(
            "workbench_pins",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("owner", sa.String(80), nullable=False),
            sa.Column("case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
            sa.Column("notes", sa.Text(), nullable=True),
            sa.Column("tags", sa.JSON(), nullable=True),
            sa.Column("folder", sa.String(80), nullable=True),
            sa.Column("pinned_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
            sa.UniqueConstraint("owner", "case_id", name="uq_workbench_pin_owner_case"),
        )
        op.create_index("ix_workbench_pins_owner", "workbench_pins", ["owner"])
        op.create_index("ix_workbench_pins_case_id", "workbench_pins", ["case_id"])


def downgrade() -> None:
    op.drop_table("workbench_pins")
    op.drop_table("workbench_cases")
