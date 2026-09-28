"""Produce counts-only coverage metrics for the Federal Court Activity tables."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import select, text

from backend.database import (
    FCActivityCase,
    FCActivityClassification,
    FCActivityDocument,
    SessionLocal,
)


def _value(payload: dict[str, Any] | None, key: str) -> Any:
    return payload.get(key) if isinstance(payload, dict) else None


def _is_bom(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("\ufeff")


def _status_counts(value: Any, counts: Counter[str]) -> None:
    if not isinstance(value, dict):
        return
    status = value.get("status")
    if status is not None:
        counts[str(status)] += 1


def build_report() -> dict[str, Any]:
    cases: list[FCActivityCase] = []
    documents_by_case: defaultdict[int, list[FCActivityDocument]] = defaultdict(list)
    classifications: list[FCActivityClassification] = []
    with SessionLocal() as session:
        session.execute(text("SET TRANSACTION READ ONLY"))
        cases = list(session.scalars(select(FCActivityCase).order_by(FCActivityCase.id)))
        for document in session.scalars(select(FCActivityDocument).order_by(FCActivityDocument.case_id, FCActivityDocument.id)):
            documents_by_case[document.case_id].append(document)
        classifications = list(session.scalars(select(FCActivityClassification).order_by(FCActivityClassification.id)))

    classification_by_case: defaultdict[int, list[FCActivityClassification]] = defaultdict(list)
    case_by_id = {case.id: case for case in cases}
    versions = Counter[str]()
    top_level_status: defaultdict[str, Counter[str]] = defaultdict(Counter)
    classified_before_scraped = 0
    for row in classifications:
        classification_by_case[row.source_case_id].append(row)
        versions[str(row.classifier_version)] += 1
        case = case_by_id.get(row.source_case_id)
        if case and row.classified_at and case.scraped_timestamp and row.classified_at < case.scraped_timestamp:
            classified_before_scraped += 1
        if isinstance(row.classification_json, dict):
            for key, value in row.classification_json.items():
                _status_counts(value, top_level_status[key])

    year_counts = Counter[str]()
    unclassified_by_year = Counter[str]()
    nulls = Counter[str]()
    bom_fields = Counter[str]()
    timestamp = Counter[str]()
    raw_payload_comparison = Counter[str]()
    duplicate_entry_hashes = set[str]()
    seen_entry_hashes: dict[str, int] = {}
    null_docno = 0
    order_disagreement = 0
    citation_imm_different = 0
    for case in cases:
        year_counts[str(case.year) if case.year is not None else "null"] += 1
        if not classification_by_case[case.id]:
            unclassified_by_year[str(case.year) if case.year is not None else "null"] += 1
        payload = case.raw_payload if isinstance(case.raw_payload, dict) else {}
        imm_number = _value(payload, "imm_number")
        if imm_number is None:
            nulls["imm_number"] += 1
        if case.citation is None:
            nulls["citation"] += 1
        if imm_number is not None and case.citation is not None and str(imm_number) != str(case.citation):
            citation_imm_different += 1
        for field, value in (("citation", case.citation), ("imm_number", imm_number)):
            if _is_bom(value):
                bom_fields[field] += 1

        documents = documents_by_case[case.id]
        if not documents:
            nulls["documents"] += 1
        doc_dates = [document.doc_dt for document in documents if document.doc_dt is not None]
        if len(doc_dates) != len(documents):
            timestamp["null_doc_dt"] += 1
        if doc_dates and doc_dates != sorted(doc_dates):
            timestamp["out_of_order_doc_dt"] += 1
        if len(doc_dates) > 1:
            timestamp["comparable_cases"] += 1

        re_order = [str(document.re_no or "") for document in documents]
        date_order = [document.doc_dt for document in documents]
        if len(documents) > 1 and all(value is not None for value in date_order):
            re_sorted = sorted(range(len(documents)), key=lambda index: re_order[index])
            date_sorted = sorted(range(len(documents)), key=lambda index: date_order[index])
            if re_sorted != date_sorted:
                order_disagreement += 1

        payload_documents = payload.get("entries_json", payload.get("documents"))
        if isinstance(payload_documents, list):
            raw_count = len(payload_documents)
            raw_payload_comparison["comparable_cases"] += 1
            if raw_count == len(documents):
                raw_payload_comparison["equal"] += 1
            else:
                raw_payload_comparison["mismatch"] += 1

        case_hashes = Counter[str]()
        for document in documents:
            if document.docno is None:
                null_docno += 1
            if _is_bom(document.docno):
                bom_fields["docno"] += 1
            if _is_bom(document.re_no):
                bom_fields["re_no"] += 1
            if _is_bom(document.doc_dt):
                bom_fields["doc_dt"] += 1
            if _is_bom(document.recorded_entry):
                bom_fields["recorded_entry"] += 1
            if document.entry_hash:
                case_hashes[document.entry_hash] += 1
                previous_case = seen_entry_hashes.get(document.entry_hash)
                if previous_case is not None and previous_case != case.id:
                    duplicate_entry_hashes.add(document.entry_hash)
                seen_entry_hashes[document.entry_hash] = case.id
        if any(count > 1 for count in case_hashes.values()):
            duplicate_entry_hashes.update(hash_value for hash_value, count in case_hashes.items() if count > 1)

    classification_distribution = Counter[str](str(len(rows)) for rows in classification_by_case.values())
    classification_distribution["0"] = sum(1 for case in cases if not classification_by_case[case.id])
    return {
        "cases": {"total": len(cases), "by_year": dict(sorted(year_counts.items()))},
        "documents": {"total": sum(len(rows) for rows in documents_by_case.values()), "null_docno": null_docno},
        "classifications": {
            "total": len(classifications),
            "rows_per_case": dict(sorted(classification_distribution.items(), key=lambda item: int(item[0]))),
            "versions": dict(sorted(versions.items())),
            "classified_before_case_created_at": classified_before_scraped,
            "top_level_status_counts": {key: dict(sorted(value.items())) for key, value in sorted(top_level_status.items())},
        },
        "unclassified_by_year": dict(sorted(unclassified_by_year.items())),
        "null_or_different_imm_and_citation": {
            "null_imm_number": nulls["imm_number"],
            "null_citation": nulls["citation"],
            "cases_both_present_but_different": citation_imm_different,
        },
        "bom_fields": dict(sorted(bom_fields.items())),
        "hash_duplication": {"duplicate_entry_hash_values": len(duplicate_entry_hashes)},
        "timestamp_ordering": dict(sorted(timestamp.items())),
        "re_no_vs_doc_dt_order_disagreement": order_disagreement,
        "raw_payload_document_count_comparison": dict(sorted(raw_payload_comparison.items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit(f"refusing to overwrite existing output: {args.output}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build_report(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
