"""Persist local short-form citation anchor provenance."""

from alembic import op
import sqlalchemy as sa


revision = "0023_citation_anchor_provenance"
down_revision = "0022_case_outcomes"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("citations", sa.Column("anchor_citation_text", sa.Text(), nullable=True))
    op.add_column("citations", sa.Column("anchor_offset_start", sa.Integer(), nullable=True))
    op.add_column("citations", sa.Column("anchor_offset_end", sa.Integer(), nullable=True))
    op.add_column("citations", sa.Column("declared_alias", sa.String(length=255), nullable=True))


def downgrade() -> None:
    op.drop_column("citations", "declared_alias")
    op.drop_column("citations", "anchor_offset_end")
    op.drop_column("citations", "anchor_offset_start")
    op.drop_column("citations", "anchor_citation_text")