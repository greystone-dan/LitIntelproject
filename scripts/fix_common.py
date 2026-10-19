"""Shared helpers for the scripts/fix_*.py database repair scripts (undo files, batching).

Every fix script is a dry run unless --apply is given, writes an undo file BEFORE it changes anything, and can
put the rows back with --undo FILE. Undo files are JSON lines (one row per line) in data/db_fix_backups/
(ignored by git).
"""

from __future__ import annotations

import json
import os
from collections.abc import Iterable, Iterator, Sequence
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BACKUP_DIR = PROJECT_ROOT / "data" / "db_fix_backups"


def default_undo_path(name: str, backup_dir: Path | None = None) -> Path:
	"""A new timestamped undo file path, for example data/db_fix_backups/self_citations_20261019T120000Z.jsonl."""
	stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
	return (backup_dir or DEFAULT_BACKUP_DIR) / f"{name}_{stamp}.jsonl"


def _json_default(value: Any) -> str:
	if isinstance(value, (datetime, date)):
		return value.isoformat()
	raise TypeError(f"cannot write {type(value).__name__} to an undo file")


def write_undo_file(path: Path, rows: Iterable[dict[str, Any]]) -> int:
	"""Write rows as JSON lines, flush to disk, and return how many were written. Refuses to overwrite a file."""
	path.parent.mkdir(parents=True, exist_ok=True)
	count = 0
	with open(path, "x", encoding="utf-8") as handle:
		for row in rows:
			handle.write(json.dumps(dict(row), default=_json_default, ensure_ascii=False) + "\n")
			count += 1
		handle.flush()
		os.fsync(handle.fileno())
	return count


def read_undo_file(path: Path) -> Iterator[dict[str, Any]]:
	with open(path, encoding="utf-8") as handle:
		for line in handle:
			line = line.strip()
			if line:
				yield json.loads(line)


def count_lines(path: Path) -> int:
	return sum(1 for _ in read_undo_file(path))


def chunked(items: Sequence[Any], size: int) -> Iterator[Sequence[Any]]:
	if size < 1:
		raise ValueError("batch size must be at least 1")
	for start in range(0, len(items), size):
		yield items[start : start + size]
