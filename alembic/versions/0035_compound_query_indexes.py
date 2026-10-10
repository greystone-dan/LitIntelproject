"""Add compound indexes for common multi-column filter queries.

These indexes optimize frequent filtering patterns without data migration:
- case_tags(case_id, category) for case detail pages
- case_tags(category, taxonomy_version) for tag search/filter
- case_chunks(case_id, chunk_set) for case text retrieval
- citations(source_case_id, target_case_id) for citation lookups

Revision ID: 0035_compound_query_indexes
Revises: 0034_merge_similarity_main
Create Date: 2026-10-04 00:00:00.000000
"""

from alembic import op

revision = "0035_compound_query_indexes"
down_revision = "0034_merge_similarity_main"
branch_labels = None
depends_on = None

INDEXES = (
    ("idx_case_tags_case_cat", "case_tags", ["case_id", "category"]),
    ("idx_case_tags_cat_taxonomy", "case_tags", ["category", "taxonomy_version"]),
    ("idx_case_chunks_case_set", "case_chunks", ["case_id", "chunk_set"]),
    ("idx_citations_both", "citations", ["source_case_id", "target_case_id"]),
)


def upgrade():
    for name, table, columns in INDEXES:
        op.create_index(name, table, columns)


def downgrade():
    for name, table, _ in reversed(INDEXES):
        op.drop_index(name, table_name=table)
