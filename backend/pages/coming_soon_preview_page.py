"""Coming soon: the public preview of what iLit is adding, written to be shown in a demo.

The detailed side (evidence tiers, where each item stands, what it depends on, filters, internal notes)
lives on the Status board at ``/roadmap`` inside the Lab, which only shows when the Experimental switch is on.
This page keeps every area and item reachable but in plain words, with one simple availability label per
item and the demos and the guided tour attached. It reads the same data as the Status board, so the two
cannot drift apart. Nothing here needs AI.
"""

from __future__ import annotations

import html
import json
from functools import lru_cache
from pathlib import Path

from .coming_soon_content import PARTS, SECTIONS
from .coming_soon_page import _DEMO_LINKS, _EXTRA_CSS, _about_css, _first_sentence
from .roadmap_page import DEMOS, place_of

# One plain label per item, from where it stands. Concept and paused work never reads as available.
EXAMPLES_FILE = Path(__file__).with_name("coming_soon_examples.json")


@lru_cache(maxsize=1)
def examples() -> dict:
    """The one place the example data and test numbers live. Edit the JSON file; no code change is needed."""
    return json.loads(EXAMPLES_FILE.read_text(encoding="utf-8"))


AVAILABILITY = {
    "live": ("Available now", "now"),
    "experimental": ("Being checked", "check"),
    "files": ("Being prepared", "check"),
    "planned": ("Planned", "plan"),
    "paused": ("Later", "plan"),
}


def _e(value: str) -> str:
    return html.escape(value, quote=False)


def _chip(place: str) -> str:
    label, kind = AVAILABILITY[place]
    return f'<span class="cp-chip cp-{kind}">{label}</span>'


def _area_chip(places: list[str]) -> str:
    live = sum(1 for p in places if p == "live")
    if live == len(places):
        return '<span class="cp-chip cp-now">Available now</span>'
    if live:
        return f'<span class="cp-chip cp-part">{live} of {len(places)} available now</span>'
    if any(p in ("experimental", "files") for p in places):
        return '<span class="cp-chip cp-check">Being checked</span>'
    return '<span class="cp-chip cp-plan">Planned</span>'


def _card(slug: str) -> str:
    area = SECTIONS[slug]
    entries = area["items"]
    places = [place_of(entry[0]) for entry in entries]
    # Up to three items are shown on the card with what you could do; the rest sit under "All items".
    shown = "".join(
        f'<li><span class="cp-row"><span class="cp-it">{_e(entry[1])}</span>{_chip(place_of(entry[0]))}</span>'
        f'<span class="cp-what">{_e(entry[4])}</span></li>'
        for entry in entries[:3]
    )
    rest = "".join(
        f'<li><span class="cp-row"><span class="cp-it">{_e(entry[1])}</span>{_chip(place_of(entry[0]))}</span>'
        f'<span class="cp-what">{_e(_first_sentence(entry[3][0]))}</span></li>'
        for entry in entries[3:]
    )
    more = f'<details><summary>{len(entries) - 3} more in this area</summary><ul class="cp-list">{rest}</ul></details>' if rest else ""
    demos = "".join(
        f'<a class="cp-demo" href="#demo-{key}" data-open="demo-{key}">&#9654; {_e(label)}</a>'
        for key, label, _what in _DEMO_LINKS.get(slug, [])
    )
    return (
        f'<article class="cp-card" id="{slug}"><div class="cp-head"><h3>{_e(area["label"])}</h3>{_area_chip(places)}</div>'
        f'<p class="cp-sum">{_e(area["summary"])}</p>'
        f'<ul class="cp-list">{shown}</ul>{more}'
        f'{f"<div class=cp-demos>{demos}</div>" if demos else ""}</article>'
    )


