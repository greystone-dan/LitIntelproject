"""Read-only cohort search helpers for the Discussion Units experiment."""

from __future__ import annotations

import csv
from functools import lru_cache
import json
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
PARAGRAPH_EVIDENCE_BRIDGE = (
    Path(__file__).resolve().parents[1]
    / "data/eval/llm_discussion_units_pilot/paragraph_level_300_run/citation_evidence_bridge.json"
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


@lru_cache(maxsize=1)
def load_cohort_assessment_records() -> tuple[dict[str, Any], ...]:
    if not PARAGRAPH_EVIDENCE_BRIDGE.exists():
        return ()
    data = json.loads(PARAGRAPH_EVIDENCE_BRIDGE.read_text(encoding="utf-8"))
    cohort_ids = set(load_discussion_unit_cohort())
    return tuple(record for record in data.get("records", []) if record.get("case_id") in cohort_ids)


def _assessment_search_tokens(value: str) -> set[str]:
    return {token for token in re.findall(r"[a-z0-9]+", value.casefold()) if len(token) > 2}


def search_cohort_assessments(query: str, *, limit: int = 50) -> dict[str, Any]:
    query = " ".join(query.split())
    query_tokens = _assessment_search_tokens(query)
    if not query_tokens:
        return {"mode": "assessment_search", "cohort_id": "discussion_units_core_300", "cohort_size": 300, "query": query, "results": []}
    results: list[dict[str, Any]] = []
    for record in load_cohort_assessment_records():
        assessment = record.get("assessment") or {}
        fields = {name: str(assessment.get(name) or "") for name in ("topic", "role", "explanation")}
        fields["paragraph"] = str(record.get("text") or "")
        match_reasons = [name for name, value in fields.items() if query_tokens & _assessment_search_tokens(value)]
        if not match_reasons:
            continue
        matched_tokens = set().union(*(query_tokens & _assessment_search_tokens(fields[name]) for name in match_reasons))
        score = len(matched_tokens) / len(query_tokens)
        if "topic" in match_reasons:
            score += 0.25
        if "role" in match_reasons:
            score += 0.1
        citations = [{"id": citation.get("id"), "case_id": record.get("case_id"), "paragraph": record.get("paragraph"), "chunk_id": citation.get("chunk_id"), "paragraph_chunk_id": citation.get("paragraph_chunk_id"), "offset_start": citation.get("offset_start"), "offset_end": citation.get("offset_end"), "paragraph_offset_start": citation.get("paragraph_offset_start"), "paragraph_offset_end": citation.get("paragraph_offset_end"), "target_case_id": citation.get("target_case_id"), "normalized_citation": citation.get("normalized_citation"), "link_method": citation.get("link_method"), "link_status": citation.get("link_status"), "assessment_key": {"topic": fields["topic"], "role": fields["role"]}} for citation in record.get("citations", [])]
        results.append({"case_id": record.get("case_id"), "paragraph": record.get("paragraph"), "topic": fields["topic"], "role": fields["role"], "confidence": assessment.get("confidence"), "explanation": fields["explanation"], "text": fields["paragraph"], "score": round(min(score, 1.0), 4), "match_reasons": match_reasons, "citations": citations, "bridge_status": record.get("status", "unknown")})
    results.sort(key=lambda item: (-item["score"], item["case_id"], str(item["paragraph"])))
    return {"mode": "assessment_search", "cohort_id": "discussion_units_core_300", "cohort_size": 300, "query": query, "results": results[: max(1, min(limit, 100))]}


def compare_cohort_assessments(query: str = "", *, topic: str = "", role: str = "", limit: int = 25) -> dict[str, Any]:
    base = search_cohort_assessments(query, limit=100)
    results = [item for item in base["results"] if (not topic or item["topic"] == topic) and (not role or item["role"] == role) and item.get("bridge_status") in {"exact", "unknown"}]
    if topic or role:
        comparison_tokens = _assessment_search_tokens(" ".join((topic, role)))
        results = []
        for record in load_cohort_assessment_records():
            if record.get("status") not in {"exact", "unknown"}:
                continue
            assessment = record.get("assessment") or {}
            if topic and str(assessment.get("topic") or "") != topic:
                continue
            if role and str(assessment.get("role") or "") != role:
                continue
            fields = {name: str(assessment.get(name) or "") for name in ("topic", "role", "explanation")}
            fields["paragraph"] = str(record.get("text") or "")
            matched_tokens = set().union(*(comparison_tokens & _assessment_search_tokens(value) for value in fields.values()))
            citations = [{"id": citation.get("id"), "case_id": record.get("case_id"), "paragraph": record.get("paragraph"), "chunk_id": citation.get("chunk_id"), "paragraph_chunk_id": citation.get("paragraph_chunk_id"), "offset_start": citation.get("offset_start"), "offset_end": citation.get("offset_end"), "paragraph_offset_start": citation.get("paragraph_offset_start"), "paragraph_offset_end": citation.get("paragraph_offset_end"), "target_case_id": citation.get("target_case_id"), "normalized_citation": citation.get("normalized_citation"), "link_method": citation.get("link_method"), "link_status": citation.get("link_status"), "assessment_key": {"topic": fields["topic"], "role": fields["role"]}} for citation in record.get("citations", [])]
            results.append({"case_id": record.get("case_id"), "paragraph": record.get("paragraph"), "topic": fields["topic"], "role": fields["role"], "score": round(len(matched_tokens) / len(comparison_tokens), 4) if comparison_tokens else 0, "explanation": fields["explanation"], "text": fields["paragraph"], "citations": citations, "bridge_status": record.get("status", "unknown")})
    groups: dict[tuple[str, str], dict[str, Any]] = {}
    for item in results:
        key = (item["topic"], item["role"])
        group = groups.setdefault(key, {"topic": item["topic"], "role": item["role"], "cases": [], "citations": []})
        group["cases"].append({"case_id": item["case_id"], "paragraph": item["paragraph"], "score": item["score"], "explanation": item["explanation"], "text": item["text"], "citations": item["citations"]})
        group["citations"].extend(item["citations"])
    for group in groups.values():
        group["cases"].sort(key=lambda item: (-item["score"], item["case_id"], str(item["paragraph"])))
        group["citations"].sort(key=lambda item: (item.get("normalized_citation") or "", item.get("case_id"), str(item.get("paragraph"))))
    return {"mode": "assessment_comparison", "cohort_id": "discussion_units_core_300", "cohort_size": 300, "query": query, "topic": topic, "role": role, "groups": list(groups.values())[: max(1, min(limit, 100))]}


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
