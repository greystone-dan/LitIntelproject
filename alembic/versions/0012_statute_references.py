"""add statute references table

Revision ID: 0012_statute_references
Revises: 0011_case_chunk_sets
Create Date: 2026-08-07 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0012_statute_references"
down_revision = "0011_case_chunk_sets"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "statute_references",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("source_case_id", sa.Integer(), nullable=False),
        sa.Column("chunk_id", sa.Integer(), nullable=True),
        sa.Column("offset_start", sa.Integer(), nullable=True),
        sa.Column("offset_end", sa.Integer(), nullable=True),
        sa.Column("reference_text", sa.Text(), nullable=True),
        sa.Column("normalized_reference", sa.Text(), nullable=True),
        sa.Column("reference_kind", sa.String(length=20), nullable=False),
        sa.ForeignKeyConstraint(["chunk_id"], ["case_chunks.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["source_case_id"], ["cases.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_statute_references_source_case_id", "statute_references", ["source_case_id"])
    op.create_index("ix_statute_references_chunk_id", "statute_references", ["chunk_id"])
    op.create_index("ix_statute_references_normalized_reference", "statute_references", ["normalized_reference"])
    op.create_index("ix_statute_references_reference_kind", "statute_references", ["reference_kind"])


def downgrade() -> None:
    op.drop_index("ix_statute_references_reference_kind", table_name="statute_references")
    op.drop_index("ix_statute_references_normalized_reference", table_name="statute_references")
    op.drop_index("ix_statute_references_chunk_id", table_name="statute_references")
    op.drop_index("ix_statute_references_source_case_id", table_name="statute_references")
    op.drop_table("statute_references")
