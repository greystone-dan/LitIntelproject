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

 /* Guard: the stored data can name paragraph numbers the decision does not have (bracketed numbers inside quotations).
    Tags are drawn only on paragraphs in the page (fmt-para[data-para]) and the colour legend counts only those.
   The data for whatever is open now: {available, mode, notice, paragraphs} or null while it loads. */
 function current(){
  const payload=readerState.payload;if(!payload)return {none:true};
  const live=payload.readerData&&payload.readerData.position_tags;
  if(readerState.caseId==null)return live?(live.available?live:{unavailable:true,empty_note:live.empty_note||''}):{none:true};
  const id=readerState.caseId;
  if(pos.cache.has(id))return pos.cache.get(id);
  if(!pos.loading.has(id)){
   pos.loading.add(id);
   fetch('/cases/'+encodeURIComponent(id)+'/paragraph-positions').then(r=>r.ok?r.json():{available:false}).catch(()=>({available:false})).then(data=>{
    pos.loading.delete(id);pos.cache.set(id,data&&data.available?data:{unavailable:true,empty_note:(data&&data.empty_note)||'Not tagged yet. Whose-position tags are prepared ahead of time for a growing set of decisions, and this one is not in it yet.'});schedule();});
  }
  return null;
 }

 /* What kind of document is open, and where a dissent begins. Read from the text on the page, so it works the same
    for stored decisions and Live Analysis documents. */
 function docInfo(){
  const payload=readerState.payload||{},item=payload.item||(payload.readerData&&payload.readerData.case)||{};
  const head=String(item.full_text||'').slice(0,3000);
  const memo=/memorandum of (?:argument|fact and law)|\bfactum\b|written (?:submissions|representations)|m[ée]moire des faits et du droit/i.test(head)
   &&!/reasons for (?:judgment|order|decision)|judgment and reasons|order and reasons|reasons and decision|motifs/i.test(head);
  let start=null,kind='';
  body.querySelectorAll('.fmt-heading,.fmt-doctitle,.fmt-role').forEach(h=>{
   if(start)return;const t=(h.textContent||'').trim();
   if(/dissent|dissidents?\b/i.test(t)&&t.length<160){start=h;kind='dissent';}
   else if(/^concurring\b|^motifs concordants/i.test(t)&&t.length<160){start=h;kind='concurrence';}
  });
  return {memo,start,kind,title:start?(start.textContent||'').trim().slice(0,90):''};
 }
 /* Wording by forum. The stored layer and holder names were written for a court reviewing an earlier decision. In a
    tribunal decision (RPD, RAD, IAD, ID) there is no "Court" and nobody argues "to the Court", so the words change. */
 function forum(){
  const payload=readerState.payload||{},item=payload.item||(payload.readerData&&payload.readerData.case)||{};
  const c=String(item.court||'');
  if(/refugee appeal|\brad\b/i.test(c))return 'rad';
  if(/refugee protection|\brpd\b|immigration (?:appeal )?division|\biad\b/i.test(c)||/^(?:id|iad)$/i.test(c.trim()))return 'tribunal';
  return 'court';
 }
 const WORDS={
  court:{},
  tribunal:{court:'The Member',layer:{judge:'Member’s evaluation',jr_party:'Position put to the Member',earlier_decision:'Earlier decision',first_instance:'Position reported in the earlier decision'},help:{court:'The Member writing this decision: facts found, reasoning and the ruling.'}},
  rad:{court:'The Member',layer:{judge:'Member’s evaluation',jr_party:'Position put on the appeal',earlier_decision:'The RPD decision under appeal',first_instance:'Position reported in the RPD decision'},help:{court:'The Member writing this decision: facts found, reasoning and the ruling.',earlier_decision_maker:'The Refugee Protection Division member whose decision is being appealed.'}}
 };
 function words(){return WORDS[forum()]||WORDS.court;}
 function layerLabel(lay){const w=words();return (w.layer&&w.layer[lay.key])||lay.label;}
 function posLabel(p){const w=words();return p.key==='court'&&w.court?w.court:p.label;}
 function afterStart(info,el){return !!(info.start&&el&&(info.start.compareDocumentPosition(el)&Node.DOCUMENT_POSITION_FOLLOWING));}

 function legendHtml(data,present,framework,minority){
  const w=words(),items=(data.legend_items||[]).filter(i=>present.has(i.key)).map(i=>'<li><span class="pos-chip pos-'+E(i.key)+'">'+E(i.key==='court'&&w.court?w.court:i.label)+'</span><span class="pos-help">'+E((w.help&&w.help[i.key])||i.help)+'</span></li>');
  if(framework)items.push('<li><span class="pos-chip pos-framework">'+E(data.framework_label||'Law and tests')+'</span><span class="pos-help">'+E(data.framework_note||'')+'</span></li>');
  if(minority)items.push('<li><span class="pos-chip pos-dissent">'+E(minority)+'</span><span class="pos-help">A judge who disagreed with the majority. This is not the Court’s holding.</span></li>');
  return '<details class="pos-legend-box" open><summary>What the colours mean</summary><ul class="pos-legend-list">'+items.join('')+'</ul></details>';
 }
 function levels(data){
  return '<details class="pos-levels"><summary>How the indents work</summary><p>'+E(data.legend||'')+'</p></details>';
 }
 function overview(data,info){
  const rows=(data.overview||[]).filter(r=>!(info.memo&&r.key==='court'));
  if(!rows.length)return '';
  return '<div class="pos-glance"><div class="pos-glance-h">At a glance'+(data.mode==='rules'?' (first cue phrase in each voice)':'')+'</div>'
   +rows.map(r=>'<div class="pos-g pos-b-'+E(r.key)+'"><span class="pos-g-l">'+E(words().court?r.label.replace(/judge/i,'Member'):r.label)+'</span><span class="pos-g-t">'+E(r.text)+'</span>'
    +'<button type="button" class="pos-g-go" data-pos-go="'+E(r.para)+'" aria-label="Go to paragraph '+E(r.para)+'">¶'+E(r.para)+'</button></div>').join('')+'</div>';
 }
 function markers(info){
  let h='';
  if(info.memo)h+='<p class="pos-flag pos-flag-memo"><b>A party’s memorandum, not a decision.</b> No judge has ruled here. Everything below is one side’s argument.</p>';
  if(info.kind==='dissent')h+='<p class="pos-flag pos-flag-dissent"><b>This decision has a dissent.</b> Text from “'+E(info.title)+'” on is the dissenting judge’s view, not the majority’s ruling, and is marked as such below.</p>';
  if(info.kind==='concurrence')h+='<p class="pos-flag pos-flag-dissent"><b>This decision has separate concurring reasons.</b> Text from “'+E(info.title)+'” on is a judge agreeing in the result but for different reasons.</p>';
  return h;
 }
 function reliability(data){
  return '<details class="pos-rely"><summary><span class="pos-badge">Preview</span> How reliable are these tags?</summary><p>'+E((data.reliability||data.notice||'').replace(/^How reliable are these tags\?\s*/,''))+'</p></details>';
 }

 function bar(data){
  const el=document.createElement('div');el.className='pos-bar';el.setAttribute('data-pos-bar','');
  const info=docInfo();
  if(data.unavailable){
   el.classList.add('is-empty');
   el.innerHTML='<div class="pos-top"><span class="pos-title">Whose position</span><span class="pos-badge pos-badge-empty">Not tagged yet</span></div><p class="pos-notice">'+E(data.empty_note||'')+'</p>'+markers(info);
   return el;
  }
  const real=new Set([...body.querySelectorAll('.fmt-para[data-para]')].map(p=>String(p.dataset.para))),shown=Object.entries(data.paragraphs).filter(([n])=>real.has(n)).map(([,row])=>row),present=new Set();shown.forEach(row=>row.positions.forEach(p=>present.add(p.key)));
  const framework=shown.some(r=>r.framework==='yes');
  let minority='';
  if(info.start){minority=info.kind==='dissent'?'Dissenting judge':'Concurring judge';}
  el.innerHTML='<div class="pos-top"><button type="button" class="pos-switch" aria-pressed="'+pos.on+'" data-pos-switch>'+(pos.on?'Hide':'Show')+' whose position</button>'
   +'<span class="pos-hint">'+(pos.on?'Each paragraph is labelled with who is speaking.':(data.mode==='rules'?'Labels paragraphs from cue phrases in the text.':'Labels each paragraph: the judge, each side, or the earlier decision-maker.'))+'</span></div>'
   +markers(info)+overview(data,info)
   +(pos.on?legendHtml(data,present,framework,minority)+levels(data):'')
   +reliability(data);
  return el;
 }

 function note(row,mode,minority){
  const lead=row.positions[0].key,mino=minority&&lead==='court';
  const chips=row.positions.map((p,i)=>'<span class="pos-chip pos-'+E(i===0&&mino?'dissent':p.key)+'">'+E(i===0&&mino?minority:posLabel(p))+'</span>').join('')+(row.framework==='yes'?'<span class="pos-chip pos-framework">Law and tests</span>':'');
  const kinds=row.kinds&&row.kinds.length?'<span class="pos-kinds">'+E(row.kinds.slice(0,2).join(' · '))+'</span>':'';
  const text=mode==='rules'?(row.cue?'<span class="pos-cue">Cue: “'+E(row.cue)+'”</span>':''):(row.summary?'<span class="pos-sum">'+E(row.summary)+'</span>':'');
  const lay=row.layer||{key:'unknown',label:'Level not yet detected',depth:null},depth=lay.depth==null?'u':lay.depth;
  const layer='<span class="pos-layer'+(lay.detected===false?' is-unknown':'')+'">'+E(layerLabel(lay))+'</span>';
  return '<aside class="pos-note pos-d'+depth+' pos-b-'+E(mino?'dissent':lead)+'" data-pos-note data-pos-layer="'+E(lay.key)+'">'+layer+'<span class="pos-tags">'+chips+kinds+'</span>'+text+'<span class="pos-cites" data-pos-cites hidden></span></aside>';
 }

 function sync(){
  if(pos.busy)return;pos.busy=true;
  try{
   body.querySelectorAll('[data-pos-bar],[data-pos-note]').forEach(n=>n.remove());
   const data=current();
   if(!data||data.none)return;
   if(!data.unavailable&&!data.paragraphs)return;
   body.insertBefore(bar(data),body.firstChild);
   if(!pos.on)return;
   if(data.unavailable)return;
   const info=docInfo(),minority=info.start?(info.kind==='dissent'?'Dissenting judge':'Concurring judge'):'';
   body.querySelectorAll('.fmt-para[data-para]').forEach(p=>{const row=data.paragraphs[String(p.dataset.para)];if(row)p.insertAdjacentHTML('afterend',note(row,data.mode,afterStart(info,p)?minority:''));});
  }finally{pos.busy=false;}
 }
 function schedule(){window.clearTimeout(pos.timer);pos.timer=window.setTimeout(sync,30);}

 body.addEventListener('click',ev=>{
  const go=ev.target.closest&&ev.target.closest('[data-pos-go]');
  if(go){const target=body.querySelector('.fmt-para[data-para="'+String(go.dataset.posGo).replace(/"/g,'')+'"]');if(target&&target.scrollIntoView)target.scrollIntoView({block:'center',behavior:'smooth'});return;}
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
