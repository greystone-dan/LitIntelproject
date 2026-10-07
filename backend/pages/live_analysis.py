"""Live Analysis page: the case reader's markup view for a document the user brings.

The page is the site's own research page (same header, navigation, styles and reader code), with a
Workbench view where a DOCX, text PDF or pasted text is read in memory and shown in the reader's
markup mode. Nothing is stored and no model is called; see ``backend/live_reader.py``.
"""

from __future__ import annotations

from .data_explorer import data_explorer_page_html

PANEL_HTML = r'''<section id="liveAnalysisPanel" class="panel-card search-layout live-analysis-panel" hidden>
<div class="page-header"><div class="eyebrow">Workbench</div><h2>Live Analysis</h2><p>Bring a memo, factum or decision and read it the way the case reader shows a decision: its case citations and statute references marked in the text, with the cited paragraph, the Act's provision text and the library's cited-by counts in the margin.</p></div>
<div class="la-privacy" role="note"><strong>Not stored, no AI.</strong> The document is read in memory for this request and discarded. It is never saved to the library and never sent to any model. Only the existing rule-based citation and statute checks run, against the library as it already is.</div>
<div class="la-inputs">
<label class="la-drop" id="laDrop"><input id="laFile" type="file" accept=".docx,.pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/pdf"><strong id="laFileLabel">Choose a DOCX or text PDF</strong><span>or drop it here. Up to 10 MB. Scanned PDFs are not read.</span></label>
<div class="la-or">or paste text</div>
<label class="la-paste"><span class="la-sr">Pasted text</span><textarea id="laText" rows="7" placeholder="Paste the text of a memo or decision here. Blank lines separate paragraphs."></textarea></label>
</div>
<div class="la-actions"><button type="button" class="la-go" id="laAnalyze" disabled>Read in markup mode</button><button type="button" class="la-clear" id="laClear">Clear</button><span class="la-status" id="laStatus" role="status">Nothing selected yet</span></div>
<div class="la-error" id="laError" role="alert" hidden></div>
<p class="la-note">Headings and paragraph numbers in an uploaded document are worked out from line shape (a heuristic), not read from the file's own styles. The case information panels that rely on a stored decision (outcome, judge, discussion units, tags) are not available for your own text.</p>
</section>
'''

