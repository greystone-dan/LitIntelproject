"""Generated-page contracts and executable offline tour/browser regressions."""

import ast
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time
from urllib.parse import parse_qs, urlsplit

import pytest

os.environ["PYTHON_DOTENV_DISABLED"] = "1"

from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.start import TASKS, start_page_html
from backend.pages.memo_citation_check import memo_citation_check_page_html
from backend.pages.citation_map import citation_map_html
from backend.pages.live_analysis import live_analysis_page_html


ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.links.append(dict(attrs).get("href"))


class Scripts(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.scripts = []
        self.current = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.current = []

    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.current is not None:
            self.scripts.append("".join(self.current))
            self.current = None


def test_onboarding_start_cards_routes_examples_and_shared_help():
    assert [task[0] for task in TASKS] == [
        "Find a case", "See how the Federal Court ruled on an issue",
        "Check a memo's citations", "Look at a judge's record", "Export results",
    ]
    html = start_page_html()
    assert html.count('<article class="task-card">') == 5
    route_tree = ast.parse((ROOT / "backend/routes.py").read_text())
    routes = {
        decorator.args[0].value
        for function in ast.walk(route_tree) if isinstance(function, ast.FunctionDef)
        for decorator in function.decorator_list
        if isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Attribute)
        and decorator.func.attr == "get" and decorator.args
        and isinstance(decorator.args[0], ast.Constant)
    }
    for link in Links(html).links:
        assert urlsplit(link).path in routes
    for _, _, route, example, _ in TASKS:
        assert urlsplit(route).path == urlsplit(example).path
        assert parse_qs(urlsplit(example).query)
        assert "case_id" not in parse_qs(urlsplit(example).query)
    for builder in (data_explorer_page_html, memo_citation_check_page_html, citation_map_html, live_analysis_page_html):
        assert 'href="/start" aria-label="Help: start a research task"' in builder()
    assert 'query=procedural%20fairness&court=FC&search_full_text=true' in html.replace("&amp;", "&")
    assert "judge_query=Zinn" in html
    assert "example=vavilov" in html


def test_onboarding_tour_generated_contract_and_wrapper_order():
    assert Scripts("<SCRIPT>const example = 1;</SCRIPT >").scripts == ["const example = 1;"]
    html = data_explorer_page_html()
    assert html.index("const mostCitedOpenDecision") < html.index("const seenThisSession")
    assert html.index("Citation Intelligence and Judge Profile snapshot views") < html.index("const seenThisSession")
    for marker in ("dialog.showModal()", "aria-labelledby", "aria-describedby",
                   "previousFocus", "dialog.contains(document.activeElement)",
                   "event.shiftKey", "event.key === 'Escape'",
                   "localStorage.getItem", "localStorage.setItem", "seenThisSession.add",
                   "searchTourButton", "readerTourButton"):
        assert marker in html
    assert "if(!current())return;" in html
    assert "readerLoadGeneration++" in html
    assert "params.get('query')" in html
    assert "['FC', 'FCA', 'SCC'].includes(court)" in html
    assert "fullText === 'true'" in html
    assert "params.get('judge_query')" in html
    assert "Read the available decision text in full" in html
    assert "Source offsets remain owned by the backend" not in html
    for script in Scripts(html).scripts:
        node = shutil.which("node")
        if node:
            result = subprocess.run([node, "--check"], input=script, text=True, capture_output=True)
            assert result.returncode == 0, result.stderr


def test_onboarding_preserves_operator_search_and_lazy_judge_issue_controls():
    """Both entry paths share the existing controls, not alternate renderers."""
    html = data_explorer_page_html()
    for marker in (
        'id="searchTipsToggle"', 'id="searchTipsPopover"', 'id="searchQueryEcho"',
        "queryEcho.textContent=", "data.query_echo", "runProfessionalSearch()",
        "const query = params.get('query')", "query.slice(0, 500)",
        "entryParams.get('judge_query')", "$('jpSearch').value=jp.q",
        "issueData:null", "issueRequest:0", "jp.issueRequest!==request",
        "Load issue outcomes", "searchTourButton", "readerTourButton",
    ):
        assert marker in html
    assert html.index("const researchEntryParams=") < html.index("const entryParams=")
    assert html.index("const entryParams=") < html.index("const seenThisSession")
    assert "<<<<<<<" not in html
    assert ">>>>>>>" not in html


