"""Read-only stored case summary. All excerpt offsets are full_text code points.

This is independent of the reader's technical discussion-unit summary. No
classification, text generation, citation resolution or persistence occurs here.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from datetime import date as date_type
from typing import Any, Iterable, Literal

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from .case_formatter import format_decision
from .database import Case, CaseOutcome, CaseTag, StatuteReference, get_db
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION


class SummaryExcerpt(BaseModel):
    """Exact source slice and numbered backend formatter anchor."""

    text: str
    start: int = Field(ge=0)
    end: int = Field(gt=0)
    block_start: int = Field(ge=0)
    paragraph_number: int = Field(ge=0)


class IssueExcerpt(SummaryExcerpt):
    kind: Literal["issue", "standard_of_review"]


class SummaryStatute(BaseModel):
    instrument_key: str
    count: int = Field(gt=0)
    evidence: SummaryExcerpt | None = None


class SummaryTag(BaseModel):
    category: str
    value: str
    score: float
    source: str
    evidence: SummaryExcerpt


class StoredCaseSummaryResponse(BaseModel):
    case_id: int
    style_of_cause: str | None = None
    citation: str | None = None
    court: str | None = None
    date: date_type | None = None
    decision_outcome: str
    outcome_source: str
    disposition: SummaryExcerpt | None = None
    issue: IssueExcerpt | None = None
    top_statutes: list[SummaryStatute] = Field(default_factory=list, max_length=5)
    top_tags: list[SummaryTag] = Field(default_factory=list, max_length=5)


def _paragraphs(blocks: list[dict[str, Any]]) -> Iterable[tuple[dict[str, Any], int]]:
    """Same continuation boundary contract as reader_service's evidence helper."""
    for index, block in enumerate(blocks):
        if block["type"] != "para":
            continue
        end = block["end"]
        for continuation in blocks[index + 1:]:
            if continuation["type"] not in {"text", "quote", "listitem"}:
                break
            end = continuation["end"]
        yield block, end


def _verified_excerpt(
    text: str, evidence: Any, start: Any, end: Any,
    paragraphs: list[tuple[dict[str, Any], int]],
) -> SummaryExcerpt | None:
    if not evidence or type(start) is not int or type(end) is not int:
        return None
    if not (0 <= start < end <= len(text)) or text[start:end] != evidence:
        return None
    for block, paragraph_end in paragraphs:
        if block["start"] <= start < end <= paragraph_end:
            return SummaryExcerpt(
                text=evidence, start=start, end=end,
                block_start=block["start"], paragraph_number=block["num"],
            )
    return None


# Only explicit, well-known non-terminal abbreviations are supported. Unknown
# abbreviated forms, initials, ellipses, quotes and incomplete tails are omitted,
# not "repaired" or guessed into sentences.
_ABBREVIATION = re.compile(
    r"\b(?:Mr|Mrs|Ms|Dr|Prof|No|s|ss|para|paras|v)\."
    r"|\b(?:e\.g\.|i\.e\.)",
    re.IGNORECASE,
)
_ISSUE_OPENING = re.compile(
    r"^(?:The (?:only |main |central )?issues? (?:is|are|in this|before)|"
    r"The question (?:is|before)|At issue is)\b", re.IGNORECASE,
)
_REVIEW_OPENING = re.compile(r"^The (?:applicable )?standard of review\b", re.IGNORECASE)


def _sentence_end(body: str) -> int | None:
    """End of the first one/two complete sentences, or no safe selection.

    Validate the whole paragraph before selecting its prefix. This deliberately
    sacrifices recall rather than displaying a truncated or ambiguous sentence.
    """
    if not body or not body[0].isupper() or any(c in body for c in '“”"…'):
        return None
    protected = {
        index
        for match in _ABBREVIATION.finditer(body)
        for index in range(match.start(), match.end())
    }
    ends = []
    sentence_start = 0
    for index, char in enumerate(body):
        if char not in ".?!" or index in protected:
            continue
        if index + 1 < len(body) and not body[index + 1].isspace():
            return None  # decimals, unknown dotted acronyms and ellipses
        if char == ".":
            token = re.search(r"(\w+)$", body[sentence_start:index])
            if token and (
                len(token[1]) == 1
                or token[1].lower() in {
                    "ltd", "inc", "corp", "etc", "cf", "viz", "approx", "dept",
                }
                or (token[1][0].isupper() and len(token[1]) <= 4)
            ):
                return None
        if not body[sentence_start:index].strip():
            return None
        ends.append(index + 1)
        sentence_start = index + 1
        while sentence_start < len(body) and body[sentence_start].isspace():
            sentence_start += 1
        if sentence_start < len(body) and not body[sentence_start].isupper():
            return None
    if not ends or body[sentence_start:].strip():
        return None
    return ends[min(len(ends), 2) - 1]


def _issue_excerpt(
    text: str, blocks: list[dict[str, Any]],
    paragraphs: list[tuple[dict[str, Any], int]],
) -> IssueExcerpt | None:
    candidates: dict[str, list[IssueExcerpt]] = {"issue": [], "standard_of_review": []}
    previous_heading = None
    paragraph_ends = {block["start"]: end for block, end in paragraphs}
    for block in blocks:
        if block["type"] == "heading":
            heading = text[block["start"]:block["end"]].strip()
            heading = re.sub(r"^(?:[IVX]+|[A-Z]|\d+)\.\s*", "", heading)
            previous_heading = (
                "issue" if heading.lower() in {"issue", "issues"} else
                "standard_of_review" if heading.lower() == "standard of review" else None
            )
            continue
        if block["type"] != "para":
            previous_heading = None
            continue
        start = block["mark_end"]
        end = paragraph_ends[block["start"]]
        while start < end and text[start].isspace():
            start += 1
        body = text[start:end].rstrip()
        kind = (
            "issue" if _ISSUE_OPENING.match(body) else
            "standard_of_review" if _REVIEW_OPENING.match(body) else previous_heading
        )
        previous_heading = None
        if kind is None:
            continue
        selected_end = _sentence_end(body)
        if selected_end is not None:
            candidates[kind].append(IssueExcerpt(
                kind=kind, text=text[start:start + selected_end],
                start=start, end=start + selected_end, block_start=block["start"],
                paragraph_number=block["num"],
            ))
    for kind in ("issue", "standard_of_review"):
        if candidates[kind]:
            return candidates[kind][0]
    return None


