"""Pure generated-page contracts; run with an isolated conftest boundary."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(os.environ.get("TIMING_REPO", Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT))

from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.decision_timing import TIMING_JS
from backend.pages.fc_analytics import FC_ANALYTICS_JS


def test_generated_hooks_and_sibling_panels():
    html = data_explorer_page_html()
    for identity in ("judgeDecisionTiming", "activityDecisionTiming"):
        assert html.count(f'id="{identity}"') == 1
    assert '<div id="judgeProfileContent" class="search-meta">Loading judge profiles...</div>\n<section id="judgeDecisionTiming"' in html
    assert "async function loadJudgeProfile(slug,minister){window.dispatchEvent" in html
    assert "async function loadJudgeProfiles(){window.dispatchEvent" in html
    assert "async function searchJudgeProfiles(event){window.dispatchEvent" in html
    assert "async function jpSelect(slug,keepFilters){if(!slug)return;jpShell();window.dispatchEvent" in html
    assert "if(slug&&slug!==jp.slug)jpSelect(slug);else window.dispatchEvent" in html
    assert html.index("window.addEventListener('judge-decision-timing'") < html.index("async function loadJudgeProfile(")
    assert html.index("window.addEventListener('fc-analytics-timing'") < html.index("async function load(){const mine=++seq")
    assert "MutationObserver" not in TIMING_JS


def test_success_hook_uses_full_captured_query():
    assert "const q=query();syncUrl();" in FC_ANALYTICS_JS
    assert "const f={...state.filters,...extra}" in FC_ANALYTICS_JS
    assert "Object.entries(state.chips)" in FC_ANALYTICS_JS
    assert "p.set('year_from',c.value);p.set('year_to',c.value)" in FC_ANALYTICS_JS
    success = "detail:{status:'loaded',query:q.toString()}"
    assert success in FC_ANALYTICS_JS
    assert FC_ANALYTICS_JS.index("if(mine!==seq)return;") < FC_ANALYTICS_JS.index(success)
    assert FC_ANALYTICS_JS.index("renderAll();") < FC_ANALYTICS_JS.index(success)
    assert "detail:{status:'loading',query:q.toString()}" in FC_ANALYTICS_JS
    assert "detail:{status:'error',query:q.toString()}" in FC_ANALYTICS_JS


def test_accessibility_and_safety_contract():
    html = data_explorer_page_html()
    assert 'aria-label="Judge decision timing" aria-live="polite" hidden' in html
    assert 'aria-label="Activity decision timing" aria-live="polite"' in html
    assert "th.setAttribute('scope','col')" in TIMING_JS
    assert "overflow-x:auto" in html
    assert "@media(max-width:600px)" in html
    assert "innerHTML" not in TIMING_JS
    assert "textContent=String(text)" in TIMING_JS
    assert "n<10" in TIMING_JS
    assert "Independent of profile Minister filters" in TIMING_JS
    assert "not predictions or rankings" in TIMING_JS


@pytest.mark.skipif(not shutil.which("node"), reason="Node unavailable")
def test_javascript_syntax_and_fixture_interactions():
    script = TIMING_JS.removeprefix("\n<script>\n").removesuffix("</script>\n")
    fc_script = FC_ANALYTICS_JS.split("<script>", 1)[1].split("</script>", 1)[0]
    for source in (script, fc_script):
        syntax = subprocess.run(["node", "--check"], input=source, text=True, capture_output=True, check=False)
        assert syntax.returncode == 0, syntax.stderr
    query_function = FC_ANALYTICS_JS.split("function query(", 1)[1].split("\nfunction setFilter", 1)[0]
    query_check = subprocess.run(
        ["node"],
        input=r"""
const assert=require('node:assert/strict');
const state={filters:{city:'Toronto',year_from:'2000',year_to:'2024',
decision_body:'irb',application_type:'direct',representation:'represented',language:'french'},
chips:{year:{value:'2020'},office:{value:'Montreal'},resolution:{value:'jr_granted'},
judge:{value:'judge-a'},counsel:{value:'counsel-a'}}};
""" + "function query(" + query_function + r"""
assert.deepEqual(Object.fromEntries(query()),{city:'Toronto',year_from:'2020',year_to:'2020',
decision_body:'irb',application_type:'direct',representation:'represented',language:'french',
office:'Montreal',resolution:'jr_granted',judge:'judge-a',counsel:'counsel-a'});
""",
        text=True, capture_output=True, timeout=15, check=False,
    )
    assert query_check.returncode == 0, query_check.stderr
    harness = r"""
