"""Add citation edges and citation metrics.

Revision ID: 0005_citation_network
Revises: 0004_case_chunks
"""
from alembic import op
import sqlalchemy as sa

revision = "0005_citation_network"
down_revision = "0004_case_chunks"
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.create_table(
		"citations",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("source_case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
		sa.Column("target_case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=True),
		sa.Column("citation_text", sa.Text(), nullable=True),
		sa.Column("normalized_citation", sa.Text(), nullable=True),
		sa.Column("chunk_id", sa.Integer(), sa.ForeignKey("case_chunks.id", ondelete="SET NULL"), nullable=True),
		sa.Column("offset_start", sa.Integer(), nullable=True),
		sa.Column("offset_end", sa.Integer(), nullable=True),
		sa.Column("unresolved", sa.Boolean(), nullable=False, server_default=sa.text("false")),
	)
	op.create_index("ix_citations_source_case_id", "citations", ["source_case_id"])
	op.create_index("ix_citations_target_case_id", "citations", ["target_case_id"])
	op.create_index("ix_citations_normalized_citation", "citations", ["normalized_citation"])
	op.create_index("ix_citations_chunk_id", "citations", ["chunk_id"])

	op.create_table(
		"citation_metrics",
		sa.Column("case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), primary_key=True),
		sa.Column("in_degree", sa.Integer(), nullable=True),
		sa.Column("out_degree", sa.Integer(), nullable=True),
		sa.Column("pagerank", sa.Float(), nullable=True),
	)


def downgrade() -> None:
	op.drop_table("citation_metrics")
	op.drop_index("ix_citations_chunk_id", table_name="citations")
	op.drop_index("ix_citations_normalized_citation", table_name="citations")
	op.drop_index("ix_citations_target_case_id", table_name="citations")
	op.drop_index("ix_citations_source_case_id", table_name="citations")
	op.drop_table("citations")