"""add indexed legislation reference documents and sections"""

from alembic import op
import sqlalchemy as sa


revision = "0018_legislation_reference_docs"
down_revision = "0017_structured_legislation_cite"
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.create_table(
		"legislation_documents",
		sa.Column("id", sa.Integer(), nullable=False),
		sa.Column("instrument_key", sa.String(length=100), nullable=False),
		sa.Column("title", sa.Text(), nullable=False),
		sa.Column("citation", sa.Text(), nullable=True),
		sa.Column("source_url", sa.Text(), nullable=True),
		sa.Column("local_path", sa.Text(), nullable=True),
		sa.Column("source_hash", sa.String(length=64), nullable=True),
		sa.PrimaryKeyConstraint("id"),
		sa.UniqueConstraint("instrument_key"),
	)
	op.create_index("ix_legislation_documents_instrument_key", "legislation_documents", ["instrument_key"], unique=True)
	op.create_table(
		"legislation_sections",
		sa.Column("id", sa.Integer(), nullable=False),
		sa.Column("document_id", sa.Integer(), nullable=False),
		sa.Column("section_number", sa.String(length=100), nullable=False),
		sa.Column("label", sa.Text(), nullable=True),
		sa.Column("text", sa.Text(), nullable=False),
		sa.Column("display_order", sa.Integer(), nullable=False),
		sa.ForeignKeyConstraint(["document_id"], ["legislation_documents.id"], ondelete="CASCADE"),
		sa.PrimaryKeyConstraint("id"),
	)
	op.create_index("ix_legislation_sections_document_id", "legislation_sections", ["document_id"])
	op.create_index("ix_legislation_sections_section_number", "legislation_sections", ["section_number"])


def downgrade() -> None:
	op.drop_index("ix_legislation_sections_section_number", table_name="legislation_sections")
	op.drop_index("ix_legislation_sections_document_id", table_name="legislation_sections")
	op.drop_table("legislation_sections")
	op.drop_index("ix_legislation_documents_instrument_key", table_name="legislation_documents")
	op.drop_table("legislation_documents")