from __future__ import annotations

from collections.abc import Callable
from hashlib import sha256
from typing import Any

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from .citations import rebuild_citations_for_case, rebuild_statute_references_for_case
from .database import Case, CaseChunk, CaseOutcome, CaseTag, CaseTaggingStatus
from .legal_tagger_v3 import TAXONOMY_VERSION
from .metadata_outcomes import OUTCOME_CLASSIFIER_VERSION, build_case_outcome
from scripts.tag_cases_v3 import build_case_tag_rows
from .metadata import extract_case_metadata
from scripts.chunk_cases import case_text, _build_section_chunks, _build_paragraph_chunks


StageRunner = Callable[[Session, Case], int]


def _run_metadata_layer(session: Session, case: Case) -> int:
    changed = 0
    metadata = dict(case.metadata_json or {})
    extracted = extract_case_metadata(case.full_text or case.summary)
    if metadata.get("reader_extracted") != extracted:
        metadata["reader_extracted"] = extracted
        case.metadata_json = metadata
        changed += 1

    if case.full_text:
        digest = sha256(case.full_text.encode("utf-8")).hexdigest()
        if case.full_text_hash != digest:
            case.full_text_hash = digest
            changed += 1

    if changed:
        session.add(case)
    return changed


def _run_outcome_layer(session: Session, case: Case) -> int:
    metadata = dict(case.metadata_json or {})
    extracted = dict(metadata.get("reader_extracted") or {})
    record = build_case_outcome(case.full_text or case.summary or "", extracted)
    session.execute(
        delete(CaseOutcome).where(
            CaseOutcome.case_id == case.id,
            CaseOutcome.classifier_version == OUTCOME_CLASSIFIER_VERSION,
        )
    )
    session.add(CaseOutcome(case_id=case.id, **record))
    return 1


def _replace_chunk_set(session: Session, case_id: int, chunk_set: str, rows: list[CaseChunk]) -> int:
    session.execute(
        delete(CaseChunk).where(
            CaseChunk.case_id == case_id,
            CaseChunk.chunk_set == chunk_set,
        )
    )
    if rows:
        session.add_all(rows)
    return len(rows)


def _run_full_case_chunk_layer(session: Session, case: Case) -> int:
    text = case_text(case)
    if not text.strip():
        _replace_chunk_set(session, case.id, "full_case", [])
        return 0

    row = CaseChunk(
        case_id=case.id,
        chunk_set="full_case",
        chunk_index=0,
        chunk_label="Full case",
        paragraph_start=None,
        paragraph_end=None,
        text=text,
        text_hash=sha256(text.encode("utf-8")).hexdigest(),
        token_estimate=max(1, len(text) // 4),
    )
    return _replace_chunk_set(session, case.id, "full_case", [row])


def _run_heading_chunk_layer(session: Session, case: Case) -> int:
    text = case_text(case)
    if not text.strip():
        _replace_chunk_set(session, case.id, "section", [])
        _replace_chunk_set(session, case.id, "paragraph", [])
        return 0

    section_rows = _build_section_chunks(case, text)
    paragraph_rows = _build_paragraph_chunks(case, text)
    section_count = _replace_chunk_set(session, case.id, "section", section_rows)
    paragraph_count = _replace_chunk_set(session, case.id, "paragraph", paragraph_rows)
    return section_count + paragraph_count


def _run_case_citation_layer(session: Session, case: Case) -> int:
    chunks = list(
        session.scalars(
            select(CaseChunk)
            .where(CaseChunk.case_id == case.id)
            .order_by(CaseChunk.chunk_set, CaseChunk.chunk_index)
        )
    )
    return rebuild_citations_for_case(session, case, chunks)


def _run_statute_layer(session: Session, case: Case) -> int:
    chunks = list(
        session.scalars(
            select(CaseChunk)
            .where(CaseChunk.case_id == case.id)
            .order_by(CaseChunk.chunk_set, CaseChunk.chunk_index)
        )
    )
    return rebuild_statute_references_for_case(session, case, chunks)


def _run_v3_tag_layer(session: Session, case: Case) -> int:
    """Replace only this case's V3 occurrences while preserving every match."""
    rows = build_case_tag_rows(case.full_text or case.summary or "")
    session.execute(
        delete(CaseTag).where(
            CaseTag.case_id == case.id,
            CaseTag.taxonomy_version == TAXONOMY_VERSION,
        )
    )
    session.execute(
        delete(CaseTaggingStatus).where(
            CaseTaggingStatus.case_id == case.id,
            CaseTaggingStatus.taxonomy_version == TAXONOMY_VERSION,
        )
    )
    session.add_all(CaseTag(case_id=case.id, **row) for row in rows)
    session.add(
        CaseTaggingStatus(
            case_id=case.id,
            taxonomy_version=TAXONOMY_VERSION,
            tags_count=len(rows),
        )
    )
    return len(rows)


STAGES: tuple[tuple[str, StageRunner], ...] = (
    ("full_case", _run_full_case_chunk_layer),
    ("heading_chunks", _run_heading_chunk_layer),
    ("metadata", _run_metadata_layer),
    ("outcome", _run_outcome_layer),
    ("case_citations", _run_case_citation_layer),
    ("statutes", _run_statute_layer),
    ("tags_v3", _run_v3_tag_layer),
)


STAGE_ORDER = tuple(name for name, _runner in STAGES)


def process_case_in_five_layers(
    session: Session,
    case_id: int,
    *,
    stage_order: list[str] | tuple[str, ...] | None = None,
) -> dict[str, int]:
    case = session.scalar(select(Case).where(Case.id == case_id))
    if case is None:
        raise ValueError(f"Case {case_id} not found")

    stage_map: dict[str, StageRunner] = dict(STAGES)
    selected = list(stage_order or STAGE_ORDER)
    invalid = [name for name in selected if name not in stage_map]
    if invalid:
        raise ValueError(f"Unknown stage(s): {', '.join(invalid)}")

    report: dict[str, int] = {}
    for stage_name in selected:
        report[stage_name] = int(stage_map[stage_name](session, case))
    return report
