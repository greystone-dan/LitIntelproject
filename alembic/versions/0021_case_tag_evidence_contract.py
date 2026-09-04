"""Preserve V3 tag rule, language, role, and optional chunk provenance."""

from alembic import op
import sqlalchemy as sa


revision = "0021_case_tag_evidence_contract"
down_revision = "0020_tag_occurrence_identity"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "case_tags",
        sa.Column("chunk_id", sa.Integer(), nullable=True),
    )
    op.create_foreign_key(
        "fk_case_tags_chunk_id",
        "case_tags",
        "case_chunks",
        ["chunk_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_index("ix_case_tags_chunk_id", "case_tags", ["chunk_id"])
    op.add_column("case_tags", sa.Column("rule_id", sa.String(length=150), nullable=True))
    op.create_index("ix_case_tags_rule_id", "case_tags", ["rule_id"])
    op.add_column(
        "case_tags",
        sa.Column("language", sa.String(length=16), nullable=False, server_default="unknown"),
    )
    op.create_index("ix_case_tags_language", "case_tags", ["language"])
    op.add_column(
        "case_tags",
        sa.Column("evidence_role", sa.String(length=30), nullable=False, server_default="mention"),
    )
    op.create_index("ix_case_tags_evidence_role", "case_tags", ["evidence_role"])


def downgrade() -> None:
    op.drop_index("ix_case_tags_evidence_role", table_name="case_tags")
    op.drop_column("case_tags", "evidence_role")
    op.drop_index("ix_case_tags_language", table_name="case_tags")
    op.drop_column("case_tags", "language")
    op.drop_index("ix_case_tags_rule_id", table_name="case_tags")
    op.drop_column("case_tags", "rule_id")
    op.drop_index("ix_case_tags_chunk_id", table_name="case_tags")
    op.drop_constraint("fk_case_tags_chunk_id", "case_tags", type_="foreignkey")
    op.drop_column("case_tags", "chunk_id")