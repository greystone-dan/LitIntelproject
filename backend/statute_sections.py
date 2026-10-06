"""Section-level statute library: table of contents with case counts and a per-section view.

Read-only and deterministic. Section text comes from legislation_sections; case counts and
decision lists come from statute_references. The section of a reference is its stored
provision_section, or the leading section number of its pinpoint when that column is empty
(most rows were stored before provision_section existed), so the page works before and after
the backfill.
"""

from __future__ import annotations

import math
import re
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import HTMLResponse
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .database import Case, CaseOutcome, LegislationDocument, LegislationSection, StatuteReference, get_db
from .statute_consideration import MAX_PAGE_SIZE, aggregate_consideration
from .statutes import parse_provision_identity

router = APIRouter()

_SECTION_PATTERN = r"^[0-9]{1,3}(?:\.[0-9]+)?[A-Za-z]?"


def normalize_section(value: str | None) -> str:
    """Base section number in lower case ("34(1)(f)" -> "34", "98.03(4)" -> "98.03")."""
    match = re.match(r"\s*(\d{1,3}(?:\.\d+)?[A-Za-z]?)", value or "")
    return match.group(1).lower() if match else ""


def _section_expr():
    return func.lower(
        func.coalesce(StatuteReference.provision_section, func.substring(StatuteReference.pinpoint, _SECTION_PATTERN))
    )


def provision_label(pinpoint: str | None) -> str:
    """Subsection-level label such as "(1)(f)" for the breakdown; "whole section" when none."""
    section, subsection, paragraph, _depth, _is_list = parse_provision_identity(pinpoint)
    if not section:
        return "whole section"
    parts = [f"({value})" for value in (subsection, paragraph) if value]
    return "".join(parts) or "whole section"


def _get_document(db: Session, act: str) -> LegislationDocument:
    requested = (act or "").strip().lower()
    documents = list(db.scalars(select(LegislationDocument)))
    for document in documents:
        key = document.instrument_key.lower()
        if requested in {key, key.split(".")[-1], (document.title or "").lower()}:
            return document
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Unknown act '{act}'. Use an instrument key such as canada.irpa.",
    )


def list_acts(db: Session) -> list[dict[str, Any]]:
    counts = {
        key: (cases, refs)
        for key, cases, refs in db.execute(
            select(
                StatuteReference.instrument_key,
                func.count(func.distinct(StatuteReference.source_case_id)),
                func.count(StatuteReference.id),
            )
            .where(StatuteReference.instrument_key.isnot(None))
            .group_by(StatuteReference.instrument_key)
        )
    }
    section_counts = {
        document_id: total
        for document_id, total in db.execute(
            select(LegislationSection.document_id, func.count(LegislationSection.id)).group_by(
                LegislationSection.document_id
            )
        )
    }
    rows = []
    for document in db.scalars(select(LegislationDocument)):
        cases, refs = counts.get(document.instrument_key, (0, 0))
        rows.append(
            {
                "instrument_key": document.instrument_key,
                "title": document.title,
                "section_count": section_counts.get(document.id, 0),
                "case_count": cases,
                "reference_count": refs,
            }
        )
    rows.sort(key=lambda row: (-row["case_count"], row["title"]))
    return rows


def fetch_table_of_contents(db: Session, act: str) -> dict[str, Any]:
    document = _get_document(db, act)
    section_key = _section_expr()
    counts = {
        key: (cases, refs)
        for key, cases, refs in db.execute(
            select(
                section_key,
                func.count(func.distinct(StatuteReference.source_case_id)),
                func.count(StatuteReference.id),
            )
            .where(StatuteReference.instrument_key == document.instrument_key)
            .group_by(section_key)
        )
        if key
    }
    sections = []
    seen: set[str] = set()
    for section in db.scalars(
        select(LegislationSection)
        .where(LegislationSection.document_id == document.id)
        .order_by(LegislationSection.display_order)
    ):
        key = section.section_number.strip().lower()
        seen.add(key)
        cases, refs = counts.get(key, (0, 0))
        sections.append(
            {
                "section": section.section_number,
                "label": section.label,
                "case_count": cases,
                "reference_count": refs,
            }
        )
    # Cited sections with no row in the text layer stay visible rather than silently vanishing.
    missing = [
        {"section": key, "label": None, "case_count": cases, "reference_count": refs, "no_text": True}
        for key, (cases, refs) in counts.items()
        if key not in seen
    ]
    missing.sort(key=lambda row: -row["case_count"])
    return {
        "act": {"instrument_key": document.instrument_key, "title": document.title, "citation": document.citation},
        "sections": sections,
        "cited_without_text": missing,
        "note": "Counts are distinct decisions with a stored reference to the section; descriptive only.",
    }


