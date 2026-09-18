"""Persist citation target paragraph links."""

from alembic import op
import sqlalchemy as sa


revision = "0024_citation_target_paragraph"
down_revision = "0023_citation_anchor_provenance"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("citations", sa.Column("target_paragraph", sa.Integer(), nullable=True))
    op.add_column("citations", sa.Column("target_chunk_id", sa.Integer(), nullable=True))
    op.create_index("ix_citations_target_paragraph", "citations", ["target_paragraph"])
    op.create_index("ix_citations_target_chunk_id", "citations", ["target_chunk_id"])
    op.create_foreign_key(
        "fk_citations_target_chunk_id_case_chunks",
        "citations",
        "case_chunks",
        ["target_chunk_id"],
        ["id"],
        ondelete="SET NULL",
    )


def downgrade() -> None:
    op.drop_constraint("fk_citations_target_chunk_id_case_chunks", "citations", type_="foreignkey")
    op.drop_index("ix_citations_target_chunk_id", table_name="citations")
    op.drop_index("ix_citations_target_paragraph", table_name="citations")
    op.drop_column("citations", "target_chunk_id")
    op.drop_column("citations", "target_paragraph")
