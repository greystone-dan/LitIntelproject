"""add citation kind

Revision ID: 0013_citation_kind
Revises: 0012_statute_references
Create Date: 2026-08-07 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0013_citation_kind"
down_revision = "0012_statute_references"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "citations",
        sa.Column("citation_kind", sa.String(length=20), server_default="unknown", nullable=False),
    )
    op.create_index("ix_citations_citation_kind", "citations", ["citation_kind"])


def downgrade() -> None:
    op.drop_index("ix_citations_citation_kind", table_name="citations")
    op.drop_column("citations", "citation_kind")