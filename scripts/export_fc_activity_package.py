"""Export reproducible Federal Court Activity source and derived cohorts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from contextlib import contextmanager
from datetime import date, datetime, timezone
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator, Sequence

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import Select, select, text

from backend.database import FCActivityCase, FCActivityClassification, FCActivityDocument, SessionLocal

EXPORT_VERSION = "fc_activity_package_v2"


@dataclass(frozen=True)
class CohortOptions:
    cohort_name: str | None = None
    year_from: int | None = None
    year_to: int | None = None
    classification_filters: tuple[tuple[str, tuple[str, ...]], ...] = ()
    entry_regexes: tuple[str, ...] = ()
    classification_or_entry_regexes: tuple[str, ...] = ()
    entry_regex_exclude: str | None = None
    no_classification: bool = False
    empty_history: bool = False
    duplicate_court_file: bool = False
    bom: bool = False
    min_entries_matching: tuple[str, int] | None = None
    per_year: int | None = None
    sample_seed: int | None = None
    limit: int | None = None


def _json_default(value: Any) -> str:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return str(value)


def _write_jsonl(handle: Any, record: dict[str, Any]) -> None:
    handle.write(json.dumps(record, ensure_ascii=False, default=_json_default, separators=(",", ":")))
    handle.write("\n")


def _case_record(case: FCActivityCase) -> dict[str, Any]:
    return {
        "activity_case_id": case.id,
        "source_key": case.source_key,
        "citation": case.citation,
        "imm_number": (case.raw_payload or {}).get("imm_number") if case.raw_payload else None,
        "year": case.year,
        "case_name": case.case_name,
        "date_filed": case.date_filed,
        "city_filed": case.city_filed,
        "nature": case.nature,
        "case_class": case.case_class,
        "track": case.track,
        "source_url": case.source_url,
        "scraped_timestamp": case.scraped_timestamp,
        "raw_payload": case.raw_payload,
    }


def _document_record(document: FCActivityDocument) -> dict[str, Any]:
    return {
        "activity_document_id": document.id,
        "activity_case_id": document.case_id,
        "re_no": document.re_no,
        "docno": document.docno,
        "doc_dt": document.doc_dt,
        "recorded_entry": document.recorded_entry,
        "entry_hash": document.entry_hash,
        "raw_document": document.raw_document,
    }


def _classification_record(classification: FCActivityClassification) -> dict[str, Any]:
    return {
        "classification_id": classification.id,
        "activity_case_id": classification.source_case_id,
        "source_key": classification.source_key,
        "imm_number": classification.imm_number,
        "year": classification.year,
        "case_name": classification.case_name,
        "date_filed": classification.date_filed,
        "city_filed": classification.city_filed,
        "nature": classification.nature,
        "case_class": classification.case_class,
        "track": classification.track,
        "source_url": classification.source_url,
        "scraped_timestamp": classification.scraped_timestamp,
        "classifier_version": classification.classifier_version,
        "classified_at": classification.classified_at,
        "updated_at": classification.updated_at,
        "classification": classification.classification_json,
    }


def _normalize_file_number(value: Any) -> str | None:
    if value is None:
        return None
    normalized = str(value).lstrip("\ufeff").strip().upper()
    return normalized or None


def _raw_payload_citation(payload: Any) -> Any:
    return payload.get("citation") if isinstance(payload, dict) else None


def _starts_with_bom(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("\ufeff")


def _json_path(value: Any, path: str) -> Any:
    current = value
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def _matches_classification(value: Any, expected: tuple[str, ...]) -> bool:
    return str(value).casefold() in {item.casefold() for item in expected}


def _entry_match(entry: str | None, patterns: Sequence[re.Pattern[str]], exclude: re.Pattern[str] | None) -> bool:
    if not entry or not patterns:
        return False
    return any(pattern.search(entry) and not (exclude and exclude.search(entry)) for pattern in patterns)


def _case_matches(
    case: dict[str, Any],
    documents: Sequence[dict[str, Any]],
    classifications: Sequence[dict[str, Any]],
    options: CohortOptions,
    duplicate_file_numbers: set[str] | None = None,
) -> bool:
    year = case.get("year")
    if options.year_from is not None and (year is None or year < options.year_from):
        return False
    if options.year_to is not None and (year is None or year > options.year_to):
        return False
    if options.empty_history and documents:
        return False
    if options.no_classification and (not documents or classifications):
        return False
    if options.duplicate_court_file and not duplicate_file_numbers:
        return False
    payload = case.get("raw_payload") or {}
    if options.bom and not any(_starts_with_bom(value) for value in (case.get("citation"), payload.get("imm_number"), payload.get("citation"))):
        return False
    if options.classification_filters:
        for path, expected in options.classification_filters:
            if not any(_matches_classification(_json_path(row.get("classification"), path), expected) for row in classifications):
                return False
    patterns = tuple(re.compile(pattern, re.IGNORECASE) for pattern in options.entry_regexes)
    exclude = re.compile(options.entry_regex_exclude, re.IGNORECASE) if options.entry_regex_exclude else None
    if options.entry_regexes and not any(_entry_match(row.get("recorded_entry"), patterns, exclude) for row in documents):
        return False
    if options.min_entries_matching:
        pattern = re.compile(options.min_entries_matching[0], re.IGNORECASE)
        if sum(bool(pattern.search(row.get("recorded_entry") or "")) for row in documents) < options.min_entries_matching[1]:
            return False
    return True


def _predicate_description(options: CohortOptions) -> str:
    clauses: list[str] = []
    if options.year_from is not None:
        clauses.append(f"year >= {options.year_from}")
    if options.year_to is not None:
        clauses.append(f"year <= {options.year_to}")
    clauses.extend(f"classification[{path}] in {list(values)!r}" for path, values in options.classification_filters)
    if options.entry_regexes:
        clauses.append(f"any entry matches one of {list(options.entry_regexes)!r}")
    if options.entry_regex_exclude:
        clauses.append(f"matching entries do not also match {options.entry_regex_exclude!r}")
    if options.no_classification:
        clauses.append("at least one document and no classification row")
    if options.empty_history:
        clauses.append("zero documents")
    if options.duplicate_court_file:
        clauses.append("normalized citation or fallback IMM is shared by another case")
    if options.bom:
        clauses.append("citation, IMM, or raw payload citation begins with U+FEFF")
    if options.min_entries_matching:
        clauses.append(f"at least {options.min_entries_matching[1]} entries match {options.min_entries_matching[0]!r}")
    return " AND ".join(clauses) if clauses else "all Activity case rows"


def _sample_key(case_source_key: str, seed: int | None) -> str:
    return hashlib.sha256(f"{seed}{case_source_key}".encode("utf-8")).hexdigest() if seed is not None else case_source_key


def _filter_arguments(options: CohortOptions) -> dict[str, Any]:
    return {
        "cohort_name": options.cohort_name,
        "year_from": options.year_from,
        "year_to": options.year_to,
        "classification_filters": [{"path": path, "values": list(values)} for path, values in options.classification_filters],
        "entry_regex": list(options.entry_regexes),
        "classification_or_entry_regex": list(options.classification_or_entry_regexes),
        "entry_regex_exclude": options.entry_regex_exclude,
        "no_classification": options.no_classification,
        "empty_history": options.empty_history,
        "duplicate_court_file": options.duplicate_court_file,
        "bom": options.bom,
        "min_entries_matching": list(options.min_entries_matching) if options.min_entries_matching else None,
        "per_year": options.per_year,
        "limit": options.limit,
        "sample_seed": options.sample_seed,
    }


@contextmanager
def _read_only_session() -> Iterator[Any]:
    session = SessionLocal()
    try:
        with session.begin():
            session.execute(text("SET TRANSACTION READ ONLY"))
            yield session
    finally:
        session.close()


def _candidate_case_ids(session: Any, options: CohortOptions) -> tuple[list[int], dict[int, str], dict[str, list[int]]]:
    all_ids: set[int] = set()
    candidate: set[int] | None = None
    source_keys: dict[int, str] = {}
    court_files: dict[str, list[int]] = defaultdict(list)
    bom_ids: set[int] = set()
    year_ids: set[int] = set()
    case_query = select(FCActivityCase.id, FCActivityCase.source_key, FCActivityCase.citation, FCActivityCase.year, FCActivityCase.raw_payload)
    for case_id, source_key, citation, year, raw_payload in session.execute(case_query).yield_per(5000):
        all_ids.add(case_id)
        source_keys[case_id] = source_key
        if options.year_from is None or (year is not None and year >= options.year_from):
            if options.year_to is None or (year is not None and year <= options.year_to):
                year_ids.add(case_id)
        if options.duplicate_court_file:
            file_number = _normalize_file_number(citation) or _normalize_file_number((raw_payload or {}).get("imm_number") if isinstance(raw_payload, dict) else None)
            if file_number:
                court_files[file_number].append(case_id)
        if options.bom and (_starts_with_bom(citation) or _starts_with_bom((raw_payload or {}).get("imm_number") if isinstance(raw_payload, dict) else None) or _starts_with_bom(_raw_payload_citation(raw_payload))):
            bom_ids.add(case_id)
    candidate = set(all_ids)
    if options.year_from is not None or options.year_to is not None:
        candidate &= year_ids
    if options.bom:
        candidate &= bom_ids
    if options.duplicate_court_file:
        duplicate_ids = {case_id for ids in court_files.values() if len(ids) > 1 for case_id in ids}
        candidate &= duplicate_ids

    doc_counts: Counter[int] = Counter()
    entry_ids: set[int] = set()
    min_entry_counts: Counter[int] = Counter()
    classification_or_entry_ids: set[int] = set()
    entry_patterns = tuple(re.compile(pattern, re.IGNORECASE) for pattern in options.entry_regexes)
    exclude_pattern = re.compile(options.entry_regex_exclude, re.IGNORECASE) if options.entry_regex_exclude else None
    min_pattern = re.compile(options.min_entries_matching[0], re.IGNORECASE) if options.min_entries_matching else None
    classification_or_entry_patterns = tuple(re.compile(pattern, re.IGNORECASE) for pattern in options.classification_or_entry_regexes)
    document_query = select(FCActivityDocument.case_id, FCActivityDocument.recorded_entry).order_by(FCActivityDocument.case_id, FCActivityDocument.id)
    for case_id, recorded_entry in session.execute(document_query).yield_per(10000):
        doc_counts[case_id] += 1
        if _entry_match(recorded_entry, entry_patterns, exclude_pattern):
            entry_ids.add(case_id)
        if min_pattern and recorded_entry and min_pattern.search(recorded_entry):
            min_entry_counts[case_id] += 1
        if classification_or_entry_patterns and any(pattern.search(recorded_entry or "") for pattern in classification_or_entry_patterns):
            classification_or_entry_ids.add(case_id)
    if options.empty_history:
        candidate &= {case_id for case_id in all_ids if doc_counts[case_id] == 0}
    if options.entry_regexes:
        candidate &= entry_ids
    if options.min_entries_matching:
        candidate &= {case_id for case_id, count in min_entry_counts.items() if count >= options.min_entries_matching[1]}
    if options.no_classification:
        classified_ids = {case_id for (case_id,) in session.execute(select(FCActivityClassification.source_case_id)).yield_per(10000)}
        candidate &= {case_id for case_id, count in doc_counts.items() if count > 0 and case_id not in classified_ids}

    if options.classification_filters:
        for path, expected in options.classification_filters:
            matching: set[int] = set()
            query = select(FCActivityClassification.source_case_id, FCActivityClassification.classification_json)
            for case_id, classification_json in session.execute(query).yield_per(5000):
                if _matches_classification(_json_path(classification_json, path), expected):
                    matching.add(case_id)
            candidate &= matching
    if options.classification_or_entry_regexes:
        classification_ids: set[int] = set()
        for path, expected in options.classification_filters:
            query = select(FCActivityClassification.source_case_id, FCActivityClassification.classification_json)
            classification_ids.update(
                case_id
                for case_id, classification_json in session.execute(query).yield_per(5000)
                if _matches_classification(_json_path(classification_json, path), expected)
            )
        candidate &= classification_ids | classification_or_entry_ids
    duplicate_groups = {
        file_number: [case_id for case_id in case_ids if case_id in candidate]
        for file_number, case_ids in court_files.items()
        if len(case_ids) > 1
    }
    return sorted(candidate), source_keys, duplicate_groups


def _select_ids(session: Any, options: CohortOptions) -> tuple[list[int], int, dict[int, str]]:
    candidate_ids, source_keys, duplicate_groups = _candidate_case_ids(session, options)
    total_matching = len(candidate_ids)
    ordered = sorted(candidate_ids, key=lambda case_id: (_sample_key(source_keys[case_id], options.sample_seed), case_id))
    if options.per_year:
        years = {case_id: year for case_id, year in session.execute(select(FCActivityCase.id, FCActivityCase.year).where(FCActivityCase.id.in_(ordered))).yield_per(5000)} if ordered else {}
        per_year_counts: Counter[Any] = Counter()
        stratified: list[int] = []
        for case_id in ordered:
            if per_year_counts[years.get(case_id)] < options.per_year:
                stratified.append(case_id)
                per_year_counts[years.get(case_id)] += 1
        ordered = stratified
    if options.limit is not None:
        if options.duplicate_court_file:
            groups = sorted(
                duplicate_groups.values(),
                key=lambda group: min(_sample_key(source_keys[case_id], options.sample_seed) for case_id in group),
            )
            ordered = [case_id for group in groups[: options.limit] for case_id in sorted(group)]
        else:
            ordered = ordered[: options.limit]
    return ordered, total_matching, source_keys


def _git_commit() -> str | None:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=PROJECT_ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def _manifest(*, counts: dict[str, int], classifier_versions: list[str], options: CohortOptions, total_matching: int) -> dict[str, Any]:
    return {
        "export_version": EXPORT_VERSION,
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "cohort_name": options.cohort_name,
        "filter_arguments": _filter_arguments(options),
        "predicate_description": _predicate_description(options),
        "total_matching_cases_before_sampling": total_matching,
        "exported_case_count": counts.get("cases", 0),
        "sample_seed": options.sample_seed,
        "git_commit": _git_commit(),
        "selection": {"case_limit": options.limit, "limit_semantics": "duplicate mode limits groups; otherwise Activity case rows", "per_year": options.per_year},
        "counts": counts,
        "classifier_versions": classifier_versions,
        "source_tables": ["fc_activity_cases", "fc_activity_documents", "fc_activity_classifications"],
        "relationships": {"documents.activity_case_id": "cases.activity_case_id", "classifications.activity_case_id": "cases.activity_case_id", "source_key": "stable source identity; database row IDs remain included for joins"},
        "provenance": {"layer_boundary": "Federal Court Activity is procedural history, not canonical judgment or citation data", "raw_source_fields": "raw_payload and raw_document are preserved exactly as stored", "derived_fields": "classification is deterministic output and must not be treated as an authoritative legal conclusion", "jsonl_encoding": "UTF-8 without BOM"},
        "known_limitations": ["A missing classification row means the case was not classified or classification was not persisted.", "Document identity follows the database registry identity and entry-hash deduplication rules.", "BOM-prefixed IMM values are retained and should be normalized only for matching.", "Empty document lists do not prove no procedural history exists outside the captured response."],
        "files": {"cases.jsonl": "source fc_activity_cases rows including raw_payload", "documents.jsonl": "source fc_activity_documents rows including raw_document", "classifications.jsonl": "derived fc_activity_classifications rows"},
    }


def export_package(output: Path, options: CohortOptions | None = None, limit: int | None = None) -> dict[str, Any]:
    options = options or CohortOptions(limit=limit)
    output.mkdir(parents=True, exist_ok=False)
    case_path, document_path, classification_path = output / "cases.jsonl", output / "documents.jsonl", output / "classifications.jsonl"
    counts = Counter(cases=0, documents=0, classifications=0)
    classifier_versions: set[str] = set()
    case_ids_with_documents: set[int] = set()
    with _read_only_session() as session:
        selected_ids, total_matching, _ = _select_ids(session, options)
        case_query: Select[tuple[FCActivityCase]] = select(FCActivityCase).where(FCActivityCase.id.in_(selected_ids)).order_by(FCActivityCase.id) if selected_ids else select(FCActivityCase).where(False)
        with case_path.open("w", encoding="utf-8", newline="\n") as handle:
            for case in session.scalars(case_query).yield_per(1000):
                counts["cases"] += 1
                _write_jsonl(handle, _case_record(case))
        document_query = select(FCActivityDocument).where(FCActivityDocument.case_id.in_(selected_ids)).order_by(FCActivityDocument.case_id, FCActivityDocument.id) if selected_ids else select(FCActivityDocument).where(False)
        with document_path.open("w", encoding="utf-8", newline="\n") as handle:
            for document in session.scalars(document_query).yield_per(5000):
                counts["documents"] += 1
                case_ids_with_documents.add(document.case_id)
                _write_jsonl(handle, _document_record(document))
        classification_query = select(FCActivityClassification).where(FCActivityClassification.source_case_id.in_(selected_ids)).order_by(FCActivityClassification.source_case_id, FCActivityClassification.id) if selected_ids else select(FCActivityClassification).where(False)
        with classification_path.open("w", encoding="utf-8", newline="\n") as handle:
            for classification in session.scalars(classification_query).yield_per(5000):
                counts["classifications"] += 1
                classifier_versions.add(classification.classifier_version)
                _write_jsonl(handle, _classification_record(classification))
    counts["cases_with_documents"] = len(case_ids_with_documents)
    counts["cases_without_documents"] = counts["cases"] - counts["cases_with_documents"]
    manifest = _manifest(counts=dict(counts), classifier_versions=sorted(classifier_versions), options=options, total_matching=total_matching)
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2, default=_json_default) + "\n", encoding="utf-8")
    return manifest


def _parse_classification_filters(paths: list[str], values: list[str]) -> tuple[tuple[str, tuple[str, ...]], ...]:
    if len(paths) != len(values):
        raise SystemExit("--classification-path and --classification-value must be supplied in matching pairs")
    return tuple((path, tuple(value.split(","))) for path, value in zip(paths, values))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--cohort-name")
    parser.add_argument("--year-from", type=int)
    parser.add_argument("--year-to", type=int)
    parser.add_argument("--classification-path", action="append", default=[])
    parser.add_argument("--classification-value", action="append", default=[])
    parser.add_argument("--entry-regex", action="append", default=[])
    parser.add_argument("--classification-or-entry-regex", action="append", default=[])
    parser.add_argument("--entry-regex-exclude")
    parser.add_argument("--no-classification", action="store_true")
    parser.add_argument("--empty-history", action="store_true")
    parser.add_argument("--duplicate-court-file", action="store_true")
    parser.add_argument("--bom", action="store_true")
    parser.add_argument("--min-entries-matching")
    parser.add_argument("--per-year", type=int)
    parser.add_argument("--sample-seed", type=int)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.output.exists():
        raise SystemExit(f"Refusing to overwrite existing output directory: {args.output}")
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be a positive integer")
    minimum = None
    if args.min_entries_matching:
        try:
            pattern, count = args.min_entries_matching.rsplit(":", 1)
            minimum = (pattern, int(count))
        except ValueError as exc:
            raise SystemExit("--min-entries-matching must be REGEX:N") from exc
    options = CohortOptions(cohort_name=args.cohort_name, year_from=args.year_from, year_to=args.year_to, classification_filters=_parse_classification_filters(args.classification_path, args.classification_value), entry_regexes=tuple(args.entry_regex), classification_or_entry_regexes=tuple(args.classification_or_entry_regex), entry_regex_exclude=args.entry_regex_exclude, no_classification=args.no_classification, empty_history=args.empty_history, duplicate_court_file=args.duplicate_court_file, bom=args.bom, min_entries_matching=minimum, per_year=args.per_year, sample_seed=args.sample_seed, limit=args.limit)
    manifest = export_package(args.output, options)
    print(json.dumps(manifest["counts"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
