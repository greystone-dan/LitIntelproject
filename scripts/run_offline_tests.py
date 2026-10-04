"""Run pytest without dotenv access or application/external database connections.

Only isolated SQLite fixtures may connect: in-memory engines or files within
this run's disposable pytest temporary directory. Application engines and
PostgreSQL DBAPI connections are forbidden, including raw connection paths.
"""

import os
from pathlib import Path
import sys
import tempfile
from urllib.parse import parse_qs, unquote, urlsplit


def install_connection_guard(fixture_root, forbidden_engines):
    import psycopg2
    import sqlalchemy
    import sqlite3

    def permitted_sqlite(database):
        if database in (None, "", ":memory:"):
            return True
        value = os.fsdecode(database)
        if value.startswith("file:"):
            # One existing staging fixture uses read-only SQLite URI syntax.
            # Permit only that mode, and only within this run's fixture root.
            uri = urlsplit(value)
            if uri.netloc or parse_qs(uri.query) != {"mode": ["ro"]} or uri.fragment:
                return False
            value = unquote(uri.path)
        return Path(value).resolve().is_relative_to(fixture_root.resolve())

    original_connect = sqlalchemy.engine.Engine.connect
    original_raw = sqlalchemy.engine.Engine.raw_connection
    original_sqlite = sqlite3.connect

    def check_engine(engine):
        if (engine in forbidden_engines or engine.dialect.name != "sqlite"
                or not permitted_sqlite(engine.url.database)):
            raise RuntimeError("Offline validation forbids this database connection")

    def offline_connect(engine, *args, **kwargs):
        check_engine(engine)
        return original_connect(engine, *args, **kwargs)

    def offline_raw(engine, *args, **kwargs):
        check_engine(engine)
        return original_raw(engine, *args, **kwargs)

    def offline_sqlite(database, *args, **kwargs):
        if not permitted_sqlite(database):
            raise RuntimeError("Offline validation forbids this database connection")
        return original_sqlite(database, *args, **kwargs)

    def reject_postgres(*args, **kwargs):
        raise RuntimeError("Offline validation forbids PostgreSQL connections")

    offline_connect.offline_validation_guard = True
    sqlalchemy.engine.Engine.connect = offline_connect
    sqlalchemy.engine.Engine.raw_connection = offline_raw
    sqlite3.connect = sqlite3.dbapi2.connect = offline_sqlite
    psycopg2.connect = reject_postgres


def main() -> int:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    import dotenv
    import dotenv.main

    # Patch before any backend import, rather than depending on dotenv version.
    dotenv.load_dotenv = dotenv.main.load_dotenv = lambda *args, **kwargs: False
    for key in ("POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_HOST",
                "POSTGRES_PORT", "POSTGRES_DB"):
        os.environ.pop(key, None)
    os.environ["DATABASE_URL"] = "sqlite:///:memory:"
    os.environ["CASELIBRARY_AUDIT_LOG"] = ""

    forbidden_engines = set()
    with tempfile.TemporaryDirectory(prefix="caselibrary-pytest-") as directory:
        # Coverage uses SQLite too; keep its instrumentation DB in this run's
        # disposable root rather than granting access to arbitrary files.
        os.environ["COVERAGE_FILE"] = str(Path(directory) / ".coverage")
        install_connection_guard(Path(directory), forbidden_engines)
        from backend import database
        forbidden_engines.add(database.engine)

        import pytest
        return pytest.main(["--basetemp", directory, *sys.argv[1:]])


if __name__ == "__main__":
    raise SystemExit(main())
