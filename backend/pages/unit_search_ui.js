/* Find the unit (experimental): a keyword search that returns the passage and the discussion unit it sits in.
   Calls GET /unit-search (stored text and fixed rules only; nothing typed here goes to any model). Shown only under Experimental. */
(function(){
const panel=document.getElementById('unitSearchPanel');
if(!panel)return;
const $=id=>document.getElementById(id);
const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
/* unit-search-cards:start */
const ROLE_NAMES={metadata:'Header / footer',overview:'Overview',facts:'Facts',issues:'Issues',analysis:'Analysis',disposition:'Disposition'};
function unitRange(r){
 if(r.start_number==null)return 'no paragraph number';
 return '¶'+r.start_number+(r.end_number!=null&&r.end_number!==r.start_number?'–'+r.end_number:'');
}
function unitCardHtml(r){
 const outcome=r.outcome?String(r.outcome).replace(/_/g,' '):'',who=r.judge?(r.judge_label||'Judge')+': '+r.judge:'';
 const meta=[r.citation,r.court,r.date,who,outcome&&'Outcome: '+outcome].filter(Boolean).map(esc).join(' · ');
 const where='Unit '+r.unit_index+' · '+unitRange(r)+(r.role?' · '+(ROLE_NAMES[r.role]||r.role):'')+(r.paragraph_number!=null?' · match at ¶'+r.paragraph_number:'');
 return '<button type="button" class="us-card" data-us-case="'+r.case_id+'" data-us-para="'+(r.paragraph_number==null?'':r.paragraph_number)+'">'
  +'<div class="us-title">'+esc(r.title||'Untitled decision')+'</div>'
  +'<div class="us-meta">'+meta+'</div>'
  +'<div class="us-where">'+esc(where)+'</div>'
  +'<div class="us-snippet">'+esc(r.snippet||'')+'</div></button>';
}
/* unit-search-cards:end */
function jumpToParagraph(num){
 if(num==null||num==='')return;
 let tries=0;
 const timer=setInterval(()=>{
  tries++;
  const body=$('decisionBody');
  const el=body&&Array.from(body.querySelectorAll('[id^="decision-source-"]')).find(node=>new RegExp('^\\s*\\['+num+'\\]').test(node.textContent||''));
  if(el){clearInterval(timer);el.scrollIntoView({behavior:'smooth',block:'start'});el.classList.add('us-flash');setTimeout(()=>el.classList.remove('us-flash'),2400);}
  else if(tries>24)clearInterval(timer);
 },300);
}
async function run(event){
 event.preventDefault();
 const q=$('unitSearchQuery').value.trim(),status=$('unitSearchStatus'),box=$('unitSearchResults');
 if(q.split(/\s+/).filter(Boolean).length<3){status.textContent='Type at least three words, e.g. state protection adequacy.';return;}
 const court=$('unitSearchCourt').value,params=new URLSearchParams({q:q,limit:'8'});
 if(court)params.set('court',court);
 status.textContent='Searching…';box.innerHTML='';
 try{
  const res=await fetch('/unit-search?'+params.toString());
  if(res.status===404){const detail=(await res.json().catch(()=>({}))).detail;status.textContent=detail==='Not found'?'Unit search is switched off on this server.':'No passages matched. Try other words, or another court.';return;}
  if(!res.ok){status.textContent='Unit search could not run just now.';return;}
  const data=await res.json(),rows=data.results||[];
  status.textContent=rows.length?rows.length+' passage'+(rows.length===1?'':'s')+' · '+(data.note||'')+(data.truncated?' Stopped early to stay fast; narrow the court for more.':''):'No passages matched. Try other words, or another court.';
  box.innerHTML=rows.map(unitCardHtml).join('');
 }catch(error){status.textContent='Unit search could not run just now.';}
}
$('unitSearchForm').addEventListener('submit',run);
$('unitSearchResults').addEventListener('click',event=>{
 const card=event.target.closest('[data-us-case]');
 if(!card||typeof openDecision!=='function')return;
 const para=card.dataset.usPara;
 Promise.resolve(openDecision(Number(card.dataset.usCase))).catch(()=>{}).then(()=>jumpToParagraph(para));
});
})();