def _layers() -> str:
    data = examples()
    intro = data["layers_intro"]
    cases = data["cases"]
    switch = "".join(
        f'<button type="button" data-case="{i}" aria-pressed="{"true" if i == 0 else "false"}">{_e(c["cite"])} <span>{_e(c["tag"])}</span></button>'
        for i, c in enumerate(cases)
    )
    live = "".join(
        f'<a class="cp-demo" href="/data-explorer?tab=search&amp;group=research&amp;q={_e(item["cite"].replace(" ", "%20"))}" target="_top">{_e(item["label"])} &rarr;</a>'
        for item in data.get("live_examples", [])
    )
    return (
        '<section class="cp-part-block" id="layers"><h2>' + _e(intro["title"]) + '</h2>'
        f'<p class="cp-lede">{_e(intro["text"])}</p>'
        f'<div class="cp-switch" role="group" aria-label="Choose an example decision">{switch}</div>'
        '<div class="rd" id="rd"></div>'
        f'<p class="cp-note">{_e(intro["limits"])}</p>'
        f'<div class="cp-demos">{live}</div></section>'
    )


def _pass_card(p: dict) -> str:
    label, kind = AVAILABILITY[{"now": "live", "check": "experimental", "plan": "planned"}[p["status"]]]
    number = (
        f'<div class="cp-big">{_e(p["number"])}</div><div class="cp-biglabel">{_e(p["number_label"])}</div>' if p.get("number") else
        '<div class="cp-big cp-none">Not measured yet</div>'
    )
    def facts(pairs):
        return "".join(f'<div><dt>{name}</dt><dd>{_e(p[key])}</dd></div>' for name, key in pairs if p.get(key))

    more = facts((("Written / graded by", "grader"), ("Where it is", "where")))
    rows = facts((("Tested on", "sample"), ("Limits", "caveat")))
    details = f'<details><summary>Who graded it, and where it is</summary><dl class="cp-facts">{more}</dl></details>' if more else ""
    return (
        f'<article class="cp-card cp-pass" id="pass-{_e(p["key"])}"><div class="cp-head"><h3>{_e(p["title"])}</h3><span class="cp-chip cp-{kind}">{label}</span></div>'
        f'<p class="cp-sum">{_e(p["what"])}</p>{number}<dl class="cp-facts">{rows}</dl>{details}</article>'
    )


def _evidence() -> str:
    data = examples()
    cards = "".join(_pass_card(p) for p in data["passes"])
    limits = "".join(f"<li>{_e(line)}</li>" for line in data["limits"])
    return (
        '<section class="cp-part-block" id="evidence"><h2>What has been tested, and how well</h2>'
        '<p class="cp-lede">Each part of the reading layer, with the number it earned, what it was tested on, who graded it and where it falls short. A part with no number says so.</p>'
        f'<div class="cp-grid">{cards}</div>'
        f'<aside class="cp-say"><h3>{_e(data["limits_title"])}</h3><ul>{limits}</ul></aside></section>'
    )


def _tiers() -> str:
    passes = examples()["passes"]
    live = sum(1 for p in passes if p["status"] == "now" and p.get("number"))
    tested = sum(1 for p in passes if p["status"] != "now" and p.get("number"))
    none = sum(1 for p in passes if not p.get("number"))
    tiles = (
        (live, "cp-now", "Live and measured", "On the site today, with a test number."),
        (tested, "cp-check", "Tested, not live", "Built and scored on a small sample, still being checked."),
        (none, "cp-plan", "Not measured yet", "Built or planned, with no accuracy number."),
    )
    return '<div class="cp-tiers" aria-label="Evidence at a glance">' + "".join(
        f'<a class="cp-tier cp-t-{kind[3:]}" href="#evidence"><b>{n}</b><span><strong>{_e(name)}</strong>{_e(text)}</span></a>'
        for n, kind, name, text in tiles
    ) + "</div>"


def _helps() -> str:
    data = examples()
    helps = data["helps"]
    passes = {p["key"]: p for p in data["passes"]}
    rows = ""
    for item in helps["items"]:
        p = passes[item["pass"]]
        label, kind = AVAILABILITY[{"now": "live", "check": "experimental", "plan": "planned"}[p["status"]]]
        number = f' <b>{_e(p["number"])}</b>' if p.get("number") else " not measured yet"
        rows += (
            f'<li><span class="cp-who">{_e(item["who"])}</span><strong>{_e(item["job"])}</strong><span class="cp-what">{_e(item["how"])}</span>'
            f'<a class="cp-ev" href="#pass-{_e(p["key"])}"><span class="cp-chip cp-{kind}">{label}</span>{number} &middot; see the evidence</a></li>'
        )
    return f'<section class="cp-part-block" id="helps"><h2>{_e(helps["title"])}</h2><p class="cp-lede">{_e(helps["text"])}</p><ul class="cp-helps">{rows}</ul></section>'


