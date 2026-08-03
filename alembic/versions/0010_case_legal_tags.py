"""Add versioned, evidence-bearing legal tags and resumable tagging status."""

from alembic import op
import sqlalchemy as sa

revision = "0010_case_legal_tags"
down_revision = "0009_local_chunk_embeddings"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "case_tags",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("case_id", sa.Integer(), nullable=False),
        sa.Column("category", sa.String(length=100), nullable=False),
        sa.Column("value", sa.String(length=255), nullable=False),
        sa.Column("score", sa.Float(), nullable=False),
        sa.Column("evidence", sa.Text(), nullable=False),
        sa.Column("source", sa.String(length=50), nullable=False),
        sa.Column("taxonomy_version", sa.String(length=100), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.ForeignKeyConstraint(["case_id"], ["cases.id"], ondelete="CASCADE"),
        sa.UniqueConstraint(
            "case_id",
            "category",
            "value",
            "taxonomy_version",
            name="uq_case_tag_taxonomy",
        ),
    )
    op.create_index("ix_case_tags_case_id", "case_tags", ["case_id"])
    op.create_index("ix_case_tags_category", "case_tags", ["category"])
    op.create_index("ix_case_tags_value", "case_tags", ["value"])
    op.create_index("ix_case_tags_source", "case_tags", ["source"])
    op.create_index("ix_case_tags_taxonomy_version", "case_tags", ["taxonomy_version"])
    op.create_index("ix_case_tags_category_value", "case_tags", ["category", "value"])

    op.create_table(
        "case_tagging_status",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("case_id", sa.Integer(), nullable=False),
        sa.Column("taxonomy_version", sa.String(length=100), nullable=False),
        sa.Column("tags_count", sa.Integer(), nullable=False),
        sa.Column(
            "tagged_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.ForeignKeyConstraint(["case_id"], ["cases.id"], ondelete="CASCADE"),
        sa.UniqueConstraint("case_id", "taxonomy_version", name="uq_case_tagging_status"),
    )
    op.create_index("ix_case_tagging_status_case_id", "case_tagging_status", ["case_id"])
    op.create_index(
        "ix_case_tagging_status_taxonomy_version",
        "case_tagging_status",
        ["taxonomy_version"],
    )


def downgrade() -> None:
    op.drop_index("ix_case_tagging_status_taxonomy_version", table_name="case_tagging_status")
    op.drop_index("ix_case_tagging_status_case_id", table_name="case_tagging_status")
    op.drop_table("case_tagging_status")
    op.drop_index("ix_case_tags_category_value", table_name="case_tags")
    op.drop_index("ix_case_tags_taxonomy_version", table_name="case_tags")
    op.drop_index("ix_case_tags_source", table_name="case_tags")
    op.drop_index("ix_case_tags_value", table_name="case_tags")
    op.drop_index("ix_case_tags_category", table_name="case_tags")
    op.drop_index("ix_case_tags_case_id", table_name="case_tags")
    op.drop_table("case_tags")