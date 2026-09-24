"""Read-only cohort search helpers for the Discussion Units experiment."""

from __future__ import annotations

import csv
from functools import lru_cache
from pathlib import Path
import re
from typing import Any

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .analytics_service import fetch_analytics_search_cases


COHORT_MANIFEST = (
    Path(__file__).resolve().parents[1]
    / "data/eval/llm_discussion_units_pilot/discussion_unit_core_300.csv"
)
PARAGRAPH_ASSESSMENT_DIR = (
    Path(__file__).resolve().parents[1]
    / "data/eval/llm_discussion_units_pilot/paragraph_level_300_run/reviews"
)


def discussion_units_sandbox_page_html() -> str:
    from .pages.data_explorer import data_explorer_page_html

    html = data_explorer_page_html()
    for source, target in (
        ("/analytics/search/cases/", "/discussion-units-sandbox/cases/"),
        ("/analytics/search/cases?", "/discussion-units-sandbox/search?"),
        ("/cases/${caseId}/reader-data", "/discussion-units-sandbox/cases/${caseId}/reader-data"),
        ("/cases/${readerState.caseId}/statute-references", "/discussion-units-sandbox/cases/${readerState.caseId}/statute-references"),
        ("/cases/${data.case?.id}/activity", "/discussion-units-sandbox/cases/${data.case?.id}/activity"),
        ("/data-explorer", "/discussion-units-sandbox"),
    ):
        html = html.replace(source, target)
    html = html.replace("<title>Immigration Litigation Intelligence Tool | iLIT</title>", "<title>Sandbox | iLIT</title>")
    html = html.replace("<a class=\"active\" href=\"/discussion-units-sandbox\">Research</a>", "<a class=\"active\" href=\"/discussion-units-sandbox\">Sandbox</a>")
    html = html.replace("Immigration Litigation Intelligence Tool", "Sandbox")
    html = html.replace(
        "</body>",
        """<script>
const sandboxAssessmentState={enabled:false,caseId:null,rows:{}};
function sandboxAssessmentHtml(row){return `<aside class="sandbox-assessment"><strong>${esc(row.topic||'Unclassified')}</strong><span>${esc(row.role||'Role unavailable')} · confidence ${esc(row.confidence??'n/a')}</span><p>${esc(row.explanation||'')}</p></aside>`;}
async function loadSandboxAssessments(){const caseId=readerState.caseId;if(!caseId)return;sandboxAssessmentState.caseId=caseId;const response=await fetch(`/discussion-units-sandbox/cases/${caseId}/paragraph-assessments`);if(!response.ok)throw new Error(`Assessment request failed (${response.status})`);const data=await response.json();sandboxAssessmentState.rows=data.assessments||{};sandboxAssessmentState.enabled=true;renderSandboxAssessments();}
function renderSandboxAssessments(){document.querySelectorAll('#decisionBody .chunk-body').forEach((body,index)=>{body.closest('.reader-chunk')?.querySelector('.sandbox-assessment')?.remove();const chunk=readerState.payload?.readerData?.chunks?.[index],number=String(chunk?.paragraph_start??index+1),row=sandboxAssessmentState.rows[number];if(row)body.insertAdjacentHTML('afterend',sandboxAssessmentHtml(row));});}
function installSandboxAssessmentToggle(){const target=document.getElementById('decisionTarget');if(!target||target.querySelector('#sandboxAssessmentToggle'))return;const button=document.createElement('button');button.id='sandboxAssessmentToggle';button.className='secondary';button.type='button';button.textContent='Show paragraph assessments';button.onclick=async()=>{if(!sandboxAssessmentState.enabled){button.textContent='Loading assessments...';try{await loadSandboxAssessments()}catch(error){button.textContent=error.message;return}}else{sandboxAssessmentState.enabled=false;document.querySelectorAll('.sandbox-assessment').forEach(item=>item.remove())}button.textContent=sandboxAssessmentState.enabled?'Hide paragraph assessments':'Show paragraph assessments'};target.querySelector('.reader-controls')?.append(button);}
new MutationObserver(installSandboxAssessmentToggle).observe(document.getElementById('decisionTarget'),{childList:true,subtree:true});
</script></body>""",
    )
    return html


@lru_cache(maxsize=1)
def load_discussion_unit_cohort() -> dict[int, dict[str, str]]:
    with COHORT_MANIFEST.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    cohort = {int(row["case_id"]): row for row in rows}
    if len(cohort) != 300 or len(rows) != 300:
        raise RuntimeError("Discussion Unit sandbox manifest must contain 300 unique cases")
    return cohort


def require_discussion_unit_case(case_id: int) -> None:
    if case_id not in load_discussion_unit_cohort():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Case is outside the experimental cohort",
        )


def load_paragraph_assessments(case_id: int, *, enforce_cohort: bool = True) -> dict[str, Any]:
    if enforce_cohort:
        require_discussion_unit_case(case_id)
    path = PARAGRAPH_ASSESSMENT_DIR / f"case_{case_id}_paragraph_assessment.md"
    if not path.exists():
        return {"case_id": case_id, "available": False, "assessments": {}, "source": "paragraph_level_300_run"}
    assessments: dict[str, dict[str, Any]] = {}
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| Paragraph |"):
            in_table = True
            continue
        if not in_table or not line.startswith("|"):
            if in_table and line and not line.startswith("|"):
                in_table = False
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 5 or not re.fullmatch(r"\d+", cells[0]):
            continue
        try:
            confidence: float | str | None = float(cells[3])
        except ValueError:
            confidence = cells[3] or None
        assessments[cells[0]] = {"topic": cells[1], "role": cells[2], "confidence": confidence, "explanation": cells[4]}
    return {
        "case_id": case_id,
        "available": bool(assessments),
        "assessments": assessments,
        "source": "paragraph_level_300_run",
    }


def search_discussion_unit_cases(
    db: Session,
    *,
    query: str = "",
    cites: str = "",
    government_outcome: str = "",
    decision_outcome: str = "",
    minister: str = "",
    judge: str = "",
    court: str = "",
    year: str = "",
    search_full_text: bool = False,
    sort_by: str = "relevance",
    limit: int = 50,
    offset: int = 0,
) -> dict[str, Any]:
    cohort = load_discussion_unit_cohort()
    result = fetch_analytics_search_cases(
        db,
        query=query,
        cites=cites,
        government_outcome=government_outcome,
        decision_outcome=decision_outcome,
        minister=minister,
        judge=judge,
        court=court,
        year=year,
        search_full_text=search_full_text,
        sort_by=sort_by,
        limit=limit,
        offset=offset,
        cohort_ids=list(cohort),
    )
    result.update({"cohort": "discussion_unit_core_300", "cohort_size": len(cohort)})
    return result
