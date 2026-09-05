"""Add the dedicated versioned case outcome source of truth."""

from alembic import op
import sqlalchemy as sa


revision = "0022_case_outcomes"
down_revision = "0021_case_tag_evidence_contract"
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.create_table(
		"case_outcomes",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("case_id", sa.Integer(), nullable=False),
		sa.Column("classifier_version", sa.String(length=100), nullable=False),
		sa.Column("decision_outcome", sa.String(length=50), nullable=True),
		sa.Column("outcome_status", sa.String(length=30), nullable=False, server_default="undetermined"),
		sa.Column("winner_side", sa.String(length=30), nullable=True),
		sa.Column("loser_side", sa.String(length=30), nullable=True),
		sa.Column("government_role", sa.String(length=30), nullable=True),
		sa.Column("government_outcome", sa.String(length=30), nullable=True),
		sa.Column("challenged_issue", sa.String(length=100), nullable=True),
		sa.Column("challenged_issues", sa.JSON(), nullable=True),
		sa.Column("disposition_evidence", sa.Text(), nullable=True),
		sa.Column("evidence_offset_start", sa.Integer(), nullable=True),
		sa.Column("evidence_offset_end", sa.Integer(), nullable=True),
		sa.Column("confidence", sa.Float(), nullable=False, server_default="0"),
		sa.Column("source", sa.String(length=50), nullable=False, server_default="deterministic_outcome"),
		sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
		sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
	sa.ForeignKeyConstraint(["case_id"], ["cases.id"], ondelete="CASCADE"),
		sa.UniqueConstraint("case_id", "classifier_version", name="uq_case_outcome_version"),
	)
	op.create_index("ix_case_outcomes_case_id", "case_outcomes", ["case_id"])
	op.create_index("ix_case_outcomes_classifier_version", "case_outcomes", ["classifier_version"])
	op.create_index("ix_case_outcomes_outcome_status", "case_outcomes", ["outcome_status"])
	op.create_index("ix_case_outcomes_winner_side", "case_outcomes", ["winner_side"])
	op.create_index("ix_case_outcomes_loser_side", "case_outcomes", ["loser_side"])
	op.create_index("ix_case_outcomes_government_role", "case_outcomes", ["government_role"])
	op.create_index("ix_case_outcomes_government_outcome", "case_outcomes", ["government_outcome"])
	op.create_index("ix_case_outcomes_challenged_issue", "case_outcomes", ["challenged_issue"])


def downgrade() -> None:
	for index in (
		"ix_case_outcomes_challenged_issue",
		"ix_case_outcomes_government_outcome",
		"ix_case_outcomes_government_role",
		"ix_case_outcomes_loser_side",
		"ix_case_outcomes_winner_side",
		"ix_case_outcomes_outcome_status",
		"ix_case_outcomes_classifier_version",
		"ix_case_outcomes_case_id",
	):
		op.drop_index(index, table_name="case_outcomes")
	op.drop_table("case_outcomes")