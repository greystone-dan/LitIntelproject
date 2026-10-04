"""Real Chromium/CDP acceptance over synthetic page content; no server or DB.

Uses installed Chromium and Node's built-in WebSocket, not a new dependency.
"""

import json
import re
import shutil
import subprocess

import pytest

from backend.case_formatter import format_decision
from backend.pages.data_explorer import data_explorer_page_html


CDP_RUNNER = r"""
const {spawn} = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'paragraph-counts-chrome-'));
const chrome = spawn(input.chromium, ['--headless', '--no-sandbox', '--disable-gpu',
  '--disable-background-networking', '--no-first-run', '--remote-debugging-port=0',
  '--user-data-dir=' + profile, 'about:blank'], {stdio:['ignore','ignore','pipe']});
let ws, closeBrowser;
const timeout = setTimeout(() => { console.error('Browser acceptance timed out'); chrome.kill(); process.exitCode=1; }, 45000);
(async () => {
  let stderr = '';
  const endpoint = await new Promise((resolve,reject) => {
    chrome.stderr.on('data', chunk => {
      stderr += chunk.toString();
      const match = stderr.match(/DevTools listening on (ws:\/\/[^\s]+)/);
      if (match) resolve(match[1]);
    });
    chrome.on('error', reject);
    chrome.on('exit', code => reject(new Error('Chromium exited: ' + code)));
  });
  ws = new WebSocket(endpoint);
  await new Promise(resolve => ws.addEventListener('open', resolve, {once:true}));
  let id=0, session, errors=[];
  const pending = new Map();
  ws.addEventListener('message', event => {
    const data=JSON.parse(event.data);
    if(data.id) {
      const task=pending.get(data.id); pending.delete(data.id);
      if(data.error)task.reject(new Error(JSON.stringify(data.error))); else task.resolve(data.result);
    } else if(data.method==='Runtime.exceptionThrown') {
      errors.push(data.params.exceptionDetails.exception?.description || data.params.exceptionDetails.text);
    } else if(data.method==='Fetch.requestPaused') {
      const request=data.params;
      if(request.resourceType==='Document' && request.request.url==='http://fixture.invalid/data-explorer') {
        command('Fetch.fulfillRequest',{requestId:request.requestId,responseCode:200,
          responseHeaders:[{name:'Content-Type',value:'text/html; charset=utf-8'}],
          body:Buffer.from(input.html).toString('base64')});
      } else {
        command('Fetch.failRequest',{requestId:request.requestId,errorReason:'BlockedByClient'});
      }
    }
  });
  const command=(method,params={},page=true)=>new Promise((resolve,reject)=>{
    const current=++id; pending.set(current,{resolve,reject});
    ws.send(JSON.stringify({id:current,method,params,...(page&&session?{sessionId:session}:{})}));
  });
  closeBrowser=()=>command('Browser.close',{},false);
  const target=await command('Target.createTarget',{url:'about:blank'},false);
  session=(await command('Target.attachToTarget',{targetId:target.targetId,flatten:true},false)).sessionId;
  await command('Runtime.enable');
  await command('Page.enable');
  await command('Network.enable');
  await command('Fetch.enable',{patterns:[{urlPattern:'*'}]});
  const evaluate=async expression=>{
    const result=await command('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});
    if(result.exceptionDetails)throw new Error(result.exceptionDetails.exception?.description || result.exceptionDetails.text);
    return result.result.value;
  };
  await command('Page.navigate',{url:'http://fixture.invalid/data-explorer'});
  for(let attempt=0;attempt<100;attempt++){
    if(await evaluate("document.readyState==='complete' && typeof openDecision==='function'"))break;
    await new Promise(resolve=>setTimeout(resolve,25));
  }
  const results=[];
  for (const width of [1440,390]) {
    await command('Emulation.setDeviceMetricsOverride',{width,height:900,deviceScaleFactor:1,mobile:false});
    results.push(await evaluate(input.checks));
    await evaluate("document.getElementById('readerParagraphCountsToggle').focus()");
    for(const type of ['keyDown','keyUp'])await command('Input.dispatchKeyEvent',{type,key:' ',code:'Space',windowsVirtualKeyCode:32});
    if(await evaluate("document.getElementById('readerParagraphCountsToggle').getAttribute('aria-pressed')")!=='false')throw new Error('Native Space toggle off');
    await evaluate("document.getElementById('readerParagraphCountsToggle').focus()");
    for(const type of ['keyDown','keyUp'])await command('Input.dispatchKeyEvent',{type,key:'Enter',code:'Enter',windowsVirtualKeyCode:13,...(type==='keyDown'?{text:'\r'}:{})});
    if(await evaluate("document.getElementById('readerParagraphCountsToggle').getAttribute('aria-pressed')")!=='true')throw new Error('Native Enter toggle on');
    await command('Emulation.setEmulatedMedia',{media:'print'});
    results.push(await evaluate(input.printChecks));
    await command('Emulation.setEmulatedMedia',{media:''});
  }
  results.push(await evaluate(input.lifecycleChecks));
  if(errors.length)throw new Error(errors.join('\n'));
  console.log(JSON.stringify({results,errors}));
})().catch(error=>{console.error(error.stack);process.exitCode=1;}).finally(async()=>{
  chrome.on('close',()=>fs.rm(profile,{recursive:true,force:true,maxRetries:10,retryDelay:100},error=>{
    if(error)console.warn('Temporary browser profile cleanup: '+error.message);
  }));
  try { await closeBrowser?.(); } catch {}
  clearTimeout(timeout);ws?.close();chrome.kill();
});
"""

