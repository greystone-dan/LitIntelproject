"""Add standalone citation refinement tables.

Revision ID: 0039_citation_refinement
Revises: 0038_search_indexes
Create Date: 2026-10-05
"""

import sqlalchemy as sa
from alembic import op


revision = "0039_citation_refinement"
down_revision = "0038_search_indexes"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing_tables = set(inspector.get_table_names())

    if "citations_refined" not in existing_tables:
        op.create_table(
            "citations_refined",
            sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
            sa.Column("source_case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
            sa.Column("target_case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=True),
            sa.Column("citation_kind", sa.String(20), nullable=False, server_default="unknown"),
            sa.Column("citation_text", sa.Text(), nullable=True),
            sa.Column("normalized_citation", sa.Text(), nullable=True),
            sa.Column("anchor_citation_text", sa.Text(), nullable=True),
            sa.Column("anchor_offset_start", sa.Integer(), nullable=True),
            sa.Column("anchor_offset_end", sa.Integer(), nullable=True),
            sa.Column("declared_alias", sa.String(255), nullable=True),
            sa.Column("target_paragraph", sa.Integer(), nullable=True),
            sa.Column("target_chunk_id", sa.Integer(), sa.ForeignKey("case_chunks.id", ondelete="SET NULL"), nullable=True),
            sa.Column("provenance", sa.String(20), nullable=False, server_default="local"),
            sa.Column("chunk_id", sa.Integer(), sa.ForeignKey("case_chunks.id", ondelete="SET NULL"), nullable=True),
            sa.Column("offset_start", sa.Integer(), nullable=True),
            sa.Column("offset_end", sa.Integer(), nullable=True),
            sa.Column("unresolved", sa.Boolean(), nullable=False, default=False),
            sa.Column("refine_step", sa.String(50), nullable=True),
            sa.Column("confidence", sa.Float(), nullable=True),
            sa.Column("refine_version", sa.Integer(), nullable=False),
            sa.Column("source_citation_id", sa.Integer(), nullable=True),
        )
        op.create_index("ix_citations_refined_source_case_id", "citations_refined", ["source_case_id"])

    if "citation_paragraph_links" not in existing_tables:
        op.create_table(
            "citation_paragraph_links",
            sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
            sa.Column("refined_citation_id", sa.Integer(), sa.ForeignKey("citations_refined.id", ondelete="CASCADE"), nullable=False),
            sa.Column("target_case_id", sa.Integer(), nullable=True),
            sa.Column("target_paragraph", sa.Integer(), nullable=False),
            sa.Column("link_status", sa.String(50), nullable=False),
        )

    if "statute_references_refined" not in existing_tables:
        op.create_table(
            "statute_references_refined",
            sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
            sa.Column("source_case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
            sa.Column("chunk_id", sa.Integer(), sa.ForeignKey("case_chunks.id", ondelete="SET NULL"), nullable=True),
            sa.Column("statute_version_id", sa.Integer(), sa.ForeignKey("statute_versions.id", ondelete="SET NULL"), nullable=True),
            sa.Column("offset_start", sa.Integer(), nullable=True),
            sa.Column("offset_end", sa.Integer(), nullable=True),
            sa.Column("reference_text", sa.Text(), nullable=True),
            sa.Column("normalized_reference", sa.Text(), nullable=True),
            sa.Column("instrument_key", sa.String(100), nullable=True),
            sa.Column("pinpoint", sa.String(255), nullable=True),
            sa.Column("provision_section", sa.String(50), nullable=True),
            sa.Column("provision_subsection", sa.String(50), nullable=True),
            sa.Column("provision_paragraph", sa.String(50), nullable=True),
            sa.Column("provision_nested_depth", sa.Integer(), nullable=True),
            sa.Column("provision_is_range_or_list", sa.Boolean(), nullable=False, default=False),
            sa.Column("legislation_url", sa.Text(), nullable=True),
            sa.Column("section_text", sa.Text(), nullable=True),
            sa.Column("reference_kind", sa.String(20), nullable=False),
            sa.Column("refine_step", sa.String(50), nullable=True),
            sa.Column("confidence", sa.Float(), nullable=True),
            sa.Column("group_start", sa.Integer(), nullable=True),
            sa.Column("group_end", sa.Integer(), nullable=True),
            sa.Column("group_index", sa.Integer(), nullable=True),
            sa.Column("refine_version", sa.Integer(), nullable=False),
        )
        op.create_index(
            "ix_statute_references_refined_source_case_id",
            "statute_references_refined",
            ["source_case_id"],
        )

    if "citation_refine_status" not in existing_tables:
        op.create_table(
            "citation_refine_status",
            sa.Column("source_case_id", sa.Integer(), primary_key=True, nullable=False),
            sa.Column("refine_version", sa.Integer(), nullable=False),
            sa.Column("status", sa.String(50), nullable=False),
            sa.Column("processed_at", sa.DateTime(timezone=True), nullable=True),
            sa.Column("case_rows", sa.Integer(), nullable=False),
            sa.Column("statute_rows", sa.Integer(), nullable=False),
        )


def downgrade() -> None:
    # Tables may pre-exist this migration. Preserve their schema and refinement
    # data because a downgrade cannot distinguish pre-existing tables from new ones.
    pass
