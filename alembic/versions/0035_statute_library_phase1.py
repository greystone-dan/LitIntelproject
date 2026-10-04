"""Add statute library with point-in-time versioning for Phase 1 (federal laws)

Revision ID: 0035_statute_library_phase1
Revises: 0034_merge_similarity_main
Create Date: 2026-10-03 12:45:00.000000
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import LargeBinary


revision = "0035_statute_library_phase1"
down_revision = "0034_merge_similarity_main"
branch_labels = None
depends_on = None


def upgrade() -> None:
	# Create statutes table
	op.create_table(
		"statutes",
		sa.Column("id", sa.Integer(), nullable=False),
		sa.Column("instrument_key", sa.String(100), nullable=False, unique=True),
		sa.Column("title", sa.Text(), nullable=False),
		sa.Column("short_title", sa.String(255), nullable=True),
		sa.Column("jurisdiction", sa.String(100), nullable=False),
		sa.Column("statute_type", sa.String(50), nullable=False),  # Act, Regulation, Rules
		sa.Column("consolidated_year", sa.Integer(), nullable=True),
		sa.Column("source", sa.String(100), nullable=False),  # justice_laws_xml, canlii, huggingface
		sa.Column("source_url", sa.Text(), nullable=True),
		sa.Column("license", sa.String(100), nullable=True),  # OGL, CC-BY-NC, etc.
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.PrimaryKeyConstraint("id"),
		sa.UniqueConstraint("instrument_key", name="uq_statute_instrument_key"),
	)
	op.create_index("ix_statute_instrument_key", "statutes", ["instrument_key"])
	op.create_index("ix_statute_jurisdiction", "statutes", ["jurisdiction"])
	op.create_index("ix_statute_source", "statutes", ["source"])

	# Create statute_versions table
	op.create_table(
		"statute_versions",
		sa.Column("id", sa.Integer(), nullable=False),
		sa.Column("statute_id", sa.Integer(), nullable=False),
		sa.Column("version_number", sa.String(50), nullable=False),
		sa.Column("in_force_date", sa.Date(), nullable=False),
		sa.Column("end_date", sa.Date(), nullable=True),
		sa.Column("full_text", sa.Text(), nullable=True),
		sa.Column("text_compressed", LargeBinary(), nullable=True),  # gzip for large text
		sa.Column("source_url", sa.Text(), nullable=True),
		sa.Column("fetched_at", sa.DateTime(timezone=True), nullable=True),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.PrimaryKeyConstraint("id"),
		sa.ForeignKeyConstraint(["statute_id"], ["statutes.id"], ondelete="CASCADE"),
		sa.UniqueConstraint("statute_id", "in_force_date", name="uq_statute_version_date"),
	)
	op.create_index("ix_statute_version_statute_id", "statute_versions", ["statute_id"])
	op.create_index("ix_statute_version_in_force_date", "statute_versions", ["statute_id", "in_force_date"])
	op.create_index("ix_statute_version_date_range", "statute_versions", ["statute_id", "in_force_date", "end_date"])

	# Create statute_sections table
	op.create_table(
		"statute_sections",
		sa.Column("id", sa.Integer(), nullable=False),
		sa.Column("statute_version_id", sa.Integer(), nullable=False),
		sa.Column("section_number", sa.String(50), nullable=False),
		sa.Column("subsection", sa.String(50), nullable=True),
		sa.Column("paragraph", sa.String(50), nullable=True),
		sa.Column("heading", sa.Text(), nullable=True),
		sa.Column("text", sa.Text(), nullable=True),
		sa.Column("offset_start", sa.Integer(), nullable=True),
		sa.Column("offset_end", sa.Integer(), nullable=True),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.PrimaryKeyConstraint("id"),
		sa.ForeignKeyConstraint(["statute_version_id"], ["statute_versions.id"], ondelete="CASCADE"),
	)
	op.create_index("ix_statute_section_version_id", "statute_sections", ["statute_version_id"])
	op.create_index("ix_statute_section_lookup", "statute_sections", ["statute_version_id", "section_number", "subsection"])

	# Extend statute_references table to link to specific statute versions
	op.add_column(
		"statute_references",
		sa.Column("statute_version_id", sa.Integer(), nullable=True),
	)
	op.add_column(
		"statute_references",
		sa.Column("section_text", sa.Text(), nullable=True),
	)
	op.create_foreign_key(
		"fk_statute_references_statute_version",
		"statute_references",
		"statute_versions",
		["statute_version_id"],
		["id"],
		ondelete="SET NULL",
	)
	op.create_index("ix_statute_references_statute_version_id", "statute_references", ["statute_version_id"])


def downgrade() -> None:
	# Drop foreign key and columns from statute_references
	op.drop_index("ix_statute_references_statute_version_id", table_name="statute_references")
	op.drop_constraint("fk_statute_references_statute_version", "statute_references", type_="foreignkey")
	op.drop_column("statute_references", "section_text")
	op.drop_column("statute_references", "statute_version_id")

	# Drop statute_sections table
	op.drop_index("ix_statute_section_lookup", table_name="statute_sections")
	op.drop_index("ix_statute_section_version_id", table_name="statute_sections")
	op.drop_table("statute_sections")

	# Drop statute_versions table
	op.drop_index("ix_statute_version_date_range", table_name="statute_versions")
	op.drop_index("ix_statute_version_in_force_date", table_name="statute_versions")
	op.drop_index("ix_statute_version_statute_id", table_name="statute_versions")
	op.drop_table("statute_versions")

	# Drop statutes table
	op.drop_index("ix_statute_source", table_name="statutes")
	op.drop_index("ix_statute_jurisdiction", table_name="statutes")
	op.drop_index("ix_statute_instrument_key", table_name="statutes")
	op.drop_table("statutes")
