/* Markup mode: a third case-reader view.
   The decision is the whole page; intelligence the reader already stores (citations with pinpoint
   text, discussion units and sub-themes, verified outcome, judge, tags, cited-by counts) is shown as
   comment-style notes in a right-hand margin. Reads only payloads the reader already loaded: no
   network calls and no AI at view time. */
(function(){
'use strict';
const E=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const clip=(s,n)=>{s=String(s==null?'':s).replace(/\s+/g,' ').trim();return s.length>n?s.slice(0,n-1).trimEnd()+'…':s};
const ROLE_LABELS={evidence_fact:'Evidence / fact',governing_rule:'Governing rule',reasoning_application:'Reasoning application',counterargument_limitation:'Counterargument',issue:'Issue',disposition:'Disposition',party_position:'Party position'};
const roleLabel=r=>ROLE_LABELS[r]||String(r||'').replace(/_/g,' ').replace(/^./,c=>c.toUpperCase());
const BAND_COLORS=['#a78bfa','#0f766e','#d97706','#2563eb','#db2777','#65a30d','#0891b2','#9333ea','#dc2626','#0d9488','#ca8a04','#4f46e5'];
const TYPE={cite:{label:'Citation',color:'#c28e2d'},unit:{label:'Discussion unit',color:'#2563eb'},outcome:{label:'Outcome',color:'#1f6b45'},judge:{label:'Judge',color:'#475569'},citedby:{label:'Cited by others',color:'#0f766e'}};
const LAYER_DEFS=[
 {key:'cite',label:'Citations',states:['off','markers','open'],def:'markers'},
 {key:'unit',label:'Discussion units',states:['off','markers','open'],def:'markers'},
 {key:'outcome',label:'Outcome',states:['off','markers','open'],def:'open'},
 {key:'judge',label:'Judge',states:['off','markers','open'],def:'markers'},
 {key:'tags',label:'Tags',states:['off','soft'],def:'soft'},
 {key:'citedby',label:'Cited by others',states:['off','gutter'],def:'gutter'}
];
const STATE_LABEL={off:'Off',markers:'Markers',open:'Open',soft:'Soft',gutter:'Gutter'};

/* ---------- pure data helpers (no DOM) ---------- */
function paraNumberForIndex(chunks,index){
  const c=Array.isArray(chunks)?chunks[index]:null;
  const m=c&&/^\s*\[(\d{1,3})\]/.exec(String(c.text||''));
  return m?Number(m[1]):null;
}
function rangeParas(chunks,start,end){
  let first=null,last=null;
  for(let i=start;i<=end;i++){const n=paraNumberForIndex(chunks,i);if(n!==null){if(first===null)first=n;last=n;}}
  return first===null?null:{first,last};
}
function metaValue(meta,key){
  for(const row of meta||[]){if(row&&row.key===key&&row.value!==null&&row.value!==undefined)return row;}
  return null;
}
function subthemeRanges(payload){
  const rd=payload&&payload.readerData||{},chunks=rd.chunks||[],units=(rd.evidence_summary&&rd.evidence_summary.units)||[];
  const out=[];let n=0;
  for(const u of units){
    for(const s of u.subthemes||[]){
      const idx=(s.paragraph_indices||[]).filter(Number.isInteger);
      if(!idx.length)continue;
      const r=rangeParas(chunks,Math.min(...idx),Math.max(...idx));
      if(!r)continue;
      out.push({id:s.subtheme_id,unit:u.unit_index,first:r.first,last:r.last,terms:(s.display_key_terms&&s.display_key_terms.length?s.display_key_terms:s.key_terms||[]).slice(0,5),roles:(s.argument_roles||[]).map(roleLabel),color:BAND_COLORS[n%BAND_COLORS.length]});
      n++;
    }
  }
  return out;
}
/* Notes the margin can show. anchor: {kind:'cite',id} | {kind:'para',num} | {kind:'top'}. */
function buildNotes(payload){
  const rd=payload&&payload.readerData||{},item=Object.assign({},rd.case||{},payload&&payload.item||{});
  const chunks=rd.chunks||[],meta=rd.extracted_metadata||[],notes=[];
  /* judge */
  const judge=String(item.judge||'').trim();
  if(judge)notes.push({id:'judge',type:'judge',anchor:{kind:'top'},pill:'Judge · '+clip(judge,28),title:judge,meta:[item.court,item.date&&String(item.date).slice(0,10)].filter(Boolean).join(' · '),body:'Judge named on this decision.',foot:[]});
  /* outcome: verified only when stored evidence maps to one formatter paragraph */
  const oc=metaValue(meta,'decision_outcome'),dp=metaValue(meta,'disposition_paragraph'),dn=metaValue(meta,'disposition_paragraph_number');
  if(oc){
    const verified=!!(dp&&dn);
    const label=String(oc.value).replace(/_/g,' ').replace(/^./,c=>c.toUpperCase());
    notes.push({id:'outcome',type:'outcome',anchor:verified?{kind:'para',num:Number(dn.value)}:{kind:'top'},pill:'Outcome · '+clip(label,24)+(verified?'':' (unverified)'),title:label,meta:verified?'Verified against the decision text at ¶['+dn.value+']':'Stored outcome — evidence passage not verified',body:verified?'':'No verified disposition passage is stored for this decision, so this outcome is shown for reference only.',quote:verified?clip(dp.value,500):'',quoteLabel:verified?'Disposition passage as stored':'',foot:[],unverified:!verified});
  }
  /* citations: resolved or unresolved case citations that have a position in the text */
  const seen=new Set();
  for(const row of rd.citations||[]){
    if(!row||row.id==null||seen.has(row.id)||row.citation_kind==='statute'||row.citation_kind==='instrument')continue;
    if(!row.target_case_id&&(row.citation_kind==='case_short'||row.citation_kind==='case_name'))continue;
    seen.add(row.id);
    const title=row.target_title||row.citation_text||row.normalized_citation||'Citation';
    const hasPin=row.target_paragraph!=null;
    notes.push({id:'cite-'+row.id,type:'cite',anchor:{kind:'cite',id:row.id},pill:clip(row.target_citation||row.citation_text||title,26)+(hasPin?' ¶'+row.target_paragraph:''),title:title,meta:[row.target_citation||row.normalized_citation,row.pinpoint,hasPin?'pinpoint ¶'+row.target_paragraph:''].filter(Boolean).join(' · '),body:row.target_case_id?'':'Not in the library yet — no cited text available.',quote:row.target_chunk_text?clip(row.target_chunk_text,700):'',quoteLabel:hasPin?'Pinpoint text, ¶'+row.target_paragraph+' of the cited case':(row.target_chunk_text?'Cited text':''),foot:row.target_case_id?[{label:'Open case',action:'open-case',arg:row.target_case_id}]:[]});
  }
  /* discussion units and their sub-themes */
  const units=(rd.evidence_summary&&rd.evidence_summary.units)||[];
  for(const u of units){
    const r=rangeParas(chunks,u.start_paragraph,u.end_paragraph);
    if(!r)continue;
    const subs=subthemeRanges({readerData:{chunks:chunks,evidence_summary:{units:[u]}}});
    notes.push({id:'unit-'+u.unit_index,type:'unit',anchor:{kind:'para',num:r.first},pill:'Unit '+u.unit_index+' · ¶'+r.first+(r.last!==r.first?'–'+r.last:''),title:'Discussion unit '+u.unit_index+' (¶['+r.first+']'+(r.last!==r.first?'–['+r.last+']':'')+')',meta:subs.length+' sub-theme'+(subs.length===1?'':'s')+' · automatic segmentation',body:'',subs:subs,foot:[]});
  }
  /* cited-by counts per paragraph come from the formatter's blocks */
  for(const b of rd.format_blocks||[]){
    if(b&&b.type==='para'&&Number(b.cited_by_count)>0)notes.push({id:'citedby-'+b.start,type:'citedby',anchor:{kind:'para',num:b.num,blockStart:b.start},count:Number(b.cited_by_count),pill:'Cited by '+b.cited_by_count,title:'¶['+b.num+'] is cited by '+b.cited_by_count+' other case'+(Number(b.cited_by_count)===1?'':'s'),meta:'Distinct cases in the library that cite this paragraph',body:b.citation_tooltip||'',foot:[],gutter:true});
  }
  return notes;
}
/* Stack notes top to bottom without overlap. items: [{y,h}] in any order; returns [{index,top}]. */
function layoutNotes(items,gap){
  gap=gap==null?8:gap;
  const order=items.map((it,i)=>i).sort((a,b)=>items[a].y-items[b].y||a-b);
  let prev=-Infinity;const out=[];
  for(const i of order){const top=Math.max(items[i].y,prev+gap);out.push({index:i,top});prev=top+items[i].h;}
  return out;
}
function defaultLayers(){const o={};for(const d of LAYER_DEFS)o[d.key]=d.def;return o}
function sanitizeLayers(raw){
  const out=defaultLayers();
  if(raw&&typeof raw==='object')for(const d of LAYER_DEFS)if(d.states.includes(raw[d.key]))out[d.key]=raw[d.key];
  return out;
}
function noteState(note,layers,overrides){
  const layer=layers[note.type];
  if(layer==='off'||layer===undefined)return 'off';
  if(note.type==='citedby')return overrides&&overrides[note.id]===true?'open':'off';
  if(overrides&&overrides[note.id]===true)return 'open';
  if(overrides&&overrides[note.id]===false)return 'markers';
  return layer==='open'?'open':'markers';
}
const api={E,clip,roleLabel,paraNumberForIndex,rangeParas,subthemeRanges,buildNotes,layoutNotes,defaultLayers,sanitizeLayers,noteState,LAYER_DEFS,TYPE};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
if(typeof window==='undefined'||typeof document==='undefined')return;
window.__markupMode=api;

/* ---------- browser behaviour ---------- */
const $=id=>document.getElementById(id);
const state={on:false,layers:defaultLayers(),overrides:{},notes:[],infoOpen:false,outlineOpen:false,findTerm:'',findHits:[],findAt:-1};
const store={get(){try{return JSON.parse(localStorage.getItem('ilit.markup.layers')||'null')}catch(e){return null}},set(v){try{localStorage.setItem('ilit.markup.layers',JSON.stringify(v))}catch(e){}}};
state.layers=sanitizeLayers(store.get());
let rafPending=false;
const schedule=()=>{if(rafPending)return;rafPending=true;requestAnimationFrame(()=>{rafPending=false;if(state.on)render()})};

function panel(){return $('caseReaderPanel')}
function ensureStage(){
  let stage=$('markupStage');
  if(stage)return stage;
  const body=$('decisionBody'),source=body&&body.parentElement;
  if(!body||!source)return null;
  const bar=document.createElement('div');bar.id='markupBar';
  stage=document.createElement('div');stage.id='markupStage';
  stage.innerHTML='<div id="markupOutline" hidden></div><div id="markupBands" aria-hidden="true"></div><div id="markupBodySlot"></div><div id="markupMargin"><svg id="markupConn" aria-hidden="true"></svg></div>';
  source.insertBefore(bar,body);source.insertBefore(stage,body);
  $('markupBodySlot').appendChild(body);
  return stage;
}
function removeStage(){
  const stage=$('markupStage');if(!stage)return;
  const body=$('decisionBody'),source=stage.parentElement;
  if(body)source.insertBefore(body,stage);
  stage.remove();const bar=$('markupBar');if(bar)bar.remove();
}
function setOn(on){
  if(on===state.on)return;
  const p=panel();if(!p)return;
  const toggle=$('readerMarkupToggle');
  if(on){
    const rd=readerState&&readerState.payload&&readerState.payload.readerData;
    if(!rd||!(rd.format_blocks||[]).length){toggle&&toggle.setAttribute('title','Markup mode needs the formatted reader, which is unavailable for this case');return}
    state.on=true;
    readerState.formatted=true;
    readerState.mode='normalized';
    setReaderMode('normalized');
  }else{
    state.on=false;state.infoOpen=false;state.outlineOpen=false;
    removeStage();p.classList.remove('markup-on','markup-info-open');
    document.querySelectorAll('mark.markup-find').forEach(unwrap);
  }
  if(toggle){toggle.setAttribute('aria-pressed',String(state.on));}
}
function unwrap(m){const t=document.createTextNode(m.textContent);m.replaceWith(t);if(t.parentNode)t.parentNode.normalize()}
function afterRender(){
  const p=panel();if(!p||!state.on)return;
  const payload=readerState.payload;
  if(!payload||!$('decisionBody')||!$('decisionBody').querySelector('.fmt-decision')){setOn(false);return}
  p.classList.add('markup-on');
  ensureStage();
  state.notes=buildNotes(payload);
  state.overrides={};
  state.findHits=[];state.findAt=-1;
  render();
}
function countFor(type){return state.notes.filter(n=>n.type===type).length}
function renderBar(){
  const bar=$('markupBar');if(!bar)return;
  const L=state.layers;
  const chips=LAYER_DEFS.filter(d=>d.key!=='tags').map(d=>{
    const n=d.key==='citedby'?state.notes.filter(x=>x.type==='citedby').length:countFor(d.key);
    if(!n)return '';
    return `<button type="button" class="mk-chip${L[d.key]==='off'?' is-off':''}" data-mk-chip="${d.key}" aria-pressed="${L[d.key]!=='off'}"><i style="background:${(TYPE[d.key]||{color:'#2d8a50'}).color}"></i>${E(d.label)} <b>${n}</b></button>`;
  }).join('')+`<button type="button" class="mk-chip${L.tags==='off'?' is-off':''}" data-mk-chip="tags" aria-pressed="${L.tags!=='off'}"><i style="background:#2d8a50"></i>Tags</button>`;
  const rows=LAYER_DEFS.map(d=>`<div class="mk-lr"><b>${E(d.label)}</b><span class="mk-seg" role="group" aria-label="${E(d.label)} layer">${d.states.map(s=>`<button type="button" data-mk-layer="${d.key}" data-mk-state="${s}" aria-pressed="${L[d.key]===s}">${STATE_LABEL[s]}</button>`).join('')}</span></div>`).join('');
  bar.innerHTML=`<div class="mk-row"><button type="button" class="mk-btn" data-mk-act="layers" aria-expanded="${!!state.layersOpen}">Layers ▾</button>${chips}<span class="mk-sp"></span><button type="button" class="mk-btn" data-mk-act="expand">Expand all</button><button type="button" class="mk-btn" data-mk-act="collapse">Collapse all</button></div>`+
  `<div class="mk-row mk-row2"><label class="mk-find"><span class="mk-find-ico" aria-hidden="true">⌕</span><input type="search" id="markupFind" placeholder="Find in this case" value="${E(state.findTerm)}" aria-label="Find in this case"><span id="markupFindCount" class="mk-find-count"></span></label><button type="button" class="mk-btn" data-mk-act="info" aria-expanded="${state.infoOpen}">Case info ▾</button><button type="button" class="mk-btn" data-mk-act="outline" aria-expanded="${state.outlineOpen}">Outline</button><span class="mk-sp"></span><button type="button" class="mk-btn" data-mk-act="print">Print annotated</button></div>`+
  `<div class="mk-pop" id="markupLayerPop"${state.layersOpen?'':' hidden'}><div class="mk-pop-h">Margin layers<small>Off · Markers (collapsed pills) · Open (full bubbles)</small></div>${rows}<div class="mk-pop-f"><button type="button" class="mk-btn" data-mk-act="reset">Reset layers</button><span>Click a pill or bubble to open or fold just that note.</span></div></div>`;
}
function anchorEl(n){
  const body=$('decisionBody');if(!body)return null;
  const a=n.anchor;
  if(a.kind==='cite')return body.querySelector(`[data-cite-id="${a.id}"]`);
  if(a.kind==='para'){
    if(a.blockStart!=null)return body.querySelector(`[id="decision-source-${a.blockStart}"]`)||body.querySelector(`.fmt-para[data-para="${a.num}"]`);
    return body.querySelector(`.fmt-para[data-para="${a.num}"]`);
  }
  return body.querySelector('.fmt-decision');
}
function noteHTML(n,st){
  const t=TYPE[n.type];
  if(st==='markers'||(st==='off'))return `<button type="button" class="mk-pill" data-mk-note="${E(n.id)}" aria-expanded="false" title="${E(n.title)}"><i style="background:${t.color}"></i>${E(n.pill)}</button>`;
  const subs=n.subs&&n.subs.length?`<div class="mk-subs">${n.subs.map(s=>`<div class="mk-sub" style="--c:${s.color}"><b>¶[${s.first}]${s.last!==s.first?'–['+s.last+']':''}</b><span>${E(s.terms.join(' · '))}</span><div>${s.roles.map(r=>`<em>${E(r)}</em>`).join('')}</div></div>`).join('')}</div>`:'';
  const foot=(n.foot||[]).map(f=>`<button type="button" class="mk-link" data-mk-foot="${E(f.action)}" data-mk-arg="${E(f.arg)}">${E(f.label)}</button>`).join('');
  return `<div class="mk-card ${n.type}${n.unverified?' is-unverified':''}" style="--c:${t.color}" data-mk-note="${E(n.id)}"><div class="mk-card-t"><i style="background:${t.color}"></i>${E(t.label)}<button type="button" class="mk-x" data-mk-fold="${E(n.id)}" aria-label="Fold this note">✕</button></div><h4>${E(n.title)}</h4>${n.meta?`<div class="mk-meta">${E(n.meta)}</div>`:''}${n.quote?`<blockquote>${E(n.quote)}<small>${E(n.quoteLabel)}</small></blockquote>`:''}${n.body?`<div class="mk-body">${E(n.body)}</div>`:''}${subs}${foot?`<div class="mk-foot">${foot}</div>`:''}</div>`;
}
function render(){
  const stage=$('markupStage');if(!stage)return;
  renderBar();
  const body=$('decisionBody'),margin=$('markupMargin'),svg=$('markupConn');
  const shown=state.notes.filter(n=>n.type!=='citedby'&&noteState(n,state.layers,state.overrides)!=='off'&&anchorEl(n));
  const shownCb=state.notes.filter(n=>n.type==='citedby'&&state.layers.citedby!=='off'&&anchorEl(n));
  [...margin.querySelectorAll('.mk-note')].forEach(e=>e.remove());
  const base=margin.getBoundingClientRect();
  const els=[],items=[];
  for(const n of shown){
    const st=noteState(n,state.layers,state.overrides);
    const el=document.createElement('div');el.className='mk-note';el.dataset.id=n.id;el.innerHTML=noteHTML(n,st);
    margin.appendChild(el);
    const a=anchorEl(n),r=a.getBoundingClientRect();
    els.push({n,el,a,st});items.push({y:r.top-base.top-2,h:el.offsetHeight});
  }
  for(const n of shownCb){
    const st=noteState(n,state.layers,state.overrides);
    if(st!=='open')continue;
    const el=document.createElement('div');el.className='mk-note';el.dataset.id=n.id;el.innerHTML=noteHTML(n,'open');
    margin.appendChild(el);
    const a=anchorEl(n),r=a.getBoundingClientRect();
    els.push({n,el,a,st});items.push({y:r.top-base.top-2,h:el.offsetHeight});
  }
  const lay=layoutNotes(items,8);
  let bottom=0,g='';
  for(const l of lay){
    const o=els[l.index];o.el.style.top=l.top+'px';bottom=Math.max(bottom,l.top+items[l.index].h);
    const ar=o.a.getBoundingClientRect(),col=TYPE[o.n.type].color;
    const bodyR=body.getBoundingClientRect();
    const ay=ar.top-base.top+Math.min(11,ar.height/2),ty=l.top+(o.st==='open'?16:12);
    if(o.n.anchor.kind==='cite'){g+=`<path d="M${bodyR.right-base.left-2} ${ay} L-4 ${ty}" fill="none" stroke="${col}" stroke-width="${o.st==='open'?1.4:1}" opacity="${o.st==='open'?.85:.4}"/>`;}
  }
  stage.style.minHeight=Math.max(bottom+24,body.offsetHeight)+'px';
  svg.setAttribute('width',Math.max(margin.offsetWidth,1));svg.setAttribute('height',Math.max(bottom+24,body.offsetHeight));
  svg.style.left=0;svg.innerHTML=g;
  body.classList.toggle('mk-tags-off',state.layers.tags==='off');
  renderBands(stage,base);
  renderOutline();
  const p=panel();
  p.classList.toggle('markup-info-open',state.infoOpen);
  const ob=$('markupOutline');if(ob)ob.hidden=!state.outlineOpen;
}
function renderBands(stage,base){
  const bands=$('markupBands');if(!bands)return;
  bands.innerHTML='';
  const sb=bands.getBoundingClientRect();
  const subs=subthemeRanges(readerState.payload);
  const body=$('decisionBody');
  const paraEls=[...body.querySelectorAll('.fmt-para')];
  const top=n=>{const e=paraEls.find(x=>Number(x.dataset.para)===n);return e?e.getBoundingClientRect():null};
  if(state.layers.unit!=='off'){
    for(const s of subs){
      const a=top(s.first),b=top(s.last);if(!a||!b)continue;
      const d=document.createElement('div');d.className='mk-band';d.style.cssText=`top:${a.top-sb.top}px;height:${Math.max(4,b.bottom-a.top)}px;background:${s.color}`;
      d.title=`Sub-theme ¶${s.first}–${s.last}: ${s.terms.join(', ')}`;bands.appendChild(d);
    }
  }
  if(state.layers.citedby!=='off'){
    const rd=readerState.payload.readerData||{},max=Math.max(1,...(rd.format_blocks||[]).map(b=>Number(b.cited_by_count)||0));
    for(const b of rd.format_blocks||[]){
      const c=Number(b&&b.cited_by_count)||0;if(b.type!=='para'||c<=0)continue;
      const e=body.querySelector(`[id="decision-source-${b.start}"]`);if(!e)continue;const r=e.getBoundingClientRect();
      const d=document.createElement('button');d.type='button';d.className='mk-heat';d.dataset.mkNote='citedby-'+b.start;
      d.style.cssText=`top:${r.top-sb.top+2}px;height:${Math.max(6,r.height-4)}px;opacity:${(0.3+0.7*Math.min(c,max)/max).toFixed(2)}`;
      d.title=`Cited by ${c} case${c===1?'':'s'} in the library`;d.setAttribute('aria-label',d.title);bands.appendChild(d);
    }
  }
}
function renderOutline(){
  const box=$('markupOutline');if(!box)return;
  if(!state.outlineOpen){box.innerHTML='';return}
  const rd=readerState.payload.readerData||{},blocks=rd.format_blocks||[],text=readerState.payload.item&&readerState.payload.item.full_text||'';
  const heads=blocks.filter(b=>b.type==='heading').map(b=>({start:b.start,level:b.level||1,label:Array.from(text).slice(b.start,b.end).join('').trim()}));
  const subs=subthemeRanges(readerState.payload);
  const rows=heads.map(h=>`<button type="button" class="mk-ol l${Math.min(h.level,3)}" data-mk-goto="${h.start}">${E(clip(h.label,60))}</button>`);
  const subRows=subs.map(s=>`<button type="button" class="mk-ol sub" data-mk-para="${s.first}" style="--c:${s.color}"><i></i>${E(s.terms.slice(0,3).join(', ')||s.id)}<em>¶${s.first}${s.last!==s.first?'–'+s.last:''}</em></button>`);
  box.innerHTML=`<h5>Outline</h5>${rows.join('')||'<div class="mk-meta">No headings recognised.</div>'}${subRows.length?`<h5>Sub-themes</h5>${subRows.join('')}<div class="mk-meta">Automatic key terms; headings are the judgment’s own.</div>`:''}`;
}
function goto(el){if(!el)return;el.scrollIntoView({behavior:window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'center'})}

/* ---------- find in case ---------- */
function runFind(term){
  document.querySelectorAll('mark.markup-find').forEach(unwrap);
  state.findTerm=term;state.findHits=[];state.findAt=-1;
  const body=$('decisionBody');if(!body||!term||term.trim().length<2){updateFindCount();schedule();return}
  const needle=term.trim().toLowerCase(),walker=document.createTreeWalker(body,NodeFilter.SHOW_TEXT);
  const nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);
  for(const node of nodes){
    const low=node.nodeValue.toLowerCase();let idx=low.indexOf(needle);if(idx<0)continue;
    const frag=document.createDocumentFragment();let pos=0;
    while(idx>=0){
      frag.appendChild(document.createTextNode(node.nodeValue.slice(pos,idx)));
      const m=document.createElement('mark');m.className='markup-find';m.textContent=node.nodeValue.slice(idx,idx+needle.length);frag.appendChild(m);state.findHits.push(m);
      pos=idx+needle.length;idx=low.indexOf(needle,pos);
    }
    frag.appendChild(document.createTextNode(node.nodeValue.slice(pos)));node.replaceWith(frag);
  }
  if(state.findHits.length){state.findAt=0;focusHit()}
  updateFindCount();schedule();
}
function focusHit(){state.findHits.forEach((m,i)=>m.classList.toggle('is-current',i===state.findAt));goto(state.findHits[state.findAt])}
function updateFindCount(){const c=$('markupFindCount');if(c)c.textContent=state.findHits.length?`${state.findAt+1}/${state.findHits.length}`:(state.findTerm.trim().length>=2?'0 hits':'')}

/* ---------- events ---------- */
function persist(){store.set(state.layers)}
function setLayer(key,val){state.layers[key]=val;persist();render()}
document.addEventListener('click',ev=>{
  if(!state.on){const t=ev.target.closest&&ev.target.closest('#readerMarkupToggle');if(t){ev.preventDefault();setOn(true)}return}
  const t=ev.target;if(!t.closest)return;
  if(t.closest('#readerMarkupToggle')){ev.preventDefault();setOn(false);return}
  if(t.closest('#readerViewToggle')){setOn(false);return}
  const chip=t.closest('[data-mk-chip]');
  if(chip){const k=chip.dataset.mkChip,d=LAYER_DEFS.find(x=>x.key===k),on=state.layers[k]!=='off';setLayer(k,on?'off':(k==='tags'?'soft':k==='citedby'?'gutter':d.def==='off'?'markers':d.def));return}
  const ls=t.closest('[data-mk-layer]');if(ls){setLayer(ls.dataset.mkLayer,ls.dataset.mkState);return}
  const act=t.closest('[data-mk-act]');
  if(act){
    const a=act.dataset.mkAct;
    if(a==='layers'){state.layersOpen=!state.layersOpen;render()}
    else if(a==='expand'){for(const d of LAYER_DEFS)if(d.states.includes('open'))state.layers[d.key]='open';state.overrides={};persist();render()}
    else if(a==='collapse'){for(const d of LAYER_DEFS)if(d.states.includes('open'))state.layers[d.key]='markers';state.overrides={};persist();render()}
    else if(a==='reset'){state.layers=defaultLayers();state.overrides={};persist();render()}
    else if(a==='info'){state.infoOpen=!state.infoOpen;render()}
    else if(a==='outline'){state.outlineOpen=!state.outlineOpen;render()}
    else if(a==='print'){window.print()}
    return;
  }
  const fold=t.closest('[data-mk-fold]');if(fold){state.overrides[fold.dataset.mkFold]=false;render();return}
  const foot=t.closest('[data-mk-foot]');
  if(foot){if(foot.dataset.mkFoot==='open-case'&&typeof openDecision==='function'){setOn(false);openDecision(Number(foot.dataset.mkArg))}return}
  const go=t.closest('[data-mk-goto]');if(go){goto($('decisionBody').querySelector(`[id="decision-source-${go.dataset.mkGoto}"]`));return}
  const gp=t.closest('[data-mk-para]');if(gp){goto($('decisionBody').querySelector(`.fmt-para[data-para="${gp.dataset.mkPara}"]`));return}
  const pill=t.closest('.mk-pill[data-mk-note],.mk-heat[data-mk-note]');
  if(pill){const id=pill.dataset.mkNote;state.overrides[id]=true;render();return}
},false);
/* A citation click in markup mode toggles its note instead of opening the linked-case pane. */
document.addEventListener('click',ev=>{
  if(!state.on)return;const c=ev.target.closest&&ev.target.closest('#decisionBody [data-cite-id]');
  if(!c)return;
  ev.stopPropagation();
  const id='cite-'+c.dataset.citeId,cur=noteState(state.notes.find(n=>n.id===id)||{type:'cite',id},state.layers,state.overrides);
  state.overrides[id]=cur!=='open';render();
  const target=document.querySelector(`.mk-note[data-id="${id}"]`);if(target&&cur!=='open')target.scrollIntoView({block:'nearest'});
},true);
document.addEventListener('input',ev=>{if(ev.target&&ev.target.id==='markupFind')runFind(ev.target.value)});
document.addEventListener('keydown',ev=>{
  if(!state.on)return;
  if((ev.metaKey||ev.ctrlKey)&&ev.key.toLowerCase()==='k'){ev.preventDefault();const f=$('markupFind');if(f)f.focus();return}
  if(ev.target&&ev.target.id==='markupFind'&&ev.key==='Enter'&&state.findHits.length){ev.preventDefault();state.findAt=(state.findAt+(ev.shiftKey?-1:1)+state.findHits.length)%state.findHits.length;focusHit();updateFindCount()}
  if(ev.key==='Escape'&&(state.layersOpen||state.infoOpen)){state.layersOpen=false;state.infoOpen=false;render()}
});
window.addEventListener('resize',schedule);
const prevSet=setReaderMode;
setReaderMode=function(mode){prevSet(mode);if(state.on)afterRender();};
const prevClose=closeDecisionReader;
closeDecisionReader=function(){setOn(false);return prevClose.apply(this,arguments)};
})();
