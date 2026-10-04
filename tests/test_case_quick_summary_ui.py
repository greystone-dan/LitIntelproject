"""Bounded, offline fixtures for the stored quick-summary reader slice."""

import json
import re
import shutil
import subprocess

import pytest

from backend.pages.case_quick_summary import QUICK_SUMMARY_JS
from backend.pages.data_explorer import data_explorer_page_html


@pytest.fixture
def summary_fixture():
    # Emoji before the evidence makes JS UTF-16 indices differ from code points.
    text = '😀 Header\n[2] Earlier duplicate.\n[2] The application is dismissed. <script>& "quoted"\n'
    block_start = text.index("[2]", text.index("[2]") + 1)
    start = text.index("The application")
    evidence = dict(
        text=text[start:].strip(), start=start, end=len(text) - 1,
        block_start=block_start, paragraph_number=2,
    )
    blocks = [
        dict(type="text", start=0, end=9),
        dict(type="para", num=2, start=text.index("[2]"), end=block_start),
        dict(type="para", num=2, start=block_start, end=len(text) - 1, mark_end=block_start + 4),
    ]
    payload = dict(item=dict(full_text=text), readerData=dict(format_blocks=blocks))
    data = dict(
        case_id=7, style_of_cause='<img src=x onerror="alert(1)">',
        citation="2025 FC 7", court="Federal Court", date="2025-01-02",
        decision_outcome="dismissed", outcome_source="stored_rule",
        disposition=evidence, issue=dict(evidence, kind="standard_of_review"),
        top_statutes=[dict(instrument_key="<IRPA>", count=3, evidence=evidence),
                      dict(instrument_key="IRPR", count=1, evidence=None)],
        top_tags=[dict(category="issue", value="<refugee>", score=0.9,
                       source="<stored_tag>", evidence=evidence)],
    )
    return payload, data


NODE_SETUP = r"""
const assert=require('node:assert/strict');
const events={};
const body={
 html:'',panel:null,
 querySelectorAll(){return this.panel?[{remove:()=>{this.panel=null;this.html=''}}]:[]},
 insertAdjacentHTML(position,html){assert.equal(position,'afterbegin');this.html=html;
   this.panel={isConnected:true,open:html.includes(' open '),addEventListener(){}}},
 querySelector(selector){return selector==='.reader-quick-summary'?this.panel:target},
 addEventListener(name,handler){events[name]=handler}
};
const target={setAttribute(){},closest(){return null},scrollIntoView(){this.scrolled=true},focus(){this.focused=true}};
const readerPanel={hidden:false};
const document={getElementById:id=>id==='decisionBody'?body:readerPanel};
const window={matchMedia:()=>({matches:true})};
let readerState={caseId:7,mode:'normalized',formatted:true,payload:PAYLOAD};
let setReaderMode=mode=>{readerState.mode=mode;body.panel=null;body.html=''};
let openDecision=async id=>{readerState.caseId=id;readerState.payload=PAYLOAD;setReaderMode('normalized')};
let closeDecisionReader=()=>{readerState.caseId=null;readerState.payload=null;readerPanel.hidden=true};
const pending=[];
const fetch=(url,options)=>new Promise((resolve,reject)=>pending.push({url,options,resolve,reject}));
const tick=()=>new Promise(resolve=>setImmediate(resolve));
"""


def run_node(summary_fixture, assertions):
    node = shutil.which("node")
    if not node:
        pytest.skip("Node required")
    payload, data = summary_fixture
    script = NODE_SETUP.replace("PAYLOAD", json.dumps(payload))
    script += "\nconst DATA=" + json.dumps(data) + ";\nreaderPanel.hidden=true;\n" + QUICK_SUMMARY_JS
    script += "\nreaderPanel.hidden=false;\n"
    script += "\n(async()=>{" + assertions + "})().catch(e=>{console.error(e);process.exitCode=1});"
    result = subprocess.run([node, "-"], input=script, text=True, capture_output=True, timeout=20)
    assert result.returncode == 0, result.stderr