def _parts() -> str:
    out = ""
    for key, label, text, slugs in PARTS:
        out += f'<section class="cp-part-block" id="part-{key}"><h2>{_e(label)}</h2><p class="cp-lede">{_e(text)}</p><div class="cp-grid">'
        out += "".join(_card(slug) for slug in slugs if slug in SECTIONS)
        out += "</div></section>"
    return (
        '<details class="cp-roadmap" id="roadmap-all" open><summary><h2>The wider roadmap</h2>'
        '<span class="cp-lede">More data, new features and what an agency deployment would need. Tap to open or close.</span></summary>'
        + out + "</details>"
    )


def _demos() -> str:
    tiles = "".join(
        f'<details class="cp-demo-tile" id="demo-{key}" data-lazy="1"><summary><strong>{_e(name)}</strong>'
        f'<span class="cp-tag">{_e(chip)}</span><span class="cp-what">{_e(what)}</span></summary>'
        f'<iframe class="cp-frame" title="{_e(name)} demo" data-src="/coming-soon-demo#{key}" loading="lazy"></iframe></details>'
        for key, name, chip, what in DEMOS
    )
    return (
        '<section class="cp-part-block" id="demos"><h2>Try it</h2>'
        '<p class="cp-lede">Click-through demos on fixed, invented data, drawn in the site’s own look. They run in your browser and touch no real case, account or AI.</p>'
        f'<div class="cp-demo-grid">{tiles}</div>'
        '<details class="cp-demo-tile cp-tour" id="tour" data-lazy="1"><summary><strong>Guided tour of what is coming</strong>'
        '<span class="cp-tag">Mock-ups</span><span class="cp-what">A short paced tour: better data, profiles and teams, and an optional local AI layer.</span></summary>'
        '<iframe class="cp-frame cp-tall" title="Guided tour" data-src="/roadmap/tour" loading="lazy"></iframe></details></section>'
    )