CHECKS = r"""
(async()=>{
  const assert=(value,message)=>{if(!value)throw new Error(message);};
  await openDecision(42);
  const button=document.getElementById('readerParagraphCountsToggle');
  const para=number=>document.querySelector(`#decisionBody .fmt-para[data-para="${number}"]`);
  assert(!button.disabled && button.getAttribute('aria-pressed')==='false','default-off formatted control');
  assert(para(1).title==='Cited by 9 cases','legacy tooltip preserved');
  assert(getComputedStyle(para(1)).backgroundColor==='rgb(255, 249, 232)','legacy shading preserved');
  assert(!document.getElementById('readerMostCited').hidden,'legacy top-five list preserved');
  assert(document.querySelectorAll('#readerMostCitedList a').length===2,'legacy ranking entries');
  const anchors=Array.from(document.querySelectorAll('#decisionBody .fmt-para')).map(p=>p.id);
  button.click();await new Promise(resolve=>setTimeout(resolve,30));
  assert(button.getAttribute('aria-pressed')==='true','toggle pressed');
  assert(para(1).title==='Cited by 2 later decisions','later tooltip');
  assert(para(3).querySelector('.reader-paragraph-count-label').textContent==='Cited by 1 later decision','singular visible count');
  assert(para(7).querySelector('.reader-paragraph-count-label').textContent==='Cited by 0 later decisions','zero visible count');
  assert(getComputedStyle(para(7)).backgroundColor==='rgba(0, 0, 0, 0)','zero unshaded');
  assert(getComputedStyle(para(1)).backgroundColor!==getComputedStyle(para(3)).backgroundColor,'relative intensity');
  assert(document.getElementById('readerParagraphCountsCoverage').textContent.includes('2 of 3 later citing decisions'),'decision coverage');
  assert(document.getElementById('readerParagraphCountsCoverage').textContent.includes('2 of 5 stored citation occurrences'),'occurrence denominator');
  assert(JSON.stringify(anchors)===JSON.stringify(Array.from(document.querySelectorAll('#decisionBody .fmt-para')).map(p=>p.id)),'backend anchors unchanged');
  for(const block of readerState.payload.readerData.format_blocks.filter(b=>b.type==='para')){
    assert(para(block.num).querySelector('.fmt-para-body').textContent===Array.from(readerState.payload.item.full_text).slice(block.mark_end,block.end).join(''),'source text and code-point spans unchanged');
    const label=para(block.num).querySelector('.reader-paragraph-count-label');
    assert(getComputedStyle(label).gridColumnStart==='2','count label aligns with paragraph body, not number gutter');
    assert(label.getBoundingClientRect().right<=para(block.num).getBoundingClientRect().right+1,'count label stays within paragraph on mobile');
  }
  button.click();
  assert(para(1).title==='Cited by 9 cases' && !para(1).hasAttribute('data-citation-heat'),'toggle restores original tooltip and shading');
  assert(getComputedStyle(para(1)).backgroundColor==='rgb(255, 249, 232)','toggle restores default color');
  button.focus(); // native keyboard-accessible button activation
  button.click();await new Promise(resolve=>setTimeout(resolve,10));
  setReaderMode('chunks');
  assert(button.disabled && !document.querySelector('.reader-paragraph-count-label'),'chunk mode unchanged');
  setReaderMode('normalized');
  assert(!button.disabled && para(1).hasAttribute('data-citation-heat'),'formatted mode reapplies counts');
  readerState.formatted=false;setReaderMode('normalized');
  assert(button.disabled && !document.querySelector('.reader-paragraph-count-label'),'plain mode unchanged');
  readerState.formatted=true;setReaderMode('normalized');
  document.querySelector('#readerMostCitedList a').click();
  assert(document.activeElement.id===para(1).id,'existing most-cited jump and focus');
  document.activeElement.blur();
  document.dispatchEvent(new KeyboardEvent('keydown',{key:'j',bubbles:true}));
  assert(document.querySelector('#decisionBody .is-reader-current'),'existing keyboard paragraph navigation');
  await new Promise(resolve=>setTimeout(resolve,10));
  assert(document.querySelector('[data-paragraph-similar]') || document.getElementById('decisionBody').textContent.includes('Similar paragraphs'),'similarity control preserved');
  document.querySelector('.reader-extracted-summary a').click();
  assert(document.activeElement.id===para(3).id,'extracted summary source-link focus preserved');
  document.getElementById('readerSummaryToggle').click();
  assert(!document.getElementById('readerSummaryDetail').hidden,'structure control preserved');
  document.getElementById('readerSummaryToggle').click();
  await new Promise(resolve=>setTimeout(resolve,10));
  document.querySelector('[data-paragraph-similar]').click();
  await new Promise(resolve=>setTimeout(resolve,10));
  assert(document.getElementById('paragraphSimilarity').textContent.includes('No matches found'),'similarity request preserved');
  document.getElementById('paragraphSimilarity').remove();
  return {viewport:innerWidth,paragraphs:anchors.length,defaultShading:true,toggle:true,modes:true,keyboard:true,list:true,summary:true,structure:true,similarity:true};
})()
"""