def test_evidence_codepoints_duplicate_numbers_and_escaping(summary_fixture):
    run_node(summary_fixture, r"""
assert.ok(quickSummaryVerifiedEvidence(DATA.disposition,readerState.payload));
for(const patch of [{paragraph_number:3},{block_start:10},{start:DATA.disposition.start+1},
                   {end:9999},{text:'fabricated'},{start:-1},{block_start:'32'}]){
 assert.equal(quickSummaryVerifiedEvidence({...DATA.disposition,...patch},readerState.payload),false);
}
const html=quickSummaryHtml(DATA,readerState.payload);
assert.ok(html.includes(`href="#decision-source-${DATA.disposition.block_start}"`));
assert.ok(!html.includes('<script>'));assert.ok(!html.includes('<img'));
for(const value of ['&lt;script&gt;&amp; &quot;quoted&quot;','&lt;IRPA&gt;','&lt;refugee&gt;',
                   'stored_rule','score 0.9','&lt;stored_tag&gt;','Standard of review','2025 FC 7','2025-01-02']){
 assert.ok(html.includes(value),value);
}
const continuation=structuredClone(readerState.payload);
continuation.readerData.format_blocks.at(-1).end=DATA.disposition.start+1;
continuation.readerData.format_blocks.push({type:'quote',start:DATA.disposition.start+1,end:DATA.disposition.end});
assert.ok(quickSummaryVerifiedEvidence(DATA.disposition,continuation));
continuation.readerData.format_blocks.at(-1).type='heading';
assert.equal(quickSummaryVerifiedEvidence(DATA.disposition,continuation),false);
""")


def test_unavailable_elements_omitted_outcome_retained(summary_fixture):
    run_node(summary_fixture, r"""
for(const data of [
 {case_id:7},
 {case_id:7,style_of_cause:null,citation:'',court:'  ',date:null,
  disposition:{...DATA.disposition,text:'fabricated'},issue:{...DATA.issue,end:9999},
  top_statutes:[],top_tags:[]}
]){
 const html=quickSummaryHtml(data,readerState.payload);
 for(const value of ['Decision outcome','unclassified','source: unknown'])assert.ok(html.includes(value),value);
 for(const value of ['Style of cause','Citation','Court','Date','Disposition','Issue','Standard of review',
                     'Top statutes','Top tags','Not stored','No verified source excerpt stored.',
                     'No stored statutes available.','No stored tags available.','<blockquote','<a ']){
  assert.ok(!html.includes(value),value);
 }
}
const partial=quickSummaryHtml({case_id:7,citation:DATA.citation,decision_outcome:'dismissed',
 outcome_source:'stored_rule'},readerState.payload);
assert.ok(partial.includes('<dt>Citation</dt><dd>2025 FC 7</dd>'));
assert.ok(partial.includes('dismissed · source: stored_rule'));
assert.ok(!partial.includes('Disposition'));
""")


def test_unverified_tags_omitted_statute_counts_retained(summary_fixture):
    run_node(summary_fixture, r"""
const invalid={...DATA.disposition,text:'fabricated'};
assert.equal(quickSummaryEvidenceHtml(invalid,readerState.payload),'');
const data={case_id:7,top_statutes:[
 {instrument_key:'IRPR',count:1,evidence:null},
 {instrument_key:'IRPA',count:3,evidence:invalid}],
 top_tags:[null,{category:'issue',value:'missing',score:1,source:'stored',evidence:null},
 {category:'issue',value:'invalid',score:1,source:'stored',evidence:invalid}]};
const html=quickSummaryHtml(data,readerState.payload);
assert.ok(html.includes('Top statutes'));
assert.ok(html.includes('<strong>IRPR</strong> · 1 stored occurrence(s)</li>'));
assert.ok(html.includes('<strong>IRPA</strong> · 3 stored occurrence(s)</li>'));
for(const value of ['Top tags','missing','invalid','No verified','<blockquote','<a '])assert.ok(!html.includes(value),value);
data.top_tags.push(DATA.top_tags[0]);
const mixed=quickSummaryHtml(data,readerState.payload);
assert.ok(mixed.includes('Top tags'));
assert.ok(mixed.includes('&lt;refugee&gt;'));
assert.ok(mixed.includes('score 0.9 · source &lt;stored_tag&gt;'));
assert.ok(mixed.includes('Source paragraph [2]'));
assert.ok(!mixed.includes('invalid'));
""")


def test_modes_errors_jumps_and_close(summary_fixture):
    run_node(summary_fixture, r"""
await openDecision(7);
assert.equal(pending.length,1);assert.equal(pending[0].url,'/api/cases/7/summary');
assert.equal(pending[0].options.method,'GET');assert.ok(body.html.includes('Loading stored quick summary'));
pending[0].resolve({ok:true,json:async()=>DATA});await tick();
assert.ok(body.html.includes('Quick summary'));assert.ok(body.html.includes(' open '));
setReaderMode('chunks');assert.equal(body.html,'');
setReaderMode('normalized');assert.ok(body.html.includes('Quick summary'));
readerState.formatted=false;setReaderMode('normalized');assert.equal(body.html,'');
readerState.formatted=true;setReaderMode('normalized');
events.click({preventDefault(){},target:{closest:()=>({dataset:{
 quickSummaryStart:String(DATA.disposition.block_start),quickSummaryParagraph:'2'}})}});
assert.ok(target.scrolled);assert.ok(target.focused);
target.focused=false;
events.click({preventDefault(){},target:{closest:()=>({dataset:{quickSummaryStart:'999',quickSummaryParagraph:'2'}})}});
assert.equal(target.focused,false);
closeDecisionReader();assert.equal(body.html,'');assert.equal(quickSummaryState.caseId,null);
readerPanel.hidden=false;await openDecision(7);pending[1].resolve({ok:false});await tick();
assert.ok(body.html.includes('Quick summary unavailable'));assert.ok(readerState.payload);
await openDecision(7);pending[2].reject(new Error('network'));await tick();
assert.ok(body.html.includes('Quick summary unavailable'));assert.ok(readerState.payload);
await openDecision(7);pending[3].resolve({ok:true,json:async()=>({...DATA,case_id:8})});await tick();
assert.ok(body.html.includes('Quick summary unavailable'));
""")


