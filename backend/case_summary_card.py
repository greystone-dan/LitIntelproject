"""Read-only extractive case summary card built from stored legal evidence."""

from __future__ import annotations

from collections import Counter
from datetime import date as date_type
import math
import re
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .case_formatter import format_decision
from .database import (
    Case,
    CaseOutcome,
    CaseTag,
    Citation,
    StatuteReference,
    get_db,
)
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION
from .reader_service import _build_reader_extracted_summary

_STANDARD_OF_REVIEW = re.compile(r"\bstandard of review\b", re.IGNORECASE)
_CONCLUSION_HEADINGS = {"conclusion", "disposition"}


class SummaryCardJudge(BaseModel):
    name: str
    source: str


class SummaryCardOutcome(BaseModel):
    value: str
    source: str | None = None
    status: str | None = None
    confidence: float | None = None


class SummaryCardStatute(BaseModel):
    instrument_key: str
    count: int = Field(gt=0)


class SummaryCardTag(BaseModel):
    category: str
    value: str
    score: float
    source: str


class SummaryCardParagraph(BaseModel):
    paragraph_number: int = Field(ge=0)
    text: str
    start: int = Field(ge=0)
    end: int = Field(gt=0)
    block_start: int = Field(ge=0)
    selection_rule: str
    pinpoint_citation_count: int | None = Field(default=None, ge=0)


class CaseSummaryCardResponse(BaseModel):
    case_id: int
    citation: str | None = None
    court: str | None = None
    date: date_type | None = None
    judge: SummaryCardJudge | None = None
    outcome: SummaryCardOutcome | None = None
    statutes: list[SummaryCardStatute] = Field(default_factory=list, max_length=5)
    top_tags: list[SummaryCardTag] = Field(default_factory=list, max_length=5)
    key_paragraphs: list[SummaryCardParagraph] = Field(default_factory=list, max_length=3)