STYLE = r'''<style>
.live-analysis-panel .la-privacy{margin:14px 0;padding:11px 14px;border:1px solid var(--border);border-left:3px solid var(--blue,#2563eb);border-radius:4px;background:var(--surface-alt);font-size:13px;line-height:1.55}
.la-inputs{display:grid;grid-template-columns:minmax(0,1fr);gap:10px;max-width:820px}
.la-drop{display:block;padding:22px 18px;border:1.5px dashed var(--border);border-radius:6px;background:var(--surface);text-align:center;cursor:pointer}
.la-drop.is-drag,.la-drop:focus-within{border-color:var(--blue,#2563eb);background:var(--surface-alt)}
.la-drop input{position:absolute;opacity:0;width:1px;height:1px}
.la-drop strong{display:block;font-size:14px}.la-drop span{display:block;margin-top:4px;color:var(--muted);font-size:12px}
.la-or{color:var(--muted);font-size:12px;text-align:center}
.la-paste textarea{width:100%;box-sizing:border-box;padding:10px 12px;border:1px solid var(--border);border-radius:6px;font:13px/1.55 Georgia,"Times New Roman",serif;background:var(--surface);color:var(--text);resize:vertical}
.la-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.la-actions{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:14px 0}
.la-go,.la-clear{padding:8px 16px;border-radius:5px;border:1px solid var(--border);font:600 13px "IBM Plex Sans",sans-serif;cursor:pointer;background:var(--surface);color:var(--text)}
.la-go{background:var(--blue,#2563eb);border-color:var(--blue,#2563eb);color:#fff}.la-go:disabled{opacity:.5;cursor:not-allowed}
.la-status{color:var(--muted);font-size:12px}.la-error{margin:0 0 10px;padding:9px 12px;border:1px solid #e3b5b5;border-radius:4px;background:#fdf1f1;color:#8a1f1f;font-size:13px}
.la-note{max-width:820px;color:var(--muted);font-size:12px;line-height:1.55}
html.wb-embedded .topbar,html.wb-embedded #researchViews{display:none!important}
html.wb-embedded .center-pane{padding-top:12px}
body.live-doc-open #v6Card .v6-court,body.live-doc-open #v6Card [data-v6-copy],body.live-doc-open #v6Card .v6-stat[data-v6-go="intel"]{display:none}
.la-tools{padding:8px 20px 0;flex-wrap:wrap;align-items:center;gap:8px;margin:10px 0 0}
body .reader-head>#laTools#laTools.la-tools{display:flex!important}
.la-tools button{padding:6px 12px;border:1px solid var(--border);border-radius:5px;background:var(--surface);font:600 12px "IBM Plex Sans",sans-serif;cursor:pointer;color:var(--text)}
.la-tools button:hover{border-color:var(--teal,#176c68);color:var(--teal,#176c68)}
.la-tools .la-msg{color:var(--muted);font-size:12px}
.la-modal{position:fixed;inset:0;z-index:80;display:flex;align-items:center;justify-content:center;padding:18px;background:rgba(32,37,34,.45)}
.la-modal[hidden]{display:none}
.la-dialog{display:flex;flex-direction:column;width:min(980px,100%);max-height:88vh;border:1px solid var(--border);border-radius:6px;background:var(--surface);box-shadow:0 20px 50px rgba(0,0,0,.25)}
.la-dialog header{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 16px;border-bottom:1px solid var(--border)}
.la-dialog h3{margin:0;font:600 19px "Newsreader",serif}
.la-dialog .la-scroll{overflow:auto;padding:0 16px 14px}
.la-table{width:100%;min-width:560px;border-collapse:collapse;font-size:13px}
.la-table th{position:sticky;top:0;padding:9px 8px;background:var(--surface);border-bottom:1px solid var(--border);text-align:left;color:var(--muted);font-size:11px;letter-spacing:.06em;text-transform:uppercase}
.la-table td{padding:8px;border-bottom:1px solid var(--border);vertical-align:top}
.la-yes{color:#115450;font-weight:600}.la-no{color:var(--muted)}
.la-foot{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:10px 16px;border-top:1px solid var(--border)}
body.live-doc-open [data-side-tab="about"],body.live-doc-open [data-side-tab="structure"],body.live-doc-open [data-side-tab="tags"],body.live-doc-open [data-mk-act="export"],body.live-doc-open #readerViewToggle,body.live-doc-open #readerCompareLink,body.live-doc-open #readerCopyCite,body.live-doc-open #readerFormatToggle,body.live-doc-open #readerPrintCitation{display:none!important}
</style>
'''

