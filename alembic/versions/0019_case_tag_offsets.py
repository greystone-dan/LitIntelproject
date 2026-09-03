"""Add source offsets to evidence-bearing case tags."""

from alembic import op
import sqlalchemy as sa


revision = "0019_case_tag_offsets"
down_revision = "0018_legislation_reference_docs"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("case_tags", sa.Column("offset_start", sa.Integer(), nullable=True))
    op.add_column("case_tags", sa.Column("offset_end", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("case_tags", "offset_end")
    op.drop_column("case_tags", "offset_start")