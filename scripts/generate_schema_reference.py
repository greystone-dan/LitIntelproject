"""Generate the checked-in schema reference and ERD from SQLAlchemy metadata."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import MetaData, Table

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))
DEFAULT_OUTPUT = PROJECT_ROOT / "docs" / "SCHEMA_REFERENCE.generated.md"


def _type_label(column) -> str:
	return str(column.type).replace("VARCHAR", "String").replace("INTEGER", "Integer")


def _default_label(column) -> str:
	if column.server_default is not None:
		return str(column.server_default.arg)
	if column.default is not None:
		return str(column.default.arg)
	return ""


def _column_flags(column) -> str:
	flags: list[str] = []
	if column.primary_key:
		flags.append("PK")
	for foreign_key in column.foreign_keys:
		flags.append(f"FK -> {foreign_key.target_fullname}")
	if not column.nullable:
		flags.append("NOT NULL")
	default = _default_label(column)
	if default:
		flags.append(f"default={default}")
	return "; ".join(flags) or "-"


def _erd(metadata: MetaData) -> list[str]:
	lines = ["```mermaid", "erDiagram"]
	for table in sorted(metadata.tables.values(), key=lambda item: item.name):
		lines.append(f"    {table.name} {{")
		for column in table.columns:
			flags = "PK" if column.primary_key else ""
			foreign = " FK" if column.foreign_keys else ""
			lines.append(f"        {_type_label(column)} {column.name} {flags}{foreign}".rstrip())
		lines.append("    }")
	for table in sorted(metadata.tables.values(), key=lambda item: item.name):
		for foreign_key in sorted(table.foreign_keys, key=lambda item: item.parent.name):
			target = foreign_key.column.table.name
			lines.append(f'    {target} ||--o{{ {table.name} : "{foreign_key.parent.name}"')
	lines.extend(["```", ""])
	return lines


def _table_reference(table: Table) -> list[str]:
	lines = [f"## `{table.name}`", ""]
	lines.extend(["### Columns", "", "| Column | Type | Nullable | Constraints and defaults |", "| --- | --- | --- | --- |"])
	for column in table.columns:
		lines.append(
			f"| `{column.name}` | `{_type_label(column)}` | {'yes' if column.nullable else 'no'} | {_column_flags(column)} |"
		)
	lines.append("")
	indexes = sorted(table.indexes, key=lambda index: index.name or "")
	unique_constraints = [constraint for constraint in table.constraints if constraint.__class__.__name__ == "UniqueConstraint"]
	if indexes:
		lines.extend(["### Indexes", ""])
		for index in indexes:
			columns = ", ".join(f"`{column.name}`" for column in index.columns)
			kind = "unique index" if index.unique else "index"
			lines.append(f"- `{index.name}`: {kind} on {columns}")
		lines.append("")
	if unique_constraints:
		lines.extend(["### Unique Constraints", ""])
		for constraint in unique_constraints:
			columns = ", ".join(f"`{column.name}`" for column in constraint.columns)
			lines.append(f"- `{constraint.name or 'unnamed'}`: {columns}")
		lines.append("")
	foreign_keys = sorted(table.foreign_keys, key=lambda item: item.parent.name)
	if foreign_keys:
		lines.extend(["### Foreign Keys", ""])
		for foreign_key in foreign_keys:
			ondelete = f"; on delete `{foreign_key.ondelete}`" if foreign_key.ondelete else ""
			lines.append(f"- `{foreign_key.parent.name}` -> `{foreign_key.target_fullname}`{ondelete}")
		lines.append("")
	return lines


def render_schema_reference(metadata: MetaData) -> str:
	tables = sorted(metadata.tables.values(), key=lambda item: item.name)
	lines = [
		"# Generated Database Schema Reference",
		"",
		"This file is generated from `backend.database.Base.metadata` by "
		"`scripts/generate_schema_reference.py`. Do not edit it manually.",
		"",
		f"Generated: {datetime.now(timezone.utc).isoformat()}",
		f"Tables: {len(tables)}",
		"",
		"The reference documents the ORM schema declared in this repository. Apply "
		"Alembic migrations for deployment changes; use database inspection as the "
		"final authority for an already-running environment.",
		"",
		"## Entity Relationship Diagram",
		"",
	]
	lines.extend(_erd(metadata))
	lines.extend(["## Table Summary", "", "| Table | Columns | Primary key |", "| --- | ---: | --- |"])
	for table in tables:
		primary_key = ", ".join(f"`{column.name}`" for column in table.primary_key.columns) or "none"
		lines.append(f"| `{table.name}` | {len(table.columns)} | {primary_key} |")
	lines.append("")
	for table in tables:
		lines.extend(_table_reference(table))
	return "\n".join(lines).rstrip() + "\n"


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
	args = parser.parse_args()

	from backend.database import Base

	output = args.output.resolve()
	output.parent.mkdir(parents=True, exist_ok=True)
	output.write_text(render_schema_reference(Base.metadata), encoding="utf-8")
	print(f"generated={output}")


if __name__ == "__main__":
	main()