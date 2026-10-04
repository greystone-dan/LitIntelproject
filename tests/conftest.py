"""Pytest configuration and fixtures for LitIntel tests."""

import pytest
from sqlalchemy import text
from backend.database import SessionLocal


def check_postgres_available() -> bool:
    """Check if Postgres database is accessible."""
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        return True
    except Exception:
        return False


pytest_postgres_available = check_postgres_available()


@pytest.fixture
def requires_postgres():
    """Fixture that skips test if Postgres is not available."""
    if not pytest_postgres_available:
        pytest.skip("Postgres database not accessible (localhost:5432)")