def test_stale_switch_reopen_and_close(summary_fixture):
    run_node(summary_fixture, r"""
await openDecision(7);const old=pending[0];
await openDecision(8);assert.equal(old.options.signal.aborted,true);
pending[1].resolve({ok:true,json:async()=>({...DATA,case_id:8,style_of_cause:'Current eight'})});await tick();
old.resolve({ok:true,json:async()=>({...DATA,style_of_cause:'STALE seven'})});await tick();
assert.ok(body.html.includes('Current eight'));assert.ok(!body.html.includes('STALE'));
await openDecision(8);const reopen=pending[2];await openDecision(8);
pending[3].resolve({ok:true,json:async()=>({...DATA,case_id:8,style_of_cause:'Newest eight'})});await tick();
reopen.resolve({ok:true,json:async()=>({...DATA,case_id:8,style_of_cause:'STALE reopen'})});await tick();
assert.ok(body.html.includes('Newest eight'));assert.ok(!body.html.includes('STALE'));
await openDecision(7);const closing=pending[4];closeDecisionReader();
closing.resolve({ok:true,json:async()=>DATA});await tick();assert.equal(body.html,'');
""")


def test_builder_additive_integration():
    html = data_explorer_page_html()
    assert html.count(QUICK_SUMMARY_JS) == 1
    assert html.index(QUICK_SUMMARY_JS) > html.index("const mostCitedSetReaderMode=")
    for retained in ["Extracted case summary", "extractedReaderSummaryHtml", "readerMostCited",
                     "renderChunkedDecision", "readerAssessmentToggle", "Similar paragraphs"]:
        assert retained in html


def test_initial_deep_link_load_started_before_wrapper_installation(summary_fixture):
    run_node(summary_fixture, r"""
await quickSummaryPreviousOpen(7);
assert.equal(pending.length,1);
assert.equal(pending[0].url,'/api/cases/7/summary');
pending[0].resolve({ok:true,json:async()=>DATA});await tick();
assert.ok(body.html.includes('Quick summary'));
setReaderMode('normalized');
assert.equal(pending.length,1);
""")


def test_initial_deep_link_already_loaded_before_script_installation(summary_fixture):
    run_node(summary_fixture, r"""
adoptLoadedQuickSummary();mountQuickSummary();
assert.equal(pending.length,1);
pending[0].resolve({ok:true,json:async()=>DATA});await tick();
assert.ok(body.html.includes('Quick summary'));
adoptLoadedQuickSummary();
assert.equal(pending.length,1);
""")


