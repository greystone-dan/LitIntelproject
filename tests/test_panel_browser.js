// Fixture-only browser acceptance; no server, dependencies or external requests.
// Run: node tests/test_panel_browser.js
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {spawnSync} = require('node:child_process');
const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'backend/pages/data_explorer.py'), 'utf8');
const helper = fs.readFileSync(path.join(root, 'backend/degraded_mode.py'), 'utf8')
    .match(/return r"""<script>\n([\s\S]*?)\n<\/script>"""/)[1];
const queue = source.slice(source.indexOf('const panelRequests='), source.indexOf('function readerPanelCurrent'));
const card = source.slice(source.indexOf('function professionalResultCard('), source.indexOf('let professionalSearchGeneration='));
const search = source.slice(source.indexOf('let professionalSearchGeneration='), source.indexOf('function bindProfessionalSearch('));
const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'ilit-panel-browser-'));
const fixture = `<!doctype html><html><head><meta charset="utf-8"></head><body>
<div id="neighbor">Healthy sibling</div><div id="panel"></div>
<div id="searchQueryEcho"></div><div id="searchResults"></div><div id="status"></div>
<pre id="result">RUNNING</pre><script>
const errors=[];
addEventListener('error',e=>errors.push(e.message));
addEventListener('unhandledrejection',e=>errors.push(String(e.reason)));
const check=(condition,message)=>{if(!condition)throw Error(message)};
const tick=()=>new Promise(resolve=>setTimeout(resolve,0));
const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const num=value=>String(Number(value||0));
const closeSearchSuggestions=()=>{};
const searchValues=()=>({query:'Fixture',limit:'5'});
const setSearchStatus=value=>document.getElementById('status').textContent=value;
const openDecision=()=>{};
${helper}
${queue}
${card}
${search}
(async()=>{
 const panel=document.getElementById('panel'),neighbor=document.getElementById('neighbor');
 let calls=0,renders=0,release;
 window.fetch=async()=>{
   calls++;
   if(calls===1)return {ok:false,json:async()=>{throw Error('must not parse failure')}};
   return new Promise(resolve=>{release=()=>resolve({ok:true,json:async()=>({label:'Recovered'})})});
 };
 await fetchPanel('/fixture',panel,{render:data=>{renders++;panel.textContent=data.label}});
 check(panel.textContent==='This section could not load.Retry','plain-language failure');
 check(neighbor.textContent==='Healthy sibling','failure isolation');
 const retry=panel.querySelector('button');retry.click();retry.click();
 check(retry.disabled,'disabled retry');
 check(panel.querySelector('[aria-live="polite"]'),'loading live region');
 await tick();check(calls===2,'bounded concurrency');release();await tick();
 check(renders===1&&panel.textContent==='Recovered','retry uses renderer');
 check(neighbor.textContent==='Healthy sibling','retry isolation');
 let searchCalls=0;
 window.fetch=async url=>{
   check(url.startsWith('/analytics/search/cases?'),'unchanged search endpoint');
   searchCalls++;
   return searchCalls===1?{ok:false}:{ok:true,json:async()=>({results:[{
     case_id:229,title:'Fixture decision',citation:'2026 FC 229',court:'FC',
     citation_mentions:2,unique_cited_authorities:1,resolved_target_cases:1
   }]})};
 };
 await runProfessionalSearch();
 check(document.getElementById('searchResults').textContent==='This section could not load.Retry','search failure');
 document.querySelector('#searchResults button').click();await tick();await tick();
 check(searchCalls===2,'search retry one request');
 check(document.querySelector('#searchResults .case-result').dataset.caseId==='229','healthy search renderer');
 check(document.getElementById('searchResults').textContent.includes('2026 FC 229'),'citation preserved');
 check(errors.length===0,'no browser errors: '+errors.join(','));
 document.getElementById('result').textContent='PASS: browser isolation, loading, disabled retry and Case Search rendering';
})().catch(error=>{document.getElementById('result').textContent='FAIL: '+error.message});
</script></body></html>`;
try {
    const file = path.join(directory, 'fixture.html');
    fs.writeFileSync(file, fixture);
    const result = spawnSync(process.env.CHROME_BIN || 'chromium', [
        '--headless', '--no-sandbox', '--disable-gpu', '--disable-background-networking',
        '--no-first-run', '--no-default-browser-check', '--disable-extensions',
        `--user-data-dir=${path.join(directory, 'profile')}`,
        '--virtual-time-budget=3000', '--dump-dom', `file://${file}`,
    ], {encoding: 'utf8', timeout: 90000, maxBuffer: 2 * 1024 * 1024});
    assert.equal(result.error, undefined, result.error?.message);
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /<pre id="result">PASS: browser isolation, loading, disabled retry and Case Search rendering<\/pre>/);
    console.log('Fixture-only Chromium panel and Case Search checks passed.');
} finally {
    fs.rmSync(directory, {recursive: true, force: true});
}
