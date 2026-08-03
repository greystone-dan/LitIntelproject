"""Add fc_procedural_history table.

Revision ID: 0007_fc_procedural_history
Revises: 0006_a2aj_citation_network
"""
from alembic import op
import sqlalchemy as sa

revision = "0007_fc_procedural_history"
down_revision = "0006_a2aj_citation_network"
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.create_table(
		"fc_procedural_history",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("imm_number", sa.String(length=50), nullable=False, unique=True),
		sa.Column("style_of_cause", sa.Text(), nullable=True),
		sa.Column("judge", sa.String(length=120), nullable=True),
		sa.Column("leave_decision", sa.String(length=30), nullable=True),
		sa.Column("leave_date", sa.Date(), nullable=True),
		sa.Column("jr_decision", sa.String(length=40), nullable=True),
		sa.Column("jr_decision_date", sa.Date(), nullable=True),
		sa.Column("case_status", sa.String(length=40), nullable=True),
		sa.Column("latest_activity_date", sa.Date(), nullable=True),
		sa.Column("full_activity_text", sa.Text(), nullable=True),
		sa.Column("entries_json", sa.JSON(), nullable=True),
		sa.Column("conflict_flag", sa.Boolean(), nullable=False, server_default=sa.text("false")),
		sa.Column("fetched_at", sa.DateTime(timezone=True), nullable=True),
	)
	op.create_index("ix_fc_procedural_history_imm_number", "fc_procedural_history", ["imm_number"])
	op.create_index("ix_fc_procedural_history_case_status", "fc_procedural_history", ["case_status"])
	op.create_index("ix_fc_procedural_history_leave_decision", "fc_procedural_history", ["leave_decision"])


def downgrade() -> None:
	op.drop_table("fc_procedural_history")
