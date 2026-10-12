"""Coming soon: the public preview of what iLit is adding, written to be shown in a demo.

The detailed side (evidence tiers, where each item stands, what it depends on, filters, internal notes)
lives on the Status board at ``/roadmap`` inside the Lab, which only shows when the Experimental switch is on.
This page keeps every area and item reachable but in plain words, with one simple availability label per
item and the demos and the guided tour attached. It reads the same data as the Status board, so the two
cannot drift apart. Nothing here needs AI.
"""

from __future__ import annotations

import html

from .coming_soon_content import PARTS, SECTIONS
from .coming_soon_page import _DEMO_LINKS, _EXTRA_CSS, _about_css, _first_sentence
from .roadmap_page import DEMOS, place_of

# One plain label per item, from where it stands. Concept and paused work never reads as available.
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


def _parts() -> str:
    out = ""
    for key, label, text, slugs in PARTS:
        out += f'<section class="cp-part-block" id="part-{key}"><h2>{_e(label)}</h2><p class="cp-lede">{_e(text)}</p><div class="cp-grid">'
        out += "".join(_card(slug) for slug in slugs if slug in SECTIONS)
        out += "</div></section>"
    return out


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
"""

_JS = """
(function(){
function open(id){var d=document.getElementById(id);if(!d)return;d.open=true;d.scrollIntoView({behavior:'smooth',block:'start'})}
document.querySelectorAll('details[data-lazy]').forEach(function(d){d.addEventListener('toggle',function(){if(!d.open)return;var f=d.querySelector('iframe[data-src]');if(f&&!f.getAttribute('src'))f.setAttribute('src',f.getAttribute('data-src'))})});
document.querySelectorAll('[data-open]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();open(a.getAttribute('data-open'))})});
document.querySelectorAll('[data-go]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();open(a.getAttribute('data-go'))})});
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
        '<p><a class="cp-demo" href="#tour" data-go="tour">&#9654; Take the guided tour</a> '
        '<a class="cp-demo" href="#demos" data-go="demos">Try a demo</a></p>'
        f'<div class="cp-legend small">{legend}</div></header>'
        f"{_parts()}{_demos()}"
        '<p class="cp-foot">Nothing here is a promise. Demos use invented data. Features marked Planned do not exist yet.</p>'
    )
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
        "<title>iLit: coming soon</title>"
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,600&display=swap" rel="stylesheet">'
        f"<style>{_about_css()}{_EXTRA_CSS}{_CSS}</style></head>"
        f'<body><div class="ilit-about"><div class="wrap">{body}</div></div><script>{_JS}</script></body></html>'
    )
