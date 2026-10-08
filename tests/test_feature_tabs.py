from types import SimpleNamespace
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess

import pytest

from backend import routes
from backend.analytics_service import fetch_fc_activity_breakdowns, fetch_fc_activity_flow
from backend.citation_map import _build_citation_intelligence_insights


class ScalarDatabase:
    def __init__(self, scalar_values):
        self.scalar_values = iter(scalar_values)

    def scalar(self, statement):
        return next(self.scalar_values)


def test_about_stats_returns_library_counts():
    database = ScalarDatabase([10, 11, 12, 13, 20, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    result = routes.about_stats(database)

    assert result == {
        "cases": 10,
        "case_chunks": 11,
        "case_sources": 12,
        "ingestion_runs": 13,
        "citations": 20,
        "linked_citations": 15,
        "judge_profiles": 3,
        "case_judge_profiles": 4,
        "citation_metrics": 5,
        "statute_references": 6,
        "case_tags": 7,
        "case_chunk_embeddings": 8,
        "fc_activity_cases": 9,
        "fc_activity_documents": 10,
        "fc_procedural_history": 11,
    }


def test_build_citation_intelligence_insights_are_actionable():
    insights = _build_citation_intelligence_insights(
        unique_citing_cases=12,
        total_occurrences=47,
        avg_mentions_per_case=3.9,
        max_mentions_in_single_case=12,
        top_citing_case={"title": "A v. Canada", "mention_count": 12},
        top_court={"court": "Federal Court", "case_count": 9},
        top_judge={"judge": "Justice Smith", "case_count": 4},
        top_statute={"provision": "IRPA s. 34(1)(f)", "case_count": 6},
    )

    assert len(insights) >= 4
    assert any(item["title"] == "Most active citing decision" for item in insights)
    assert any(item["title"] == "Top court" for item in insights)
    assert any("IRPA" in item["detail"] for item in insights)


def test_citation_intelligence_routes_delegate_to_existing_helpers(monkeypatch):
    case = SimpleNamespace(id=7)
    database = object()
    monkeypatch.setattr(routes, "_get_case_or_404", lambda case_id, db: case)
    monkeypatch.setattr(routes, "_ci_overview", lambda db, case_id: {"case_id": case_id})
    monkeypatch.setattr(routes, "_ci_timeline", lambda db, case_id: [{"year": 2025}])

    assert routes.citation_intelligence_overview(7, database) == {"case_id": 7}
    assert routes.citation_intelligence_timeline(7, database) == [{"year": 2025}]


def test_compatibility_routes_select_tabs():
    assert routes.about_page().headers["location"] == "/data-explorer?tab=about"
    assert routes.citation_intelligence_page().headers["location"] == "/data-explorer?tab=citation-intelligence"
    assert routes.judges_page().headers["location"] == "/data-explorer?tab=judge-profile"
    assert routes.fc_history_page().headers["location"] == "/data-explorer?tab=fc-history"


def test_fc_activity_flow_route_delegates_to_live_aggregation(monkeypatch):
    database = object()
    expected = {"total": 4, "nodes": [], "links": []}
    monkeypatch.setattr(routes, "fetch_fc_activity_flow", lambda db, city="", source_type="": expected)

    assert routes.fc_activity_flow("Toronto", "a2aj", database) == expected


def test_fc_activity_breakdowns_use_structured_case_fields():
    class Database:
        def __init__(self):
            self.rows = iter(
                [
                    [SimpleNamespace(label="Toronto", count=12), SimpleNamespace(label="Vancouver", count=4)],
                    [SimpleNamespace(label="Immigration", count=13), SimpleNamespace(label="Administrative", count=3)],
                    [SimpleNamespace(label="Regular", count=11), SimpleNamespace(label="Simplified", count=5)],
                ]
            )

        def execute(self, statement):
            return SimpleNamespace(all=lambda: next(self.rows))

    result = fetch_fc_activity_breakdowns(Database(), city="Toronto")

    assert result == {
        "city": "Toronto",
        "registry_locations": [{"label": "Toronto", "count": 12}, {"label": "Vancouver", "count": 4}],
        "case_classes": [{"label": "Immigration", "count": 13}, {"label": "Administrative", "count": 3}],
        "tracks": [{"label": "Regular", "count": 11}, {"label": "Simplified", "count": 5}],
    }


def test_fc_activity_flow_uses_exclusive_procedural_branches():
    class Database:
        def execute(self, statement):
            return SimpleNamespace(
                all=lambda: [
                    SimpleNamespace(branch="active", count=2),
                    SimpleNamespace(branch="leave_refused", count=3),
                    SimpleNamespace(branch="leave_jr_granted", count=4),
                    SimpleNamespace(branch="leave_jr_dismissed", count=5),
                    SimpleNamespace(branch="leave_granted_pending_jr", count=6),
                    SimpleNamespace(branch="direct_jr_granted", count=7),
                    SimpleNamespace(branch="direct_jr_pending", count=8),
                    SimpleNamespace(branch="closed_before_leave", count=9),
                    SimpleNamespace(branch="unresolved", count=10),
                ]
            )

    result = fetch_fc_activity_flow(Database())
    links = {(item["source"], item["target"]): item["value"] for item in result["links"]}

    assert result["total"] == 54
    assert result["semantics"] == "exclusive_procedural_branches"
    assert sum(value for (source, _), value in links.items() if source == "total") == result["total"]
    assert links[("leave_granted", "leave_jr_granted")] == 4
    assert links[("leave_granted", "leave_jr_dismissed")] == 5
    assert links[("direct_jr", "direct_jr_granted")] == 7
    assert "overlap" in result["note"]


def test_rendered_shell_exposes_tabs_and_product_title():
    html = routes._data_explorer_page_html()

    for label in (
        "About",
        "Case search",
        "Research Bench",
        "Site Architecture",
        "Citation Intelligence",
        "Judge Profile",
        "Data explorer",
        "FC History",
        "Immigration Litigation Intelligence Tool",
    ):
        assert label in html

    assert "Decision desk" not in html
    assert "Litigation workbench" not in html
    assert "Case search and analytics" not in html
    assert 'id="aboutOutcomeChart"' not in html
    assert 'data-tab="judge">Judge outcomes</button>' not in html
    assert 'id="judgePanel"' not in html


def test_data_explorer_word_export_shares_search_actions_with_csv():
    html = routes._data_explorer_page_html()

    search_actions = re.findall(r'<div class="search-actions">(.*?)</div>', html)
    export_actions = next(actions for actions in search_actions if 'id="downloadSearchWord"' in actions)
    assert 'type="submit" class="sq-go">Search cases</button>' in export_actions
    assert (
        '<a id="downloadSearchWord" class="qf-link" href="/search/export.docx" '
        'hidden aria-hidden="true">Download Word</a>'
    ) in export_actions
    assert 'id="downloadSearchCsv"' not in html
    assert '<div class="search-status" id="searchMeta"' in html
    assert 'id="searchTipsPopover" popover role="dialog"' in html
    assert 'id="searchTipsToggle" popovertarget="searchTipsPopover"' in html
    assert 'id="searchQueryEcho" role="status"' in html
    assert "data.query_echo" in html
    assert "button.href='/search/export.docx'+(params.size?'?'+params:'')" in html
    assert "Object.entries(searchValues()).forEach(([name,value])=>{if(value)params.set(name,value)})" in html
    search_values = re.search(r"function searchValues\(\)\{return \{([^}]+)\};\}", html)
    assert search_values is not None
    assert re.findall(r"(?:^|,)([a-z_]+):", search_values.group(1)) == [
        "query",
        "cites",
        "cites_case_id",
        "tags",
        "government_outcome",
        "minister",
        "judge",
        "court",
        "year",
        "case_type",
        "sort_by",
        "limit",
    ]
    assert "let filtersDirty=false" in html
    assert "requestEditVersion=editVersion" in html
    assert "filtersDirty=editVersion!==requestEditVersion" in html
    assert "professionalSearchGeneration=0" in html
    assert "isCurrent:()=>requestId===professionalSearchGeneration" in html
    assert "document.addEventListener('input',markFiltersDirty)" in html
    assert "document.addEventListener('change',markFiltersDirty)" in html
    assert (
        "!document.getElementById('searchUseRag')?.checked&&!filtersDirty"
        "&&meta.dataset.state==='success'&&meta.textContent.includes('matching decision')"
        "&&Boolean(results.querySelector('.case-result'))"
    ) in html
    assert "#downloadSearchWord[hidden]{display:none!important}" in html


def test_reader_renders_backend_cited_paragraph_metadata():
    html = routes._data_explorer_page_html()

    assert "Number(b.cited_by_count)>0" in html
    assert "Cited by ${b.cited_by_count} cases" in html
    assert "background:#fff9e8" in html
    assert ".fmt-para.is-cited-by{color:#202522}" in html
    def luminance(color):
        channels = [int(color[index : index + 2], 16) / 255 for index in (0, 2, 4)]
        linear = [
            channel / 12.92
            if channel <= 0.04045
            else ((channel + 0.055) / 1.055) ** 2.4
            for channel in channels
        ]
        return sum(value * weight for value, weight in zip(linear, (0.2126, 0.7152, 0.0722)))

    def contrast_ratio(background, foreground):
        return (luminance(background) + 0.05) / (luminance(foreground) + 0.05)

    assert contrast_ratio("fff9e8", "202522") >= 4.5
    assert ".rs-context-text .fmt-para.is-cited .fmt-para-num{color:#202522}" in html
    assert contrast_ratio("fff4c2", "202522") >= 4.5
    assert 'data-para="${b.num}"' in html


def test_inline_reader_keyboard_navigation_and_print_contract():
    html = routes._data_explorer_page_html()

    assert 'id="readerKeyboardHelpToggle"' in html
    assert 'id="readerKeyboardHelp"' in html
    assert '<kbd>j</kbd> / <kbd>n</kbd> Next paragraph' in html
    assert '<kbd>k</kbd> / <kbd>p</kbd> Previous paragraph' in html
    assert 'id="readerPrintCitation"' in html
    assert '#decisionBody .fmt-para.is-reader-current' in html
    assert '@media print' in html
    assert '#decisionBody .fmt-para{break-inside:avoid!important;page-break-inside:avoid!important' in html
    assert '#caseReaderPanel .reader-pane.target' in html
    assert '#caseReaderPanel .reader-pane.linked' in html
    controller = html.split('/* Inline reader keyboard navigation and print behavior. */', 1)[1]
    controller = controller.split('</script>', 1)[0]
    assert "key==='j'||key==='n'?1:key==='k'||key==='p'?-1:0" in controller
    assert "readerTypingTarget(event.target)" in controller
    assert "target.setAttribute('aria-current','location')" in controller
    assert "target.classList.add('is-reader-current')" in controller
    assert "readerState.formatted=true" in controller
    assert "window.addEventListener('beforeprint'" in controller
    assert "window.addEventListener('afterprint'" in controller


def test_reader_most_cited_paragraphs_ranking_jumps_and_reset():
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is required to execute the reader controls')
    html = routes._data_explorer_page_html()
    panel = html.split('<details id="readerMostCited"', 1)[1].split('</details>', 1)[0]
    assert 'hidden' in panel.split('>', 1)[0]
    assert 'open' not in panel.split('>', 1)[0]
    assert '<summary>Most cited paragraphs</summary>' in panel
    controller = html.split('/* Most cited paragraphs: reader-only controls. */', 1)[1].split('</script>', 1)[0]
    summary_controller = html[html.index('function extractedReaderSummaryHtml('):].split('</script>', 1)[0]
    formatter = html.split('function formattedDecision(', 1)[1].split('\n', 1)[0]
    loader = html.split('async function openDecision(', 1)[1].split('\nfunction renderJudge(', 1)[0]
    assert html.index('const sidePreviousSetReaderMode=') < html.index('const mostCitedSetReaderMode=')
    assert html.index('const extractedSummaryPreviousMode=') < html.index('const mostCitedSetReaderMode=')
    assert html.index('const citationWorkspaceOpenDecision=') < html.index('const mostCitedOpenDecision=')
    script = r"""
const assert=require('node:assert/strict');
const esc=value=>String(value).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const readerState={caseId:7,mode:'chunks',formatted:false,payload:null};
const nodes={readerMostCited:{hidden:true,open:false},readerMostCitedList:{innerHTML:''},decisionBody:{querySelectorAll(selector){return selector==='.reader-extracted-summary'?[]:[target,duplicate]},querySelector(selector){assert.equal(selector,`[id="decision-source-${block.start}"]`);return target},insertAdjacentHTML(where,html){assert.equal(where,'afterbegin');this.summaryHtml=html},addEventListener(name,handler){this[name]=handler}}};
const target={dataset:{para:'2'},setAttribute(name,value){this[name]=value},scrollIntoView(options){this.scrolled=options},focus(options){this.focused=options},closest(){return null}};
const duplicate={dataset:{para:'2'},setAttribute(){throw Error('Duplicate paragraph received an anchor')}};
const document={getElementById(id){return nodes[id]??={scrollIntoView(){},replaceChildren(){}}},addEventListener(name,handler){this[name]=handler}};
let reducedMotion=false;
const window={matchMedia(query){assert.equal(query,'(prefers-reduced-motion: reduce)');return {matches:reducedMotion}}};
let fail=false,closed=false,modeCalls=0;
let openDecision=async function(id){assert.equal(nodes.readerMostCited.hidden,true);assert.equal(nodes.readerMostCited.open,false);assert.equal(nodes.readerMostCitedList.innerHTML,'');if(fail)return;readerState.caseId=id;readerState.payload=payload;setReaderMode('normalized');};
let closeDecisionReader=function(){closed=true;readerState.payload=null};
let setReaderMode=function(mode){modeCalls++;readerState.mode=mode;if(mode==='normalized'&&readerState.formatted)target.id=`decision-source-${block.start}`;else delete target.id};
function highlightedDecision(text,citations,tags,start,end,chars){return esc(chars.slice(start,end).join(''))}
function formattedDecision(FORMATTER
CONTROLLER
// This ranking fixture stubs transport only; durable helper/Retry contracts
// execute the real helper in test_panel_helpers.js.
async function fetchCurrentPanel(url,container,{render,onError}){
  try{await render(await(await fetch(url)).json(),()=>true)}catch(_){onError?.()}
}
const actualOpenDecision=async function(BASE_LOADER
const num=Number,extractDocketFromPayload=()=>null;
let renderFailure=false;
function renderCaseReaderPane(){if(renderFailure)throw Error('Rendering failed')}
const fetch=async()=>({ok:true,json:async()=>({case:{full_text:text},citation_metrics:{},format_blocks:[block]})});
const text='😀 prefix [2] <script>& "quoted" 😀 body';
const chars=Array.from(text),start=chars.join('').indexOf('[2]')-1;
const block={type:'para',num:2,start,mark_end:start+3,end:chars.length,cited_by_count:4};
const payload={item:{full_text:text},readerData:{format_blocks:[block],extracted_summary:[{key:'disposition',label:'Disposition',value:'stored disposition',evidence:'stored disposition',block_start:start,block_type:'para',paragraph_number:2}]}};
const rows=[{...block,num:10,cited_by_count:4},{...block,num:1,cited_by_count:0},{...block,num:3,cited_by_count:9},{...block,num:9,cited_by_count:4},{...block,num:4,cited_by_count:4},{...block,num:5,cited_by_count:4},block,{...block,type:'heading',num:6,cited_by_count:99}];
assert.deepEqual(mostCitedParagraphs(rows).map(b=>b.num),[3,2,4,5,9]);
const duplicateBlock={...block,num:'2',start:block.start+1,cited_by_count:99};
assert.deepEqual(mostCitedParagraphs([...rows,duplicateBlock]).map(b=>b.num),[3,2,4,5,9]);
assert.equal(mostCitedParagraphs([block,duplicateBlock])[0],block);
assert.deepEqual(mostCitedParagraphs([{...block,cited_by_count:0},duplicateBlock]),[]);
assert.deepEqual(mostCitedParagraphs([]),[]);
assert.deepEqual(mostCitedParagraphs([{...block,cited_by_count:-1}]),[]);
for(const count of [1.5,Infinity,NaN,'not a count'])assert.deepEqual(mostCitedParagraphs([{...block,cited_by_count:count}]),[]);
for(const num of [0,-1,1.5,'not a paragraph'])assert.deepEqual(mostCitedParagraphs([{...block,num}]),[]);
assert.ok(!formattedDecision(text,[],[],[block]).includes('id="reader-source-para-'));
assert.ok(formattedDecision(text,[],[],[block]).includes(`id="decision-source-${block.start}"`));
(async()=>{
await openDecision(7);
assert.equal(target.id,undefined);
assert.equal(nodes.readerMostCited.hidden,false);
assert.equal(nodes.readerMostCited.open,false);
assert.match(nodes.decisionBody.summaryHtml,/stored disposition/);
assert.ok(nodes.decisionBody.summaryHtml.includes(`href="#decision-source-${block.start}"`));
assert.match(nodes.readerMostCitedList.innerHTML,/4 other cases/);
assert.ok(nodes.readerMostCitedList.innerHTML.includes(`<a href="#decision-source-${block.start}" class="reader-evidence-toggle" data-reader-para-jump="2">Jump to paragraph 2</a>`));
assert.ok(!nodes.readerMostCitedList.innerHTML.includes('<button'));
assert.match(nodes.readerMostCitedList.innerHTML,/&lt;script&gt;&amp; &quot;quoted&quot; 😀 body/);
assert.ok(!nodes.readerMostCitedList.innerHTML.includes('<script>'));
assert.ok(!nodes.readerMostCitedList.innerHTML.includes('[2]'));
readerState.mode='chunks';readerState.formatted=false;
let prevented=false;
document.click({preventDefault(){prevented=true;assert.equal(readerState.mode,'chunks')},target:{closest(selector){assert.equal(selector,'#readerMostCited a[data-reader-para-jump]');return {dataset:{readerParaJump:'2'}}}}});
assert.equal(prevented,true);
document.click({preventDefault(){throw Error('Unrelated click prevented')},target:{closest(){return null}}});
assert.equal(readerState.mode,'normalized');assert.equal(readerState.formatted,true);
assert.equal(target.id,`decision-source-${block.start}`);assert.equal(target.tabindex,'-1');assert.equal(duplicate.id,undefined);
assert.equal(target.scrolled.block,'center');assert.equal(target.scrolled.behavior,'smooth');assert.equal(target.focused.preventScroll,true);
readerState.mode='chunks';readerState.formatted=false;
nodes.decisionBody.click({preventDefault(){},target:{closest(){return {dataset:{summarySource:String(block.start)}}}}});
assert.equal(readerState.mode,'normalized');assert.equal(readerState.formatted,true);
assert.equal(target.id,`decision-source-${block.start}`);assert.equal(target.focused.preventScroll,true);
assert.equal(nodes.readerMostCited.hidden,false);
reducedMotion=true;jumpToReaderParagraph(2);assert.equal(target.scrolled.behavior,'auto');
readerState.mode='normalized';readerState.formatted=false;jumpToReaderParagraph(2);
assert.equal(readerState.formatted,true);assert.equal(readerState.mode,'normalized');
const calls=modeCalls;jumpToReaderParagraph('999');assert.equal(modeCalls,calls);
nodes.readerMostCited.open=true;await openDecision(8);assert.equal(nodes.readerMostCited.open,false);
nodes.readerMostCited.open=true;fail=true;await openDecision(9);
assert.equal(nodes.readerMostCited.hidden,true);assert.equal(nodes.readerMostCitedList.innerHTML,'');
assert.equal(readerState.payload,null);
fail=false;await openDecision(10);closeDecisionReader();
assert.equal(closed,true);assert.equal(nodes.readerMostCited.hidden,true);assert.equal(nodes.readerMostCited.open,false);
assert.equal(nodes.readerMostCitedList.innerHTML,'');
readerState.payload={item:{full_text:text},readerData:{format_blocks:[]}};renderMostCitedParagraphs();
assert.equal(nodes.readerMostCited.hidden,true);
const longText='x'.repeat(219)+'😀tail';
readerState.payload={item:{full_text:longText},readerData:{format_blocks:[{...block,start:0,mark_end:0,end:224,cited_by_count:1}]}};
renderMostCitedParagraphs();assert.match(nodes.readerMostCitedList.innerHTML,/1 other case</);
assert.ok(nodes.readerMostCitedList.innerHTML.includes('x'.repeat(219)+'😀…'));
readerState.payload=payload;payload.readerData.format_blocks=[block,duplicateBlock];renderMostCitedParagraphs();
assert.equal((nodes.readerMostCitedList.innerHTML.match(/data-reader-para-jump="2"/g)||[]).length,1);
assert.match(nodes.readerMostCitedList.innerHTML,/4 other cases/);
nodes.readerMostCited.open=true;renderFailure=true;await actualOpenDecision(11);
assert.equal(readerState.payload,null);assert.equal(nodes.readerMostCited.hidden,true);
assert.equal(nodes.readerMostCited.open,false);assert.equal(nodes.readerMostCitedList.innerHTML,'');
})().catch(error=>{console.error(error);process.exitCode=1});
"""
    script = script.replace('FORMATTER', formatter).replace('CONTROLLER', summary_controller + '\n' + controller).replace('BASE_LOADER', loader)
    result = subprocess.run([node, '-'], input=script, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr


def test_extracted_reader_summary_omits_missing_fields_and_escapes_source_quote():
    node = shutil.which("node")
    if not node:
        pytest.skip("Node is required to execute the extracted reader summary")
    html = routes._data_explorer_page_html()
    helpers = "\n".join([
        html.split("const esc=", 1)[1].split("\n", 1)[0],
    ])
    helpers = "const esc=" + helpers
    helpers += "\n" + html[html.index("function sideFact("):].split("\n", 1)[0]
    helpers += "\n" + html[html.index("function extractedReaderSummaryHtml("):].split(
        "const extractedSummaryPreviousMode=", 1
    )[0]
    script = helpers + """
const assert=require('node:assert/strict');
assert.equal(extractedReaderSummaryHtml({}), '');
assert.equal(extractedReaderSummaryHtml(null), '');
const sparse=extractedReaderSummaryHtml({case:{court:'Federal Court'}});
assert.equal(sparse,'');
const quote='[42] The application is dismissed.\\n<script>alert("x")</script> & costs.';
const data={
  case:{court:'Federal Court',date:'2026-10-03'},
  format_blocks:[{type:'meta',start:0},{type:'para',num:42,start:100}],
  extracted_summary:[
    {key:'court',label:'Court',value:'Federal Court',evidence:'Federal Court',block_start:0,block_type:'meta',paragraph_number:null},
    {key:'judge',label:'Judge',value:'Justice "Smith"',evidence:'Justice "Smith"',block_start:0,block_type:'meta',paragraph_number:null},
    ...[['outcome','Outcome','dismissed'],['outcome_source','Outcome source','stored <rule>'],['disposition','Disposition',quote]].map(([key,label,value])=>({key,label,value,evidence:quote,block_start:100,block_type:'para',paragraph_number:42}))
  ],
  tags:[{category:'issue',value:'unverified tag',score:1}]
};
const rendered=extractedReaderSummaryHtml(data);
assert.ok(rendered.includes('dismissed'));
assert.ok(rendered.includes('stored &lt;rule&gt;'));
assert.ok(rendered.includes('Justice &quot;Smith&quot;'));
assert.ok(rendered.includes(esc(quote)));
assert.ok(!rendered.includes('<script>'));
assert.equal((rendered.match(/href="#decision-source-100"/g)||[]).length,3);
assert.equal((rendered.match(/href="#decision-source-0"/g)||[]).length,2);
assert.ok(rendered.includes('data-summary-source="100"'));
assert.ok(!rendered.includes('unverified tag'));
assert.ok(!rendered.includes('2026-10-03'));
delete data.format_blocks;
assert.equal(extractedReaderSummaryHtml(data),'');
data.extracted_summary=data.extracted_summary.filter(row=>!row.key.startsWith('outcome'));
data.format_blocks=[{type:'para',num:42,start:100}];
const noOutcome=extractedReaderSummaryHtml(data);
assert.ok(noOutcome.includes('Disposition'));
assert.ok(!noOutcome.includes('Outcome source'));
data.format_blocks=[{type:'para',num:42,start:200}];
assert.equal(extractedReaderSummaryHtml(data),''); // same number is not the same source block
console.log('Extracted summary rendering assertions passed');
"""
    result = subprocess.run([node, "-e", script], capture_output=True, text=True, timeout=20)
    assert result.returncode == 0, result.stderr
    assert "Extracted summary rendering assertions passed" in result.stdout


def test_extracted_reader_summary_mounts_in_active_reader_and_links_formatter_paragraphs():
    html = routes._data_explorer_page_html()
    assert "body.insertAdjacentHTML('afterbegin',extractedReaderSummaryHtml(readerState.payload.readerData))" in html
    assert 'const anchor=`id="decision-source-${b.start}"`' in html
    assert "const start=link.dataset.summarySource;readerState.formatted=true;setReaderMode('normalized')" in html
    assert "target.focus({preventScroll:true})" in html
    node = shutil.which("node")
    if not node:
        pytest.skip("Node is required to execute the active reader summary mount")
    mount = html[html.index("const extractedSummaryPreviousMode="):].split(
        "document.getElementById('decisionBody')?.addEventListener('click',event=>{", 1
    )[0]
    script = """
const assert=require('node:assert/strict');
const readerState={payload:{readerData:{marker:'stored reader data'}}};
let modeCalls=[],insertions=[],removed=0;
const paragraph={dataset:{para:'42'}};
const body={
  querySelectorAll:selector=>selector==='.reader-extracted-summary'?[{remove:()=>removed++}]:[paragraph],
  insertAdjacentHTML:(where,html)=>insertions.push([where,html])
};
const document={getElementById:id=>id==='decisionBody'?body:null};
let setReaderMode=mode=>modeCalls.push(mode);
const extractedReaderSummaryHtml=data=>{assert.equal(data.marker,'stored reader data');return '<section>quote</section>';};
""" + mount + """
setReaderMode('normalized');setReaderMode('chunks');setReaderMode('normalized');
assert.deepEqual(modeCalls,['normalized','chunks','normalized']);
assert.equal(removed,3);
assert.deepEqual(insertions,Array(3).fill(['afterbegin','<section>quote</section>']));
readerState.payload=null;
setReaderMode('normalized');
assert.equal(insertions.length,3);
"""
    result = subprocess.run([node, "-e", script], capture_output=True, text=True, timeout=20)
    assert result.returncode == 0, result.stderr


def test_extracted_summary_browser_source_links():
    """Optional local Chromium acceptance; no browser dependency for CI."""
    playwright = pytest.importorskip("playwright.sync_api")
    chromium = shutil.which("chromium")
    if not chromium:
        pytest.skip("Chromium is required for local browser acceptance")
    from datetime import date
    from backend.case_formatter import format_decision
    from backend.reader_service import _build_reader_extracted_summary
    from backend.models import CaseReaderMetadataFieldResponse

    text = ("Federal Court\nDate: 20250102\nJudge: Justice Smith\nDecision Content\n"
            "[1] Refugee evidence 😀.\n[2] The application is dismissed.")
    case = SimpleNamespace(full_text=text, court="Federal Court",
                           date=date(2025, 1, 2), metadata_json={})
    start = text.index("application is dismissed")
    outcome = SimpleNamespace(
        decision_outcome="dismissed", source="stored_rule",
        disposition_evidence="application is dismissed",
        evidence_offset_start=start, evidence_offset_end=start + len("application is dismissed"),
    )
    start = text.index("Refugee evidence")
    tag = SimpleNamespace(
        category="issue", value="refugee", score=1, source="stored_tag",
        evidence="Refugee evidence", offset_start=start, offset_end=start + len("Refugee evidence"),
    )
    judge = CaseReaderMetadataFieldResponse(
        key="judge", value="Justice Smith", source="reader_extracted", evidence="Justice Smith",
    )
    blocks = format_decision(text)

    def payload(stored_outcome):
        return {
            "format_blocks": blocks,
            "extracted_summary": [
                row.model_dump() for row in _build_reader_extracted_summary(
                    case, stored_outcome, blocks, [tag], [judge],
                )
            ],
        }

    html = routes._data_explorer_page_html()
    helpers = "const esc=" + html.split("const esc=", 1)[1].split("\n", 1)[0] + "\n"
    for name in ["highlightedDecision", "formattedDecision"]:
        helpers += html[html.index("function " + name + "("):].split("\n", 1)[0] + "\n"
    helpers += html[html.index("function extractedReaderSummaryHtml("):].split(
        "const extractedSummaryPreviousMode=", 1,
    )[0]
    hooks = html[html.index("const extractedSummaryPreviousMode="):].split("</script>", 1)[0]
    setup = (
        "const readerState={formatted:false,payload:{readerData:" + json.dumps(payload(outcome)) +
        "}};const storedText=" + json.dumps(text) + ";"
        "let setReaderMode=mode=>{document.getElementById('decisionBody').innerHTML="
        "mode==='chunks'?'<div>Chunks</div>':"
        "formattedDecision(storedText,[],[],readerState.payload.readerData.format_blocks);};"
    )
    with playwright.sync_playwright() as browser_driver:
        browser = browser_driver.chromium.launch(
            executable_path=chromium, headless=True, args=["--no-sandbox"],
        )
        page = browser.new_page()
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.set_content("<div id=decisionBody></div>")
        page.add_script_tag(content=helpers + setup + hooks)
        for size in [{"width": 1280, "height": 900}, {"width": 390, "height": 844}]:
            page.set_viewport_size(size)
            page.evaluate("setReaderMode('chunks')")
            assert page.locator(".reader-extracted-summary").count() == 1
            assert page.locator(".reader-extracted-summary a").count() == 7
            assert page.locator(".reader-extracted-summary").evaluate("node => node.open") is False  # closed until the reader opens it
            page.evaluate("extractedSummaryState.open = true")
            for index in range(7):
                page.evaluate("setReaderMode('chunks')")
                link = page.locator(".reader-extracted-summary a").nth(index)
                href = link.get_attribute("href")
                link.click()
                assert page.locator("#decisionBody " + href).count() == 1
                assert page.evaluate("document.activeElement.id") == href[1:]
            assert page.locator("blockquote").inner_text() == "[2] The application is dismissed."
        update = "data=>{readerState.payload.readerData=data;setReaderMode('normalized')}"
        for stored_outcome in [None, SimpleNamespace(**(vars(outcome) | {"evidence_offset_start": -1}))]:
            page.evaluate(update, payload(stored_outcome))
            assert page.locator(".reader-extracted-summary a").count() == 4
            assert "Outcome" not in page.locator(".reader-extracted-summary").inner_text()
        page.evaluate(update, {"case": {"court": "unverified"}, "format_blocks": [], "extracted_summary": []})
        assert page.locator(".reader-extracted-summary").count() == 0
        assert not errors
        browser.close()


class NavigationParser(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.controls = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if 'data-group' in attributes or 'data-nav-group' in attributes:
            self.controls.append((tag, attributes))


def test_primary_navigation_has_brand_left_and_groups_right():
    html = routes._data_explorer_page_html()
    header = html.split('<header class="topbar">', 1)[1].split('</header>', 1)[0]
    controls = NavigationParser(header).controls
    assert [attrs['data-group'] for _, attrs in controls] == ['info', 'research', 'intel', 'roadmap', 'soon', 'testing']
    assert all(tag == 'button' and attrs['aria-controls'] == 'researchViews' for tag, attrs in controls)
    assert [attrs['data-group'] for _, attrs in controls if attrs['aria-pressed'] == 'true'] == ['research']
    assert header.index('class="brand-home"') < header.index('primary-groups')
    assert 'href="/data-explorer?tab=about&amp;group=info"' in header
    assert 'siteExperimentalToggle' not in header and 'Show experimental' not in header
    assert header.count('<a ') == 3 and 'href="/welcome"' in header and '<a class="primary-link" href="/workbench">Workbench</a>' in header  # the brand home link, the Workbench page and the Welcome link
    assert '.topbar{justify-content:flex-start;flex-wrap:wrap;' in html
    assert '.group-views{flex-wrap:wrap;overflow:visible;' in html
    for label in ('About', 'Research', 'Intelligence / Statistics', 'Coming soon', 'Development', 'Testing'):
        assert f'>{label}</button>' in header


def test_secondary_navigation_groups_existing_views_and_functional_tools():
    controls = NavigationParser(routes._data_explorer_page_html()).controls
    views = {attrs['data-tab']: attrs['data-nav-group'] for _, attrs in controls if 'data-tab' in attrs}
    soon = {tab: group for tab, group in views.items() if tab.startswith('soon-')}
    assert set(soon.values()) == {'soon'}
    assert {'soon-themes', 'soon-tag-analytics', 'soon-citation-map'} <= set(soon)
    assert not ({'soon-live-analysis', 'soon-deidentify'} & set(soon))  # both live in the Workbench now
    assert {'soon-site-architecture', 'soon-statutes', 'soon-quick-search', 'soon-tag-finder'} <= set(soon)
    assert len(soon) == 13 and 'soon-business-case' not in soon
    assert 'soon-fc-analytics' not in soon
    roadmap = {tab: group for tab, group in views.items() if tab.startswith('roadmap-')}
    assert set(roadmap.values()) == {'roadmap'}
    assert list(roadmap) == ['roadmap-overview', 'roadmap-accuracy', 'roadmap-expansion', 'roadmap-intelligence', 'roadmap-fc-files', 'roadmap-team', 'roadmap-readiness', 'roadmap-internal', 'roadmap-local-ai']
    assert {tab: group for tab, group in views.items() if tab not in soon and tab not in roadmap} == {
        'about': 'info', 'about-how': 'info', 'about-changelog': 'info', 'search': 'research',
        'judge-profile': 'intel', 'citation-intelligence': 'intel', 'fc-analytics': 'intel',
        'research-bench': 'testing',
    }
    links = {attrs['href']: attrs['data-nav-group'] for tag, attrs in controls if tag == 'a'}
    assert links == {'/discussion-units-sandbox': 'testing', '/citation-pass': 'testing'}
    assert all('hidden' in attrs for _, attrs in controls if attrs.get('data-nav-group') in ('info', 'intel', 'soon', 'roadmap', 'testing'))


@pytest.mark.parametrize(('query', 'selected', 'group'), [
    ('', 'search', 'research'), ('?tab=info', 'about', 'info'),
    ('?tab=about', 'about', 'info'), ('?tab=site-architecture', 'site-architecture', 'direct'),
    ('?tab=citation-intelligence&case_id=7', 'citation-intelligence', 'intel'),
    ('?tab=judge-profile&judge=smith', 'judge-profile', 'intel'),
    ('?tab=fc-history&imm=IMM-12-26', 'fc-history', 'direct'), ('?tab=fc-analytics', 'fc-analytics', 'intel'),
    ('?tab=themes', 'themes', 'direct'), ('?tab=research-bench', 'research-bench', 'testing'),
    ('?tab=soon-citation-map', 'soon', 'soon'), ('?group=soon', 'themes', 'soon'), ('?group=roadmap', 'soon', 'roadmap'), ('?tab=roadmap-team', 'soon', 'roadmap'), ('?tab=soon-themes', 'themes', 'soon'), ('?group=intel', 'judge-profile', 'intel'),
    ('?group=workbench', 'search', 'research'), ('?group=testing', 'research-bench', 'testing'),
    ('?group=info', 'about', 'info'), ('?group=research', 'search', 'research'),
    ('?tab=search&case_id=7', 'search', 'research'),
    ('?tab=themes&group=info', 'themes', 'direct'),
    ('?tab=unknown', 'search', 'research'),
])
def test_navigation_controller_initializes_deep_links_and_restores_history(query, selected, group):
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is required to execute the navigation controller')
    html = routes._data_explorer_page_html()
    controls = [attrs for _, attrs in NavigationParser(html).controls]
    controller = html[html.index('const activeResearchPanels='):].split('</script>', 1)[0]
    controller = controller.split('const initialCaseId=', 1)[0]
    script = """
const assert=require('node:assert/strict');
const controls=CONTROLS.map(attrs=>({attrs,hidden:'hidden' in attrs,dataset:{group:attrs['data-group'],navGroup:attrs['data-nav-group'],tab:attrs['data-tab']},classList:{active:(attrs.class||'').includes('active'),toggle(key,value){this[key]=value}},setAttribute(key,value){this.attrs[key]=value}}));
const panels={};
const location=new URL('http://localhost/data-explorer'+QUERY);
const history={pushState(state,title,path){location.href=new URL(path,location).href}};
const window={addEventListener(name,handler){this[name]=handler}};
const document={getElementById(id){return panels[id]??=( {hidden:id!=='searchPanel',setAttribute(){},getAttribute(){return null}} )},querySelectorAll(selector){if(selector==='[data-group]')return controls.filter(item=>item.dataset.group);if(selector==='[data-nav-group]')return controls.filter(item=>item.dataset.navGroup);if(selector==='[data-tab]')return controls.filter(item=>item.dataset.tab);return []},addEventListener(){}};
function loadAbout(){} function loadCitationIntelligence(){} function loadJudgeProfiles(){} function loadThemes(){} function loadStatuteAffinity(){} function loadFcActivityTimeline(){} function loadFcActivityBreakdowns(){} function openDecision(){}
CONTROLLER
assert.equal(controls.find(item=>item.dataset.group&&item.attrs['aria-pressed']==='true')?.dataset.group,GROUP==='direct'?undefined:GROUP);
assert.deepEqual(controls.filter(item=>item.dataset.navGroup&&!item.hidden).map(item=>item.dataset.navGroup),controls.filter(item=>item.dataset.navGroup===GROUP).map(()=>GROUP));
assert.equal(panels[activeResearchPanels[SELECTED]].hidden,false);
const original=location.href;
activateResearchTab('workbench');
assert.equal(location.searchParams.get('group'),'direct');
assert.equal(location.searchParams.get('tab'),'workbench');
assert.equal(location.searchParams.has('case_id'),false);
assert.ok(Object.entries(activeResearchPanels).every(([key,id])=>panels[id].hidden===(key!=='workbench')));
location.href=original;window.popstate();
assert.equal(controls.find(item=>item.dataset.group&&item.classList.active)?.dataset.group,GROUP==='direct'?undefined:GROUP);
activateResearchTab('research-bench');
assert.equal(location.searchParams.get('group'),'testing');
assert.equal(panels.researchBenchPanel.hidden,false);
assert.equal(location.searchParams.get('judge'),new URL(original).searchParams.get('judge'));
assert.equal(location.searchParams.get('imm'),new URL(original).searchParams.get('imm'));
"""
    for marker, value in [('CONTROLS', json.dumps(controls)), ('QUERY', json.dumps(query)),
                          ('CONTROLLER', controller), ('SELECTED', json.dumps(selected)), ('GROUP', json.dumps(group))]:
        script = script.replace(marker, value)
    result = subprocess.run([node, '-'], input=script, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr


def test_fc_activity_panel_exposes_three_non_overlapping_charts():
    html = routes._data_explorer_page_html()

    assert 'id="fcActivityChart"' in html
    assert 'id="fcActivityRegistryChart"' in html
    assert 'id="fcActivityClassChart"' in html
    assert 'id="fcActivityTrackChart"' in html
    assert 'id="fcActivitySankey"' not in html
    assert 'id="fcActivityFlowSummary"' not in html


def test_research_bench_tab_exposes_three_prototype_views():
    html = routes._data_explorer_page_html()

    assert 'data-tab="research-bench"' in html
    assert 'id="researchBenchPanel" class="panel-card search-layout research-bench-panel"' in html
    assert 'data-bench-tab="library"' in html
    assert 'data-bench-tab="tracker"' in html
    assert 'data-bench-tab="analysis"' in html
    assert ".research-bench-panel" in html
    assert "LibraryService" in html
    assert "CaseTrackerService" in html
    assert "DocketAdapter" in html
    assert "AnalysisService" in html
    assert "activeResearchPanels" in html
    assert "activateResearchTab" in html
    assert "new URLSearchParams(location.search).get('tab')||'search'" in html


def test_site_architecture_panel_lists_data_layers_and_feature_map():
    html = routes._data_explorer_page_html()

    for label in (
        "Data inventory",
        "Case records",
        "Citation records",
        "Judge profiles",
        "Federal Court activity",
        "Feature-to-data map",
    ):
        assert label in html


def test_about_tab_contains_interactive_system_map_and_architecture_owns_overview():
    html = routes._data_explorer_page_html()
    about_start = html.index('<section id="aboutPanel"')
    about_end = html.index('<section id="searchPanel"', about_start)
    about_panel = html[about_start:about_end]
    architecture_start = html.index('<section id="siteArchitecturePanel"')
    architecture_end = html.index('<section id="citationIntelligencePanel"', architecture_start)
    architecture_panel = html[architecture_start:architecture_end]

    assert 'class="ilit-about"' in about_panel
    assert '<h1>iLit: immigration litigation intelligence</h1>' in about_panel
    for section in ('pipeline', 'library', 'derived', 'tabs', 'soon', 'progress', 'principles'):
        assert f'id="{section}"' in about_panel
    assert 'id="funding"' not in about_panel
    assert 'Data layer coverage' in architecture_panel
    assert 'id="aboutSummary"' in architecture_panel
    assert architecture_panel.index('Data layer coverage') < architecture_panel.index('Site Architecture')
    assert 'id="aboutSystemMap"' not in about_panel
    assert 'id="casePipelineGraphic"' not in about_panel
    assert 'id="movedAboutOverview"' in architecture_panel
    assert 'Citation records' in architecture_panel


def test_citation_intelligence_case_search_is_title_scoped():
    case = SimpleNamespace(
        id=12,
        title="Vavilov v. Canada (Citizenship and Immigration)",
        citation="2019 SCC 65",
        court="SCC",
        date="2019-12-19",
    )

    class Database:
        def scalars(self, statement):
            return iter([case])

    result = routes.citation_intelligence_cases("Vavilov", 12, Database())

    assert result == [
        {
            "case_id": 12,
            "title": case.title,
            "citation": case.citation,
            "court": case.court,
            "date": case.date,
        }
    ]


def test_rendered_shell_exposes_focused_feature_searches():
    html = routes._data_explorer_page_html()

    assert 'id="citationCaseQuery"' in html
    assert 'Find a case by title' in html
    assert 'id="judgeProfileQuery"' in html
    assert 'Find a judge by name' in html
    assert '<option value="newest" selected>Newest decision</option>' in html

    for subtab in ("Overview", "Timeline", "Neighborhood", "Outcomes", "Courts", "Judges", "Companions", "Statutes", "Evidence"):
        assert subtab in html

    assert "Research readout" in html
    assert "Open citation evidence" in html
    assert "Compare use over time" in html


def test_citation_intelligence_overview_exposes_case_fingerprint_pattern():
    html = routes._data_explorer_page_html()

    assert "Case fingerprint" in html
    assert "Where this authority is cited" in html
    assert "Shared-authority cluster" in html
    assert "ci-fingerprint-row" in html
    assert "ci-cluster-row" in html
    assert "/api/citation-intelligence/${ciState.caseId}/table?page=1&page_size=8" in html
    assert "/citation-map/cases/${ciState.caseId}/similar?limit=6&min_shared=2" in html


def test_citation_intelligence_is_a_case_workspace_with_visual_footprint():
    html = routes._data_explorer_page_html()

    panel_start = html.index('<section id="citationIntelligencePanel"')
    panel_end = html.index('<section id="judgeProfilePanel"', panel_start)
    panel = html[panel_start:panel_end]

    assert 'class="panel-card search-layout citation-workspace"' in panel
    assert 'Authority analysis workspace' in panel
    assert panel.index('citation-subtabs') < panel.index('citationSearchResults')
    assert 'ci-overview-visual' in html
    assert 'Citation footprint' in html
    assert 'Stored counts' in html
    assert 'top-decision concentration' in html
    assert "document.getElementById('citationSearchResults').innerHTML=''" in html


def test_citation_timeline_drills_into_year_filtered_evidence():
    html = routes._data_explorer_page_html()

    assert 'class="ci-timeline-year"' in html
    assert "loadCitationEvidenceForYear" in html
    assert "/api/citation-intelligence/${ciState.caseId}/table?page=${page}&page_size=25&year=" in html
    assert "Clear year filter" in html


def test_citation_overview_exposes_authority_signals():
    html = routes._data_explorer_page_html()

    assert "Distinctive cited authorities" in html
    assert "ci-authority-signals" in html
    assert "ci-signal-row" in html
    assert "/citation-map/cases/${ciState.caseId}/authority-signals?limit=4&context_limit=1" in html


def test_citation_neighborhood_exposes_direct_relationships():
    html = routes._data_explorer_page_html()

    assert "Direct citation neighborhood" in html
    assert "ci-neighborhood-row" in html
    assert "loadCitationNeighborhood" in html
    assert "/citation-map/cases/${ciState.caseId}/neighborhood?limit=20" in html


def test_citation_intelligence_overview_has_stable_context_and_result_states():
    html = routes._data_explorer_page_html()

    assert "Selected authority" in html
    assert "Research paths" in html
    assert "Stored citation evidence is shown separately from derived research signals." in html
    assert 'data-ci-action="timeline"' in html
    assert 'data-ci-action="neighborhood"' in html
    assert 'data-ci-action="table"' in html
    assert "data-ci-state=\"${state}\"" in html
    assert "Promise.allSettled" in html
    assert "Citation Intelligence unavailable:" in html
    assert "data-ci-retry" in html
    assert "originalLoadCitationIntelligence" in html


def test_case_search_has_clear_primary_query_and_filter_state():
    html = routes._data_explorer_page_html()

    assert 'class="sp-title"' in html
    assert 'class="search-query-row"' in html
    assert 'role="combobox"' in html
    assert 'id="searchSuggestions"' in html
    assert 'aria-live="polite"' in html
    assert 'id="searchFilterSummary"' in html
    assert 'id="recentCases"' in html
    assert 'id="toggleAdvancedSearch"' in html
    assert 'function updateSearchFilterSummary()' in html
    assert 'function requestSearchSuggestions(query)' in html
    assert "limit:'5'" in html
    assert "sort_by:'relevance'" in html
    assert 'function professionalResultCard(item)' in html


def test_case_search_can_save_current_query_and_filters():
    html = routes._data_explorer_page_html()

    assert 'id="saveCurrentSearch"' in html
    assert 'href="/saved-searches-ui"' in html
    assert "filters})" in html
    assert "search_mode:'metadata'" in html
    assert "async function saveCurrentSearch()" in html


def test_chunk_reader_uses_compact_sections_and_inherited_reference_type():
    html = routes._data_explorer_page_html()

    assert '.chunk-header{display:none}' in html
    assert '.chunk-panel{margin:0;border:0;border-top:1px solid' in html
    assert '.chunk-body{padding:7px 3px' in html
    assert '.chunk-citation{display:inline' in html


def test_main_search_and_reader_expose_core_case_and_assessment_controls():
    html = routes._data_explorer_page_html()

    assert "Display core cases" in html
    assert "readerAssessmentToggle" in html
    assert "discussion_units_core_300" in html
    assert "/cases/${readerState.caseId}/paragraph-assessments" in html
    assert ".paragraph-assessment{display:grid" in html
    assert ".paragraph-assessment p{grid-column:2" in html
    assert ".paragraph-assessment{grid-template-columns:1fr" in html
    assert '.chunk-statute{display:inline' in html
    assert 'font-family:inherit;font-size:inherit;line-height:inherit' in html


def test_reader_legal_development_banner_and_similar_paragraph_buttons_are_off():
    html = routes._data_explorer_page_html()

    # Daniel, 2026-10-05: the yellow legal-development indicator and the per-paragraph
    # "Similar paragraphs" button are off everywhere; the APIs stay for later.
    assert "/api/overruling-risk/${encodeURIComponent(caseId)}" not in html
    assert "dataset.paragraphSimilar" not in html


def test_reader_overruling_risk_banner_renders_only_returned_flags():
    node = shutil.which("node")
    if not node:
        pytest.skip("Node is required to execute the reader warning")
    controller = Path("backend/pages/overruling_risk_reader.js").read_text(encoding="utf-8")
    script = r"""
const assert=require('node:assert/strict');
const banner={hidden:true,children:[],replaceChildren(){this.children=[]},append(...nodes){this.children.push(...nodes)}};
const document={
  getElementById(id){assert.equal(id,'readerOverrulingRisk');return banner},
  createElement(tag){return {tag,textContent:'',children:[],append(...nodes){this.children.push(...nodes)}}},
  createTextNode(text){return {tag:'text',textContent:String(text),children:[]}}
};
global.window={ILIT_SHOW_LEGAL_NOTICE:true};
const readerState={caseId:null,payload:null};
let payload={flags:[{
  assignment:'indirect',event:'Framework update',event_date:'2019-12-19',
  decision_date:'2018-04-03',rationale:'<img src=x onerror=alert(1)>',
  source:'Primary source',how_assigned:'Stored resolved citation relationship',
  notice:'seed list, needs lawyer review.'
}],assessment:'This case may be affected by the listed development.'};
let openDecision=async id=>{readerState.caseId=Number(id);readerState.payload={}};
let closeDecisionReader=()=>{readerState.payload=null};
const fetch=async url=>{assert.equal(url,'/api/overruling-risk/7');return {ok:true,json:async()=>payload}};
const controller = __CONTROLLER__;
function text(node){return String(node.textContent||'')+(node.children||[]).map(text).join('')}
(async()=>{
  await openDecision(7);
  await new Promise(resolve=>setTimeout(resolve,0));
  assert.equal(banner.hidden,false);
  const rendered=text(banner);
  assert.match(rendered,/this case may be affected/);
  assert.match(rendered,/How assigned/);
  assert.match(rendered,/seed list, needs lawyer review\./);
  assert.match(rendered,/<img src=x onerror=alert\(1\)>/);
  assert.equal(banner.innerHTML,undefined);
  payload={flags:[],assessment:'No seeded indicator matched.'};
  await openDecision(7);
  await new Promise(resolve=>setTimeout(resolve,0));
  assert.equal(banner.hidden,true);
  payload={flags:[{
    assignment:'direct',event:'Framework update',event_date:'2019-12-19',
    decision_date:'2019-12-19',rationale:'Listed development authority',
    source:'Primary source',how_assigned:'Direct seed match',
    notice:'seed list, needs lawyer review.'
  }],assessment:'This case is itself a listed development authority; other cases may be affected by this development.'};
  await openDecision(7);
  await new Promise(resolve=>setTimeout(resolve,0));
  assert.match(text(banner),/This case is itself a listed legal-development authority/);
  assert.match(text(banner),/other cases may be affected/);
  await openDecision(7);
  closeDecisionReader();
  assert.equal(banner.hidden,true);
})().catch(error=>{console.error(error);process.exitCode=1});
"""
    script = script.replace("__CONTROLLER__", controller)
    result = subprocess.run([node, "-"], input=script, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr


def test_judge_profiles_default_to_most_linked_profiles():
    class FakeProfile:
        def __init__(self, slug, display_name, case_link_count):
            self.id = hash(slug)
            self.slug = slug
            self.display_name = display_name
            self.primary_court = "Federal Court"
            self.aliases = []
            self.case_links = list(range(case_link_count))

    class Database:
        def execute(self, statement):
            return iter([])  # no alias rows

        def scalars(self, statement):
            return iter([
                FakeProfile("judge-b", "Judge B", 2),
                FakeProfile("judge-a", "Judge A", 7),
                FakeProfile("judge-c", "Judge C", 4),
            ])

    result = routes.judge_profiles("", 10, Database())

    assert [item["slug"] for item in result] == ["judge-a", "judge-c", "judge-b"]


def test_judge_issue_outcomes_are_lazy_loaded_and_disclose_safe_denominators():
    html = routes._data_explorer_page_html()

    assert "Outcome patterns by issue" in html
    assert (
        "Outcome method: government outcome “won” = Minister win, “lost” = applicant win, "
        "“mixed” = other; undetermined, unrecognized, and missing values are unclassified, "
        "and percentages use all issue decisions, including unclassified."
    ) in html
    assert "At least " in html
    assert "${N(hidden)} issue${hidden===1?'':'s'} hidden (each has fewer than ${minimum} decisions)." in html
    assert "including unclassified" in html
    assert "undetermined, unrecognized, and missing values are unclassified" in html
    assert "Federal Court issue outcomes" in html
    assert "data-jp-issues" in html
    assert "/api/judge-profiles/${encodeURIComponent(slug)}/issues" in html
    profile_loader = html.split("async function jpSelect", 1)[1].split("function tally", 1)[0]
    assert "/issues" not in profile_loader
    issue_loader = html.split("async function jpLoadIssues", 1)[1].split("function jpMainClick", 1)[0]
    assert "getJSON(`/api/judge-profiles/${encodeURIComponent(slug)}/issues`)" in issue_loader
    click_handler = html.split("function jpMainClick", 1)[1].split("/* ---------------- Citation intelligence", 1)[0]
    assert "closest('[data-jp-issues]')" in click_handler
    assert "jpLoadIssues()" in click_handler
    assert "jpIssueCategories" in html


def test_rendered_shell_exposes_original_source_link_action():
    html = routes._data_explorer_page_html()

    assert 'Original source' in html


def test_rendered_shell_exposes_docket_to_fc_history_action():
    html = routes._data_explorer_page_html()

    assert 'Open FC History' in html
    assert 'data-fc-docket' in html
    assert 'fcHistoryForm' in html


def test_fc_history_tab_uses_full_entry_list_and_distinct_panel_mapping():
    html = routes._data_explorer_page_html()

    assert "'fc-history':'fcHistoryPanel'" in html
    assert 'const entries=(data.entries_json||[])' in html
    assert 'const entries=(data.entries_json||[]).map' in html
    assert 'slice(0,8)' not in html.split('const entries=', 1)[1].split('results.innerHTML', 1)[0]


def test_rendered_shell_exposes_case_reader_tag_tabs():
    html = routes._data_explorer_page_html()

    assert 'Case information' in html
    assert 'Header metadata' in html
    assert 'Extracted metadata' in html
    assert 'Case information' in html
    assert 'Tags' in html
    assert "['info','Info']" in html
    assert "['advanced','Advanced']" in html
    assert "row('Case name'" in html
    assert "row('Minister / government party'" in html
    assert 'tag-highlight' in html
    assert 'chunk-statute' in html
    assert 'chunk-citation' in html
    assert 'groupedTagHtml' in html
    assert 'unique tag' in html
    assert 'reader-tag-occurrence' in html
    assert 'groupedStatuteHtml' in html
    assert 'reader-statute-source' in html
    assert 'reader-statute-section' in html
    assert 'reader-statute-occurrence' in html
    assert 'fullTextTags' in html
    assert '.reader-statute-source,.reader-statute-section' in html
    assert '.reader-statute-occurrence{padding:8px 0;border-top:1px solid var(--border)' in html


def test_rendered_shell_exposes_evidence_details_control():
    html = routes._data_explorer_page_html()

    assert 'id="readerEvidenceToggle"' in html
    assert 'Show evidence details' in html
    assert 'readerEvidenceDetail' in html
    assert 'Hide evidence details' in html


def test_rendered_shell_exposes_independent_case_summary_control():
    html = routes._data_explorer_page_html()

    assert 'id="readerSummaryToggle"' in html
    assert 'Show case structure' in html
    assert 'id="readerCaseSummaryToggle"' in html
    assert 'Show case summary' in html
    assert 'id="readerCaseSummaryDetail"' in html
    assert 'renderCaseSummary' in html


def test_fc_activity_panel_exposes_procedural_insights():
    html = routes._data_explorer_page_html()

    for element_id in ("fcInsights", "fcInsightsKpis", "fcInsightsDurations", "fcInsightsBreakdowns", "fcJudgeTable", "fcCaseForm"):
        assert f'id="{element_id}"' in html
    assert "/api/fc-activity/insights" in html
    assert "/api/fc-activity/judges" in html
    assert "/api/fc-activity/case" in html


def test_fc_analytics_tab_is_wired_into_research_navigation():
    html = routes._data_explorer_page_html()

    assert 'data-tab="fc-analytics" aria-pressed="false" aria-controls="fcAnalyticsPanel" hidden>Federal Court Analytics' in html
    assert '>FC Activity</button>' not in html
    assert 'id="fcAnalyticsPanel"' in html
    assert "'fc-analytics':'fcAnalyticsPanel'" in html
    assert "window.fcxLoadDashboard" in html
    assert "/api/fc-activity/dashboard" in html
    for chart in ("fcxKpis", "fcxFunnel", "fcxRates", "fcxOutcomes", "fcxMotions", "fcxJudges", "fcxCompliance"):
        assert f'id="{chart}"' in html


def test_panel_helper_is_included_once_before_all_callers():
    html = routes._data_explorer_page_html()
    assert html.count("const fetchPanel =") == 1
    assert html.index("const fetchPanel =") < html.index("function fetchCurrentPanel")
    assert html.index("const fetchPanel =") < html.index("window.fcxLoadDashboard")
    assert "window.fetch=" not in html
    assert "panelSelections.get(container)===selection" in html
    assert "container.isConnected" in html


@pytest.mark.parametrize(
    "function,endpoint,success",
    [
        ("runProfessionalSearch", "/analytics/search/cases?", "professionalResultCard"),
        ("loadSearch", "/analytics/search/cases?", "resultCard"),
        ("loadPersistedReaderStatutes", "/statute-references", "setReaderMode"),
        ("loadReaderActs", "/statute-references", "render(rows)"),
        ("loadJudgeProfiles", "/api/judge-profiles?limit=100", ".judge-profile-result"),
        ("loadJudgeProfile", "/api/judge-profiles/${encodeURIComponent(slug)}", "syncJudgeMinisterCheckboxes()"),
        ("searchJudgeProfiles", "/api/judge-profiles?q=", ".judge-profile-result"),
        ("loadFcHistory", "/api/fc-history?", "data.entries_json"),
        ("loadFcActivityTimeline", "/api/fc-activity/timeline", "renderFcActivityTimeline(data)"),
        ("loadFcAnalytics", "/api/fc-activity/analytics?", "renderFcAnalytics(data)"),
        ("loadFcActivityFlow", "/api/fc-activity/flow", "renderFcActivitySankey(data)"),
        ("loadFcActivityBreakdowns", "/api/fc-activity/breakdowns", "data.registry_locations"),
        ("loadFcMotions", "/api/fc-activity/motions?", "renderFcMotions()"),
        ("loadFcCounsel", "/api/fc-activity/counsel?", "renderFcCounsel()"),
        ("loadFcInsights", "/api/fc-activity/insights?", "renderFcBodies()"),
        ("loadFcJudges", "/api/fc-activity/judges?", "renderFcJudges()"),
        ("lookupFcCase", "/api/fc-activity/case?", "fcCaseRows(data)"),
        ("showSimilarParagraphs", "/paragraphs/${n}/similar?", "row.why_matched"),
    ],
)
def test_adopted_panel_success_and_events_are_inside_retry_renderer(function, endpoint, success):
    html = routes._data_explorer_page_html()
    start = re.search(rf"(?:async )?function {function}\(", html).start()
    # Each owner ends before the next named function or script boundary.
    tail = html[start:]
    end = re.search(r"\n(?:async )?function |\n</script>", tail[1:])
    body = tail[:end.start() + 1] if end else tail
    assert "fetchCurrentPanel(" in body
    assert endpoint in body
    assert "render" in body
    assert body.index("render") < body.index(success)
    assert "catch(error)" not in body
    assert "error.message" not in body


def test_reader_sidepanel_owners_preserve_local_renderers_and_stale_guards():
    html = routes._data_explorer_page_html()
    for endpoint, tab in [
        ("/cases/${caseId}/activity", "activity"),
        ("/analytics/cases/${caseId}/thematic-cluster", "cluster"),
        ("/search/tags/similar?case_id=", "similar"),
    ]:
        line = next(line for line in html.splitlines() if f"fetchCurrentPanel(`{endpoint}" in line)
        assert f"readerPanelCurrent(caseId,'{tab}',content)" in line
        assert "render:" in line
        assert ".catch(" not in line
    intelligence = html[html.index("async function loadCaseIntelligence"):html.index("function renderCaseReaderPane", html.index("async function loadCaseIntelligence"))]
    for endpoint in ("authority-signals?", "similar?", "missing-authorities?", "completion-suggestions?"):
        assert endpoint in intelligence
    assert "Promise.allSettled" in intelligence
    assert "panel.innerHTML=intelligenceRows(rows,row)" in intelligence
    assert "readerPanelCurrent(caseId,'intelligence',box)" in intelligence
    assert "no second bubbling Acts request" in html
    assert "await readerStatutePending" in html
    assert "const loadedJudgeProfile=" not in html
    assert "Showing all ${num(data.decisions.length)} linked decisions." in html
    assert html.count("fetchCurrentPanel(`/api/judge-profiles/${encodeURIComponent(slug)}") == 1
    linked = html[html.index("openLinkedCase=async function"):html.index("function sideShowPara")]
    assert "fetchCurrentPanel(" in linked
    assert "sideState.linkedId===caseId" in linked


def test_fc_dashboard_owners_do_not_render_independent_siblings():
    from backend.pages.fc_analytics import FC_ANALYTICS_JS

    script = FC_ANALYTICS_JS
    assert "Promise.allSettled" in script
    assert "renderAll" not in script
    assert script.count("fetchCurrentPanel(`/api/fc-activity/dashboard?") == 1
    assert "filter(key=>key!=='judges').forEach(renderView)" in script
    for endpoint, container, renderer in [
        ("dashboard", "fcxKpis", "renderDashboard()"),
        ("judges", "fcxJudges", "renderView('judges')"),
        ("counsel", "fcxCounsel", "renderCounsel()"),
    ]:
        line = next(line for line in script.splitlines() if f"fetchCurrentPanel(`/api/fc-activity/{endpoint}?" in line)
        assert f"$('{container}')" in line
        assert "render:" in line
        assert line.index("render:") < line.index(renderer)


def test_panel_helpers_node_behavior():
    node = shutil.which("node")
    if not node:
        pytest.skip("Node.js is not available")
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [node, str(root / "tests/test_panel_helpers.js")],
        cwd=root, capture_output=True, text=True, timeout=90, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_panel_fixture_browser_when_chromium_available():
    node = shutil.which("node")
    if not node or not shutil.which("chromium"):
        pytest.skip("Node.js and Chromium are required for fixture browser acceptance")
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [node, str(root / "tests/test_panel_browser.js")],
        cwd=root, capture_output=True, text=True, timeout=90, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_workbench_group_has_a_landing_panel_linking_its_tools():
    html = routes._data_explorer_page_html()

    assert 'id="workbenchPanel"' in html
    assert "workbench:'workbenchPanel'" in html
    for href in ("/citation-map", "/deidentify"):
        assert f'class="workbench-card" href="{href}"' in html
    # Live Analysis is paused (coming soon): shown, but not a link.
    assert 'class="workbench-card tab-coming-soon" aria-disabled="true"><strong>Live Analysis' in html
    assert 'href="/live-analysis"' not in html


def test_reader_splitters_and_search_results_have_valid_aria():
    html = routes._data_explorer_page_html()

    for name in ("target", "linked"):
        assert f'data-reader-splitter="{name}" role="separator" aria-valuemin="220" aria-valuemax="520" aria-valuenow="300"' in html
    assert 'id="searchResults" role="region" aria-label="Case search results"' in html


def test_unfinished_site_areas_are_hidden_until_show_experimental_is_on():
    html = routes._data_explorer_page_html()

    hide_rule = 'body:not(.reader-experimental) :is([data-group="testing"],#displayCoreCases,#cohortSearchPanel){display:none!important}'
    assert hide_rule in html
    assert 'id="siteExperimentalToggle"' not in html
    assert "#readerExperimentalToggle,#siteExperimentalToggle" in html


def test_plain_search_echo_uses_plain_words():
    html = routes._data_explorer_page_html()
    assert "in the name or citation." in html
    assert "Search interpreted as: ${data.query_echo}" in html


def test_reader_overruling_risk_notice_is_off_unless_a_page_opts_in():
    node = shutil.which("node")
    if not node:
        pytest.skip("Node is required to execute the reader warning")
    controller = Path("backend/pages/overruling_risk_reader.js").read_text(encoding="utf-8")
    script = r"""
const assert=require('node:assert/strict');
const banner={hidden:true,children:[],replaceChildren(){this.children=[]},append(){}};
const document={getElementById(){return banner}};
let fetched=0;const fetch=async()=>{fetched++;return {ok:true,json:async()=>({flags:[{}]})}};
const readerState={caseId:null,payload:null};
let openDecision=async id=>{readerState.caseId=Number(id);readerState.payload={}};
let closeDecisionReader=()=>{};
const original=openDecision;
const controller = __CONTROLLER__;
(async()=>{await openDecision(7);await new Promise(r=>setTimeout(r,0));assert.equal(fetched,0);assert.equal(openDecision,original);assert.equal(banner.hidden,true)})().catch(e=>{console.error(e);process.exitCode=1});
""".replace("__CONTROLLER__", controller)
    result = subprocess.run([node, "-"], input=script, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr


def test_coming_soon_items_load_their_real_page_under_the_banner():
    from backend.pages.pitch_nav import COMING_SOON, SOON_TARGETS

    html = routes._data_explorer_page_html()
    assert 'id="comingSoonBanner"' in html and 'id="comingSoonFrame"' in html
    framed = {key: target for key, (kind, target) in SOON_TARGETS.items() if kind == 'page'}
    assert 'business-case' not in framed
    assert framed['citation-map'] == '/citation-map' and framed['statutes'] == '/statute-library'
    assert {key for key, _, _ in COMING_SOON} - set(SOON_TARGETS) == {'markup'}
    assert all(path in {r.path for r in routes.router.routes} for path in framed.values())


def test_main_tab_clicks_reset_state_in_page_without_reloading():
    html = routes._data_explorer_page_html()
    assert "function pitchResetState()" in html and "function pitchCleanOpen(group)" in html
    assert "location.assign('/data-explorer" not in html
    assert "{info:'about',research:'search',intel:'judge-profile',roadmap:'roadmap-overview',soon:'soon-themes',testing:'research-bench'}" in html
    for step in ("closeDecisionReader()", "getElementById('clearSearch')?.click()", "ciState.caseId=null", "document.getElementById('fcxClear')?.click()"):
        assert step in html


def test_coming_soon_roadmap_pages_serve_overview_and_every_section():
    from fastapi import HTTPException

    from backend.pages.coming_soon_page import ORDER, SECTIONS, STATUSES

    for slug in ORDER:
        page = routes.coming_soon_page(slug)
        assert page.status_code == 200 and b"Coming soon" in page.body
    with pytest.raises(HTTPException):
        routes.coming_soon_page("nope")
    assert all(item[2] in STATUSES and len(item) in (7, 8) for area in SECTIONS.values() for item in area['items'])
    assert b"Internal documentation" in routes.coming_soon_page("overview").body
    assert "/coming-soon/overview" in routes._data_explorer_page_html()