def run_node(script, data=None):
    node = shutil.which("node")
    if not node:
        pytest.skip("Node required for executable browser controls")
    result = subprocess.run(
        [node, "-e", script], input=json.dumps(data or {}), text=True,
        capture_output=True, timeout=90,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return result.stdout


def test_onboarding_executable_storage_focus_prefill_and_reader_lifecycle():
    run_node(r"""
const assert=require('node:assert/strict'),vm=require('node:vm');
const js=JSON.parse(require('node:fs').readFileSync(0,'utf8')).js;
async function scenario(readThrows,writeThrows,stored=false){
 const nodes={},writes=[],classes=new Set();
 let active=null;
 function element(id){
  return nodes[id] ||= {id,hidden:false,open:false,value:'',checked:false,disabled:false,isConnected:true,dataset:{},
   classList:{add(x){classes.add(id+x)},remove(x){classes.delete(id+x)},toggle(){}},
   getClientRects(){return this.hidden?[]:[{}]},closest(){return this.hidden?this:null},
   scrollIntoView(){},focus(){active=this},setAttribute(k,v){this[k]=v},append(){},
   addEventListener(k,f){this[k]=f},showModal(){this.open=true},close(){this.open=false},
   contains(e){return ['tourBack','tourNext','tourDismiss'].includes(e?.id)},
   querySelectorAll(){return ['tourBack','tourNext','tourDismiss'].map(element)}};
 }
 const document={get activeElement(){return active},body:{append(){}},
  createElement(tag){return element(tag==='dialog'?'researchTour':`button${Object.keys(nodes).length}`)},
  querySelector(selector){return element(selector==='#caseSearch .search-actions'?'actions':selector==='#caseReaderPanel .reader-toolbar'?'toolbar':selector.replace(/^#/,''))},
  getElementById:element,querySelectorAll(){return []}};
 element('caseReaderPanel').hidden=true;element('searchQuery').focus();
 const readerState={caseId:null,payload:null};
 const context={document,readerState,URLSearchParams,initialCaseId:0,researchEntryParams:new URLSearchParams('?query=%3Cscript%3E&court=FC&search_full_text=true&judge=forbidden'),location:{search:''},
  localStorage:{getItem(){if(readThrows)throw Error('blocked read');return stored?'done':null},setItem(k,v){if(writeThrows)throw Error('blocked write');writes.push(k)}},
  queueMicrotask,qfSync(){},updateSearchFilterSummary(){},setReaderMode(){},activateResearchTab(tab){element('caseReaderPanel').hidden=true;element('searchPanel').hidden=tab!=='search'},
  closeDecisionReader(){element('caseReaderPanel').hidden=true;element('searchPanel').hidden=false;readerState.payload=null;element('searchQuery').focus()},
  openDecision:async(id)=>{element('searchPanel').hidden=true;element('caseReaderPanel').hidden=false;readerState.caseId=id;readerState.payload={readerData:{}}}};
 vm.createContext(context);vm.runInContext(js,context);
 const dialog=element('researchTour');
 assert.equal(element('searchQuery').value,'<script>');assert.equal(element('courtFilter').value,'FC');assert.equal(element('searchFullText').checked,true);
 assert.equal(element('advancedSearchOptions').hidden,false);
 if(!stored){
  assert.equal(dialog.open,true);assert.equal(active.id,'tourNext');assert.equal(element('tourBack').disabled,true);
  active=element('tourDismiss');let prevented=false;
  dialog.keydown({key:'Tab',shiftKey:false,preventDefault(){prevented=true}});
  assert.equal(prevented,true);assert.equal(active.id,'tourNext');
  dialog.keydown({key:'Tab',shiftKey:true,preventDefault(){}});
  assert.equal(active.id,'tourDismiss');
  element('tourNext').onclick();assert.equal(element('tourBack').disabled,false);
  for(let i=0;i<2;i++)element('tourNext').onclick();
  assert.equal(element('tourNext').textContent,'Finish tour');element('tourNext').onclick();
  assert.equal(dialog.open,false);assert.equal(active.id,'searchQuery');assert.equal(classes.size,0);
 }
 await context.openDecision(4);assert.equal(dialog.open,!stored);
 if(!stored){dialog.cancel({preventDefault(){}});assert.equal(dialog.open,false)}
 context.closeDecisionReader();assert.equal(dialog.open,false); // per-session fallback
 if(!writeThrows&&!stored)assert.equal(writes.length,2);
 // Manual re-open works even when storage remembered/throws.
 const searchButton=Object.values(nodes).find(node=>node.id==='searchTourButton');
 assert.ok(searchButton);searchButton.focus();searchButton.onclick();assert.equal(dialog.open,true);
 dialog.keydown({key:'Escape',preventDefault(){}});assert.equal(dialog.open,false);assert.equal(active,searchButton);
 searchButton.onclick();context.activateResearchTab('themes');await Promise.resolve();assert.equal(dialog.open,false);
 // Failed or hidden reader is never offered a reader tour.
 readerState.payload=null;element('caseReaderPanel').hidden=false;
 context.setReaderMode('normalized');assert.equal(dialog.open,false);
}
(async()=>{await scenario(true,true);await scenario(true,false);await scenario(false,true);await scenario(false,false,true);console.log('four storage/focus/lifecycle scenarios passed')})().catch(e=>{console.error(e);process.exit(1)});
""", {"js": (ROOT / "backend/pages/explorer_tours.js").read_text()})


def test_onboarding_sample_pdf_is_valid_and_not_automatically_uploaded():
    html = memo_citation_check_page_html()
    function = re.search(r"function sampleMemoPdf\(\)\{.*?\n\}", html, re.S).group(0)
    output = run_node(function + """
const file=sampleMemoPdf();
file.arrayBuffer().then(buffer=>console.log(Buffer.from(buffer).toString('base64')));
""")
    import base64
    from io import BytesIO
    from pypdf import PdfReader
    reader = PdfReader(BytesIO(base64.b64decode(output.strip())))
    assert "2019 SCC 65" in reader.pages[0].extract_text()
    assert "Synthetic sample - not a real memo or legal advice" in reader.pages[0].extract_text()
    assert "Synthetic sample: not a real memo or legal advice" in html
    assert "sampleButton.onclick=()=>{fileInput.value='';choose(sampleMemoPdf())" in html
    assert "if(new URLSearchParams(location.search).get('example')==='vavilov')sampleButton.click();" in html


def test_onboarding_browser_generated_html_mocked_requests():
    """Real Chromium, no app server: every HTTP request is fulfilled or blocked."""
    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    if not chrome:
        pytest.skip("Chromium required for offline generated-HTML browser check")
    with tempfile.TemporaryDirectory(prefix="ilit-browser-") as profile:
        process = subprocess.Popen([
            chrome, "--headless", "--no-sandbox", "--disable-gpu",
            "--disable-background-networking", "--disable-component-update",
            "--no-first-run", "--remote-debugging-port=0",
            f"--user-data-dir={profile}", "about:blank",
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            port_file = Path(profile) / "DevToolsActivePort"
            for _ in range(300):
                if port_file.exists():
                    break
                time.sleep(.1)
            assert port_file.exists(), "Chromium did not expose DevTools"
            port = int(port_file.read_text().splitlines()[0])
            evidence = run_node(BROWSER_CHECK, {
                "port": port, "explorer": data_explorer_page_html(),
                "memo": memo_citation_check_page_html(), "start": start_page_html(),
            })
            assert "offline browser checks passed" in evidence
        finally:
            process.terminate()
            try:
                process.wait(timeout=20)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=10)


BROWSER_CHECK = r"""
const assert=require('node:assert/strict');
const input=JSON.parse(require('node:fs').readFileSync(0,'utf8'));
(async()=>{
 const tabs=await (await fetch(`http://127.0.0.1:${input.port}/json/list`)).json();
 const tab=tabs.find(tab=>tab.type==='page'&&tab.url==='about:blank');
 assert.ok(tab,'isolated blank browser tab');
 const ws=new WebSocket(tab.webSocketDebuggerUrl);
 await new Promise(resolve=>ws.addEventListener('open',resolve,{once:true}));
 let seq=0;const pending=new Map(),handlers={};
 ws.addEventListener('message',event=>{
  const message=JSON.parse(event.data);
  if(message.id){const p=pending.get(message.id);pending.delete(message.id);message.error?p.reject(Error(JSON.stringify(message.error))):p.resolve(message.result)}
  else handlers[message.method]?.(message.params);
 });
 const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++seq;pending.set(id,{resolve,reject});ws.send(JSON.stringify({id,method,params}))});
 const errors=[];
 handlers['Runtime.exceptionThrown']=event=>errors.push(event.exceptionDetails.exception?.description||event.exceptionDetails.text);
 await send('Runtime.enable');await send('Page.enable');
 // CDP request interception provides generated pages and prevents external/backend traffic.
 handlers['Fetch.requestPaused']=async event=>{
  const url=new URL(event.request.url);
  const html=url.pathname==='/data-explorer'?input.explorer:url.pathname==='/memo-citation-check'?input.memo:url.pathname==='/start'?input.start:null;
  await send('Fetch.fulfillRequest',{requestId:event.requestId,responseCode:html?200:404,responseHeaders:[{name:'Content-Type',value:html?'text/html':'application/json'}],body:Buffer.from(html||'{}').toString('base64')});
 };
 await send('Fetch.enable',{patterns:[{urlPattern:'*'}]});
 await send('Page.addScriptToEvaluateOnNewDocument',{source:`
 Object.defineProperty(window,'localStorage',{get(){throw new Error('storage blocked')}});
 window.fetch=async url=>{
  url=String(url);
  if(url.includes('/analytics/search/cases?')){
   (window.searchRequests ||= []).push(url);
   return {ok:true,json:async()=>({results:[],query_echo:'Court FC; year 2020; fairness AND NOT delay <literal>'})};
  }
  if(url.includes('/analytics/search/cases/')){
   const id=Number(url.split('/').pop());
   if(id===91)await new Promise(r=>setTimeout(r,220));
   if(id===93)return {ok:false,status:500,json:async()=>({})};
   return {ok:true,json:async()=>({case:{id,title:'Mock decision '+id,citation:'2019 SCC 65',court:'SCC',full_text:'[1] Mock reasons.'},citation_metrics:{citation_mentions:0},citations:[]})};
  }
  if(url.includes('/reader-data')){
   const id=Number(url.split('/')[2]);
   if(id===94)return {ok:false,status:404,json:async()=>({})};
   if(id===91)await new Promise(r=>setTimeout(r,220));
   return {ok:true,json:async()=>({case:{id,title:'Mock decision '+id,full_text:'[1] Mock reasons.'},full_text:'[1] Mock reasons.',chunks:[],citations:[],tags:[],formatted:{blocks:[]}})};
  }
  if(url.includes('/statute-references'))return {ok:true,json:async()=>[]};
  if(url.includes('/api/judge-profiles?'))return {ok:true,json:async()=>[{slug:'zinn',display_name:'Justice Zinn',primary_court:'FC',decision_count:12}]};
  if(url.includes('/api/judge-profiles/zinn/issues')){
   window.issueRequests=(window.issueRequests||0)+1;
   return {ok:true,json:async()=>({issues:[],hidden_issue_count:2,metadata:{minimum_decisions_per_visible_issue:10}})};
  }
  if(url.includes('/api/judge-profiles/zinn'))return {ok:true,json:async()=>({profile:{slug:'zinn',display_name:'Justice Zinn',primary_court:'FC'},decisions:[],outcomes:{}})};
  return {ok:true,json:async()=>({results:[],profiles:[],judges:[],rows:[],tags:[],ministers:[]})};
 };`});
 const evaluate=async expression=>{
  const result=await send('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});
  if(result.exceptionDetails)throw Error(result.exceptionDetails.exception?.description||result.exceptionDetails.text);
  return result.result.value;
 };
 const wait=async expression=>{for(let i=0;i<80;i++){if(await evaluate(expression))return;await new Promise(r=>setTimeout(r,40))}throw Error('wait failed: '+expression+'; '+await evaluate("location.href+' '+document.body?.innerText.slice(0,500)")+'; '+errors.join(';'))};
 await send('Page.navigate',{url:'http://ilit.test/start'});
 await wait("document.querySelectorAll('.task-card').length===5");
 assert.equal(await evaluate("document.querySelectorAll('.task-example').length"),5);
 await send('Page.navigate',{url:'http://ilit.test/data-explorer?query=procedural%20fairness&court=FC&search_full_text=true'});
 await wait("!!document.getElementById('researchTour')?.open");
 assert.equal(await evaluate("document.getElementById('searchQuery').value"),'procedural fairness');
 assert.equal(await evaluate("document.getElementById('courtFilter').value"),'FC');
 assert.equal(await evaluate("document.getElementById('searchFullText').checked"),true);
 assert.equal(await evaluate("document.getElementById('searchFilterSummary').textContent"),'2 active filters');
 assert.equal(await evaluate("document.querySelector('#quickFilters [data-qf=\"court\"][data-value=\"FC\"]').classList.contains('is-active')"),true);
 assert.equal(await evaluate("document.activeElement.id"),'tourNext');
 await send('Input.dispatchKeyEvent',{type:'keyDown',key:'Tab',code:'Tab',windowsVirtualKeyCode:9,modifiers:8});
 await send('Input.dispatchKeyEvent',{type:'keyUp',key:'Tab',code:'Tab',windowsVirtualKeyCode:9,modifiers:8});
 assert.equal(await evaluate("document.activeElement.id"),'tourDismiss');
 await evaluate("document.getElementById('searchQuery').focus()");
 assert.equal(await evaluate("document.getElementById('researchTour').contains(document.activeElement)"),true);
 await evaluate("document.getElementById('tourNext').focus()");
 await evaluate("document.getElementById('tourDismiss').focus()");
 await send('Input.dispatchKeyEvent',{type:'keyDown',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});
 await send('Input.dispatchKeyEvent',{type:'keyUp',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});
 assert.equal(await evaluate("document.activeElement.id"),'tourNext');
 await send('Input.dispatchKeyEvent',{type:'keyDown',key:'Escape',code:'Escape',windowsVirtualKeyCode:27});
 await send('Input.dispatchKeyEvent',{type:'keyUp',key:'Escape',code:'Escape',windowsVirtualKeyCode:27});
 assert.equal(await evaluate("document.getElementById('researchTour').open"),false);
 await evaluate("document.getElementById('searchTourButton').focus();document.getElementById('searchTourButton').click();document.getElementById('tourDismiss').click()");
 assert.equal(await evaluate("document.activeElement.id"),'searchTourButton');
 // Operator-rich URLs still prefill only, and submit through the normal search.
 const operatorQuery='court:FC year:2020 fairness AND -delay';
 await send('Page.navigate',{url:'http://ilit.test/data-explorer?query='+encodeURIComponent(operatorQuery)});
 await wait("!!document.getElementById('researchTour')?.open");
 assert.equal(await evaluate("document.getElementById('searchQuery').value"),operatorQuery);
 assert.equal(await evaluate("(window.searchRequests||[]).length"),0);
 assert.equal(await evaluate("!!document.getElementById('searchTipsToggle') && !!document.getElementById('downloadSearchCsv')"),true);
 await evaluate("document.getElementById('tourDismiss').click();document.getElementById('caseSearch').requestSubmit()");
 await wait("!document.getElementById('searchQueryEcho').hidden");
 const searchUrl=await evaluate("window.searchRequests.at(-1)");
 assert.equal(new URL(searchUrl,'http://ilit.test').searchParams.get('query'),operatorQuery);
 assert.equal(await evaluate("document.getElementById('searchQueryEcho').textContent"),'Search interpreted as: Court FC; year 2020; fairness AND NOT delay <literal>');
 assert.equal(await evaluate("document.getElementById('searchQueryEcho').children.length"),0);
 await evaluate("document.getElementById('searchTourButton').click();document.getElementById('tourDismiss').click()");
 assert.equal(await evaluate("document.getElementById('searchQuery').value"),operatorQuery);
 // Overlapping real reader loaders: delayed old result must not replace the current reader.
 await evaluate("openDecision(91);openDecision(92);true");
 await wait("readerState.caseId===92 && document.getElementById('researchTour').open");
 await new Promise(r=>setTimeout(r,350));
 assert.equal(await evaluate("readerState.caseId"),92);
 assert.equal(await evaluate("document.getElementById('decisionTitle').textContent"),'Mock decision 92');
 assert.equal(await evaluate("document.getElementById('tourProgress').textContent"),'Step 1 of 5');
 await evaluate("document.getElementById('tourDismiss').click();closeDecisionReader()");
 assert.equal(await evaluate("document.getElementById('researchTour').open"),false);
 await evaluate("openDecision(93)");
 assert.equal(await evaluate("document.getElementById('researchTour').open"),false);
 await evaluate("closeDecisionReader();openDecision(91);activateResearchTab('research-bench');true");
 await new Promise(r=>setTimeout(r,350));
 assert.equal(await evaluate("document.getElementById('caseReaderPanel').hidden"),true);
 assert.equal(await evaluate("document.getElementById('researchTour').open"),false);
 await send('Page.navigate',{url:'http://ilit.test/data-explorer?tab=search&case_id=93'});
 await wait("document.getElementById('decisionBody')?.textContent.includes('Request failed')");
 assert.equal(await evaluate("document.getElementById('researchTour').open"),false);
 await send('Page.navigate',{url:'http://ilit.test/data-explorer?tab=search&case_id=94'});
 await wait("typeof readerState!=='undefined' && readerState.caseId===94");
 assert.equal(await evaluate("document.getElementById('researchTour').open"),false);
 await send('Page.navigate',{url:'http://ilit.test/data-explorer?tab=search&case_id=95'});
 await wait("typeof readerState!=='undefined' && readerState.caseId===95 && document.getElementById('researchTour').open");
 assert.equal(await evaluate("document.getElementById('tourProgress').textContent"),'Step 1 of 5');
 await send('Page.navigate',{url:'http://ilit.test/data-explorer?tab=judge-profile&judge_query=Zinn'});
 await wait("document.getElementById('jpSearch')?.value==='Zinn'");
 assert.equal(await evaluate("document.getElementById('researchTour').open"),false);
 await wait("!!document.querySelector('#jpList [data-slug=\"zinn\"]')");
 assert.equal(await evaluate("window.issueRequests||0"),0);
 await evaluate("document.querySelector('#jpList [data-slug=\"zinn\"]').click()");
 await wait("!!document.querySelector('#jpIssuesContent [data-jp-issues]')");
 assert.equal(await evaluate("window.issueRequests||0"),0);
 await evaluate("document.querySelector('#jpIssuesContent [data-jp-issues]').click()");
 await wait("!!document.querySelector('#jpIssuesContent .jp-issue-scope')");
 assert.equal(await evaluate("window.issueRequests"),1);
 assert.equal(await evaluate("document.getElementById('jpSearch').value"),'Zinn');
 await send('Page.navigate',{url:'http://ilit.test/memo-citation-check?example=vavilov'});
 await wait("document.getElementById('fileLabel')?.textContent==='example-memo.pdf'");
 assert.equal(await evaluate("document.getElementById('analyze').disabled"),false);
 assert.equal(await evaluate("document.getElementById('status').textContent.includes('Analyzing')"),false);
 assert.deepEqual(errors,[]);
 console.log('offline browser checks passed: five cards, operator search echo/tour coexistence, judge prefill/lazy issue outcomes, memo prefill, Tab/Escape/focus restoration, blocked storage, actual reader stale/error/tab-switch/close guards');
 ws.close();
})().catch(error=>{console.error(error);process.exit(1)});
"""