_CSS = """
.cp-hero{padding:6px 0 18px}.cp-hero h1{margin:4px 0 8px}.cp-hero .cp-lede{max-width:70ch}
.cp-legend{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 0}
.cp-part-block{margin:30px 0 0}.cp-part-block h2{margin:0 0 4px}.cp-lede{color:var(--muted,#5f6368);margin:0 0 14px;max-width:75ch}
.cp-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:14px}
.cp-card{background:#fffdf9;border:1px solid var(--line,#ddd6c8);border-radius:10px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}
.cp-card h3{margin:0;font-size:18px}.cp-card p{margin:0;line-height:1.5;font-size:14px}.cp-sum{color:#5f6368}.cp-row{display:flex;align-items:center;justify-content:space-between;gap:8px}
.cp-head{display:flex;align-items:flex-start;justify-content:space-between;gap:10px}
.cp-chip{display:inline-block;white-space:nowrap;padding:2px 9px;border-radius:999px;font-size:11px;font-weight:600;border:1px solid transparent}
.cp-now{background:#e1f2ee;color:#0b5d52;border-color:#a9d8cf}.cp-part{background:#e7f0f8;color:#1d4f7a;border-color:#b7d0e6}
.cp-check{background:#fbf1d6;color:#7a5a00;border-color:#ebd593}.cp-plan{background:#eeeeea;color:#555;border-color:#d4d2c9}
.cp-card details{margin-top:4px}.cp-card .cp-demos{margin-top:auto;padding-top:6px}.cp-card summary{cursor:pointer;font-size:13px;font-weight:600;color:var(--teal,#0b6e63)}
.cp-list{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:10px}.cp-list li{display:grid;gap:3px;padding-top:8px;border-top:1px solid #eee8da}
.cp-it{font-weight:600;font-size:14px}.cp-what{display:block;font-size:13px;color:#5f6368;line-height:1.45}
.cp-demos{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}.cp-demo{font-size:13px;font-weight:600;color:var(--teal,#0b6e63);text-decoration:none;border:1px solid #a9d8cf;border-radius:6px;padding:5px 10px;background:#f2faf8}
.cp-demo:hover{background:#e1f2ee}
.cp-demo-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:14px;align-items:start}
.cp-demo-tile{background:#fffdf9;border:1px solid var(--line,#ddd6c8);border-radius:10px;padding:14px 16px}.cp-demo-tile summary{cursor:pointer;display:grid;gap:4px;list-style:none}
.cp-demo-tile summary::-webkit-details-marker{display:none}.cp-demo-tile[open]{grid-column:1/-1}
.cp-tag{justify-self:start;font-size:11px;font-weight:600;background:#eeeeea;border-radius:4px;padding:1px 7px;color:#555}
.cp-frame{width:100%;height:640px;border:1px solid #ddd6c8;border-radius:8px;margin-top:12px;background:#fff}.cp-frame.cp-tall{height:760px}
.cp-tour{margin-top:14px}.cp-foot{margin:34px 0 8px;font-size:13px;color:#5f6368}
@media(max-width:600px){.cp-frame{height:520px}.cp-card{padding:14px}}
.cp-tiers{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px;margin:16px 0 0}
.cp-tier{display:flex;gap:12px;align-items:center;text-decoration:none;color:inherit;border:1px solid var(--line,#ddd6c8);border-radius:10px;padding:10px 14px;background:#fffdf9}
.cp-tier b{font-size:30px;font-family:Newsreader,Georgia,serif;line-height:1}.cp-tier span{font-size:12px;color:#5f6368;line-height:1.35}.cp-tier strong{display:block;font-size:13px;color:#222}
.cp-t-now{border-left:4px solid #0b5d52}.cp-t-check{border-left:4px solid #b88a00}.cp-t-plan{border-left:4px solid #999}
.cp-helps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:14px}
.cp-helps li{background:#fffdf9;border:1px solid var(--line,#ddd6c8);border-radius:10px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}
.cp-who{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;color:#5f6368}.cp-ev{margin-top:auto;font-size:13px;text-decoration:none;color:var(--teal,#0b6e63)}.cp-ev .cp-chip{margin-right:6px}
.cp-roadmap>summary{cursor:pointer;list-style:none;margin-top:30px}.cp-roadmap>summary::-webkit-details-marker{display:none}.cp-roadmap>summary h2{margin:0 0 4px}.cp-roadmap>summary h2::after{content:" \25BE";font-size:16px;color:#5f6368}.cp-roadmap:not([open])>summary h2::after{content:" \25B8"}
.cp-nav{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.cp-switch{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 12px}.cp-switch button{font:500 13px inherit;font-family:inherit;border:1px solid var(--line,#ddd6c8);background:#fffdf9;border-radius:999px;padding:6px 14px;cursor:pointer}
.cp-switch button span{color:#5f6368;margin-left:4px}.cp-switch button[aria-pressed=true]{background:#315d8d;border-color:#315d8d;color:#fff}.cp-switch button[aria-pressed=true] span{color:#e7eef6}
.cp-note{font-size:13px;color:#5f6368;margin:12px 0 8px;padding:9px 12px;border:1px dashed #d8d5ca;border-radius:6px;background:#fffdf9}
.rd{border:1px solid #d8d5ca;border-radius:10px;background:#fffef9;overflow:hidden}
.rd-tb{display:flex;flex-wrap:wrap;align-items:center;gap:8px;padding:10px 14px;background:#f8f6ef;border-bottom:1px solid #d8d5ca}.rd-tb b{font:600 16px Newsreader,Georgia,serif;flex:1;min-width:120px}
.rd-chip{font:600 12.5px inherit;font-family:inherit;border:1px solid #d8d5ca;background:#fffef9;border-radius:999px;padding:5px 12px;cursor:pointer;color:#202522}.rd-chip.on{background:#176c68;border-color:#176c68;color:#fff}
.rd-chip i{font-style:normal;margin-left:6px;background:rgba(0,0,0,.1);border-radius:999px;padding:0 6px}
.rd-strip{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:9px 14px;background:#edf5f3;border-bottom:1px solid #d8d5ca;font-size:13.5px}
.rd-strip button{font:600 12.5px inherit;font-family:inherit;color:#176c68;background:none;border:0;cursor:pointer;white-space:nowrap}
.rd-glance{padding:14px 16px;background:#edf5f3;border-bottom:1px solid #d8d5ca;border-left:4px solid #176c68}
.rd-glance h4{margin:0 0 6px;font:600 17px Newsreader,Georgia,serif}.rd-gg{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 22px;font-size:13.5px;margin:0}
.rd-gg dt{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#176c68}.rd-gg dd{margin:2px 0 0}.rd-gg .full{grid-column:1/-1}.rd-gg ul{margin:2px 0 0;padding-left:18px}
.rd-main{display:grid;grid-template-columns:minmax(0,1fr);}.rd-main.has-panel{grid-template-columns:minmax(0,1fr) 320px}
.rd-body{max-height:540px;overflow:auto;padding:10px 14px;scroll-behavior:smooth}
.rd-p{display:grid;grid-template-columns:34px 1fr;gap:8px;padding:9px 8px;border-radius:6px;border:1px solid transparent}.rd-p.hl{background:#f8f0dc;border-color:#8a6418}
.rd-pn{font-size:12px;color:#5f6863;padding-top:3px}.rd-pt{font:16px/1.6 Newsreader,Georgia,serif}
.rd-mk{display:inline-block;margin:4px 6px 0 0;font:600 11.5px inherit;font-family:inherit;color:#176c68;background:#edf5f3;border:1px solid #bfdcd7;border-radius:999px;padding:1px 9px;cursor:pointer}
.rd-nl{display:inline-block;margin-top:4px;font:12px inherit;font-family:inherit;color:#315d8d;background:none;border:0;cursor:pointer;text-decoration:underline;padding:0}
.rd-note{display:block;margin-top:6px;padding:5px 10px;background:#e7eef6;border-radius:4px;font-size:13px;line-height:1.45}.rd-note.h{display:none}.rd-note b{font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:#315d8d;margin-right:6px}
.rd-panel{border-left:1px solid #d8d5ca;background:#f8f6ef;padding:12px 14px;max-height:540px;overflow:auto}.rd-panel h4{margin:0 0 8px;font:600 16px Newsreader,Georgia,serif}
.rd-iss{border:1px solid #d8d5ca;border-radius:6px;background:#fffef9;padding:10px 12px;margin-bottom:10px}.rd-iss q{display:block;quotes:none;font:600 14px/1.4 inherit;font-family:inherit}
.rd-res{display:inline-block;margin-top:6px;font-size:11.5px;font-weight:700;padding:1px 9px;border-radius:999px}.rd-res.ok{background:#edf5f3;color:#176c68}.rd-res.no{background:#f7e8e3;color:#a4412b}.rd-res.nd{background:#f8f0dc;color:#8a6418}
.rd-iss blockquote{margin:6px 0 0;padding-left:10px;border-left:3px solid #d8d5ca;font:14px/1.5 Newsreader,Georgia,serif;color:#5f6863}
.rd-iss button{margin-top:6px;font:600 12.5px inherit;font-family:inherit;color:#315d8d;background:none;border:0;padding:0;cursor:pointer;text-decoration:underline}
.cp-pass .cp-big{font:600 34px/1.1 Newsreader,Georgia,serif;color:#176c68;margin-top:4px}.cp-pass .cp-big.cp-none{font-size:20px;color:#7a5a00}.cp-biglabel{font-size:13px;color:#202522}
.cp-facts{margin:6px 0 0;display:grid;gap:8px}.cp-facts dt{font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#5f6368}.cp-facts dd{margin:1px 0 0;font-size:13px;line-height:1.45}
.cp-say{margin-top:18px;padding:14px 18px;border:1px solid #e3d28a;border-left:4px solid #c9a100;border-radius:6px;background:#fdf8e1}.cp-say h3{margin:0 0 6px;font-size:16px}.cp-say ul{margin:0;padding-left:18px;font-size:14px;line-height:1.55}
@media(max-width:900px){.rd-main.has-panel{grid-template-columns:1fr}.rd-panel{border-left:0;border-top:1px solid #d8d5ca;order:-1;max-height:340px}.rd-gg{grid-template-columns:1fr}.rd-body{max-height:480px}}

"""

