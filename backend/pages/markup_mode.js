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
const TYPE={cite:{label:'Citation',color:'#c28e2d'},unit:{label:'Discussion unit',color:'#2563eb'},outcome:{label:'Outcome',color:'#1f6b45'},judge:{label:'Judge',color:'#475569'},citedby:{label:'Cited by others',color:'#0f766e'},statute:{label:'Act / statute',color:'#8b5bb2'},mine:{label:'My note',color:'#7c3aed'}};
const LAYER_DEFS=[
 {key:'cite',label:'Citations',states:['off','markers','open'],def:'markers'},
 {key:'unit',label:'Discussion units',states:['off','markers','open'],def:'markers'},
 {key:'outcome',label:'Outcome',states:['off','markers','open'],def:'open'},
 {key:'judge',label:'Judge',states:['off','markers','open'],def:'markers'},
 {key:'statute',label:'Acts / statutes',states:['off','markers','open'],def:'markers'},
 {key:'tags',label:'Tags',states:['off','underline','tint','bubbles'],def:'underline'},
 {key:'citedby',label:'Cited by others',states:['off','gutter'],def:'gutter'},
 {key:'mine',label:'My notes',states:['off','markers','open'],def:'open'}
];
const MINE_MAX=200,MINE_TEXT=2000;
const STATE_LABEL={off:'Off',markers:'Markers',open:'Open',underline:'Underline',tint:'Tint',bubbles:'Bubbles',gutter:'Gutter'};

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
/* Topics: sub-theme key terms ranked by how many paragraphs they cover. */
function topicIndex(payload,limit){
  const subs=subthemeRanges(payload),by=new Map();
  for(const s of subs)for(const t of s.terms){
    const key=String(t).trim().toLowerCase();if(!key)continue;
    const e=by.get(key)||{key:key,label:String(t).trim(),ranges:[],paras:0};
    e.ranges.push({first:s.first,last:s.last});e.paras+=s.last-s.first+1;by.set(key,e);
  }
  const out=[...by.values()].sort((a,b)=>b.paras-a.paras||a.key.localeCompare(b.key)).slice(0,limit||10);
  out.forEach((t,i)=>{t.color=BAND_COLORS[i%BAND_COLORS.length]});
  return out;
}
function topicParas(topics,selected){
  const set=new Set();
  for(const t of topics||[])if(selected&&selected.includes(t.key))for(const r of t.ranges)for(let n=r.first;n<=r.last;n++)set.add(n);
  return set;
}
/* visible: array of booleans in document order; returns runs of consecutive hidden entries. */
function foldRuns(visible){
  const runs=[];let start=-1;
  for(let i=0;i<=visible.length;i++){
    const hidden=i<visible.length&&!visible[i];
    if(hidden&&start<0)start=i;
    if(!hidden&&start>=0){runs.push({start:start,end:i-1});start=-1;}
  }
  return runs;
}
/* By-topic view: every sub-theme as a group of its own paragraphs (lead sentence, full text on request). */
function leadSentence(text,max){
  const t=String(text||'').replace(/^\s*\[\d+\]\s*/,'').replace(/\s+/g,' ').trim();
  const m=/^(.{20,}?[.!?])(?=\s+[A-Z“"(\[]|$)/.exec(t);
  const first=m?m[1]:t;
  return first.length>max?first.slice(0,max-1).trimEnd()+'…':first;
}
function topicGroups(payload){
  const rd=payload&&payload.readerData||{},item=Object.assign({},rd.case||{},payload&&payload.item||{}),blocks=rd.format_blocks||[],full=String(item.full_text||'');
  const byNum=new Map();
  for(const b of blocks)if(b&&b.type==='para'&&b.num!=null&&!byNum.has(b.num))byNum.set(b.num,b);
  return subthemeRanges(payload).map(s=>{
    const paras=[];
    for(let n=s.first;n<=s.last;n++){const b=byNum.get(n);if(!b)continue;const text=full.slice(b.start,b.end).replace(/^\s*\[\d+\]\s*/,'').trim();if(text)paras.push({num:n,lead:leadSentence(text,220),text:text})}
    return Object.assign({title:sectionHeading(blocks,full,s.first,true)||('Paragraphs ¶['+s.first+']–['+s.last+']'),paras:paras},s);
  }).filter(g=>g.paras.length);
}
const PURPOSE_SHORT={disagreed:'Disagreed',distinguished:'Distinguished',followed:'Followed',quoted:'Quoted',compared:'Compared',see:'See',mentioned:'Mentioned'};
/* "Cited by 3 cases · Followed 1, See 2" from a stored paragraph cited-by summary. */
function citedByLine(s){
  if(!s||!(Number(s.citer_count)>0))return '';
  const n=Number(s.citer_count),parts=Object.keys(s.purposes||{}).filter(k=>s.purposes[k]>0).map(k=>(PURPOSE_SHORT[k]||k)+' '+s.purposes[k]);
  return 'Cited by '+n+' case'+(n===1?'':'s')+(parts.length?' · '+parts.join(', '):'');
}
/* What the Peek panel shows for a citation note: only stored data, never fetched. */
function peekFor(note){
  const c=note&&note.cite;if(!c)return null;
  return {id:note.id,loc:note.loc==null?null:note.loc,title:note.title,citation:c.citation,inLibrary:c.inLibrary,caseId:c.caseId,paragraph:c.paragraph,
    text:c.inLibrary?(note.quote||''):'',label:c.inLibrary&&note.quote?(note.quoteLabel||''):'',noText:c.inLibrary&&!note.quote?(note.body||''):'',
    missing:c.inLibrary?'':'Not in the library yet: iLit has no text for this authority.',
    citedBy:c.inLibrary?citedByLine(c.citedBy):''};
}
/* "Canada (Citizenship and Immigration) v Vavilov" -> "Vavilov": the party that is not the Crown, for the short pill label. */
const CROWN=/^(canada|the minister|minister|attorney general|ministre|procureur|her majesty|his majesty|the queen|the king|mci|mpsep|mcic)\b/i;
function shortCaseName(title){
  const t=String(title||'').replace(/\s+/g,' ').trim();if(!t)return '';
  const parts=t.split(/\s+v\.?\s+|\s+c\.\s+/i).map(x=>x.replace(/\s*\(.*?\)\s*/g,' ').replace(/[,;].*$/,'').trim()).filter(Boolean);
  if(!parts.length)return clip(t,18);
  const pick=parts.find(x=>!CROWN.test(x)&&x.length>2)||parts.find(x=>x.length>2)||parts[0];
  return clip(pick,20);
}
/* "Strachn 2012 FC 984": short party name plus neutral citation, for the margin pill. */
const NEUTRAL=/\b\d{4}\s+[A-Z]{2,5}\s+\d+\b/;
function citePill(row,title){
  const text=String(row.target_title||row.citation_text||'');
  const neutral=(NEUTRAL.exec(row.target_citation||'')||NEUTRAL.exec(row.citation_text||'')||NEUTRAL.exec(row.normalized_citation||'')||[''])[0];
  const name=shortCaseName(text.split(/,\s*(?:\d{4}|\[)/)[0].replace(/\s+(at\s+)?para.*$/i,''));
  if(name&&/\s(v\.?|c\.)\s/i.test(text))return (name+' '+neutral).trim();
  return clip(row.target_citation||row.citation_text||title,26);
}
/* Heading of the section a paragraph sits in ("Analysis"), from heading blocks and the decision text. */
function sectionHeading(blocks,fullText,paraNum,nearest){
  if(paraNum==null||!blocks||!fullText)return '';
  let top=null,near=null;
  for(const b of blocks){
    if(!b)continue;
    if(b.type==='para'&&b.num===paraNum)break;
    if(b.type==='heading'){near=b;if(b.level==null||b.level<=1)top=b;}
  }
  const h=nearest?near:(top||near);if(!h)return '';
  return String(fullText).slice(h.start,h.end).replace(/\s+/g,' ').trim();
}
/* Case-level facts for the header pills: outcome, judge, file number. */
function headerInfo(payload){
  const rd=payload&&payload.readerData||{},item=Object.assign({},rd.case||{},payload&&payload.item||{}),meta=rd.extracted_metadata||[];
  const oc=metaValue(meta,'decision_outcome'),jm=metaValue(meta,'judge');
  const file=String(item.docket_number||(metaValue(meta,'docket')||{}).value||(metaValue(meta,'imm_number')||{}).value||(metaValue(meta,'case_number')||{}).value||'').trim();
  return {outcome:oc?String(oc.value).replace(/_/g,' ').replace(/^./,c=>c.toUpperCase()):'',judge:String(item.judge||(jm&&jm.value)||'').trim(),file:file};
}
/* The cited paragraph's own text, from the stored chunk, only when the chunk really starts with that paragraph number. */
function paraText(chunk,num){
  const t=String(chunk||'');if(num==null||!t)return '';
  const m=new RegExp('^\\s*\\['+Number(num)+'\\]\\s*').exec(t);if(!m)return '';
  let body=t.slice(m[0].length);
  const cut=[/\n\s*\[\d+\]\s/,/\n[A-Z][A-Z .,'’-]{3,}\s*(?:\n|$)/].map(r=>{const x=r.exec(body);return x?x.index:-1}).filter(i=>i>=0);
  if(cut.length)body=body.slice(0,Math.min(...cut));
  return body.replace(/\s+/g,' ').trim();
}
/* What a citation note can honestly say about its pinpoint: the paragraph text, or why there is none. Stored text only. */
function pinpointInfo(row){
  const n=row.target_paragraph,short=shortCaseName(row.target_title||row.target_citation||'');
  if(!row.target_case_id)return {quote:'',label:'',body:'Not in the library yet — no cited text available.'};
  if(n==null)return {quote:'',label:'',body:'No pinpoint paragraph was cited, so there is no paragraph text to show.'};
  const paras=Array.isArray(row.target_paragraphs)&&row.target_paragraphs.length?row.target_paragraphs:[n];
  if(paras.length>1){
    const texts=row.target_chunk_texts||{};
    const found=paras.map(p=>({p:p,t:paraText(texts[p]||(p===n?row.target_chunk_text:''),p)})).filter(x=>x.t);
    const label=(row.target_pinpoint_label||'paras '+paras[0]+'–'+paras[paras.length-1])+(short?' of '+short:' of the cited case');
    if(!found.length)return {quote:'',label:'',body:'Pinpoint '+(row.target_pinpoint_label||'paragraphs')+' has no stored text in the library.'};
    const more=paras.length-found.length;
    const note=more>0?' (text shown for '+found.length+' of '+paras.length+' paragraphs)':'';
    return {quote:found.map(x=>'¶['+x.p+'] '+x.t).join('\n\n'),label:label+note+(row.target_pinpoint_open_ended?' — "ff": later paragraphs not named':''),body:''};
  }
  const q=paraText(row.target_chunk_text,n);
  if(q)return {quote:q,label:'¶['+n+']'+(short?' of '+short:' of the cited case')+(row.target_pinpoint_open_ended?' — "ff": later paragraphs not named':''),body:''};
  return {quote:'',label:'',body:row.target_chunk_text?'Pinpoint ¶['+n+'] was not found in the stored text of the cited case, so no paragraph text is shown.':'Pinpoint ¶['+n+'] has no stored text in the library.'};
}
/* Short Act names for the pill; anything else falls back to the stored document title. */
const ACT_SHORT={'canada.irpa':'IRPA','canada.irpr':'IRPR'};
function statuteNote(row){
  const key=row.instrument_key||'';
  const act=ACT_SHORT[key]||(key?String(key.split('.').pop()).toUpperCase():'');
  if(!act&&!row.authority_document_title&&row.unresolved)return null;   /* "In the Order": not a real instrument */
  const doc=row.authority_document_title||row.normalized_citation||row.citation_text||'Statute reference';
  const pin=String(row.pinpoint||row.section_number||row.provision_section||'').trim();
  const label=(act||clip(doc,18))+(pin?' s '+pin:'');
  const text=String(row.provision_text||row.authority_section_text||'').trim();
  const url=/^https:\/\//i.test(row.legislation_url||'')?row.legislation_url:(/^https:\/\//i.test(row.source_url||'')?row.source_url:'');
  const status=row.unresolved?'Instrument or section not matched to stored legislation':(text?'Provision text as stored':'Provision text is not stored for this section');
  return {id:'statute-'+row.id,type:'statute',anchor:{kind:'cite',id:row.id},pill:clip(label,28),title:label,meta:[doc,row.statute_version_label&&row.statute_version_label!=='Version unknown'?row.statute_version_label:''].filter(Boolean).join(' · '),body:text?'':status+'.',quote:text?clip(text,900):'',quoteLabel:text?'Provision text as stored':'',statute:{act:act,pinpoint:pin,url:url},foot:(url?[{label:'Open the Act',action:'open-url',arg:url}]:[])};
}
/* Notes the margin can show. anchor: {kind:'cite',id} | {kind:'para',num} | {kind:'top'}. */
function buildNotes(payload){
  const rd=payload&&payload.readerData||{},item=Object.assign({},rd.case||{},payload&&payload.item||{});
  const chunks=rd.chunks||[],meta=rd.extracted_metadata||[],notes=[];
  /* judge */
  const judge=String(item.judge||(metaValue(meta,'judge')||{}).value||'').trim();
  if(judge)notes.push({id:'judge',type:'judge',anchor:{kind:'top'},pill:'Judge · '+clip(judge,28),title:judge,meta:[item.court,item.citation,item.date&&String(item.date).slice(0,10)].filter(Boolean).join(' · '),body:'Judge named on this decision.',foot:[{label:'Open judge profile',action:'judge-profile',arg:judge}]});
  /* outcome: verified only when stored evidence maps to one formatter paragraph */
  const oc=metaValue(meta,'decision_outcome'),dp=metaValue(meta,'disposition_paragraph'),dn=metaValue(meta,'disposition_paragraph_number');
  if(oc){
    const verified=!!(dp&&dn);
    const label=String(oc.value).replace(/_/g,' ').replace(/^./,c=>c.toUpperCase());
    notes.push({id:'outcome',type:'outcome',anchor:verified?{kind:'para',num:Number(dn.value)}:{kind:'top'},pill:'Outcome · '+clip(label,24)+(verified?'':' (unverified)'),title:label,meta:verified?'Verified against the decision text at ¶['+dn.value+']':'Stored outcome — evidence passage not verified',body:verified?'':'No verified disposition passage is stored for this decision, so this outcome is shown for reference only.',quote:verified?clip(dp.value,500):'',quoteLabel:verified?'Disposition passage as stored':'',foot:verified?[{label:'Show ¶['+dn.value+']',action:'goto-para',arg:dn.value}]:[],unverified:!verified});
  }
  /* statutes and regulations: one note per reference, with the provision text only when it is stored */
  const sseen=new Set();
  for(const row of rd.citations||[]){
    if(!row||row.id==null||sseen.has(row.id)||!(row.citation_kind==='statute'||row.citation_kind==='instrument'))continue;
    const sn=statuteNote(row);if(!sn)continue;
    sseen.add(row.id);notes.push(sn);
  }
  /* citations: resolved or unresolved case citations that have a position in the text */
  const seen=new Set();
  for(const row of rd.citations||[]){
    if(!row||row.id==null||seen.has(row.id)||row.citation_kind==='statute'||row.citation_kind==='instrument')continue;
    /* a bare case name or short form with no stored target is still highlighted in the text, so it keeps a note (hover, click, Peek) but no margin pill until opened */
    const quiet=!row.target_case_id&&(row.citation_kind==='case_short'||row.citation_kind==='case_name');
    seen.add(row.id);
    const title=row.target_title||row.citation_text||row.normalized_citation||'Citation';
    const hasPin=row.target_paragraph!=null,pin=pinpointInfo(row);
    notes.push({id:'cite-'+row.id,type:'cite',quiet:quiet,anchor:{kind:'cite',id:row.id},pill:citePill(row,title)+(hasPin?' ¶'+(row.target_paragraphs&&row.target_paragraphs.length>1?(row.target_pinpoint_label||row.target_paragraph).toString().replace(/^paras? /,''):row.target_paragraph):''),title:title,meta:[row.target_citation||row.normalized_citation,row.pinpoint,hasPin?'pinpoint '+(row.target_paragraphs&&row.target_paragraphs.length>1?row.target_pinpoint_label:'¶'+row.target_paragraph):''].filter(Boolean).join(' · '),body:pin.body,quote:pin.quote,quoteLabel:pin.label,cite:{inLibrary:!!row.target_case_id,caseId:row.target_case_id||null,citation:row.target_citation||row.normalized_citation||row.citation_text||'',paragraph:hasPin?row.target_paragraph:null,pinpoint:row.pinpoint||'',text:row.citation_text||'',citedBy:row.target_cited_by||null},foot:(row.target_case_id?[{label:'Open '+shortCaseName(row.target_title||row.target_citation||'case'),action:'open-case',arg:row.target_case_id}]:[]).concat([{label:'Pin',action:'pin',arg:'cite-'+row.id}])});
  }
  /* discussion units and their sub-themes */
  const units=(rd.evidence_summary&&rd.evidence_summary.units)||[];
  for(const u of units){
    const r=rangeParas(chunks,u.start_paragraph,u.end_paragraph);
    if(!r)continue;
    const head=sectionHeading(rd.format_blocks,item.full_text,r.first);
    const subs=subthemeRanges({readerData:{chunks:chunks,evidence_summary:{units:[u]}}});
    notes.push({id:'unit-'+u.unit_index,type:'unit',anchor:{kind:'para',num:r.first},pill:'Unit · '+(head?clip(head.replace(/^(?:[IVXLC]+|\d+|[A-Z])[.)]\s+/,''),18)+' ':u.unit_index+' · ')+'¶'+r.first+(r.last!==r.first?'–'+r.last:''),title:'Discussion unit '+u.unit_index+(head?': '+clip(head,40):'')+' (¶['+r.first+']'+(r.last!==r.first?'–['+r.last+']':'')+')',meta:subs.length+' sub-theme'+(subs.length===1?'':'s')+' · automatic segmentation',body:'',subs:subs,foot:[]});
  }
  /* cited-by counts per paragraph come from the formatter's blocks; the batch job's stored rows add who and why */
  const stored=rd.paragraph_cited_by||null,storedBy={};
  if(stored)for(const p of stored.paragraphs||[])storedBy[p.paragraph]=p;
  const cov=stored&&stored.coverage;
  for(const b of rd.format_blocks||[]){
    if(!(b&&b.type==='para'&&Number(b.cited_by_count)>0))continue;
    const sp=storedBy[b.num],citers=sp?sp.citers||[]:[];
    const meta=sp?(cov&&!cov.complete?'Partial: '+cov.sources_processed+' of '+cov.sources_total+' citing cases analysed so far · ':'')+citedByLine(sp):'Distinct cases in the library that cite this paragraph';
    const body=sp?citers.map(c=>(c.citation||c.title||'Case '+c.case_id)+(c.mentions>1?' ×'+c.mentions:'')+' · '+(PURPOSE_SHORT[c.purpose]||c.purpose)+(c.signal&&c.purpose!=='mentioned'?' ("'+c.signal+'")':'')).join('\n')+(sp.citer_count>citers.length?'\n+ '+(sp.citer_count-citers.length)+' more':''):(b.citation_tooltip||'');
    const foot=citers.filter(c=>c.case_id).slice(0,3).map(c=>({label:'Open '+clip(c.citation||c.title||'case',22),action:'open-case',arg:c.case_id}));
    notes.push({id:'citedby-'+b.start,type:'citedby',anchor:{kind:'para',num:b.num,blockStart:b.start},count:Number(b.cited_by_count),pill:'Cited by '+b.cited_by_count,title:'¶['+b.num+'] is cited by '+b.cited_by_count+' other case'+(Number(b.cited_by_count)===1?'':'s'),meta:meta,body:body,foot:foot,gutter:true,stored:!!sp});
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
  if(raw&&typeof raw==='object')for(const d of LAYER_DEFS){const v=d.key==='tags'&&raw.tags==='soft'?'underline':raw[d.key];if(d.states.includes(v))out[d.key]=v;}
  return out;
}
function noteState(note,layers,overrides){
  const layer=layers[note.type];
  if(layer==='off'||layer===undefined)return 'off';
  if(note.type==='citedby'||note.quiet)return overrides&&overrides[note.id]===true?'open':'off';
  if(overrides&&overrides[note.id]===true)return 'open';
  if(overrides&&overrides[note.id]===false)return 'markers';
  return layer==='open'?'open':'markers';
}
/* ---------- private notes (this browser only) and Word export plan: pure ---------- */
function mineToNotes(list){
  return (list||[]).filter(m=>m&&m.para!=null&&String(m.text||'').trim()).map(m=>({id:'mine-'+m.para,type:'mine',anchor:{kind:'para',num:Number(m.para)},pill:'My note · ¶'+m.para+': '+clip(m.text,18),title:'My note on ¶['+m.para+']',meta:'Private: saved in this browser only',body:String(m.text),foot:[{label:'Edit',action:'mine-edit',arg:m.para}]}));
}
function mineUpsert(list,para,text,hl){
  const rest=(list||[]).filter(m=>Number(m.para)!==Number(para));
  text=String(text||'').slice(0,MINE_TEXT);
  if(!text.trim()&&!hl)return rest;
  return rest.concat([{para:Number(para),text:text,hl:!!hl,ts:Date.now()}]).sort((a,b)=>a.para-b.para).slice(0,MINE_MAX);
}
/* What one note says in a Word comment: a bold first line (label), then plain lines. */
function commentFor(n){
  const t=TYPE[n.type]||{label:'Note'};
  const lines=[];
  if(n.meta&&n.type!=='mine')lines.push(String(n.meta));
  if(n.quote)lines.push((n.quoteLabel?n.quoteLabel+': ':'')+'“'+clip(String(n.quote).replace(/\s+/g,' ').trim(),700)+'”');
  if(n.body)lines.push(String(n.body));
  for(const s of n.subs||[])lines.push('¶['+s.first+']'+(s.last!==s.first?'–['+s.last+']':'')+': '+(s.terms||[]).join(', ')+(s.roles&&s.roles.length?' ('+s.roles.join(', ')+')':''));
  return {label:t.label+(n.title&&n.type!=='mine'?': '+clip(n.title,90):''),text:lines.join('\n'),quote:n.cite&&n.cite.text?String(n.cite.text):null};
}
/* Comments for the Word file: every note whose layer is on, anchored by blockOf(note) (a block start, or null for the case header). Tags are left out: they are too many to read as comments. */
function exportPlan(notes,layers,blockOf){
  const out=[];
  for(const n of notes||[]){
    if(n.type==='tags'||n.quiet)continue;
    const st=layers&&layers[n.type];if(st===undefined||st==='off')continue;
    const c=commentFor(n),b=blockOf?blockOf(n):null;
    out.push({block:b==null?null:Number(b),label:c.label,text:c.text,quote:c.quote,author:n.type==='mine'?'My note':'iLit Markup'});
  }
  return out;
}
const api={paraText,pinpointInfo,mineToNotes,mineUpsert,commentFor,exportPlan,E,clip,roleLabel,paraNumberForIndex,rangeParas,subthemeRanges,buildNotes,citePill,topicGroups,leadSentence,shortCaseName,sectionHeading,headerInfo,layoutNotes,defaultLayers,sanitizeLayers,noteState,topicIndex,topicParas,foldRuns,peekFor,citedByLine,LAYER_DEFS,TYPE};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
if(typeof window==='undefined'||typeof document==='undefined')return;
window.__markupMode=api;

/* ---------- browser behaviour ---------- */
const $=id=>document.getElementById(id);
const state={on:false,layers:defaultLayers(),overrides:{},notes:[],infoOpen:false,outlineOpen:false,layersOpen:false,findTerm:'',findHits:[],findAt:-1,
  caseId:null,mine:[],editing:null,pins:[],dock:'float',panelPos:null,topics:[],topicSel:[],foldOthers:false,unfolded:[],view:'reading',topicOpen:[],printing:false,peekOpen:[],qopen:{}};
const store={get(){try{return JSON.parse(localStorage.getItem('ilit.markup.layers')||'null')}catch(e){return null}},set(v){try{localStorage.setItem('ilit.markup.layers',JSON.stringify(v))}catch(e){}}};
state.layers=sanitizeLayers(store.get());
const MINE_KEY='ilit.markup.notes.v1';
const mineStore={
  all(){try{const r=JSON.parse(localStorage.getItem(MINE_KEY)||'{}');return r&&typeof r==='object'&&!Array.isArray(r)?r:{}}catch(e){return {}}},
  get(cid){const a=cid==null?null:this.all()[cid];return Array.isArray(a)?a:[]},
  set(cid,list){if(cid==null)return;try{const all=this.all();if(list.length)all[cid]=list;else delete all[cid];localStorage.setItem(MINE_KEY,JSON.stringify(all))}catch(e){}}
};
let rafPending=false;
const schedule=()=>{if(rafPending)return;rafPending=true;requestAnimationFrame(()=>{rafPending=false;if(state.on)render()})};

function panel(){return $('caseReaderPanel')}
let bodyObserver=null;
function ensureStage(){
  let stage=$('markupStage');
  if(stage)return stage;
  const body=$('decisionBody'),source=body&&body.parentElement;
  if(!body||!source)return null;
  const bar=document.createElement('div');bar.id='markupBar';
  stage=document.createElement('div');stage.id='markupStage';
  stage.innerHTML='<div id="markupOutline" hidden></div><div id="markupBands" aria-hidden="true"></div><div id="markupTopicView" hidden></div><div id="markupBodySlot"></div><div id="markupMargin"><svg id="markupConn" aria-hidden="true"></svg></div><div id="markupMini" aria-hidden="true"><div class="mk-mini-in"></div><i class="mk-mini-vp"></i></div>';
  const head=document.createElement('div');head.id='markupPrintHead';
  source.insertBefore(bar,body);source.insertBefore(head,body);source.insertBefore(stage,body);
  $('markupBodySlot').appendChild(body);
  /* the reader adds things to paragraphs after first paint (similar-paragraph buttons, fonts); re-place the notes whenever the text's height changes */
  if(typeof ResizeObserver==='function'){bodyObserver=new ResizeObserver(()=>schedule());bodyObserver.observe(body)}
  return stage;
}
function removeStage(){
  if(bodyObserver){bodyObserver.disconnect();bodyObserver=null}
  const stage=$('markupStage');if(!stage)return;
  const body=$('decisionBody'),source=stage.parentElement;
  if(body)source.insertBefore(body,stage);
  stage.remove();for(const id of ['markupBar','markupPrintHead']){const e=$(id);if(e)e.remove()}
}
function setOn(on){
  if(on===state.on)return;
  const p=panel();if(!p)return;
  const toggle=$('readerMarkupToggle');
  if(on){
    const rd=readerState&&readerState.payload&&readerState.payload.readerData;
    if(!rd||!(rd.format_blocks||[]).length){toggle&&toggle.setAttribute('title','Markup mode needs the formatted reader, which is unavailable for this case');return}
    state.on=true;document.body.classList.add('markup-mode-on');
    readerState.formatted=true;
    readerState.mode='normalized';
    setReaderMode('normalized');
  }else{
    state.on=false;document.body.classList.remove('markup-mode-on');state.infoOpen=false;state.outlineOpen=false;state.layersOpen=false;
    hideHover(true);clearFold();cleanMine();decorateNums(false);closeEditor();
    removeStage();p.classList.remove('markup-on','markup-info-open','markup-docked','markup-peeking');
    const pn=$('mkPanel');if(pn)pn.remove();
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
  const cid=(payload.item&&payload.item.id)||(payload.readerData&&payload.readerData.case&&payload.readerData.case.id)||null;
  if(cid!==state.caseId){state.caseId=cid;state.pins=[];state.topicSel=[];state.foldOthers=false;state.unfolded=[];state.view='reading';state.topicOpen=[];closeEditor()}
  state.mine=mineStore.get(cid);
  state.notes=buildNotes(payload).concat(mineToNotes(state.mine));
  state.topics=topicIndex(payload,10);
  state.topicSel=state.topicSel.filter(k=>state.topics.some(t=>t.key===k));
  state.overrides={};
  state.findHits=[];state.findAt=-1;
  render();
}
function countFor(type){return state.notes.filter(n=>n.type===type).length}
function tagCount(){const rd=readerState.payload&&readerState.payload.readerData;return rd&&Array.isArray(rd.tags)?rd.tags.length:0}
/* Re-render the toolbar without losing the user's place: keep focus (and caret in the find box). */
function focusKey(el){
  if(!el||!el.closest||!el.closest('#markupBar'))return null;
  if(el.id==='markupFind')return {sel:'#markupFind',s:el.selectionStart,e:el.selectionEnd};
  for(const a of ['mkAct','mkChip','mkTopic']){if(el.dataset&&el.dataset[a]!==undefined)return {sel:`[data-${a.replace(/[A-Z]/g,c=>'-'+c.toLowerCase())}="${el.dataset[a]}"]`};}
  if(el.dataset&&el.dataset.mkLayer)return {sel:`[data-mk-layer="${el.dataset.mkLayer}"][data-mk-state="${el.dataset.mkState}"]`};
  return null;
}
let groupsCache={key:null,list:[]};
function topicGroupsCached(){
  const p=readerState.payload,key=p&&p.readerData;
  if(groupsCache.key!==key){groupsCache={key:key,list:p?topicGroups(p):[]}}
  return groupsCache.list;
}
function renderTopicView(){
  const stage=$('markupStage'),tv=$('markupTopicView');if(!stage||!tv)return;
  const on=state.view==='topic'&&topicGroupsCached().length>0;
  stage.classList.toggle('is-topic',on);tv.hidden=!on;
  if(!on){tv.innerHTML='';return}
  const open=new Set(state.topicOpen);
  tv.innerHTML=`<div class="mk-tv-note"><b>By topic.</b> The automatic sub-themes of this decision, each with its own paragraphs, in reading order. The judgment's own wording is shown unchanged; only the order and grouping differ. Use the paragraph number to jump back to it in reading order.</div>`+
    topicGroupsCached().map((g,i)=>{const isOpen=open.has(i),shown=g.paras;return `<section class="mk-tg" style="--c:${g.color}"><header><button type="button" class="mk-tg-t" data-mk-tg="${i}" aria-expanded="${isOpen}"><span class="mk-tg-c">${isOpen?'▾':'▸'}</span><b>${E(g.title)}</b></button><span class="mk-tg-r">¶[${g.first}]${g.last!==g.first?'–['+g.last+']':''} · ${g.paras.length} paragraph${g.paras.length===1?'':'s'} · ${isOpen?'showing full text':'showing lead sentences'}</span></header><div class="mk-tg-m">${E(g.terms.join(' · '))}</div><div class="mk-tg-roles">${g.roles.map(r=>`<em>${E(r)}</em>`).join('')}</div>${shown.map(p=>`<p class="mk-tp"><button type="button" class="mk-tn" data-mk-tgo="${p.num}" title="Show in reading order">[${p.num}]</button>${E(isOpen?p.text:p.lead)}</p>`).join('')}</section>`}).join('');
}
function renderBar(){
  const bar=$('markupBar');if(!bar)return;
  const keep=focusKey(document.activeElement);
  const L=state.layers;
  const tagsN=tagCount(),groupsN=topicGroupsCached().length;
  const chips=LAYER_DEFS.filter(d=>d.key!=='tags').map(d=>{
    const n=countFor(d.key);
    if(!n)return '';
    return `<button type="button" class="mk-chip${L[d.key]==='off'?' is-off':''}" data-mk-chip="${d.key}" aria-pressed="${L[d.key]!=='off'}"><i style="background:${(TYPE[d.key]||{color:'#2d8a50'}).color}"></i>${E(d.label)} <b>${n}</b></button>`;
  }).join('')+(tagsN?`<button type="button" class="mk-chip${L.tags==='off'?' is-off':''}" data-mk-chip="tags" aria-pressed="${L.tags!=='off'}"><i style="background:#2d8a50"></i>Tags <b>${tagsN}</b></button>`:'');
  const countOf=d=>d.key==='tags'?tagsN:countFor(d.key);
  const live=LAYER_DEFS.filter(d=>countOf(d)>0),liveOn=live.filter(d=>L[d.key]!=='off').length;
  const rows=LAYER_DEFS.map(d=>`<div class="mk-lr${countOf(d)?'':' is-empty'}"><b>${E(d.label)}</b><span class="mk-lc">${countOf(d)||'—'}</span><span class="mk-seg" role="group" aria-label="${E(d.label)} layer">${d.states.map(s=>`<button type="button"${countOf(d)?'':' disabled'} data-mk-layer="${d.key}" data-mk-state="${s}" aria-pressed="${L[d.key]===s}">${STATE_LABEL[s]}</button>`).join('')}</span></div>`).join('');
  const topicRow=state.topics.length?`<div class="mk-row mk-row2 mk-topics" role="group" aria-label="Topics"><span class="mk-lbl">Topics</span>${state.topics.map(t=>`<button type="button" class="mk-topic" data-mk-topic="${E(t.key)}" aria-pressed="${state.topicSel.includes(t.key)}" style="--c:${t.color}" title="${t.paras} paragraph${t.paras===1?'':'s'}"><i></i>${E(t.label)}</button>`).join('')}<span class="mk-sp"></span><button type="button" class="mk-btn" data-mk-act="fold" aria-pressed="${state.foldOthers}"${state.topicSel.length?'':' disabled'}>${state.foldOthers?'Show all paragraphs':'Show only selected'}</button>${state.topicSel.length?'<button type="button" class="mk-btn" data-mk-act="topics-clear">Clear topics</button>':''}</div>`:'';
  bar.classList.toggle('is-open',!!state.barOpen);
  const hi=headerInfo(readerState.payload),hdr=[hi.outcome&&`<span class="mk-hp is-outcome">${E(hi.outcome)}</span>`,hi.judge&&`<span class="mk-hp">${E(clip(hi.judge.replace(/^The Honourable\s+(Mr\.?|Madam|Mrs\.?|Ms\.?)?\s*Justice\s+/i,'Justice '),40))}</span>`,hi.file&&`<span class="mk-hp">${E(hi.file)}</span>`].filter(Boolean).join('');
  bar.innerHTML=(hdr?`<div class="mk-row mk-hdr">${hdr}</div>`:'')+`<div class="mk-row"><button type="button" class="mk-btn" data-mk-act="layers" aria-expanded="${!!state.layersOpen}">Layers ▾ <small>${liveOn} of ${live.length}</small></button><button type="button" class="mk-btn mk-more" data-mk-act="more" aria-expanded="${!!state.barOpen}">${state.barOpen?'Fewer tools ▴':'Find · Topics · More ▾'}</button>${chips}<span class="mk-sp"></span><button type="button" class="mk-btn" data-mk-act="expand">Expand all</button><button type="button" class="mk-btn" data-mk-act="collapse">Collapse all</button></div>`+
  `${groupsN?`<div class="mk-row mk-row2 mk-viewrow"><span class="mk-seg" role="group" aria-label="Reading order or by topic"><button type="button" data-mk-act="view-reading" aria-pressed="${state.view==='reading'}">Reading order</button><button type="button" data-mk-act="view-topic" aria-pressed="${state.view==='topic'}">By topic</button></span>${state.view==='topic'?`<span class="mk-sp"></span><button type="button" class="mk-btn" data-mk-act="topic-fold">Fold all</button><button type="button" class="mk-btn" data-mk-act="topic-unfold">Unfold all</button>`:''}</div>`:''}<div class="mk-row mk-row2"><label class="mk-find"><span class="mk-find-ico" aria-hidden="true">⌕</span><input type="search" id="markupFind" placeholder="Find in this case" value="${E(state.findTerm)}" aria-label="Find in this case"><span id="markupFindCount" class="mk-find-count" aria-live="polite"></span></label><button type="button" class="mk-btn" data-mk-act="info" aria-expanded="${state.infoOpen}">Case info ▾</button><button type="button" class="mk-btn" data-mk-act="outline" aria-expanded="${state.outlineOpen}">Outline</button><span class="mk-sp"></span><button type="button" class="mk-btn" data-mk-act="experimental" aria-pressed="${typeof experimentalState!=='undefined'&&!!experimentalState.on}" title="Show or hide the unfinished reader tools (summary cards, paragraph assessments, similar paragraphs)">Experimental</button><button type="button" class="mk-btn" data-mk-act="export" title="Word file of this case with the margin notes as comments">Export to Word</button><button type="button" class="mk-btn" data-mk-act="print">Print annotated</button></div>`+topicRow+
  `<div class="mk-pop" id="markupLayerPop"${state.layersOpen?'':' hidden'}><div class="mk-pop-h">Margin layers<small>Off · Markers (collapsed pills) · Open (full bubbles). Tags: Underline · Tint · Bubbles.</small></div>${rows}<div class="mk-pop-f"><button type="button" class="mk-btn" data-mk-act="showall">Show all layers</button><button type="button" class="mk-btn" data-mk-act="reset">Reset</button><span>Click a pill or bubble to open or fold just that note.</span></div></div>`;
  if(keep){const f=bar.querySelector(keep.sel);if(f){f.focus({preventScroll:true});if(keep.s!=null){try{f.setSelectionRange(keep.s,keep.e)}catch(e){}}}}
  updateFindCount();
  const lb=bar.querySelector('[data-mk-act="layers"]');if(lb)bar.style.setProperty('--mk-pop-top',(lb.offsetTop+lb.offsetHeight+6)+'px');
  const p=panel();if(p)p.style.setProperty('--mk-bar-h',bar.offsetHeight+'px');
}
const isShown=el=>!!el&&el.getClientRects().length>0;
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
/* A quoted paragraph: trimmed with a "Show full paragraph" toggle when it is long. */
function qBlock(text,label,id,max){
  const t=String(text||'');if(!t)return '';
  const long=t.length>max,open=!!(state.qopen&&state.qopen[id]);
  return `<blockquote>${E(long&&!open?clip(t,max):t)}${long?` <button type="button" class="mk-link mk-qx" data-mk-qx="${E(id)}" aria-expanded="${open}">${open?'Show less':'Show full paragraph'}</button>`:''}${label?`<small>${E(label)}</small>`:''}</blockquote>`;
}
function noteHTML(n,st){
  const t=TYPE[n.type];
  if(st==='markers'||(st==='off'))return `<button type="button" class="mk-pill" data-mk-note="${E(n.id)}" aria-expanded="false" title="${E(n.title)}"><i style="background:${t.color}"></i>${E(n.pill)}</button>`;
  const subs=n.subs&&n.subs.length?`<div class="mk-subs">${n.subs.map(s=>`<div class="mk-sub" style="--c:${s.color}"><b>¶[${s.first}]${s.last!==s.first?'–['+s.last+']':''}</b><span>${E(s.terms.join(' · '))}</span><div>${s.roles.map(r=>`<em>${E(r)}</em>`).join('')}</div></div>`).join('')}</div>`:'';
  const foot=(n.foot||[]).map(f=>`<button type="button" class="mk-link" data-mk-foot="${E(f.action)}" data-mk-arg="${E(f.arg)}">${E(f.label)}</button>`).join('');
  return `<div class="mk-card ${n.type}${n.unverified?' is-unverified':''}" style="--c:${t.color}" data-mk-note="${E(n.id)}"><div class="mk-card-t"><i style="background:${t.color}"></i>${E(t.label)}${n.loc!=null?`<span class="mk-loc">¶[${E(n.loc)}]</span>`:''}<button type="button" class="mk-x" data-mk-fold="${E(n.id)}" aria-label="Fold this note">✕</button></div><h4>${E(n.title)}</h4>${n.meta?`<div class="mk-meta">${E(n.meta)}</div>`:''}${n.alsoAt&&n.alsoAt.length?`<div class="mk-meta">also cited at ${n.alsoAt.map(x=>'¶['+E(x)+']').join(', ')}</div>`:''}${n.quote?qBlock(n.quote,n.quoteLabel,n.id,420):''}${n.body?`<div class="mk-body">${E(n.body)}</div>`:''}${subs}${foot?`<div class="mk-foot">${foot}</div>`:''}</div>`;
}
/* Fold view: topic emphasis and "show only selected" with fold bars for the hidden runs. */
function clearFold(){
  const d=$('decisionBody');if(!d)return;
  d.querySelectorAll('.mk-folded').forEach(e=>e.classList.remove('mk-folded'));
  d.querySelectorAll('.mk-foldbar').forEach(e=>e.remove());
  d.querySelectorAll('.mk-topic-hit').forEach(e=>{e.classList.remove('mk-topic-hit');e.style.removeProperty('--tc')});
}
function applyFold(){
  clearFold();
  const dec=document.querySelector('#decisionBody .fmt-decision');if(!dec||!state.topicSel.length)return;
  const paras=[...dec.querySelectorAll(':scope > .fmt-para')];
  const hit=topicParas(state.topics,state.topicSel);
  for(const e of paras){
    const n=Number(e.dataset.para);if(!hit.has(n))continue;
    const t=state.topics.find(x=>state.topicSel.includes(x.key)&&x.ranges.some(r=>n>=r.first&&n<=r.last));
    e.classList.add('mk-topic-hit');if(t)e.style.setProperty('--tc',t.color);
  }
  if(!state.foldOthers)return;
  const vis=paras.map(e=>hit.has(Number(e.dataset.para))||state.unfolded.includes(Number(e.dataset.para)));
  for(const run of foldRuns(vis)){
    const a=Number(paras[run.start].dataset.para),b=Number(paras[run.end].dataset.para),cnt=run.end-run.start+1;
    const bar=document.createElement('button');bar.type='button';bar.className='mk-foldbar';bar.dataset.mkUnfold=paras.slice(run.start,run.end+1).map(e=>e.dataset.para).join(',');
    bar.textContent=`¶[${a}]${b!==a?'–['+b+']':''} · ${cnt} paragraph${cnt===1?'':'s'} hidden · show`;
    dec.insertBefore(bar,paras[run.start]);
    for(let i=run.start;i<=run.end;i++)paras[i].classList.add('mk-folded');
  }
}
function render(){
  const stage=$('markupStage');if(!stage||!readerState.payload)return;   /* a case switch can leave a render queued with no payload */
  applyFold();
  applyMine();
  renderBar();
  renderTopicView();
  if(state.view==='topic'&&topicGroupsCached().length){const p0=panel();if(p0)p0.classList.toggle('markup-info-open',state.infoOpen);return}
  const body=$('decisionBody'),margin=$('markupMargin'),svg=$('markupConn');
  /* tag style changes line wrapping, so it must be applied before anything is measured */
  body.classList.remove('mk-tags-off','mk-tags-underline','mk-tags-tint','mk-tags-bubbles');
  body.classList.add('mk-tags-'+state.layers.tags);
  body.querySelectorAll('.mk-pn').forEach(e=>e.remove());
  /* where each citation sits in this decision (the stored offsets are per chunk, so read the placed paragraph) and where else the same case is cited */
  const placed={};
  for(const n of state.notes){
    if(!n.cite)continue;
    const el=anchorEl(n),p=el&&el.closest&&el.closest('.fmt-para');
    n.loc=p&&p.dataset.para!=null?Number(p.dataset.para):null;
    if(n.cite.caseId&&n.loc!=null)(placed[n.cite.caseId]=placed[n.cite.caseId]||[]).push({id:n.id,para:n.loc});
  }
  for(const n of state.notes)if(n.cite)n.alsoAt=n.cite.caseId?(placed[n.cite.caseId]||[]).filter(x=>x.id!==n.id).map(x=>x.para).filter((v,i,a)=>a.indexOf(v)===i):[];
  const stateOf=n=>{const st=noteState(n,state.layers,state.overrides);return state.printing&&n.type!=='citedby'&&st!=='off'?'open':st};
  const wanted=state.notes.filter(n=>{const st=stateOf(n);return n.type==='citedby'?st==='open':st!=='off'});
  [...margin.querySelectorAll('.mk-note')].forEach(e=>e.remove());
  const frag=document.createDocumentFragment(),els=[];
  for(const n of wanted){
    const a=anchorEl(n);if(!a||!isShown(a))continue;
    const st=stateOf(n);
    const el=document.createElement('div');el.className='mk-note';el.dataset.id=n.id;el.innerHTML=noteHTML(n,st);
    frag.appendChild(el);els.push({n,el,a,st});
  }
  margin.appendChild(frag);                       /* one write, then reads: no layout thrash on long cases */
  const base=margin.getBoundingClientRect(),bodyR=body.getBoundingClientRect();
  const items=els.map(o=>({y:o.a.getBoundingClientRect().top-base.top-2,h:o.el.offsetHeight}));
  const lay=layoutNotes(items,8);
  let bottom=0,g='';
  const rowSeen={};
  for(const l of lay){
    const o=els[l.index];o.el.style.top=l.top+'px';bottom=Math.max(bottom,l.top+items[l.index].h);
    if(o.n.anchor.kind==='cite'){
      /* the line starts at this citation's own text: a dot at the end of its first line, a leader in the gap under that line to the margin, so two citations on one line never share a start point */
      const rs=o.a.getClientRects(),r0=rs.length?rs[0]:o.a.getBoundingClientRect(),col=TYPE[o.n.type].color;
      /* the leader runs in the gap under the text line, not through the words */
      const ay=Math.round((r0.bottom+1-base.top)*10)/10,ax=r0.right-base.left,ty=l.top+(o.st==='open'?16:12);
      const rowKey=Math.round(ay/8),k=rowSeen[rowKey]=(rowSeen[rowKey]||0)+1;
      const elbow=Math.max(ax,bodyR.right-base.left-2)+(k-1)*5;
      const op=o.st==='open'?.85:.4,sw=o.st==='open'?1.4:1;
      g+=`<path d="M${ax} ${ay} H${elbow} L-4 ${ty}" fill="none" stroke="${col}" stroke-width="${sw}" opacity="${op}"/><circle cx="${ax}" cy="${ay}" r="2.4" fill="${col}" opacity="${Math.max(op,.6)}"/>`;
    }
  }
  if(state.printing){
    /* numbered markers in the text and matching numbers on the margin comments, in reading order */
    lay.forEach((l,i)=>{const o=els[l.index],n=i+1;o.el.dataset.n=n;
      const sup=document.createElement('span');sup.className='mk-pn';sup.textContent=n;sup.style.setProperty('--c',TYPE[o.n.type].color);
      /* inside the anchor itself, never as a new sibling: some blocks lay their children out in a grid */
      const host=o.n.anchor.kind==='cite'?o.a:(o.n.anchor.kind==='para'?o.a.querySelector('.fmt-para-num'):null);
      if(host)host.appendChild(sup);});
  }
  const ph=$('markupPrintHead');
  if(ph){const hi=headerInfo(readerState.payload),it=(readerState.payload&&readerState.payload.item)||{},on=LAYER_DEFS.filter(d=>state.layers[d.key]!=='off'&&(d.key==='tags'?tagCount():countFor(d.key))).map(d=>d.label);
    ph.innerHTML=`<b>${E(it.title||'')}</b> · ${E([it.citation,it.court,hi.judge,it.date&&String(it.date).slice(0,10),hi.outcome].filter(Boolean).join(' · '))}<span>Annotated copy · layers: ${E(on.join(', ')||'none')}</span>`}
  stage.style.minHeight=Math.max(bottom+24,body.offsetHeight)+'px';
  svg.setAttribute('width',Math.max(margin.offsetWidth,1));svg.setAttribute('height',Math.max(bottom+24,body.offsetHeight));
  svg.style.left=0;svg.innerHTML=g;
  renderBands(stage,base);
  renderMini();
  renderOutline();
  renderPanel();
  const p=panel();
  p.classList.toggle('markup-info-open',state.infoOpen);
  const ob=$('markupOutline');if(ob)ob.hidden=!state.outlineOpen;
}
/* ---------- private notes: paragraph highlight, inline copy on narrow screens, editor ---------- */
function cleanMine(){
  const d=$('decisionBody');if(!d)return;
  d.querySelectorAll('.mk-mine-hl').forEach(e=>e.classList.remove('mk-mine-hl'));
  d.querySelectorAll('.mk-mine-inline').forEach(e=>e.remove());
}
function decorateNums(on){
  const d=$('decisionBody');if(!d)return;
  d.querySelectorAll('.fmt-para-num').forEach(e=>{
    const p=e.closest('.fmt-para'),n=p&&p.dataset.para;
    if(on&&n){e.classList.add('mk-num');e.tabIndex=0;e.setAttribute('role','button');e.setAttribute('aria-label','Add or edit my note on paragraph '+n);e.title='Add a private note to ¶'+n}
    else{e.classList.remove('mk-num');e.removeAttribute('tabindex');e.removeAttribute('role');e.removeAttribute('aria-label');e.removeAttribute('title')}
  });
}
function applyMine(){
  cleanMine();decorateNums(true);
  const d=$('decisionBody');if(!d||state.layers.mine==='off')return;
  for(const m of state.mine){
    const p=d.querySelector(`.fmt-para[data-para="${m.para}"]`);if(!p)continue;
    if(m.hl)p.classList.add('mk-mine-hl');
    if(String(m.text||'').trim()){
      const el=document.createElement('div');el.className='mk-mine-inline';
      el.innerHTML=`<b>My note · ¶[${E(m.para)}]</b>${E(m.text)}<button type="button" class="mk-link" data-mk-foot="mine-edit" data-mk-arg="${E(m.para)}">Edit</button>`;
      p.insertAdjacentElement('afterend',el);
    }
  }
}
function closeEditor(){const e=$('mkEditor');if(e)e.remove();state.editing=null}
function openEditor(num){
  num=Number(num);if(!(num>0))return;
  const had=state.mine.find(x=>Number(x.para)===num),m=had||{text:'',hl:false};
  closeEditor();state.editing={para:num,existing:!!had};
  const ed=document.createElement('div');ed.id='mkEditor';ed.setAttribute('role','dialog');ed.setAttribute('aria-label','My note on paragraph '+num);
  ed.innerHTML=`<div class="mk-card-t"><i style="background:${TYPE.mine.color}"></i>My note · ¶[${num}]<button type="button" class="mk-x" data-mk-ed="cancel" aria-label="Close">✕</button></div><textarea id="mkEditorText" maxlength="${MINE_TEXT}" rows="4" placeholder="Private note" aria-label="Note text"></textarea><label class="mk-hlbox"><input type="checkbox" id="mkEditorHl"> Highlight this paragraph</label><div class="mk-foot"><button type="button" class="mk-btn mk-primary" data-mk-ed="save">Save</button><button type="button" class="mk-btn" data-mk-ed="cancel">Cancel</button>${had?'<button type="button" class="mk-btn" data-mk-ed="delete">Delete</button>':''}</div><div class="mk-hint">Saved on this computer only. Not shared. Ctrl+Enter saves.</div>`;
  document.body.appendChild(ed);
  $('mkEditorText').value=m.text||'';$('mkEditorHl').checked=!!m.hl;
  const a=document.querySelector(`#decisionBody .fmt-para[data-para="${num}"] .fmt-para-num`);
  if(a){const r=a.getBoundingClientRect(),w=ed.offsetWidth,h=ed.offsetHeight;
    ed.style.left=Math.max(8,Math.min(r.left,window.innerWidth-w-8))+'px';
    ed.style.top=Math.max(8,Math.min(r.bottom+6,window.innerHeight-h-8))+'px'}
  $('mkEditorText').focus();
}
function saveEditor(del){
  if(!state.editing)return;
  const para=state.editing.para,t=$('mkEditorText'),h=$('mkEditorHl');
  state.mine=del?mineUpsert(state.mine,para,'',false):mineUpsert(state.mine,para,t?t.value:'',h&&h.checked);
  mineStore.set(state.caseId,state.mine);
  closeEditor();
  state.notes=state.notes.filter(n=>n.type!=='mine').concat(mineToNotes(state.mine));
  render();
}
/* Word export: the notes whose layers are on, as comments, sent to the server only to be typeset. Nothing is stored there. */
let exportBusy=false;
async function exportWord(btn){
  const rd=readerState&&readerState.payload&&readerState.payload.readerData,cid=state.caseId;
  if(exportBusy||!rd||cid==null)return;
  exportBusy=true;const label=btn?btn.textContent:'';if(btn){btn.disabled=true;btn.textContent='Preparing…'}
  const byNum={};for(const b of rd.format_blocks||[])if(b&&b.type==='para'&&b.num!=null)byNum[b.num]=b.start;
  const blockOf=n=>{
    const a=n.anchor;if(a.kind==='top')return null;
    if(a.kind==='cite'){const el=document.querySelector(`#decisionBody [data-cite-id="${a.id}"]`),p=el&&el.closest('.fmt-para'),m=p&&/decision-source-(\d+)/.exec(p.id||'');return m?Number(m[1]):null}
    if(a.blockStart!=null)return a.blockStart;
    return byNum[a.num]!=null?byNum[a.num]:null;
  };
  const comments=exportPlan(state.notes,state.layers,blockOf).slice(0,3000);
  const highlights=state.mine.filter(m=>m.hl&&byNum[m.para]!=null).map(m=>byNum[m.para]);
  let msg=label;
  try{
    const res=await fetch(`/cases/${encodeURIComponent(cid)}/markup-export`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({comments,highlights})});
    if(!res.ok)throw new Error('HTTP '+res.status);
    const blob=await res.blob(),url=URL.createObjectURL(blob),a=document.createElement('a');
    a.href=url;a.download='ilit-case-'+cid+'-markup.docx';document.body.appendChild(a);a.click();a.remove();
    setTimeout(()=>URL.revokeObjectURL(url),4000);
  }catch(e){msg='Export failed, try again'}
  exportBusy=false;
  if(btn){btn.disabled=false;btn.textContent=msg;if(msg!==label)setTimeout(()=>{if(btn.isConnected)btn.textContent=label},3500)}
}
/* Right-edge overview: the sub-theme colours at document scale, a window for what is on screen, click to jump. */
function renderMini(){
  const mini=$('markupMini'),body=$('decisionBody');if(!mini||!body)return;
  const inner=mini.firstElementChild,subs=state.layers.unit!=='off'?subthemeRanges(readerState.payload):[];
  const br=body.getBoundingClientRect(),H=Math.max(1,br.height);
  const rects=new Map();body.querySelectorAll('.fmt-para').forEach(e=>{if(isShown(e))rects.set(Number(e.dataset.para),e.getBoundingClientRect())});
  inner.innerHTML=subs.map(s=>{const a=rects.get(s.first),b=rects.get(s.last);if(!a||!b)return '';return `<b style="top:${((a.top-br.top)/H*100).toFixed(2)}%;height:${Math.max(.4,(b.bottom-a.top)/H*100).toFixed(2)}%;background:${s.color}"></b>`}).join('');
  mini.hidden=!subs.length;
  updateMini();
}
function updateMini(){
  const mini=$('markupMini'),body=$('decisionBody');if(!mini||mini.hidden||!body)return;
  const vp=mini.querySelector('.mk-mini-vp'),br=body.getBoundingClientRect(),H=Math.max(1,br.height);
  const top=Math.max(0,-br.top)/H*100,h=Math.min(100-top,window.innerHeight/H*100);
  vp.style.top=top.toFixed(2)+'%';vp.style.height=Math.max(1,h).toFixed(2)+'%';
}
function renderBands(stage,base){
  const bands=$('markupBands');if(!bands)return;
  bands.innerHTML='';
  const sb=bands.getBoundingClientRect();
  const subs=subthemeRanges(readerState.payload);
  const body=$('decisionBody');
  const rects=new Map();body.querySelectorAll('.fmt-para').forEach(e=>{if(isShown(e))rects.set(Number(e.dataset.para),e.getBoundingClientRect())});
  if(state.layers.unit!=='off'){
    for(const s of subs){
      const a=rects.get(s.first),b=rects.get(s.last);if(!a||!b)continue;
      const d=document.createElement('div');d.className='mk-band';d.style.cssText=`top:${a.top-sb.top}px;height:${Math.max(4,b.bottom-a.top)}px;background:${s.color}`;
      d.title=`Sub-theme ¶${s.first}–${s.last}: ${s.terms.join(', ')}`;bands.appendChild(d);
    }
  }
  if(state.layers.citedby!=='off'){
    const rd=readerState.payload.readerData||{},max=Math.max(1,...(rd.format_blocks||[]).map(b=>Number(b.cited_by_count)||0));
    for(const b of rd.format_blocks||[]){
      const c=Number(b&&b.cited_by_count)||0;if(b.type!=='para'||c<=0)continue;
      const e=body.querySelector(`[id="decision-source-${b.start}"]`);if(!e||!isShown(e))continue;const r=e.getBoundingClientRect();
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
  const chars=Array.from(text);
  const heads=blocks.filter(b=>b.type==='heading').map(b=>({start:b.start,level:b.level||1,label:chars.slice(b.start,b.end).join('').trim()}));
  const subs=subthemeRanges(readerState.payload);
  const rows=heads.map(h=>`<button type="button" class="mk-ol l${Math.min(h.level,3)}" data-mk-goto="${h.start}">${E(clip(h.label,60))}</button>`);
  const subRows=subs.map(s=>`<button type="button" class="mk-ol sub" data-mk-para="${s.first}" style="--c:${s.color}"><i></i>${E(s.terms.slice(0,3).join(', ')||s.id)}<em>¶${s.first}${s.last!==s.first?'–'+s.last:''}</em></button>`);
  box.innerHTML=`<h5>Outline</h5>${rows.join('')||'<div class="mk-meta">No headings recognised.</div>'}${subRows.length?`<h5>Sub-themes</h5>${subRows.join('')}<div class="mk-meta">Automatic key terms; headings are the judgment’s own.</div>`:''}`;
}
function goto(el){
  if(!el)return;
  const f=el.closest&&el.closest('.mk-folded');if(f||el.classList.contains('mk-folded')){const n=Number((f||el).dataset.para);if(n&&!state.unfolded.includes(n)){state.unfolded.push(n);render();}}
  el.scrollIntoView({behavior:window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'center'});
}

/* ---------- Peek panel (stored data only) ---------- */
function pinNote(id){
  const n=state.notes.find(x=>x.id===id&&x.cite);if(!n)return;
  state.pins=[id].concat(state.pins.filter(x=>x!==id)).slice(0,5);
  hideHover(true);renderPanel();
}
function renderPanel(){
  let el=$('mkPanel');const p=panel();
  if(!state.on||!state.pins.length){if(el)el.remove();if(p)p.classList.remove('markup-docked','markup-peeking');return}
  const cards=state.pins.map(id=>peekFor(state.notes.find(n=>n.id===id))).filter(Boolean);
  if(!cards.length){state.pins=[];if(el)el.remove();if(p)p.classList.remove('markup-peeking');return}
  if(!el){el=document.createElement('aside');el.id='mkPanel';el.setAttribute('aria-label','Citation peek panel');document.body.appendChild(el)}
  el.className='mk-panel '+state.dock;
  el.innerHTML=`<div class="mk-panel-h" data-mk-drag><b>Peek · ${cards.length} citation${cards.length===1?'':'s'}</b><span class="mk-sp"></span><button type="button" class="mk-btn" data-mk-act="dock">${state.dock==='dock'?'Float':'Dock to bottom'}</button><button type="button" class="mk-btn" data-mk-act="clearpins">Close all</button></div><div class="mk-panel-b">${cards.map((c,i)=>{const open=i===0||state.peekOpen.includes(c.id);const short=shortCaseName(c.title)+(c.paragraph!=null?' ¶'+c.paragraph:'');return open?`<article class="mk-peek${c.inLibrary?'':' is-missing'}"><div class="mk-card-t" data-mk-peek-toggle="${E(c.id)}" title="Click to collapse"><i style="background:${TYPE.cite.color}"></i>Citation<button type="button" class="mk-x" data-mk-unpin="${E(c.id)}" aria-label="Close this peek">✕</button></div><h4>${E(c.title)}</h4><div class="mk-meta">${E([c.citation,c.paragraph!=null?'¶['+c.paragraph+']':''].filter(Boolean).join(' · '))}</div>${c.inLibrary?(c.text?qBlock(c.text,c.label,c.id,900):`<div class="mk-body">${E(c.noText||'No paragraph text is stored for this pinpoint.')}</div>`):`<div class="mk-body">${E(c.missing)}</div>`}${c.citedBy?`<div class="mk-cb">${E(c.citedBy)}</div>`:''}<div class="mk-foot"><button type="button" class="mk-link" data-mk-goto-cite="${E(c.id)}">${c.loc!=null?`Back to ¶[${E(c.loc)}]`:'Go to citation'}</button>${c.inLibrary?`<button type="button" class="mk-link" data-mk-foot="open-case" data-mk-arg="${E(c.caseId)}">Open case</button>`:''}</div></article>`:`<article class="mk-peek is-collapsed"><button type="button" class="mk-peek-row" data-mk-peek-toggle="${E(c.id)}"><i style="background:${TYPE.cite.color}"></i><b>${E(clip(short,40))}</b><small>expand ▾</small></button><button type="button" class="mk-x" data-mk-unpin="${E(c.id)}" aria-label="Close this peek">✕</button></article>`}).join('')}</div>`;
  if(state.dock==='float'&&state.panelPos){el.style.left=state.panelPos.x+'px';el.style.top=state.panelPos.y+'px';el.style.right='auto';el.style.bottom='auto'}
  if(p){p.classList.toggle('markup-docked',state.dock==='dock');p.classList.add('markup-peeking')}
}

/* ---------- hover card ---------- */
let showT=null,hideT=null;
function hideHover(now){
  clearTimeout(showT);clearTimeout(hideT);
  const kill=()=>{const h=$('mkHover');if(h)h.remove()};
  if(now)kill();else hideT=setTimeout(kill,220);
}
function showHover(span){
  const n=state.notes.find(x=>x.id==='cite-'+span.dataset.citeId&&x.cite);if(!n)return;
  const c=peekFor(n);let h=$('mkHover');if(h)h.remove();
  h=document.createElement('div');h.id='mkHover';h.setAttribute('role','tooltip');
  h.innerHTML=`<div class="mk-card-t"><i style="background:${TYPE.cite.color}"></i>Citation</div><h4>${E(c.title)}</h4><div class="mk-meta">${E([c.citation,c.paragraph!=null?'¶['+c.paragraph+']':''].filter(Boolean).join(' · '))}</div>${c.inLibrary?(c.text?`<blockquote>${E(clip(c.text,320))}<small>${E(c.label)}${c.text.length>320?' · click for the full paragraph':''}</small></blockquote>`:`<div class="mk-body">${E(c.noText||'')}</div>`):`<div class="mk-body">${E(c.missing)}</div>`}${c.citedBy?`<div class="mk-cb">${E(c.citedBy)}</div>`:''}<div class="mk-foot"><button type="button" class="mk-link" data-mk-foot="pin" data-mk-arg="${E(c.id)}">Peek in panel</button>${c.inLibrary?`<button type="button" class="mk-link" data-mk-foot="open-case" data-mk-arg="${E(c.caseId)}">Open case</button>`:''}<span class="mk-hint">Click: note · Shift-click: peek</span></div>`;
  document.body.appendChild(h);
  const r=span.getBoundingClientRect(),w=h.offsetWidth,hh=h.offsetHeight;
  const left=Math.max(8,Math.min(r.left,window.innerWidth-w-8));
  let top=r.bottom+6;if(top+hh>window.innerHeight-8)top=Math.max(8,r.top-hh-6);
  h.style.left=left+'px';h.style.top=top+'px';
}
function scheduleHover(span){if(window.matchMedia&&window.matchMedia('(hover: none)').matches)return;clearTimeout(hideT);clearTimeout(showT);showT=setTimeout(()=>showHover(span),180)}

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
const marginHidden=()=>{const m=$('markupMargin');return !m||getComputedStyle(m).display==='none'};
function citeActivate(c,ev){
  const id='cite-'+c.dataset.citeId;
  if(!state.notes.some(n=>n.id===id))return false;
  if(ev.shiftKey||marginHidden()){pinNote(id);return true}
  const cur=noteState(state.notes.find(n=>n.id===id),state.layers,state.overrides);
  state.overrides[id]=cur!=='open';render();
  const target=document.querySelector(`.mk-note[data-id="${id}"]`);if(target&&cur!=='open')target.scrollIntoView({block:'nearest'});
  return true;
}
document.addEventListener('click',ev=>{
  if(!state.on){const t=ev.target.closest&&ev.target.closest('#readerMarkupToggle');if(t){ev.preventDefault();setOn(true)}return}
  const t=ev.target;if(!t.closest)return;
  if(t.closest('#readerMarkupToggle')){ev.preventDefault();setOn(false);return}
  if(t.closest('#readerViewToggle')){setOn(false);return}
  if(state.infoOpen&&!t.closest('#decisionTarget,[data-mk-act="info"]')){state.infoOpen=false;render()}
  if(state.layersOpen&&!t.closest('#markupLayerPop,[data-mk-act="layers"]')){state.layersOpen=false;render()}
  const chip=t.closest('[data-mk-chip]');
  if(chip){const k=chip.dataset.mkChip,d=LAYER_DEFS.find(x=>x.key===k),on=state.layers[k]!=='off';setLayer(k,on?'off':(k==='citedby'?'gutter':d.def==='off'?(d.states[1]):d.def));return}
  const ls=t.closest('[data-mk-layer]');if(ls){setLayer(ls.dataset.mkLayer,ls.dataset.mkState);return}
  const tp=t.closest('[data-mk-topic]');
  if(tp){const k=tp.dataset.mkTopic,i=state.topicSel.indexOf(k);if(i>=0)state.topicSel.splice(i,1);else state.topicSel.push(k);if(!state.topicSel.length)state.foldOthers=false;state.unfolded=[];render();return}
  const tg=t.closest('[data-mk-tg]');
  if(tg){const i=Number(tg.dataset.mkTg),at=state.topicOpen.indexOf(i);if(at>=0)state.topicOpen.splice(at,1);else state.topicOpen.push(i);render();return}
  const tgo=t.closest('[data-mk-tgo]');
  if(tgo){const n=tgo.dataset.mkTgo;state.view='reading';render();const e=$('decisionBody').querySelector(`.fmt-para[data-para="${n}"]`);if(e)goto(e);return}
  const ed=t.closest('[data-mk-ed]');
  if(ed){const k=ed.dataset.mkEd;if(k==='save')saveEditor(false);else if(k==='delete')saveEditor(true);else closeEditor();return}
  const num=t.closest('#decisionBody .fmt-para-num.mk-num');
  if(num){openEditor(num.closest('.fmt-para').dataset.para);return}
  if(state.editing&&!t.closest('#mkEditor'))closeEditor();
  const act=t.closest('[data-mk-act]');
  if(act){
    const a=act.dataset.mkAct;
    if(a==='layers'){state.layersOpen=!state.layersOpen;render()}
    else if(a==='expand'){for(const d of LAYER_DEFS)if(d.states.includes('open'))state.layers[d.key]='open';state.overrides={};persist();render()}
    else if(a==='collapse'){for(const d of LAYER_DEFS)if(d.states.includes('open'))state.layers[d.key]='markers';state.overrides={};persist();render()}
    else if(a==='view-topic'){state.view='topic';render()}
    else if(a==='view-reading'){state.view='reading';render()}
    else if(a==='topic-fold'){state.topicOpen=[];render()}
    else if(a==='topic-unfold'){state.topicOpen=topicGroupsCached().map((g,i)=>i);render()}
    else if(a==='showall'){for(const d of LAYER_DEFS)if(state.layers[d.key]==='off')state.layers[d.key]=d.def;persist();render()}
    else if(a==='reset'){state.layers=defaultLayers();state.overrides={};persist();render()}
    else if(a==='info'){state.infoOpen=!state.infoOpen;render();if(state.infoOpen){const d=$('decisionTarget');if(d)d.scrollTop=0}}
    else if(a==='more'){state.barOpen=!state.barOpen;render()}
    else if(a==='outline'){state.outlineOpen=!state.outlineOpen;render()}
    else if(a==='experimental'){if(typeof setReaderExperimental==='function')setReaderExperimental(!(typeof experimentalState!=='undefined'&&experimentalState.on));render()}
    else if(a==='print'){window.print()}
    else if(a==='export'){exportWord(act)}
    else if(a==='fold'){state.foldOthers=!state.foldOthers;state.unfolded=[];render()}
    else if(a==='topics-clear'){state.topicSel=[];state.foldOthers=false;state.unfolded=[];render()}
    else if(a==='dock'){state.dock=state.dock==='dock'?'float':'dock';render()}
    else if(a==='clearpins'){state.pins=[];render()}
    return;
  }
  const uf=t.closest('[data-mk-unfold]');
  if(uf){for(const n of uf.dataset.mkUnfold.split(',').map(Number))if(!state.unfolded.includes(n))state.unfolded.push(n);render();return}
  const pk=t.closest('[data-mk-peek-toggle]');
  if(pk&&!t.closest('[data-mk-unpin]')){const id=pk.dataset.mkPeekToggle,i=state.peekOpen.indexOf(id);if(i>=0)state.peekOpen.splice(i,1);else state.peekOpen.push(id);renderPanel();return}
  const unpin=t.closest('[data-mk-unpin]');if(unpin){state.pins=state.pins.filter(x=>x!==unpin.dataset.mkUnpin);render();return}
  const gc=t.closest('[data-mk-goto-cite]');
  if(gc){const n=state.notes.find(x=>x.id===gc.dataset.mkGotoCite);const a=n&&anchorEl(n);if(a)goto(a);return}
  const fold=t.closest('[data-mk-fold]');if(fold){state.overrides[fold.dataset.mkFold]=false;render();return}
  const foot=t.closest('[data-mk-foot]');
  if(foot){
    if(foot.dataset.mkFoot==='pin'){pinNote(foot.dataset.mkArg);return}
    if(foot.dataset.mkFoot==='mine-edit'){openEditor(foot.dataset.mkArg);return}
    if(foot.dataset.mkFoot==='goto-para'){const e=$('decisionBody').querySelector(`.fmt-para[data-para="${foot.dataset.mkArg}"]`);if(e)goto(e);return}
    if(foot.dataset.mkFoot==='judge-profile'){const tab=document.querySelector('[data-tab="judge-profile"]');if(tab){setOn(false);tab.click();const q=$('judgeProfileQuery');if(q){q.value=foot.dataset.mkArg||'';q.dispatchEvent(new Event('input',{bubbles:true}))}}return}
    if(foot.dataset.mkFoot==='open-url'){if(/^https:\/\//i.test(foot.dataset.mkArg||''))window.open(foot.dataset.mkArg,'_blank','noopener,noreferrer');return}
    if(foot.dataset.mkFoot==='open-case'&&typeof openDecision==='function'){setOn(false);openDecision(Number(foot.dataset.mkArg))}return}
  const qx=t.closest('[data-mk-qx]');if(qx){const k=qx.dataset.mkQx;state.qopen[k]=!state.qopen[k];render();renderPanel();return}
  const go=t.closest('[data-mk-goto]');if(go){goto($('decisionBody').querySelector(`[id="decision-source-${go.dataset.mkGoto}"]`));return}
  const gp=t.closest('[data-mk-para]');if(gp){goto($('decisionBody').querySelector(`.fmt-para[data-para="${gp.dataset.mkPara}"]`));return}
  const pill=t.closest('.mk-pill[data-mk-note],.mk-heat[data-mk-note]');
  if(pill){const id=pill.dataset.mkNote;state.overrides[id]=true;render();return}
},false);
/* A citation click in markup mode toggles its note (Shift-click pins it to the Peek panel) instead of opening the linked-case pane. */
document.addEventListener('click',ev=>{
  if(!state.on)return;const c=ev.target.closest&&ev.target.closest('#decisionBody [data-cite-id]');
  if(!c)return;
  ev.stopPropagation();
  citeActivate(c,ev);
},true);
document.addEventListener('mousedown',ev=>{
  /* Shift-click on a citation pins it; stop the browser extending a text selection instead */
  if(state.on&&ev.shiftKey&&ev.target.closest&&ev.target.closest('#decisionBody [data-cite-id]'))ev.preventDefault();
},true);
document.addEventListener('mouseover',ev=>{
  if(!state.on||!ev.target.closest)return;
  const c=ev.target.closest('#decisionBody [data-cite-id]');
  if(c){scheduleHover(c);return}
  if(ev.target.closest('#mkHover'))clearTimeout(hideT);
});
document.addEventListener('mouseout',ev=>{
  if(!state.on||!ev.target.closest)return;
  if(ev.target.closest('#decisionBody [data-cite-id],#mkHover')){clearTimeout(showT);hideHover(false)}
});
document.addEventListener('focusin',ev=>{
  if(!state.on||!ev.target.closest)return;
  const c=ev.target.closest('#decisionBody [data-cite-id]');
  if(c)scheduleHover(c);else if(!ev.target.closest('#mkHover'))hideHover(true);
});
document.addEventListener('input',ev=>{if(ev.target&&ev.target.id==='markupFind')runFind(ev.target.value)});
document.addEventListener('keydown',ev=>{
  if(!state.on)return;
  if(ev.target.closest&&ev.target.closest('#mkEditor')){
    if(ev.key==='Escape')closeEditor();else if(ev.key==='Enter'&&(ev.ctrlKey||ev.metaKey)){ev.preventDefault();saveEditor(false)}
    ev.stopPropagation();return;
  }
  const nb=ev.target.closest&&ev.target.closest('#decisionBody .fmt-para-num.mk-num');
  if(nb&&(ev.key==='Enter'||ev.key===' ')&&!ev.ctrlKey&&!ev.metaKey&&!ev.altKey){ev.preventDefault();ev.stopPropagation();openEditor(nb.closest('.fmt-para').dataset.para);return}
  const c=ev.target.closest&&ev.target.closest('#decisionBody [data-cite-id]');
  if(c&&(ev.key==='Enter'||ev.key===' ')&&!ev.ctrlKey&&!ev.metaKey&&!ev.altKey){ev.preventDefault();ev.stopPropagation();citeActivate(c,ev);return}
  if((ev.metaKey||ev.ctrlKey)&&ev.key.toLowerCase()==='k'){ev.preventDefault();const f=$('markupFind');if(f)f.focus();return}
  if(ev.target&&ev.target.id==='markupFind'&&ev.key==='Enter'&&state.findHits.length){ev.preventDefault();state.findAt=(state.findAt+(ev.shiftKey?-1:1)+state.findHits.length)%state.findHits.length;focusHit();updateFindCount()}
  if(ev.key==='Escape'){
    if($('mkHover')){hideHover(true);return}
    if(state.layersOpen||state.infoOpen){state.layersOpen=false;state.infoOpen=false;render()}
  }
},true);
/* drag the floating Peek panel by its header */
document.addEventListener('pointerdown',ev=>{
  const h=ev.target.closest&&ev.target.closest('[data-mk-drag]');
  if(!h||ev.target.closest('button')||state.dock!=='float')return;
  const el=$('mkPanel');if(!el)return;
  const r=el.getBoundingClientRect(),dx=ev.clientX-r.left,dy=ev.clientY-r.top;
  const move=e=>{const x=Math.max(0,Math.min(window.innerWidth-120,e.clientX-dx)),y=Math.max(0,Math.min(window.innerHeight-60,e.clientY-dy));state.panelPos={x,y};el.style.left=x+'px';el.style.top=y+'px';el.style.right='auto';el.style.bottom='auto'};
  const up=()=>{document.removeEventListener('pointermove',move);document.removeEventListener('pointerup',up)};
  document.addEventListener('pointermove',move);document.addEventListener('pointerup',up);ev.preventDefault();
});
window.addEventListener('resize',schedule);
window.addEventListener('scroll',()=>{if(state.on)updateMini()},{passive:true});
document.addEventListener('click',ev=>{const mini=ev.target.closest&&ev.target.closest('#markupMini');if(!mini||mini.hidden)return;const body=$('decisionBody'),r=mini.getBoundingClientRect(),f=Math.min(1,Math.max(0,(ev.clientY-r.top)/Math.max(1,r.height))),b=body.getBoundingClientRect();window.scrollTo({top:Math.max(0,scrollY+b.top+f*b.height-window.innerHeight/3),behavior:'smooth'})});
/* Print hides the toolbar and re-flows the page, so lay the notes out again for the print layout and back. */
const setPrinting=v=>{if(!state.on||state.printing===v)return;state.printing=v;render()};
window.addEventListener('beforeprint',()=>setPrinting(true));
window.addEventListener('afterprint',()=>setPrinting(false));
try{const mq=window.matchMedia('print');const onPrint=()=>setPrinting(mq.matches);mq.addEventListener?mq.addEventListener('change',onPrint):mq.addListener(onPrint)}catch(e){}
const prevSet=setReaderMode;
setReaderMode=function(mode){prevSet(mode);if(state.on)afterRender();};
const prevClose=closeDecisionReader;
closeDecisionReader=function(){setOn(false);return prevClose.apply(this,arguments)};
})();
