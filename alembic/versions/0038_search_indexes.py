"""Add case search indexes (trigram on title and citation, court+date).

Revision ID: 0038_search_indexes
Revises: 0037_cases_docket_number
Create Date: 2026-10-05

Additive and idempotent: the live database already has these indexes (built by
hand), and IF NOT EXISTS makes this a no-op there. Only the title/citation
trigram indexes are created here; a full_text index is far too heavy for a
normal deploy migration and is deliberately not included.
"""

from alembic import op


revision = "0038_search_indexes"
down_revision = "0037_cases_docket_number"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    if bind.dialect.name != "postgresql":
        return
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
    op.execute("CREATE INDEX IF NOT EXISTS ix_cases_title_trgm ON cases USING gin (title gin_trgm_ops)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_cases_citation_trgm ON cases USING gin (citation gin_trgm_ops)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_cases_court_date ON cases (court, date)")


def downgrade() -> None:
    # Indexes may pre-exist this migration; leave them in place.
    pass
