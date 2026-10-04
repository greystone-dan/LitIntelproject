"""FC Analytics tab: an interactive dashboard over the classified Federal Court activity data.

Everything is drawn client-side from /api/fc-activity/dashboard (plus the judges and counsel
endpoints). One filter row scopes every chart; clicking a bar, year, judge or counsel adds a
cross-filter chip. Each chart can switch to a table view, and every value is reachable without
hovering. Colours follow the validated categorical order (blue, orange, aqua, yellow, magenta,
green), checked against this page's #fffef9 surface; three slots sit under 3:1 contrast, so every
chart carries a legend or direct labels and a table view.
"""

FC_ANALYTICS_TAB = (
    '<button class="tab" type="button" data-nav-group="research" data-tab="fc-analytics" aria-pressed="false" '
    'aria-controls="fcAnalyticsPanel">FC Analytics</button>'
)

FC_ANALYTICS_CSS = r"""
.fcx{--fcx-surface:#fffef9;--fcx-ink:#0b0b0b;--fcx-ink-2:#52514e;--fcx-muted:#7a7972;--fcx-grid:#e7e4da;--fcx-line:#d8d5ca;
--fcx-s1:#2a78d6;--fcx-s2:#eb6834;--fcx-s3:#1baf7a;--fcx-s4:#eda100;--fcx-s5:#e87ba4;--fcx-s6:#008300;--fcx-neutral:#c9c6bb;
--fcx-q1:#86b6ef;--fcx-q2:#6da7ec;--fcx-q3:#5598e7;--fcx-q4:#3987e5;--fcx-q5:#2a78d6;--fcx-q6:#256abf;color:var(--fcx-ink)}
.fcx .fcx-filters{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;gap:8px 10px;align-items:flex-end;padding:12px 16px;background:var(--fcx-surface);border-bottom:1px solid var(--fcx-line)}
.fcx .fcx-filters label{display:block;font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--fcx-ink-2);margin-bottom:3px}
.fcx .fcx-filters select{min-width:120px;max-width:220px;height:32px;border:1px solid var(--fcx-line);background:#fff;padding:0 8px;font:inherit;font-size:12px}
.fcx .fcx-presets{display:flex;gap:4px}.fcx .fcx-presets button,.fcx .fcx-clear,.fcx .fcx-toggle{height:32px;border:1px solid var(--fcx-line);background:#fff;padding:0 10px;font:inherit;font-size:12px;cursor:pointer;color:var(--fcx-ink)}
.fcx .fcx-presets button[aria-pressed=true]{border-color:var(--fcx-ink);font-weight:600}
.fcx .fcx-chips{display:flex;flex-wrap:wrap;gap:6px;padding:8px 16px 0;min-height:8px}
.fcx .fcx-chip{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--fcx-line);background:#fff;padding:3px 8px;font-size:12px}
.fcx .fcx-chip button{border:0;background:none;cursor:pointer;font-size:14px;line-height:1;color:var(--fcx-ink-2)}
.fcx .fcx-status{padding:6px 16px;font-size:12px;color:var(--fcx-ink-2)}
.fcx .fcx-body{transition:opacity .15s}.fcx .fcx-body.is-loading{opacity:.45}
.fcx .fcx-kpis{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;padding:12px 16px}
.fcx .fcx-kpi{border:1px solid var(--fcx-line);background:#fff;padding:12px 12px 10px}
.fcx .fcx-kpi span{display:block;font-size:11px;color:var(--fcx-ink-2)}.fcx .fcx-kpi b{display:block;margin-top:4px;font-size:26px;font-weight:600;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.fcx .fcx-kpi small{display:block;margin-top:2px;font-size:11px;color:var(--fcx-muted)}
.fcx .fcx-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;padding:0 16px 16px}
.fcx .fcx-card{border:1px solid var(--fcx-line);background:#fff;padding:12px 14px 14px;min-width:0}
.fcx .fcx-card.wide{grid-column:1 / -1}
.fcx .fcx-card header{display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-bottom:6px}
.fcx .fcx-card h3{margin:0;font-size:14px;font-weight:600}.fcx .fcx-card header p{margin:2px 0 0;font-size:11px;color:var(--fcx-ink-2);line-height:1.4}
.fcx .fcx-toggle{height:26px;font-size:11px;padding:0 8px;flex:none}
.fcx svg{display:block;width:100%;height:auto;overflow:visible}
.fcx .fcx-axis{font-size:11px;fill:var(--fcx-ink-2);font-variant-numeric:tabular-nums}.fcx .fcx-gridline{stroke:var(--fcx-grid);stroke-width:1}
.fcx .fcx-label{font-size:11px;fill:var(--fcx-ink)}.fcx .fcx-value{font-size:11px;fill:var(--fcx-ink-2);font-variant-numeric:tabular-nums}
.fcx .fcx-hit{cursor:pointer}.fcx .fcx-hit:hover .fcx-mark,.fcx .fcx-hit:focus .fcx-mark{filter:brightness(1.12)}.fcx .fcx-hit:focus{outline:none}.fcx .fcx-hit:focus .fcx-mark{stroke:var(--fcx-ink);stroke-width:1.5}
.fcx .fcx-legend{display:flex;flex-wrap:wrap;gap:4px 14px;margin:6px 0 2px;font-size:11px;color:var(--fcx-ink-2)}
.fcx .fcx-legend i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px;vertical-align:-1px}.fcx .fcx-legend i.line{height:2px;width:14px;border-radius:1px;vertical-align:3px}
.fcx table{width:100%;border-collapse:collapse;font-size:12px}.fcx th,.fcx td{padding:6px 8px;border-bottom:1px solid var(--fcx-grid);text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
.fcx th:first-child,.fcx td:first-child{text-align:left;white-space:normal}.fcx th{color:var(--fcx-ink-2);font-weight:600;cursor:pointer;position:sticky;top:0;background:#fff}
.fcx .fcx-scroll{max-height:440px;overflow-x:auto;overflow-y:auto}.fcx tr.fcx-row{cursor:pointer}.fcx tr.fcx-row:hover td{background:#f6f4ee}
.fcx .fcx-note{font-size:11px;color:var(--fcx-muted);margin-top:6px;line-height:1.45}
.fcx .fcx-empty{padding:28px 0;text-align:center;font-size:12px;color:var(--fcx-ink-2)}
#fcxTooltip{position:fixed;z-index:50;pointer-events:none;background:#fff;border:1px solid var(--border,#d8d5ca);box-shadow:0 4px 14px rgba(0,0,0,.12);padding:8px 10px;font-size:12px;max-width:280px;display:none}
#fcxTooltip .t{font-weight:600;margin-bottom:4px;color:#0b0b0b}#fcxTooltip .r{display:flex;align-items:center;gap:6px;color:#52514e}#fcxTooltip .r b{color:#0b0b0b;font-variant-numeric:tabular-nums}
#fcxTooltip .k{display:inline-block;width:12px;height:2px}
@media(max-width:1100px){.fcx .fcx-kpis{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media(max-width:820px){.fcx .fcx-grid{grid-template-columns:1fr}.fcx .fcx-card.wide{grid-column:auto}.fcx .fcx-kpis{grid-template-columns:repeat(2,minmax(0,1fr))}.fcx .fcx-filters{position:static}.fcx .fcx-filters select{min-width:0;width:100%}.fcx .fcx-filters>div{flex:1 1 140px}}
"""

