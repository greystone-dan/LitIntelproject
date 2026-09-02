"""add structured legislation citation identity"""

from alembic import op
import sqlalchemy as sa


revision = "0017_structured_legislation_cite"
down_revision = "0016_case_source_html"
branch_labels = None
depends_on = None


def upgrade() -> None:
	with op.batch_alter_table("statute_references") as batch_op:
		batch_op.add_column(sa.Column("instrument_key", sa.String(length=100), nullable=True))
		batch_op.add_column(sa.Column("pinpoint", sa.String(length=255), nullable=True))
		batch_op.add_column(sa.Column("legislation_url", sa.Text(), nullable=True))
		batch_op.create_index("ix_statute_references_instrument_key", ["instrument_key"])
		batch_op.create_index("ix_statute_references_pinpoint", ["pinpoint"])


def downgrade() -> None:
	with op.batch_alter_table("statute_references") as batch_op:
		batch_op.drop_index("ix_statute_references_pinpoint")
		batch_op.drop_index("ix_statute_references_instrument_key")
		batch_op.drop_column("legislation_url")
		batch_op.drop_column("pinpoint")
		batch_op.drop_column("instrument_key")