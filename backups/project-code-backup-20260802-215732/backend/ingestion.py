from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from typing import Any, Literal

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from .database import Case, CaseSource, IngestionRun
from .models import CaseIngestRequest

SOURCE_PRIORITIES = {
    "federal_court": 400,
    "fc_scraper": 400,
    "official_court": 400,
    "canlii_html_seed": 300,
    "canlii": 300,
    "a2aj_parquet": 200,
    "a2aj_api_seed": 200,
    "a2aj_curated": 200,
    "a2aj_immigration_core": 200,
    "huggingface": 200,
    "canlii_html_seed_fallback": 200,
    "synthetic": 10,
}

CANONICAL_FIELDS = (
    "title",
    "court",
    "jurisdiction",
    "date",
    "citation",
    "secondary_citation",
    "summary",
    "full_text",
    "source_url",
    "source_name",
    "source_id",
    "dataset_version",
    "upstream_license",
    "scraped_at",
    "language",
)


def source_priority(source_type: str | None) -> int:
    normalized = (source_type or "").strip().lower()
    if normalized in SOURCE_PRIORITIES:
        return SOURCE_PRIORITIES[normalized]
    if normalized.startswith("federal_court") or normalized.startswith("official"):
        return 400
    if normalized.startswith("canlii") and "fallback" not in normalized:
        return 300
    if normalized.startswith("a2aj") or normalized.startswith("huggingface"):
        return 200
    return 100 if normalized else 0


