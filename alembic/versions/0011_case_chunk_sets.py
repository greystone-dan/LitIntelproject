"""Add chunk set metadata for section and paragraph storage.

Revision ID: 0011_case_chunk_sets
Revises: 0010_case_legal_tags
"""

from alembic import op
import sqlalchemy as sa

revision = "0011_case_chunk_sets"
down_revision = "0010_case_legal_tags"
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.add_column(
		"case_chunks",
		sa.Column("chunk_set", sa.String(length=50), nullable=False, server_default="legacy"),
	)
	op.add_column("case_chunks", sa.Column("chunk_label", sa.String(length=255), nullable=True))
	op.add_column("case_chunks", sa.Column("paragraph_start", sa.Integer(), nullable=True))
	op.add_column("case_chunks", sa.Column("paragraph_end", sa.Integer(), nullable=True))
	op.create_index("ix_case_chunks_chunk_set", "case_chunks", ["chunk_set"])
	op.create_index(
		"ix_case_chunks_case_set_index",
		"case_chunks",
		["case_id", "chunk_set", "chunk_index"],
	)


def downgrade() -> None:
	op.drop_index("ix_case_chunks_case_set_index", table_name="case_chunks")
	op.drop_index("ix_case_chunks_chunk_set", table_name="case_chunks")
	op.drop_column("case_chunks", "paragraph_end")
	op.drop_column("case_chunks", "paragraph_start")
	op.drop_column("case_chunks", "chunk_label")
	op.drop_column("case_chunks", "chunk_set")