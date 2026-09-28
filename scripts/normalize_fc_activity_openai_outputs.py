"""Normalize open-ended FC Activity model outputs for evaluation only."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterator


FILING_KEYS = ("filing_date", "filed_date", "file_date", "date_filed", "application_date")
DATE_KEYS = ("decision_date", "order_date", "result_date", "date")
DECISION_TYPE_KEYS = ("decision_type", "type", "decision_description", "decision_text", "details")
MOTION_KEYS = ("motions", "motion", "motion_events", "procedural_motions")
JUDGE_KEYS = ("judge", "judges", "decision_maker")


def scalar(value: Any) -> str | None:
    return value if isinstance(value, str) and value.strip() else None


def walk(value: Any, path: str = "") -> Iterator[tuple[str, Any]]:
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else key
            yield from walk(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def first_string(mapping: dict[str, Any], keys: tuple[str, ...]) -> tuple[str | None, str | None]:
    for key in keys:
        value = scalar(mapping.get(key))
        if value:
            return value, key
    return None, None


def filing_date(extraction: dict[str, Any]) -> tuple[str | None, str | None]:
    application = extraction.get("application")
    if isinstance(application, dict):
        value, key = first_string(application, FILING_KEYS)
        if value:
            return value, f"application.{key}"
    for path, value in walk(extraction):
        if path.endswith((".filing_date", ".filed_date", ".file_date", ".date_filed", ".application_date")):
            candidate = scalar(value)
            if candidate:
                return candidate, path
    return None, None


def decision_fields(extraction: dict[str, Any]) -> dict[str, Any]:
    blocks: list[tuple[str, dict[str, Any]]] = []
    direct = extraction.get("challenged_decision")
    if isinstance(direct, dict):
        blocks.append(("challenged_decision", direct))
    for path, value in walk(extraction):
        if path.endswith(".challenged_decision") and isinstance(value, dict):
            blocks.append((path, value))
    date: str | None = None
    date_key: str | None = None
    for block_path, block in blocks:
        date, local_key = first_string(block, ("decision_date", "order_date", "result_date", "date"))
        if date:
            date_key = f"{block_path}.{local_key}"
            break
    if not date:
        for path, value in walk(extraction):
            if path.endswith((".decision_date", ".order_date", ".result_date")):
                date = scalar(value)
                if date:
                    date_key = path
                    break
    decision_type: str | None = None
    type_key: str | None = None
    for block_path, block in blocks:
        decision_type, local_key = first_string(block, ("decision_type",))
        if decision_type:
            type_key = f"{block_path}.{local_key}"
            break
        for path, value in walk(block):
            if path.endswith((".decision_description", ".decision_text", ".details", ".type")):
                candidate = scalar(value)
                if candidate:
                    decision_type = candidate
                    type_key = f"{block_path}.{path}" if path else block_path
                    break
        if decision_type:
            break
    if decision_type and decision_type.lower() == "unknown":
        decision_type = None
    return {
        "decision_date": date,
        "decision_date_source": date_key,
        "decision_type": decision_type,
        "decision_type_source": type_key,
    }


def judge_rows(extraction: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str | None]] = set()
    for path, value in walk(extraction):
        key = path.rsplit(".", 1)[-1].split("[")[0]
        if key not in JUDGE_KEYS:
            continue
        values = value if isinstance(value, list) else [value]
        for item in values:
            if isinstance(item, dict):
                name = scalar(item.get("name")) or scalar(item.get("judge")) or scalar(item.get("decision_maker"))
                stage = scalar(item.get("stage"))
                date, _ = first_string(item, DATE_KEYS)
            else:
                name = scalar(item)
                stage = None
                date = None
            if not name or name.lower() in {"unknown", "none"}:
                continue
            identity = (name, date)
            if identity in seen:
                continue
            seen.add(identity)
            rows.append({"name": name, "stage": stage, "date": date, "source_path": path})
    return rows


def motion_rows(extraction: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path, value in walk(extraction):
        key = path.rsplit(".", 1)[-1].split("[")[0]
        if key not in MOTION_KEYS or not isinstance(value, list):
            continue
        for item in value:
            if not isinstance(item, dict):
                continue
            date, date_key = first_string(item, ("filing_date", "filed_date", "date_filed", "motion_date", "date"))
            motion_type, type_key = first_string(item, ("type", "motion_type", "request", "description", "motion_description"))
            result, result_key = first_string(item, ("result", "outcome", "effect"))
            if not any((date, motion_type, result)):
                continue
            rows.append({
                "reference": scalar(item.get("reference")) or scalar(item.get("document_id")) or scalar(item.get("doc_id")),
                "filing_date": date,
                "type": motion_type,
                "result": result,
                "result_date": scalar(item.get("result_date")),
                "evidence_doc_id": item.get("evidence_doc_id") if isinstance(item.get("evidence_doc_id"), int) else None,
                "source_path": path,
                "field_sources": {"date": date_key, "type": type_key, "result": result_key},
            })
    return rows


def normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    extraction = record.get("extraction")
    if not isinstance(extraction, dict):
        extraction = {}
    case = extraction.get("case") if isinstance(extraction.get("case"), dict) else {}
    activity_case_id = case.get("activity_case_id") or extraction.get("activity_case_id") or record.get("activity_case_id")
    imm_number = case.get("imm_number") or extraction.get("imm_number") or record.get("imm_number")
    filing, filing_source = filing_date(extraction)
    decisions = decision_fields(extraction)
    judges = judge_rows(extraction)
    motions = motion_rows(extraction)
    missing = []
    if not filing:
        missing.append("filing_date")
    if not decisions["decision_date"]:
        missing.append("decision_date")
    if not decisions["decision_type"]:
        missing.append("decision_type")
    if not judges:
        missing.append("judges")
    if not motions:
        missing.append("motions")
    return {
        "activity_case_id": activity_case_id,
        "imm_number": imm_number,
        "source_status": record.get("status"),
        "source_cost_usd": record.get("cost_usd"),
        "filing_date": filing,
        "filing_date_source": filing_source,
        **decisions,
        "judges": judges,
        "motions": motions,
        "normalization_missing": missing,
    }


def normalize_artifact(path: Path) -> dict[str, Any]:
    artifact = json.loads(path.read_text(encoding="utf-8"))
    records = [normalize_record(record) for record in artifact.get("results", [])]
    return {
        "source_artifact": str(path),
        "model": artifact.get("model"),
        "sample_size": artifact.get("sample_size"),
        "completed_count": artifact.get("completed_count"),
        "failure_count": artifact.get("failure_count"),
        "normalized_records": records,
        "coverage": {
            "filing_date": sum(bool(record["filing_date"]) for record in records),
            "decision_date": sum(bool(record["decision_date"]) for record in records),
            "decision_type": sum(bool(record["decision_type"]) for record in records),
            "judges": sum(bool(record["judges"]) for record in records),
            "motions": sum(bool(record["motions"]) for record in records),
            "motion_rows": sum(len(record["motions"]) for record in records),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {"artifacts": [normalize_artifact(path) for path in args.input]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({
        artifact["model"]: artifact["coverage"] for artifact in result["artifacts"]
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
