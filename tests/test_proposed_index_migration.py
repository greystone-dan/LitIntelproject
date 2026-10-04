import ast
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MIGRATION = ROOT / "docs" / "proposed-migrations" / "indexes.py.txt"
DATABASE_MODELS = ROOT / "backend" / "database.py"

CREATE_INDEX = re.compile(
    r"^CREATE INDEX CONCURRENTLY IF NOT EXISTS "
    r"(?P<name>[a-z_][a-z0-9_]*) ON (?P<table>[a-z_][a-z0-9_]*) "
    r"USING gin \((?P<column>[a-z_][a-z0-9_]*) gin_trgm_ops\)$",
    re.IGNORECASE,
)
DROP_INDEX = re.compile(
    r"^DROP INDEX CONCURRENTLY IF EXISTS (?P<name>[a-z_][a-z0-9_]*)$",
    re.IGNORECASE,
)


def _executed_sql() -> list[str]:
    tree = ast.parse(MIGRATION.read_text(encoding="utf-8"))
    statements = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "op"
            and node.func.attr == "execute"
            and node.args
        ):
            statement = ast.literal_eval(node.args[0])
            assert isinstance(statement, str)
            statements.append(statement)
    return statements


def _model_columns_by_table() -> dict[str, set[str]]:
    tree = ast.parse(DATABASE_MODELS.read_text(encoding="utf-8"))
    tables = {}
    for model in (node for node in tree.body if isinstance(node, ast.ClassDef)):
        table_name = None
        columns = set()
        for member in model.body:
            if isinstance(member, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == "__tablename__"
                for target in member.targets
            ):
                table_name = ast.literal_eval(member.value)
            elif isinstance(member, ast.AnnAssign) and isinstance(
                member.target, ast.Name
            ):
                value = member.value
                if isinstance(value, ast.Call) and (
                    (
                        isinstance(value.func, ast.Name)
                        and value.func.id == "mapped_column"
                    )
                    or (
                        isinstance(value.func, ast.Attribute)
                        and value.func.attr == "mapped_column"
                    )
                ):
                    column_name = member.target.id
                    if value.args and isinstance(value.args[0], ast.Constant):
                        if isinstance(value.args[0].value, str):
                            column_name = value.args[0].value
                    columns.add(column_name)
        if table_name is not None:
            tables[table_name] = columns
    return tables


def test_proposed_index_migration_statements_match_models_and_rollback():
    statements = _executed_sql()
    create_statements = [s for s in statements if s.upper().startswith("CREATE INDEX")]
    drop_statements = [s for s in statements if s.upper().startswith("DROP INDEX")]
    creates = [CREATE_INDEX.fullmatch(statement) for statement in create_statements]
    drops = [DROP_INDEX.fullmatch(statement) for statement in drop_statements]

    assert len(creates) == 4
    assert all(creates)
    assert len(drops) == len(creates)
    assert all(drops)

    index_names = [match.group("name") for match in creates]
    assert len(index_names) == len(set(index_names))
    assert {match.group("name") for match in drops} == set(index_names)

    tables = _model_columns_by_table()
    for match in creates:
        table_name = match.group("table")
        column_name = match.group("column")
        assert table_name in tables
        assert column_name in tables[table_name]

    assert "CREATE EXTENSION IF NOT EXISTS pg_trgm" in statements