_JS = r"""
(function(){
function open(id){var d=document.getElementById(id);if(!d)return;d.open=true;d.scrollIntoView({behavior:'smooth',block:'start'})}
document.querySelectorAll('details[data-lazy]').forEach(function(d){d.addEventListener('toggle',function(){if(!d.open)return;var f=d.querySelector('iframe[data-src]');if(f&&!f.getAttribute('src'))f.setAttribute('src',f.getAttribute('data-src'))})});
document.querySelectorAll('[data-open]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();open(a.getAttribute('data-open'))})});
if(window.innerWidth<=600){var rm=document.getElementById('roadmap-all');if(rm)rm.open=false}
document.querySelectorAll('[data-go]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();var id=a.getAttribute('data-go'),t=document.getElementById(id);if(t&&t.tagName==='DETAILS')t.open=true;if(t)t.scrollIntoView({behavior:'smooth',block:'start'})})});
var dataEl=document.getElementById('cp-data'),root=document.getElementById('rd');
if(!dataEl||!root)return;
var D=JSON.parse(dataEl.textContent).cases,cur=0,S={open:false,issues:false,notes:false,one:{}};
var esc=function(t){return String(t).replace(/[&<>"]/g,function(c){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'})[c]})};
function glance(d){return '<div class="rd-glance"><h4>Case at a glance</h4><dl class="rd-gg">'
 +'<div class="full"><dt>About</dt><dd>'+esc(d.subject)+'</dd></div>'
 +'<div><dt>Parties</dt><dd>'+esc(d.applicant)+' v. '+esc(d.respondent)+'</dd></div>'
 +'<div><dt>Path</dt><dd>'+esc(d.level)+'</dd></div>'
 +'<div class="full"><dt>This decision</dt><dd>'+esc(d.outcome)+'</dd></div>'
 +'<div class="full"><dt>Main arguments</dt><dd><ul>'+d.args.map(function(a){return '<li><i>'+(a.side==='applicant'?'Applicant':'Respondent')+':</i> '+esc(a.text)+'</li>'}).join('')+'</ul></dd></div></dl>'
 +'<button type="button" class="rd-chip" data-act="open" style="margin-top:10px">Collapse summary</button></div>'}
function issues(d){return '<h4>Issues decided</h4>'+d.issues.map(function(i,k){return '<div class="rd-iss"><q>'+(k+1)+'. '+esc(i.q)+'</q><span class="rd-res '+i.cls+'">'+esc(i.how)+'</span><blockquote>&ldquo;'+esc(i.quote)+'&rdquo; <small>['+i.para+']</small></blockquote><button type="button" data-jump="'+i.para+'">Jump to paragraph '+i.para+'</button></div>'}).join('')+'<p style="font-size:12.5px;color:#5f6863;margin:0">Checked by a model, not a lawyer.</p>'}
function draw(){
 var d=D[cur],mk={};d.issues.forEach(function(i,k){(mk[i.para]=mk[i.para]||[]).push(k+1)});
 var paras=d.notes.map(function(n){var show=S.notes||S.one[n[0]];
  var tags=(mk[n[0]]||[]).map(function(k){return '<button type="button" class="rd-mk" data-issue="'+k+'">&#9679; Issue '+k+' answered here</button>'}).join('');
  var nl=S.notes?'':'<button type="button" class="rd-nl" data-note="'+n[0]+'">'+(S.one[n[0]]?'hide note':'note')+'</button>';
  return '<div class="rd-p" id="rdp'+n[0]+'"><div class="rd-pn">['+n[0]+']</div><div><div class="rd-pt">'+esc(n[2])+'</div>'+tags+nl+'<span class="rd-note'+(show?'':' h')+'"><b>Note</b>'+esc(n[1])+'</span></div></div>'}).join('');
 var h='<div class="rd-tb"><b>'+esc(d.cite)+'</b><button type="button" class="rd-chip'+(S.issues?' on':'')+'" data-act="issues">Issues decided<i>'+d.issues.length+'</i></button><button type="button" class="rd-chip'+(S.notes?' on':'')+'" data-act="notes">Notes: '+(S.notes?'On':'Off')+'</button></div>';
 h+=S.open?glance(d):'<div class="rd-strip"><span><b>'+esc(d.outcome.split(';')[0].replace(/^./,function(c){return c.toUpperCase()}))+'.</b> '+esc(d.tag)+'.</span><button type="button" data-act="open">At a glance &#9662;</button></div>';
 h+='<div class="rd-main'+(S.issues?' has-panel':'')+'"><div class="rd-body" id="rdb">'+paras+'</div>'+(S.issues?'<div class="rd-panel">'+issues(d)+'</div>':'')+'</div>';
 root.innerHTML=h}
root.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var jump=b.dataset.jump;
 if(b.dataset.act){var a=b.dataset.act;S[a]=!S[a];if(a==='notes')S.one={}}
 else if(b.dataset.note)S.one[b.dataset.note]=!S.one[b.dataset.note];
 else if(b.dataset.issue)S.issues=true;
 draw();
 if(jump){var t=document.getElementById('rdp'+jump),box=document.getElementById('rdb');if(t){t.classList.add('hl');if(box)box.scrollTop=t.offsetTop-box.offsetTop-8}}});
document.querySelectorAll('.cp-switch button').forEach(function(b){b.addEventListener('click',function(){cur=+b.dataset.case;S.one={};document.querySelectorAll('.cp-switch button').forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});draw()})});
draw();
})();
"""


