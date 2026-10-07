"""Offline migration regressions; never import the application's DB engine."""

import importlib.util
from pathlib import Path
from unittest.mock import Mock

import pytest
import sqlalchemy as sa
from alembic.config import Config
from alembic.migration import MigrationContext
from alembic.operations import Operations
from alembic.script import ScriptDirectory
from alembic.util import CommandError


ROOT = Path(__file__).resolve().parents[1]


def load_migration(filename):
    spec = importlib.util.spec_from_file_location(
        filename.removesuffix(".py"), ROOT / "alembic" / "versions" / filename
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def engine():
    engine = sa.create_engine("sqlite://")

    @sa.event.listens_for(engine, "before_cursor_execute", retval=True)
    def parenthesize_postgres_defaults(connection, cursor, statement, parameters, context, executemany):
        # SQLite requires parentheses around expression defaults. Keep the
        # migration's PostgreSQL schema unchanged; adapt only test execution.
        return statement.replace("DEFAULT now()", "DEFAULT (now())"), parameters

    yield engine
    engine.dispose()


@pytest.mark.parametrize("existing", [False, True])
def test_cases_inspection_is_guarded_and_existing_columns_preserved(monkeypatch, existing):
    migration = load_migration("0001_case_metadata.py")
    columns = [
        "id", "title", "court", "date", "summary", "embedding", "created_at",
        "jurisdiction", "citation", "full_text", "issues", "metadata_json",
        "source_url", "source_name",
    ]
    inspector = Mock()
    inspector.get_table_names.return_value = ["cases"] if existing else []

    def get_columns(table):
        assert existing, "must not inspect columns of a missing cases table"
        assert table == "cases"
        inspector.get_table_names.assert_called_once()
        return [{"name": name} for name in columns]

    inspector.get_columns.side_effect = get_columns
    monkeypatch.setattr(migration.sa, "inspect", Mock(return_value=inspector))
    operations = Mock()
    monkeypatch.setattr(migration, "op", operations)
    migration.upgrade()

    operations.add_column.assert_not_called()
    operations.drop_table.assert_not_called()
    operations.drop_column.assert_not_called()
    if existing:
        inspector.get_columns.assert_called_once_with("cases")
        operations.create_table.assert_not_called()
        operations.create_index.assert_not_called()
        operations.execute.assert_called_once()
    else:
        inspector.get_columns.assert_not_called()
        args = operations.create_table.call_args.args
        assert args[0] == "cases"
        assert {column.name for column in args[1:]} == set(columns)
        assert operations.create_index.call_count == 5


def test_existing_cases_adds_only_missing_metadata(monkeypatch):
    migration = load_migration("0001_case_metadata.py")
    inspector = Mock()
    inspector.get_table_names.return_value = ["cases"]
    inspector.get_columns.return_value = [{"name": "citation"}, {"name": "source_name"}]
    monkeypatch.setattr(migration.sa, "inspect", Mock(return_value=inspector))
    operations = Mock()
    monkeypatch.setattr(migration, "op", operations)
    migration.upgrade()
    assert {call.args[1].name for call in operations.add_column.call_args_list} == {
        "jurisdiction", "full_text", "issues", "metadata_json", "source_url",
    }
    operations.create_index.assert_called_once_with(
        "ix_cases_jurisdiction", "cases", ["jurisdiction"]
    )
    operations.create_table.assert_not_called()


def test_missing_parent_has_frozen_schema_and_accepts_0027(monkeypatch, engine):
    migration = load_migration("0015_fc_activity_classifications.py")
    provenance = load_migration("0027_fc_activity_source_provenance.py")
    with engine.begin() as connection:
        operations = Operations(MigrationContext.configure(connection))
        monkeypatch.setattr(migration, "op", operations)
        monkeypatch.setattr(provenance, "op", operations)
        migration.upgrade()
        inspector = sa.inspect(connection)
        columns = {column["name"]: column for column in inspector.get_columns("fc_activity_cases")}
        expected_types = {
            "id": sa.Integer(), "source_key": sa.String(255), "citation": sa.String(255),
            "year": sa.Integer(), "case_name": sa.Text(), "date_filed": sa.Date(),
            "city_filed": sa.String(255), "nature": sa.Text(), "case_class": sa.String(120),
            "track": sa.String(120), "source_url": sa.String(2048),
            "scraped_timestamp": sa.DateTime(timezone=True), "raw_payload": sa.JSON(),
            "created_at": sa.DateTime(timezone=True), "updated_at": sa.DateTime(timezone=True),
        }
        assert set(columns) == set(expected_types)
        for name, expected_type in expected_types.items():
            assert str(columns[name]["type"]) == str(expected_type)
            assert columns[name]["nullable"] == (name not in {"id", "source_key", "created_at", "updated_at"})
        for name in ("created_at", "updated_at"):
            assert "now()" in columns[name]["default"]
        assert inspector.get_pk_constraint("fc_activity_cases")["constrained_columns"] == ["id"]
        assert {
            (constraint["name"], tuple(constraint["column_names"]))
            for constraint in inspector.get_unique_constraints("fc_activity_cases")
        } == {
            ("uq_fc_activity_case_citation", ("citation",)),
            ("uq_fc_activity_case_source_key", ("source_key",)),
        }
        assert {
            (index["name"], tuple(index["column_names"]), bool(index["unique"]))
            for index in inspector.get_indexes("fc_activity_cases")
        } == {
            ("ix_fc_activity_cases_source_key", ("source_key",), True),
            ("ix_fc_activity_cases_citation", ("citation",), False),
            ("ix_fc_activity_cases_year", ("year",), False),
            ("ix_fc_activity_cases_date_filed", ("date_filed",), False),
        }
        foreign_key, = inspector.get_foreign_keys("fc_activity_classifications")
        assert foreign_key["referred_table"] == "fc_activity_cases"
        assert foreign_key["referred_columns"] == ["id"]
        assert foreign_key["options"]["ondelete"] == "CASCADE"

        # The real later revision must add provenance without duplicate columns.
        provenance.upgrade()
        for table in ("fc_activity_cases", "fc_activity_classifications"):
            reflected = {column["name"]: column for column in sa.inspect(connection).get_columns(table)}
            for name, length in (("source_type", 100), ("source_name", 255), ("source_id", 255)):
                assert reflected[name]["nullable"]
                assert reflected[name]["type"].length == length
            assert {
                f"ix_{table}_{name}" for name in ("source_type", "source_name", "source_id")
            } <= {index["name"] for index in sa.inspect(connection).get_indexes(table)}


def test_existing_parent_schema_and_data_are_untouched_even_on_downgrade(monkeypatch, engine):
    migration = load_migration("0015_fc_activity_classifications.py")

    def columns(connection):
        return [
            {**column, "type": str(column["type"])}
            for column in sa.inspect(connection).get_columns("fc_activity_cases")
        ]

    with engine.begin() as connection:
        connection.exec_driver_sql(
            "CREATE TABLE fc_activity_cases (id INTEGER PRIMARY KEY, legacy_marker TEXT NOT NULL)"
        )
        connection.exec_driver_sql("INSERT INTO fc_activity_cases VALUES (7, 'preserve me')")
        connection.exec_driver_sql("CREATE INDEX legacy_parent_index ON fc_activity_cases (legacy_marker)")
        before_columns = columns(connection)
        before_indexes = sa.inspect(connection).get_indexes("fc_activity_cases")
        monkeypatch.setattr(migration, "op", Operations(MigrationContext.configure(connection)))
        migration.upgrade()
        assert "fc_activity_classifications" in sa.inspect(connection).get_table_names()
        for phase in ("upgrade", "downgrade"):
            if phase == "downgrade":
                migration.downgrade()
            inspector = sa.inspect(connection)
            assert columns(connection) == before_columns
            assert inspector.get_indexes("fc_activity_cases") == before_indexes
            assert connection.exec_driver_sql("SELECT * FROM fc_activity_cases").all() == [(7, "preserve me")]


def test_repository_has_exactly_one_expected_head():
    config = Config(str(ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(ROOT / "alembic"))
    scripts = ScriptDirectory.from_config(config)
    assert scripts.get_heads() == ["0043_workbench"]
    assert scripts.get_current_head() == "0043_workbench"
    assert scripts.get_revision("0001_case_metadata").down_revision is None
    assert scripts.get_revision("0015_fc_activity_classifications").down_revision == "0014_judge_profiles"


def test_single_head_check_rejects_synthetic_multiple_heads(tmp_path):
    versions = tmp_path / "versions"
    versions.mkdir()
    for revision in ("branch_a", "branch_b"):
        (versions / f"{revision}.py").write_text(
            f"revision = {revision!r}\ndown_revision = None\n"
            "branch_labels = None\ndepends_on = None\n",
            encoding="utf-8",
        )
    scripts = ScriptDirectory(str(tmp_path))
    assert len(scripts.get_heads()) == 2
    with pytest.raises(CommandError, match="multiple heads"):
        scripts.get_current_head()