SCRIPT = r'''<script>
/* Live Analysis: send the document to /live-analysis/reader, then show the reader's markup view over the result. */
if(window.self!==window.top)document.documentElement.classList.add('wb-embedded');
(function(){
const $=id=>document.getElementById(id);
const panel=$('liveAnalysisPanel'),file=$('laFile'),text=$('laText'),go=$('laAnalyze'),status=$('laStatus'),err=$('laError'),drop=$('laDrop');
if(!panel)return;
let chosen=null;
const showError=m=>{err.textContent=m||'';err.hidden=!m};
function refresh(){go.disabled=!(chosen||text.value.trim());status.textContent=chosen?`${chosen.name} · ${(chosen.size/1048576).toFixed(2)} MB`:(text.value.trim()?'Pasted text ready':'Nothing selected yet')}
function choose(f){chosen=f||null;$('laFileLabel').textContent=chosen?chosen.name:'Choose a DOCX or text PDF';if(chosen)text.value='';refresh();showError('')}
file.addEventListener('change',()=>choose(file.files[0]));
text.addEventListener('input',()=>{if(text.value.trim()&&chosen){chosen=null;file.value='';$('laFileLabel').textContent='Choose a DOCX or text PDF'}refresh()});
['dragenter','dragover'].forEach(n=>drop.addEventListener(n,e=>{e.preventDefault();drop.classList.add('is-drag')}));
['dragleave','drop'].forEach(n=>drop.addEventListener(n,e=>{e.preventDefault();drop.classList.remove('is-drag')}));
drop.addEventListener('drop',e=>{const f=e.dataTransfer&&e.dataTransfer.files[0];if(f)choose(f)});
$('laClear').addEventListener('click',()=>{chosen=null;file.value='';text.value='';refresh();showError('');if(!$('caseReaderPanel').hidden)closeDecisionReader()});
async function analyze(){
  showError('');go.disabled=true;status.textContent='Reading the document…';
  try{
    let response;
    if(chosen){const body=new FormData();body.append('file',chosen);response=await fetch('/live-analysis/reader',{method:'POST',body})}
    else response=await fetch('/live-analysis/reader-text',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:text.value,title:'Pasted text'})});
    if(!response.ok){let d='The document could not be read.';try{const j=await response.json();if(j&&j.detail)d=typeof j.detail==='string'?j.detail:d}catch(e){}throw new Error(d)}
    open(await response.json());
    status.textContent='';
  }catch(e){showError(e.message||'The document could not be read.')}
  finally{refresh()}
}
go.addEventListener('click',analyze);

/* Authority table: every distinct authority the document cites, with library status, as a table and a CSV. */
const escHtml=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let lastData=null;
function authorityRows(data){
  const map=new Map();
  (data.citations||[]).forEach(c=>{
    const statute=c.citation_kind==='statute';
    const key=(statute?'s|':'c|')+String(c.normalized_citation||c.citation_text||'').toLowerCase();
    let row=map.get(key);
    if(!row){row={kind:statute?'Statute':'Case',text:c.citation_text||'',title:c.target_title||'',caseId:c.target_case_id||null,inLibrary:statute?!c.unresolved:c.target_case_id!=null,mentions:0};map.set(key,row)}
    row.mentions+=1;
    if(!row.title&&c.target_title)row.title=c.target_title;
  });
  return [...map.values()].sort((a,b)=>(a.kind===b.kind?0:a.kind==='Case'?-1:1)||b.mentions-a.mentions);
}
function csvCell(v){let t=String(v??'');if(/^[=+\-@\t\r]/.test(t))t="'"+t;return /[",\n]/.test(t)?'"'+t.replace(/"/g,'""')+'"':t}
function authorityCsv(rows){return ['Kind,Citation as written,Title in library,In library,Mentions,Case ID'].concat(rows.map(r=>[r.kind,r.text,r.title,r.inLibrary?'Yes':'No',r.mentions,r.caseId||''].map(csvCell).join(','))).join('\r\n')}
function downloadCsv(rows,name){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['﻿'+authorityCsv(rows)],{type:'text/csv'}));a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},400)}
function ensureModal(){
  let m=$('laModal');if(m)return m;
  m=document.createElement('div');m.id='laModal';m.className='la-modal';m.hidden=true;
  m.innerHTML='<div class="la-dialog" role="dialog" aria-modal="true" aria-labelledby="laModalTitle"><header><h3 id="laModalTitle">Authorities in this document</h3><button type="button" class="la-clear" id="laModalClose">Close</button></header><div class="la-scroll" id="laModalBody"></div><div class="la-foot" id="laModalFoot"></div></div>';
  document.body.appendChild(m);
  m.addEventListener('click',e=>{if(e.target===m)m.hidden=true});
  m.querySelector('#laModalClose').addEventListener('click',()=>{m.hidden=true});
  document.addEventListener('keydown',e=>{if(e.key==='Escape')m.hidden=true});
  return m;
}
async function saveCasesToWorkbench(rows,msg){
  const ids=[...new Set(rows.filter(r=>r.caseId).map(r=>r.caseId))];
  if(!ids.length){msg.textContent='No library cases found to save.';return}
  msg.textContent='Saving…';let ok=0;
  for(const id of ids){
    const r=await fetch('/workbench/api/pins',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({case_id:id})});
    if(r.status===401){msg.textContent='Sign in on the Workbench home first, then try again.';return}
    if(r.ok)ok+=1;
  }
  msg.textContent=`Saved ${ok} of ${ids.length} library cases to your pinned decisions.`;
}
function showAuthorities(){
  if(!lastData)return;
  const rows=authorityRows(lastData),m=ensureModal();
  const cases=rows.filter(r=>r.kind==='Case'),acts=rows.filter(r=>r.kind==='Statute');
  $('laModalBody').innerHTML=rows.length?`<p class="la-note">${cases.length} distinct case citation${cases.length===1?'':'s'} (${cases.filter(r=>r.inLibrary).length} in the library) and ${acts.length} statute reference${acts.length===1?'':'s'}. Citations are matched by fixed rules, so read them against the document.</p><table class="la-table"><thead><tr><th>Kind</th><th>As written</th><th>In the library</th><th>Mentions</th></tr></thead><tbody>${rows.map(r=>`<tr><td>${r.kind}</td><td>${escHtml(r.text)}${r.title?`<div class="la-note">${escHtml(r.title)}</div>`:''}</td><td>${r.caseId?`<a class="la-yes" href="/data-explorer?tab=search&case_id=${r.caseId}" target="_blank" rel="noopener">Open case</a>`:r.inLibrary?'<span class="la-yes">Yes</span>':'<span class="la-no">Not found</span>'}</td><td>${r.mentions}</td></tr>`).join('')}</tbody></table>`:'<p class="la-note">No case or statute citations were found in this document.</p>';
  const foot=$('laModalFoot');
  foot.innerHTML='<button type="button" class="la-clear" id="laCsv">Download CSV</button><button type="button" class="la-clear" id="laPinAll">Save library cases to Workbench</button><span class="la-status" id="laPinMsg"></span>';
  $('laCsv').onclick=()=>downloadCsv(rows,'authorities.csv');
  $('laPinAll').onclick=()=>saveCasesToWorkbench(rows,$('laPinMsg'));
  m.hidden=false;$('laModalClose').focus();
}
function setTools(data){
  lastData=data;
  let bar=$('laTools');
  if(!bar){bar=document.createElement('div');bar.id='laTools';bar.className='la-tools';const toolbar=$('caseReaderPanel').querySelector('.reader-toolbar');(toolbar?toolbar.before.bind(toolbar):$('decisionTarget').before.bind($('decisionTarget')))(bar)}
  bar.innerHTML='<button type="button" id="laAuth">Authority table</button><button type="button" id="laAuthCsv">Download authorities CSV</button>';
  $('laAuth').onclick=showAuthorities;
  $('laAuthCsv').onclick=()=>downloadCsv(authorityRows(lastData),'authorities.csv');
}
function clearTools(){const bar=$('laTools');if(bar)bar.remove();lastData=null}
function open(data){
  setTools(data);
  const reader=$('caseReaderPanel');
  document.body.classList.add('live-doc-open');
  readerState.caseId=null;readerState.payload={item:data.item,citations:data.citations,readerData:data.readerData};readerState.formatted=true;readerState.mode='normalized';
  $('decisionTitle').textContent=data.filename;
  const s=data.summary||{};
  try{console.info('Live Analysis library lookup',{failed:!!s.library_lookup_failed,error:s.library_lookup_error||null,ms:s.library_lookup_ms,cases:s.case_citations,inLibrary:s.resolved_case_citations})}catch(e){}
  $('decisionEyebrow').textContent='Your document · read in memory, not stored';
  $('decisionMeta').innerHTML=[`${s.paragraphs} paragraphs`,`${s.case_citations} case citation${s.case_citations===1?'':'s'} (${s.resolved_case_citations} in the library)`,`${s.statute_references} statute reference${s.statute_references===1?'':'s'}`].concat(s.library_lookup_failed?['Library could not be checked: '+(s.library_lookup_error||'unknown error')]:[]).map(v=>`<span class="meta-pill">${v}</span>`).join('');
  $('decisionTarget').replaceChildren();
  sideState.caseId=null;sideState.tab='authorities';sideState.linkedId=null;
  const back=reader.querySelector('.return-to-results');if(back)back.innerHTML='&larr; Back to Live Analysis';
  panel.hidden=true;$('searchPanel').hidden=true;reader.hidden=false;
  setReaderMode('normalized');
  const toggle=$('readerMarkupToggle');if(toggle&&toggle.getAttribute('aria-pressed')!=='true')toggle.click();
  reader.scrollIntoView({block:'start'});
}
/* A library case opens in a new tab so the uploaded document (held only in this page) is not lost. */
document.addEventListener('click',e=>{
  const foot=e.target.closest&&e.target.closest('[data-mk-foot="open-case"]');
  if(!foot||!document.body.classList.contains('live-doc-open'))return;
  e.preventDefault();e.stopImmediatePropagation();
  window.open('/data-explorer?tab=search&case_id='+encodeURIComponent(foot.dataset.mkArg),'_blank','noopener');
},true);
const previousClose=closeDecisionReader;
closeDecisionReader=function(){
  previousClose.apply(this,arguments);
  if(!document.body.classList.contains('live-doc-open'))return;
  document.body.classList.remove('live-doc-open');clearTools();
  $('searchPanel').hidden=true;panel.hidden=false;
  const back=$('caseReaderPanel').querySelector('.return-to-results');if(back)back.innerHTML='&larr; Back to case results';
};
refresh();
})();
</script>
'''