FC_ANALYTICS_PANEL = r"""
<section id="fcAnalyticsPanel" class="panel-card search-layout fcx" hidden>
<div class="page-header"><div class="eyebrow">Federal Court immigration files</div><h2>FC Analytics</h2><p>Outcomes, timing, motions, judges and counsel across the classified Federal Court docket. Every chart follows the filters; click a bar, year, judge or counsel to drill in.</p></div>
<div class="fcx-filters" role="group" aria-label="Dashboard filters">
<div><label>Years filed</label><div class="fcx-presets" id="fcxPresets"><button type="button" data-preset="all" aria-pressed="true">All</button><button type="button" data-preset="10" aria-pressed="false">Last 10</button><button type="button" data-preset="5" aria-pressed="false">Last 5</button></div></div>
<div><label for="fcxYearFrom">From</label><select id="fcxYearFrom" data-filter="year_from"><option value="">Any</option></select></div>
<div><label for="fcxYearTo">To</label><select id="fcxYearTo" data-filter="year_to"><option value="">Any</option></select></div>
<div><label for="fcxCity">Registry</label><select id="fcxCity" data-filter="city"><option value="">All registries</option></select></div>
<div><label for="fcxBody">Decision under review</label><select id="fcxBody" data-filter="decision_body"><option value="">All decision makers</option></select></div>
<div><label for="fcxType">Application type</label><select id="fcxType" data-filter="application_type"><option value="">All types</option></select></div>
<div><label for="fcxRep">Representation</label><select id="fcxRep" data-filter="representation"><option value="">Any</option><option value="represented">Counsel named</option><option value="self_represented">Self-represented</option><option value="unknown">Not recorded</option></select></div>
<div><label for="fcxLang">Language</label><select id="fcxLang" data-filter="language"><option value="">Any</option><option value="english">English</option><option value="french">French</option><option value="mixed">Mixed</option></select></div>
<div><label>&nbsp;</label><button type="button" class="fcx-clear" id="fcxClear">Clear all</button></div>
</div>
<div class="fcx-chips" id="fcxChips" aria-live="polite"></div>
<div class="fcx-status" id="fcxStatus">Loading the dashboard...</div>
<div class="fcx-body" id="fcxBody">
<div class="fcx-kpis" id="fcxKpis"></div>
<div class="fcx-grid">
<article class="fcx-card"><header><div><h3>How files progress</h3><p>Files reaching each stage; the rest were discontinued, are open, or ended another way.</p></div><button class="fcx-toggle" data-table="funnel">Table</button></header><div id="fcxFunnel"></div></article>
<article class="fcx-card"><header><div><h3>Grant rates by year filed</h3><p>Share of leave decisions and of merits judgments that were granted.</p></div><button class="fcx-toggle" data-table="rates">Table</button></header><div id="fcxRates"></div></article>
<article class="fcx-card wide"><header><div><h3>Outcomes by year filed</h3><p>How each year's files ended. Click a year to filter the whole page.</p></div><button class="fcx-toggle" data-table="outcomes">Table</button></header><div id="fcxOutcomes"></div></article>
<article class="fcx-card"><header><div><h3>Leave granted by decision under review</h3><p>Bar length is the leave grant rate; files in brackets. Click to filter.</p></div><button class="fcx-toggle" data-table="bodies">Table</button></header><div id="fcxBodies"></div></article>
<article class="fcx-card"><header><div><h3>Office that made the decision</h3><p>Most frequent visa posts, IRB regions and processing centres. Click to filter.</p></div><button class="fcx-toggle" data-table="offices">Table</button></header><div id="fcxOffices"></div></article>
<article class="fcx-card"><header><div><h3>Time between steps</h3><p>Median days (tick) with the middle half of files (band).</p></div><button class="fcx-toggle" data-table="durations">Table</button></header><div id="fcxDurations"></div></article>
<article class="fcx-card"><header><div><h3>Median days from filing to leave decision</h3><p>By year filed; years with fewer than 30 leave decisions (often recent, still open) are left out.</p></div><button class="fcx-toggle" data-table="leavetime">Table</button></header><div id="fcxLeaveTime"></div></article>
<article class="fcx-card wide"><header><div><h3>Motions by type</h3><p>Ruled motions split granted / dismissed, plus withdrawn and never ruled. Grant rate counts ruled motions only.</p></div><button class="fcx-toggle" data-table="motions">Table</button></header><div id="fcxMotions"></div></article>
<article class="fcx-card wide"><header><div><h3>Judges: leave versus judicial review</h3><p>Each dot is a judge (at least 25 leave decisions): leave grant rate across, judicial review grant rate up, size by decisions. Click a dot to filter.</p></div><button class="fcx-toggle" data-table="judges">Table</button></header><div id="fcxJudges"></div></article>
<article class="fcx-card"><header><div><h3>Applicant counsel</h3><p>Counsel named in a quarter of files. Click a row to filter.</p></div></header><div id="fcxCounsel"></div></article>
<article class="fcx-card"><header><div><h3>Procedural deadlines</h3><p>IRPA s. 72 and the FC Immigration Rules 10, 11 and 15.</p></div><button class="fcx-toggle" data-table="compliance">Table</button></header><div id="fcxCompliance"></div></article>
<article class="fcx-card"><header><div><h3>Why leave was refused</h3><p>Refusals where the applicant never filed a record, against refusals on the record.</p></div><button class="fcx-toggle" data-table="refusals">Table</button></header><div id="fcxRefusals"></div></article>
<article class="fcx-card"><header><div><h3>Registry</h3><p>Files by registry office, with leave grant rate. Click to filter.</p></div><button class="fcx-toggle" data-table="cities">Table</button></header><div id="fcxCities"></div></article>
</div>
<p class="fcx-note" style="padding:0 16px 16px">Read from the Federal Court registry entries for each file. Rates use files with an observed decision; small groups are not reliable, so counts sit beside every rate. Motions never ruled on are inferred from what happened next in the file.</p>
</div>
</section>
"""

