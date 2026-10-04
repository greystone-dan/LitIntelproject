"""Additive timing panels and explicit selection hooks; no database imports.

Listeners are installed in the head before existing deep-link startup calls.
Panels are siblings, preserving the profile's positional table selectors.
"""

TIMING_CSS = """
.decision-timing{margin:12px 16px;padding:12px;border:1px solid var(--border,#d8d5ca);
background:var(--surface,#fff);border-radius:7px;font-size:12px;min-width:0;overflow-wrap:anywhere}
.decision-timing h3{margin:0 0 6px;font-size:14px}
.decision-timing p{margin:6px 0;line-height:1.5}
.decision-timing .timing-scroll{overflow-x:auto;max-width:100%}
.decision-timing table{width:100%;border-collapse:collapse;font-size:12px}
.decision-timing th,.decision-timing td{text-align:left;padding:6px;border-bottom:1px solid #ddd}
@media(max-width:600px){.decision-timing{margin:8px;padding:8px}}
"""

TIMING_JS = r"""
<script>
(function(){
'use strict';
const jobs={activity:{version:0},judge:{version:0}};
const node=(tag,text)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=String(text);return n};
const count=v=>Number.isInteger(v)&&v>=0?v:null;
const shown=v=>v===null||v===undefined?'—':String(v);
const days=v=>typeof v==='number'&&Number.isFinite(v)&&v>=0?String(v):'—';
function panel(kind){return document.getElementById(kind==='activity'?'activityDecisionTiming':'judgeDecisionTiming')}
function clear(kind,message){const box=panel(kind);if(!box)return;box.hidden=false;box.replaceChildren(node('h3','Hearing-to-judgment timing'),node('p',message));box.appendChild(node('p','Descriptive recorded-date coverage only — not predictions or rankings. Same-day judgments are included; missing, invalid and reversed dates are excluded. Statistics require n ≥ 10.'))}
function cancel(kind){const job=jobs[kind];job.version++;job.controller?.abort();return job}
function statsTable(box,rows){
 const wrap=node('div');wrap.className='timing-scroll';
 const table=node('table'),head=node('thead'),hr=node('tr');
 for(const text of ['Cohort','n','Median days','p25 days','p75 days']){const th=node('th',text);th.setAttribute('scope','col');hr.appendChild(th)}head.appendChild(hr);table.appendChild(head);
 const body=node('tbody');
 for(const [label,s] of rows){const n=count(s?.n),suppressed=n===null||n<10||s?.suppressed===true,tr=node('tr');
 for(const value of [label,shown(n),suppressed?'Withheld (n < 10 or suppressed)':days(s?.median_days),suppressed?'—':days(s?.p25_days),suppressed?'—':days(s?.p75_days)])tr.appendChild(node('td',value));
 body.appendChild(tr)}table.appendChild(body);wrap.appendChild(table);box.appendChild(wrap);
}
function coverage(box,label,data){box.appendChild(node('p',`${label}: eligible records ${shown(count(data?.eligible_records))}. Exclusions: missing dates ${shown(count(data?.excluded?.missing_dates))}; invalid dates ${shown(count(data?.excluded?.invalid_dates))}; reversed dates ${shown(count(data?.excluded?.reversed_dates))}; duplicate records ${shown(count(data?.excluded?.duplicate_records))}.`))}
function renderActivity(box,data){
 box.appendChild(node('p','Staged FC Activity classifications only. Years are filing years. All active dashboard filters apply; no canonical case join.'));
 const yearly=Array.isArray(data.by_year)?data.by_year:[],visible=yearly.filter(s=>count(s.n)!==null&&s.n>=10&&!s.suppressed);
 statsTable(box,[['Overall',data.overall],...visible.map(s=>[String(s.year),s])]);
 const omitted=yearly.filter(s=>!visible.includes(s)),hidden=data.hidden_groups?.by_year;
 box.appendChild(node('p',`Hidden year groups (each n < 10 or suppressed): ${shown(count(hidden?.groups)===null?null:hidden.groups+omitted.length)}; timed samples in hidden groups: ${shown(count(hidden?.samples)===null?null:hidden.samples+omitted.reduce((n,s)=>n+(count(s.n)??0),0))}. Ungrouped year samples: ${shown(count(data.ungrouped_year_samples))}.`));
 coverage(box,'Activity coverage',data);
 box.appendChild(node('p','Issue groups are stored challenged-decision subjects; tag groups are stored challenge categories. Neither is canonical Case.issues or V3 tags. Groups can overlap; each file counts once per label.'));
 for(const [key,label] of [['by_issue','By issue'],['by_tag','By tag']]){
 const group=data[key];
 if(Array.isArray(group)){
  box.appendChild(node('h4',label));
  const field=key==='by_issue'?'issue':'tag',visible=group.filter(s=>count(s.n)!==null&&s.n>=10&&!s.suppressed);
  if(visible.length)statsTable(box,visible.map(s=>[s[field],s]));else box.appendChild(node('p','No groups meet n ≥ 10.'));
  const omitted=group.filter(s=>!visible.includes(s)),hidden=data.hidden_groups?.[key];
  box.appendChild(node('p',`Hidden ${label.toLowerCase()} groups (each n < 10 or suppressed): ${shown(count(hidden?.groups)===null?null:hidden.groups+omitted.length)}; timed group memberships hidden: ${shown(count(hidden?.samples)===null?null:hidden.samples+omitted.reduce((n,s)=>n+(count(s.n)??0),0))}.`));
 }else box.appendChild(node('p',`${label}: ${group?.status==='unavailable'?'unavailable':'not displayed'}. ${typeof group?.reason==='string'?group.reason:'No verified grouping available.'}`));
 }
}
function renderJudge(box,data){
 box.appendChild(node('p','Canonical Federal Court decisions only. Independent of profile Minister filters. Federal Court baseline includes this judge’s decisions.'));
 statsTable(box,[['Selected judge',data.judge],['Federal Court baseline',data.baseline]]);
 coverage(box,'Judge coverage',data.coverage?.judge);coverage(box,'Baseline coverage',data.coverage?.baseline);
}
async function request(kind,url){
 const job=cancel(kind),version=job.version;job.controller=new AbortController();
 clear(kind,'Loading timing…');
 try{const response=await fetch(url,{signal:job.controller.signal});if(!response.ok)throw new Error(`Request failed (${response.status})`);
 const data=await response.json();if(version!==job.version)return;
 if(data.status&&data.status!=='ok')throw new Error('Timing cohort unavailable');
 clear(kind,'Recorded hearing-to-judgment days');const box=panel(kind);if(!box)return;
 (kind==='activity'?renderActivity:renderJudge)(box,data);
 }catch(error){if(version!==job.version)return;clear(kind,`Timing unavailable: ${error.message||String(error)}`)}
}
window.addEventListener('fc-analytics-timing',event=>{
 const detail=event.detail||{};
 if(detail.status==='loading'){cancel('activity');clear('activity','Waiting for the updated dashboard…')}
 else if(detail.status==='error'){cancel('activity');clear('activity','Timing unavailable: dashboard load failed.')}
 else if(detail.status==='loaded')request('activity','/api/fc-activity/timing?'+new URLSearchParams(detail.query||'').toString());
});
window.addEventListener('judge-decision-timing',event=>{
 const slug=event.detail?.slug;
 if(!slug){cancel('judge');const box=panel('judge');if(box){box.replaceChildren();box.hidden=true}return}
 request('judge','/api/judge-profiles/'+encodeURIComponent(slug)+'/timing');
});
})();
</script>
"""


