"""add derived FC activity classifications

Revision ID: 0015_fc_activity_classifications
Revises: 0014_judge_profiles
Create Date: 2026-08-21 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


revision = "0015_fc_activity_classifications"
down_revision = "0014_judge_profiles"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "fc_activity_classifications",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("source_case_id", sa.Integer(), nullable=False),
        sa.Column("source_key", sa.String(length=255), nullable=False),
        sa.Column("imm_number", sa.String(length=255), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("case_name", sa.Text(), nullable=True),
        sa.Column("date_filed", sa.Date(), nullable=True),
        sa.Column("city_filed", sa.String(length=255), nullable=True),
        sa.Column("nature", sa.Text(), nullable=True),
        sa.Column("case_class", sa.String(length=120), nullable=True),
        sa.Column("track", sa.String(length=120), nullable=True),
        sa.Column("source_url", sa.String(length=2048), nullable=True),
        sa.Column("scraped_timestamp", sa.DateTime(timezone=True), nullable=True),
        sa.Column("classification_json", sa.JSON(), nullable=False),
        sa.Column("classifier_version", sa.String(length=80), nullable=False),
        sa.Column("classified_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["source_case_id"], ["fc_activity_cases.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("source_case_id"),
    )
    op.create_index("ix_fc_activity_classifications_source_case_id", "fc_activity_classifications", ["source_case_id"])
    op.create_index("ix_fc_activity_classifications_source_key", "fc_activity_classifications", ["source_key"])
    op.create_index("ix_fc_activity_classifications_imm_number", "fc_activity_classifications", ["imm_number"])
    op.create_index("ix_fc_activity_classifications_year", "fc_activity_classifications", ["year"])
    op.create_index("ix_fc_activity_classifications_date_filed", "fc_activity_classifications", ["date_filed"])


def downgrade() -> None:
    op.drop_index("ix_fc_activity_classifications_date_filed", table_name="fc_activity_classifications")
    op.drop_index("ix_fc_activity_classifications_year", table_name="fc_activity_classifications")
    op.drop_index("ix_fc_activity_classifications_imm_number", table_name="fc_activity_classifications")
    op.drop_index("ix_fc_activity_classifications_source_key", table_name="fc_activity_classifications")
    op.drop_index("ix_fc_activity_classifications_source_case_id", table_name="fc_activity_classifications")
    op.drop_table("fc_activity_classifications")
