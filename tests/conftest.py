"""Pytest configuration and fixtures for LitIntel tests."""

import os

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine import make_url

from backend.database import DATABASE_URL

# The site hides the judge profile feature unless ILIT_JUDGE_PROFILES is set; the suite tests it switched on.
os.environ.setdefault("ILIT_JUDGE_PROFILES", "1")


@pytest.fixture
def requires_postgres():
    """Skip database-backed tests when configured PostgreSQL is unavailable."""
    if make_url(DATABASE_URL).get_backend_name() != "postgresql":
        pytest.skip("Configured database URL is not PostgreSQL")

    probe_engine = create_engine(DATABASE_URL, connect_args={"connect_timeout": 2})
    try:
        with probe_engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError:
        pytest.skip("PostgreSQL is unavailable at the configured database URL")
    finally:
        probe_engine.dispose()
