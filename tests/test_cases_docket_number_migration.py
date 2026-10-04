"""Focused coverage for the additive cases.docket_number migration."""

import os
import uuid
from pathlib import Path

import pytest
import sqlalchemy as sa
from alembic import command
from alembic.config import Config

ROOT = Path(__file__).resolve().parents[1]


def test_migration_from_zero_matches_case_metadata(monkeypatch):
    if os.environ.get("CASELIBRARY_PGVECTOR_TESTS") != "1":
        pytest.skip("requires explicit disposable PostgreSQL test opt-in")

    dotenv_paths = (ROOT / ".env", ROOT / "backend" / ".env")
    if any(path.exists() or path.is_symlink() for path in dotenv_paths):
        pytest.fail("refusing migration test with root or backend dotenv overrides")

    required_settings = (
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_HOST",
        "POSTGRES_PORT",
        "POSTGRES_DB",
    )
    missing_settings = [name for name in required_settings if not os.environ.get(name)]
    if missing_settings:
        pytest.fail(
            "disposable PostgreSQL test opt-in requires all POSTGRES_* settings: "
            + ", ".join(missing_settings)
        )

    from backend import database
    from backend.database import Case

    try:
        with database.engine.connect() as connection:
            connection.exec_driver_sql("SELECT 1")
    except sa.exc.SQLAlchemyError as exc:
        pytest.skip(f"disposable PostgreSQL is unavailable: {type(exc).__name__}")

    schema = f"test_case_docket_{uuid.uuid4().hex}"
    base_engine = database.engine
    isolated_engine = None
    schema_created = False

    try:
        with base_engine.begin() as connection:
            connection.exec_driver_sql(f'CREATE SCHEMA "{schema}"')
        schema_created = True

        isolated_engine = sa.create_engine(
            database.DATABASE_URL,
            connect_args={"options": f"-csearch_path={schema},public"},
        )
        monkeypatch.setattr(database, "engine", isolated_engine)

        config = Config(str(ROOT / "alembic.ini"))
        config.set_main_option("script_location", str(ROOT / "alembic"))
        command.upgrade(config, "head")

        with isolated_engine.connect() as connection:
            inspector = sa.inspect(connection)
            actual_columns = {
                column["name"]: column for column in inspector.get_columns("cases")
            }
            expected_columns = {column.name: column for column in Case.__table__.columns}
            assert set(actual_columns) == set(expected_columns)
            for name, expected in expected_columns.items():
                assert str(actual_columns[name]["type"]) == str(expected.type)
                assert actual_columns[name]["nullable"] == expected.nullable

            actual_indexes = {
                (index["name"], tuple(index["column_names"]), bool(index["unique"]))
                for index in inspector.get_indexes("cases")
            }
            expected_indexes = {
                (
                    index.name,
                    tuple(column.name for column in index.columns),
                    bool(index.unique),
                )
                for index in Case.__table__.indexes
            }
            # The initial schema also owns a specialized HNSW index not
            # represented by Case metadata; require every model index here.
            assert expected_indexes <= actual_indexes
    finally:
        if isolated_engine is not None:
            isolated_engine.dispose()
        if schema_created:
            with base_engine.begin() as connection:
                connection.exec_driver_sql(f'DROP SCHEMA "{schema}" CASCADE')


def test_upgrade_is_idempotent_and_preserves_existing_objects(monkeypatch):
    import importlib.util

    migration_path = ROOT / "alembic" / "versions" / "0037_cases_docket_number.py"
    spec = importlib.util.spec_from_file_location("cases_docket_migration", migration_path)
    migration = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(migration)

    state = {
        "tables": ["cases"],
        "columns": [{"name": "id"}, {"name": "legacy_marker"}],
        "indexes": [
            {"name": "ix_cases_legacy_marker", "column_names": ["legacy_marker"]}
        ],
    }

    class Inspector:
        def get_table_names(self):
            return list(state["tables"])

        def get_columns(self, table_name):
            assert table_name == "cases"
            return list(state["columns"])

        def get_indexes(self, table_name):
            assert table_name == "cases"
            return list(state["indexes"])

    class Operations:
        added_columns = []

        def get_bind(self):
            return object()

        def add_column(self, table_name, column):
            assert table_name == "cases"
            self.added_columns.append(column)
            state["columns"].append({"name": column.name})

        def create_index(self, name, table_name, columns):
            assert table_name == "cases"
            state["indexes"].append({"name": name, "column_names": columns})

    operations = Operations()
    monkeypatch.setattr(migration.sa, "inspect", lambda _bind: Inspector())
    monkeypatch.setattr(migration, "op", operations)

    migration.upgrade()
    migration.upgrade()

    assert [column["name"] for column in state["columns"]].count("docket_number") == 1
    assert [index["name"] for index in state["indexes"]].count("ix_cases_docket_number") == 1
    assert len(operations.added_columns) == 1
    assert isinstance(operations.added_columns[0].type, sa.String)
    assert operations.added_columns[0].type.length == 255
    assert operations.added_columns[0].nullable is True
    assert state["indexes"][0] == {
        "name": "ix_cases_legacy_marker",
        "column_names": ["legacy_marker"],
    }

    # Objects that already have the declared names are preserved too.
    state["columns"] = [{"name": "id"}, {"name": "docket_number"}]
    state["indexes"] = [
        {"name": "ix_cases_docket_number", "column_names": ["docket_number"]},
        {"name": "ix_cases_legacy_marker", "column_names": ["legacy_marker"]},
    ]
    migration.upgrade()
    assert len(operations.added_columns) == 1
    assert [index["name"] for index in state["indexes"]].count("ix_cases_docket_number") == 1
