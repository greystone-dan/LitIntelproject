"""Read-only statute-consideration analytics and their small browser interface."""

from __future__ import annotations

import math
import re
from collections import Counter
from datetime import date
from typing import Any, Iterable

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import HTMLResponse
from sqlalchemy import func
from sqlalchemy.orm import Session

from .database import Case, CaseOutcome, Statute, StatuteReference, get_db
from .statutes import LEGISLATION_REGISTRY
from .statute_versioning import find_statute_version_at_date, get_statute_version_label

router = APIRouter()
MAX_PAGE_SIZE = 50


def _normalize_section(value: str) -> str:
    section = re.sub(r"\s+", "", value or "").casefold()
    match = re.fullmatch(r"(\d+(?:\.\d+)?[a-z]?)(?:\([^()]+\))*", section)
    return match.group(1) if match else ""


def _act_aliases(statute: Statute) -> set[str]:
    aliases = {statute.instrument_key, statute.title}
    if statute.short_title:
        aliases.add(statute.short_title)
    definition = LEGISLATION_REGISTRY.get(statute.instrument_key, {})
    aliases.update(alias for alias in definition.get("aliases", ()) if isinstance(alias, str))
    return {re.sub(r"\s+", " ", alias).strip().casefold() for alias in aliases if alias}


def resolve_statute(db: Session, act: str) -> Statute:
    """Resolve a user-entered act name/key against the stored statute catalog."""
    requested = re.sub(r"\s+", " ", act or "").strip().casefold()
    statutes = db.query(Statute).all()
    for statute in statutes:
        if requested in _act_aliases(statute):
            return statute
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Unknown act '{act}'. Hint: use an act title, short title, or stored instrument key from the Statute Library.",
    )


def aggregate_consideration(
    occurrence_rows: Iterable[tuple[StatuteReference, Case]],
    outcome_rows: Iterable[CaseOutcome],
) -> dict[str, Any]:
    """Aggregate matching reference occurrences into distinct-decision statistics."""
    outcome_by_case: dict[int, str] = {}
    for outcome in outcome_rows:
        # The caller orders stored outcome records newest-first; retain one per decision.
        outcome_by_case.setdefault(
            outcome.case_id,
            (outcome.decision_outcome or "").strip() or "unclassified",
        )

    cases: dict[int, dict[str, Any]] = {}
    for _reference, case in occurrence_rows:
        if case.id not in cases:
            cases[case.id] = {
                "case_id": case.id,
                "title": case.title,
                "citation": case.citation,
                "court": case.court or "Unknown court",
                "date": case.date.isoformat() if case.date else None,
                "year": case.date.year if case.date else None,
                "reference_count": 0,
                "outcome": outcome_by_case.get(case.id, "unclassified"),
            }
        cases[case.id]["reference_count"] += 1

    decisions = list(cases.values())
    total = len(decisions)

    def distribution(key: str) -> list[dict[str, Any]]:
        counts = Counter(str(row[key]) if row[key] is not None else "Unknown" for row in decisions)
        return [
            {
                "value": value,
                "decision_count": count,
                "denominator": total,
                "percentage": round(count * 100 / total, 1) if total else 0.0,
            }
            for value, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        ]

    # Stable two-pass ordering: reference frequency first, then recency for ties.
    decisions.sort(key=lambda row: (row["date"] or "", row["case_id"]), reverse=True)
    decisions.sort(key=lambda row: row["reference_count"], reverse=True)
    return {
        "summary": {
            "decision_count": total,
            "reference_occurrences": sum(row["reference_count"] for row in decisions),
            "denominator": total,
            "description": "Descriptive counts of distinct decisions with stored references; not evidence of legal effect or causation.",
        },
        "by_court": distribution("court"),
        "by_year": distribution("year"),
        "by_outcome": distribution("outcome"),
        "decisions": decisions,
    }


def fetch_statute_consideration(
    db: Session, act: str, section: str, page: int = 1, page_size: int = 25
) -> dict[str, Any]:
    statute = resolve_statute(db, act)
    normalized_section = _normalize_section(section)
    if not normalized_section:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unknown section '{section}' for {statute.title}. Hint: enter a base section number such as 34.",
        )

    occurrence_rows = (
        db.query(StatuteReference, Case)
        .join(Case, StatuteReference.source_case_id == Case.id)
        .filter(
            StatuteReference.instrument_key == statute.instrument_key,
            func.lower(StatuteReference.provision_section) == normalized_section,
        )
        .all()
    )
    if not occurrence_rows:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No stored references found for section {normalized_section} of {statute.title}. Hint: check the act and section, or try a base section number such as 34.",
        )

    case_ids = {case.id for _reference, case in occurrence_rows}
    outcome_rows = (
        db.query(CaseOutcome)
        .filter(CaseOutcome.case_id.in_(case_ids))
        .order_by(CaseOutcome.updated_at.desc().nullslast(), CaseOutcome.id.desc())
        .all()
    )
    result = aggregate_consideration(occurrence_rows, outcome_rows)
    page = max(1, page)
    page_size = max(1, min(MAX_PAGE_SIZE, page_size))
    total = result["summary"]["decision_count"]
    pages = max(1, math.ceil(total / page_size))
    start = (page - 1) * page_size
    result["act"] = {
        "instrument_key": statute.instrument_key,
        "title": statute.title,
        "short_title": statute.short_title,
    }
    result["section"] = normalized_section
    result["pagination"] = {
        "page": page,
        "page_size": page_size,
        "max_page_size": MAX_PAGE_SIZE,
        "total_decisions": total,
        "total_pages": pages,
    }
    result["decisions"] = result["decisions"][start : start + page_size]
    # Version lookup is limited to this bounded page and uses decision dates.
    for decision in result["decisions"]:
        decision_date = date.fromisoformat(decision["date"]) if decision["date"] else None
        version = find_statute_version_at_date(db, statute.instrument_key, decision_date)
        decision["statute_version"] = get_statute_version_label(version)
    return result


