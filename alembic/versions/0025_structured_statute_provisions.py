"""Add structured statute provision identity fields."""

from alembic import op
import sqlalchemy as sa


revision = "0025_structured_statute_prov"
down_revision = "0024_citation_target_paragraph"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("statute_references", sa.Column("provision_section", sa.String(length=50), nullable=True))
    op.add_column("statute_references", sa.Column("provision_subsection", sa.String(length=50), nullable=True))
    op.add_column("statute_references", sa.Column("provision_paragraph", sa.String(length=50), nullable=True))
    op.add_column("statute_references", sa.Column("provision_nested_depth", sa.Integer(), nullable=True))
    op.add_column("statute_references", sa.Column("provision_is_range_or_list", sa.Boolean(), nullable=False, server_default=sa.false()))
    op.create_index("ix_statute_references_provision_section", "statute_references", ["provision_section"])
    op.create_index("ix_statute_references_provision_subsection", "statute_references", ["provision_subsection"])
    op.create_index("ix_statute_references_provision_paragraph", "statute_references", ["provision_paragraph"])
    op.create_index("ix_statute_references_provision_is_range_or_list", "statute_references", ["provision_is_range_or_list"])


def downgrade() -> None:
    op.drop_index("ix_statute_references_provision_is_range_or_list", table_name="statute_references")
    op.drop_index("ix_statute_references_provision_paragraph", table_name="statute_references")
    op.drop_index("ix_statute_references_provision_subsection", table_name="statute_references")
    op.drop_index("ix_statute_references_provision_section", table_name="statute_references")
    op.drop_column("statute_references", "provision_is_range_or_list")
    op.drop_column("statute_references", "provision_nested_depth")
    op.drop_column("statute_references", "provision_paragraph")
    op.drop_column("statute_references", "provision_subsection")
    op.drop_column("statute_references", "provision_section")