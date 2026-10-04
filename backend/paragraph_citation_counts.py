"""Read-only, later-decision pinpoint coverage for actual formatted paragraphs.

This additive projection deliberately does not change the legacy reader counts.
It reads resolved case-citation rows, never statutes, chunks, or inferred offsets.
"""

import re
from collections.abc import Iterable
from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from .case_formatter import format_decision
from .database import Case, Citation, get_db

router = APIRouter(tags=["cases"])


def distinct_citing_cases_by_paragraph(rows: Iterable[tuple[int | None, int | None]], case_id: int) -> dict[int, int]:
    """Shared legacy-compatible distinct-source fold; eligibility is caller-owned."""
    sources_by_paragraph: dict[int, set[int]] = {}
    for source_case_id, paragraph in rows:
        if source_case_id is None or source_case_id == case_id or paragraph is None:
            continue
        sources_by_paragraph.setdefault(int(paragraph), set()).add(int(source_case_id))
    return {paragraph: len(sources) for paragraph, sources in sources_by_paragraph.items()}


_LABEL = re.compile(r"\b(?:paras?\.?|paragraphs?\.?)\s+", re.IGNORECASE)
_ITEM = r"\d+(?:\s*(?:[-–—]|\bto\b)\s*\d+)?"
_NUMBERS = re.compile(
    rf"{_ITEM}(?:\s*(?:,\s*(?:and\s+|or\s+)?|;|and\b|or\b)\s*{_ITEM})*",
    re.IGNORECASE,
)
_PARTS = re.compile(rf"{_ITEM}", re.IGNORECASE)


class ParagraphCitationCountsResponse(BaseModel):
    case_id: int
    counts: dict[int, int] = Field(description="Actual paragraph number to distinct later citing decisions, including zeros.")
    chronology_known: bool
    total_citing_decisions: int
    citing_decisions_with_usable_pinpoint: int
    citing_decisions_without_usable_pinpoint: int
    total_citations: int = Field(description="Stored resolved incoming citation rows from strictly later decisions; duplicate rows remain in this occurrence denominator.")
    citations_without_usable_pinpoint: int = Field(description="Eligible citation rows with no pinpoint mapping to an actual numbered paragraph.")


def _stored_pinpoints(text: str | None, actual: set[int]) -> tuple[int | None, set[int]] | None:
    """Read only explicitly paragraph-labelled lists/ranges in stored citations.

    Intersect ranges with actual numbers rather than expanding arbitrary ranges.
    Page pinpoints, malformed/reversed ranges, decimals and nested provisions
    are not paragraph evidence. The first number supports stored-scalar precedence.
    """
    if not text or (label := _LABEL.search(text)) is None:
        return None
    tail = text[label.end():]
    match = _NUMBERS.match(tail)
    if match is None:
        return (None, set())
    remainder = tail[match.end():].lstrip()
    if re.match(r"(?:[-–—,;(]|\.\d|\d|\b(?:to|and|or)\b)", remainder, re.IGNORECASE):
        return (None, set())
    found: set[int] = set()
    first = None
    for part in _PARTS.findall(match.group()):
        ends = re.split(r"\s*(?:[-–—]|\bto\b)\s*", part, flags=re.IGNORECASE)
        try:
            low, high = int(ends[0]), int(ends[-1])
        except ValueError:
            return (None, set())
        if low <= 0 or high < low:
            return (None, set())
        if first is None:
            first = low
        found.update(number for number in actual if low <= number <= high)
    return first, found


def usable_pinpoints(stored: int | None, text: str | None, normalized: str | None, actual: set[int]) -> set[int]:
    parsed = _stored_pinpoints(text, actual)
    if parsed is None:
        parsed = _stored_pinpoints(normalized, actual)
    if stored is not None:
        # A scalar wins a conflict, but a matching list/range can add its other
        # paragraphs, even when the range's first number is absent from the
        # formatted decision. A conflicting invalid scalar is not repaired.
        if parsed is not None and parsed[0] == stored:
            return parsed[1] | ({stored} if stored in actual else set())
        return {stored} if stored in actual else set()
    return parsed[1] if parsed is not None else set()


def aggregate_paragraph_citations(
    case_id: int, target_date: date | None, blocks: list[dict],
    rows: Iterable[tuple[int, date | None, int | None, str | None, str | None]],
) -> ParagraphCitationCountsResponse:
    """Each source decision contributes at most once per actual paragraph.

    Only a strictly later known source date is eligible. Same-day, earlier,
    unknown-date and self citations do not enter either denominator.
    """
    actual = {block["num"] for block in blocks if block["type"] == "para" and block["num"] > 0}
    all_sources: set[int] = set()
    usable_sources: set[int] = set()
    total = missing = 0

    def pairs():
        nonlocal total, missing
        for source_id, source_date, stored, text, normalized in rows:
            if source_id is None or source_id == case_id or target_date is None or source_date is None or source_date <= target_date:
                continue
            all_sources.add(source_id)
            total += 1
            numbers = usable_pinpoints(stored, text, normalized, actual)
            if not numbers:
                missing += 1
            else:
                usable_sources.add(source_id)
                for number in numbers:
                    yield source_id, number

    counts = distinct_citing_cases_by_paragraph(pairs(), case_id)
    return ParagraphCitationCountsResponse(
        case_id=case_id, counts={number: counts.get(number, 0) for number in sorted(actual)},
        chronology_known=target_date is not None,
        total_citing_decisions=len(all_sources),
        citing_decisions_with_usable_pinpoint=len(usable_sources),
        citing_decisions_without_usable_pinpoint=len(all_sources - usable_sources),
        total_citations=total, citations_without_usable_pinpoint=missing,
    )


@router.get(
    "/api/cases/{case_id}/paragraph-citation-counts",
    response_model=ParagraphCitationCountsResponse,
    responses={404: {"description": "Case not found"}},
)
def get_paragraph_citation_counts(case_id: int, db: Session = Depends(get_db)) -> ParagraphCitationCountsResponse:
    """Count distinct strictly later resolved citing decisions per actual paragraph.

    Includes decision and stored-occurrence coverage denominators; no citation
    treatment inference, source-text reparsing, or statute interpretation.
    """
    target = db.execute(select(Case.date, Case.full_text).where(Case.id == case_id)).first()
    if target is None:
        raise HTTPException(status_code=404, detail="Case not found")
    blocks = format_decision(target.full_text)
    if target.date is None:
        return aggregate_paragraph_citations(case_id, None, blocks, ())
    rows = db.execute(
        select(Citation.source_case_id, Case.date, Citation.target_paragraph,
               Citation.citation_text, Citation.normalized_citation)
        .join(Case, Case.id == Citation.source_case_id)
        .where(Citation.target_case_id == case_id, Citation.source_case_id != case_id,
               Case.date > target.date)
    )
    return aggregate_paragraph_citations(case_id, target.date, blocks, rows)
