/* Formatted reader, desktop layout: one left panel (About / Authorities / Intelligence), a title card,
   colour matched hover cards, click cards with a pin, a blue line on paragraphs cited by other cases,
   and "Search this decision". Deterministic only: every figure is stored data read through existing
   endpoints; nothing the user types is sent to a model. */
(function(){
 'use strict';
 const layout=document.querySelector('.reader-layout'),side=document.getElementById('decisionTarget'),body=document.getElementById('decisionBody'),head=document.querySelector('.reader-head');
 if(!layout||!side||!body||!head||typeof sideData!=='function')return;
 const E=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const N=value=>Number(value||0).toLocaleString('en-CA');
 const getJson=async url=>{const response=await fetch(url);if(!response.ok)throw new Error(`Request failed (${response.status})`);return response.json();};
 const v6={caseId:null,tab:'about',isub:'intel',open:null,outline:false,units:false,view:null,stack:[],filter:'',af:'all',cursor:{},cfind:{},intel:new Map(),judges:new Map(),cards:new Map()};
 const fullCaseUrl=id=>`/data-explorer?case_id=${encodeURIComponent(id)}`;
 const openFull=id=>{if(id)window.open(fullCaseUrl(id),'_blank','noopener');};
 const SHOW_COMPARE=false; /* the Compare page is not pitch-ready; set true to bring the button back */
 const cap=value=>{const text=String(value||'').replace(/_/g,' ').trim();return text.charAt(0).toUpperCase()+text.slice(1);};
 const shortCourt=court=>{const text=String(court||'');if(/supreme court of canada/i.test(text))return 'SCC';if(/federal court of appeal/i.test(text))return 'FCA';if(/federal court/i.test(text))return 'FC';if(/refugee protection/i.test(text))return 'RPD';if(/refugee appeal/i.test(text))return 'RAD';return text;};
 const benchNames=name=>String(name||'').split(';').map(x=>x.trim()).filter(Boolean).map(x=>{const m=/^([^,]+),\s*(.+)$/.exec(x);return m?`${m[2].trim()} ${m[1].trim()}`:x;});
 const benchLabel=name=>{const n=String(name||'').split(';').map(x=>x.trim()).filter(Boolean).length;return n>2?`Bench of ${n}`:String(name||'');};
 const longCourt=court=>({SCC:'Supreme Court of Canada',FCA:'Federal Court of Appeal',FC:'Federal Court',RPD:'Refugee Protection Division',RAD:'Refugee Appeal Division'}[String(court||'').trim()]||court||'');
 const isFed=court=>/^(FC|FCA)$/.test(String(court||'').trim())||/federal court/i.test(String(court||''));
 const isScc=court=>/supreme court of canada/i.test(String(court||''));

 /* ---------- cited text, formatted ---------- */
 function citedTextHtml(text,statute){
  const parts=String(text||'').split(/\n\s*\n/).map(part=>part.trim()).filter(Boolean);if(!parts.length)return '';
  return parts.map(part=>{const m=/^\[(\d{1,4})\]\s*/.exec(part),label=m?`Paragraph ${m[1]}`:'',raw=m?part.slice(m[0].length):part,lines=raw.split(/\n+/).map(line=>line.trim()).filter(Boolean);
   return `<div class="v6-cited${statute?' is-statute':''}">${label?`<div class="v6-cited-label">${E(label)}</div>`:''}${lines.map((line,index)=>index?`<blockquote>${E(line)}</blockquote>`:`<p>${E(line)}</p>`).join('')}</div>`;}).join('');
 }

 /* ---------- intelligence (stored citation figures) ---------- */
 function spark(rows,key){if(!rows||!rows.length)return '';const max=Math.max(...rows.map(row=>row[key]),1),w=300,h=52,bw=w/rows.length;return `<svg class="v6-spark" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none">${rows.map((row,index)=>{const bh=Math.max(1,row[key]/max*(h-4));return `<rect x="${index*bw+1}" y="${h-bh}" width="${Math.max(1,bw-2)}" height="${bh}" fill="#176c68" opacity=".78"><title>${E(row.year)}: ${row[key]}</title></rect>`;}).join('')}</svg><div class="v6-years"><span>${E(rows[0].year)}</span><span>${E(rows[rows.length-1].year)}</span></div>`;}
 function outcomeBar(o){const total=o.total_cases||0;if(!total)return '';const segs=[['government_win','#315d8d','Government won'],['government_loss','#2f8a5a','Government lost'],['mixed','#c28e2d','Mixed'],['unknown','#b9b5a6','Unclassified']];return `<div class="v6-bar">${segs.map(([k,c])=>`<i style="width:${(o[k]||0)/total*100}%;background:${c}"></i>`).join('')}</div><div class="v6-legend">${segs.map(([k,c,l])=>`<span><b style="background:${c}"></b>${l} ${N(o[k])}</span>`).join('')}</div>`;}
 function loadIntel(caseId){if(!v6.intel.has(caseId)){const base=`/api/citation-intelligence/${caseId}`;v6.intel.set(caseId,Promise.all(['overview','outcomes','timeline','courts'].map(part=>getJson(`${base}/${part}`).catch(()=>null))).then(([overview,outcomes,timeline,courts])=>({overview,outcomes,timeline,courts})));}return v6.intel.get(caseId);}
 function intelHtml(caseId,d){const o=d.overview;if(!o)return '<div class="v6-note">No citation intelligence is stored for this decision yet.</div>';
  return `<div class="v6-tiles"><div class="v6-tile"><b>${N(o.unique_citing_cases)}</b><span>Citing cases</span></div><div class="v6-tile"><b>${N(o.total_occurrences)}</b><span>Mentions</span></div><div class="v6-tile"><b>${E(o.avg_mentions_per_case)}</b><span>Avg per case</span></div></div>
  ${d.outcomes?`<div class="v6-sec"><h4>Outcome of citing cases</h4>${outcomeBar(d.outcomes)}</div>`:''}
  ${d.timeline&&d.timeline.length?`<div class="v6-sec"><h4>Citing cases per year</h4>${spark(d.timeline,'citing_cases')}</div>`:''}
  ${d.courts&&d.courts.length?`<div class="v6-sec"><h4>By court</h4>${d.courts.map(c=>`<div class="v6-hb"><b>${E(c.court)}</b><span class="t"><i style="width:${c.pct}%"></i></span><span>${N(c.case_count)}</span></div>`).join('')}</div>`:''}
  <a class="v6-link" href="/data-explorer?tab=citation-intelligence&group=research&case_id=${caseId}" target="_blank" rel="noopener">Open full citation intelligence ↗</a>`;}
 function similarRows(rows,why){return rows.map(r=>`<button type="button" class="v6-row" data-v6-newtab="${r.case_id}"><span><strong>${E(r.title)}</strong><small>${E([r.citation,r.court,String(r.date||'').slice(0,4)].filter(Boolean).join(' · '))}${why&&r.shared&&r.shared.length?` · in common: ${E(r.shared.join(', '))}`:''}</small></span></button>`).join('');}
 function similarHtml(d){if(!d||!d.available||(!d.similar.length&&!d.shares_authorities.length))return '';return `${d.similar.length?`<div class="v6-sec"><h4>Similar cases</h4><div class="v6-note-sm">Decisions about the same subject, matched on legal tags and statute provisions.</div>${similarRows(d.similar,true)}</div>`:''}${d.shares_authorities.length?`<div class="v6-sec"><h4>Shares authorities</h4><div class="v6-note-sm">Decisions that cite many of the same cases.</div>${similarRows(d.shares_authorities,false)}</div>`:''}`;}
 async function fillIntel(box,caseId){box.innerHTML='<div class="v6-note">Loading citation intelligence…</div>';const data=await loadIntel(caseId);if(!box.isConnected)return;box.innerHTML=intelHtml(caseId,data);getJson(`/api/cases/${caseId}/similar-cases`).then(similar=>{const html=similarHtml(similar);if(html&&box.isConnected){const link=box.querySelector('.v6-link');if(link)link.insertAdjacentHTML('beforebegin',html);else box.insertAdjacentHTML('beforeend',html);}}).catch(()=>{});}

 /* ---------- judge profiles (stored profiles) ---------- */
 function judgeHtml(profile){const j=profile.profile||{},o=profile.outcomes||{},total=(o.government_wins||0)+(o.individual_wins||0),yearly=(profile.yearly_decisions||profile.yearly||[]).map(y=>({year:y.year,n:y.decisions})),recent=(profile.decisions||profile.recent||[]).slice(0,5);
  return `<div class="v6-tiles"><div class="v6-tile"><b>${N(o.all_linked)}</b><span>Decisions</span></div><div class="v6-tile"><b>${o.government_win_rate!=null?E(o.government_win_rate)+'%':'-'}</b><span>Government won</span></div><div class="v6-tile"><b>${N(o.individual_wins)}</b><span>Individual won</span></div></div>
  ${total?`<div class="v6-sec"><h4>Outcomes</h4><div class="v6-bar"><i style="width:${o.government_wins/total*100}%;background:#315d8d"></i><i style="width:${o.individual_wins/total*100}%;background:#2f8a5a"></i></div><div class="v6-legend"><span><b style="background:#315d8d"></b>Government ${N(o.government_wins)}</span><span><b style="background:#2f8a5a"></b>Individual ${N(o.individual_wins)}</span><span>Unclassified ${N(o.unclassified)}</span></div></div>`:''}
  ${yearly.length?`<div class="v6-sec"><h4>Decisions per year</h4>${spark(yearly,'n')}</div>`:''}
  ${recent.length?`<div class="v6-sec"><h4>Recent decisions</h4>${recent.map(r=>`<div class="v6-line"><strong>${E(r.title)}</strong><small>${E([r.citation,r.date||r.decision_date].filter(Boolean).join(' · '))}</small></div>`).join('')}</div>`:''}
  ${j.slug?`<a class="v6-link" href="/judges/${encodeURIComponent(j.slug)}" target="_blank" rel="noopener">Open full judge profile ↗</a>`:''}`;}
 const plain=text=>String(text||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().replace(/[^a-z\s'-]/g,' ').replace(/\s+/g,' ').trim();
 const TITLE_WORDS=new Set(['the','honourable','hon','justice','mr','mrs','ms','mme','madam','madame','chief','deputy','associate','puisne','j','ja','cj','cjc','jj','jja']);
 /* A decision-maker string as the case stores it ("Justice Gagné", "Grammond, Sébastien", "Mr. Justice Noël J.") to the words that can identify a profile. */
 function judgeTokens(name){const raw=String(name||'').split(';')[0],comma=/^([^,]+),\s*(.+)$/.exec(raw),ordered=comma?`${comma[2]} ${comma[1]}`:raw;return plain(ordered).split(' ').map(t=>t.replace(/^[-']+|[-']+$/g,'')).filter(t=>t.length>1&&!TITLE_WORDS.has(t));}
 async function loadJudge(name,court){const ck=name+'|'+shortCourt(court);if(!v6.judges.has(ck)){
   v6.judges.set(ck,(async()=>{const tokens=judgeTokens(name);if(!tokens.length)return null;const surname=tokens[tokens.length-1];
    const find=async q=>{try{return await getJson(`/api/judge-profiles?q=${encodeURIComponent(q)}&limit=30`);}catch(error){return [];}};
    let list=await find(surname);if(!(list||[]).length&&surname!==String(name).toLowerCase())list=await find(String(name).replace(/^(?:the\s+)?(?:hon\w*\.?\s+)?(?:(?:mr|mme|madam|madame)\.?\s+)?(?:chief\s+)?justice\s+/i,'').replace(/[,.].*$/,'').trim());
    const wantCourt=shortCourt(court);
    const scored=(list||[]).map(p=>{const hay=plain([p.display_name,...(p.aliases||[])].join(' '));const hits=tokens.filter(t=>new RegExp(`(^| )${t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}( |$)`).test(hay)).length;return {p,hits,court:(p.primary_court||'')===wantCourt?1:0,n:p.decision_count||0};}).filter(x=>x.hits>=1&&plain((x.p.display_name+' '+(x.p.aliases||[]).join(' '))).includes(surname)).sort((a,b)=>b.hits-a.hits||b.court-a.court||b.n-a.n);
    const best=scored[0];if(!best)return null;
    try{return await getJson(`/api/judge-profiles/${encodeURIComponent(best.p.slug)}`);}catch(error){return null;}})());}
  return v6.judges.get(ck);}
 async function fillJudge(box,name,court){
  const bench=benchNames(name);
  if(bench.length>1){box.innerHTML=`<div class="v6-who">Bench of ${bench.length}<small>Open a judge to see their profile.</small></div>${bench.map(n=>`<button type="button" class="v6-row" data-v6-judge="${E(n)}"><span><strong>${E(n)}</strong></span><span class="v6-chev">▸</span></button>`).join('')}`;return;}
  if(isScc(court)){box.innerHTML='<div class="v6-note">Judge profiles do not cover the Supreme Court of Canada yet.</div>';return;}
  if(!name){box.innerHTML='<div class="v6-note">The decision maker is not recorded for this case.</div>';return;}
  box.innerHTML='<div class="v6-note">Loading judge profile…</div>';const profile=await loadJudge(name,court);if(!box.isConnected)return;
  box.innerHTML=profile?`<div class="v6-who">${E((profile.profile||{}).display_name||name)}<small>${E((profile.profile||{}).primary_court||'')}</small></div>${judgeHtml(profile)}`:`<div class="v6-note">No judge profile for ${E(name)} yet. Profiles cover Federal Court and Federal Court of Appeal decision-makers.</div>`;}

 /* ---------- left panel ---------- */
 const subTabs=(items,current,attr)=>`<div class="v6-subtabs">${items.map(([key,label])=>`<button type="button" ${attr}="${key}" class="${current===key?'on':''}">${label}</button>`).join('')}</div>`;
 function outlineRows(d){const sec=(d.readerData&&d.readerData.structure_outline)||[],heads=headings(d);if(!sec.length)return heads;const have=new Set(sec.map(r=>r.start)),extra=heads.filter(h=>!have.has(h.start)).map(h=>({title:h.title,start:h.start,para:h.para,level:2}));return sec.concat(extra).sort((a,b)=>a.start-b.start);}
 function headings(d){const blocks=d.readerData.format_blocks||[],text=Array.from(d.item.full_text||''),out=[];blocks.forEach((b,i)=>{if(b.type!=='heading')return;const title=text.slice(b.start,b.end).join('').replace(/\s+/g,' ').trim();if(!title)return;const next=blocks.slice(i+1).find(x=>x.type==='para'&&x.num!=null);out.push({title,start:b.start,para:next?next.num:null,level:b.level||1});});return out;}
 const kv=rows=>{const list=rows.filter(row=>row&&row[1]!==''&&row[1]!=null);return list.length?`<div class="v6-kv">${list.map(([k,v])=>`<div><small>${E(k)}</small><b>${E(v)}</b></div>`).join('')}</div>`:'';};
 const LANG={en:'English',fr:'French',english:'English',french:'French'};
 const TAPE='<span class="v6-tape"><b>COMING SOON</b></span>';
 function aboutHtml(d){
  const cf=sideCaseFacts(d),outcome=sideOutcome(d.item),meta=d.meta,docket=extractDocketFromPayload(d.item)||cf.docket,tags=Array.from(sideTagGroups(d.tags).flatMap(g=>g.values.map(v=>({...v,category:g.category}))).sort((a,b)=>b.count-a.count).reduce((seen,v)=>{const key=String(v.value||v.label||v.name||'').replace(/[_\s]+/g,' ').trim().toLowerCase();if(!seen.has(key))seen.set(key,v);return seen;},new Map()).values()).slice(0,10),heads=headings(d),outl=outlineRows(d);
  const disposition=[...outl].reverse().find(h=>h.role==='disposition')||[...heads].reverse().find(h=>/disposition|conclusion|judgment|order/i.test(h.title));
  /* The title card already shows citation, case type, dates, docket, decision maker and the counts; this panel only adds what it does not. */
  const lang=String(d.item.language||meta.language||'').trim(),status=[d.item.source_name||d.item.source_type?`Text from ${d.item.source_name||d.item.source_type}`:'',d.item.processing_status?`status: ${d.item.processing_status}`:''].filter(Boolean).join(', ');
  const details=kv([['Court',longCourt(cf.court)],['Minister or party',d.item.minister||meta.minister],['Language',LANG[lang.toLowerCase()]||lang],['Jurisdiction',d.item.jurisdiction]]);
  const links=[d.item.source_url?`<a href="${E(d.item.source_url)}" target="_blank" rel="noopener noreferrer">Original decision ↗</a>`:'',docket&&isFed(cf.court)?`<a href="/data-explorer?tab=fc-history&imm=${encodeURIComponent(docket)}" target="_blank" rel="noopener">Full FC activity ↗</a>`:''].filter(Boolean).join('');
  return `<div class="v6-outrow"><span class="v6-ol">Outcome</span>${outcome?`<span class="v6-pill ${outcome.cls}">${E(outcome.text)}</span>`:'<span class="v6-pill none">Not recorded</span>'}${disposition?`<button type="button" class="v6-lk" data-v6-outline="${disposition.start}">Go to ${E(disposition.title)} ↓</button>`:''}</div>${outcome&&outcome.note?`<div class="v6-small v6-outnote">${E(outcome.note)}</div>`:''}
  ${details||links||status?`<div class="v6-sec v6-compact"><h4>Case details</h4>${details}${links?`<div class="v6-links">${links}</div>`:''}${status?`<div class="v6-small">${E(status)}</div>`:''}</div>`:''}
  ${tags.length?`<div class="v6-sec v6-compact"><h4>Topics in the text</h4><div class="v6-chips">${tags.map(t=>`<button type="button" class="v6-chip" data-v6-find="tag" data-v6-needles="${E(String(t.value).toLowerCase())}" data-v6-key="tag:${E(t.value)}">${E(cap(t.value))}<b>${t.count}</b></button>`).join('')}</div></div>`:''}
  ${outl.length?`<div class="v6-sec v6-compact"><button type="button" class="v6-outbtn${v6.outline?' open':''}" data-v6-outl-toggle aria-expanded="${v6.outline}"><span class="v6-ot">Outline<small>${outl.length} section${outl.length===1?'':'s'}</small></span>${TAPE}<span class="v6-chev">${v6.outline?'▾':'▸'}</span></button>${v6.outline?`<div class="v6-outline">${outl.map(h=>`<button type="button" class="v6-orow${h.level>1?' v6-sub':''}" data-v6-outline="${h.start}"><span>${E(h.title)}</span>${h.para?`<span class="v6-ct">${E(h.para)}</span>`:''}</button>`).join('')}</div>`:''}</div>`:''}${unitsSectionHtml(d)}`;}


 /* unit-rows:start */
 /* Discussion units for the left panel: where each unit starts and ends (printed paragraph numbers), the rule-based role
    of the unit, and the paragraphs the position rules read as the applicant's or respondent's argument. Stored data only. */
 const UNIT_ROLE_NAMES={metadata:'Header / footer',overview:'Overview',facts:'Facts',issues:'Issues',analysis:'Analysis',disposition:'Disposition'};
 function unitOutlineRows(rd){
  const es=rd&&rd.evidence_summary,units=(es&&es.units)||[],chunks=(rd&&rd.chunks)||[],blocks=(rd&&rd.format_blocks)||[];
  const numAt=i=>{const c=chunks[i],m=c&&/^\s*\[(\d{1,3})\]/.exec(String(c.text||''));return m?Number(m[1]):null;};
  const startOf=n=>{const b=blocks.find(x=>x.type==='para'&&x.num===n);return b?b.start:null;};
  const rows=[];
  for(const u of units){
   let first=null,last=null;
   if(u.start_number!=null&&u.end_number!=null){first=u.start_number;last=u.end_number;}
   else for(let i=u.start_paragraph;i<=u.end_paragraph;i++){const n=numAt(i);if(n!==null){if(first===null)first=n;last=n;}}
   if(first===null)continue;
   const by={};
   for(const a of u.party_arguments||[]){const n=a.paragraph_number!=null?a.paragraph_number:numAt(a.paragraph_index);if(n!==null)(by[a.party]=by[a.party]||[]).push(n);}
   rows.push({index:u.unit_index,first:first,last:last,start:startOf(first),role:u.role||null,roleName:u.role?(UNIT_ROLE_NAMES[u.role]||u.role):'',
    parties:['applicant','respondent'].filter(k=>by[k]).map(k=>({party:k,label:k==='applicant'?'Applicant':'Respondent',nums:by[k]}))});
  }
  return {rows:rows,roleNote:(es&&es.role_note)||'',partyNote:(es&&es.party_note)||''};
 }
 /* unit-rows:end */
 function unitsSectionHtml(d){
  const info=unitOutlineRows(d.readerData);if(!info.rows.length)return '';
  const range=r=>'¶'+r.first+(r.last!==r.first?'–'+r.last:'');
  const rows=v6.units?`<div class="v6-uwhy">Experimental. Roles and party arguments come from fixed text rules, not a reader.${info.roleNote?' '+E(info.roleNote):''}${info.partyNote?' '+E(info.partyNote):''}</div><div class="v6-outline">${info.rows.map(r=>{
   const label=`<span>${E(range(r))}${r.roleName?' · '+E(r.roleName):''}</span>`,sub=r.parties.length?`<small class="v6-uparty">${r.parties.map(p=>E(p.label)+' '+p.nums.map(n=>'¶'+n).join(', ')).join(' · ')}</small>`:'';
   return r.start!=null?`<button type="button" class="v6-orow v6-urow" data-v6-outline="${r.start}">${label}${sub}</button>`:`<div class="v6-orow v6-urow">${label}${sub}</div>`;}).join('')}</div>`:'';
  return `<div class="v6-sec v6-compact v6-exp"><button type="button" class="v6-outbtn${v6.units?' open':''}" data-v6-units-toggle aria-expanded="${v6.units}"><span class="v6-ot">Discussion units<small>${info.rows.length} unit${info.rows.length===1?'':'s'} · experimental</small></span><span class="v6-chev">${v6.units?'▾':'▸'}</span></button>${rows}</div>`;}

 function authorityRows(d){
  const q=v6.filter.toLowerCase(),cases=v6.af==='stat'?[]:sideAuthorityGroups(d.citations).filter(g=>!q||(g.label+' '+g.citation).toLowerCase().includes(q)).map(g=>({k:'case',key:'c:'+g.key,g})),
   acts=v6.af==='case'?[]:sideActGroups(d.citations).filter(g=>!q||(g.title+' '+g.sections.map(s=>s.number).join(' ')).toLowerCase().includes(q)).map(g=>({k:'stat',key:'s:'+g.title,g}));
  return cases.concat(acts);}
 function caseBody(g,d){
  const rows=g.rows.filter(r=>r.target_case_id&&r.target_paragraph!=null),seen=new Set(),pins=[];rows.forEach(r=>{const k=String(r.target_paragraph);if(!seen.has(k)&&pins.length<3){seen.add(k);pins.push(r);}});
  const texts=pins.map(row=>{const r=hoverRow(row.id)||row,info=hoverCitationInfo(r);if(info.fetch&&!r._hoverFetched)hoverFetchText(r).then(ok=>{if(ok)renderPanel();});return info.text?citedTextHtml(info.text):`<div class="v6-note">${E(info.note||'')}</div>`;}).join('');
  const body=g.caseId?(texts||'<div class="v6-note">Cited without a paragraph number, so there is no pinpoint to show.</div>'):'<div class="v6-note">iLit has not matched this citation to a case in its library, so there is no paragraph to show.</div>';
  return `<div class="v6-abody"><div class="v6-small">Paragraph text from the cited decision</div>${body}</div>`;}
 function actBody(g){return `<div class="v6-abody">${g.sections.map(s=>{const name=s.number?`Section ${s.number}${s.pinpoint&&s.pinpoint!==s.number?` (${s.pinpoint})`:''}`:(s.pinpoint?`Pinpoint ${s.pinpoint}`:'Whole Act or general reference');return `<div class="v6-sect"><div class="v6-sect-h"><strong>${E(name)}</strong><span class="v6-ct">${s.rows.length}</span>${s.url?`<a href="${E(s.url)}" target="_blank" rel="noopener noreferrer">Read ↗</a>`:''}</div>${s.text?citedTextHtml(s.text,true):''}</div>`;}).join('')}</div>`;}
 const findGroup=(kind,needles,key)=>{const at=`data-v6-find="${kind}" data-v6-needles="${E(needles)}" data-v6-key="${E(key)}"`;return `<span class="v6-fg"><button type="button" class="v6-fn" ${at} data-v6-dir="-1" title="Previous place in the text" aria-label="Previous place in the text">↑</button><button type="button" class="v6-find" ${at} title="Next place in the text">${E(v6.cfind&&v6.cfind[key]||'Find')}</button><button type="button" class="v6-fn" ${at} data-v6-dir="1" title="Next place in the text" aria-label="Next place in the text">↓</button></span>`;};
 function authoritiesHtml(d){
  const all=authorityRows(d),nCase=sideAuthorityGroups(d.citations).length,nStat=sideActGroups(d.citations).length;
  const chips=[['all','All',nCase+nStat],['case','Cases',nCase],['stat','Statutes',nStat]].map(([k,l,n])=>`<button type="button" class="v6-fchip${v6.af===k?' on':''}" data-v6-af="${k}">${l}<b>${N(n)}</b></button>`).join('');
  const rows=all.map(r=>{const open=v6.open===r.key,g=r.g,toggle=label=>`<button type="button" class="v6-ab${open?' on':''}" data-v6-row="${E(r.key)}" aria-expanded="${open}" title="${open?'Hide':'Show'} the paragraph text">${label} ${open?'▾':'▸'}</button>`;
   if(r.k==='case'){const n=g.rows.length,paras=[...g.paras].slice(0,4).join(', ');
    return `<div class="v6-arow case${open?' open':''}"><div class="v6-ah"${g.caseId?` data-v6-case="${g.caseId}"`:''}><span class="v6-at"><strong>${E(g.label)}</strong>${g.citation&&g.citation!==g.label?`<small>${E(g.citation)}</small>`:''}</span><span class="v6-cnt" title="Times cited in this decision"><b>${n}</b>${n===1?'citation':'citations'}</span></div>${paras?`<div class="v6-asub">at ${E(paras)}</div>`:''}<div class="v6-aact">${findGroup('cite',[...g.jump].join('|'),r.key)}${g.caseId?`<button type="button" class="v6-ab pri" data-v6-ent="${g.caseId}" data-v6-title="${E(g.label)}" data-v6-cite="${E(g.citation)}">Citation intelligence</button><button type="button" class="v6-ab" data-v6-newtab="${g.caseId}">Full case ↗</button>${toggle('Text')}`:'<span class="v6-small">Not matched to a case in the library</span>'}</div>${open?caseBody(g,d):''}</div>`;}
   const needles=g.sections.flatMap(s=>[...s.jump]).join('|');
   return `<div class="v6-arow stat${open?' open':''}"><div class="v6-ah"><span class="v6-at"><strong>${E(g.title)}</strong><small>${E(g.sections.slice(0,3).map(s=>s.number?`s. ${s.number}`:'general').join(' · '))}</small></span><span class="v6-cnt" title="Times cited in this decision"><b>${g.total}</b>${g.total===1?'citation':'citations'}</span></div><div class="v6-aact">${findGroup('act',needles,r.key)}<button type="button" class="v6-ab pri" data-v6-stat="${E(g.title)}" data-v6-sub="${E(g.sections.slice(0,3).map(s=>s.number?`s. ${s.number}`:'').filter(Boolean).join(' · '))}">Statute intelligence</button>${g.url?`<a class="v6-ab" href="${E(g.url)}" target="_blank" rel="noopener noreferrer">Read the Act ↗</a>`:''}${toggle('Text')}</div>${open?actBody(g):''}</div>`;}).join('');
  return `<div class="v6-legend2"><span><i class="c"></i>Case citations</span><span><i class="s"></i>Statutes and regulations</span></div><input class="v6-filter" type="search" data-v6-filter placeholder="Filter authorities" value="${E(v6.filter)}"><div class="v6-fchips">${chips}</div>${rows||'<div class="v6-note">Nothing matches.</div>'}`;}

 const COLLAPSE='<button type="button" class="v6-collapse" data-v6-collapse title="Hide this panel" aria-label="Hide the case panel"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M10 3L5 8l5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>';
 const ititle=(kind,name,sub,back,extra,tabbed)=>`<div class="v6-ititle">${tabbed?'':COLLAPSE}${back?`<button type="button" class="v6-bk" data-v6-back>← ${E(back)}</button>`:''}<div class="k">${E(kind)}</div><h3>${E(name)}</h3><div class="s">${E(sub)}</div>${extra||''}</div>`;
 function intelligenceHtml(entity,d){
  const isThis=!entity,cf=sideCaseFacts(d),court=isThis?cf.court:entity.court||'',name=isThis?(cf.name||'This case'):entity.title,sub=isThis?[cf.citation,metricsLine(d)].filter(Boolean).join(' · '):[entity.cite].filter(Boolean).join(' · ');
  const back=isThis?'':(v6.stack.length?v6.stack[v6.stack.length-1].label:'Authorities');
  const extra=isThis?'':`<div class="v6-links"><button type="button" data-v6-newtab="${entity.id}">Open full case ↗</button></div>`;
  const pane=v6.isub==='intel'?`<div data-v6-intel="${isThis?readerState.caseId:entity.id}"></div>`:`<div data-v6-judgebox data-v6-judge-name="${E(isThis?cf.judge:entity.judge||'')}" data-v6-court="${E(court)}" ${isThis?'':`data-v6-entity="${entity.id}"`}></div>`;
  return ititle(isThis?'This case':'Cited case',name,sub,back,extra,isThis&&!v6.view)+subTabs([['intel','Citation intelligence'],['judge','Judge profile']],v6.isub,'data-v6-isub')+`<div class="v6-pane">${pane}</div>`;}
 function statuteHtml(view){const back=v6.stack.length?v6.stack[v6.stack.length-1].label:'Authorities';
  return ititle('Statute',view.title,view.sub||'',back)+`<div class="v6-pane"><div class="v6-soon">${TAPE}<h4>Statute intelligence</h4><p>Coming soon.</p></div></div>`;}
 function metricsLine(d){const n=d.metrics&&d.metrics.in_degree;return n!=null?`cited by ${N(n)} cases`:'';}

 const TABS=[['about','About'],['auth','Authorities'],['intel','Intelligence']];
 function panelHtml(d){
  if(v6.view&&v6.view.type==='judge')return `${ititle('Judge profile',v6.view.name,'',v6.stack.length?v6.stack[v6.stack.length-1].label:'Case')}<div class="v6-pane"><div data-v6-judgebox data-v6-judge-name="${E(v6.view.name)}" data-v6-court=""></div></div>`;
  if(v6.view&&v6.view.type==='statute')return statuteHtml(v6.view);
  if(v6.view&&v6.view.type==='case')return intelligenceHtml(v6.view.entity,d);
  const tabs=`<nav class="v6-tabs" role="tablist">${TABS.map(([k,l])=>`<button type="button" role="tab" data-v6-tab="${k}" class="${v6.tab===k?'on':''}" aria-selected="${v6.tab===k}">${l}</button>`).join('')}${COLLAPSE}</nav>`;
  const content=v6.tab==='about'?`<div class="v6-pane">${aboutHtml(d)}</div>`:v6.tab==='auth'?`<div class="v6-pane">${authoritiesHtml(d)}</div>`:intelligenceHtml(null,d);
  return tabs+content;}
 function renderPanel(){
  if(!readerState.payload)return;
  const d=sideData();
  if(v6.caseId!==readerState.caseId){Object.assign(v6,{caseId:readerState.caseId,tab:'about',isub:'intel',open:null,outline:false,view:null,stack:[],filter:'',af:'all',cursor:{},cfind:{}});clearCards();}
  const keep=side.querySelector('[data-v6-filter]'),focused=keep&&document.activeElement===keep,pos=keep?keep.selectionStart:0,scroll=side.querySelector('.v6-pane');const top=scroll?scroll.scrollTop:0;
  side.innerHTML=panelHtml(d);
  const pane=side.querySelector('.v6-pane');if(pane&&top)pane.scrollTop=top;
  if(focused){const f=side.querySelector('[data-v6-filter]');if(f){f.focus();f.setSelectionRange(pos,pos);}}
  const intel=side.querySelector('[data-v6-intel]');if(intel)fillIntel(intel,Number(intel.dataset.v6Intel));
  const jb=side.querySelector('[data-v6-judgebox]');
  if(jb){if(jb.dataset.v6Entity&&!jb.dataset.v6JudgeName){const id=Number(jb.dataset.v6Entity);jb.innerHTML='<div class="v6-note">Loading judge profile…</div>';getJson(`/analytics/search/cases/${id}`).then(data=>{const item=data.case||{};if(v6.view&&v6.view.entity){v6.view.entity.judge=sideJudge(item.judge);v6.view.entity.court=item.court||v6.view.entity.court;}if(jb.isConnected)fillJudge(jb,sideJudge(item.judge),item.court||'');}).catch(()=>{jb.innerHTML='<div class="v6-note">The decision maker could not be loaded.</div>';});}
   else fillJudge(jb,jb.dataset.v6JudgeName,jb.dataset.v6Court);}
  renderCard(d);
 }
 renderReaderSidebar=function(){try{renderPanel();}catch(error){console.warn('Reader panel failed',error);}};

 /* ---------- Save to Workbench (demo sign-in; stored server side per demo user) ---------- */
 const wb={signedIn:false,pinned:false};
 function paintSave(label){const b=document.getElementById('v6SaveWb');if(b){b.textContent=label;b.classList.toggle('is-saved',wb.pinned);}}
 async function syncSave(id){
  if(!id)return;
  try{const r=await getJson('/workbench/api/pins/state?case_id='+encodeURIComponent(id));wb.signedIn=r.signed_in;wb.pinned=r.pinned;}catch(error){wb.signedIn=false;wb.pinned=false;}
  paintSave(wb.pinned?'Saved to Workbench ✓':'Save to Workbench');
 }
 async function saveToWorkbench(id){
  if(wb.pinned){window.open('/workbench#home','_blank','noopener');return;}
  if(!wb.signedIn){window.open('/workbench','_blank','noopener');paintSave('Sign in on the Workbench, then save');return;}
  try{
   const response=await fetch('/workbench/api/pins',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({case_id:Number(id)})});
   if(response.status===401){wb.signedIn=false;window.open('/workbench','_blank','noopener');return;}
   if(!response.ok)throw new Error('failed');
   wb.pinned=true;paintSave('Saved to Workbench ✓');
  }catch(error){paintSave('Could not save, try again');}
 }

 /* ---------- title card ---------- */
 /* stored case type (primary only, no AI); empty for decisions without a label so nothing is drawn */
 function caseTypeText(d){const t=d&&d.readerData&&d.readerData.case_type,p=t&&t.primary;return p&&p.label?p.label+(p.provision?' ('+p.provision+')':''):'';}
 function renderCard(d){
  const title=document.getElementById('decisionTitle');let kick=document.getElementById('v6Kicker'),card=document.getElementById('v6Card');
  if(!kick){kick=document.createElement('div');kick.id='v6Kicker';title.before(kick);}
  if(!card){card=document.createElement('div');card.id='v6Card';title.after(card);}
  const cf=sideCaseFacts(d),item=d.item,outcome=sideOutcome(item),docket=extractDocketFromPayload(item)||cf.docket,compare=document.getElementById('readerCompareLink'),authorities=sideAuthorityGroups(d.citations).length,acts=sideActGroups(d.citations).length,citedBy=d.metrics&&d.metrics.in_degree;
  const cell=(label,value,raw)=>value?`<div class="v6-fs"><small>${E(label)}</small><b>${raw?value:E(value)}</b></div>`:'';
  kick.innerHTML=`<span class="v6-court">${E(shortCourt(cf.court)||'Court')}</span>${outcome?`<span class="v6-pill ${outcome.cls}">${E(outcome.text)}</span>`:''}<span class="v6-actions"><button type="button" data-v6-copy>Copy citation</button>${item.source_url?`<a href="${E(item.source_url)}" target="_blank" rel="noopener noreferrer">Case source ↗</a>`:''}${compare&&SHOW_COMPARE?`<a href="${E(compare.getAttribute('href')||'/compare')}">Compare with…</a>`:''}${docket&&isFed(cf.court)?`<a href="/data-explorer?tab=fc-history&imm=${encodeURIComponent(docket)}" target="_blank" rel="noopener">FC activity ↗</a>`:''}${item.id?`<button type="button" data-v6-save="${E(item.id)}" id="v6SaveWb">Save to Workbench</button>`:''}</span>`;
  card.innerHTML=`<div class="v6-facts-strip">${cell('Citation',cf.citation)}${cell('Case type',caseTypeText(d))}${cell('Decided',cf.decided)}${cell(/^IMM/i.test(docket)?'Docket (IMM no.)':'File no.',docket)}${cell('Decision maker',cf.judge?(cf.court==='RPD'?E(cf.judge):`<button type="button" class="v6-lk" data-v6-go="judge">${E(benchLabel(cf.judge))}</button>`):'',true)}${cell('Heard',cf.hearing)}<span class="v6-stats"><button type="button" class="v6-stat" data-v6-go="intel"><b>${citedBy==null?'-':N(citedBy)}</b><span>Cited by</span></button><button type="button" class="v6-stat" data-v6-go="auth-case"><b>${N(authorities)}</b><span>Cites</span></button><button type="button" class="v6-stat" data-v6-go="auth-stat"><b>${N(acts)}</b><span>Statutes</span></button></span></div>`;
   syncSave(item&&item.id);
 }

 /* ---------- find in the text, jump to outline ---------- */
 function flash(el){document.querySelectorAll('.v6-flash').forEach(x=>x.classList.remove('v6-flash'));el.classList.add('v6-flash');setTimeout(()=>el.classList.remove('v6-flash'),1800);}
 function findMarks(button){return sideFindMarks(button.dataset.v6Find==='cite'?'cite':button.dataset.v6Find,button.dataset.v6Needles||'');}
 function runFind(button,dir){const marks=findMarks(button),key=button.dataset.v6Key,group=button.closest('.v6-fg'),label=group?group.querySelector('.v6-find'):button;if(!marks.length){const old=label.textContent;label.textContent='Not in text';setTimeout(()=>{label.textContent=old;},1500);return;}
  const index=((v6.cursor[key]??(dir<0?0:-1))+(dir<0?-1:1)+marks.length)%marks.length;v6.cursor[key]=index;const target=marks[index];target.scrollIntoView({behavior:'smooth',block:'center'});flash(target);
  if(label.classList.contains('v6-find')){label.textContent=`${index+1} of ${marks.length}`;(v6.cfind=v6.cfind||{})[key]=label.textContent;}}
 function jumpOutline(start){const el=document.getElementById('decision-source-'+start);if(el){el.scrollIntoView({behavior:'smooth',block:'start'});flash(el);}}

 /* ---------- left panel clicks ---------- */
 function go(view){if(v6.view)v6.stack.push({view:v6.view,isub:v6.isub,label:v6.view.type==='judge'?'Judge':v6.view.type==='statute'?'Statute':(v6.view.entity.title||'Case').slice(0,28)});else v6.stack.push({view:null,isub:v6.isub,label:v6.tab==='auth'?'Authorities':'Case'});v6.view=view;v6.isub='intel';renderPanel();}
 function back(){const prev=v6.stack.pop();if(prev){v6.view=prev.view;v6.isub=prev.isub;}else v6.view=null;renderPanel();}
 function goTab(tab,af){if(layout.classList.contains('is-target-collapsed'))document.getElementById('toggleCaseInformation')?.click();v6.view=null;v6.stack=[];v6.tab=tab;v6.isub='intel';if(af)v6.af=af;v6.open=null;v6.filter='';renderPanel();}
 side.addEventListener('click',event=>{const t=event.target;let m;
  if(t.closest('[data-v6-back]'))return back();
  if(m=t.closest('[data-v6-tab]')){v6.tab=m.dataset.v6Tab;v6.isub='intel';v6.filter='';return renderPanel();}
  if(m=t.closest('[data-v6-isub]')){v6.isub=m.dataset.v6Isub;return renderPanel();}
  if(m=t.closest('[data-v6-af]')){v6.af=m.dataset.v6Af;return renderPanel();}
  if(t.closest('[data-v6-collapse]')){document.getElementById('toggleCaseInformation')?.click();return;}
  if(m=t.closest('[data-v6-outl-toggle]')){v6.outline=!v6.outline;return renderPanel();}
  if(m=t.closest('[data-v6-units-toggle]')){v6.units=!v6.units;return renderPanel();}
  if(m=t.closest('[data-v6-find]'))return runFind(m,Number(m.dataset.v6Dir||1));
  if(m=t.closest('[data-v6-stat]'))return go({type:'statute',title:m.dataset.v6Stat,sub:m.dataset.v6Sub||''});
  if(m=t.closest('[data-v6-outline]'))return jumpOutline(m.dataset.v6Outline);
  if(m=t.closest('[data-v6-go]')){const g=m.dataset.v6Go;if(g==='judge'){v6.tab='intel';v6.isub='judge';v6.view=null;v6.stack=[];return renderPanel();}return goTab(g);}
  if(m=t.closest('[data-v6-judge]'))return go({type:'judge',name:m.dataset.v6Judge});
  if(m=t.closest('[data-v6-ent]')){const id=Number(m.dataset.v6Ent);return go({type:'case',entity:{id,title:m.dataset.v6Title||'Cited case',cite:m.dataset.v6Cite||'',judge:'',court:''}});}
  if(m=t.closest('[data-v6-newtab]'))return openFull(m.dataset.v6Newtab);
  if(m=t.closest('[data-v6-row]')){const key=m.dataset.v6Row;v6.open=v6.open===key?null:key;renderPanel();const row=side.querySelector('.v6-arow.open');if(row)row.scrollIntoView({block:'nearest',behavior:'smooth'});}
 });
 side.addEventListener('dblclick',event=>{const m=event.target.closest('[data-v6-case]');if(m){window.getSelection().removeAllRanges();openFull(m.dataset.v6Case);}});
 side.addEventListener('input',event=>{if(event.target.matches('[data-v6-filter]')){v6.filter=event.target.value;renderPanel();}});
 head.addEventListener('click',event=>{const t=event.target;let m;
  if(t.closest('[data-v6-save]')){saveToWorkbench(t.closest('[data-v6-save]').dataset.v6Save);return;}
  if(t.closest('[data-v6-copy]')){document.getElementById('readerCopyCite')?.click();const b=t.closest('[data-v6-copy]'),old=b.textContent;b.textContent='Copied';setTimeout(()=>{b.textContent=old;},1400);return;}
  if(m=t.closest('[data-v6-go]')){const g=m.dataset.v6Go;if(g==='judge'){v6.tab='intel';v6.isub='judge';v6.view=null;v6.stack=[];if(layout.classList.contains('is-target-collapsed'))document.getElementById('toggleCaseInformation')?.click();return renderPanel();}
   if(g==='intel')return goTab('intel');if(g==='auth-case')return goTab('auth','case');if(g==='auth-stat')return goTab('auth','stat');}});

 /* ---------- hover cards: colour matched ---------- */
 const SEL='#decisionBody [data-authority]';
 const kindOf=el=>el.classList.contains('tag-highlight')?'tag':el.classList.contains('chunk-statute')?'stat':'case';
 document.addEventListener('mouseover',event=>{const el=event.target.closest?.(SEL);if(!el)return;const tip=document.querySelector('.reader-hover-tooltip');if(tip){tip.classList.remove('v6-case','v6-stat','v6-tag');tip.classList.add('v6-'+kindOf(el));}});

 /* ---------- click card with a pin ---------- */
 const PIN='<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M9.5 1.5l5 5-1.6.9-2.2 2.2.4 3-1.2 1.2-2.9-2.9-4 4-.8-.8 4-4-2.9-2.9 1.2-1.2 3 .4 2.2-2.2z" fill="currentColor"/></svg>';
 const io=new IntersectionObserver(entries=>entries.forEach(entry=>{const card=entry.target;if(!entry.isIntersecting&&!card.classList.contains('is-pinned'))dropCard(card.dataset.v6Key);}),{threshold:0});
 function dropCard(key){const card=v6.cards.get(key);if(!card)return;io.unobserve(card);card.remove();v6.cards.delete(key);document.querySelectorAll('.v6-sel').forEach(x=>{if(x.dataset.v6CardKey===key)x.classList.remove('v6-sel');});updateClear();}
 function dropUnpinned(){[...v6.cards.entries()].forEach(([key,card])=>{if(!card.classList.contains('is-pinned'))dropCard(key);});}
 function clearCards(){[...v6.cards.keys()].forEach(dropCard);}
 function updateClear(){const n=[...v6.cards.values()].filter(card=>card.classList.contains('is-pinned')).length,b=document.getElementById('v6Clear');if(b){b.hidden=!n;b.textContent=`Clear pinned cards (${n})`;}}
 function blockOf(el){return el.closest('.fmt-para, .fmt-quote, .fmt-heading, .fmt-meta, .fmt-footer-line, .chunk-body, .fmt-decision > *');}
 function citationCardHtml(el){
  const kind=kindOf(el);
  if(kind==='tag'){const title=String(el.getAttribute('title')||''),parts=title.split(': ');return `<div class="v6-ck">Tag</div><div class="v6-ct2">${E(cap(el.dataset.authority||el.textContent))}</div>${parts.length>1?`<div class="v6-cl">${E(cap(parts[0]))}</div>`:''}`;}
  const row=el.dataset.citeId?hoverRow(el.dataset.citeId):null;
  if(!row)return `<div class="v6-ck">${kind==='stat'?'Statute or regulation':'Cited case'}</div><div class="v6-ct2">${E(el.textContent)}</div>`;
  const info=hoverCitationInfo(row);if(info.fetch&&!row._hoverFetched)hoverFetchText(row).then(ok=>{if(!ok)return;const card=v6.cards.get(cardKey(el));if(card&&card.isConnected){const btns=card.querySelector('.v6-cbtns');card.innerHTML=citationCardHtml(el);card.appendChild(btns);}});
  return `<div class="v6-ck">${E(info.kind)}</div><div class="v6-ct2">${E(info.title)}</div>${info.label?`<div class="v6-cl">${E(info.label)}</div>`:''}${info.text?citedTextHtml(info.text,kind==='stat'):`<div class="v6-cn">${E(info.note||'')}</div>`}${row.target_case_id?'<div class="v6-dh">Double-click the citation to open this case in a new tab</div>':''}`;}
 /* Card buttons: an "i" that opens the citation in the left panel's Intelligence view (a statute goes to its Coming soon page) and a pin. */
 const INFO_I='<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><circle cx="8" cy="8" r="6.4" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="8" cy="4.9" r="1" fill="currentColor"/><path d="M8 7.3v4.2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>';
 function cardButtons(el){const kind=el?kindOf(el):'para',row=el&&el.dataset.citeId?hoverRow(el.dataset.citeId):null;
  const info=kind==='case'?(row&&row.target_case_id?`<button type="button" class="v6-ibtn" data-v6-i="case" title="Open this citation in Intelligence" aria-label="Open this citation in Intelligence">${INFO_I}</button>`:`<button type="button" class="v6-ibtn" disabled title="iLit has not matched this citation to a case, so there is no intelligence to show" aria-label="No intelligence for this citation">${INFO_I}</button>`):kind==='stat'?`<button type="button" class="v6-ibtn" data-v6-i="stat" title="Statute intelligence" aria-label="Statute intelligence">${INFO_I}</button>`:'';
  return `<span class="v6-cbtns">${info}<button type="button" class="v6-pinbtn" title="Pin this card so it stays" aria-label="Pin card">${PIN}</button></span>`;}
 function openIntel(card){const key=card.dataset.v6Key,el=[...document.querySelectorAll('#decisionBody [data-v6-card-key]')].find(x=>x.dataset.v6CardKey===key);if(!el)return;
  if(layout.classList.contains('is-target-collapsed'))document.getElementById('toggleCaseInformation')?.click();
  if(kindOf(el)==='stat'){const row=el.dataset.citeId?hoverRow(el.dataset.citeId):null,info=row?hoverCitationInfo(row):null;go({type:'statute',title:(info&&info.title)||el.textContent,sub:(info&&info.label)||''});}
  else{const row=el.dataset.citeId?hoverRow(el.dataset.citeId):null;if(!row||!row.target_case_id)return;go({type:'case',entity:{id:row.target_case_id,title:row.target_title||row.target_citation||el.textContent,cite:row.target_citation||'',judge:'',court:''}});}
  side.scrollTop=0;}
 const cardKey=el=>'c:'+(el.dataset.citeId||el.textContent);
 function showCard(el){
  const key=cardKey(el),old=v6.cards.get(key);
  if(old){if(!old.classList.contains('is-pinned'))dropCard(key);return;}
  dropUnpinned();const block=blockOf(el);if(!block)return;
  const card=document.createElement('div');card.className='v6-card2 v6-'+kindOf(el);card.dataset.v6Key=key;card.innerHTML=citationCardHtml(el)+cardButtons(el);
  block.after(card);v6.cards.set(key,card);el.classList.add('v6-sel');el.dataset.v6CardKey=key;requestAnimationFrame(()=>io.observe(card));}
 function showParaCard(para){
  const key='p:'+para.dataset.para,old=v6.cards.get(key);if(old){if(!old.classList.contains('is-pinned'))dropCard(key);return;}
  dropUnpinned();const title=String(para.getAttribute('title')||''),count=(/(\d[\d,]*)/.exec(title)||[])[1]||'';
  const card=document.createElement('div');card.className='v6-card2 v6-para';card.dataset.v6Key=key;
  card.innerHTML=`<div class="v6-ck">Paragraph ${E(para.dataset.para)}</div><div class="v6-ct2">${count?`Cited by ${E(count)} case${Number(count.replace(/,/g,''))===1?'':'s'}`:'Cited by other cases'}</div><div class="v6-cl">${E(title.replace(/^Cited by [\d,]+ cases?[.:]?\s*/i,'')||'Other decisions in the iLit library cite this paragraph by number.')}</div>${cardButtons(null)}`;
  para.after(card);v6.cards.set(key,card);requestAnimationFrame(()=>io.observe(card));}
 let clickTimer=null;
 body.addEventListener('click',event=>{
  const ib=event.target.closest('.v6-ibtn');if(ib){if(!ib.disabled)openIntel(ib.closest('.v6-card2'));return;}
  const pin=event.target.closest('.v6-pinbtn');if(pin){const card=pin.closest('.v6-card2');card.classList.toggle('is-pinned');pin.title=card.classList.contains('is-pinned')?'Unpin':'Pin this card so it stays';updateClear();return;}
  const num=event.target.closest('.fmt-para.is-cited-by .fmt-para-num');if(num){showParaCard(num.closest('.fmt-para'));return;}
  const el=event.target.closest(SEL);if(!el||event.target.closest('.v6-card2'))return;if(body.classList.contains('hide-'+{case:'cites',stat:'laws',tag:'tags'}[kindOf(el)]))return;event.stopImmediatePropagation();clearTimeout(clickTimer);clickTimer=setTimeout(()=>showCard(el),230);},true);
 body.addEventListener('dblclick',event=>{const el=event.target.closest(SEL);if(!el)return;clearTimeout(clickTimer);window.getSelection().removeAllRanges();
  const row=el.dataset.citeId?hoverRow(el.dataset.citeId):null;if(!row)return;
  if(row.target_case_id)return openFull(row.target_case_id);
  const sec=/^\d{1,3}(?:\.\d+)?[A-Za-z]?/.exec(String(row.section_number||row.pinpoint||''));
  if(row.instrument_key&&sec)return void window.open(`/statute-library?act=${encodeURIComponent(row.instrument_key)}&section=${encodeURIComponent(sec[0])}`,'_blank','noopener');
  const url=row.legislation_url||row.authority_document_url;if(url)window.open(url,'_blank','noopener');});
 openLinkedCase=function(){};
 document.addEventListener('keydown',event=>{if(event.key==='Escape'&&[...v6.cards.values()].some(c=>c.classList.contains('is-pinned')))clearCards();});

 /* ---------- Search this decision ---------- */
 const bar=document.querySelector('.reader-evidence-bar');let hits=[],cursor=-1,input,counter,prev,next;
 if(bar){const wrap=document.createElement('div');wrap.className='v6-ft';wrap.innerHTML='<input id="v6Search" type="search" placeholder="Search this decision" autocomplete="off" aria-label="Search this decision"><span class="v6-ftc" id="v6SearchCount" aria-live="polite"></span><button type="button" id="v6SearchPrev" title="Previous hit (Shift+Enter)" aria-label="Previous hit" disabled>↑</button><button type="button" id="v6SearchNext" title="Next hit (Enter)" aria-label="Next hit" disabled>↓</button>';
  const clear=document.createElement('button');clear.type='button';clear.id='v6Clear';clear.className='v6-clear';clear.hidden=true;clear.addEventListener('click',clearCards);
  bar.append(clear,wrap);input=wrap.querySelector('#v6Search');counter=wrap.querySelector('#v6SearchCount');prev=wrap.querySelector('#v6SearchPrev');next=wrap.querySelector('#v6SearchNext');}
 function clearHits(){document.querySelectorAll('#decisionBody .v6-hit').forEach(span=>{const parent=span.parentNode;span.replaceWith(document.createTextNode(span.textContent));parent.normalize();});hits=[];cursor=-1;}
 function showHit(){hits.forEach((h,i)=>h.classList.toggle('cur',i===cursor));if(hits[cursor])hits[cursor].scrollIntoView({behavior:'smooth',block:'center'});counter.textContent=hits.length?`${cursor+1} of ${N(hits.length)}`:(input.value.trim().length>1?'No hits':'');prev.disabled=next.disabled=!hits.length;}
 function runSearch(){clearHits();const value=input.value.trim();if(value.length<2){showHit();return;}
  const re=new RegExp(value.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'),'gi'),root=body.querySelector('.fmt-decision')||body,walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:n=>n.parentElement&&n.parentElement.closest('.v6-card2, script, style')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT}),nodes=[];
  while(walker.nextNode())nodes.push(walker.currentNode);
  nodes.forEach(node=>{const text=node.nodeValue;re.lastIndex=0;let m,last=0,frag=null;while((m=re.exec(text))){if(!m[0].length){re.lastIndex++;continue;}frag=frag||document.createDocumentFragment();frag.append(text.slice(last,m.index));const span=document.createElement('span');span.className='v6-hit';span.textContent=m[0];frag.append(span);hits.push(span);last=m.index+m[0].length;}if(frag){frag.append(text.slice(last));node.replaceWith(frag);}});
  cursor=hits.length?0:-1;showHit();}
 const step=delta=>{if(!hits.length)return;cursor=(cursor+delta+hits.length)%hits.length;showHit();};
 if(input){input.addEventListener('input',runSearch);input.addEventListener('keydown',event=>{if(event.key==='Enter'){event.preventDefault();step(event.shiftKey?-1:1);}if(event.key==='Escape'){input.value='';runSearch();input.blur();event.stopPropagation();}});prev.addEventListener('click',()=>step(-1));next.addEventListener('click',()=>step(1));
  document.addEventListener('keydown',event=>{if((event.ctrlKey||event.metaKey)&&event.key==='f'&&!document.getElementById('caseReaderPanel').hidden){event.preventDefault();input.focus();input.select();}});}

 /* A fresh render of the text drops the cards and the hits. */
 const previousSetReaderMode=setReaderMode;
 setReaderMode=function(mode){clearCards();if(input){hits=[];cursor=-1;if(counter){counter.textContent='';prev.disabled=next.disabled=true;}input.value='';}previousSetReaderMode(mode);};
 /* Layer toggles in the order Citations, Statutes, Tags (the old bar says Acts). */
 (function(){const legend=document.querySelector('.reader-layer-legend');if(!legend)return;const by=k=>legend.querySelector(`[data-layer="${k}"]`);
  const names={cites:'Citations',laws:'Statutes',tags:'Tags'};
  ['cites','laws','tags'].forEach(k=>{const b=by(k);if(!b)return;legend.append(b);const dot=b.querySelector('i,.dot,span');const label=[...b.childNodes].reverse().find(n=>n.nodeType===3&&n.nodeValue.trim());if(label)label.nodeValue=' '+names[k];else if(!dot)b.textContent=names[k];});})();

 /* The collapsed Counsel, appearances and record block also sits at the start of the decision. */
 (function(){let busy=false;const addTop=()=>{if(busy)return;const root=body.querySelector('.fmt-decision'),foot=body.querySelector('.fmt-footer:not(.fmt-footer-top):not(.fmt-source)');if(!root||!foot||root.querySelector('.fmt-footer-top'))return;busy=true;
  const clone=foot.cloneNode(true);clone.classList.add('fmt-footer-top');clone.removeAttribute('open');clone.querySelectorAll('[id]').forEach(n=>n.removeAttribute('id'));
  const kids=[...root.children],anchor=kids.find(c=>c.classList.contains('fmt-caption'))||kids.find(c=>!c.classList.contains('fmt-meta'));
  if(anchor)root.insertBefore(clone,anchor);else root.append(clone);busy=false;};
  new MutationObserver(addTop).observe(body,{childList:true});addTop();})();

 if(readerState.payload)renderPanel();
})();
