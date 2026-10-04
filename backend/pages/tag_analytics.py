"""Tag Analytics tab: trends, specialization, and frequencies for legal tags.

Shows tag usage over time, judge specialization by tag, and the most frequently appearing tags.
"""

TAG_ANALYTICS_TAB = (
    '<button class="tab" type="button" data-nav-group="research" data-tab="tag-analytics" aria-pressed="false" '
    'aria-controls="tagAnalyticsPanel">Tag Analytics</button>'
)

TAG_ANALYTICS_CSS = r"""
.tga{--tga-surface:#fffef9;--tga-ink:#0b0b0b;--tga-ink-2:#52514e;--tga-muted:#7a7972;--tga-grid:#e7e4da;--tga-line:#d8d5ca;
--tga-s1:#2a78d6;--tga-s2:#eb6834;--tga-s3:#1baf7a;--tga-s4:#eda100;--tga-s5:#e87ba4;--tga-s6:#008300;color:var(--tga-ink)}
.tga .tga-header{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;margin-bottom:16px;padding:16px 16px 0}
.tga .tga-summary{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:0 16px 16px}
.tga .tga-kpi{border:1px solid var(--tga-line);background:#fff;padding:12px;border-radius:4px}
.tga .tga-kpi span{display:block;font-size:11px;color:var(--tga-ink-2);margin-bottom:4px}
.tga .tga-kpi b{display:block;font-size:22px;font-weight:600;color:var(--tga-ink)}
.tga .tga-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;padding:0 16px 16px}
.tga .tga-card{border:1px solid var(--tga-line);background:#fff;padding:12px 14px 14px;border-radius:4px}
.tga .tga-card.wide{grid-column:1 / -1}
.tga .tga-card h3{margin:0 0 6px;font-size:14px;font-weight:600}
.tga .tga-card p{margin:0 0 10px;font-size:11px;color:var(--tga-ink-2);line-height:1.4}
.tga svg{display:block;width:100%;height:auto}
.tga table{width:100%;border-collapse:collapse;font-size:11px;margin-top:8px}
.tga th,.tga td{padding:6px 8px;border-bottom:1px solid var(--tga-grid);text-align:right}
.tga th:first-child,.tga td:first-child{text-align:left}
.tga th{color:var(--tga-ink-2);font-weight:600;background:#fff}
.tga tr:hover td{background:#f6f4ee}
.tga .tga-empty{padding:20px;text-align:center;font-size:12px;color:var(--tga-ink-2)}
.tga .tga-loading{opacity:.5}
@media(max-width:820px){.tga .tga-grid{grid-template-columns:1fr}.tga .tga-card.wide{grid-column:auto}.tga .tga-summary{grid-template-columns:1fr}}
"""

TAG_ANALYTICS_PANEL = r"""
<section id="tagAnalyticsPanel" class="panel-card search-layout tga" hidden>
<div class="page-header"><div class="eyebrow">V3 Core Tagging</div><h2>Tag Analytics</h2><p>Usage trends, judge specialization, and top tags across the corpus. See which legal issues appear most frequently and which judges handle which topics.</p></div>
<div class="tga-header" id="tgaStatus">Loading tag analytics...</div>
<div class="tga-summary" id="tgaSummary"></div>
<div class="tga-grid">
<article class="tga-card wide"><header><h3>Tag frequency by year</h3><p>Top 5 tags by case count, trending over time.</p></header><div id="tgaTrends"></div></article>
<article class="tga-card"><header><h3>Top 15 tags</h3><p>Most frequently appearing tags in the corpus.</p></header><div id="tgaFrequency"></div></article>
<article class="tga-card"><header><h3>Judge specialization</h3><p>Most common tags per judge (judges with 5+ tagged cases).</p></header><div id="tgaJudges"></div></article>
</div>
</section>
"""

