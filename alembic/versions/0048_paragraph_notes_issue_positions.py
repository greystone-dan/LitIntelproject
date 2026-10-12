"""Add paragraph_notes, and position/flag columns on issue_maps. Additive only.

Undo: DROP TABLE paragraph_notes; ALTER TABLE issue_maps DROP COLUMN applicant_position, DROP COLUMN respondent_position,
DROP COLUMN review_flags;  (or alembic downgrade 0047_case_frames).

Revision ID: 0048_paragraph_notes
Revises: 0047_case_frames
"""

from alembic import op
import sqlalchemy as sa

revision = "0048_paragraph_notes"
down_revision = "0047_case_frames"
branch_labels = None
depends_on = None

NEW_COLUMNS = (
	("applicant_position", sa.Text()),
	("respondent_position", sa.Text()),
	("review_flags", sa.JSON()),
)


def upgrade() -> None:
	inspector = sa.inspect(op.get_bind())
	tables = set(inspector.get_table_names())
	if "paragraph_notes" not in tables:
		op.create_table(
			"paragraph_notes",
			sa.Column("id", sa.Integer(), primary_key=True),
			sa.Column("case_id", sa.Integer(), sa.ForeignKey("cases.id", ondelete="CASCADE"), nullable=False),
			sa.Column("para", sa.Integer(), nullable=False),
			sa.Column("version", sa.Integer(), server_default="1", nullable=False),
			sa.Column("note", sa.Text(), nullable=False),
			sa.Column("source", sa.String(40), nullable=False),
			sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
			sa.UniqueConstraint("case_id", "para", "version", name="uq_paragraph_note_case_para_version"),
		)
		op.create_index("ix_paragraph_notes_case_id", "paragraph_notes", ["case_id"])
	if "issue_maps" in tables:
		have = {c["name"] for c in inspector.get_columns("issue_maps")}
		for name, kind in NEW_COLUMNS:
			if name not in have:
				op.add_column("issue_maps", sa.Column(name, kind, nullable=True))


def downgrade() -> None:
	inspector = sa.inspect(op.get_bind())
	tables = set(inspector.get_table_names())
	if "issue_maps" in tables:
		have = {c["name"] for c in inspector.get_columns("issue_maps")}
		for name, _ in NEW_COLUMNS:
			if name in have:
				op.drop_column("issue_maps", name)
	if "paragraph_notes" in tables:
		op.drop_table("paragraph_notes")
