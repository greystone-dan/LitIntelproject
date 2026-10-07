"""Workbench page: demo sign-in, then three views (Analyst home, Live analysis, De-identifier).

Same look as the research site (cream paper, Newsreader headings, ink buttons). Analyst home is drawn
here from ``/workbench/api/*``; Live analysis and De-identifier are the existing tools shown in
same-origin frames in their embedded mode, so their own pages keep working at their own addresses.
"""

from __future__ import annotations

_HEAD = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Workbench | iLIT</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,600;6..72,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#f1efe8;--surface:#fffef9;--surface-alt:#f8f6ef;--border:#d8d5ca;--text:#202522;--muted:#69726d;--muted-2:#8b928d;--ink:#202522;--blue:#315d8d;--blue-soft:#e7eef6;--teal:#176c68;--green:#176c68;--green-soft:#edf5f3;--amber:#c28e2d;--amber-soft:#f8f0dc;--rust:#a4412b;--red-soft:#f7e8e3}
*{box-sizing:border-box}html,body{margin:0;min-height:100%}
body{background:var(--bg);color:var(--text);font:14px/1.5 "IBM Plex Sans",sans-serif;background-image:linear-gradient(rgba(32,37,34,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(32,37,34,.035) 1px,transparent 1px);background-size:26px 26px}
button,input,select,textarea{font:inherit;color:inherit}
a{color:var(--teal)}
:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
.topbar{display:flex;align-items:center;flex-wrap:wrap;gap:16px;min-height:68px;padding:10px 24px;border-bottom:1px solid var(--border);background:rgba(255,254,249,.96)}
.topnav{display:flex;flex-wrap:wrap;gap:4px}
.topnav a{display:flex;align-items:center;min-width:72px;min-height:40px;padding:8px 12px;border-radius:5px;color:var(--muted);font-size:12px;font-weight:600;text-decoration:none;justify-content:center}
.topnav a:hover{color:var(--teal)}.topnav a.active{background:var(--ink);color:#fff}
.brand{margin-right:auto;display:flex;align-items:baseline;gap:13px;color:inherit;text-decoration:none;padding:6px 10px;border-radius:6px}.brand:hover{background:#f1efe6}
.brand-name{font:700 28px/1 "Newsreader",serif}.brand-sub{font-size:12px;color:var(--muted)}
.userpill{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted)}
.userpill b{color:var(--text)}
.demo-flag{padding:2px 7px;border:1px solid #e3c88d;border-radius:999px;background:var(--amber-soft);color:#7a5714;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.linkbtn{border:0;background:none;color:var(--teal);cursor:pointer;font-size:12px;text-decoration:underline;padding:0}
main{max-width:1280px;margin:0 auto;padding:18px 28px 48px}
.eyebrow{color:var(--rust);font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
h1{margin:6px 0 4px;font:700 31px/1.1 "Newsreader",serif}
.lead{margin:0;color:var(--muted);font-size:13px;max-width:70ch}
h2{margin:0;font:600 19px/1.2 "Newsreader",serif}
.card{border:1px solid var(--border);border-radius:5px;background:rgba(255,254,249,.94)}
.card>header{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;padding:12px 16px;border-bottom:1px solid var(--border)}
.card>.body{padding:14px 16px}
.btn{height:36px;padding:0 14px;border:1px solid var(--ink);border-radius:5px;background:var(--ink);color:#fff;font-size:11px;font-weight:700;letter-spacing:.04em;cursor:pointer;white-space:nowrap}
.btn.secondary{background:var(--surface);color:var(--ink);border-color:var(--border)}
.btn.small{height:30px;padding:0 10px;font-size:11px}
.btn.danger{background:var(--surface);color:var(--rust);border-color:#e0bcb2}
.btn:disabled{opacity:.5;cursor:not-allowed}
input[type=text],input[type=date],select,textarea{width:100%;padding:8px 10px;border:1px solid var(--border);border-radius:5px;background:#fff;font-size:13px}
textarea{resize:vertical;min-height:70px;line-height:1.5}
label.fl{display:block;margin:0 0 5px;color:var(--muted);font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.hint{color:var(--muted);font-size:12px}
.err{margin:10px 0 0;padding:9px 12px;border:1px solid #e0bcb2;border-radius:5px;background:var(--red-soft);color:#7d2f1d;font-size:13px}
.hidden{display:none!important}
/* sign-in */
.signin{max-width:480px;margin:40px auto}
.signin .body{display:grid;gap:12px}
.demo-note{padding:10px 12px;border-left:3px solid var(--amber);background:var(--amber-soft);font-size:12px;color:#5c4510}
/* tabs */
.subtabs{display:flex;gap:0;margin:16px 0 14px;border-bottom:1px solid var(--border);overflow-x:auto}
.subtabs button{border:0;background:transparent;padding:10px 14px;color:var(--muted);font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;cursor:pointer;white-space:nowrap}
.subtabs button[aria-selected=true]{color:var(--text);box-shadow:inset 0 -2px var(--rust)}
.reading-live .toolframe{position:fixed;inset:0;z-index:60;width:100vw;height:100vh;min-height:0;border:0;border-radius:0}
.toolframe{display:block;width:100%;height:calc(100vh - 210px);min-height:560px;border:1px solid var(--border);border-radius:5px;background:var(--surface)}
/* home */
.tiles{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin-bottom:14px}
.tile{padding:12px 14px;border:1px solid var(--border);border-radius:5px;background:var(--surface);text-align:left;cursor:default}
button.tile{cursor:pointer}button.tile:hover{border-color:var(--teal)}
.tile b{display:block;font:700 26px/1.1 "Newsreader",serif}.tile span{color:var(--muted);font-size:11px;letter-spacing:.04em}
.tile.alert b{color:var(--rust)}
.homegrid{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(300px,1fr);gap:14px;align-items:start}
.stack{display:grid;gap:14px;min-width:0}
.addrow{display:grid;grid-template-columns:minmax(0,1fr) 170px auto;gap:10px;align-items:end}
.filters{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:14px 0 6px}
.filters input[type=text]{max-width:210px}.filters select{width:auto;max-width:170px}
.chk{display:inline-flex;align-items:center;gap:6px;font-size:12px;color:var(--muted)}
.rows{display:grid;gap:0;margin-top:6px}
.row{border-top:1px solid var(--border)}
.row:first-child{border-top:0}
.rowhead{display:grid;grid-template-columns:150px minmax(0,1fr);gap:6px 12px;align-items:center;width:100%;padding:11px 4px;border:0;background:transparent;text-align:left;cursor:pointer}
.rowhead:hover{background:var(--surface-alt)}
.imm{font:600 13px "IBM Plex Mono",monospace;color:var(--text)}
.soc{min-width:0}.soc strong{display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:600;font-size:13px}
.soc small{color:var(--muted);font-size:11px}
.chips{display:flex;flex-wrap:wrap;gap:5px;justify-content:flex-start;align-items:center}.rowhead .chips{grid-column:2}
.pill{display:inline-flex;align-items:center;padding:3px 8px;border:1px solid var(--border);border-radius:999px;background:var(--surface-alt);color:var(--muted);font-size:11px;white-space:nowrap}
.pill.flag{background:var(--rust);border-color:var(--rust);color:#fff;font-weight:700}
.pill.warn{background:var(--amber-soft);border-color:#e3c88d;color:#7a5714}
.pill.over{background:var(--red-soft);border-color:#e0bcb2;color:#7d2f1d;font-weight:700}
.pill.tag{background:var(--blue-soft);border-color:#c9d8ea;color:#27476b}
.pill.ok{background:var(--green-soft);border-color:#c5dfda;color:#115450}
.detail{padding:4px 4px 16px 4px;display:grid;gap:12px}
.detail .two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.newbox{padding:10px 12px;border:1px solid #e0bcb2;border-left:3px solid var(--rust);border-radius:5px;background:#fffaf8;font-size:12px}
.newbox ul{margin:6px 0 0;padding-left:18px}
.timeline{max-height:230px;overflow:auto;border:1px solid var(--border);border-radius:5px;background:#fff;font-size:12px}
.timeline div{display:grid;grid-template-columns:86px minmax(0,1fr);gap:10px;padding:6px 10px;border-top:1px solid var(--border)}
.timeline div:first-child{border-top:0}.timeline .d{font-family:"IBM Plex Mono",monospace;color:var(--muted)}.timeline .n{background:#fff6f2}
.actions{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.empty{padding:18px 6px;color:var(--muted);font-size:13px}
.pin{padding:11px 0;border-top:1px solid var(--border)}.pin:first-child{border-top:0}
.pin .t{display:grid;grid-template-columns:auto minmax(0,1fr);gap:9px;align-items:start}
.pin a.ttl{font-weight:600;color:var(--text);text-decoration:none}.pin a.ttl:hover{color:var(--teal);text-decoration:underline}
.pin .meta{color:var(--muted);font-size:11px}
.pin .more{margin:8px 0 0 25px;display:grid;gap:8px}
.mini{display:grid;gap:6px;font-size:13px}.mini .line{display:flex;justify-content:space-between;gap:10px;padding:6px 0;border-top:1px solid var(--border)}.mini .line:first-child{border-top:0}
.mini button.sq{border:0;background:none;padding:0;text-align:left;cursor:pointer;color:var(--text)}.mini button.sq:hover{color:var(--teal);text-decoration:underline}
.toast{position:fixed;left:50%;bottom:22px;transform:translateX(-50%);padding:9px 16px;border-radius:5px;background:var(--ink);color:#fff;font-size:13px;z-index:50;box-shadow:0 8px 24px rgba(0,0,0,.2)}
@media(max-width:980px){.homegrid{grid-template-columns:minmax(0,1fr)}.tiles{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:640px){main{padding:14px 16px 40px}.topbar{padding:10px 16px}.brand{margin:0;flex-basis:100%}.topnav{width:100%;margin-left:0!important}.topnav a{flex:1;min-width:0;padding:8px 4px}.addrow{grid-template-columns:1fr}.rowhead{grid-template-columns:minmax(0,1fr)}.rowhead .chips{grid-column:1}.detail .two{grid-template-columns:1fr}.toolframe{height:calc(100vh - 160px)}h1{font-size:26px}.card>header{padding:10px 12px}.card>.body{padding:12px}}
</style>
</head>
'''

_BODY = r'''<body>
<header class="topbar">
<a class="brand" href="/data-explorer?tab=about&group=info" title="Back to the About page" aria-label="ILIT, Immigration Litigation Intelligence System: back to the About page"><span class="brand-name">ILIT</span><span class="brand-sub">Immigration Litigation Intelligence System</span></a>
<nav class="topnav" style="margin-left:auto" aria-label="Primary navigation">
<a href="/data-explorer?tab=about">About</a>
<a href="/data-explorer?tab=search">Research</a>
<a href="/data-explorer?tab=judge-profile">Intelligence / Statistics</a>
<a href="/workbench" class="active" aria-current="page">Workbench</a>
<a href="/data-explorer?tab=soon-themes&group=soon">Coming soon</a>
</nav>
<div class="userpill hidden" id="userPill"><span class="demo-flag">Demo</span><span>Signed in as <b id="userName"></b></span><button class="linkbtn" id="signOut" type="button">Sign out</button></div>
</header>
<main>
<section id="signinView" class="hidden">
<div class="signin card">
<header><div><div class="eyebrow">Workbench</div><h2>Sign in to your Workbench</h2></div><span class="demo-flag">Demo</span></header>
<div class="body">
<p class="hint" style="margin:0">Your own space for tracked IMM files, pinned decisions, notes, and the two document tools.</p>
<div class="demo-note"><strong>Demo sign-in only.</strong> There is no password and no real account yet. The name you enter just keeps your list apart from other demo users. Do not enter anything sensitive. Documents you open in Live analysis or the De-identifier are never saved.</div>
<div><label class="fl" for="signinName">Your name</label><input type="text" id="signinName" maxlength="60" autocomplete="off" placeholder="For example: Demo analyst"></div>
<div class="err hidden" id="signinErr"></div>
<div class="actions"><button class="btn" id="signinGo" type="button">Enter the Workbench</button><button class="btn secondary" id="signinDemo" type="button">Continue as demo analyst</button></div>
</div>
</div>
</section>

<section id="appView" class="hidden">
<div class="eyebrow">Workbench</div>
<h1>Your analyst workbench</h1>
<p class="lead">Track your Federal Court files, keep the decisions you rely on, and work on your own documents without leaving the site. Demo sign-in: lists are kept per name, with no password.</p>
<div class="subtabs" role="tablist" aria-label="Workbench views">
<button type="button" role="tab" id="tab-home" data-view="home" aria-selected="true" aria-controls="view-home">Analyst home</button>
<button type="button" role="tab" id="tab-live" data-view="live" aria-selected="false" aria-controls="view-live">Live analysis</button>
<button type="button" role="tab" id="tab-deid" data-view="deid" aria-selected="false" aria-controls="view-deid">De-identifier</button>
</div>

<section id="view-home" role="tabpanel" aria-labelledby="tab-home">
<div class="card hidden" id="briefCard" style="margin-bottom:14px"><header><div><h2>Morning brief</h2><div class="hint" id="briefSub"></div></div><div class="actions"><a class="btn secondary small" style="display:inline-flex;align-items:center;text-decoration:none" href="/workbench/brief" target="_blank" rel="noopener">Printable brief</a><button class="btn small" id="briefSeen" type="button">Mark all viewed</button></div></header><div class="body"><div class="mini" id="briefList"></div></div></div>
<div class="tiles" id="tiles"></div>
<div class="homegrid">
<div class="stack">
<div class="card" id="caseCard">
<header><div><h2>Case list</h2><div class="hint">IMM files you follow. A flag shows when the stored Federal Court docket has moved since you last viewed the file.</div></div>
<div class="actions"><button class="btn secondary small" id="markAll" type="button">Mark all viewed</button><a class="btn secondary small" style="display:inline-flex;align-items:center;text-decoration:none" href="/workbench/api/cases/export.csv" id="exportCases">Export CSV</a></div></header>
<div class="body">
<div class="addrow">
<div><label class="fl" for="addText">Add IMM numbers</label><textarea id="addText" rows="2" style="min-height:40px" placeholder="IMM-1234-19, IMM-5678-24. You can also paste rows from Excel (IMM number, then a name)." autocomplete="off"></textarea></div>
<div><label class="fl" for="addFolder">Folder (optional)</label><input type="text" id="addFolder" list="folderList" maxlength="80" placeholder="e.g. H&amp;C files"></div>
<button class="btn" id="addGo" type="button">Add to list</button>
</div>
<div class="hint" style="margin-top:6px">Bulk import: paste a table, or <label class="linkbtn" style="cursor:pointer">choose a .csv or .txt file<input type="file" id="addFile" accept=".csv,.txt,.tsv,text/plain,text/csv" class="hidden"></label>. Ctrl+Enter adds.</div>
<div class="err hidden" id="addErr"></div>
<div class="hint hidden" id="addMsg" style="margin-top:8px"></div>
<div class="filters">
<input type="text" id="fText" placeholder="Filter by IMM, name or note" aria-label="Filter the case list">
<select id="fFolder" aria-label="Folder"><option value="">All folders</option></select>
<select id="fTag" aria-label="Tag"><option value="">All tags</option></select>
<label class="chk"><input type="checkbox" id="fFlag"> Only flagged</label>
<span class="hint" id="countNote"></span>
</div>
<div class="rows" id="caseRows"><div class="empty">Loading…</div></div>
</div>
</div>
</div>
<div class="stack">
<div class="card">
<header><div><h2>Pinned decisions</h2><div class="hint">Saved from the case reader with “Save to Workbench”.</div></div>
<div class="actions"><button class="btn secondary small" id="compareGo" type="button" disabled>Compare selected</button><a class="btn secondary small" style="display:inline-flex;align-items:center;text-decoration:none" href="/workbench/api/pins/export.csv">Export CSV</a></div></header>
<div class="body"><div class="filters" style="margin-top:0"><select id="pFolder" aria-label="Folder"><option value="">All folders</option></select></div><div id="pinRows"><div class="empty">Loading…</div></div></div>
</div>
<div class="card"><header><h2>Deadlines</h2></header><div class="body"><div class="mini" id="deadlineList"></div></div></div>
<div class="card"><header><h2>Saved and recent searches</h2><button class="linkbtn" id="clearRecent" type="button">Clear</button></header><div class="body"><div class="mini" id="recentList"></div></div></div>
</div>
</div>
<datalist id="folderList"></datalist>
</section>

<section id="view-live" role="tabpanel" aria-labelledby="tab-live" class="hidden"><iframe class="toolframe" id="frame-live" title="Live analysis" data-src="/live-analysis?embed=1"></iframe></section>
<section id="view-deid" role="tabpanel" aria-labelledby="tab-deid" class="hidden"><iframe class="toolframe" id="frame-deid" title="De-identifier" data-src="/deidentify?embed=1"></iframe></section>
</section>
</main>
'''

_SCRIPT = r'''<script>
(function(){
const $=id=>document.getElementById(id);
const E=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let cases=[],pins=[],summary=null,openCase=null,openPin=null;
const picked=new Set();
function toast(m){const t=document.createElement('div');t.className='toast';t.textContent=m;document.body.appendChild(t);setTimeout(()=>t.remove(),2200)}
async function api(url,opt){
  const r=await fetch(url,Object.assign({headers:{'Content-Type':'application/json'}},opt||{}));
  if(r.status===401){showSignin();throw new Error('Sign in first.')}
  const j=await r.json().catch(()=>({}));
  if(!r.ok)throw new Error(typeof j.detail==='string'?j.detail:'Something went wrong ('+r.status+').');
  return j;
}
const post=(u,b)=>api(u,{method:'POST',body:JSON.stringify(b||{})});
const patch=(u,b)=>api(u,{method:'PATCH',body:JSON.stringify(b)});
const del=u=>api(u,{method:'DELETE'});
const fmt=d=>{if(!d)return '';const x=new Date(String(d).slice(0,10)+'T00:00:00');return isNaN(x)?String(d):x.toLocaleDateString('en-CA',{year:'numeric',month:'short',day:'numeric'})};
const daysTo=d=>Math.round((new Date(d+'T00:00:00')-new Date(new Date().toDateString()))/864e5);

/* ---------- sign-in ---------- */
window.addEventListener('message',e=>{if(e.origin!==location.origin||!e.data||!e.data.ilitLive)return;const f=$('frame-live');if(!f||e.source!==f.contentWindow)return;document.body.classList.toggle('reading-live',e.data.ilitLive==='open')});
function showSignin(){$('appView').classList.add('hidden');$('userPill').classList.add('hidden');$('signinView').classList.remove('hidden');setTimeout(()=>$('signinName').focus(),50)}
async function signIn(name){
  $('signinErr').classList.add('hidden');
  try{const me=await post('/workbench/api/signin',{name});enter(me)}
  catch(e){$('signinErr').textContent=e.message;$('signinErr').classList.remove('hidden')}
}
$('signinGo').onclick=()=>signIn($('signinName').value);
$('signinName').addEventListener('keydown',e=>{if(e.key==='Enter')signIn($('signinName').value)});
$('signinDemo').onclick=()=>signIn('Demo analyst');
$('signOut').onclick=async()=>{await post('/workbench/api/signout');cases=[];pins=[];showSignin()};
function enter(me){
  $('signinView').classList.add('hidden');$('appView').classList.remove('hidden');
  $('userName').textContent=me.display;$('userPill').classList.remove('hidden');
  route();loadAll();
}

/* ---------- sub views ---------- */
const VIEWS=['home','live','deid'];
function route(){
  let v=(location.hash||'#home').slice(1);if(!VIEWS.includes(v))v='home';showView(v,false);
}
function showView(v,push=true){
  document.body.classList.remove('reading-live');
  VIEWS.forEach(n=>{$('view-'+n).classList.toggle('hidden',n!==v);$('tab-'+n).setAttribute('aria-selected',String(n===v))});
  const f=$('frame-'+v);if(f&&!f.getAttribute('src'))f.setAttribute('src',f.dataset.src);
  if(push&&location.hash!=='#'+v)history.replaceState(null,'','#'+v);
}
document.querySelectorAll('.subtabs button').forEach(b=>{b.onclick=()=>showView(b.dataset.view);b.addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight'].includes(e.key))return;const i=VIEWS.indexOf(b.dataset.view),n=VIEWS[(i+(e.key==='ArrowRight'?1:-1)+VIEWS.length)%VIEWS.length];showView(n);$('tab-'+n).focus()})});
window.addEventListener('hashchange',route);

/* ---------- load ---------- */
async function loadAll(){
  try{
    const [c,p,s]=await Promise.all([api('/workbench/api/cases'),api('/workbench/api/pins'),api('/workbench/api/summary')]);
    cases=c.cases;pins=p.pins;summary=s;renderAll();
  }catch(e){$('caseRows').innerHTML='<div class="empty">'+E(e.message)+'</div>'}
}
function renderAll(){renderBrief();renderTiles();renderFilters();renderCases();renderPins();renderDeadlines();renderRecent()}
function renderBrief(){
  const flagged=cases.filter(c=>c.flagged),dl=((summary&&summary.deadlines)||[]).filter(d=>d.days<=7);
  $('briefCard').classList.toggle('hidden',!flagged.length&&!dl.length);
  $('briefSub').textContent=`${flagged.length} file${flagged.length===1?'':'s'} moved since you last looked${dl.length?`, ${dl.length} deadline${dl.length===1?'':'s'} within a week or overdue`:''}.`;
  $('briefList').innerHTML=dl.map(d=>`<div class="line"><span><b>${E(d.imm_number)}</b> <span class="hint">${E(d.label)}</span></span><span class="pill ${d.days<0?'over':'warn'}">${d.days<0?'Overdue '+(-d.days)+' d':d.days===0?'Today':'in '+d.days+' d'}</span></div>`).join('')+
   flagged.slice(0,8).map(c=>`<div class="line"><span style="min-width:0"><button class="sq" type="button" data-brief="${c.id}"><b>${E(c.imm_number)}</b> ${E(c.label||c.style_of_cause||'')}</button><div class="hint">${E(c.flag_reasons.join('; '))}${c.new_entry_preview.length?' · '+E(c.new_entry_preview[c.new_entry_preview.length-1].entry.slice(0,110)):''}</div></span></div>`).join('')+(flagged.length>8?`<div class="hint">and ${flagged.length-8} more in the case list below.</div>`:'');
  document.querySelectorAll('[data-brief]').forEach(b=>b.onclick=()=>{openCase=Number(b.dataset.brief);renderCases();toggleDetailLoad(cases.find(c=>c.id===openCase));const r=document.querySelector(`.row[data-id="${openCase}"]`);r&&r.scrollIntoView({behavior:'smooth',block:'center'})});
}
$('briefSeen').onclick=()=>$('markAll').click();

function renderTiles(){
  const s=summary||{cases:0,flagged:0,pins:0,deadlines:[]};
  const due=s.deadlines.length;
  $('tiles').innerHTML=
   `<button class="tile${s.flagged?' alert':''}" type="button" data-go="flag"><b>${s.flagged}</b><span>Files with new activity</span></button>`+
   `<div class="tile"><b>${s.cases}</b><span>IMM files tracked</span></div>`+
   `<div class="tile"><b>${s.pins}</b><span>Pinned decisions</span></div>`+
   `<div class="tile${due?' alert':''}"><b>${due}</b><span>Deadlines in 30 days</span></div>`;
  const t=document.querySelector('[data-go=flag]');if(t)t.onclick=()=>{$('fFlag').checked=true;renderCases();$('caseCard').scrollIntoView({behavior:'smooth'})};
}

function renderFilters(){
  const folders=[...new Set([...cases.map(c=>c.folder),...pins.map(p=>p.folder)].filter(Boolean))].sort();
  const tags=[...new Set(cases.flatMap(c=>c.tags))].sort();
  const keep=(sel,list,all)=>{const cur=sel.value;sel.innerHTML=`<option value="">${all}</option>`+list.map(x=>`<option>${E(x)}</option>`).join('');if(list.includes(cur))sel.value=cur};
  keep($('fFolder'),folders,'All folders');keep($('fTag'),tags,'All tags');keep($('pFolder'),folders,'All folders');
  $('folderList').innerHTML=folders.map(x=>`<option value="${E(x)}">`).join('');
}

/* ---------- case list ---------- */
function visibleCases(){
  const q=$('fText').value.trim().toLowerCase(),f=$('fFolder').value,t=$('fTag').value,fl=$('fFlag').checked;
  return cases.filter(c=>(!f||c.folder===f)&&(!t||c.tags.includes(t))&&(!fl||c.flagged)&&(!q||[c.imm_number,c.style_of_cause,c.label,c.notes,c.status,c.tags.join(' ')].join(' ').toLowerCase().includes(q)));
}
function deadlinePill(c){
  if(!c.deadline)return '';const d=daysTo(c.deadline);
  const txt=(c.deadline_label||'Due')+' '+fmt(c.deadline);
  if(d<0)return `<span class="pill over" title="${E(txt)}">Overdue ${-d} d</span>`;
  if(d<=7)return `<span class="pill warn" title="${E(txt)}">${E(c.deadline_label||'Due')} in ${d} d</span>`;
  return `<span class="pill" title="${E(txt)}">${E(c.deadline_label||'Due')} ${E(fmt(c.deadline))}</span>`;
}
function renderCases(){
  const list=visibleCases();
  $('countNote').textContent=cases.length?`${list.length} of ${cases.length} shown`:'';
  if(!cases.length){$('caseRows').innerHTML='<div class="empty">No files yet. Type or paste IMM numbers above to start your list.</div>';return}
  if(!list.length){$('caseRows').innerHTML='<div class="empty">No files match these filters.</div>';return}
  $('caseRows').innerHTML=list.map(c=>{
    const open=openCase===c.id;
    return `<div class="row" data-id="${c.id}"><button type="button" class="rowhead" data-open="${c.id}" aria-expanded="${open}">
      <span class="imm">${E(c.imm_number)}</span>
      <span class="soc"><strong>${E(c.label||c.style_of_cause||(c.known?'(no style of cause stored)':'Not in the stored docket data yet'))}</strong><small>${c.known?`${c.entries} docket entries${c.latest_activity?' · latest '+E(fmt(c.latest_activity)):''}`:'Added to your list; flags appear once the file is loaded'}</small></span>
      <span class="chips">${c.flagged?`<span class="pill flag">● ${E(c.flag_reasons[0])}</span>`:''}${c.status?`<span class="pill">${E(c.status)}</span>`:''}${c.folder?`<span class="pill" title="Folder">&#128193; ${E(c.folder)}</span>`:''}${deadlinePill(c)}${c.tags.slice(0,3).map(t=>`<span class="pill tag">${E(t)}</span>`).join('')}</span></button>${open?detailHtml(c):''}</div>`}).join('');
  document.querySelectorAll('[data-open]').forEach(b=>b.onclick=()=>toggleCase(Number(b.dataset.open)));
  if(openCase!==null)wireDetail();
}
function detailHtml(c){
  const d=c._detail;
  const nb=c.flagged?`<div class="newbox"><strong>Since you last viewed:</strong> ${c.flag_reasons.map(E).join('; ')}.${c.new_entry_preview.length?`<ul>${c.new_entry_preview.map(e=>`<li><b>${E(fmt(e.date))}</b> ${E(e.entry)}</li>`).join('')}</ul>`:''}</div>`:'';
  const tl=d?(d.timeline.length?`<div class="timeline" role="log" aria-label="Docket entries, newest last">${d.timeline.slice(-25).map(e=>`<div class="${e.new?'n':''}"><span class="d">${E(fmt(e.date))}</span><span>${E(e.entry)}</span></div>`).join('')}</div>`:'<div class="hint">No docket entries are stored for this file yet.</div>'):'<div class="hint">Loading docket…</div>';
  const ms=d&&d.milestones&&d.milestones.length?`<div class="chips" aria-label="Milestones">${d.milestones.map(m=>`<span class="pill" title="${E(m.entry)}"><b style="margin-right:4px">${E(m.label)}</b>${E(fmt(m.date))}</span>`).join('')}</div>`:'';
  return `<div class="detail">${nb}
   <div class="actions"><button class="btn small" data-act="seen" type="button">${c.flagged?'Mark as viewed':'Mark viewed now'}</button>
   <a class="btn secondary small" style="display:inline-flex;align-items:center;text-decoration:none" href="/data-explorer?tab=fc-history&imm=${encodeURIComponent(c.imm_number)}" target="_blank" rel="noopener">Open FC activity</a>
   <a class="btn secondary small" style="display:inline-flex;align-items:center;text-decoration:none" href="/workbench/brief/case/${c.id}" target="_blank" rel="noopener">Printable case brief</a>
   <button class="btn secondary small" data-act="refresh" type="button" title="Fetches this one file from the Federal Court website and stores the result">Check FC website now</button>
   <button class="btn danger small" data-act="remove" type="button">Remove from list</button><span class="hint" id="detMsg"></span></div>
   ${ms}${tl}
   <div class="two"><div><label class="fl">Notes (saved when you click away)</label><textarea data-f="notes" maxlength="20000">${E(c.notes)}</textarea></div>
   <div><label class="fl">Label (optional)</label><input type="text" data-f="label" maxlength="255" value="${E(c.label||'')}" placeholder="Short name for this file">
   <div style="height:8px"></div><label class="fl">Folder</label><input type="text" data-f="folder" list="folderList" maxlength="80" value="${E(c.folder)}">
   <div style="height:8px"></div><label class="fl">Tags (comma separated)</label><input type="text" data-f="tags" value="${E(c.tags.join(', '))}" placeholder="e.g. urgent, H&amp;C, stay"></div></div>
   <div class="two"><div><label class="fl">Deadline</label><input type="date" data-f="deadline" value="${E(c.deadline||'')}"></div>
   <div><label class="fl">Deadline note</label><input type="text" data-f="deadline_label" maxlength="120" value="${E(c.deadline_label)}" placeholder="e.g. Respondent's record due"></div></div></div>`;
}
async function toggleCase(id){
  if(openCase===id){openCase=null;renderCases();return}
  openCase=id;renderCases();
  try{const d=await api('/workbench/api/cases/'+id);const c=cases.find(x=>x.id===id);if(c){c._detail=d;renderCases()}}catch(e){}
}
function wireDetail(){
  const row=document.querySelector(`.row[data-id="${openCase}"]`);if(!row)return;
  const c=cases.find(x=>x.id===openCase);
  row.querySelectorAll('[data-f]').forEach(el=>el.addEventListener('change',async()=>{
    const f=el.dataset.f;let v=el.value;const body={};
    body[f]=f==='tags'?v.split(',').map(s=>s.trim()).filter(Boolean):v;
    if(f==='deadline'&&!v){body.deadline_label=''}
    try{const u=await patch('/workbench/api/cases/'+c.id,body);Object.assign(c,u);$('detMsg')&&($('detMsg').textContent='Saved');const s=await api('/workbench/api/summary');summary=s;renderTiles();renderFilters();renderDeadlines();updateHead(c)}catch(e){toast(e.message)}
  }));
  row.querySelectorAll('[data-act]').forEach(b=>b.onclick=()=>caseAction(b.dataset.act,c,b));
}
function updateHead(c){/* keep the open row; refresh only its header chips */
  const row=document.querySelector(`.row[data-id="${c.id}"] .rowhead`);if(!row)return;
  const keepOpen=document.querySelector(`.row[data-id="${c.id}"] .detail`);
  const ae=document.activeElement;const tmp=document.createElement('div');tmp.innerHTML=`<div>${rowHeadOnly(c)}</div>`;
  row.innerHTML=tmp.firstChild.firstChild.innerHTML;
}
function rowHeadOnly(c){
  return `<button type="button" class="rowhead"><span class="imm">${E(c.imm_number)}</span><span class="soc"><strong>${E(c.label||c.style_of_cause||(c.known?'(no style of cause stored)':'Not in the stored docket data yet'))}</strong><small>${c.known?`${c.entries} docket entries${c.latest_activity?' · latest '+E(fmt(c.latest_activity)):''}`:'Added to your list; flags appear once the file is loaded'}</small></span><span class="chips">${c.flagged?`<span class="pill flag">● ${E(c.flag_reasons[0])}</span>`:''}${c.status?`<span class="pill">${E(c.status)}</span>`:''}${c.folder?`<span class="pill" title="Folder">&#128193; ${E(c.folder)}</span>`:''}${deadlinePill(c)}${c.tags.slice(0,3).map(t=>`<span class="pill tag">${E(t)}</span>`).join('')}</span></button>`;
}
async function caseAction(act,c,btn){
  try{
    if(act==='seen'){const u=await post(`/workbench/api/cases/${c.id}/seen`);Object.assign(c,u);toast('Marked as viewed');refreshSummary();renderCases();toggleDetailLoad(c)}
    else if(act==='remove'){if(!confirm('Remove '+c.imm_number+' from your list? Your notes on it are deleted too.'))return;await del('/workbench/api/cases/'+c.id);cases=cases.filter(x=>x.id!==c.id);openCase=null;toast('Removed');refreshSummary();renderAll()}
    else if(act==='refresh'){
      btn.disabled=true;$('detMsg').textContent='Checking the Federal Court website…';
      const r=await fetch('/api/fc-history?imm='+encodeURIComponent(c.imm_number));
      if(!r.ok){const j=await r.json().catch(()=>({}));throw new Error(j.detail||'The Federal Court website could not be reached.')}
      const fresh=await api('/workbench/api/cases/'+c.id);Object.assign(c,fresh);c._detail=fresh;refreshSummary();renderCases();toast(c.flagged?'New activity found':'Up to date')
    }
  }catch(e){toast(e.message);btn.disabled=false;const m=$('detMsg');if(m)m.textContent=''}
}
async function toggleDetailLoad(c){try{c._detail=await api('/workbench/api/cases/'+c.id);renderCases()}catch(e){}}
async function refreshSummary(){try{summary=await api('/workbench/api/summary');renderTiles();renderDeadlines()}catch(e){}}

$('addGo').onclick=async()=>{
  $('addErr').classList.add('hidden');$('addMsg').classList.add('hidden');
  const text=$('addText').value;if(!text.trim()){return}
  try{
    const r=await post('/workbench/api/cases',{text,folder:$('addFolder').value||null});
    $('addText').value='';
    const msg=[r.added.length?`Added ${r.added.length}.`:'',r.already_on_list.length?`Already on your list: ${r.already_on_list.join(', ')}.`:''].join(' ');
    $('addMsg').textContent=msg;$('addMsg').classList.remove('hidden');
    await loadAll();
  }catch(e){$('addErr').textContent=e.message;$('addErr').classList.remove('hidden')}
};
$('addText').addEventListener('keydown',e=>{if(e.key==='Enter'&&(e.ctrlKey||e.metaKey)){e.preventDefault();$('addGo').click()}});
$('addFile').addEventListener('change',async()=>{const f=$('addFile').files[0];if(!f)return;if(f.size>2e6){toast('That file is too large (2 MB limit).');return}$('addText').value=(await f.text()).slice(0,20000);$('addFile').value='';toast('File read. Check the text, then Add to list.')});
['fText','fFolder','fTag','fFlag'].forEach(id=>$(id).addEventListener('input',renderCases));
$('markAll').onclick=async()=>{if(!cases.some(c=>c.flagged)){toast('Nothing new to mark');return}await post('/workbench/api/cases/seen-all');toast('All files marked as viewed');loadAll()};

/* ---------- pinned decisions ---------- */
function renderPins(){
  const f=$('pFolder').value;
  const list=pins.filter(p=>!f||p.folder===f);
  $('compareGo').disabled=picked.size!==2;
  if(!pins.length){$('pinRows').innerHTML='<div class="empty">Nothing pinned yet. Open a decision in the case reader and choose “Save to Workbench”.</div>';return}
  $('pinRows').innerHTML=list.map(p=>{
    const open=openPin===p.id;
    return `<div class="pin" data-pin="${p.id}"><div class="t"><input type="checkbox" data-pick="${p.id}" aria-label="Select to compare" ${picked.has(p.id)?'checked':''}><div><a class="ttl" href="/data-explorer?tab=search&case_id=${p.case_id}" target="_blank" rel="noopener">${E(p.title)}</a>
      <div class="meta">${[p.citation,p.court,fmt(p.date)].filter(Boolean).map(E).join(' · ')}</div>
      <div class="chips" style="justify-content:flex-start;margin-top:5px">${p.folder?`<span class="pill">${E(p.folder)}</span>`:''}${p.tags.map(t=>`<span class="pill tag">${E(t)}</span>`).join('')}${p.cited_by?`<span class="pill" title="Decisions in the library that cite this one">cited by ${Number(p.cited_by).toLocaleString('en-CA')}</span>`:''}${p.notes?'<span class="pill ok">note</span>':''}<button class="linkbtn" data-pmore="${p.id}" type="button">${open?'Close':'Notes and tags'}</button></div></div></div>
      ${open?`<div class="more"><textarea data-pf="notes" placeholder="Notes on this decision" maxlength="20000">${E(p.notes)}</textarea><input type="text" data-pf="tags" placeholder="Tags, comma separated" value="${E(p.tags.join(', '))}"><input type="text" data-pf="folder" list="folderList" placeholder="Folder" maxlength="80" value="${E(p.folder)}"><div class="actions"><button class="btn danger small" data-punpin="${p.id}" type="button">Remove pin</button></div></div>`:''}</div>`}).join('');
  document.querySelectorAll('[data-pick]').forEach(cb=>cb.onchange=()=>{const id=Number(cb.dataset.pick);if(cb.checked){if(picked.size>=2){cb.checked=false;toast('Pick two decisions to compare');return}picked.add(id)}else picked.delete(id);$('compareGo').disabled=picked.size!==2});
  document.querySelectorAll('[data-pmore]').forEach(b=>b.onclick=()=>{const id=Number(b.dataset.pmore);openPin=openPin===id?null:id;renderPins()});
  document.querySelectorAll('[data-pf]').forEach(el=>el.addEventListener('change',async()=>{
    const id=openPin,p=pins.find(x=>x.id===id),f=el.dataset.pf,body={};body[f]=f==='tags'?el.value.split(',').map(s=>s.trim()).filter(Boolean):el.value;
    try{Object.assign(p,await patch('/workbench/api/pins/'+id,body));toast('Saved');renderFilters()}catch(e){toast(e.message)}}));
  document.querySelectorAll('[data-punpin]').forEach(b=>b.onclick=async()=>{const id=Number(b.dataset.punpin);if(!confirm('Remove this pin and its notes?'))return;await del('/workbench/api/pins/'+id);pins=pins.filter(x=>x.id!==id);picked.delete(id);openPin=null;refreshSummary();renderPins();renderFilters()});
}
$('pFolder').addEventListener('input',renderPins);
$('compareGo').onclick=()=>{const [a,b]=[...picked];location.href=`/compare?a=${a&&pins.find(p=>p.id===a).case_id}&b=${b&&pins.find(p=>p.id===b).case_id}`};

/* ---------- deadlines and recent searches ---------- */
function renderDeadlines(){
  const d=(summary&&summary.deadlines)||[];
  $('deadlineList').innerHTML=d.length?d.map(x=>`<div class="line"><button class="sq" type="button" data-dl="${x.id}">${E(x.imm_number)} <span class="hint">${E(x.label)}</span></button><span class="pill ${x.days<0?'over':x.days<=7?'warn':''}">${x.days<0?'Overdue '+(-x.days)+' d':x.days===0?'Today':fmt(x.deadline)}</span></div>`).join(''):'<div class="hint">No deadlines in the next 30 days. Add one to a file on your case list.</div>';
  document.querySelectorAll('[data-dl]').forEach(b=>b.onclick=()=>{openCase=Number(b.dataset.dl);$('fText').value='';$('fFolder').value='';$('fTag').value='';$('fFlag').checked=false;renderCases();toggleDetailLoad(cases.find(c=>c.id===openCase));const r=document.querySelector(`.row[data-id="${openCase}"]`);r&&r.scrollIntoView({behavior:'smooth',block:'center'})});
}
function load(key){try{return JSON.parse(localStorage.getItem(key)||'[]')}catch(e){return []}}
function store(key,v){try{localStorage.setItem(key,JSON.stringify(v))}catch(e){}}
const recent=()=>load('ilit_recent_searches'),saved=()=>load('ilit_saved_searches');
function renderRecent(){
  const r=recent(),sv=saved(),isSaved=q=>sv.some(x=>x.q.toLowerCase()===q.toLowerCase());
  const link=x=>`<a href="/data-explorer?tab=search&q=${encodeURIComponent(x.q)}">${E(x.q)}</a>`;
  $('recentList').innerHTML=(sv.length?`<div class="hint" style="text-transform:uppercase;letter-spacing:.06em;font-size:10px;font-weight:700">Saved searches</div>`+sv.map(x=>`<div class="line">${link(x)}<button class="linkbtn" data-unsave="${E(x.q)}" type="button" aria-label="Remove saved search ${E(x.q)}">Remove</button></div>`).join(''):'')+
   (r.length?`<div class="hint" style="text-transform:uppercase;letter-spacing:.06em;font-size:10px;font-weight:700;margin-top:6px">Recent</div>`+r.slice(0,8).map(x=>`<div class="line">${link(x)}<span class="hint">${isSaved(x.q)?'saved':`<button class="linkbtn" data-save="${E(x.q)}" type="button">Save</button>`} · ${E(fmt(x.at))}</span></div>`).join(''):(sv.length?'':'<div class="hint">Searches you run on the case search page appear here, and you can save the ones you repeat. Kept in this browser only.</div>'));
  document.querySelectorAll('[data-save]').forEach(b=>b.onclick=()=>{const q=b.dataset.save;store('ilit_saved_searches',[{q,at:new Date().toISOString()},...saved()].slice(0,30));renderRecent()});
  document.querySelectorAll('[data-unsave]').forEach(b=>b.onclick=()=>{store('ilit_saved_searches',saved().filter(x=>x.q!==b.dataset.unsave));renderRecent()});
}
$('clearRecent').onclick=()=>{try{localStorage.removeItem('ilit_recent_searches')}catch(e){}renderRecent()};

/* ---------- start ---------- */
(async function(){
  try{const me=await (await fetch('/workbench/api/me')).json();me.signed_in?enter(me):showSignin()}catch(e){showSignin()}
})();
})();
</script>
</body></html>
'''


def workbench_page_html() -> str:
	from ..site_tour import inject_site_tour

	return inject_site_tour(_HEAD + _BODY + _SCRIPT)