PRINT_CHECKS = r"""
(()=>{
  const assert=(value,message)=>{if(!value)throw new Error(message);};
  const paras=Array.from(document.querySelectorAll('#decisionBody .fmt-para'));
  assert(paras.length===3,'print paragraphs retained');
  paras.forEach(p=>{
    assert(getComputedStyle(p).backgroundColor==='rgba(0, 0, 0, 0)','print has no paragraph shading');
    assert(getComputedStyle(p).boxShadow==='none','print has no paragraph shadow');
  });
  assert(getComputedStyle(document.querySelector('.reader-paragraph-count-label')).display==='none','print labels hidden');
  assert(getComputedStyle(document.querySelector('.reader-paragraph-count-controls')).display==='none','print controls hidden');
  return {print:true,noShading:true};
})()
"""

LIFECYCLE_CHECKS = r"""
(async()=>{
  const assert=(value,message)=>{if(!value)throw new Error(message);};
  const button=document.getElementById('readerParagraphCountsToggle');
  await openDecision(43);
  assert(button.getAttribute('aria-pressed')==='false','new case resets toggle');
  assert(!document.querySelector('[data-citation-heat]'),'new case has no stale counts');
  window.fixtureFailure=true;
  button.click();await new Promise(resolve=>setTimeout(resolve,20));
  assert(button.getAttribute('aria-pressed')==='false','failure resets toggle');
  assert(document.getElementById('readerParagraphCountsCoverage').textContent.includes('unavailable'),'failure is visible');
  window.fixtureFailure=false;
  window.fixtureDelay=true;
  button.click();
  await openDecision(42);
  window.fixturePending({ok:true,json:async()=>window.fixtureCounts(43)});
  await new Promise(resolve=>setTimeout(resolve,20));
  assert(!document.querySelector('[data-citation-heat]'),'late prior-case response ignored');
  window.fixtureDelay=false;
  button.click();await new Promise(resolve=>setTimeout(resolve,20));
  closeDecisionReader();
  assert(button.disabled && button.getAttribute('aria-pressed')==='false','close resets toggle');
  assert(!document.querySelector('[data-citation-heat]'),'close clears annotation');
  await openDecision(44);
  button.click();await new Promise(resolve=>setTimeout(resolve,20));
  assert(document.getElementById('readerParagraphCountsCoverage').textContent.includes('0 of 0 later citing decisions'),'empty coverage');
  assert(Array.from(document.querySelectorAll('[data-citation-heat]')).every(p=>p.dataset.citationHeat==='0'),'empty counts all zero');
  await openDecision(45);
  button.click();await new Promise(resolve=>setTimeout(resolve,20));
  assert(document.getElementById('readerParagraphCountsCoverage').textContent.includes('date unavailable'),'unknown chronology is visible');
  assert(!document.querySelector('[data-citation-heat]'),'unknown chronology does not imply zero later citations');
  return {caseReset:true,failure:true,staleResponse:true,close:true,empty:true,unknownDate:true};
})()
"""


