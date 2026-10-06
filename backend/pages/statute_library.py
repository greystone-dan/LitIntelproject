"""Browser page for the section-level statute library."""


def statute_library_page_html() -> str:
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Statute Library | iLit</title>
<style>
:root{--ink:#14212b;--muted:#63707a;--paper:#f6f4ee;--panel:#fffdfa;--line:#d9d5ca;--accent:#285d75}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:15px/1.5 system-ui,sans-serif}
main{max-width:1240px;margin:auto;padding:24px 18px 56px}h1{font:normal 30px Georgia,serif;margin:6px 0}
.muted{color:var(--muted)}a{color:var(--accent)}.bar{display:flex;gap:12px;flex-wrap:wrap;align-items:end;margin:16px 0}
select,input,button{font:inherit;padding:8px 10px;border:1px solid #b9b5aa;border-radius:4px;background:#fff}
button{background:var(--accent);color:#fff;border:0;cursor:pointer}button[disabled]{opacity:.45;cursor:default}
.grid{display:grid;grid-template-columns:minmax(260px,380px) 1fr;gap:18px;align-items:start}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:14px}
.toc{max-height:78vh;overflow:auto;padding:0}.toc button.row{display:grid;grid-template-columns:54px 1fr 54px;gap:8px;width:100%;text-align:left;background:none;color:inherit;border:0;border-bottom:1px solid #eee9dd;border-radius:0;padding:8px 10px}
.toc button.row:hover,.toc button.row.on{background:#eaf1f4}.toc .n{font-weight:700;color:var(--accent)}.toc .c{text-align:right;font-variant-numeric:tabular-nums}.toc .zero{opacity:.45}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin:12px 0}
.stats h3{font-size:14px;margin:0 0 6px}.line{display:grid;grid-template-columns:1fr 46px;gap:6px;font-size:13px;margin:2px 0}
.meter{height:6px;background:#e5e1d8;border-radius:3px;margin-bottom:3px}.meter i{display:block;height:100%;background:var(--accent);border-radius:3px}
.sectiontext{white-space:pre-wrap;max-height:260px;overflow:auto;border-left:3px solid var(--accent);padding:6px 12px;background:#fff;font:14px/1.55 Georgia,serif}
table{border-collapse:collapse;width:100%}th,td{text-align:left;padding:8px;border-bottom:1px solid #e5e1d8;vertical-align:top;font-size:14px}th{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}
.pager{display:flex;justify-content:space-between;align-items:center;margin-top:10px}.error{padding:10px;background:#fff0ed;color:#8d3021;border-left:4px solid #b44734}
@media(max-width:820px){.grid{grid-template-columns:1fr}.toc{max-height:300px}}
</style></head><body><main>
<a href="/">&larr; iLit</a>
<h1>Statute Library</h1>
<p class="muted">Pick a section to read it and see every decision in the library that cites it, by year, court and outcome. Counts are distinct decisions with a stored reference; they are descriptive, not a measure of legal effect. Statute text is an unofficial Justice Laws consolidation. Counts for decimal sections such as 18.1 or 25.1 are currently included in the base section (18, 25) until the references are re-extracted.</p>
<div class="bar"><label>Act<br><select id="act"></select></label><label>Find a section<br><input id="find" placeholder="e.g. 34 or inadmissibility"></label>
<label><input type="checkbox" id="onlycited" checked> only sections cited in decisions</label></div>
<div id="msg" aria-live="polite"></div>
<div class="grid"><div class="panel toc" id="toc"><p class="muted" style="padding:10px">Loading&hellip;</p></div><div id="detail"><div class="panel muted">Select a section on the left.</div></div></div>
<script>
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const $=id=>document.getElementById(id);
let toc=null,state={act:null,section:null,page:1};
const qs=new URLSearchParams(location.search);
async function api(url){const r=await fetch(url),d=await r.json();if(!r.ok)throw new Error(d.detail||'Request failed');return d}
function fail(e){$('msg').innerHTML=`<div class="error">${esc(e.message)}</div>`}
async function init(){try{const acts=await api('/api/statute-library/acts');
$('act').innerHTML=acts.map(a=>`<option value="${esc(a.instrument_key)}">${esc(a.title)} (${a.case_count.toLocaleString()} decisions)</option>`).join('');
const want=qs.get('act');if(want&&acts.some(a=>a.instrument_key===want))$('act').value=want;else if(acts.some(a=>a.instrument_key==='canada.irpa'))$('act').value='canada.irpa';
await loadToc();if(qs.get('section'))openSection(qs.get('section'))}catch(e){fail(e)}}
async function loadToc(){$('msg').innerHTML='';state.act=$('act').value;$('toc').innerHTML='<p class="muted" style="padding:10px">Loading&hellip;</p>';
try{toc=await api(`/api/statute-library/${encodeURIComponent(state.act)}/sections`);renderToc()}catch(e){fail(e)}}
function renderToc(){if(!toc)return;const q=$('find').value.trim().toLowerCase(),only=$('onlycited').checked;
const rows=toc.sections.concat(toc.cited_without_text||[]).filter(s=>(!only||s.case_count>0)&&(!q||String(s.section).toLowerCase().startsWith(q)||String(s.label||'').toLowerCase().includes(q)));
$('toc').innerHTML=rows.length?rows.map(s=>`<button class="row${s.section===state.section?' on':''}" data-s="${esc(s.section)}"><span class="n">${esc(s.section)}</span><span class="${s.case_count?'':'zero'}">${esc(s.label||(s.no_text?'(no text indexed)':''))}</span><span class="c">${s.case_count.toLocaleString()}</span></button>`).join(''):'<p class="muted" style="padding:10px">No sections match.</p>'}
function lines(rows,label,total){return `<div class="panel"><h3>${label}</h3>${rows.length?rows.map(r=>`<div><div class="line"><span>${esc(r.value)}</span><span>${r.decision_count}</span></div><div class="meter"><i style="width:${total?Math.max(2,Math.round(r.decision_count*100/total)):0}%"></i></div></div>`).join(''):'<span class="muted">None</span>'}</div>`}
async function openSection(section,page=1){state.section=section;state.page=page;renderToc();
history.replaceState(null,'',`?act=${encodeURIComponent(state.act)}&section=${encodeURIComponent(section)}`);
$('detail').innerHTML='<div class="panel muted">Loading&hellip;</div>';
try{const d=await api(`/api/statute-library/${encodeURIComponent(state.act)}/sections/${encodeURIComponent(section)}?page=${page}&page_size=25`);const t=d.summary.decision_count;
const rows=d.decisions.map(x=>`<tr><td><a href="/case-reader-ui/${encodeURIComponent(x.case_id)}">${esc(x.title||x.citation||'Decision')}</a><br><small class="muted">${esc(x.citation||'')}</small></td><td>${esc(x.court)}</td><td>${esc(x.date||'')}</td><td>${esc(x.outcome)}</td><td>${x.reference_count}</td></tr>`).join('');
$('detail').innerHTML=`<div class="panel"><h2 style="margin:0 0 4px">${esc(d.act.title)} s.&nbsp;${esc(d.section.number)}${d.section.label?` <span class="muted">&mdash; ${esc(d.section.label)}</span>`:''}</h2>
<p class="muted" style="margin:0 0 8px"><strong>${t.toLocaleString()}</strong> decision${t===1?'':'s'} cite this section (${d.summary.reference_occurrences.toLocaleString()} references).</p>${/^\d+$/.test(d.section.number)?'<small class="muted">Includes references to decimal sections of the same number (for example 18.1) until re-extraction.</small>':''}
${d.section.text_available?`<div class="sectiontext">${esc(d.section.text)}</div><small class="muted">${esc(d.section.text_note)}</small>`:'<p class="muted">No statute text is indexed for this section.</p>'}</div>
<div class="stats">${lines(d.by_provision,'By subsection / paragraph',t)}${lines(d.by_year,'By year',t)}${lines(d.by_court,'By court',t)}${lines(d.by_outcome,'Decision outcomes',t)}</div>
<div class="panel"><h3>Decisions</h3><p class="muted" style="margin-top:0">Most references in the decision first, then most recent.</p><div style="overflow:auto"><table><thead><tr><th>Decision</th><th>Court</th><th>Date</th><th>Outcome</th><th>Refs</th></tr></thead><tbody>${rows||'<tr><td colspan="5" class="muted">No decisions.</td></tr>'}</tbody></table></div>
<div class="pager"><button ${d.pagination.page<=1?'disabled':''} onclick="openSection(state.section,${d.pagination.page-1})">Previous</button><span>Page ${d.pagination.page} of ${d.pagination.total_pages}</span><button ${d.pagination.page>=d.pagination.total_pages?'disabled':''} onclick="openSection(state.section,${d.pagination.page+1})">Next</button></div></div>`;
}catch(e){$('detail').innerHTML=`<div class="error">${esc(e.message)}</div>`}}
$('toc').addEventListener('click',e=>{const b=e.target.closest('button.row');if(b)openSection(b.dataset.s)});
$('act').addEventListener('change',()=>{state.section=null;$('detail').innerHTML='<div class="panel muted">Select a section on the left.</div>';loadToc()});
$('find').addEventListener('input',renderToc);$('onlycited').addEventListener('change',renderToc);init();
</script></main></body></html>"""
