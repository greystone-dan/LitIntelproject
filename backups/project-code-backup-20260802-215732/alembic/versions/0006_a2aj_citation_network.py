"""Add A2AJ citation network provenance tables.

Revision ID: 0006_a2aj_citation_network
Revises: 0005_citation_network
"""
from alembic import op
import sqlalchemy as sa

revision = "0006_a2aj_citation_network"
down_revision = "0005_citation_network"
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.add_column(
		"citations",
		sa.Column("provenance", sa.String(length=20), nullable=False, server_default=sa.text("'local'")),
	)
	op.create_index("ix_citations_provenance", "citations", ["provenance"])

	op.create_table(
		"a2aj_cases",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("a2aj_case_id", sa.Text(), nullable=False, unique=True),
		sa.Column("neutral_citation", sa.Text(), nullable=True),
		sa.Column("court", sa.Text(), nullable=True),
		sa.Column("decision_date", sa.Date(), nullable=True),
		sa.Column("cases_cited", sa.JSON(), nullable=True),
		sa.Column("cases_citing", sa.JSON(), nullable=True),
		sa.Column("citing_cases_count", sa.Integer(), nullable=True),
	)
	op.create_index("ix_a2aj_cases_a2aj_case_id", "a2aj_cases", ["a2aj_case_id"])
	op.create_index("ix_a2aj_cases_neutral_citation", "a2aj_cases", ["neutral_citation"])
	op.create_index("ix_a2aj_cases_decision_date", "a2aj_cases", ["decision_date"])

	op.create_table(
		"a2aj_citation_edges",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("source_a2aj_case_id", sa.Text(), nullable=False),
		sa.Column("target_a2aj_case_id", sa.Text(), nullable=True),
		sa.Column("normalized_citation", sa.Text(), nullable=True),
	)
	op.create_index("ix_a2aj_citation_edges_source", "a2aj_citation_edges", ["source_a2aj_case_id"])
	op.create_index("ix_a2aj_citation_edges_target", "a2aj_citation_edges", ["target_a2aj_case_id"])
	op.create_index("ix_a2aj_citation_edges_normalized", "a2aj_citation_edges", ["normalized_citation"])

	op.create_table(
		"a2aj_case_map",
		sa.Column("a2aj_case_id", sa.Text(), sa.ForeignKey("a2aj_cases.a2aj_case_id", ondelete="CASCADE"), primary_key=True),
		sa.Column("local_case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
	)
	op.create_index("ix_a2aj_case_map_local_case_id", "a2aj_case_map", ["local_case_id"])


def downgrade() -> None:
	op.drop_index("ix_a2aj_case_map_local_case_id", table_name="a2aj_case_map")
	op.drop_table("a2aj_case_map")
	op.drop_index("ix_a2aj_citation_edges_normalized", table_name="a2aj_citation_edges")
	op.drop_index("ix_a2aj_citation_edges_target", table_name="a2aj_citation_edges")
	op.drop_index("ix_a2aj_citation_edges_source", table_name="a2aj_citation_edges")
	op.drop_table("a2aj_citation_edges")
	op.drop_index("ix_a2aj_cases_decision_date", table_name="a2aj_cases")
	op.drop_index("ix_a2aj_cases_neutral_citation", table_name="a2aj_cases")
	op.drop_index("ix_a2aj_cases_a2aj_case_id", table_name="a2aj_cases")
	op.drop_table("a2aj_cases")
	op.drop_index("ix_citations_provenance", table_name="citations")
	op.drop_column("citations", "provenance")