def render() -> str:
    legend = "".join(
        f'<span>{chip}</span>'
        for chip in (
            '<span class="cp-chip cp-now">Available now</span> works on the site today',
            '<span class="cp-chip cp-check">Being checked</span> built, still being tested',
            '<span class="cp-chip cp-plan">Planned</span> decided, not built yet',
        )
    )
    body = (
        '<header class="cp-hero"><p class="eyebrow">Coming soon</p><h1>What iLit is adding next</h1>'
        '<p class="cp-lede">iLit today is a library of Canadian immigration decisions with a formatted reader, search, citations and links to the law. '
        'This page previews what is being added, in plain words. Each area says honestly how far it has got, and you can click through demos of the screens.</p>'
        '<div class="cp-nav"><a class="cp-demo" href="#layers" data-go="layers">&#9654; See it on a decision</a> '
        '<a class="cp-demo" href="#helps" data-go="helps">Where it helps</a> '
        '<a class="cp-demo" href="#evidence" data-go="evidence">How well it works</a> '
        '<a class="cp-demo" href="#tour" data-go="tour">Guided tour</a> '
        '<a class="cp-demo" href="#demos" data-go="demos">Try a demo</a></div>'
        f'<div class="cp-legend small">{legend}</div>{_tiers()}</header>'
        f"{_layers()}{_helps()}{_evidence()}{_parts()}{_demos()}"
        '<p class="cp-foot">Nothing here is a promise. Demos use invented data. Features marked Planned do not exist yet.</p>'
    )
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
        "<title>iLit: coming soon</title>"
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,600&display=swap" rel="stylesheet">'
        f"<style>{_about_css()}{_EXTRA_CSS}{_CSS}</style></head>"
        f'<body><div class="ilit-about"><div class="wrap">{body}</div></div>'
        f'<script type="application/json" id="cp-data">{json.dumps({"cases": examples()["cases"]}, ensure_ascii=False).replace("</", "<\\/")}</script><script>{_JS}</script></body></html>'
    )
