"""Add provenance and ingestion tracking tables for canonical case inventory."""

from alembic import op
import sqlalchemy as sa

revision = "0008_case_provenance_tables"
down_revision = "0007_fc_procedural_history"
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.create_table(
		"case_sources",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("case_id", sa.Integer(), nullable=False),
		sa.Column("source_type", sa.String(length=100), nullable=False),
		sa.Column("source_name", sa.String(length=255), nullable=True),
		sa.Column("source_id", sa.String(length=255), nullable=True),
		sa.Column("source_url", sa.String(length=2048), nullable=True),
		sa.Column("dataset_version", sa.String(length=100), nullable=True),
		sa.Column("upstream_license", sa.Text(), nullable=True),
		sa.Column("scraped_at", sa.DateTime(timezone=True), nullable=True),
		sa.Column("is_primary", sa.Boolean(), nullable=False, server_default=sa.text("false")),
		sa.Column("raw_hash", sa.String(length=64), nullable=True),
		sa.Column("metadata_json", sa.JSON(), nullable=True),
		sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
		sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
		sa.ForeignKeyConstraint(["case_id"], ["cases.id"], ondelete="CASCADE"),
	)
	op.create_index("ix_case_sources_case_id", "case_sources", ["case_id"])
	op.create_index("ix_case_sources_source_type", "case_sources", ["source_type"])
	op.create_index("ix_case_sources_raw_hash", "case_sources", ["raw_hash"])

	op.create_table(
		"ingestion_runs",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("source_type", sa.String(length=100), nullable=False),
		sa.Column("source_name", sa.String(length=255), nullable=True),
		sa.Column("run_type", sa.String(length=50), nullable=False),
		sa.Column("status", sa.String(length=30), nullable=False, server_default="started"),
		sa.Column("started_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
		sa.Column("finished_at", sa.DateTime(timezone=True), nullable=True),
		sa.Column("records_seen", sa.Integer(), nullable=True),
		sa.Column("records_ingested", sa.Integer(), nullable=True),
		sa.Column("records_updated", sa.Integer(), nullable=True),
		sa.Column("records_failed", sa.Integer(), nullable=True),
		sa.Column("metadata_json", sa.JSON(), nullable=True),
	)
	op.create_index("ix_ingestion_runs_source_type", "ingestion_runs", ["source_type"])
	op.create_index("ix_ingestion_runs_run_type", "ingestion_runs", ["run_type"])
	op.create_index("ix_ingestion_runs_status", "ingestion_runs", ["status"])

	op.execute(
		"""
		INSERT INTO case_sources (
			case_id,
			source_type,
			source_name,
			source_id,
			source_url,
			dataset_version,
			upstream_license,
			scraped_at,
			is_primary,
			metadata_json,
			created_at,
			updated_at
		)
		SELECT
			id,
			COALESCE(source_type, 'unknown'),
			source_name,
			source_id,
			source_url,
			dataset_version,
			upstream_license,
			scraped_at,
			true,
			metadata_json,
			created_at,
			created_at
		FROM cases
		WHERE
			COALESCE(source_type, '') <> ''
			OR source_name IS NOT NULL
			OR source_id IS NOT NULL
			OR source_url IS NOT NULL
			OR dataset_version IS NOT NULL
			OR upstream_license IS NOT NULL
			OR scraped_at IS NOT NULL
			OR metadata_json IS NOT NULL
		"""
	)


def downgrade() -> None:
	op.drop_index("ix_ingestion_runs_status", table_name="ingestion_runs")
	op.drop_index("ix_ingestion_runs_run_type", table_name="ingestion_runs")
	op.drop_index("ix_ingestion_runs_source_type", table_name="ingestion_runs")
	op.drop_table("ingestion_runs")
	op.drop_index("ix_case_sources_raw_hash", table_name="case_sources")
	op.drop_index("ix_case_sources_source_type", table_name="case_sources")
	op.drop_index("ix_case_sources_case_id", table_name="case_sources")
	op.drop_table("case_sources")