TAG_ANALYTICS_JS = r"""
<script>
(function(){
const el=(tag,attrs={},text)=>{const node=document.createElement(tag);for(const [k,v] of Object.entries(attrs))node.setAttribute(k,v);if(text!==undefined)node.textContent=text;return node};
const svgEl=(tag,attrs={},text)=>{const n=document.createElementNS('http://www.w3.org/2000/svg',tag);for(const [k,v] of Object.entries(attrs))n.setAttribute(k,v);if(text)n.textContent=text;return n};
const num=v=>v===null||v===undefined?'—':new Intl.NumberFormat().format(v);
const $=id=>document.getElementById(id);

let state={data:null,loaded:false};

function renderSummary(data){const box=$('tgaSummary');box.replaceChildren();
const items=[
['Total Tags','',data.summary.total_tags],
['Cases Tagged','',data.summary.unique_cases_tagged],
['Categories','',data.summary.unique_categories],
];
items.forEach(([label,_,value])=>{const kpi=el('div',{class:'tga-kpi'});kpi.appendChild(el('span',{},label));kpi.appendChild(el('b',{},num(value)));box.appendChild(kpi)});
}

function renderTrends(data){const box=$('tgaTrends');
if(!data.trends||Object.keys(data.trends).length===0)return box.replaceChildren(el('div',{class:'tga-empty'},'No trend data available'));
const years=Object.keys(data.trends).sort().reverse().slice(0,5);
if(!years.length)return box.replaceChildren(el('div',{class:'tga-empty'},'No data'));
const allTags=new Set();years.forEach(y=>data.trends[y].forEach(t=>allTags.add(t.category+':'+t.value)));
const topTags=Array.from(allTags).slice(0,5);
const W=1100,H=250,L=150,R=50,T=20,B=30;
const maxV=Math.max(...years.flatMap(y=>data.trends[y].map(t=>t.case_count)),1)*1.1;
const x=i=>L+(W-L-R)/(years.length-1)*i;
const y=v=>T+(H-T-B)*(1-v/maxV);
const svg=svgEl('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Tag trends over time'});
const colors=['#2a78d6','#eb6834','#1baf7a','#eda100','#e87ba4'];
topTags.forEach((tag,ti)=>{const points=years.map((year,i)=>{const t=data.trends[year]?.find(t=>t.category+':'+t.value===tag);return[i,t?.case_count||0]}).filter(p=>p[1]>0);
if(!points.length)return;const path=points.map(([i,v],n)=>`${n?'L':'M'}${x(i)},${y(v)}`).join(' ');
svg.appendChild(svgEl('path',{d:path,fill:'none',stroke:colors[ti%colors.length],'stroke-width':'2','stroke-linejoin':'round'}));});
years.forEach((yr,i)=>svg.appendChild(svgEl('text',{x:x(i),y:H-8,'text-anchor':'middle',class:'tga-axis',style:'font-size:10px'},String(yr))));
const labels=topTags.slice(0,3).map((t,i)=>[t.split(':')[1],colors[i]]);
const legend=el('div',{style:'display:flex;gap:14px;margin:8px 0;font-size:11px;flex-wrap:wrap'});
labels.forEach(([name,color])=>{const s=el('span');const k=el('i',{style:`display:inline-block;width:10px;height:2px;background:${color};margin-right:5px`});s.appendChild(k);s.appendChild(document.createTextNode(name));legend.appendChild(s)});
box.replaceChildren(svg,legend);
}

function renderFrequency(data){const box=$('tgaFrequency');
if(!data.frequency||!data.frequency.length)return box.replaceChildren(el('div',{class:'tga-empty'},'No frequency data'));
const t=el('table');const thead=el('thead');const tr=el('tr');
[['Tag','Cases'],['Mentions']].forEach(h=>tr.appendChild(el('th',{},h[0])));thead.appendChild(tr);t.appendChild(thead);
const body=el('tbody');
data.frequency.slice(0,15).forEach(tag=>{const tr=el('tr');
tr.appendChild(el('td',{style:'max-width:200px;white-space:normal'},`${tag.category} · ${tag.value}`));
tr.appendChild(el('td',{},num(tag.case_count)));
tr.appendChild(el('td',{},num(tag.tag_mentions)));
body.appendChild(tr)});t.appendChild(body);box.replaceChildren(t);
}

function renderJudges(data){const box=$('tgaJudges');
if(!data.judge_tags||Object.keys(data.judge_tags).length===0)return box.replaceChildren(el('div',{class:'tga-empty'},'No judge data'));
const t=el('table');const thead=el('thead');const tr=el('tr');
[['Judge','Tag','Cases']].forEach(h=>tr.appendChild(el('th',{},h[0])));thead.appendChild(tr);t.appendChild(thead);
const body=el('tbody');let count=0;
for(const[judge,tags] of Object.entries(data.judge_tags)){
for(const tag of tags.slice(0,2)){if(count>=10)break;
const tr=el('tr');tr.appendChild(el('td',{},judge.substring(0,30)));
tr.appendChild(el('td',{style:'max-width:150px;white-space:normal'},`${tag.category}·${tag.value}`));
tr.appendChild(el('td',{},num(tag.case_count)));body.appendChild(tr);count++;}
if(count>=10)break;}t.appendChild(body);box.replaceChildren(t);
}

function renderAll(data){
$('tgaStatus').textContent=`Updated: ${new Date().toLocaleTimeString()}`;
renderSummary(data);renderTrends(data);renderFrequency(data);renderJudges(data);
}

async function load(){
$('tgaStatus').textContent='Loading...';
try{
const resp=await fetch('/analytics/tags');
if(!resp.ok)throw new Error(`Failed: ${resp.status}`);
state.data=await resp.json();renderAll(state.data);
}catch(e){$('tgaStatus').textContent=`Error: ${e.message}`}
}

window.tgaLoadAnalytics=function(){if(state.loaded)return;state.loaded=true;load()};
if(new URLSearchParams(location.search).get('tab')==='tag-analytics')window.tgaLoadAnalytics();
})();
</script>
"""

def inject_tag_analytics(html: str) -> str:
	"""Inject tag analytics tab and panel into HTML."""
	if 'fcAnalyticsPanel' not in html:
		return html
	# Insert the tag analytics tab after the FC Analytics tab
	html = html.replace(
		'aria-controls="fcAnalyticsPanel">FC Analytics</button>',
		'aria-controls="fcAnalyticsPanel">FC Analytics</button>' + TAG_ANALYTICS_TAB
	)
	# Insert styles
	if '</style>' in html:
		html = html.replace('</style>', TAG_ANALYTICS_CSS + '</style>')
	# Insert the panel and script after FC Analytics panel
	if '</section>' in html:
		first_section_end = html.find('</section>')
		html = html[:first_section_end + 10] + TAG_ANALYTICS_PANEL + TAG_ANALYTICS_JS + html[first_section_end + 10:]
	return html
