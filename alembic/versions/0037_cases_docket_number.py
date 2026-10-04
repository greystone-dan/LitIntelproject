"""Add the nullable docket number to cases.

Revision ID: 0037_cases_docket_number
Revises: 0036_paragraph_cited_by
Create Date: 2026-10-04
"""

import sqlalchemy as sa
from alembic import op


revision = "0037_cases_docket_number"
down_revision = "0036_paragraph_cited_by"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "cases" not in inspector.get_table_names():
        return

    existing_columns = {column["name"] for column in inspector.get_columns("cases")}
    if "docket_number" not in existing_columns:
        op.add_column(
            "cases",
            sa.Column("docket_number", sa.String(length=255), nullable=True),
        )

    existing_indexes = {index["name"] for index in inspector.get_indexes("cases")}
    if "ix_cases_docket_number" not in existing_indexes:
        op.create_index("ix_cases_docket_number", "cases", ["docket_number"])


def downgrade() -> None:
    # The upgrade is deliberately safe on databases where either object
    # pre-existed. A downgrade cannot distinguish those objects from ones it
    # created, so leave them untouched rather than risk deleting user schema.
    pass
