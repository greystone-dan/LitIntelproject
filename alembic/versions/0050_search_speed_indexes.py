"""Add two search-speed indexes on cases. Additive only; each takes a second or two on 75k rows.

- ix_cases_date_id_desc matches "ORDER BY date DESC NULLS LAST, id DESC" (the default search order), which the
  plain date index cannot serve, so every unfiltered search sorted all decisions.
- ix_cases_title_folded_trgm serves the accent-insensitive title match ("Dore" finds "Doré").

Undo: DROP INDEX ix_cases_date_id_desc; DROP INDEX ix_cases_title_folded_trgm;

Revision ID: 0050_search_speed_indexes
Revises: 0049_note_links
"""

from alembic import op

revision = "0050_search_speed_indexes"
down_revision = "0049_note_links"
branch_labels = None
depends_on = None

FOLDED = "translate(lower(title), 'àâäãçéèêëìîïñòôöõùûüÿ', 'aaaaceeeeiiinoooouuuy')"


def upgrade() -> None:
	if op.get_bind().dialect.name != "postgresql":
		return
	op.execute("CREATE INDEX IF NOT EXISTS ix_cases_date_id_desc ON cases (date DESC NULLS LAST, id DESC)")
	op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
	op.execute(f"CREATE INDEX IF NOT EXISTS ix_cases_title_folded_trgm ON cases USING gin (({FOLDED}) gin_trgm_ops)")


def downgrade() -> None:
	if op.get_bind().dialect.name != "postgresql":
		return
	op.execute("DROP INDEX IF EXISTS ix_cases_title_folded_trgm")
	op.execute("DROP INDEX IF EXISTS ix_cases_date_id_desc")
