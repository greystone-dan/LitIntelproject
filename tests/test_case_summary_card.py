from datetime import date
from types import SimpleNamespace as Row
import json
import re
import shutil
import subprocess

from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from backend.case_summary import get_db
from backend.case_summary_card import (
    _key_paragraphs,
    _ranked_cited_paragraph,
    project_case_summary_card,
    router,
)
from backend.case_formatter import format_decision
from backend.pages.case_summary_card import SUMMARY_CARD_JS, inject_case_summary_card
from backend.pages.data_explorer import data_explorer_page_html


def _case(text="", **overrides):
    values = dict(
        id=42,
        title="Example v Canada",
        citation="2024 FC 42",
        court="Federal Court",
        date=date(2024, 1, 2),
        full_text=text,
        metadata_json=None,
    )
    values.update(overrides)
    return Row(**values)


def _outcome(text, evidence, **overrides):
    start = text.index(evidence)
    values = dict(
        decision_outcome="allowed",
        outcome_status="determined",
        confidence=0.9,
        source="stored_rule",
        disposition_evidence=evidence,
        evidence_offset_start=start,
        evidence_offset_end=start + len(evidence),
    )
    values.update(overrides)
    return Row(**values)


class _ResultRows:
    def __init__(self, rows):
        self.rows = rows

    def all(self):
        return self.rows


class _CitationRows:
    def __init__(self, rows):
        self.rows = rows
        self.statement = None

    def execute(self, statement):
        self.statement = statement
        return _ResultRows(self.rows)


def test_each_key_paragraph_rule_returns_exact_numbered_source_with_reason():
    text = (
        "Federal Court\nDate: 2024-01-02\nBefore: Justice Jane Doe\n"
        "[1] The standard of review is reasonableness.\n"
        "[2] The application is allowed.\n"
        "[3] The record is returned for reconsideration."
    )
    case = _case(text, metadata_json={
        "reader_extracted": {
            "judge": "Jane Doe",
            "_field_sources": {"judge": {"text": "Jane Doe"}},
        }
    })
    outcome = _outcome(text, "application is allowed")
    blocks = format_decision(text)
    paragraphs = _key_paragraphs(_CitationRows([(3, 5), (2, 2)]), case, outcome)

    assert [row.paragraph_number for row in paragraphs] == [2, 3, 1]
    assert [row.selection_rule for row in paragraphs] == [
        "Disposition/conclusion paragraph",
        "Most stored later pinpoint citations",
        "Standard-of-review statement",
    ]
    assert paragraphs[1].pinpoint_citation_count == 5
    for item in paragraphs:
        assert item.text == text[item.start:item.end]
        block = next(row for row in blocks if row["start"] == item.block_start)
        assert block["type"] == "para"
        assert block["num"] == item.paragraph_number


def test_disposition_heading_is_a_fallback_and_duplicate_rule_is_disclosed():
    text = "Reasons\n[1] The court finds review applies.\nConclusion\n[2] The appeal is dismissed."
    result = _key_paragraphs(_CitationRows([]), _case(text), None)

    assert [item.paragraph_number for item in result] == [2]
    assert result[0].selection_rule == "Disposition/conclusion paragraph"


def test_later_pinpoint_ranking_uses_stored_resolved_citation_occurrences():
    text = "[1] First point.\n[2] Second point."
    case = _case(text)
    rows = _CitationRows([(2, 4), (1, 2)])
    paragraphs = [
        {
            "number": block["num"],
            "start": block["start"],
            "end": block["end"],
            "text": text[block["start"]:block["end"]],
        }
        for block in format_decision(text)
        if block["type"] == "para"
    ]
    selected = _ranked_cited_paragraph(rows, case, paragraphs)

    assert selected[0]["number"] == 2
    assert selected[1] == 4
    sql = str(rows.statement)
    assert "cases.date >" in sql
    assert "citations.unresolved IS false" in sql
    assert "citations.target_paragraph IS NOT NULL" in sql


def test_missing_evidence_and_metadata_are_omitted_not_inferred():
    text = "[1] Reasons continue."
    result = project_case_summary_card(
        _case(text, citation=None, court=None, date=None, metadata_json=None),
    )

    assert result.model_dump(exclude_none=True) == {
        "case_id": 42,
        "statutes": [],
        "top_tags": [],
        "key_paragraphs": [],
    }
    assert result.judge is None
    assert result.outcome is None
    assert _key_paragraphs(_CitationRows([]), _case(text, date=None), None) == []


