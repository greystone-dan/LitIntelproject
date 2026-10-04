"""Merge paragraph similarity and main migrations

Revision ID: 0034_merge_similarity_main
Revises: 0031_paragraph_similarity, 0033_discussion_unit_cache
Create Date: 2026-10-04 12:04:07.732900
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '0034_merge_similarity_main'
down_revision: Union[str, None] = ('0031_paragraph_similarity', '0033_discussion_unit_cache')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
