"""Standalone saved-search and recorded-alert page."""


def saved_searches_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Saved searches | iLIT</title>
<style>
body{margin:0;background:#f5f7fb;color:#102038;font:15px/1.5 "IBM Plex Sans","Segoe UI",sans-serif}
main{max-width:960px;margin:0 auto;padding:28px 18px}
header,.saved-search-head,.saved-search-actions{display:flex;align-items:center;justify-content:space-between;gap:12px}
header{margin-bottom:22px}h1,h2,p{margin-top:0}h1{font:600 30px/1.15 Georgia,serif}
a{color:#1e3a8a;font-weight:650}button{padding:8px 11px;border:1px solid #cbd5e1;border-radius:5px;background:#fff;color:#102038;font:inherit;cursor:pointer}
button:hover{border-color:#2563eb}button.danger{color:#991b1b}
.saved-search{margin:12px 0;padding:16px;border:1px solid #d8dee8;border-radius:8px;background:#fff}
.saved-search h2{margin:0;font-size:18px}.saved-search p{margin:6px 0;color:#526276}
.saved-search pre{max-height:150px;overflow:auto;padding:10px;background:#f8fafc;font-size:12px;white-space:pre-wrap}
.alert-list{margin-top:12px;padding-top:10px;border-top:1px solid #e2e8f0}
.alert-item{padding:8px 0;border-bottom:1px solid #edf0f4}.muted{color:#64748b}.status{min-height:24px;margin:10px 0;color:#526276}
@media(max-width:600px){header,.saved-search-head,.saved-search-actions{align-items:flex-start;flex-direction:column}}
</style>
</head>
<body>
<main>
<header><div><p><a href="/data-explorer">← Case Search</a></p><h1>Saved searches</h1><p class="muted">Review saved query criteria and check previously recorded case alerts.</p></div><button id="refreshSavedSearches" type="button">Refresh</button></header>
<p id="savedSearchStatus" class="status" role="status" aria-live="polite">Loading saved searches…</p>
<section id="savedSearchList" aria-label="Saved searches"></section>
</main>
<script>
const esc=value=>String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
async function loadSavedSearches(){
 const status=document.getElementById('savedSearchStatus'),list=document.getElementById('savedSearchList');
 status.textContent='Loading saved searches…';list.innerHTML='';
 try{
  const response=await fetch('/saved-searches');
  if(!response.ok)throw new Error(`Request failed (${response.status})`);
  const searches=await response.json();
  status.textContent=searches.length?`${searches.length} saved search${searches.length===1?'':'es'}.`:'No saved searches yet. Save a query from Case Search to begin.';
  list.innerHTML=searches.map(search=>`<article class="saved-search" data-search-id="${Number(search.id)}"><div class="saved-search-head"><div><h2>${esc(search.name)}</h2><p>${esc(search.query||'Filter-only search')} · ${Number(search.alert_count||0)} recorded alert${Number(search.alert_count||0)===1?'':'s'}</p></div><div class="saved-search-actions"><button type="button" data-check-search="${Number(search.id)}">Check alerts</button><button class="danger" type="button" data-delete-search="${Number(search.id)}">Delete</button></div></div><pre>${esc(JSON.stringify(search.filters||{},null,2))}</pre><div class="alert-list" data-alert-list="${Number(search.id)}" hidden></div></article>`).join('');
  list.querySelectorAll('[data-check-search]').forEach(button=>button.addEventListener('click',()=>checkSavedSearch(Number(button.dataset.checkSearch))));
  list.querySelectorAll('[data-delete-search]').forEach(button=>button.addEventListener('click',()=>deleteSavedSearch(Number(button.dataset.deleteSearch))));
 }catch(error){status.textContent=`Saved searches unavailable: ${error.message}`;}
}
async function checkSavedSearch(searchId){
 const status=document.getElementById('savedSearchStatus'),target=document.querySelector(`[data-alert-list="${searchId}"]`);
 status.textContent='Checking recorded alerts…';
 try{
  const response=await fetch(`/saved-searches/${searchId}/check`,{method:'POST'});
  if(!response.ok)throw new Error(`Request failed (${response.status})`);
  const digest=await response.json(),alerts=digest.new_case_matches||[];
  target.hidden=false;
  target.innerHTML=alerts.map(alert=>`<div class="alert-item"><strong>${esc(alert.case_title||`Case ${alert.case_id}`)}</strong><span>${alert.case_citation?` · ${esc(alert.case_citation)}`:''}${alert.case_date?` · ${esc(alert.case_date)}`:''}</span>${alert.chunk_text?`<p>${esc(alert.chunk_text)}</p>`:''}</div>`).join('')||'<p class="muted">No recorded case alerts.</p>';
  status.textContent=`${alerts.length} recorded alert${alerts.length===1?'':'s'} for ${esc(digest.search_name)}.`;
 }catch(error){status.textContent=`Alert check unavailable: ${error.message}`;}
}
async function deleteSavedSearch(searchId){
 if(!window.confirm('Delete this saved search and its recorded alerts?'))return;
 const response=await fetch(`/saved-searches/${searchId}`,{method:'DELETE'});
 if(!response.ok){document.getElementById('savedSearchStatus').textContent=`Delete failed (${response.status}).`;return;}
 await loadSavedSearches();
}
document.getElementById('refreshSavedSearches').addEventListener('click',loadSavedSearches);
loadSavedSearches();
</script>
</body>
</html>"""
