"""Add issue_maps and issue_map_questions for Live Analysis issue matches. Additive only.

Undo: DROP TABLE issue_map_questions; DROP TABLE issue_maps; (or alembic downgrade 0044_refined_pinpoints).

Revision ID: 0045_issue_maps
Revises: 0044_refined_pinpoints
Create Date: 2026-10-10
"""

import sqlalchemy as sa
from alembic import op


revision = "0045_issue_maps"
down_revision = "0044_refined_pinpoints"
branch_labels = None
depends_on = None


def upgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    tables = set(inspector.get_table_names())
    if "issue_maps" not in tables:
        op.create_table(
            "issue_maps",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("source_key", sa.String(60), nullable=False),
            sa.Column("issue_no", sa.Integer(), nullable=False),
            sa.Column("case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="SET NULL"), nullable=True),
            sa.Column("citation", sa.String(120), nullable=True),
            sa.Column("court", sa.String(20), nullable=True),
            sa.Column("issue", sa.Text(), nullable=False),
            sa.Column("text", sa.Text(), nullable=False),
            sa.Column("result", sa.String(30), nullable=False),
            sa.Column("result_para", sa.Integer(), nullable=True),
            sa.Column("soften", sa.Text(), nullable=True),
            sa.Column("result_paragraph", sa.Text(), nullable=True),
            sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
            sa.UniqueConstraint("source_key", "issue_no", name="uq_issue_map_source_issue"),
        )
        op.create_index("ix_issue_maps_source_key", "issue_maps", ["source_key"])
        op.create_index("ix_issue_maps_case_id", "issue_maps", ["case_id"])
    if "issue_map_questions" not in tables:
        op.create_table(
            "issue_map_questions",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("issue_map_id", sa.Integer(), sa.ForeignKey("issue_maps.id", ondelete="CASCADE"), nullable=False),
            sa.Column("position", sa.Integer(), server_default="0", nullable=False),
            sa.Column("question", sa.Text(), nullable=False),
        )
        op.create_index("ix_issue_map_questions_issue_map_id", "issue_map_questions", ["issue_map_id"])


def downgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    tables = set(inspector.get_table_names())
    if "issue_map_questions" in tables:
        op.drop_table("issue_map_questions")
    if "issue_maps" in tables:
        op.drop_table("issue_maps")
