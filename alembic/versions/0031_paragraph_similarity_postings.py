"""Indexes for bounded paragraph similarity postings (no data rewrite)."""
from alembic import op

revision = "0031_paragraph_similarity"
down_revision = "0030_full_paragraph_ivfflat"
branch_labels = None
depends_on = None

INDEXES = (
    ("ix_similarity_paragraph", "case_chunks", ["case_id", "chunk_set", "paragraph_start", "id"]),
    ("ix_similarity_tag_posting", "case_tags", ["taxonomy_version", "category", "value", "case_id", "id"]),
    ("ix_similarity_tag_source", "case_tags", ["case_id", "taxonomy_version", "id"]),
    ("ix_similarity_authority_posting", "citations", ["target_case_id", "source_case_id", "id"]),
    ("ix_similarity_unresolved_posting", "citations", ["normalized_citation", "source_case_id", "id"]),
    ("ix_similarity_citation_source", "citations", ["source_case_id", "id"]),
)


def upgrade():
    for name, table, columns in INDEXES:
        op.create_index(name, table, columns)


def downgrade():
    for name, table, _ in reversed(INDEXES):
        op.drop_index(name, table_name=table)
