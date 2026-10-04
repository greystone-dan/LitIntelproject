import os
import subprocess
import sys

import pytest
from sqlalchemy import URL

from backend import database


@pytest.mark.parametrize(
    ("disabled", "expected_calls"),
    [("1", 0), ("true", 0), ("T", 0), ("YES", 0), ("y", 0), ("0", 2), ("", 2)],
)
def test_database_import_honors_dotenv_disable(disabled, expected_calls):
    # Mock the loader in a fresh interpreter: no dotenv contents or DB connection.
    code = (
        "from unittest.mock import patch\n"
        "with patch('dotenv.load_dotenv') as loader:\n"
        "    import backend.database\n"
        f"    assert loader.call_count == {expected_calls}\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        env={**os.environ, "PYTHON_DOTENV_DISABLED": disabled},
        capture_output=True, text=True, timeout=30,
    )
    assert result.returncode == 0, result.stderr


def test_database_url_prefers_postgres_parts(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg2://wrong:wrong@localhost:5432/ai_caselibrary")
    monkeypatch.setenv("POSTGRES_USER", "real_user")
    monkeypatch.setenv("POSTGRES_PASSWORD", "real_password")
    monkeypatch.setenv("POSTGRES_HOST", "dbhost")
    monkeypatch.setenv("POSTGRES_PORT", "5433")
    monkeypatch.setenv("POSTGRES_DB", "caselibrary")

    url = database._database_url()

    assert isinstance(url, URL)
    assert str(url).startswith("postgresql+psycopg2://real_user")
    assert url.database == "caselibrary"


def test_database_url_falls_back_to_database_url(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg2://demo:pw@localhost:5432/demo_db")
    for key in [
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_HOST",
        "POSTGRES_PORT",
        "POSTGRES_DB",
    ]:
        monkeypatch.delenv(key, raising=False)

    url = database._database_url()

    assert isinstance(url, str)
    assert url == "postgresql+psycopg2://demo:pw@localhost:5432/demo_db"