def fetch_section_view(db: Session, act: str, section: str, page: int = 1, page_size: int = 25) -> dict[str, Any]:
    document = _get_document(db, act)
    key = normalize_section(section)
    if not key:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unknown section '{section}'. Try 34.")
    text_row = db.scalar(
        select(LegislationSection).where(
            LegislationSection.document_id == document.id,
            func.lower(LegislationSection.section_number) == key,
        )
    )
    occurrence_rows = db.execute(
        select(StatuteReference, Case)
        .join(Case, StatuteReference.source_case_id == Case.id)
        .where(StatuteReference.instrument_key == document.instrument_key, _section_expr() == key)
    ).all()
    if not occurrence_rows and text_row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No text or stored references for section {key} of {document.title}.",
        )
    case_ids = {case.id for _reference, case in occurrence_rows}
    outcome_rows = (
        list(
            db.scalars(
                select(CaseOutcome)
                .where(CaseOutcome.case_id.in_(case_ids))
                .order_by(CaseOutcome.updated_at.desc().nullslast(), CaseOutcome.id.desc())
            )
        )
        if case_ids
        else []
    )
    result = aggregate_consideration([(reference, case) for reference, case in occurrence_rows], outcome_rows)

    # Subsection / paragraph breakdown, distinct decisions per label.
    label_cases: dict[str, set[int]] = {}
    for reference, case in occurrence_rows:
        label_cases.setdefault(provision_label(reference.pinpoint), set()).add(case.id)
    result["by_provision"] = sorted(
        ({"value": label, "decision_count": len(ids)} for label, ids in label_cases.items()),
        key=lambda row: (-row["decision_count"], row["value"]),
    )[:40]
    result["by_year"] = sorted(result["by_year"], key=lambda row: row["value"])

    page = max(1, page)
    page_size = max(1, min(MAX_PAGE_SIZE, page_size))
    total = result["summary"]["decision_count"]
    start = (page - 1) * page_size
    result["decisions"] = result["decisions"][start : start + page_size]
    result["pagination"] = {
        "page": page,
        "page_size": page_size,
        "total_decisions": total,
        "total_pages": max(1, math.ceil(total / page_size)),
    }
    result["act"] = {"instrument_key": document.instrument_key, "title": document.title, "citation": document.citation}
    result["section"] = {
        "number": text_row.section_number if text_row else key,
        "label": text_row.label if text_row else None,
        "text": text_row.text if text_row else None,
        "text_available": text_row is not None,
        "text_note": "Text from the Justice Laws consolidation held in the library; unofficial, current to the snapshot date, not necessarily the wording in force on each decision date.",
    }
    return result


@router.get("/api/statute-library/acts")
def statute_library_acts(db: Session = Depends(get_db)) -> list[dict[str, Any]]:
    return list_acts(db)


@router.get("/api/statute-library/{act}/sections")
def statute_library_toc(act: str, db: Session = Depends(get_db)) -> dict[str, Any]:
    return fetch_table_of_contents(db, act)


@router.get("/api/statute-library/{act}/sections/{section}")
def statute_library_section(
    act: str,
    section: str,
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1),
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    return fetch_section_view(db, act, section, page, page_size)


@router.get("/statute-library", response_class=HTMLResponse, include_in_schema=False)
def statute_library_page() -> HTMLResponse:
    from .pages.statute_library import statute_library_page_html

    return HTMLResponse(statute_library_page_html())