const assert=require('node:assert/strict');
class Element {
 constructor(tag){this.tag=tag;this.children=[];this.hidden=false;this.textContent=''}
 setAttribute(k,v){this[k]=v}
 appendChild(n){this.children.push(n);return n}
 replaceChildren(...ns){this.children=ns;this.textContent=''}
 get innerHTML(){throw Error('Unsafe HTML access')}
 set innerHTML(v){throw Error('Unsafe HTML assignment')}
}
const boxes={activityDecisionTiming:new Element('section'),judgeDecisionTiming:new Element('section')};
global.document={createElement:t=>new Element(t),getElementById:id=>boxes[id]};
const listeners={};global.window={addEventListener:(name,fn)=>listeners[name]=fn};
const pending=[];
global.fetch=(url,options)=>new Promise((resolve,reject)=>pending.push({url,options,resolve,reject}));
const emit=(name,detail)=>listeners[name]({detail});
const judge=slug=>emit('judge-decision-timing',{slug});
const activity=(status,query)=>emit('fc-analytics-timing',{status,query});
const flush=()=>new Promise(resolve=>setImmediate(resolve));
const ok=(job,data)=>job.resolve({ok:true,json:async()=>data});
const text=el=>[el.textContent,...el.children.map(text)].join(' ');
const stats=(n,median=0)=>({n,median_days:median,p25_days:0,p75_days:0});
const coverage={eligible_records:10,excluded:{missing_dates:0,invalid_dates:0,reversed_dates:0,duplicate_records:0}};
"""
    assertions = r"""
(async()=>{
 judge('old');judge('new/<x>');
 assert.equal(pending[0].options.signal.aborted,true);
 assert.equal(pending[1].url,'/api/judge-profiles/new%2F%3Cx%3E/timing');
 ok(pending[1],{status:'ok',judge:stats(9,99999),baseline:stats(10),coverage:{judge:coverage,baseline:coverage}});
 await flush();
 let current=text(boxes.judgeDecisionTiming);
 assert(!current.includes('99999'));
 assert(current.includes('Withheld'));
 assert(current.includes('Federal Court baseline 10 0 0 0'));
 assert(current.includes('Independent of profile Minister filters'));
 ok(pending[0],{status:'ok',judge:stats(10,77777),baseline:stats(10)});
 await flush();assert.equal(text(boxes.judgeDecisionTiming),current);
 judge(null);assert.equal(boxes.judgeDecisionTiming.hidden,true);
 judge('zero');ok(pending[2],{status:'ok',judge:stats(0,88888),baseline:stats(0)});
 await flush();assert(!text(boxes.judgeDecisionTiming).includes('88888'));
 judge('error');pending[3].resolve({ok:false,status:404});
 await flush();assert(text(boxes.judgeDecisionTiming).includes('Timing unavailable: Request failed (404)'));
 const query='city=A&year_from=2020&year_to=2020&decision_body=irb&application_type=direct&representation=represented&language=french&office=B&resolution=jr_granted&judge=J&counsel=C';
 activity('loading',query);assert.equal(pending.length,4);
 activity('loaded',query);assert.equal(pending[4].url,'/api/fc-activity/timing?'+query);
 activity('loading','year_from=2021');
 assert(pending[4].options.signal.aborted);
 ok(pending[4],{overall:stats(10,12345)});await flush();
 assert(!text(boxes.activityDecisionTiming).includes('12345'));
 activity('loaded','year_from=2021');
 const attack='<img src=x onerror=alert(1)>';
 ok(pending[5],{...coverage,overall:stats(10),by_year:[{year:'secret-small-year',...stats(9,45678)},{year:2021,...stats(10)}],
 hidden_groups:{by_year:{groups:2,samples:4}},ungrouped_year_samples:0,
 by_issue:{status:'unavailable',reason:attack},by_tag:{status:'unavailable',reason:'No verified tags'}});
 await flush();current=text(boxes.activityDecisionTiming);
 assert(!current.includes('secret-small-year'));assert(!current.includes('45678'));
 assert(current.includes('Overall 10 0 0 0'));
 assert(current.includes('Hidden year groups (each n < 10 or suppressed): 3; timed samples in hidden groups: 13'));
 assert(current.includes(attack));assert(current.includes('missing dates 0'));
 activity('loaded','city=Toronto');
 ok(pending[6],{...coverage,overall:stats(10),by_year:[],
  by_issue:[{issue:'safe issue',...stats(10)},{issue:'hidden issue',...stats(9,65432)}],
  by_tag:[{tag:'safe tag',...stats(10)},{tag:'hidden tag',...stats(9,65432)}],
  hidden_groups:{by_year:{groups:0,samples:0},by_issue:{groups:1,samples:2},by_tag:{groups:1,samples:2}}});
 await flush();current=text(boxes.activityDecisionTiming);
 assert(current.includes('safe issue'));assert(current.includes('safe tag'));
 assert(!current.includes('hidden issue'));assert(!current.includes('hidden tag'));assert(!current.includes('65432'));
 assert(current.includes('Neither is canonical Case.issues or V3 tags'));
 activity('error','year_from=2022');
 assert(text(boxes.activityDecisionTiming).includes('dashboard load failed'));
 judge('late');const late=pending[7];judge(null);
 ok(late,{status:'ok',judge:stats(10,98765),baseline:stats(10)});
 await flush();assert(boxes.judgeDecisionTiming.hidden);assert(!text(boxes.judgeDecisionTiming).includes('98765'));
})().catch(error=>{console.error(error);process.exitCode=1});
"""
    run = subprocess.run(
        ["node"], input=harness + script + assertions, text=True, capture_output=True, timeout=15, check=False
    )
    assert run.returncode == 0, run.stderr