FC_ANALYTICS_JS = r"""
<div id="fcxTooltip" role="tooltip"></div>
<script>
(function(){
const LABELS={leave_refused:'Leave refused',discontinued:'Discontinued or withdrawn',jr_dismissed:'JR dismissed',jr_granted:'JR granted',settled:'Settled or allowed on motion',other:'Other ending',open_or_unknown:'Open or not observed',
irb_rpd:'IRB Refugee Protection Division',irb_rad:'IRB Refugee Appeal Division',irb_iad:'IRB Immigration Appeal Division',irb_id:'IRB Immigration Division',irb:'IRB (division not stated)',prra_officer:'PRRA officer',visa_office:'Visa office abroad',cbsa:'CBSA',ircc:'IRCC / CIC officer',minister:'Minister or delegate',citizenship:'Citizenship',unknown:'Not recorded',
leave_and_judicial_review:'Leave and judicial review',leave_and_judicial_review_extension_of_time:'Leave and JR, filed late',leave_judicial_review_and_mandamus:'Mandamus (delay)',direct_judicial_review:'Direct judicial review',
within_limit:'Within the limit',late_extension_sought:'Late, extension sought',late_no_extension_noted:'Late, no extension noted',notice_date_unknown:'Notice date not recorded',on_time:'On time',within_a_few_days:'Within a few days',late:'Late',late_extension_granted:'Late, extension granted',not_filed:'Never filed',within_window:'Within 30 to 90 days',outside_window:'Outside 30 to 90 days',
not_perfected:'No applicant record filed',refused_after_perfection:'Refused on the record',not_applicable:'Leave not refused',represented:'Counsel named',self_represented:'Self-represented',mixed:'Counsel and self-represented'};
const OUTCOMES=[['leave_refused','var(--fcx-s1)'],['discontinued','var(--fcx-s2)'],['jr_dismissed','var(--fcx-s3)'],['jr_granted','var(--fcx-s4)'],['settled','var(--fcx-s5)'],['other','var(--fcx-s6)'],['open_or_unknown','var(--fcx-neutral)']];
const CHIP_LABELS={year:'Year',office:'Office',judge:'Judge',counsel:'Counsel',resolution:'Outcome',city:'Registry',decision_body:'Decision under review'};
const state={filters:{},chips:{},data:null,judges:[],counsel:[],tables:{},sort:{},years:[],loaded:false,options:false};
const $=id=>document.getElementById(id);
const label=v=>LABELS[v]||String(v??'').replace(/_/g,' ');
const num=v=>v===null||v===undefined?'—':new Intl.NumberFormat().format(v);
const pct=v=>v===null||v===undefined?'—':`${(v*100).toFixed(1)}%`;
const svgEl=(tag,attrs={},text)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);for(const [k,v] of Object.entries(attrs))el.setAttribute(k,v);if(text!==undefined)el.textContent=text;return el};
const el=(tag,attrs={},text)=>{const node=document.createElement(tag);for(const [k,v] of Object.entries(attrs))node.setAttribute(k,v);if(text!==undefined)node.textContent=text;return node};
// Tooltip: values lead, labels follow; labels are inserted as text, never HTML.
const tip=$('fcxTooltip');
function showTip(event,title,rows){tip.replaceChildren();tip.appendChild(el('div',{class:'t'},title));for(const [name,value,color] of rows){const r=el('div',{class:'r'});if(color){const k=el('span',{class:'k'});k.style.background=color;r.appendChild(k)}r.appendChild(el('b',{},value));r.appendChild(document.createTextNode(' '+name));tip.appendChild(r)}tip.style.display='block';moveTip(event)}
function moveTip(event){const rect=event.target.getBoundingClientRect?.();const x=event.clientX??(rect?rect.left+rect.width/2:0),y=event.clientY??(rect?rect.top:0);const w=tip.offsetWidth,h=tip.offsetHeight;tip.style.left=`${Math.min(window.innerWidth-w-8,x+14)}px`;tip.style.top=`${Math.max(8,y-h-12)}px`}
function hideTip(){tip.style.display='none'}
function hover(node,title,rows,onClick){node.setAttribute('tabindex','0');node.classList.add('fcx-hit');node.addEventListener('pointermove',e=>showTip(e,title,rows));node.addEventListener('pointerleave',hideTip);node.addEventListener('focus',e=>showTip(e,title,rows));node.addEventListener('blur',hideTip);if(onClick){node.addEventListener('click',()=>{hideTip();onClick()});node.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();onClick()}})}}
function empty(box,message){box.replaceChildren(el('div',{class:'fcx-empty'},message||'No files match these filters.'))}
function legend(items,line){const wrap=el('div',{class:'fcx-legend'});for(const [name,color] of items){const s=el('span');const k=el('i',line?{class:'line'}:{});k.style.background=color;s.appendChild(k);s.appendChild(document.createTextNode(name));wrap.appendChild(s)}return wrap}
function table(box,key,columns,rows,onRow){const sort=state.sort[key]||{col:null,dir:-1};const sorted=sort.col===null?rows:[...rows].sort((a,b)=>{const x=a[sort.col],y=b[sort.col];if(typeof x==='string'||typeof y==='string')return String(x??'').localeCompare(String(y??''))*sort.dir;return((x??-Infinity)-(y??-Infinity))*sort.dir});
const wrap=el('div',{class:'fcx-scroll'}),t=el('table'),head=el('tr');columns.forEach(([col,title])=>{const th=el('th',{scope:'col'},title+(sort.col===col?(sort.dir<0?' ▾':' ▴'):''));th.addEventListener('click',()=>{state.sort[key]={col,dir:sort.col===col?-sort.dir:-1};table(box,key,columns,rows,onRow)});head.appendChild(th)});const thead=el('thead');thead.appendChild(head);t.appendChild(thead);const body=el('tbody');
sorted.forEach(row=>{const tr=el('tr',onRow?{class:'fcx-row',tabindex:'0'}:{});columns.forEach(([col,,fmt])=>tr.appendChild(el('td',{},fmt?fmt(row[col],row):String(row[col]??'—'))));if(onRow){tr.addEventListener('click',()=>onRow(row));tr.addEventListener('keydown',e=>{if(e.key==='Enter')onRow(row)})}body.appendChild(tr)});t.appendChild(body);wrap.appendChild(t);box.replaceChildren(wrap)}

// ---- chart primitives ------------------------------------------------------
function barsH(box,rows,{value,fmt,title,sub,color='var(--fcx-s1)',onClick,max,tipRows}){if(!rows.length)return empty(box);const W=560,rowH=26,left=190,right=sub?140:70,H=rows.length*rowH+8,scaleMax=max??Math.max(...rows.map(r=>r[value]||0),1);const svg=svgEl('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':title});
rows.forEach((row,i)=>{const y=4+i*rowH,v=row[value]||0,w=Math.max(0,(W-left-right)*v/scaleMax);const g=svgEl('g');g.appendChild(svgEl('rect',{x:0,y,width:W,height:rowH,fill:'transparent'}));g.appendChild(svgEl('text',{x:left-8,y:y+rowH/2+4,'text-anchor':'end',class:'fcx-label'},(row._label||'').length>30?row._label.slice(0,29)+'…':row._label));
if(w>0){g.appendChild(svgEl('rect',{class:'fcx-mark',x:left,y:y+6,width:w,height:rowH-12,rx:4,fill:typeof color==='function'?color(row):color}))}g.appendChild(svgEl('text',{x:left+w+6,y:y+rowH/2+4,class:'fcx-value'},fmt(v,row)+(sub?` ${sub(row)}`:'')));hover(g,row._label,tipRows?tipRows(row):[[title,fmt(v,row)]],onClick?()=>onClick(row):null);svg.appendChild(g)});box.replaceChildren(svg)}
function lineChart(box,points,series,{yFmt,yMax,title,minN}){const W=560,H=230,L=44,R=96,T=14,B=28;if(points.length<2)return empty(box,'Not enough years with decisions for a trend.');const maxY=yMax??Math.max(...points.flatMap(p=>series.map(s=>p[s.key]??0)),1)*1.1;const x=i=>L+i*(W-L-R)/(points.length-1),y=v=>T+(H-T-B)*(1-v/maxY);const svg=svgEl('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':title});
for(let k=0;k<=4;k++){const v=maxY*k/4;svg.appendChild(svgEl('line',{class:'fcx-gridline',x1:L,x2:W-R,y1:y(v),y2:y(v)}));svg.appendChild(svgEl('text',{class:'fcx-axis',x:L-6,y:y(v)+4,'text-anchor':'end'},yFmt(v,true)))}
points.forEach((p,i)=>{if(i%Math.ceil(points.length/10)===0||i===points.length-1)svg.appendChild(svgEl('text',{class:'fcx-axis',x:x(i),y:H-8,'text-anchor':'middle'},String(p.year)))});
series.forEach(s=>{const valid=points.map((p,i)=>[i,p[s.key]]).filter(([i,v])=>v!==null&&v!==undefined&&(!s.n||s.n(points[i])>=(minN||0)));if(!valid.length)return;svg.appendChild(svgEl('path',{d:valid.map(([i,v],n)=>`${n?'L':'M'}${x(i).toFixed(1)},${y(v).toFixed(1)}`).join(' '),fill:'none',stroke:s.color,'stroke-width':2,'stroke-linejoin':'round'}));const [li,lv]=valid[valid.length-1];svg.appendChild(svgEl('circle',{cx:x(li),cy:y(lv),r:4,fill:s.color,stroke:'var(--fcx-surface)','stroke-width':2}));svg.appendChild(svgEl('text',{class:'fcx-label',x:x(li)+8,y:y(lv)+4},`${s.label} ${yFmt(lv)}`))});
const hair=svgEl('line',{x1:0,x2:0,y1:T,y2:H-B,stroke:'var(--fcx-ink-2)','stroke-width':1,visibility:'hidden'});svg.appendChild(hair);const hit=svgEl('rect',{x:L,y:T,width:W-L-R,height:H-T-B,fill:'transparent'});svg.appendChild(hit);
const at=e=>{const r=svg.getBoundingClientRect(),px=(e.clientX-r.left)*W/r.width;return Math.max(0,Math.min(points.length-1,Math.round((px-L)/((W-L-R)/(points.length-1)))))};
hit.addEventListener('pointermove',e=>{const i=at(e),p=points[i];hair.setAttribute('x1',x(i));hair.setAttribute('x2',x(i));hair.setAttribute('visibility','visible');showTip(e,String(p.year),series.map(s=>[s.label+(s.n?` (${num(s.n(p))})`:''),(!s.n||s.n(p)>=(minN||0))?yFmt(p[s.key]):'too few',s.color]))});hit.addEventListener('pointerleave',()=>{hair.setAttribute('visibility','hidden');hideTip()});
box.replaceChildren(svg);if(series.length>1)box.appendChild(legend(series.map(s=>[s.label,s.color]),true))}
function stacked(box,rows,cats,{title,onClick}){if(!rows.length)return empty(box);const W=1100,H=280,L=50,R=10,T=10,B=28,max=Math.max(...rows.map(r=>r.files),1),bw=(W-L-R)/rows.length,y=v=>T+(H-T-B)*(1-v/max);const svg=svgEl('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':title});
for(let k=0;k<=4;k++){const v=max*k/4;svg.appendChild(svgEl('line',{class:'fcx-gridline',x1:L,x2:W-R,y1:y(v),y2:y(v)}));svg.appendChild(svgEl('text',{class:'fcx-axis',x:L-6,y:y(v)+4,'text-anchor':'end'},num(Math.round(v))))}
rows.forEach((row,i)=>{const g=svgEl('g'),x0=L+i*bw+1,w=Math.max(1,bw-2);let acc=0;g.appendChild(svgEl('rect',{x:L+i*bw,y:T,width:bw,height:H-T-B,fill:'transparent'}));cats.forEach(([key,color],c)=>{const v=row.outcomes[key]||0;if(!v)return;const top=y(acc+v),h=y(acc)-top;g.appendChild(svgEl('rect',{class:'fcx-mark',x:x0,y:top+(acc?0:0),width:w,height:Math.max(0,h-1.5),fill:color,rx:c===cats.length-1?0:0}));acc+=v});
if(i%Math.ceil(rows.length/16)===0||i===rows.length-1)g.appendChild(svgEl('text',{class:'fcx-axis',x:x0+w/2,y:H-8,'text-anchor':'middle'},String(row.year)));hover(g,`${row.year} · ${num(row.files)} files`,cats.filter(([k])=>row.outcomes[k]).map(([k,c])=>[label(k),num(row.outcomes[k]),c]),onClick?()=>onClick(row):null);svg.appendChild(g)});box.replaceChildren(svg);box.appendChild(legend(cats.map(([k,c])=>[label(k),c])))}
function funnel(box,stages){if(!stages.length||!stages[0].count)return empty(box);const steps=['var(--fcx-q1)','var(--fcx-q2)','var(--fcx-q3)','var(--fcx-q4)','var(--fcx-q5)','var(--fcx-q6)'];const top=stages[0].count;barsH(box,stages.map((s,i)=>({...s,_label:s.stage,_i:i})),{value:'count',fmt:(v)=>num(v),sub:r=>`(${((r.count/top)*100).toFixed(0)}%)`,title:'Files reaching each stage',color:r=>steps[r._i]||steps[5],max:top,tipRows:r=>[['files',num(r.count)],['of all filed',`${((r.count/top)*100).toFixed(1)}%`]]})}
function ranges(box,durations){const rows=Object.values(durations).filter(d=>d.count);if(!rows.length)return empty(box);const W=560,rowH=34,L=190,R=70,H=rows.length*rowH+24,max=Math.max(...rows.map(d=>d.p75||0),30)*1.05,x=v=>L+(W-L-R)*v/max;const svg=svgEl('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Days between procedural steps'});
for(let k=0;k<=4;k++){const v=max*k/4;svg.appendChild(svgEl('line',{class:'fcx-gridline',x1:x(v),x2:x(v),y1:0,y2:H-20}));svg.appendChild(svgEl('text',{class:'fcx-axis',x:x(v),y:H-6,'text-anchor':'middle'},`${Math.round(v)}d`))}
rows.forEach((d,i)=>{const yy=i*rowH+6,g=svgEl('g');g.appendChild(svgEl('rect',{x:0,y:yy,width:W,height:rowH,fill:'transparent'}));g.appendChild(svgEl('text',{class:'fcx-label',x:L-8,y:yy+rowH/2+3,'text-anchor':'end'},d.label));g.appendChild(svgEl('rect',{class:'fcx-mark',x:x(d.p25),y:yy+9,width:Math.max(3,x(d.p75)-x(d.p25)),height:rowH-18,rx:4,fill:'var(--fcx-q2)'}));g.appendChild(svgEl('rect',{x:x(d.median)-1.5,y:yy+5,width:3,height:rowH-10,fill:'var(--fcx-ink)'}));g.appendChild(svgEl('text',{class:'fcx-value',x:x(d.p75)+6,y:yy+rowH/2+3},`${num(d.median)}d`));hover(g,d.label,[['median days',num(d.median)],['middle half',`${num(d.p25)}–${num(d.p75)} days`],['files',num(d.count)]]);svg.appendChild(g)});box.replaceChildren(svg)}
function motionBars(box,rows){if(!rows.length)return empty(box);const cats=[['granted','Granted','var(--fcx-s1)'],['dismissed','Dismissed','var(--fcx-s2)'],['withdrawn','Withdrawn','var(--fcx-s4)'],['not_ruled','Never ruled','var(--fcx-neutral)']];const W=1100,rowH=26,L=260,R=120,H=rows.length*rowH+8,max=Math.max(...rows.map(r=>r.motions),1);const svg=svgEl('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Motions by type and outcome'});
rows.forEach((r,i)=>{const y=4+i*rowH,g=svgEl('g');let acc=0;g.appendChild(svgEl('rect',{x:0,y,width:W,height:rowH,fill:'transparent'}));g.appendChild(svgEl('text',{class:'fcx-label',x:L-8,y:y+rowH/2+4,'text-anchor':'end'},r.label));cats.forEach(([k,,c])=>{const v=r[k]||0;if(!v)return;const w=(W-L-R)*v/max;g.appendChild(svgEl('rect',{class:'fcx-mark',x:L+acc,y:y+6,width:Math.max(1,w-2),height:rowH-12,fill:c}));acc+=w});g.appendChild(svgEl('text',{class:'fcx-value',x:L+acc+6,y:y+rowH/2+4},`${num(r.motions)} · ${pct(r.grant_rate)} granted`));
hover(g,r.label,[...cats.map(([k,n,c])=>[n,num(r[k]),c]),['grant rate (ruled)',pct(r.grant_rate)],['median days to ruling',num(r.median_days)]]);svg.appendChild(g)});box.replaceChildren(svg);box.appendChild(legend(cats.map(([,n,c])=>[n,c])))}
function scatter(box,judges){const pts=judges.filter(j=>j.leave_decisions>=25&&j.leave_grant_rate!==null);if(!pts.length)return empty(box,'No judge has enough decisions in this view.');const W=1100,H=360,L=50,R=20,T=12,B=34,maxX=Math.min(1,Math.max(...pts.map(p=>p.leave_grant_rate))*1.1),x=v=>L+(W-L-R)*v/maxX,y=v=>T+(H-T-B)*(1-v),maxN=Math.max(...pts.map(p=>p.leave_decisions+p.jr_decisions));const svg=svgEl('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Judges by leave and judicial review grant rate'});
for(let k=0;k<=4;k++){svg.appendChild(svgEl('line',{class:'fcx-gridline',x1:L,x2:W-R,y1:y(k/4),y2:y(k/4)}));svg.appendChild(svgEl('text',{class:'fcx-axis',x:L-6,y:y(k/4)+4,'text-anchor':'end'},`${k*25}%`));const xv=maxX*k/4;svg.appendChild(svgEl('text',{class:'fcx-axis',x:x(xv),y:H-14,'text-anchor':'middle'},`${Math.round(xv*100)}%`))}
svg.appendChild(svgEl('text',{class:'fcx-axis',x:W-R,y:H-2,'text-anchor':'end'},'Leave granted →'));svg.appendChild(svgEl('text',{class:'fcx-axis',x:L+4,y:T+10},'↑ JR granted (judges with 5+ judgments)'));
pts.sort((a,b)=>(b.leave_decisions+b.jr_decisions)-(a.leave_decisions+a.jr_decisions)).forEach(p=>{const hasJr=p.jr_decisions>=5&&p.jr_grant_rate!==null,cy=hasJr?y(p.jr_grant_rate):H-B-4,r=4+10*Math.sqrt((p.leave_decisions+p.jr_decisions)/maxN),g=svgEl('g');g.appendChild(svgEl('circle',{cx:x(p.leave_grant_rate),cy,r:Math.max(r,12),fill:'transparent'}));g.appendChild(svgEl('circle',{class:'fcx-mark',cx:x(p.leave_grant_rate),cy,r,fill:hasJr?'var(--fcx-s1)':'var(--fcx-neutral)','fill-opacity':.75,stroke:'var(--fcx-surface)','stroke-width':2}));
hover(g,p.name,[['leave granted',`${pct(p.leave_grant_rate)} of ${num(p.leave_decisions)}`],['JR granted',hasJr?`${pct(p.jr_grant_rate)} of ${num(p.jr_decisions)}`:'too few judgments'],['stays granted',p.stay_decisions?`${pct(p.stay_grant_rate)} of ${num(p.stay_decisions)}`:'—']],()=>setChip('judge',p.key,p.name));svg.appendChild(g)});box.replaceChildren(svg);box.appendChild(legend([['5 or more merits judgments','var(--fcx-s1)'],['fewer judgments (placed at bottom)','var(--fcx-neutral)']]))}

// ---- rendering ---------------------------------------------------------------
function renderKpis(k){const box=$('fcxKpis');box.replaceChildren();[['Files',num(k.files),`${num(k.record_filed)} with an applicant's record`],['Leave granted',pct(k.leave_grant_rate),`of ${num(k.leave_decisions)} leave decisions`],['JR granted',pct(k.jr_grant_rate),`of ${num(k.jr_decisions)} merits judgments`],['Settled or allowed on motion',num(k.settled),'consent orders and judgments'],['Median days to leave',num(k.median_days_to_leave),'filing to leave decision'],['Stays granted',pct(k.stay_grant_rate),`of ${num(k.stay_rulings)} stay rulings`]].forEach(([t,v,s])=>{const d=el('div',{class:'fcx-kpi'});d.appendChild(el('span',{},t));d.appendChild(el('b',{},v));d.appendChild(el('small',{},s));box.appendChild(d)})}
const VIEWS={
 funnel:{box:'fcxFunnel',chart:d=>funnel($('fcxFunnel'),d.funnel),table:d=>table($('fcxFunnel'),'funnel',[['stage','Stage'],['count','Files',num]],d.funnel)},
 rates:{box:'fcxRates',chart:d=>lineChart($('fcxRates'),d.by_year,[{key:'leave_grant_rate',label:'Leave',color:'var(--fcx-s1)',n:p=>p.leave_granted+p.leave_refused},{key:'jr_grant_rate',label:'JR',color:'var(--fcx-s2)',n:p=>p.jr_granted+p.jr_dismissed}],{yFmt:(v,axis)=>axis?`${Math.round(v*100)}%`:pct(v),yMax:1,title:'Grant rates by year',minN:20}),table:d=>table($('fcxRates'),'rates',[['year','Year'],['leave_grant_rate','Leave granted',pct],['leave_granted','Leave decisions',(v,r)=>num(r.leave_granted+r.leave_refused)],['jr_grant_rate','JR granted',pct],['jr_granted','JR judgments',(v,r)=>num(r.jr_granted+r.jr_dismissed)]],d.by_year)},
 outcomes:{box:'fcxOutcomes',chart:d=>stacked($('fcxOutcomes'),d.by_year,OUTCOMES,{title:'Outcomes by year filed',onClick:row=>setChip('year',row.year,String(row.year))}),table:d=>table($('fcxOutcomes'),'outcomes',[['year','Year'],['files','Files',num],...OUTCOMES.map(([k])=>[k,label(k),(v,r)=>num(r.outcomes[k]||0)])],d.by_year,row=>setChip('year',row.year,String(row.year)))},
 bodies:{box:'fcxBodies',chart:d=>barsH($('fcxBodies'),d.by_decision_body.filter(r=>r.value!=='unknown'&&r.leave_granted+r.leave_refused>=20).map(r=>({...r,_label:label(r.value)})),{value:'leave_grant_rate',fmt:v=>pct(v),sub:r=>`(${num(r.files)})`,title:'Leave grant rate',max:Math.max(...d.by_decision_body.map(r=>r.leave_grant_rate||0),0.05),tipRows:r=>[['leave granted',`${pct(r.leave_grant_rate)} of ${num(r.leave_granted+r.leave_refused)}`],['JR granted',`${pct(r.jr_grant_rate)} of ${num(r.jr_granted+r.jr_dismissed)}`],['files',num(r.files)]],onClick:r=>setFilter('decision_body',r.value)}),table:d=>table($('fcxBodies'),'bodies',[['value','Decision under review',v=>label(v)],['files','Files',num],['leave_grant_rate','Leave granted',pct],['jr_grant_rate','JR granted',pct]],d.by_decision_body,r=>setFilter('decision_body',r.value))},
 offices:{box:'fcxOffices',chart:d=>barsH($('fcxOffices'),d.by_office.map(r=>({...r,_label:r.value})),{value:'files',fmt:v=>num(v),sub:r=>`· ${pct(r.leave_grant_rate)} leave`,title:'Files',tipRows:r=>[['files',num(r.files)],['leave granted',`${pct(r.leave_grant_rate)} of ${num(r.leave_granted+r.leave_refused)}`]],onClick:r=>setChip('office',r.value,r.value)}),table:d=>table($('fcxOffices'),'offices',[['value','Office'],['files','Files',num],['leave_grant_rate','Leave granted',pct],['jr_grant_rate','JR granted',pct]],d.by_office,r=>setChip('office',r.value,r.value))},
 durations:{box:'fcxDurations',chart:d=>ranges($('fcxDurations'),d.durations),table:d=>table($('fcxDurations'),'durations',[['label','Step'],['median','Median days',num],['p25','25th pct',num],['p75','75th pct',num],['count','Files',num]],Object.values(d.durations))},
 leavetime:{box:'fcxLeaveTime',chart:d=>lineChart($('fcxLeaveTime'),d.by_year.filter(r=>r.median_days_to_leave!==null&&r.leave_granted+r.leave_refused>=30),[{key:'median_days_to_leave',label:'Median',color:'var(--fcx-s1)'}],{yFmt:v=>`${Math.round(v)}d`,title:'Median days from filing to leave decision'}),table:d=>table($('fcxLeaveTime'),'leavetime',[['year','Year'],['median_days_to_leave','Median days',num],['leave_granted','Leave decisions',(v,r)=>num(r.leave_granted+r.leave_refused)]],d.by_year)},
 motions:{box:'fcxMotions',chart:d=>motionBars($('fcxMotions'),d.motions),table:d=>table($('fcxMotions'),'motions',[['label','Motion type'],['motions','Filed',num],['granted','Granted',num],['dismissed','Dismissed',num],['grant_rate','Grant rate',pct],['withdrawn','Withdrawn',num],['not_ruled','Never ruled',num],['median_days','Median days',num]],d.motions)},
 judges:{box:'fcxJudges',chart:()=>scatter($('fcxJudges'),state.judges),table:()=>table($('fcxJudges'),'judges',[['name','Judge'],['leave_decisions','Leave decisions',num],['leave_grant_rate','Leave granted',pct],['jr_decisions','JR judgments',num],['jr_grant_rate','JR granted',pct],['motion_decisions','Motion rulings',num],['motion_grant_rate','Motions granted',pct],['stay_decisions','Stay rulings',num],['stay_grant_rate','Stays granted',pct],['median_days_hearing_to_judgment','Days to judgment',num]],state.judges,r=>setChip('judge',r.key,r.name))},
 compliance:{box:'fcxCompliance',chart:d=>{const box=$('fcxCompliance');box.replaceChildren();const names={filing_timeliness:'Filed within IRPA s. 72',record_timeliness:"Applicant's record (Rule 10)",memorandum_timeliness:"Respondent's memorandum (Rule 11)",hearing_window:'Hearing after leave (Rule 15)'};const colors=['var(--fcx-s1)','var(--fcx-s2)','var(--fcx-s3)','var(--fcx-s4)','var(--fcx-s5)'];for(const [key,rows] of Object.entries(d.compliance)){const known=rows.filter(r=>r.value!=='unknown'&&r.value!=='notice_date_unknown');const missing=rows.filter(r=>r.value==='unknown'||r.value==='notice_date_unknown').reduce((a,r)=>a+r.count,0);const total=known.reduce((a,r)=>a+r.count,0);const h=el('div',{class:'fcx-note'},`${names[key]} · ${num(total)} files with the dates needed`+(missing?` (${num(missing)} without)`:''));box.appendChild(h);if(!total)continue;const W=560,svg=svgEl('svg',{viewBox:`0 0 ${W} 22`,role:'img','aria-label':names[key]});let acc=0;known.forEach((r,i)=>{const w=W*r.count/total;const g=svgEl('g');g.appendChild(svgEl('rect',{class:'fcx-mark',x:acc,y:2,width:Math.max(1,w-2),height:16,rx:2,fill:colors[i%colors.length]}));hover(g,names[key],[[label(r.value),`${num(r.count)} (${(100*r.count/total).toFixed(1)}%)`,colors[i%colors.length]]]);svg.appendChild(g);acc+=w});box.appendChild(svg);box.appendChild(legend(known.map((r,i)=>[`${label(r.value)} ${(100*r.count/total).toFixed(0)}%`,colors[i%colors.length]])))}},table:d=>table($('fcxCompliance'),'compliance',[['rule','Rule'],['value','Status',v=>label(v)],['count','Files',num]],Object.entries(d.compliance).flatMap(([k,rows])=>rows.map(r=>({rule:k.replace(/_/g,' '),...r}))))},
 refusals:{box:'fcxRefusals',chart:d=>barsH($('fcxRefusals'),d.refusal_reasons.filter(r=>r.value!=='not_applicable'&&r.value!=='unknown').map(r=>({...r,_label:label(r.value)})),{value:'count',fmt:v=>num(v),title:'Leave refusals'}),table:d=>table($('fcxRefusals'),'refusals',[['value','Reason',v=>label(v)],['count','Files',num]],d.refusal_reasons)},
 cities:{box:'fcxCities',chart:d=>barsH($('fcxCities'),d.by_city.filter(r=>r.value!=='unknown').map(r=>({...r,_label:r.value})),{value:'files',fmt:v=>num(v),sub:r=>`· ${pct(r.leave_grant_rate)} leave`,title:'Files',onClick:r=>setFilter('city',r.value)}),table:d=>table($('fcxCities'),'cities',[['value','Registry'],['files','Files',num],['leave_grant_rate','Leave granted',pct],['jr_grant_rate','JR granted',pct]],d.by_city,r=>setFilter('city',r.value))},
};
function renderView(key){const view=VIEWS[key];if(!view||!state.data)return;(state.tables[key]?view.table:view.chart)(state.data);const btn=document.querySelector(`#fcAnalyticsPanel [data-table="${key}"]`);if(btn){btn.textContent=state.tables[key]?'Chart':'Table';btn.setAttribute('aria-pressed',String(!!state.tables[key]))}}
function renderCounsel(){table($('fcxCounsel'),'counsel',[['name','Counsel'],['files','Files',num],['leave_grant_rate','Leave',pct],['jr_grant_rate','JR',pct],['resolved_by_consent','Settled',num]],state.counsel,r=>setChip('counsel',r.key,r.name))}
function renderAll(){renderKpis(state.data.kpis);Object.keys(VIEWS).forEach(renderView);renderCounsel()}

// ---- filters -----------------------------------------------------------------
function query(extra={}){const p=new URLSearchParams();const f={...state.filters,...extra};for(const [k,v] of Object.entries(f))if(v!==''&&v!==null&&v!==undefined)p.set(k,v);for(const [k,c] of Object.entries(state.chips)){if(k==='year'){p.set('year_from',c.value);p.set('year_to',c.value)}else p.set(k,c.value)}return p}
function setFilter(key,value){state.filters[key]=value;const select=document.querySelector(`#fcAnalyticsPanel [data-filter="${key}"]`);if(select)select.value=value;load()}
function setChip(key,value,text){state.chips[key]={value,text};load()}
function renderChips(){const box=$('fcxChips');box.replaceChildren();for(const [k,c] of Object.entries(state.chips)){const chip=el('span',{class:'fcx-chip'});chip.appendChild(document.createTextNode(`${CHIP_LABELS[k]||k}: ${c.text}`));const x=el('button',{type:'button','aria-label':`Remove ${CHIP_LABELS[k]||k} filter`},'×');x.addEventListener('click',()=>{delete state.chips[k];load()});chip.appendChild(x);box.appendChild(chip)}}
function syncUrl(){const url=new URL(location.href);['year_from','year_to','city','decision_body','application_type','representation','language','office','judge','counsel','year'].forEach(k=>url.searchParams.delete(k));if(url.searchParams.get('tab')==='fc-analytics'){const q=query();for(const [k,v] of q)url.searchParams.set(k,v);history.replaceState(null,'',url.pathname+url.search)}}
function fillOptions(d){if(state.options)return;state.options=true;state.years=d.by_year.map(r=>r.year);for(const id of ['fcxYearFrom','fcxYearTo']){const s=$(id);state.years.forEach(y=>s.appendChild(el('option',{value:y},String(y))))}d.by_city.filter(r=>r.value!=='unknown').forEach(r=>$('fcxCity').appendChild(el('option',{value:r.value},r.value)));d.by_decision_body.filter(r=>r.value!=='unknown').forEach(r=>$('fcxBody').appendChild(el('option',{value:r.value},label(r.value))));['leave_and_judicial_review','leave_and_judicial_review_extension_of_time','leave_judicial_review_and_mandamus','direct_judicial_review'].forEach(v=>$('fcxType').appendChild(el('option',{value:v},label(v))));for(const [k,v] of Object.entries(state.filters)){const s=document.querySelector(`#fcAnalyticsPanel [data-filter="${k}"]`);if(s)s.value=v}}
let seq=0;
async function load(){const mine=++seq;renderChips();$('fcxBody').classList.add('is-loading');$('fcxStatus').textContent='Updating...';const q=query();syncUrl();
 const judgeQ=new URLSearchParams();for(const k of ['year_from','year_to','decision_body'])if(q.get(k))judgeQ.set(k,q.get(k));judgeQ.set('min_decisions','25');const counselQ=new URLSearchParams(judgeQ);counselQ.delete('min_decisions');counselQ.set('min_files','15');if(q.get('city'))counselQ.set('city',q.get('city'));
 try{const [d,j,c]=await Promise.all([fetch(`/api/fc-activity/dashboard?${q}`).then(r=>{if(!r.ok)throw new Error(`Dashboard request failed (${r.status})`);return r.json()}),fetch(`/api/fc-activity/judges?${judgeQ}`).then(r=>r.ok?r.json():{judges:[]}),fetch(`/api/fc-activity/counsel?${counselQ}`).then(r=>r.ok?r.json():{counsel:[]})]);if(mine!==seq)return;
 state.data=d;state.judges=j.judges||[];state.counsel=c.counsel||[];fillOptions(d);renderAll();$('fcxStatus').textContent=`${num(d.kpis.files)} files in this view.`+(Object.keys(state.chips).length||Object.values(state.filters).some(Boolean)?' Clear all to return to every file.':'')}
 catch(error){if(mine!==seq)return;$('fcxStatus').textContent=`Dashboard unavailable: ${error.message}`}finally{if(mine===seq)$('fcxBody').classList.remove('is-loading')}}
function preset(kind){document.querySelectorAll('#fcxPresets button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.preset===kind)));const last=state.years.length?Math.max(...state.years):new Date().getFullYear();state.filters.year_from=kind==='all'?'':String(last-Number(kind)+1);state.filters.year_to='';$('fcxYearFrom').value=state.filters.year_from;$('fcxYearTo').value='';load()}
document.querySelectorAll('#fcAnalyticsPanel [data-filter]').forEach(s=>s.addEventListener('change',()=>{state.filters[s.dataset.filter]=s.value;if(s.dataset.filter.startsWith('year'))document.querySelectorAll('#fcxPresets button').forEach(b=>b.setAttribute('aria-pressed','false'));load()}));
document.querySelectorAll('#fcxPresets button').forEach(b=>b.addEventListener('click',()=>preset(b.dataset.preset)));
$('fcxClear').addEventListener('click',()=>{state.filters={};state.chips={};document.querySelectorAll('#fcAnalyticsPanel [data-filter]').forEach(s=>s.value='');document.querySelectorAll('#fcxPresets button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.preset==='all')));load()});
document.querySelectorAll('#fcAnalyticsPanel [data-table]').forEach(b=>b.addEventListener('click',()=>{const k=b.dataset.table;state.tables[k]=!state.tables[k];renderView(k)}));
window.fcxLoadDashboard=function(){if(state.loaded)return;state.loaded=true;const params=new URLSearchParams(location.search);for(const k of ['year_from','year_to','city','decision_body','application_type','representation','language'])if(params.get(k))state.filters[k]=params.get(k);for(const k of ['office','judge','counsel'])if(params.get(k))state.chips[k]={value:params.get(k),text:params.get(k)};load()};
if(new URLSearchParams(location.search).get('tab')==='fc-analytics')window.fcxLoadDashboard();
})();
</script>
"""