def inject_decision_timing(html: str) -> str:
    """Hook active snapshot selection plus compatibility profile loaders.

    Stable function-entry anchors avoid MutationObserver and wrapping the
    already multiply-wrapped profile loader. No existing profile tables change.
    """
    anchors = {
        "async function loadJudgeProfile(slug,minister){":
            "window.dispatchEvent(new CustomEvent('judge-decision-timing',{detail:{slug}}));",
        "async function loadJudgeProfiles(){":
            "window.dispatchEvent(new CustomEvent('judge-decision-timing',{detail:{slug:null}}));",
        "async function searchJudgeProfiles(event){":
            "window.dispatchEvent(new CustomEvent('judge-decision-timing',{detail:{slug:null}}));",
        "async function jpSelect(slug,keepFilters){if(!slug)return;jpShell();":
            "window.dispatchEvent(new CustomEvent('judge-decision-timing',{detail:{slug}}));",
    }
    for anchor, hook in anchors.items():
        html = html.replace(anchor, anchor + hook, 1)
    # Re-entering the snapshot with its already-selected slug does not call
    # jpSelect; restore timing after the compatibility list loader reset.
    active_init = "if(slug&&slug!==jp.slug)jpSelect(slug)}"
    html = html.replace(active_init, "if(slug&&slug!==jp.slug)jpSelect(slug);else window.dispatchEvent(new CustomEvent('judge-decision-timing',{detail:{slug:slug||null}}))}", 1)
    profile = '<div id="judgeProfileContent" class="search-meta">Loading judge profiles...</div>'
    html = html.replace(profile, profile + '\n<section id="judgeDecisionTiming" class="decision-timing" aria-label="Judge decision timing" aria-live="polite" hidden></section>', 1)
    html = html.replace('<div class="fcx-kpis" id="fcxKpis">', '<section id="activityDecisionTiming" class="decision-timing" aria-label="Activity decision timing" aria-live="polite"></section>\n<div class="fcx-kpis" id="fcxKpis">', 1)
    return html.replace("</head>", f"<style>{TIMING_CSS}</style>\n{TIMING_JS}\n</head>", 1)