def test_outcome_statute_and_active_tag_layers_remain_separate():
    text = "[1] The application was allowed under IRPA."
    evidence = "IRPA"
    start = text.index(evidence)
    tag = Row(
        id=1, taxonomy_version="ca_legal_v3_core", category="issue",
        value="fairness", score=0.8, source="stored_tag", evidence=evidence,
        offset_start=start, offset_end=start + len(evidence),
    )
    other_taxonomy = Row(**{**tag.__dict__, "id": 2, "taxonomy_version": "old"})
    references = [
        Row(instrument_key="IRPA", reference_kind="statute"),
        Row(instrument_key="IRPA", reference_kind="statute"),
        Row(instrument_key="2024 FC 5", reference_kind="case"),
    ]
    result = project_case_summary_card(
        _case(text), _outcome(text, "allowed"), [tag, other_taxonomy], references,
    )

    assert result.outcome.value == "allowed"
    assert result.outcome.source == "stored_rule"
    assert [(row.instrument_key, row.count) for row in result.statutes] == [("IRPA", 2)]
    assert [(row.category, row.value, row.source) for row in result.top_tags] == [
        ("issue", "fairness", "stored_tag")
    ]


class _ReadOnlySession:
    def __init__(self, case):
        self.case = case
        self.statements = []

    def scalar(self, statement):
        self.statements.append(statement)
        entity = statement.column_descriptions[0]["entity"]
        return self.case if entity.__name__ == "Case" else None

    def scalars(self, statement):
        self.statements.append(statement)
        return iter(())

    def execute(self, statement):
        self.statements.append(statement)
        return _ResultRows([])


def test_independent_api_is_read_only_and_unknown_cases_return_404():
    app = FastAPI()
    app.include_router(router)
    session = _ReadOnlySession(_case("[1] A short holding."))
    app.dependency_overrides[get_db] = lambda: session
    with TestClient(app) as client:
        response = client.get("/api/cases/42/summary-card")
        assert response.status_code == 200
        assert response.json()["case_id"] == 42
        assert response.json()["citation"] == "2024 FC 42"
        assert response.json()["key_paragraphs"] == []
        assert len(session.statements) == 5
        assert all(statement.is_select for statement in session.statements)

        app.dependency_overrides[get_db] = lambda: _ReadOnlySession(None)
        assert client.get("/api/cases/43/summary-card").status_code == 404
        assert client.get("/api/cases/not-an-id/summary-card").status_code == 422
        assert "/api/cases/{case_id}/summary-card" in client.get("/openapi.json").json()["paths"]