def project_case_summary(
    case: Any, outcome: Any = None, tags: Iterable[Any] = (),
    statute_references: Iterable[Any] = (),
) -> StoredCaseSummaryResponse:
    """Pure projection accepting ORM rows or lightweight fixture namespaces."""
    text = getattr(case, "full_text", None) or ""
    blocks = format_decision(text)
    paragraphs = list(_paragraphs(blocks))
    disposition = None
    if outcome is not None:
        verified = _verified_excerpt(
            text, getattr(outcome, "disposition_evidence", None),
            getattr(outcome, "evidence_offset_start", None),
            getattr(outcome, "evidence_offset_end", None), paragraphs,
        )
        if verified is not None:
            block, end = next(
                (block, end) for block, end in paragraphs
                if block["start"] == verified.block_start
            )
            disposition = SummaryExcerpt(
                text=text[block["start"]:end], start=block["start"], end=end,
                block_start=block["start"], paragraph_number=block["num"],
            )

    verified_tags = []
    for tag in tags:
        if getattr(tag, "taxonomy_version", None) != ACTIVE_TAG_TAXONOMY_VERSION:
            continue
        score = getattr(tag, "score", None)
        if score is None or not math.isfinite(score) or not tag.category or not tag.value:
            continue
        evidence = _verified_excerpt(
            text, getattr(tag, "evidence", None), getattr(tag, "offset_start", None),
            getattr(tag, "offset_end", None), paragraphs,
        )
        if evidence is not None:
            verified_tags.append(SummaryTag(
                category=tag.category, value=tag.value, score=score,
                source=getattr(tag, "source", None) or "unknown", evidence=evidence,
            ))
    verified_tags.sort(key=lambda tag: (
        -tag.score, tag.category, tag.value, tag.evidence.start,
        tag.evidence.end, tag.source,
    ))
    top_tags = []
    seen = set()
    for tag in verified_tags:
        pair = (tag.category, tag.value)
        if pair not in seen:
            seen.add(pair)
            top_tags.append(tag)
        if len(top_tags) == 5:
            break

    counts: Counter[str] = Counter()
    statute_evidence: dict[str, SummaryExcerpt] = {}
    for reference in statute_references:
        key = getattr(reference, "instrument_key", None)
        if not key or getattr(reference, "reference_kind", None) not in {"statute", "instrument"}:
            continue
        counts[key] += 1
        # Chunk-linked statute offsets are chunk-relative. Keep their counts,
        # but do not mistake a coincidental document-prefix match for evidence.
        # This projection intentionally does not retrieve/rebase chunk text.
        evidence = None if getattr(reference, "chunk_id", None) is not None else _verified_excerpt(
            text, getattr(reference, "reference_text", None),
            getattr(reference, "offset_start", None),
            getattr(reference, "offset_end", None), paragraphs,
        )
        if evidence is not None and (
            key not in statute_evidence
            or (evidence.start, evidence.end) <
            (statute_evidence[key].start, statute_evidence[key].end)
        ):
            statute_evidence[key] = evidence
    top_statutes = [
        SummaryStatute(instrument_key=key, count=count, evidence=statute_evidence.get(key))
        for key, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:5]
    ]
    return StoredCaseSummaryResponse(
        case_id=case.id, style_of_cause=getattr(case, "title", None) or None,
        citation=getattr(case, "citation", None) or None,
        court=getattr(case, "court", None) or None, date=getattr(case, "date", None),
        decision_outcome=getattr(outcome, "decision_outcome", None) or "unclassified",
        outcome_source=getattr(outcome, "source", None) or "unknown",
        disposition=disposition, issue=_issue_excerpt(text, blocks, paragraphs),
        top_statutes=top_statutes, top_tags=top_tags,
    )


def build_case_summary(case_id: int, db: Session) -> StoredCaseSummaryResponse:
    case = db.scalar(select(Case).where(Case.id == case_id))
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    outcome = db.scalar(
        select(CaseOutcome).where(CaseOutcome.case_id == case_id)
        .order_by(CaseOutcome.updated_at.desc(), CaseOutcome.id.desc()).limit(1)
    )
    tags = db.scalars(
        select(CaseTag).where(
            CaseTag.case_id == case_id,
            CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
        ).order_by(CaseTag.score.desc(), CaseTag.category, CaseTag.value, CaseTag.id)
    )
    references = db.scalars(
        select(StatuteReference).where(StatuteReference.source_case_id == case_id)
        .order_by(StatuteReference.id)
    )
    return project_case_summary(case, outcome, tags, references)


router = APIRouter()


@router.get(
    "/api/cases/{case_id}/summary", response_model=StoredCaseSummaryResponse,
    response_model_exclude_none=True,
)
def get_case_summary(case_id: int, db: Session = Depends(get_db)) -> StoredCaseSummaryResponse:
    return build_case_summary(case_id, db)
