"""Allow multiple V2 occurrences of the same canonical tag per case."""

from alembic import op
import sqlalchemy as sa


revision = "0020_tag_occurrence_identity"
down_revision = "0019_case_tag_offsets"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint("uq_case_tag_taxonomy", "case_tags", type_="unique")
    op.create_unique_constraint(
        "uq_case_tag_taxonomy",
        "case_tags",
        ["case_id", "category", "value", "offset_start", "offset_end", "taxonomy_version"],
    )


def downgrade() -> None:
    op.drop_constraint("uq_case_tag_taxonomy", "case_tags", type_="unique")
    op.create_unique_constraint(
        "uq_case_tag_taxonomy",
        "case_tags",
        ["case_id", "category", "value", "taxonomy_version"],
    )