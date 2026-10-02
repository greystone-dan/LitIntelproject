"""reserve the retired full-corpus HNSW migration slot

Revision ID: 0028_case_chunk_embedding_index
Revises: 0027_fc_activity_provenance
Create Date: 2026-10-01 00:00:00.000000
"""

from alembic import op


revision = "0028_case_chunk_embedding_index"
down_revision = "0027_fc_activity_provenance"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # The original full-corpus HNSW attempt is intentionally retired. This
    # revision remains in the chain so fresh upgrades do not launch it.
    return None


def downgrade() -> None:
    return None