def _json_value(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {str(key): _json_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_value(item) for item in value]
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


def merge_metadata(
    existing: dict[str, Any] | None,
    incoming: dict[str, Any] | None,
    *,
    source_type: str | None,
) -> dict[str, Any]:
    merged = deepcopy(existing or {})
    conflicts = list(merged.pop("_source_conflicts", []) or [])

    def merge_mapping(target: dict[str, Any], additions: dict[str, Any], prefix: str = "") -> None:
        for key, raw_value in additions.items():
            if key == "_source_conflicts":
                continue
            value = _json_value(raw_value)
            path = f"{prefix}.{key}" if prefix else key
            if key not in target or target[key] in (None, "", [], {}):
                target[key] = deepcopy(value)
            elif isinstance(target[key], dict) and isinstance(value, dict):
                merge_mapping(target[key], value, path)
            elif target[key] != value:
                conflict = {
                    "path": path,
                    "existing": _json_value(target[key]),
                    "incoming": value,
                    "source_type": source_type or "unknown",
                }
                if conflict not in conflicts:
                    conflicts.append(conflict)

    merge_mapping(merged, incoming or {})
    if conflicts:
        merged["_source_conflicts"] = conflicts
    return merged


def _merge_unique(existing: list[Any] | None, incoming: list[Any] | None) -> list[Any] | None:
    if not existing and not incoming:
        return None
    result = []
    seen = set()
    for value in [*(existing or []), *(incoming or [])]:
        marker = str(value).strip().casefold()
        if marker and marker not in seen:
            seen.add(marker)
            result.append(value)
    return result


def merge_case_fields(existing: Case, incoming: CaseIngestRequest) -> set[str]:
    changed: set[str] = set()
    existing_priority = source_priority(existing.source_type)
    incoming_priority = source_priority(incoming.source_type)
    incoming_is_preferred = incoming_priority > existing_priority

    for field in CANONICAL_FIELDS:
        incoming_value = getattr(incoming, field)
        existing_value = getattr(existing, field)
        should_fill = existing_value in (None, "") and incoming_value not in (None, "")
        should_replace = incoming_is_preferred and incoming_value not in (None, "")
        if (should_fill or should_replace) and existing_value != incoming_value:
            setattr(existing, field, incoming_value)
            changed.add(field)

    for field in ("issues", "cases_cited", "cases_citing"):
        merged = _merge_unique(getattr(existing, field), getattr(incoming, field))
        if merged != getattr(existing, field):
            setattr(existing, field, merged)
            changed.add(field)

    if incoming.citing_cases_count is not None:
        merged_count = max(existing.citing_cases_count or 0, incoming.citing_cases_count)
        if merged_count != existing.citing_cases_count:
            existing.citing_cases_count = merged_count
            changed.add("citing_cases_count")

    metadata = merge_metadata(
        existing.metadata_json,
        incoming.metadata_json,
        source_type=incoming.source_type,
    )
    if metadata != (existing.metadata_json or {}):
        existing.metadata_json = metadata
        changed.add("metadata_json")

    if incoming_is_preferred and incoming.source_type != existing.source_type:
        existing.source_type = incoming.source_type
        changed.add("source_type")

    if existing.full_text:
        calculated_hash = sha256(existing.full_text.encode("utf-8")).hexdigest()
        if calculated_hash != existing.full_text_hash:
            existing.full_text_hash = calculated_hash
            changed.add("full_text_hash")

    return changed


def _find_existing_case(db: Session, incoming: CaseIngestRequest) -> Case | None:
    full_text_hash = (
        sha256(incoming.full_text.encode("utf-8")).hexdigest() if incoming.full_text else None
    )
    if full_text_hash:
        match = db.scalar(select(Case).where(Case.full_text_hash == full_text_hash).limit(1))
        if match:
            return match

    if incoming.citation:
        match = db.scalar(
            select(Case)
            .where(func.lower(Case.citation) == incoming.citation.strip().lower())
            .order_by(Case.id)
            .limit(1)
        )
        if match:
            return match

    if incoming.source_id:
        match = db.scalar(
            select(Case)
            .join(CaseSource, CaseSource.case_id == Case.id)
            .where(
                CaseSource.source_type == (incoming.source_type or "unknown"),
                CaseSource.source_id == incoming.source_id,
            )
            .order_by(Case.id)
            .limit(1)
        )
        if match:
            return match
    return None


def _new_case(incoming: CaseIngestRequest) -> Case:
    full_text_hash = (
        sha256(incoming.full_text.encode("utf-8")).hexdigest() if incoming.full_text else None
    )
    return Case(
        title=incoming.title,
        court=incoming.court,
        jurisdiction=incoming.jurisdiction,
        date=incoming.date,
        citation=incoming.citation,
        secondary_citation=incoming.secondary_citation,
        summary=incoming.summary,
        full_text=incoming.full_text,
        issues=incoming.issues,
        metadata_json=incoming.metadata_json,
        source_url=incoming.source_url,
        source_name=incoming.source_name,
        source_id=incoming.source_id,
        source_type=incoming.source_type,
        dataset_version=incoming.dataset_version,
        upstream_license=incoming.upstream_license,
        scraped_at=incoming.scraped_at,
        language=incoming.language,
        full_text_hash=full_text_hash,
        processing_status="raw",
        cases_cited=incoming.cases_cited,
        cases_citing=incoming.cases_citing,
        citing_cases_count=incoming.citing_cases_count,
    )


def _upsert_source(db: Session, case: Case, incoming: CaseIngestRequest, *, primary: bool) -> None:
    source_type = (incoming.source_type or "unknown").strip() or "unknown"
    identity_filters = []
    if incoming.source_id:
        identity_filters.append(CaseSource.source_id == incoming.source_id)
    if incoming.source_url:
        identity_filters.append(CaseSource.source_url == incoming.source_url)

    source = None
    if identity_filters:
        source = db.scalar(
            select(CaseSource)
            .where(
                CaseSource.case_id == case.id,
                CaseSource.source_type == source_type,
                or_(*identity_filters),
            )
            .order_by(CaseSource.id)
            .limit(1)
        )

    raw_hash = sha256(incoming.full_text.encode("utf-8")).hexdigest() if incoming.full_text else None
    if source is None:
        source = CaseSource(
            case_id=case.id,
            source_type=source_type,
            source_name=incoming.source_name,
            source_id=incoming.source_id,
            source_url=incoming.source_url,
            dataset_version=incoming.dataset_version,
            upstream_license=incoming.upstream_license,
            scraped_at=incoming.scraped_at,
            is_primary=primary,
            raw_hash=raw_hash,
            metadata_json=incoming.metadata_json or None,
        )
        db.add(source)
        return

    for field in (
        "source_name",
        "source_id",
        "source_url",
        "dataset_version",
        "upstream_license",
        "scraped_at",
        "raw_hash",
    ):
        value = raw_hash if field == "raw_hash" else getattr(incoming, field)
        if value not in (None, ""):
            setattr(source, field, value)
    source.metadata_json = merge_metadata(
        source.metadata_json,
        incoming.metadata_json,
        source_type=source_type,
    )
    source.is_primary = source.is_primary or primary


def merge_case_record(
    db: Session,
    incoming: CaseIngestRequest,
) -> tuple[Case, Literal["created", "merged"], set[str]]:
    case = _find_existing_case(db, incoming)
    if case is None:
        case = _new_case(incoming)
        db.add(case)
        db.flush()
        action: Literal["created", "merged"] = "created"
        changed = set(CANONICAL_FIELDS)
        primary = True
    else:
        action = "merged"
        previous_priority = source_priority(case.source_type)
        changed = merge_case_fields(case, incoming)
        primary = source_priority(incoming.source_type) > previous_priority
        if primary:
            for source in case.sources:
                source.is_primary = False

    _upsert_source(db, case, incoming, primary=primary)
    db.add(
        IngestionRun(
            source_type=(incoming.source_type or "unknown").strip() or "unknown",
            source_name=incoming.source_name,
            run_type="merge_ingest",
            status="completed",
            records_seen=1,
            records_ingested=1 if action == "created" else 0,
            records_updated=1 if action == "merged" and changed else 0,
            records_failed=0,
            metadata_json={
                "case_id": case.id,
                "citation": incoming.citation,
                "action": action,
                "changed_fields": sorted(changed),
            },
        )
    )
    db.commit()
    db.refresh(case)
    return case, action, changed
