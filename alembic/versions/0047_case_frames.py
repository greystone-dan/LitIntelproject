"""Add case_frames for the simple pass-1 case frame. Additive only.

Undo: DROP TABLE case_frames; (or alembic downgrade 0046_paragraph_positions).

Revision ID: 0047_case_frames
Revises: 0046_paragraph_positions
Create Date: 2026-10-11
"""

import sqlalchemy as sa
from alembic import op


revision = "0047_case_frames"
down_revision = "0046_paragraph_positions"
branch_labels = None
depends_on = None


def upgrade() -> None:
	inspector = sa.inspect(op.get_bind())
	if "case_frames" in set(inspector.get_table_names()):
		return
	op.create_table(
		"case_frames",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
		sa.Column("version", sa.Integer(), server_default="1", nullable=False),
		sa.Column("frame", sa.JSON(), nullable=False),
		sa.Column("source", sa.String(40), nullable=False),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.UniqueConstraint("case_id", "version", name="uq_case_frame_case_version"),
	)
	op.create_index("ix_case_frames_case_id", "case_frames", ["case_id"])


def downgrade() -> None:
	inspector = sa.inspect(op.get_bind())
	if "case_frames" in set(inspector.get_table_names()):
		op.drop_table("case_frames")
