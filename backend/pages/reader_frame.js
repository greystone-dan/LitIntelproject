/* Case summary card in the formatted reader (preview). Above the decision it shows who the parties are, the earlier
   decisions, the issues, the main arguments of each side and which earlier finding is challenged, with paragraph links.
   Stored decisions only: /cases/{id}/case-frame returns stored data (off unless CASELIBRARY_CASE_FRAME_ENABLED=1, then
   the card simply does not appear). No model is called here. */
(function(){
 'use strict';
 const body=document.getElementById('decisionBody');
 if(!body||typeof readerState==='undefined')return;
 const E=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const fr={cache:new Map(),loading:new Set(),timer:0,busy:false,open:false,all:false};
 const link=p=>{const n=Number(p);return n>0?` <a href="#" class="frame-para" data-frame-go="${n}">[${n}]</a>`:'';};

 function data(){
  const id=readerState.caseId;
  if(id==null||!readerState.payload)return null;
  if(fr.cache.has(id))return fr.cache.get(id);
  if(!fr.loading.has(id)){
   fr.loading.add(id);
   fetch('/cases/'+encodeURIComponent(id)+'/case-frame').then(r=>r.ok?r.json():{available:false}).catch(()=>({available:false})).then(d=>{fr.loading.delete(id);fr.cache.set(id,d);schedule();});
  }
  return null;
 }

 function who(p,key){const name=p[key]||'',role=p[key+'_role']||'';return name?E(name)+(role?' <span class="frame-role">('+E(role)+')</span>':''):'';}

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
  if(f.levels.length)h+='<h4>Earlier decisions</h4><ol class="frame-levels">'+f.levels.map(l=>'<li>'+E(l.body||'')+(l.date?' ('+E(l.date)+')':'')+(l.outcome?': '+E(l.outcome):'')+link(l.para)+'</li>').join('')+'</ol>';
  if(f.issues.length)h+='<h4>Issues</h4><ul>'+f.issues.map(i=>'<li>'+E(i.text)+link(i.para)+'</li>').join('')+'</ul>';
  h+='<div class="frame-cols">'+argList('applicant','Applicant argues')+argList('respondent','Respondent argues')+'</div>';
  if(more)h+='<p><button type="button" class="frame-more" data-frame-more>'+(fr.all?'Show main arguments only':'Show all '+f.arguments.length+' arguments')+'</button></p>';
  if(f.challenged.length)h+='<h4>Earlier finding challenged</h4><ul>'+f.challenged.map(c=>'<li><strong>'+E(c.target||'')+':</strong> '+E(c.finding||'')+link(c.para)+'</li>').join('')+'</ul>';
  return h+'</details>';
 }

 function sync(){
  fr.busy=true;
  try{
   body.querySelectorAll('[data-frame-card]').forEach(n=>n.remove());
   const d=data();
   if(d&&d.available&&d.frame){body.insertAdjacentHTML('afterbegin',card(d));}
  }finally{fr.busy=false;}
 }
 function schedule(){window.clearTimeout(fr.timer);fr.timer=window.setTimeout(sync,30);}

 body.addEventListener('click',ev=>{
  const go=ev.target.closest&&ev.target.closest('[data-frame-go]');
  if(go){ev.preventDefault();const t=body.querySelector('.fmt-para[data-para="'+String(go.dataset.frameGo).replace(/"/g,'')+'"]');if(t&&t.scrollIntoView)t.scrollIntoView({block:'center',behavior:'smooth'});return;}
  if(ev.target.closest&&ev.target.closest('[data-frame-more]')){fr.all=!fr.all;fr.open=true;sync();}
 });
 body.addEventListener('toggle',ev=>{if(ev.target.matches&&ev.target.matches('[data-frame-card]'))fr.open=ev.target.open;},true);
 new MutationObserver(muts=>{
  if(fr.busy)return;
  const real=muts.some(m=>[...m.addedNodes,...m.removedNodes].some(n=>!(n.nodeType===1&&n.hasAttribute('data-frame-card'))));
  if(real)schedule();
 }).observe(body,{childList:true});
 schedule();
})();