def test_optional_toggle_fixture_browser_desktop_mobile_print_and_lifecycle():
    chromium, node = shutil.which("chromium"), shutil.which("node")
    if not chromium or not node:
        pytest.skip("Installed Chromium and Node with built-in WebSocket required")
    if subprocess.run([node, "-p", "typeof WebSocket"], capture_output=True, text=True).stdout.strip() != "function":
        pytest.skip("Node with built-in WebSocket required for fixture browser acceptance")
    text = "Decision Content\n[1] First 😀.\n[3] Third.\n[7] Seventh."
    blocks = format_decision(text, {1: 9, 3: 4})
    fixture = {
        "case": {"id": 42, "title": "Synthetic case", "date": "2020-01-01", "court": "Fixture court", "citation": "2020 FC 42", "full_text": text},
        "format_blocks": blocks, "sources": [], "chunks": [], "tags": [], "citations": [],
        "statute_references": [], "extracted_metadata": [], "inferred_tags": [],
        "extracted_summary": [{
            "key": "tag:issue", "label": "Issue", "value": "Third",
            "evidence": "Third", "block_start": blocks[2]["start"],
            "block_type": "para", "paragraph_number": 3,
        }], "evidence_summary": None,
    }
    setup = """
window.fixtureCounts=id=>({case_id:id,counts:{1:id>=44?0:2,3:id>=44?0:1,7:0},
chronology_known:id!==45,total_citing_decisions:id>=44?0:3,
citing_decisions_with_usable_pinpoint:id>=44?0:2,citing_decisions_without_usable_pinpoint:id>=44?0:1,
total_citations:id>=44?0:5,citations_without_usable_pinpoint:id>=44?0:2});
const fixture=FIXTURE;
window.fetch=async url=>{
  const id=Number(String(url).match(/cases\\/(\\d+)/)?.[1]||42);
  if(String(url).endsWith('/paragraph-citation-counts')){
    if(window.fixtureDelay)return new Promise(resolve=>window.fixturePending=resolve);
    return {ok:!window.fixtureFailure,status:503,json:async()=>window.fixtureCounts(id)};
  }
  if(String(url).endsWith('/reader-data'))return {ok:true,json:async()=>fixture};
  if(String(url).startsWith('/analytics/search/cases/'))return {ok:true,json:async()=>({case:{...fixture.case,id},citation_metrics:{citation_mentions:0},citations:[]})};
  return {ok:true,json:async()=>({results:[],rows:[],data:[],profiles:[],available:false,assessments:{}})};
};
""".replace("FIXTURE", json.dumps(fixture))
    html = data_explorer_page_html()
    # Known pre-existing Tag Analytics syntax error is outside the reader; do
    # not change it or execute that unrelated script in this reader fixture.
    html = re.sub(r"<script>(.*?)</script>", lambda match: "" if "el('tga-empty'}" in match[1] else match[0], html, flags=re.S | re.I)
    html = html.replace("<head>", "<head><script>" + setup + "</script>", 1)
    result = subprocess.run(
        [node, "-e", CDP_RUNNER], input=json.dumps({
            "chromium": chromium, "html": html, "checks": CHECKS,
            "printChecks": PRINT_CHECKS, "lifecycleChecks": LIFECYCLE_CHECKS,
        }), text=True, capture_output=True, timeout=65,
    )
    assert result.returncode == 0, result.stderr
    output = json.loads(result.stdout)
    assert output["errors"] == []
    assert len(output["results"]) == 5
