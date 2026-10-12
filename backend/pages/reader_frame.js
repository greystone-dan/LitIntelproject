/* Stored layers in the formatted reader (preview, Experimental only). Above the decision: the case summary card (parties,
   earlier decisions, issues, main arguments, challenged finding), a card with how the court decided each issue (result, a
   jump link to the paragraph, "check this" markers), and a bar that shows or hides a one-line note under each paragraph.
   Stored decisions only: /cases/{id}/case-frame (off unless CASELIBRARY_CASE_FRAME_ENABLED=1), /issue-map and
   /paragraph-notes return stored data and say available:false when a decision has none. Nothing is fetched or drawn
   while Experimental is off. No model is called here. */
(function(){
 'use strict';
 const body=document.getElementById('decisionBody');
 if(!body||typeof readerState==='undefined')return;
 const E=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const fr={cache:new Map(),loading:new Set(),timer:0,busy:false,open:false,all:false};
 const link=p=>{const n=Number(p);return n>0?` <a href="#" class="frame-para" data-frame-go="${n}">[${n}]</a>`:'';};

 const experimental=()=>typeof experimentalState!=='undefined'&&!!experimentalState.on;
 const NOTES_KEY='ilit.notes.on';
 const noteStore={get(){try{return window.localStorage.getItem(NOTES_KEY)!=='0';}catch(e){return true;}},set(on){try{window.localStorage.setItem(NOTES_KEY,on?'1':'0');}catch(e){}}};
 fr.notesOn=noteStore.get();fr.issuesOpen=false;
 const ROUTES={frame:'case-frame',issues:'issue-map',notes:'paragraph-notes'};
 /* Stored data for the open decision, or null while it loads. Fetched only when Experimental is on. */
 function data(kind){
  const id=readerState.caseId;
  if(id==null||!readerState.payload||!experimental())return null;
  const key=kind+':'+id;
  if(fr.cache.has(key))return fr.cache.get(key);
  if(!fr.loading.has(key)){
   fr.loading.add(key);
   fetch('/cases/'+encodeURIComponent(id)+'/'+ROUTES[kind]).then(r=>r.ok?r.json():{available:false}).catch(()=>({available:false})).then(d=>{fr.loading.delete(key);fr.cache.set(key,d);schedule();});
  }
  return null;
 }

 function who(p,key){const name=p[key]||'';return name?E(name):'';}

 function card(d){
  const f=d.frame,p=f.parties||{};
  const mainArgs=side=>f.arguments.filter(a=>a.side===side&&(fr.all||a.main));
  const sideCount=side=>f.arguments.filter(a=>a.side===side).length;
  const argList=(side,title)=>{const rows=mainArgs(side);return '<div class="frame-col"><h4>'+title+'</h4>'+(rows.length?'<ul>'+rows.map(a=>'<li>'+E(a.text)+link(a.para)+'</li>').join('')+'</ul>':'<p class="frame-none">None reported in the decision.</p>')+'</div>';};
  const more=f.arguments.length>f.arguments.filter(a=>a.main).length;
  let h='<details class="frame-card" data-frame-card'+(fr.open?' open':'')+'><summary>Case summary <span class="frame-tag">preview</span></summary>';
  h+='<p class="frame-note">'+E(d.note||'')+'</p>';
  if(f.subject)h+='<p class="frame-subject">'+E(f.subject)+'</p>';
  h+='<p class="frame-parties"><strong>Applicant:</strong> '+(who(p,'applicant')||'not stated')+'<br><strong>Respondent:</strong> '+(who(p,'respondent')||'not stated')+'</p>';
  if(d.result&&d.result.text)h+='<p class="frame-result"><strong>Result:</strong> '+E(d.result.text)+' <span class="frame-rel">('+E(d.result.reliability||'')+'. '+E(d.result.source||'')+')</span></p>';
  if(f.levels.length)h+='<h4>Earlier decisions</h4><ol class="frame-levels">'+f.levels.map(l=>'<li>'+E(l.body||'')+(l.date?' ('+E(l.date)+')':'')+(l.outcome?': '+E(l.outcome):'')+link(l.para)+'</li>').join('')+'</ol>';
  if(f.issues.length)h+='<h4>Issues</h4><ul>'+f.issues.map(i=>'<li>'+E(i.text)+link(i.para)+'</li>').join('')+'</ul>';
  h+='<div class="frame-cols">'+argList('applicant','Applicant argues')+argList('respondent','Respondent argues')+'</div>';
  if(more)h+='<p><button type="button" class="frame-more" data-frame-more>'+(fr.all?'Show main arguments only':'Show all '+f.arguments.length+' arguments')+'</button></p>';
  if(f.challenged.length)h+='<h4>Earlier finding challenged</h4><ul>'+f.challenged.map(c=>'<li><strong>'+E(c.target||'')+':</strong> '+E(c.finding||'')+link(c.para)+'</li>').join('')+'</ul>';
  return h+'</details>';
 }

 const CHIP={allowed_for_applicant:['won','Applicant won'],dismissed_for_applicant:['lost','Applicant lost'],partly_allowed:['part','Partly won'],not_decided:['none','Not decided'],moot_or_procedural:['none','Moot or procedural']};

 function issuesCard(d){
  const rows=d.issues||[];
  const side=(title,text)=>text?'<div class="frame-col"><h4>'+title+'</h4><p>'+E(text)+'</p></div>':'';
  const item=i=>{
   const chip=CHIP[i.result]||['none',i.result_label||''];
   const where=Number(i.result_para)>0?link(i.result_para):'';
   const checks=(i.checks||[]).filter(c=>c.code!=='minister_applicant').map(c=>'<p class="iss-check"><span class="iss-check-tag">Check this</span> '+E(c.text)+'</p>').join('');
   const quote=i.quote?'<details class="iss-quote"><summary>The court\u2019s words</summary><blockquote>'+E(i.quote)+'</blockquote></details>':'';
   return '<li class="iss"><div class="iss-q">'+E(i.issue)+'</div><div class="iss-res"><span class="iss-chip iss-'+chip[0]+'" title="'+E(i.result_label||'')+'">'+E(chip[1])+'</span>'+(where?' <span class="iss-where">Stated at'+where+'</span>':'')+'</div>'
    +(i.applicant_position||i.respondent_position?'<div class="frame-cols iss-sides">'+side('Applicant says',i.applicant_position)+side('Respondent says',i.respondent_position)+'</div>':'')+quote+checks+'</li>';
  };
  const flagged=rows.filter(i=>(i.checks||[]).length).length;
  /* The Minister-brought warning applies to the whole decision, so it is said once at the top, not under every issue. */
  const mini=rows.map(i=>(i.checks||[]).find(c=>c.code==='minister_applicant')).find(Boolean);
  return '<details class="frame-card iss-card" data-issue-card'+(fr.issuesOpen?' open':'')+'><summary>How the court decided each issue <span class="frame-tag">preview</span>'+(flagged?' <span class="iss-check-tag">'+flagged+' to check</span>':'')+'</summary>'
   +'<p class="frame-note">'+E(d.note||'')+'</p>'+(mini?'<p class="iss-check"><span class="iss-check-tag">Check this</span> '+E(mini.text)+'</p>':'')+'<ol class="iss-list">'+rows.map(item).join('')+'</ol></details>';
 }

 function notesBar(d){
  const n=Object.keys(d.paragraphs||{}).length;
  return '<div class="pn-bar" data-notes-bar><button type="button" class="pn-switch" aria-pressed="'+fr.notesOn+'" data-notes-switch>'+(fr.notesOn?'Hide':'Show')+' paragraph notes</button>'
   +'<span class="pn-hint">'+n+' one-line notes <span class="frame-tag">preview</span></span>'
   +'<details class="pn-rely"><summary>How reliable are these?</summary><p>'+E(d.note||'')+'</p></details></div>';
 }

 function sync(){
  fr.busy=true;
  try{
   body.querySelectorAll('[data-frame-card],[data-issue-card],[data-notes-bar],[data-pn-note]').forEach(n=>n.remove());
   if(!experimental())return;
   const f=data('frame'),iss=data('issues'),nt=data('notes');
   let anchor=null;
   if(f&&f.available&&f.frame){body.insertAdjacentHTML('afterbegin',card(f));anchor=body.querySelector('[data-frame-card]');}
   if(iss&&iss.available&&iss.issues&&iss.issues.length){const h=issuesCard(iss);if(anchor)anchor.insertAdjacentHTML('afterend',h);else body.insertAdjacentHTML('afterbegin',h);anchor=body.querySelector('[data-issue-card]');}
   if(nt&&nt.available&&nt.paragraphs){
    const h=notesBar(nt);if(anchor)anchor.insertAdjacentHTML('afterend',h);else body.insertAdjacentHTML('afterbegin',h);
    if(fr.notesOn)body.querySelectorAll('.fmt-para[data-para]').forEach(p=>{const t=nt.paragraphs[String(p.dataset.para)];if(t)p.insertAdjacentHTML('afterend','<aside class="pn-note" data-pn-note><span class="pn-label">Note</span> '+E(t)+'</aside>');});
   }
  }finally{fr.busy=false;}
 }
 function schedule(){window.clearTimeout(fr.timer);fr.timer=window.setTimeout(sync,30);}

 body.addEventListener('click',ev=>{
  const go=ev.target.closest&&ev.target.closest('[data-frame-go]');
  if(go){ev.preventDefault();const t=body.querySelector('.fmt-para[data-para="'+String(go.dataset.frameGo).replace(/"/g,'')+'"]');if(t&&t.scrollIntoView)t.scrollIntoView({block:'center',behavior:'smooth'});return;}
  if(ev.target.closest&&ev.target.closest('[data-frame-more]')){fr.all=!fr.all;fr.open=true;sync();return;}
  if(ev.target.closest&&ev.target.closest('[data-notes-switch]')){fr.notesOn=!fr.notesOn;noteStore.set(fr.notesOn);sync();}
 });
 body.addEventListener('toggle',ev=>{
  if(!ev.target.matches)return;
  if(ev.target.matches('[data-frame-card]'))fr.open=ev.target.open;
  if(ev.target.matches('[data-issue-card]'))fr.issuesOpen=ev.target.open;
 },true);
 const OWN=['data-frame-card','data-issue-card','data-notes-bar','data-pn-note','data-pos-bar','data-pos-note'];
 new MutationObserver(muts=>{
  if(fr.busy)return;
  const real=muts.some(m=>[...m.addedNodes,...m.removedNodes].some(n=>!(n.nodeType===1&&OWN.some(a=>n.hasAttribute(a)))));
  if(real)schedule();
 }).observe(body,{childList:true});
 /* Experimental switched on or off: draw or clear. */
 new MutationObserver(schedule).observe(document.body,{attributes:true,attributeFilter:['class']});
 schedule();
})();
