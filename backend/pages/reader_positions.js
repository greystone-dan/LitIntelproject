/* Whose-position tags in the formatted reader (preview). A switch above the decision shows, under each
   tagged paragraph, a coloured tag for whose position it reports and a one-line summary.
   Stored decisions: /cases/{id}/paragraph-positions (stored data). Live Analysis documents: the rules-only
   block that rides in the reader payload (readerData.position_tags). The same screen draws both.
   No model is called here. Each tagged paragraph keeps an empty slot (data-pos-cites) where citation use
   will attach later. */
(function(){
 'use strict';
 const body=document.getElementById('decisionBody');
 if(!body||typeof readerState==='undefined')return;
 const E=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const KEY='ilit.positions.on';
 const store={get(){try{return window.localStorage.getItem(KEY)==='1';}catch(e){return false;}},set(on){try{window.localStorage.setItem(KEY,on?'1':'0');}catch(e){}}};
 const pos={on:store.get(),cache:new Map(),loading:new Set(),timer:0,busy:false};
 const ORDER=['applicant','respondent','earlier_decision_maker','court','prior_court_or_authority','witness_or_document','other'];

 /* The data for whatever is open now: {available, mode, notice, paragraphs} or null while it loads. */
 function current(){
  const payload=readerState.payload;if(!payload)return {none:true};
  const live=payload.readerData&&payload.readerData.position_tags;
  if(readerState.caseId==null)return live&&live.available?live:{none:true};
  const id=readerState.caseId;
  if(pos.cache.has(id))return pos.cache.get(id);
  if(!pos.loading.has(id)){
   pos.loading.add(id);
   fetch('/cases/'+encodeURIComponent(id)+'/paragraph-positions').then(r=>r.ok?r.json():{available:false}).catch(()=>({available:false})).then(data=>{
    pos.loading.delete(id);pos.cache.set(id,data&&data.available?data:{none:true});schedule();});
  }
  return null;
 }

 function bar(data){
  const el=document.createElement('div');el.className='pos-bar';el.setAttribute('data-pos-bar','');
  const present=new Set();Object.values(data.paragraphs).forEach(row=>row.positions.forEach(p=>present.add(p.key)));
  const legend=ORDER.filter(k=>present.has(k)).map(k=>{const label=Object.values(data.paragraphs).flatMap(r=>r.positions).find(p=>p.key===k).label;return '<span class="pos-chip pos-'+E(k)+'">'+E(label)+'</span>';}).join('');
  el.innerHTML='<button type="button" class="pos-switch" aria-pressed="'+pos.on+'" data-pos-switch>'+(pos.on?'Hide':'Show')+' whose position</button>'
   +'<span class="pos-badge">Preview</span>'
   +(pos.on?'<span class="pos-legend" aria-label="Tag colours">'+legend+'</span><p class="pos-notice">'+E(data.notice||'')+'</p>':'<span class="pos-hint">'+(data.mode==='rules'?'Rule-based tags from cue phrases in the text':'Who is speaking in each paragraph, with a one-line summary')+'</span>');
  return el;
 }

 function note(row,mode){
  const lead=row.positions[0].key,chips=row.positions.map(p=>'<span class="pos-chip pos-'+E(p.key)+'">'+E(p.label)+'</span>').join('');
  const kinds=row.kinds&&row.kinds.length?'<span class="pos-kinds">'+E(row.kinds.slice(0,2).join(' · '))+'</span>':'';
  const text=mode==='rules'?(row.cue?'<span class="pos-cue">Cue: “'+E(row.cue)+'”</span>':''):(row.summary?'<span class="pos-sum">'+E(row.summary)+'</span>':'');
  return '<aside class="pos-note pos-b-'+E(lead)+'" data-pos-note><span class="pos-tags">'+chips+kinds+'</span>'+text+'<span class="pos-cites" data-pos-cites hidden></span></aside>';
 }

 function sync(){
  if(pos.busy)return;pos.busy=true;
  try{
   body.querySelectorAll('[data-pos-bar],[data-pos-note]').forEach(n=>n.remove());
   const data=current();
   if(!data||data.none||!data.paragraphs)return;
   body.insertBefore(bar(data),body.firstChild);
   if(!pos.on)return;
   body.querySelectorAll('.fmt-para[data-para]').forEach(p=>{const row=data.paragraphs[String(p.dataset.para)];if(row)p.insertAdjacentHTML('afterend',note(row,data.mode));});
  }finally{pos.busy=false;}
 }
 function schedule(){window.clearTimeout(pos.timer);pos.timer=window.setTimeout(sync,30);}

 body.addEventListener('click',ev=>{
  const button=ev.target.closest&&ev.target.closest('[data-pos-switch]');if(!button)return;
  pos.on=!pos.on;store.set(pos.on);sync();
 });
 new MutationObserver(muts=>{
  if(pos.busy)return;
  const real=muts.some(m=>[...m.addedNodes,...m.removedNodes].some(n=>!(n.nodeType===1&&(n.hasAttribute('data-pos-bar')||n.hasAttribute('data-pos-note')))));
  if(real)schedule();
 }).observe(body,{childList:true,subtree:true});
 schedule();
})();