def inject_fc_analytics(html: str) -> str:
    """Add the FC Analytics tab, panel, styles and script to the data explorer page."""
    html = html.replace(
        '<button class="tab" type="button" data-nav-group="research" data-tab="fc-history"',
        FC_ANALYTICS_TAB + '\n<button class="tab" type="button" data-nav-group="research" data-tab="fc-history"',
        1,
    )
    html = html.replace("</head>", f"<style>{FC_ANALYTICS_CSS}</style>\n</head>", 1)
    html = html.replace('<section id="themesPanel"', FC_ANALYTICS_PANEL + '<section id="themesPanel"', 1)
    html = html.replace(
        "'fc-history':'fcHistoryPanel',themes:'themesPanel'};\nconst researchGroups",
        "'fc-history':'fcHistoryPanel','fc-analytics':'fcAnalyticsPanel',themes:'themesPanel'};\nconst researchGroups",
        1,
    )
    html = html.replace("research:['search','citation-intelligence','judge-profile','fc-history','themes']", "research:['search','citation-intelligence','judge-profile','fc-analytics','fc-history','themes']", 1)
    html = html.replace(
        "  if(selected==='fc-history'){loadFcActivityTimeline();",
        "  if(selected==='fc-analytics'&&window.fcxLoadDashboard)window.fcxLoadDashboard();\n  if(selected==='fc-history'){loadFcActivityTimeline();",
        1,
    )
    html = html.replace("</body>", FC_ANALYTICS_JS + "\n</body>", 1)
    return html
