"""Add paragraph-level cited-by tables (additive; filled later by an opt-in batch script)

Revision ID: 0036_paragraph_cited_by
Revises: 0035_statute_library_phase1
Create Date: 2026-10-04 20:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


revision = "0036_paragraph_cited_by"
down_revision = "0035_statute_library_phase1"
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.create_table(
		"paragraph_citation_edges",
		sa.Column("id", sa.Integer(), nullable=False),
		sa.Column("source_case_id", sa.Integer(), nullable=False),
		sa.Column("target_case_id", sa.Integer(), nullable=False),
		sa.Column("target_paragraph", sa.Integer(), nullable=False),
		sa.Column("mentions", sa.Integer(), server_default="1", nullable=False),
		sa.Column("purpose", sa.String(20), server_default="mentioned", nullable=False),
		sa.Column("purpose_counts", sa.JSON(), nullable=True),
		sa.Column("signal", sa.String(60), nullable=True),
		sa.Column("algo_version", sa.Integer(), server_default="1", nullable=False),
		sa.PrimaryKeyConstraint("id"),
		sa.ForeignKeyConstraint(["source_case_id"], ["cases.id"], ondelete="CASCADE"),
		sa.ForeignKeyConstraint(["target_case_id"], ["cases.id"], ondelete="CASCADE"),
		sa.UniqueConstraint(
			"source_case_id", "target_case_id", "target_paragraph", name="uq_paragraph_citation_edge"
		),
	)
	op.create_index(
		"ix_paragraph_citation_target",
		"paragraph_citation_edges",
		["target_case_id", "target_paragraph"],
	)
	op.create_table(
		"paragraph_citation_status",
		sa.Column("source_case_id", sa.Integer(), nullable=False),
		sa.Column("algo_version", sa.Integer(), nullable=False),
		sa.Column("edges", sa.Integer(), server_default="0", nullable=False),
		sa.Column("computed_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.PrimaryKeyConstraint("source_case_id"),
		sa.ForeignKeyConstraint(["source_case_id"], ["cases.id"], ondelete="CASCADE"),
	)


def downgrade() -> None:
	op.drop_table("paragraph_citation_status")
	op.drop_index("ix_paragraph_citation_target", table_name="paragraph_citation_edges")
	op.drop_table("paragraph_citation_edges")
