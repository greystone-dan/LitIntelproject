import csv
import io
from datetime import date, datetime
from typing import Literal

from docx import Document
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse, Response
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .database import Case, CaseOutcome, get_db
from .deidentify import text_to_docx
from .pages.research_folders import research_folders_page_html


MAX_EXPORT_CASES = 500
_NO_STORE = {"Cache-Control": "no-store", "Pragma": "no-cache"}
_DOCX_MEDIA_TYPE = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)
_HEADINGS = ("Citation", "Name", "Court", "Date", "Outcome", "Note")

router = APIRouter(tags=["research folders"])


@router.get("/research-folders", response_class=HTMLResponse)
def research_folders_page() -> str:
    return research_folders_page_html()


class ResearchFolderExportRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    case_ids: list[StrictInt] = Field(min_length=1, max_length=MAX_EXPORT_CASES)
    notes: dict[int, StrictStr] = Field(default_factory=dict)
    format: Literal["csv", "docx"] = "csv"

    @model_validator(mode="after")
    def validate_selection(self) -> "ResearchFolderExportRequest":
        selected_ids = set(self.case_ids)
        if any(case_id <= 0 for case_id in selected_ids):
            raise ValueError("Case IDs must be positive integers")
        if len(selected_ids) > MAX_EXPORT_CASES:
            raise ValueError(f"At most {MAX_EXPORT_CASES} distinct cases can be exported")
        if not set(self.notes).issubset(selected_ids):
            raise ValueError("Notes may only be supplied for selected cases")
        if any(len(note) > 5000 for note in self.notes.values()):
            raise ValueError("Notes must be 5000 characters or fewer")
        return self


def _case_outcome(government_outcome: str | None, decision_outcome: str | None) -> str:
    if government_outcome in {"won", "lost", "mixed"}:
        return government_outcome
    if decision_outcome in {"dismissed", "allowed", "granted"}:
        return decision_outcome
    return "unclassified"


def _csv_safe_cell(value: object) -> str:
    text = "" if value is None else str(value)
    if text.lstrip().startswith(("=", "+", "-", "@", "\t", "\r")):
        return "'" + text
    return text


def _display_date(value: date | datetime | str | None) -> str:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return "" if value is None else str(value)


def _load_cases(db: Session, case_ids: list[int]) -> dict[int, dict[str, object]]:
    latest_outcomes = (
        select(
            CaseOutcome.case_id.label("case_id"),
            CaseOutcome.decision_outcome.label("decision_outcome"),
            CaseOutcome.government_outcome.label("government_outcome"),
            func.row_number()
            .over(
                partition_by=CaseOutcome.case_id,
                order_by=(CaseOutcome.updated_at.desc(), CaseOutcome.id.desc()),
            )
            .label("outcome_rank"),
        )
        .where(CaseOutcome.case_id.in_(case_ids))
        .subquery()
    )
    statement = (
        select(
            Case.id,
            Case.citation,
            Case.title,
            Case.court,
            Case.date,
            latest_outcomes.c.decision_outcome,
            latest_outcomes.c.government_outcome,
        )
        .outerjoin(
            latest_outcomes,
            (latest_outcomes.c.case_id == Case.id)
            & (latest_outcomes.c.outcome_rank == 1),
        )
        .where(Case.id.in_(case_ids))
    )
    rows = db.execute(statement).mappings().all()
    return {
        int(row["id"]): {
            "citation": row["citation"],
            "name": row["title"],
            "court": row["court"],
            "date": row["date"],
            "outcome": _case_outcome(
                row["government_outcome"], row["decision_outcome"]
            ),
        }
        for row in rows
    }


@router.post("/api/research-folders/export")
def export_research_folder(
    request: ResearchFolderExportRequest, db: Session = Depends(get_db)
) -> Response:
    selected_ids = list(dict.fromkeys(request.case_ids))
    cases = _load_cases(db, selected_ids)
    if len(cases) != len(selected_ids):
        raise HTTPException(
            status_code=404, detail="One or more selected cases were not found"
        )

    rows = [
        (
            cases[case_id]["citation"],
            cases[case_id]["name"],
            cases[case_id]["court"],
            _display_date(cases[case_id]["date"]),
            cases[case_id]["outcome"],
            request.notes.get(case_id, ""),
        )
        for case_id in selected_ids
    ]

    if request.format == "csv":
        output = io.StringIO(newline="")
        writer = csv.writer(output)
        writer.writerow(_HEADINGS)
        for row in rows:
            writer.writerow(_csv_safe_cell(value) for value in row)
        return Response(
            content="\ufeff" + output.getvalue(),
            media_type="text/csv",
            headers={
                **_NO_STORE,
                "Content-Disposition": 'attachment; filename="research-folder-export.csv"',
            },
        )

    document = Document(io.BytesIO(text_to_docx("")))
    table = document.add_table(rows=1, cols=len(_HEADINGS))
    table.style = "Table Grid"
    for cell, heading in zip(table.rows[0].cells, _HEADINGS):
        cell.text = heading
    for row in rows:
        cells = table.add_row().cells
        for cell, value in zip(cells, row):
            cell.text = "" if value is None else str(value)
    buffer = io.BytesIO()
    document.save(buffer)
    return Response(
        content=buffer.getvalue(),
        media_type=_DOCX_MEDIA_TYPE,
        headers={
            **_NO_STORE,
            "Content-Disposition": 'attachment; filename="research-folder-export.docx"',
        },
    )
