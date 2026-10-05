"""DB-free contracts and opt-in PostgreSQL refinement migration coverage."""

import importlib.util
import os
import uuid
from pathlib import Path

import pytest
import sqlalchemy as sa
from alembic import command
from alembic.config import Config
from alembic.migration import MigrationContext
from alembic.operations import Operations
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import configure_mappers

ROOT = Path(__file__).resolve().parents[1]
TABLE_NAMES = {
    "citations_refined",
    "citation_paragraph_links",
    "statute_references_refined",
    "citation_refine_status",
}


@pytest.fixture
def migration():
    path = ROOT / "alembic/versions/0039_citation_refinement.py"
    spec = importlib.util.spec_from_file_location("citation_refinement_migration", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_migration_from_zero_matches_refinement_metadata(monkeypatch, migration):
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

    try:
        with database.engine.connect() as connection:
            connection.exec_driver_sql("SELECT 1")
    except sa.exc.SQLAlchemyError as exc:
        pytest.skip(f"disposable PostgreSQL is unavailable: {type(exc).__name__}")

    schema = f"test_citation_refinement_{uuid.uuid4().hex}"
    base_engine = database.engine
    isolated_engine = None
    schema_created = False

    def assert_metadata_parity():
        with isolated_engine.connect() as connection:
            inspector = sa.inspect(connection)
            assert TABLE_NAMES <= set(inspector.get_table_names(schema=schema))
            snapshot = {}
            for name in sorted(TABLE_NAMES):
                model = database.Base.metadata.tables[name]
                columns = {
                    column["name"]: column
                    for column in inspector.get_columns(name, schema=schema)
                }
                assert set(columns) == set(model.c.keys())
                for expected in model.c:
                    actual = columns[expected.name]
                    # PostgreSQL reflects FLOAT as DOUBLE PRECISION; generic
                    # types normalize that spelling without losing timezone or length.
                    assert actual["type"].as_generic().compile(
                        dialect=connection.dialect
                    ) == expected.type.compile(dialect=connection.dialect)
                    assert actual["nullable"] == expected.nullable

                primary_key = tuple(
                    inspector.get_pk_constraint(name, schema=schema)["constrained_columns"]
                )
                assert primary_key == tuple(column.name for column in model.primary_key)
                foreign_keys = inspector.get_foreign_keys(name, schema=schema)
                assert all(
                    fk["referred_schema"] in (None, schema) for fk in foreign_keys
                )
                actual_fks = {
                    (
                        tuple(fk["constrained_columns"]),
                        fk["referred_table"],
                        tuple(fk["referred_columns"]),
                        fk["options"].get("ondelete"),
                    )
                    for fk in foreign_keys
                }
                expected_fks = {
                    (
                        tuple(element.parent.name for element in fk.elements),
                        fk.referred_table.name,
                        tuple(element.column.name for element in fk.elements),
                        fk.ondelete,
                    )
                    for fk in model.foreign_key_constraints
                }
                assert actual_fks == expected_fks
                indexes = {
                    (index["name"], tuple(index["column_names"]), bool(index["unique"]))
                    for index in inspector.get_indexes(name, schema=schema)
                }
                assert indexes == {
                    (
                        index.name,
                        tuple(column.name for column in index.columns),
                        bool(index.unique),
                    )
                    for index in model.indexes
                }
                snapshot[name] = (
                    {
                        key: (str(column["type"]), column["nullable"])
                        for key, column in columns.items()
                    },
                    primary_key,
                    actual_fks,
                    indexes,
                )
            return snapshot

    try:
        with base_engine.begin() as connection:
            connection.exec_driver_sql(f'CREATE SCHEMA "{schema}"')
        schema_created = True
        isolated_engine = sa.create_engine(
            database.DATABASE_URL,
            connect_args={"options": f"-csearch_path={schema},public"},
        )
        monkeypatch.setattr(database, "engine", isolated_engine)
        with isolated_engine.connect() as connection:
            assert not sa.inspect(connection).get_table_names(schema=schema)

        config = Config(str(ROOT / "alembic.ini"))
        config.set_main_option("script_location", str(ROOT / "alembic"))
        command.upgrade(config, "head")
        before = assert_metadata_parity()

        # Repeating command.upgrade at head would not execute upgrade again.
        with isolated_engine.begin() as connection:
            monkeypatch.setattr(
                migration, "op", Operations(MigrationContext.configure(connection))
            )
            migration.upgrade()
            migration.upgrade()
        assert assert_metadata_parity() == before

        command.downgrade(config, migration.down_revision)
        assert assert_metadata_parity() == before
        command.upgrade(config, "head")
        assert assert_metadata_parity() == before
    finally:
        if isolated_engine is not None:
            isolated_engine.dispose()
        if schema_created:
            with base_engine.begin() as connection:
                connection.exec_driver_sql(f'DROP SCHEMA "{schema}" CASCADE')


def capture_upgrade(monkeypatch, migration, existing=()):
    tables = {name: object() for name in existing}
    indexes = []
    created = []

    class Inspector:
        def get_table_names(self):
            return list(tables)

    class Operations:
        def get_bind(self):
            return object()

        def create_table(self, name, *columns):
            assert name not in tables
            tables[name] = sa.Table(name, sa.MetaData(), *columns)
            created.append(name)

        def create_index(self, name, table, columns):
            indexes.append((name, table, tuple(columns)))

    monkeypatch.setattr(migration.sa, "inspect", lambda _bind: Inspector())
    monkeypatch.setattr(migration, "op", Operations())
    return tables, indexes, created


def test_upgrade_twice_creates_only_four_tables_and_two_indexes(monkeypatch, migration):
    tables, indexes, created = capture_upgrade(monkeypatch, migration)
    migration.upgrade()
    first_tables = dict(tables)
    migration.upgrade()
    assert tables == first_tables
    assert set(created) == TABLE_NAMES
    assert len(created) == 4
    assert indexes == [
        ("ix_citations_refined_source_case_id", "citations_refined", ("source_case_id",)),
        (
            "ix_statute_references_refined_source_case_id",
            "statute_references_refined",
            ("source_case_id",),
        ),
    ]
    assert created.index("citations_refined") < created.index("citation_paragraph_links")


@pytest.mark.parametrize("existing", [TABLE_NAMES, {"citations_refined"}, {"statute_references_refined"}])
def test_preexisting_tables_are_not_inspected_altered_or_reindexed(monkeypatch, migration, existing):
    tables, indexes, created = capture_upgrade(monkeypatch, migration, existing)
    preserved = dict(tables)
    migration.upgrade()
    migration.upgrade()
    assert set(created) == TABLE_NAMES - existing
    assert all(tables[name] is original for name, original in preserved.items())
    assert not any(table in existing for _, table, _ in indexes)


def test_downgrade_is_noop(monkeypatch, migration):
    tables, indexes, created = capture_upgrade(monkeypatch, migration)
    migration.upgrade()
    before = (dict(tables), list(indexes), list(created))
    # No operations (including inspection) are permitted during downgrade.
    monkeypatch.setattr(migration, "op", object())
    migration.downgrade()
    assert (tables, indexes, created) == before


def column_contract(column):
    return (
        column.type.compile(dialect=postgresql.dialect()),
        column.nullable,
        column.primary_key,
        column.default.arg if column.default is not None else None,
        str(column.server_default.arg) if column.server_default is not None else None,
        {(fk.target_fullname, fk.ondelete) for fk in column.foreign_keys},
    )


def test_models_and_frozen_migration_match(monkeypatch, migration):
    from backend.database import Base

    tables, _, _ = capture_upgrade(monkeypatch, migration)
    migration.upgrade()
    configure_mappers()
    for name in TABLE_NAMES:
        actual = tables[name]
        model = Base.metadata.tables[name]
        assert set(actual.c.keys()) == set(model.c.keys())
        for column in model.c:
            assert column_contract(actual.c[column.name]) == column_contract(column), (name, column.name)
        # Compiling DDL never opens a connection.
        metadata = sa.MetaData()
        for parent in ("cases", "case_chunks", "statute_versions", "citations_refined"):
            if parent != name:
                Base.metadata.tables[parent].to_metadata(metadata)
        copied = actual.to_metadata(metadata)
        assert f"CREATE TABLE {name}" in str(
            sa.schema.CreateTable(copied).compile(dialect=postgresql.dialect())
        )


@pytest.mark.parametrize(
    "base_name,refined_name,extras",
    [
        ("citations", "citations_refined", {"refine_step", "confidence", "refine_version", "source_citation_id"}),
        (
            "statute_references",
            "statute_references_refined",
            {"refine_step", "confidence", "group_start", "group_end", "group_index", "refine_version"},
        ),
    ],
)
def test_refined_occurrences_preserve_base_fields_without_base_indexes(base_name, refined_name, extras):
    from backend.database import Base

    base = Base.metadata.tables[base_name]
    refined = Base.metadata.tables[refined_name]
    assert set(refined.c.keys()) == set(base.c.keys()) | extras
    for column in base.c:
        assert column_contract(refined.c[column.name]) == column_contract(column)
    assert {(index.name, tuple(c.name for c in index.columns)) for index in refined.indexes} == {
        (f"ix_{refined_name}_source_case_id", ("source_case_id",))
    }
    assert not refined.c.refine_version.nullable
    assert refined.c.refine_version.default is None
    assert refined.c.confidence.nullable
    assert isinstance(refined.c.confidence.type, sa.Float)


def test_link_and_status_keys_and_no_new_relationships():
    from backend.database import CitationParagraphLink, CitationRefined, CitationRefineStatus, StatuteReferenceRefined

    links = CitationParagraphLink.__table__
    assert {(fk.target_fullname, fk.ondelete) for fk in links.foreign_keys} == {
        ("citations_refined.id", "CASCADE")
    }
    assert not links.indexes
    assert links.c.target_case_id.nullable
    assert not CitationRefined.__table__.c.source_citation_id.foreign_keys
    status = CitationRefineStatus.__table__
    assert [c.name for c in status.primary_key] == ["source_case_id"]
    assert not status.indexes
    assert not status.foreign_keys
    assert status.c.processed_at.type.timezone
    for model in (CitationParagraphLink, CitationRefined, CitationRefineStatus, StatuteReferenceRefined):
        assert not model.__mapper__.relationships
