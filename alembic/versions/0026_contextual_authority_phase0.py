"""Add additive contextual authority Phase 0 tables."""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0026_contextual_authority_p0"
down_revision = "0025_structured_statute_prov"
branch_labels = None
depends_on = None


def upgrade() -> None:
    uuid = postgresql.UUID(as_uuid=True)
    op.create_table(
        "contextual_snapshot",
        sa.Column("id", uuid, primary_key=True),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("code_sha", sa.String(length=64), nullable=False),
        sa.Column("method_set_version", sa.String(length=100), nullable=False),
        sa.Column("config", sa.JSON(), nullable=False),
        sa.Column("cohort_hash", sa.String(length=64), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_table(
        "contextual_active_snapshot",
        sa.Column("singleton", sa.Boolean(), primary_key=True, server_default=sa.true()),
        sa.Column("snapshot_id", uuid, sa.ForeignKey("contextual_snapshot.id"), nullable=True),
        sa.CheckConstraint("singleton = true", name="ck_contextual_active_singleton"),
    )
    op.create_table(
        "contextual_unit",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column("snapshot_id", uuid, sa.ForeignKey("contextual_snapshot.id", ondelete="CASCADE"), nullable=False),
        sa.Column("case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
        sa.Column("method", sa.String(length=80), nullable=False),
        sa.Column("method_version", sa.String(length=100), nullable=False),
        sa.Column("config_hash", sa.String(length=64), nullable=False),
        sa.Column("variant_key", sa.String(length=255), nullable=False),
        sa.Column("text_sha256", sa.String(length=64), nullable=False),
        sa.UniqueConstraint("snapshot_id", "case_id", "method", "variant_key", name="uq_contextual_unit_variant"),
    )
    op.create_index("ix_contextual_unit_snapshot_case", "contextual_unit", ["snapshot_id", "case_id"])
    op.create_table(
        "contextual_unit_segment",
        sa.Column("unit_id", sa.BigInteger(), sa.ForeignKey("contextual_unit.id", ondelete="CASCADE"), nullable=False),
        sa.Column("ordinal", sa.SmallInteger(), nullable=False),
        sa.Column("chunk_id", sa.Integer(), sa.ForeignKey("case_chunks.id", ondelete="CASCADE"), nullable=False),
        sa.Column("start_offset", sa.Integer(), nullable=False),
        sa.Column("end_offset", sa.Integer(), nullable=False),
        sa.Column("text_sha256", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint("unit_id", "ordinal"),
        sa.CheckConstraint("start_offset >= 0 AND start_offset < end_offset", name="ck_contextual_segment_offsets"),
    )
    op.create_table(
        "contextual_unit_citation",
        sa.Column("unit_id", sa.BigInteger(), sa.ForeignKey("contextual_unit.id", ondelete="CASCADE"), nullable=False),
        sa.Column("citation_occurrence_id", sa.Integer(), sa.ForeignKey("citations.id", ondelete="CASCADE"), nullable=False),
        sa.Column("membership_role", sa.String(length=30), nullable=False, server_default="contains"),
        sa.PrimaryKeyConstraint("unit_id", "citation_occurrence_id"),
    )
    op.create_table(
        "contextual_observation",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column("snapshot_id", uuid, sa.ForeignKey("contextual_snapshot.id", ondelete="CASCADE"), nullable=False),
        sa.Column("unit_id", sa.BigInteger(), sa.ForeignKey("contextual_unit.id", ondelete="CASCADE"), nullable=True),
        sa.Column("citation_occurrence_id", sa.Integer(), sa.ForeignKey("citations.id", ondelete="CASCADE"), nullable=True),
        sa.Column("target_authority_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="SET NULL"), nullable=True),
        sa.Column("kind", sa.String(length=40), nullable=False),
        sa.Column("label", sa.String(length=100), nullable=False),
        sa.Column("provenance_class", sa.String(length=30), nullable=False),
        sa.Column("method_version", sa.String(length=100), nullable=False),
        sa.Column("evidence_strength", sa.Float(), nullable=True),
        sa.Column("rule_agreement", sa.Float(), nullable=True),
        sa.Column("model_score", sa.Float(), nullable=True),
        sa.Column("confidence_tier", sa.String(length=5), nullable=False, server_default="U"),
        sa.Column("review_status", sa.String(length=20), nullable=False, server_default="unreviewed"),
    )
    op.create_index("ix_contextual_observation_snapshot_kind", "contextual_observation", ["snapshot_id", "kind"])
    op.create_table(
        "contextual_evidence_span",
        sa.Column("observation_id", sa.BigInteger(), sa.ForeignKey("contextual_observation.id", ondelete="CASCADE"), nullable=False),
        sa.Column("ordinal", sa.SmallInteger(), nullable=False),
        sa.Column("chunk_id", sa.Integer(), sa.ForeignKey("case_chunks.id", ondelete="CASCADE"), nullable=False),
        sa.Column("start_offset", sa.Integer(), nullable=False),
        sa.Column("end_offset", sa.Integer(), nullable=False),
        sa.Column("text_sha256", sa.String(length=64), nullable=False),
        sa.Column("quoted", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.PrimaryKeyConstraint("observation_id", "ordinal"),
        sa.CheckConstraint("start_offset >= 0 AND start_offset < end_offset", name="ck_contextual_evidence_offsets"),
    )
    op.create_table(
        "contextual_review",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column("observation_id", sa.BigInteger(), sa.ForeignKey("contextual_observation.id", ondelete="CASCADE"), nullable=False),
        sa.Column("reviewer_id", sa.String(length=255), nullable=True),
        sa.Column("decision", sa.String(length=30), nullable=False),
        sa.Column("corrected_label", sa.String(length=100), nullable=True),
        sa.Column("rationale", sa.Text(), nullable=True),
        sa.Column("reviewed_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("contextual_review")
    op.drop_table("contextual_evidence_span")
    op.drop_index("ix_contextual_observation_snapshot_kind", table_name="contextual_observation")
    op.drop_table("contextual_observation")
    op.drop_table("contextual_unit_citation")
    op.drop_table("contextual_unit_segment")
    op.drop_index("ix_contextual_unit_snapshot_case", table_name="contextual_unit")
    op.drop_table("contextual_unit")
    op.drop_table("contextual_active_snapshot")
    op.drop_table("contextual_snapshot")
