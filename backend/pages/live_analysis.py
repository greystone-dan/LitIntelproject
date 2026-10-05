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
body.live-doc-open [data-side-tab="about"],body.live-doc-open [data-side-tab="structure"],body.live-doc-open [data-side-tab="tags"],body.live-doc-open [data-mk-act="export"],body.live-doc-open #readerViewToggle,body.live-doc-open #readerCompareLink,body.live-doc-open #readerCopyCite,body.live-doc-open #readerFormatToggle,body.live-doc-open #readerPrintCitation{display:none!important}
</style>
'''

SCRIPT = r'''<script>
/* Live Analysis: send the document to /live-analysis/reader, then show the reader's markup view over the result. */
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
function open(data){
  const reader=$('caseReaderPanel');
  document.body.classList.add('live-doc-open');
  readerState.caseId=null;readerState.payload={item:data.item,citations:data.citations,readerData:data.readerData};readerState.formatted=true;readerState.mode='normalized';
  $('decisionTitle').textContent=data.filename;
  const s=data.summary||{};
  $('decisionEyebrow').textContent='Your document · read in memory, not stored';
  $('decisionMeta').innerHTML=[`${s.paragraphs} paragraphs`,`${s.case_citations} case citation${s.case_citations===1?'':'s'} (${s.resolved_case_citations} in the library)`,`${s.statute_references} statute reference${s.statute_references===1?'':'s'}`].map(v=>`<span class="meta-pill">${v}</span>`).join('');
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
  document.body.classList.remove('live-doc-open');
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
	html = data_explorer_page_html()
	html = _replace_once(
		html,
		'<a class="tab" data-nav-group="workbench" href="/live-analysis" hidden>Live Analysis</a>',
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
	html = _replace_once(html, "<title>Immigration Litigation Intelligence Tool | iLIT</title>", "<title>Live Analysis | iLIT</title>")
	html = html.replace("</head>", STYLE + "</head>", 1)
	return html.replace("</body>", SCRIPT + "</body>", 1)