def statute_consideration_page_html() -> str:
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Statute Consideration | AI CaseLibrary</title>
<style>
body{margin:0;background:#f6f4ee;color:#14212b;font:16px/1.5 system-ui,sans-serif}main{max-width:1180px;margin:auto;padding:28px 20px 56px}h1{font-family:Georgia,serif;font-weight:normal}p,.muted{color:#63707a}.form,.panel{background:#fffdfa;border:1px solid #d9d5ca;border-radius:6px;padding:18px;margin:18px 0}.form{display:flex;gap:12px;align-items:end;flex-wrap:wrap}label{display:grid;gap:5px;font-size:13px;font-weight:650}input,button{font:inherit;padding:9px 11px;border:1px solid #b9b5aa;border-radius:4px}button{background:#285d75;color:white;border:0;cursor:pointer}.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px}.stats h2{font-size:16px}.stats ul{padding-left:20px}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;background:#fffdfa}th,td{text-align:left;padding:10px;border-bottom:1px solid #e5e1d8;vertical-align:top}th{font-size:12px;text-transform:uppercase;letter-spacing:.04em}a{color:#285d75}.pager{display:flex;justify-content:space-between;align-items:center;margin-top:12px}.error{padding:12px;background:#fff0ed;color:#8d3021;border-left:4px solid #b44734}small{color:#63707a}@media(max-width:620px){main{padding:20px 12px}.form{display:grid}.form label,.form input,.form button{width:100%;box-sizing:border-box}}
</style></head><body><main><a href="/statutes">← Statute Library</a>
<h1>Statute Consideration</h1><p>Explore stored case references to an Act section. Results are descriptive counts, not a measure of legal effect, interpretation, or causation. Outcomes include unclassified decisions and use all matching decisions as their denominator.</p>
<form class="form" id="search"><label>Act or instrument<input id="act" name="act" placeholder="e.g. IRPA or canada.irpa" required></label><label>Section<input id="section" name="section" placeholder="e.g. 34" required></label><button type="submit">Show decisions</button></form>
<div id="message" aria-live="polite"></div><div id="results"></div>
<script>
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let currentPage=1, currentPageSize=25;
function listTable(title,rows){return `<section class="panel"><h2>${esc(title)}</h2>${rows.length?`<ul>${rows.map(r=>`<li>${esc(r.value)}: ${r.decision_count} / ${r.denominator} decisions (${r.percentage}%)</li>`).join('')}</ul>`:'<p class="muted">No decisions.</p>'}</section>`}
async function load(page=1){currentPage=page;const act=document.getElementById('act').value.trim(),section=document.getElementById('section').value.trim();if(!act||!section)return;
document.getElementById('message').textContent='Loading descriptive statistics…';document.getElementById('results').innerHTML='';
try{const params=new URLSearchParams({page:String(page),page_size:String(currentPageSize)});const response=await fetch(`/api/statutes/${encodeURIComponent(act)}/${encodeURIComponent(section)}/consideration?${params}`);const data=await response.json();if(!response.ok)throw new Error(data.detail||'Unable to load statute consideration.');
document.getElementById('message').textContent='';
const rows=data.decisions.map(d=>`<tr><td><a href="/case-reader-ui/${encodeURIComponent(d.case_id)}">${esc(d.title||d.citation||'Decision')}</a><br><small>${esc(d.citation||'')}</small></td><td>${esc(d.court)}</td><td>${esc(d.date||'')}</td><td>${esc(d.statute_version)}</td><td>${esc(d.outcome)}</td><td>${d.reference_count}</td></tr>`).join('');
document.getElementById('results').innerHTML=`<h2>${esc(data.act.title)} — section ${esc(data.section)}</h2><section class="panel stats"><div><strong>${data.summary.decision_count}</strong><div>distinct decisions</div><small>${data.summary.reference_occurrences} stored reference occurrences</small></div>${listTable('By court',data.by_court)}${listTable('By year',data.by_year)}${listTable('Decision outcomes',data.by_outcome)}</section><section class="panel"><h2>Decisions</h2><p class="muted">Ranked by number of matching stored references within each decision, then most recent date. Counts are per decision, not per occurrence.</p><div class="scroll"><table><thead><tr><th>Decision</th><th>Court</th><th>Date</th><th>Statute version</th><th>Outcome</th><th>References</th></tr></thead><tbody>${rows}</tbody></table></div><div class="pager"><button ${data.pagination.page<=1?'disabled':''} onclick="load(${data.pagination.page-1})">Previous</button><span>Page ${data.pagination.page} of ${data.pagination.total_pages}</span><button ${data.pagination.page>=data.pagination.total_pages?'disabled':''} onclick="load(${data.pagination.page+1})">Next</button></div></section>`;
}catch(error){document.getElementById('message').innerHTML=`<div class="error">${esc(error.message)}</div>`}}
document.getElementById('search').addEventListener('submit',event=>{event.preventDefault();load(1)});
</script></main></body></html>"""


@router.get("/api/statutes/{act}/{section}/consideration", name="statute_consideration_analytics")
def statute_consideration_analytics(
    act: str,
    section: str,
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1),
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    """Return descriptive, distinct-decision statistics for stored section references."""
    return fetch_statute_consideration(db, act, section, page, page_size)


@router.get("/statute-consideration", response_class=HTMLResponse, include_in_schema=False)
def statute_consideration_page() -> HTMLResponse:
    return HTMLResponse(statute_consideration_page_html())