def _replace_once(html: str, old: str, new: str) -> str:
	if html.count(old) != 1:
		raise RuntimeError(f"live analysis page: expected one occurrence of {old[:60]!r}, found {html.count(old)}")
	return html.replace(old, new, 1)


def live_analysis_page_html() -> str:
	html = data_explorer_page_html(pitch_navigation=False)
	html = _replace_once(
		html,
		'<span class="tab tab-coming-soon" data-nav-group="workbench" aria-disabled="true" title="Live Analysis is coming soon" hidden>Live Analysis</span>',
		'<button class="tab" type="button" data-nav-group="workbench" data-tab="live-analysis" aria-pressed="false" aria-controls="liveAnalysisPanel" hidden>Live Analysis</button>',
	)
	html = _replace_once(html, "workbench:'workbenchPanel',", "workbench:'workbenchPanel','live-analysis':'liveAnalysisPanel',")
	html = _replace_once(html, "workbench:['workbench'],", "workbench:['workbench','live-analysis'],")
	# This page opens on its own view; the research page's default is Case search.
	html = _replace_once(
		html,
		"activateResearchTab(params.get('tab')||(researchGroups[group]?lastGroupTabs[group]:'search'),false)",
		"activateResearchTab(params.get('tab')||(researchGroups[group]?lastGroupTabs[group]:'live-analysis'),false)",
	)
	html = _replace_once(html, '<section id="caseReaderPanel"', PANEL_HTML + '<section id="caseReaderPanel"')
	# This page reads your document in markup mode, so the paused-markup lock on the case reader is lifted here.
	html = _replace_once(html, ' data-coming-soon disabled aria-disabled="true" title="Markup mode is coming soon"', ' title="Markup mode: the decision with notes in the margin"')
	html = _replace_once(html, "<title>Immigration Litigation Intelligence Tool | iLIT</title>", "<title>Live Analysis | iLIT</title>")
	html = html.replace("</head>", STYLE + "</head>", 1)
	return html.replace("</body>", SCRIPT + "</body>", 1)