def test_reader_summary_card_truncates_only_at_sentence_and_links_source():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node is required to execute summary-card browser helpers")
    prefix = SUMMARY_CARD_JS.split("function resetExtractiveSummaryCard", 1)[0]
    script = prefix + r"""
const assert=require('node:assert/strict');
const state=extractiveSummaryState;
const longText='The court allows the application. '+('Further analysis without a new full stop '.repeat(30));
const clipped=extractiveSummaryTruncate(longText,50);
assert.equal(clipped.text,'The court allows the application.…');
assert.equal(clipped.truncated,true);
const fullText='[3] '+longText;
global.readerState={caseId:42,payload:{item:{full_text:fullText},
  readerData:{format_blocks:[{type:'para',num:3,start:0,end:fullText.length}]}},
  mode:'normalized',formatted:true};
const html=extractiveSummaryHtml({
  case_id:42,
  key_paragraphs:[{text:fullText,start:0,end:fullText.length,paragraph_number:3,block_start:0,
    selection_rule:'Disposition/conclusion paragraph',pinpoint_citation_count:4}]
});
assert.ok(html.includes('Selected passages, not a summary written by AI'));
assert.ok(html.includes('The court allows the application.…'));
assert.ok(html.includes('href="#decision-source-0"'));
assert.ok(html.includes('View full paragraph [3]'));
const body={removed:0,inserted:'',querySelectorAll(){return []},
  insertAdjacentHTML(where,value){assert.equal(where,'afterbegin');this.inserted=value}};
const panel={hidden:false};
global.document={getElementById(id){return id==='decisionBody'?body:id==='caseReaderPanel'?panel:null}};
state.status='ready';state.caseId=42;state.data={case_id:42};
mountExtractiveSummaryCard();
assert.equal(body.inserted,'');
state.data={case_id:42,citation:'2024 FC 42'};
mountExtractiveSummaryCard();
assert.ok(body.inserted.includes('reader-extractive-summary'));
"""
    result = subprocess.run([node, "-e", script], capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr


def test_reader_injects_independent_endpoint_and_conditionally_mounted_card():
    html = data_explorer_page_html()
    standalone = inject_case_summary_card("<body></body>")

    assert "/api/cases/${encodeURIComponent(caseId)}/summary-card" in html
    assert "reader-extractive-summary" in html
    assert "if(state.status!=='ready'||!extractiveSummaryHasData(state.data)" in html
    assert "Selected passages, not a summary written by AI" in html
    assert 'id="readerKeyboardHelpToggle"' in html
    assert '<kbd>j</kbd> / <kbd>n</kbd> Next paragraph' in html
    assert 'id="readerPrintCitation"' in html
    assert "href=\"#decision-source-${start}\"" in html
    assert "reader-extractive-summary" in standalone
    assert "</body>" in standalone


@pytest.mark.parametrize("width", [1280, 390])
def test_chromium_reader_card_is_conditional_and_source_link_focuses_paragraph(tmp_path, width):
    chromium = shutil.which("google-chrome") or shutil.which("chromium")
    if not chromium:
        pytest.skip("Chromium required for offline reader validation")
    text = "[3] The court allows the application. " + (
        "Further reasons explain the record and statutory context. " * 24
    )
    payload = {
        "item": {"full_text": text},
        "readerData": {
            "format_blocks": [{
                "type": "para", "num": 3, "start": 0, "mark_end": 3, "end": len(text),
            }],
        },
    }
    response = {
        "case_id": 42,
        "citation": "2024 FC 42",
        "key_paragraphs": [{
            "paragraph_number": 3,
            "text": text,
            "start": 0,
            "end": len(text),
            "block_start": 0,
            "selection_rule": "Disposition/conclusion paragraph",
            "pinpoint_citation_count": 4,
        }],
    }
    setup = r"""
let readerState={caseId:null,mode:'normalized',formatted:true,payload:null};
let responseData={case_id:41};
let fixturePayload=__PAYLOAD__;
const responseBody=__RESPONSE__;
const body=document.getElementById('decisionBody');
let setReaderMode=mode=>{
  readerState.mode=mode;readerState.formatted=mode==='normalized';
  if(readerState.payload&&readerState.formatted){
    const block=readerState.payload.readerData.format_blocks[0];
    body.innerHTML=`<p class="fmt-para" id="decision-source-${block.start}" data-para="${block.num}">${readerState.payload.item.full_text}</p>`;
  }else body.replaceChildren();
};
let openDecision=async id=>{
  readerState.caseId=id;readerState.payload=fixturePayload;setReaderMode('normalized');
};
let closeDecisionReader=()=>{readerState.caseId=null;readerState.payload=null;body.replaceChildren()};
let fetch=async()=>({ok:true,json:async()=>responseData});
"""
    setup = setup.replace("__PAYLOAD__", json.dumps(payload)).replace(
        "__RESPONSE__", json.dumps(response),
    )
    assertions = r"""
function check(value,label){if(!value)throw new Error(label)}
const wait=()=>new Promise(resolve=>setTimeout(resolve,30));
(async()=>{
  await openDecision(41);await wait();
  check(!body.querySelector('.reader-extractive-summary'),'missing data stays hidden');
  responseData=responseBody;
  await openDecision(42);await wait();
  const card=body.querySelector('.reader-extractive-summary');
  check(card,'data mounts card');
  check(!card.open,'native card starts collapsed');
  check(card.textContent.includes('Selected passages, not a summary written by AI'),'fixed notice');
  const excerpt=card.querySelector('li p').textContent;
  check(excerpt.startsWith('[3] The court allows the application.'),'source text retained');
  check(/[.!?]…$/.test(excerpt)&&excerpt.length<__TEXT_LENGTH__,'sentence truncation');
  const link=card.querySelector('a[data-extractive-summary-start]');
  check(link&&link.getAttribute('href')==='#decision-source-0','full paragraph source link');
  card.open=true;link.click();
  check(document.activeElement.id==='decision-source-0','source link focuses exact paragraph');
  check(document.documentElement.scrollWidth<=innerWidth,'no horizontal overflow');
  document.getElementById('result').textContent='BROWSER_PASS';
})().catch(error=>{document.getElementById('result').textContent='BROWSER_FAIL: '+error.message});
"""
    assertions = assertions.replace("__TEXT_LENGTH__", str(len(text)))
    shell = (
        "<!doctype html><html><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"></head>"
        "<body><div id=\"caseReaderPanel\"><div id=\"decisionBody\"></div></div>"
        "<pre id=\"result\"></pre><script>" + setup + "</script></body></html>"
    )
    document = inject_case_summary_card(shell)
    fixture_file = tmp_path / f"summary-card-{width}.html"
    fixture_file.write_text(document.replace("</body>", "<script>" + assertions + "</script></body>"), encoding="utf-8")
    result = subprocess.run(
        [
            chromium, "--headless", "--no-sandbox", "--disable-gpu",
            "--disable-dev-shm-usage", "--disable-background-networking",
            "--disable-extensions", "--no-first-run", "--no-default-browser-check",
            f"--user-data-dir={tmp_path / ('profile-' + str(width))}",
            f"--window-size={width},900", "--virtual-time-budget=3000",
            "--dump-dom", fixture_file.as_uri(),
        ],
        capture_output=True, text=True, timeout=30,
    )
    marker = re.search(r'<pre id="result">(.*?)</pre>', result.stdout, re.S)
    assert result.returncode == 0, result.stderr[-2000:]
    assert marker and marker.group(1) == "BROWSER_PASS", marker.group(1) if marker else result.stderr[-2000:]
