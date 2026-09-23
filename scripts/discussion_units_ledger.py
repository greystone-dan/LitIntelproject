"""Atomic, report-only ledger for resumable Discussion Unit runs."""

from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any

TERMINAL_STATUSES = frozenset({"complete", "failed"})


def _now() -> str:
	return datetime.now(timezone.utc).isoformat()


def read_ledger(path: Path) -> dict[str, Any]:
	if not path.exists():
		return {"ledger_version": 1, "updated_at": _now(), "cases": {}}
	data = json.loads(path.read_text(encoding="utf-8"))
	if not isinstance(data, dict) or not isinstance(data.get("cases"), dict):
		raise ValueError(f"invalid Discussion Unit ledger: {path}")
	return data


def write_ledger(path: Path, data: dict[str, Any]) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	data["updated_at"] = _now()
	with NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
		json.dump(data, handle, indent=2, ensure_ascii=True)
		handle.write("\n")
		temporary = Path(handle.name)
	os.replace(temporary, path)


def get_case(path: Path, case_id: int) -> dict[str, Any] | None:
	return read_ledger(path)["cases"].get(str(case_id))


def should_skip(path: Path, case_id: int, *, retry_failed: bool = False) -> bool:
	row = get_case(path, case_id)
	if not row or row.get("status") not in TERMINAL_STATUSES:
		return False
	return row["status"] != "failed" or not retry_failed


def record_case(path: Path, case_id: int, status: str, **fields: Any) -> dict[str, Any]:
	data = read_ledger(path)
	row = {"case_id": case_id, "status": status, "updated_at": _now(), **fields}
	data["cases"][str(case_id)] = row
	write_ledger(path, data)
	return row