@pytest.mark.parametrize("width", [1280, 390])
def test_chromium_offline_reader_fixture(summary_fixture, tmp_path, width):
    """Actual DOM, native disclosure, Unicode anchors; no server or database."""
    chromium = shutil.which("google-chrome") or shutil.which("chromium")
    if not chromium:
        pytest.skip("Chromium required for offline browser validation")
    payload, data = summary_fixture
    html = data_explorer_page_html()
    helpers = "const esc=" + html.split("const esc=", 1)[1].split("\n", 1)[0] + "\n"
    for name in ["highlightedDecision", "formattedDecision"]:
        helpers += html[html.index("function " + name + "("):].split("\n", 1)[0] + "\n"
    helpers += html[html.index("function extractedReaderSummaryHtml("):].split(
        "const extractedSummaryPreviousMode=", 1,
    )[0]
    payload["readerData"]["extracted_summary"] = [{
        "key": "disposition", "value": data["disposition"]["text"], "evidence": data["disposition"]["text"],
        "block_start": data["disposition"]["block_start"], "block_type": "para", "paragraph_number": 2,
    }]
    setup = r"""
const PAYLOAD=__PAYLOAD__,DATA=__DATA__;
let readerState={caseId:null,mode:'normalized',formatted:true,payload:null};
let setReaderMode=mode=>{
 readerState.mode=mode;const p=readerState.payload;
 document.getElementById('decisionBody').innerHTML=extractedReaderSummaryHtml(p.readerData)+
 (mode==='chunks'?'Chunks':formattedDecision(p.item.full_text,[],[],p.readerData.format_blocks));
};
let openDecision=async id=>{readerState.caseId=id;readerState.payload=PAYLOAD;setReaderMode('normalized')};
let closeDecisionReader=()=>{readerState.payload=null;readerState.caseId=null};
const fetch=async()=>({ok:true,json:async()=>DATA});
"""
    setup = setup.replace("__PAYLOAD__", json.dumps(payload)).replace("__DATA__", json.dumps(data))
    assertions = r"""
function check(value,label){if(!value)throw new Error(label)}
(async()=>{
 await quickSummaryPreviousOpen(7);await Promise.resolve();
 const body=document.getElementById('decisionBody');
 check(body.firstElementChild.classList.contains('reader-quick-summary'),'summary first');
 check(body.querySelector('.reader-extracted-summary'),'existing extracted card');
 check(body.querySelector('.reader-quick-summary').open,'default open');
 check(!body.querySelector('.reader-quick-summary img'),'safe identity');
 const links=body.querySelectorAll('[data-quick-summary-start]');
 check(links.length===4,'all verified links');
 for(const link of links){link.click();check(document.activeElement.id==='decision-source-'+DATA.disposition.block_start,'duplicate anchor focus')}
 const panel=body.querySelector('.reader-quick-summary');
 panel.querySelector('summary').click();await new Promise(resolve=>setTimeout(resolve,50));
 check(!panel.open,'native collapse');
 setReaderMode('chunks');check(!body.querySelector('.reader-quick-summary'),'chunks hidden');
 check(body.querySelector('.reader-extracted-summary'),'extracted retained in chunks');
 setReaderMode('normalized');check(!body.querySelector('.reader-quick-summary').open,'collapse preserved');
 readerState.formatted=false;setReaderMode('normalized');check(!body.querySelector('.reader-quick-summary'),'plain hidden');
 readerState.formatted=true;setReaderMode('normalized');check(body.querySelector('.reader-quick-summary'),'formatted remount');
 await openDecision(7);check(body.querySelector('.reader-quick-summary').open,'reopen default');
 check(document.documentElement.scrollWidth<=innerWidth,'no horizontal overflow');
 quickSummaryState.data={case_id:7,top_statutes:[{instrument_key:'IRPR',count:1,evidence:null}],
  top_tags:[{category:'issue',value:'INVALID_TAG',evidence:{...DATA.disposition,text:'fabricated'}}]};
 mountQuickSummary();
 const sparse=body.querySelector('.reader-quick-summary');
 check(sparse.querySelectorAll('dt').length===1,'missing identity rows omitted');
 check(sparse.querySelector('dt').textContent==='Decision outcome','outcome retained');
 check(sparse.textContent.includes('unclassified · source: unknown'),'honest missing outcome');
 check(sparse.querySelectorAll('h4').length===1,'only stored statute heading');
 check(sparse.textContent.includes('IRPR'),'statute count retained');
 check(!sparse.querySelector('blockquote')&&!sparse.querySelector('a'),'absent evidence omitted');
 check(!sparse.textContent.includes('INVALID_TAG')&&!sparse.textContent.includes('No verified'),'no invalid tags or placeholders');
 quickSummaryState.data={case_id:7};mountQuickSummary();
 check(!body.querySelector('.reader-quick-summary h4'),'empty sections omitted');
 closeDecisionReader();check(!body.querySelector('.reader-quick-summary'),'close removes');
 document.getElementById('result').textContent='BROWSER_PASS';
})().catch(error=>{document.getElementById('result').textContent='BROWSER_FAIL: '+error.message});
"""
    # Escape script endings in fixture text without changing the resulting JS strings.
    script = (helpers + setup + QUICK_SUMMARY_JS + assertions).replace("</script", "<\\/script")
    document = (
        '<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<style>*{box-sizing:border-box}body{margin:8px}blockquote{margin:8px}summary:focus-visible{outline:2px solid blue}</style>'
        '<div id="caseReaderPanel"><div id="decisionBody"></div></div><pre id="result"></pre><script>'
        + script + "</script>"
    )
    fixture_file = tmp_path / "reader.html"
    fixture_file.write_text(document, encoding="utf-8")
    result = subprocess.run(
        [chromium, "--headless", "--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage", "--disable-background-networking",
         "--disable-extensions", "--no-first-run", "--no-default-browser-check",
         f"--user-data-dir={tmp_path / 'profile'}", f"--window-size={width},900",
         "--virtual-time-budget=3000", "--dump-dom", fixture_file.as_uri()],
        capture_output=True, text=True, timeout=30,
    )
    marker = re.search(r'<pre id="result">(.*?)</pre>', result.stdout, re.S)
    assert result.returncode == 0, result.stderr[-2000:]
    assert marker and marker.group(1) == "BROWSER_PASS", marker.group(1) if marker else result.stderr[-2000:]
