"""Isolation checks; forbidden connection attempts must fail before any I/O."""

import sqlite3

import psycopg2
import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from backend import database

pytestmark = pytest.mark.skipif(
    not getattr(Engine.connect, "offline_validation_guard", False),
    reason="Isolation checks require scripts/run_offline_tests.py",
)


@pytest.mark.parametrize("method", ["connect", "raw_connection"])
def test_offline_runner_blocks_application_and_postgres_engines(method):
    for engine in (database.engine, create_engine("postgresql+psycopg2://localhost/offline")):
        with pytest.raises(RuntimeError, match="Offline validation forbids"):
            getattr(engine, method)()


def test_offline_runner_blocks_direct_postgres():
    with pytest.raises(RuntimeError, match="Offline validation forbids"):
        psycopg2.connect("")


def test_offline_runner_blocks_files_outside_fixture_root():
    # This path is never created/opened, even via the raw connection path.
    path = "/tmp/caselibrary-forbidden-database.sqlite"
    with pytest.raises(RuntimeError, match="Offline validation forbids"):
        sqlite3.connect(path)
    engine = create_engine(f"sqlite:///{path}")
    with pytest.raises(RuntimeError, match="Offline validation forbids"):
        engine.raw_connection()
    with pytest.raises(RuntimeError, match="Offline validation forbids"):
        sqlite3.connect("file::memory:?cache=shared", uri=True)


def test_offline_runner_allows_only_disposable_fixtures(tmp_path):
    path = tmp_path / "fixture.sqlite"
    with sqlite3.connect(path) as connection:
        assert connection.execute("SELECT 1").fetchone() == (1,)
    with sqlite3.connect(f"file:{path}?mode=ro", uri=True) as connection:
        assert connection.execute("SELECT 1").fetchone() == (1,)
    engine = create_engine("sqlite:///:memory:")
    raw = engine.raw_connection()
    try:
        assert raw.cursor().execute("SELECT 1").fetchone() == (1,)
    finally:
        raw.close()
        engine.dispose()
