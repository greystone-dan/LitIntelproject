"""Add paragraph_note_links ("possibly the same point" links between paragraph notes). Additive only.

Undo: DROP TABLE paragraph_note_links;  (or alembic downgrade 0048_paragraph_notes).

Revision ID: 0049_note_links
Revises: 0048_paragraph_notes
"""

from alembic import op
import sqlalchemy as sa

revision = "0049_note_links"
down_revision = "0048_paragraph_notes"
branch_labels = None
depends_on = None


def upgrade() -> None:
	if "paragraph_note_links" in set(sa.inspect(op.get_bind()).get_table_names()):
		return
	op.create_table(
		"paragraph_note_links",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
		sa.Column("para", sa.Integer(), nullable=False),
		sa.Column("other_case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
		sa.Column("other_para", sa.Integer(), nullable=False),
		sa.Column("score", sa.Integer(), nullable=False),
		sa.Column("source", sa.String(40), nullable=False),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.UniqueConstraint("case_id", "para", "other_case_id", "other_para", name="uq_note_link_pair"),
	)
	op.create_index("ix_paragraph_note_links_case_id", "paragraph_note_links", ["case_id"])


def downgrade() -> None:
	if "paragraph_note_links" in set(sa.inspect(op.get_bind()).get_table_names()):
		op.drop_table("paragraph_note_links")
