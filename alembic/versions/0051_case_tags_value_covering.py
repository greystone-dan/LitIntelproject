"""Add one covering index on case_tags so a topic-tag search reads an index instead of ~30,000 table pages.

The topic-tag branch of case search runs
    SELECT case_id FROM case_tags WHERE taxonomy_version = :v AND value IN (...)
For a broad topic ("reasonableness": 78,662 tag rows) the planner reads the value index, then visits about 30,000
table pages to check the taxonomy version and fetch case_id. This index holds all three columns, so the lookup can
be answered from the index alone. Additive only; built CONCURRENTLY (no write lock on case_tags).

Undo: DROP INDEX CONCURRENTLY IF EXISTS ix_case_tags_value_version_covering;  (or alembic downgrade)

Revision ID: 0051_case_tags_value_covering
Revises: 0050_search_speed_indexes
"""

from alembic import op

revision = "0051_case_tags_value_covering"
down_revision = "0050_search_speed_indexes"
branch_labels = None
depends_on = None


def upgrade() -> None:
	if op.get_bind().dialect.name != "postgresql":
		return
	with op.get_context().autocommit_block():
		op.execute(
			"CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_case_tags_value_version_covering "
			"ON case_tags (value, taxonomy_version) INCLUDE (case_id)"
		)


def downgrade() -> None:
	if op.get_bind().dialect.name != "postgresql":
		return
	with op.get_context().autocommit_block():
		op.execute("DROP INDEX CONCURRENTLY IF EXISTS ix_case_tags_value_version_covering")