def _numbered_paragraphs(text: str, blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return complete formatter paragraphs with source code-point boundaries."""
    paragraphs = []
    for index, block in enumerate(blocks):
        if block["type"] != "para":
            continue
        end = block["end"]
        for continuation in blocks[index + 1:]:
            if continuation["type"] not in {"text", "quote", "listitem"}:
                break
            end = continuation["end"]
        paragraphs.append({
            "number": block["num"],
            "start": block["start"],
            "end": end,
            "text": text[block["start"]:end],
        })
    return paragraphs


def _verified_paragraph(
    text: str, evidence: Any, start: Any, end: Any,
    paragraphs: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """Map exact, absolute evidence to one formatter paragraph without relocating it."""
    if not evidence or type(start) is not int or type(end) is not int:
        return None
    if not (0 <= start < end <= len(text)) or text[start:end] != evidence:
        return None
    return next(
        (row for row in paragraphs if row["start"] <= start < end <= row["end"]),
        None,
    )


def _disposition_paragraph(
    text: str, blocks: list[dict[str, Any]], paragraphs: list[dict[str, Any]],
    outcome: Any,
) -> dict[str, Any] | None:
    if outcome is not None:
        exact = _verified_paragraph(
            text,
            getattr(outcome, "disposition_evidence", None),
            getattr(outcome, "evidence_offset_start", None),
            getattr(outcome, "evidence_offset_end", None),
            paragraphs,
        )
        if exact is not None:
            return exact

    by_start = {row["start"]: row for row in paragraphs}
    in_conclusion = False
    for block in blocks:
        if block["type"] == "heading":
            heading = re.sub(
                r"^(?:[IVX]+|[A-Z]|\d+)\.\s*", "",
                text[block["start"]:block["end"]].strip(),
            ).strip().casefold()
            in_conclusion = heading in _CONCLUSION_HEADINGS
            continue
        if block["type"] == "para" and in_conclusion:
            return by_start.get(block["start"])
        if block["type"] not in {"text", "quote", "listitem"}:
            in_conclusion = False
    return None


def _standard_of_review_paragraph(
    text: str, blocks: list[dict[str, Any]], paragraphs: list[dict[str, Any]],
) -> dict[str, Any] | None:
    by_start = {row["start"]: row for row in paragraphs}
    under_heading = False
    for block in blocks:
        if block["type"] == "heading":
            heading = re.sub(
                r"^(?:[IVX]+|[A-Z]|\d+)\.\s*", "",
                text[block["start"]:block["end"]].strip(),
            ).strip().casefold()
            under_heading = heading == "standard of review"
            continue
        if block["type"] == "para":
            paragraph = by_start.get(block["start"])
            if paragraph is not None and (
                under_heading or _STANDARD_OF_REVIEW.search(paragraph["text"])
            ):
                return paragraph
            under_heading = False
        elif block["type"] not in {"text", "quote", "listitem"}:
            under_heading = False
    return None


def _ranked_cited_paragraph(
    db: Session, case: Case, paragraphs: list[dict[str, Any]],
) -> tuple[dict[str, Any], int] | None:
    """Select the most-mentioned paragraph with stored pinpoint citations from later cases."""
    if case.date is None or not paragraphs:
        return None
    rows = db.execute(
        select(Citation.target_paragraph, func.count(Citation.id))
        .join(Case, Case.id == Citation.source_case_id)
        .where(
            Citation.target_case_id == case.id,
            Citation.source_case_id != case.id,
            Citation.unresolved.is_(False),
            Citation.target_paragraph.is_not(None),
            Case.date > case.date,
        )
        .group_by(Citation.target_paragraph)
        .order_by(func.count(Citation.id).desc(), Citation.target_paragraph)
    ).all()
    paragraphs_by_number: dict[int, list[dict[str, Any]]] = {}
    for paragraph in paragraphs:
        paragraphs_by_number.setdefault(paragraph["number"], []).append(paragraph)
    for number, count in rows:
        matches = paragraphs_by_number.get(number, [])
        # A stored number cannot identify one source span if the formatter found
        # more than one paragraph with that number; do not guess which to quote.
        if len(matches) == 1 and count > 0:
            return matches[0], int(count)
    return None


def _key_paragraphs(
    db: Session, case: Case, outcome: Any,
) -> list[SummaryCardParagraph]:
    text = getattr(case, "full_text", None) or ""
    blocks = format_decision(text)
    paragraphs = _numbered_paragraphs(text, blocks)
    selected: list[SummaryCardParagraph] = []
    selected_by_anchor: dict[tuple[int, int], SummaryCardParagraph] = {}

    def add(paragraph: dict[str, Any] | None, rule: str, count: int | None = None) -> None:
        if paragraph is None:
            return
        anchor = (paragraph["start"], paragraph["number"])
        existing = selected_by_anchor.get(anchor)
        if existing is not None:
            if rule not in existing.selection_rule:
                existing.selection_rule += f"; also {rule}"
            return
        item = SummaryCardParagraph(
            paragraph_number=paragraph["number"],
            text=paragraph["text"],
            start=paragraph["start"],
            end=paragraph["end"],
            block_start=paragraph["start"],
            selection_rule=rule,
            pinpoint_citation_count=count,
        )
        selected.append(item)
        selected_by_anchor[anchor] = item

    add(
        _disposition_paragraph(text, blocks, paragraphs, outcome),
        "Disposition/conclusion paragraph",
    )
    cited = _ranked_cited_paragraph(db, case, paragraphs)
    add(cited[0] if cited else None, "Most stored later pinpoint citations", cited[1] if cited else None)
    add(
        _standard_of_review_paragraph(text, blocks, paragraphs),
        "Standard-of-review statement",
    )
    return selected[:3]


def _judge(case: Case, blocks: list[dict[str, Any]]) -> SummaryCardJudge | None:
    if not (getattr(case, "metadata_json", None) or {}).get("reader_extracted"):
        return None
    fields = _build_reader_extracted_summary(case, None, blocks, [], [])
    row = next((item for item in fields if item.key == "judge"), None)
    if row is None:
        return None
    return SummaryCardJudge(name=row.value, source=row.source)


def project_case_summary_card(
    case: Any,
    outcome: Any = None,
    tags=(),
    statute_references=(),
    *,
    key_paragraphs: list[SummaryCardParagraph] | None = None,
) -> CaseSummaryCardResponse:
    """Project stored facts, tag/statute layers, and supplied verified selections."""
    text = getattr(case, "full_text", None) or ""
    blocks = format_decision(text)
    verified_tags = []
    for tag in tags:
        score = getattr(tag, "score", None)
        if (
            getattr(tag, "taxonomy_version", None) != ACTIVE_TAG_TAXONOMY_VERSION
            or not getattr(tag, "category", None)
            or not getattr(tag, "value", None)
            or not isinstance(score, (int, float))
            or not math.isfinite(score)
        ):
            continue
        verified = _verified_paragraph(
            text, getattr(tag, "evidence", None), getattr(tag, "offset_start", None),
            getattr(tag, "offset_end", None),
            _numbered_paragraphs(text, blocks),
        )
        if verified is not None:
            verified_tags.append(tag)
    verified_tags.sort(key=lambda row: (
        -row.score, row.category, row.value, getattr(row, "id", 0) or 0,
    ))
    top_tags = []
    seen_tags = set()
    for tag in verified_tags:
        identity = (tag.category, tag.value)
        if identity in seen_tags:
            continue
        seen_tags.add(identity)
        top_tags.append(SummaryCardTag(
            category=tag.category,
            value=tag.value,
            score=tag.score,
            source=getattr(tag, "source", None) or "unknown",
        ))
        if len(top_tags) == 5:
            break

    statute_counts: Counter[str] = Counter()
    for reference in statute_references:
        key = getattr(reference, "instrument_key", None)
        if key and getattr(reference, "reference_kind", None) in {"statute", "instrument"}:
            statute_counts[key] += 1
    statutes = [
        SummaryCardStatute(instrument_key=key, count=count)
        for key, count in sorted(statute_counts.items(), key=lambda item: (-item[1], item[0]))[:5]
    ]

    outcome_data = None
    if outcome is not None and getattr(outcome, "decision_outcome", None):
        outcome_data = SummaryCardOutcome(
            value=outcome.decision_outcome,
            source=getattr(outcome, "source", None) or None,
            status=getattr(outcome, "outcome_status", None),
            confidence=getattr(outcome, "confidence", None),
        )

    return CaseSummaryCardResponse(
        case_id=case.id,
        citation=getattr(case, "citation", None) or None,
        court=getattr(case, "court", None) or None,
        date=getattr(case, "date", None),
        judge=_judge(case, blocks),
        outcome=outcome_data,
        statutes=statutes,
        top_tags=top_tags,
        key_paragraphs=key_paragraphs or [],
    )


def build_case_summary_card(case_id: int, db: Session) -> CaseSummaryCardResponse:
    case = db.scalar(select(Case).where(Case.id == case_id))
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    outcome = db.scalar(
        select(CaseOutcome)
        .where(CaseOutcome.case_id == case_id)
        .order_by(CaseOutcome.updated_at.desc(), CaseOutcome.id.desc())
        .limit(1)
    )
    tags = list(db.scalars(
        select(CaseTag)
        .where(
            CaseTag.case_id == case_id,
            CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
        )
        .order_by(CaseTag.score.desc(), CaseTag.category, CaseTag.value, CaseTag.id)
    ))
    statute_references = list(db.scalars(
        select(StatuteReference)
        .where(StatuteReference.source_case_id == case_id)
        .order_by(StatuteReference.id)
    ))
    key_paragraphs = _key_paragraphs(db, case, outcome)
    return project_case_summary_card(
        case, outcome, tags, statute_references, key_paragraphs=key_paragraphs,
    )


router = APIRouter()


@router.get(
    "/api/cases/{case_id}/summary-card",
    response_model=CaseSummaryCardResponse,
    response_model_exclude_none=True,
)
def get_case_summary_card(
    case_id: int, db: Session = Depends(get_db),
) -> CaseSummaryCardResponse:
    return build_case_summary_card(case_id, db)
