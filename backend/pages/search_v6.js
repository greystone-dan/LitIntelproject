/* Case search page (see search_v6.css): floating search bar, Advanced filter panel, boxed result rows, Recent cases, Show more.
   Search stays lexical: nothing typed here is sent to any model. Wraps functions defined earlier on the page. */
(function(){
const panel=document.getElementById('searchPanel');
if(!panel)return;
const $=id=>document.getElementById(id);
const escHtml=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmtNum=value=>Number(value).toLocaleString('en-CA');
const PAGE=50;

/* keep the sticky offsets matched to the real height of the search bar */
const topBar=panel.querySelector('.sp-top');
function syncTopOffset(){if(topBar)panel.style.setProperty('--sp-top',topBar.offsetHeight+'px');}
syncTopOffset();window.addEventListener('resize',syncTopOffset);
if(window.ResizeObserver&&topBar)new ResizeObserver(syncTopOffset).observe(topBar);

/* result rows */
const outcomeOf=item=>{
 if(item.government_outcome==='won')return {cls:'gov',text:'Government won'};
 if(item.government_outcome==='lost')return {cls:'ind',text:'Individual won'};
 const result=String(item.decision_outcome||'').toLowerCase();
 if(result==='unclear'||result==='procedural')return {cls:'',text:'Unclear'};
 return {cls:'',text:item.decision_outcome?String(item.decision_outcome).replace(/^./,c=>c.toUpperCase()):''};
};
const courtClass=court=>['SCC','FCA','FC'].includes(court)?'ct-'+court:'ct-other';
/* stored case type (no AI); nothing is drawn for decisions without a label */
const typeBox=t=>{if(!t||!t.primary||!t.primary.label)return '';const text=t.primary.label+(t.primary.provision?` (${t.primary.provision})`:'');return `<div class="sp-boxes sp-typeline"><span class="sp-bx type" title="Case type, worked out from the statute provisions the decision discusses (no AI)">Case type: ${escHtml(text)}</span></div>`;};
window.professionalResultCard=function(item){
 const out=outcomeOf(item),known=item.cited_by_cases!==undefined&&item.cited_by_cases!==null,count=known?item.cited_by_cases:null;
 const people=[item.judge].filter(Boolean);
 const boxes=[item.citation?`<span class="sp-bx cit">${escHtml(item.citation)}</span>`:'',item.court?`<span class="sp-bx ct ${courtClass(item.court)}">${escHtml(item.court)}</span>`:'',item.date?`<span class="sp-bx">Decision date ${escHtml(item.date)}</span>`:'',...people.map(name=>`<span class="sp-bx">${escHtml(name)}</span>`)].filter(Boolean).join('');
 const cited=known?`Cited by <b>${fmtNum(count)}</b> ${count===1?'decision':'decisions'}<span class="sp-tip"><b>Cited by ${fmtNum(count)} ${count===1?'decision':'decisions'}</b>Other cases in the library that cite this one.</span>`:'Cited by …';
 const snippet=item.snippet&&typeof snippetHtml==='function'?`<p class="sp-snippet">${snippetHtml(item.snippet,window.__spQuery||'')}</p>`:'';
 return `<div class="rc-wrap"><button type="button" class="case-result sp-row" data-case-id="${item.case_id}" aria-label="Open ${escHtml(item.title||'decision')}"><div class="rc-main"><div class="sp-title-line">${escHtml(item.title||'Untitled decision')}</div><div class="sp-boxes">${boxes}</div>${typeBox(item.case_type)}${snippet}</div><div class="sp-out ${out.cls}">${out.text?`<i></i>${escHtml(out.text)}`:''}</div><div class="sp-cited">${cited}</div></button></div>`;
};

/* "14 decisions" instead of the long status sentence */
const baseSetStatus=window.setSearchStatus;
window.setSearchStatus=function(message,state){
 const match=/^Showing (\d[\d,]*) matching decisions?\./.exec(message||'');
 if(match){const n=match[1],query=($('searchQuery').value||'').trim();message=`${n} decision${n==='1'?'':'s'}${query?` for “${query}”`:''}`;}
 return baseSetStatus(message,state);
};

/* Show more: next page by offset, appended under the current rows */
const moreButton=$('searchMore');
let shown=0,lastValues=null;
function searchParams(values,offset){
 const params=new URLSearchParams();
 Object.entries(values).forEach(([key,value])=>{if(value)params.set(key,value)});
 params.set('facets','0');params.set('citation_stats','0');params.set('limit',String(PAGE));params.set('offset',String(offset));
 return params;
}
function afterSearch(){
 const rows=document.querySelectorAll('#searchResults .case-result').length;
 shown=rows;lastValues=searchValues();window.__spQuery=lastValues.query;
 rememberSearch(lastValues.query);
 if(moreButton){moreButton.hidden=rows<PAGE;moreButton.textContent=`Show ${PAGE} more`;}
}
/* Recent searches: kept in this browser only, shown on the Workbench home. */
function rememberSearch(query){
 const q=String(query||'').trim().slice(0,200);if(!q)return;
 try{const list=JSON.parse(localStorage.getItem('ilit_recent_searches')||'[]').filter(x=>x&&x.q&&x.q.toLowerCase()!==q.toLowerCase());
  list.unshift({q,at:new Date().toISOString()});localStorage.setItem('ilit_recent_searches',JSON.stringify(list.slice(0,20)));}catch(error){}
}
const baseRun=window.runProfessionalSearch;
window.runProfessionalSearch=async function(){
 if(moreButton)moreButton.hidden=true;
 const result=await baseRun.apply(this,arguments);
 afterSearch();
 return result;
};
moreButton?.addEventListener('click',async()=>{
 if(!lastValues)return;
 moreButton.disabled=true;moreButton.textContent='Loading…';
 try{
  const response=await fetch(`/analytics/search/cases?${searchParams(lastValues,shown)}`);
  if(!response.ok)throw new Error('failed');
  const data=await response.json(),results=data.results||[],box=$('searchResults');
  const holder=document.createElement('div');
  holder.innerHTML=results.map(item=>window.professionalResultCard(item)).join('');
  const start=box.children.length;
  [...holder.children].forEach(node=>box.appendChild(node));
  box.querySelectorAll('.case-result').forEach((button,index)=>{if(index>=start&&!button.dataset.bound){button.dataset.bound='1';button.addEventListener('click',()=>openDecision(Number(button.dataset.caseId)));}});
  shown+=results.length;
  moreButton.hidden=results.length<PAGE;
  if(results.length){
   const stats=await fetch(`/analytics/search/citation-stats?ids=${results.map(item=>item.case_id).join(',')}`).then(r=>r.ok?r.json():null).catch(()=>null);
   if(stats){results.forEach((item,i)=>{Object.assign(item,(stats.stats||{})[item.case_id]||{});const wrap=box.children[start+i];if(wrap){const cell=wrap.querySelector('.sp-cited');const fresh=document.createElement('div');fresh.innerHTML=window.professionalResultCard(item);cell.innerHTML=fresh.querySelector('.sp-cited').innerHTML;}});}
  }
 }catch(error){setSearchStatus('Could not load more decisions. Try again.','error');}
 moreButton.disabled=false;moreButton.textContent=`Show ${PAGE} more`;
});

/* Advanced opens and closes the left filter panel. Captured early so the older toggle/clear handlers never run. */
const advancedButton=$('toggleAdvancedSearch');
function setAdvanced(open){
 panel.classList.toggle('sp-adv',open);
 advancedButton.setAttribute('aria-expanded',String(open));
 advancedButton.textContent=open?'Hide advanced':'Advanced';
 syncTopOffset();
}
document.addEventListener('click',event=>{
 const target=event.target;
 if(!target.closest)return;
 if(target.closest('#toggleAdvancedSearch')){event.stopImmediatePropagation();event.stopPropagation();setAdvanced(!panel.classList.contains('sp-adv'));return;}
 if(target.closest('#clearSearch')){
  event.stopImmediatePropagation();event.stopPropagation();
  $('caseSearch').reset();$('advancedSearchOptions').reset();
  ['governmentOutcome','courtFilter','citesFilter','citesCaseId','tagSearch','tagFilter','decisionOutcome','judgeFilter','yearFilter'].forEach(id=>{const el=$(id);if(el)el.value='';});
  $('ministerFilter').value='';$('searchFullText').checked=false;$('searchSort').value='newest';$('quickSort').value='newest';
  if(window.__pickReset)window.__pickReset();
  $('searchResults').innerHTML='';if(moreButton)moreButton.hidden=true;
  setSearchStatus('Search by case name or citation, or press Recent cases to see the newest decisions.');
  if(typeof qfSync==='function')qfSync();if(typeof updateSearchFilterSummary==='function')updateSearchFilterSummary();
  return;
 }
},true);
$('advancedSearchOptions').addEventListener('submit',event=>{event.preventDefault();$('caseSearch').requestSubmit();});
$('applyFilters')?.addEventListener('click',event=>{event.preventDefault();$('caseSearch').requestSubmit();});

/* Advanced: pick the case that is cited (Cases citing) and pick tags (Tag). Stored data only, no AI. */
(function(){
 const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const fire=()=>document.getElementById('advancedSearchOptions')?.dispatchEvent(new Event('input',{bubbles:true}));
 const debounce=(fn,ms)=>{let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>fn(...a),ms)}};
 const citesInput=$('citesFilter'),citesId=$('citesCaseId'),citesList=$('citesPickList'),citesNote=$('citesPickNote');
 const tagInput=$('tagSearch'),tagHidden=$('tagFilter'),tagList=$('tagPickList'),tagChips=$('tagChips');
 if(!citesInput||!tagInput)return;
 let picked=[],citeGen=0;
 const closeList=l=>{l.hidden=true;l.innerHTML=''};
 function showPicked(item){
  citesId.value=item?String(item.case_id):'';
  citesNote.hidden=!item;
  citesNote.innerHTML=item?'Showing cases that cite '+esc(item.title)+(item.citation?' ('+esc(item.citation)+')':'')+' <button type="button" class="sp-x" id="citesClear" aria-label="Remove this filter">&times;</button>':'';
  fire();
 }
 citesInput.addEventListener('input',()=>{
  if(citesId.value){citesId.value='';citesNote.hidden=true;fire();}
  lookup();
 });
 const lookup=debounce(async()=>{
  const q=citesInput.value.trim(),gen=++citeGen;
  if(q.length<2){closeList(citesList);return}
  try{
   const r=await fetch('/analytics/search/cases?'+new URLSearchParams({query:q,limit:'6',sort_by:'relevance',facets:'0',citation_stats:'0'}));
   if(!r.ok||gen!==citeGen)return;
   const rows=((await r.json()).results||[]).slice(0,6);
   citesList.innerHTML=rows.map(x=>'<button type="button" data-id="'+x.case_id+'"><b>'+esc(x.title)+'</b><span>'+esc([x.citation,x.court].filter(Boolean).join(' · '))+'</span></button>').join('')||'<div class="sp-pick-empty">No matching cases</div>';
   citesList.hidden=false;
   citesList._rows=rows;
  }catch(e){}
 },220);
 citesList.addEventListener('click',e=>{
  const b=e.target.closest('button[data-id]');if(!b)return;
  const item=(citesList._rows||[]).find(x=>String(x.case_id)===b.dataset.id);if(!item)return;
  citesInput.value=item.title;closeList(citesList);showPicked(item);
 });
 citesNote.addEventListener('click',e=>{if(e.target.closest('#citesClear')){citesInput.value='';showPicked(null);}});
 function paintTags(){
  tagHidden.value=picked.map(t=>t.value).join(',');
  tagChips.innerHTML=picked.map(t=>'<span class="sp-tag">'+esc(t.label)+' <button type="button" data-v="'+esc(t.value)+'" aria-label="Remove tag '+esc(t.label)+'">&times;</button></span>').join('');
  fire();
 }
 const lookupTags=debounce(async()=>{
  const q=tagInput.value.trim();
  try{
   const r=await fetch('/analytics/search/tags?'+new URLSearchParams({q,limit:'10'}));
   if(!r.ok||q!==tagInput.value.trim())return;
   const rows=((await r.json()).tags||[]).filter(t=>!picked.some(p=>p.value===t.value));
   tagList._rows=rows;
   tagList.innerHTML=rows.map(t=>'<button type="button" data-v="'+esc(t.value)+'"><b>'+esc(t.label)+'</b><span>'+Number(t.count).toLocaleString()+' cases'+(t.category?' · '+esc(String(t.category).replace(/_/g,' ')):'')+'</span></button>').join('')||'<div class="sp-pick-empty">No matching tags</div>';
   tagList.hidden=false;
  }catch(e){}
 },200);
 tagInput.addEventListener('input',lookupTags);
 tagInput.addEventListener('focus',lookupTags);
 tagList.addEventListener('click',e=>{
  const b=e.target.closest('button[data-v]');if(!b)return;
  const t=(tagList._rows||[]).find(x=>x.value===b.dataset.v);
  if(t&&picked.length<5){picked.push(t);tagInput.value='';closeList(tagList);paintTags();}
 });
 tagChips.addEventListener('click',e=>{
  const b=e.target.closest('button[data-v]');if(!b)return;
  picked=picked.filter(t=>t.value!==b.dataset.v);paintTags();
 });
 document.addEventListener('click',e=>{if(!e.target.closest('.sp-pick')){closeList(citesList);closeList(tagList);}});
 window.__pickReset=()=>{picked=[];paintTags();citesNote.hidden=true;closeList(citesList);closeList(tagList);};
})();

/* Recent cases: newest decisions first, current filters kept */
$('recentCases')?.addEventListener('click',()=>{
 $('searchQuery').value='';window.__sortChosen=true;
 $('searchSort').value='newest';if($('quickSort'))$('quickSort').value='newest';
 $('caseSearch').requestSubmit();
});

/* Most cited: cases cited by the most other cases, current filters kept */
$('mostCitedCases')?.addEventListener('click',()=>{
 $('searchQuery').value='';window.__sortChosen=true;
 $('searchSort').value='most_cited';if($('quickSort'))$('quickSort').value='most_cited';
 $('caseSearch').requestSubmit();
});

setSearchStatus('Search by case name or citation, or press Recent cases or Most cited.');
{ /* ?q= opens the search with that text (Workbench recent searches link here) */
 const wanted=new URLSearchParams(location.search).get('q');
 if(wanted&&!$('searchQuery').value){$('searchQuery').value=wanted;setTimeout(()=>$('caseSearch').requestSubmit(),0);}
}
})();
