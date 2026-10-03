"""add saved searches and alerts tables

Revision ID: 0031_saved_searches_alerts
Revises: 0030_full_paragraph_ivfflat
Create Date: 2026-10-03 13:00:00.000000

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0031_saved_searches_alerts"
down_revision = "0030_full_paragraph_ivfflat"
branch_labels = None
depends_on = None


def upgrade() -> None:
	# Create saved_searches table
	op.create_table(
		"saved_searches",
		sa.Column("id", sa.Integer(), nullable=False),
		sa.Column("name", sa.String(255), nullable=False),
		sa.Column("description", sa.Text(), nullable=True),
		sa.Column("query", sa.Text(), nullable=False),
		sa.Column("search_mode", sa.String(20), nullable=False),
		sa.Column("filters", postgresql.JSON(), nullable=False),
		sa.Column(
			"last_alert_check",
			sa.DateTime(timezone=True),
			nullable=True,
		),
		sa.Column(
			"created_at",
			sa.DateTime(timezone=True),
			server_default=sa.func.now(),
			nullable=False,
		),
		sa.Column(
			"updated_at",
			sa.DateTime(timezone=True),
			server_default=sa.func.now(),
			onupdate=sa.func.now(),
			nullable=False,
		),
		sa.PrimaryKeyConstraint("id"),
	)
	op.create_index("ix_saved_searches_name", "saved_searches", ["name"])
	op.create_index("ix_saved_searches_created_at", "saved_searches", ["created_at"])

	# Create search_alerts table
	op.create_table(
		"search_alerts",
		sa.Column("id", sa.Integer(), nullable=False),
		sa.Column("search_id", sa.Integer(), nullable=False),
		sa.Column("case_id", sa.Integer(), nullable=False),
		sa.Column("chunk_id", sa.Integer(), nullable=True),
		sa.Column("match_type", sa.String(50), nullable=False),
		sa.Column("relevance_score", sa.Float(), nullable=True),
		sa.Column(
			"discovered_at",
			sa.DateTime(timezone=True),
			server_default=sa.func.now(),
			nullable=False,
		),
		sa.Column(
			"created_at",
			sa.DateTime(timezone=True),
			server_default=sa.func.now(),
			nullable=False,
		),
		sa.ForeignKeyConstraint(["search_id"], ["saved_searches.id"], ondelete="CASCADE"),
		sa.ForeignKeyConstraint(["case_id"], ["cases.id"], ondelete="CASCADE"),
		sa.ForeignKeyConstraint(["chunk_id"], ["case_chunks.id"], ondelete="CASCADE"),
		sa.PrimaryKeyConstraint("id"),
	)
	op.create_index("ix_search_alerts_search_id", "search_alerts", ["search_id"])
	op.create_index("ix_search_alerts_case_id", "search_alerts", ["case_id"])
	op.create_index("ix_search_alerts_discovered_at", "search_alerts", ["discovered_at"])

	# Create fc_activity_alerts table
	op.create_table(
		"fc_activity_alerts",
		sa.Column("id", sa.Integer(), nullable=False),
		sa.Column("search_id", sa.Integer(), nullable=False),
		sa.Column("case_id", sa.Integer(), nullable=False),
		sa.Column("entry_type", sa.String(100), nullable=False),
		sa.Column(
			"discovered_at",
			sa.DateTime(timezone=True),
			server_default=sa.func.now(),
			nullable=False,
		),
		sa.Column(
			"created_at",
			sa.DateTime(timezone=True),
			server_default=sa.func.now(),
			nullable=False,
		),
		sa.ForeignKeyConstraint(["search_id"], ["saved_searches.id"], ondelete="CASCADE"),
		sa.ForeignKeyConstraint(["case_id"], ["fc_activity_cases.id"], ondelete="CASCADE"),
		sa.PrimaryKeyConstraint("id"),
	)
	op.create_index("ix_fc_activity_alerts_search_id", "fc_activity_alerts", ["search_id"])
	op.create_index("ix_fc_activity_alerts_discovered_at", "fc_activity_alerts", ["discovered_at"])


def downgrade() -> None:
	op.drop_index("ix_fc_activity_alerts_discovered_at", table_name="fc_activity_alerts")
	op.drop_index("ix_fc_activity_alerts_search_id", table_name="fc_activity_alerts")
	op.drop_table("fc_activity_alerts")
	op.drop_index("ix_search_alerts_discovered_at", table_name="search_alerts")
	op.drop_index("ix_search_alerts_case_id", table_name="search_alerts")
	op.drop_index("ix_search_alerts_search_id", table_name="search_alerts")
	op.drop_table("search_alerts")
	op.drop_index("ix_saved_searches_created_at", table_name="saved_searches")
	op.drop_index("ix_saved_searches_name", table_name="saved_searches")
	op.drop_table("saved_searches")
