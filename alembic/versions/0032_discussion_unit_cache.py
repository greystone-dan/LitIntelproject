"""Add discussion unit cache table with method versioning for batch jobs.

Revision ID: 0032_discussion_unit_cache
Revises: 0030_full_paragraph_ivfflat
Create Date: 2026-10-03 13:30:00.000000
"""

from alembic import op
import sqlalchemy as sa


revision = "0032_discussion_unit_cache"
down_revision = "0031_statute_library_schema"
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.create_table(
		"discussion_unit_cache",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("case_id", sa.Integer(), nullable=False),
		sa.Column("method_version", sa.String(length=100), nullable=False),
		sa.Column("units_json", sa.Text(), nullable=False),
		sa.Column("total_units", sa.Integer(), nullable=False, server_default="0"),
		sa.Column("total_subthemes", sa.Integer(), nullable=False, server_default="0"),
		sa.Column("computed_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
		sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
		sa.ForeignKeyConstraint(["case_id"], ["cases.id"], ondelete="CASCADE"),
		sa.UniqueConstraint("case_id", "method_version", name="uq_discussion_unit_cache_version"),
	)
	op.create_index("ix_discussion_unit_cache_case_id", "discussion_unit_cache", ["case_id"])
	op.create_index("ix_discussion_unit_cache_method_version", "discussion_unit_cache", ["method_version"])


def downgrade() -> None:
	for index in (
		"ix_discussion_unit_cache_method_version",
		"ix_discussion_unit_cache_case_id",
	):
		op.drop_index(index, table_name="discussion_unit_cache")
	op.drop_table("discussion_unit_cache")
