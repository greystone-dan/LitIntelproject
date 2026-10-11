"""The Roadmap: one long, expandable page that replaces the separate Coming soon pages.

It carries everything that used to be spread over the Coming soon areas, the Future features
page, the long argument-breakdown page, the demos and the guided preview. Every item shows
one evidence tier:

* Live: something real of the item is on the default site today.
* Tested: a measured result is stated on the item, with what was tested.
* Untested: nothing of it is on the default site, it is built but off the main menu, or it has
  not been measured.

Served at ``/roadmap`` inside the same frame the Coming soon pages used. Nothing here needs AI.
"""

from __future__ import annotations

import html
import re
from functools import lru_cache
from pathlib import Path

from .coming_soon_content import PARTS, SECTIONS
from .coming_soon_page import STATUSES, STATUS_MEANING, _EXTRA_CSS, _RULE, _about_css, _first_sentence

HERE = Path(__file__).resolve().parent

TIERS = {
	"live": ("Live", "Something real of this item is on the site today. The item says exactly what, and what is still missing."),
	"tested": ("Tested", "A measured result is stated on the item, with what was tested and who graded it. No item is called Tested without one."),
	"untested": ("Untested", "Nothing of it is on the default site, it is built but sits behind the Experimental switch or has not been applied, or it has not been measured."),
}

# One tier per roadmap item. Everything not listed here is Untested.
LIVE_ITEMS = {
	"citation-extraction", "statute-references", "case-types", "outcome-coding", "judges", "parties",
	"more-cases", "more-tags", "fc-record", "fc-analytics", "fc-follow", "fc-deadlines",
	"argument-identification", "deidentify", "citation-treatment", "discussion-units",
	"decision-maker-insights", "data-safety", "export",
}
TESTED_ITEMS = {"whose-position"}


def tier_of(slug: str) -> str:
	if slug in TESTED_ITEMS:
		return "tested"
	return "live" if slug in LIVE_ITEMS else "untested"


# Future-features item id -> the roadmap item it describes, so both carry the same tier.
FF_TO_ITEM = {
	"internal-docs": "internal-documents", "repositories": "agency-repositories", "live-analysis": "argument-identification",
	"data-safety": "data-safety", "id-iad": "id-iad", "refined-citations": "citation-extraction", "neighbourhoods": "neighbourhoods",
	"fingerprints": "fingerprints", "units": "discussion-units", "alerts": "alerts", "workbench": "teams",
	"judges": "decision-maker-insights", "smart-search": "embeddings", "citation-treatment": "citation-enhancements",
}

# (key, name, chip, what it shows). The demos run on fixed, invented data.
DEMOS = [
	("library", "Reference library", "Mock-up", "Search the law, select a paragraph, see the decisions and guidance tied to it."),
	("tags", "Smarter tags", "Mock-up", "Pick a tag and see the exact words that triggered it. Filter a list of decisions by tag."),
	("coverage", "Coverage", "Mock-up", "Choose sources and years, include French counterparts, run a pretend daily update."),
	("teams", "Profiles and teams", "Mock-up", "Sign in, join a team, share an insight, pin a decision, comment on a shared draft."),
	("ai", "Argument breakdown", "Future local AI · mock-up", "A decision split into positions, propositions, issues and citations, then read as a story."),
	("reader", "Live document reader", "Future local AI · mock-up", "A memo split into issue and arguments, each beside its authority."),
	("scc", "Supreme Court expansion", "Mock-up", "Factums, interveners and hearing material beside the decision: what was argued versus what the Court said."),
]


def _e(value: str) -> str:
	return html.escape(value, quote=False)


def _tier_chip(tier: str) -> str:
	return f'<span class="rm-tier {tier}" title="{_e(TIERS[tier][1])}">{TIERS[tier][0]}</span>'


def _status_chip(status: str) -> str:
	return f'<span class="tag {status}">{STATUSES[status]}</span>'


def _tier_counts(slugs: list[str]) -> str:
	out = ""
	for tier in TIERS:
		n = sum(1 for s in slugs if tier_of(s) == tier)
		if n:
			out += f'<span class="rm-tier {tier}">{n} {TIERS[tier][0].lower()}</span>'
	return out


def _demo_links(slug: str) -> str:
	from .coming_soon_page import _DEMO_LINKS

	links = _DEMO_LINKS.get(slug)
	if not links:
		return ""
	items = "; ".join(f'<a href="#demo-{key}"><strong>{_e(label)}</strong></a> ({_e(what)})' for key, label, what in links)
	return f'<div class="note"><strong>See it working.</strong> Click through a demo on fixed, invented data: {items}.</div>'


def _item(entry: tuple) -> str:
	anchor, title, status, paragraphs, example, today, needs, *rest = entry
	tier = tier_of(anchor)
	paras = "".join(f"<p>{_e(text)}</p>" for text in paragraphs)
	if anchor == "whose-position":
		paras += '<p><a href="#argument-breakdown"><strong>Read the full write-up on this work below &darr;</strong></a></p>'
	elsewhere = f'<div><strong>What exists elsewhere</strong><span>{_e(rest[0])}</span></div>' if rest else ""
	return (
		f'<details class="rm-item" id="{anchor}" data-tier="{tier}"><summary><span class="rm-title">{_e(title)}</span>'
		f'<span class="rm-chips">{_tier_chip(tier)}{_status_chip(status)}</span>'
		f'<span class="rm-line">{_e(_first_sentence(today))}</span></summary>'
		f'<div class="rm-body">{paras}<div class="status-list">'
		f"<div><strong>What you could do</strong><span>{_e(example)}</span></div>"
		f"<div><strong>What exists today</strong><span>{_e(today)}</span></div>"
		f"<div><strong>What it needs</strong><span>{_e(needs)}</span></div>"
		f"{elsewhere}</div></div></details>"
	)


def _areas() -> str:
	out = ""
	for number, (key, label, text, slugs) in enumerate(PARTS, 1):
		out += f'<div class="part"><h3>Part {number}: {_e(label)}</h3><p class="small">{_e(text)}</p>'
		for slug in slugs:
			area = SECTIONS[slug]
			item_slugs = [entry[0] for entry in area["items"]]
			note = f'<div class="note">{_e(area["note"])}</div>' if area.get("note") else ""
			out += (
				f'<details class="rm-area" id="{slug}"><summary><span class="rm-title">{_e(area["label"])}</span>'
				f'<span class="rm-chips">{_tier_counts(item_slugs)}</span>'
				f'<span class="rm-line">{_e(area["summary"])}</span></summary>'
				f'<div class="rm-body"><p class="lede">{_e(area["lede"])}</p><p>{_e(area["why"])}</p>{note}{_demo_links(slug)}'
				f'{"".join(_item(entry) for entry in area["items"])}</div></details>'
			)
		out += "</div>"
	return out


def _built_tools() -> str:
	from .pitch_nav import COMING_SOON

	rows = "".join(
		f'<div class="chiprow"><strong>{_e(name)}</strong><span>{_e(text)} '
		f'<a href="/data-explorer?tab=soon-{key}&amp;group=soon" target="_top">Open it (Experimental on) &rarr;</a></span></div>'
		for key, name, text in COMING_SOON
	)
	return (
		'<details class="rm-area" id="built-tools" data-tier="untested"><summary><span class="rm-title">Built tools off the main menu</span>'
		f'<span class="rm-chips">{_tier_chip("untested")}</span>'
		f'<span class="rm-line">{len(COMING_SOON)} working pages that sit behind the Experimental switch while they are checked.</span></summary>'
		'<div class="rm-body"><p class="lede">These pages run today but are not on the main menu. They appear under Development when the Experimental switch (top right) is on. None has a measured accuracy yet, so each is listed as Untested.</p>'
		f'<div class="status-list">{rows}</div></div></details>'
	)


def _scope_css(css: str) -> str:
	"""Prefix every rule with .rm-ff so the concept pictures keep their own look without touching the page."""
	out = []
	for match in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
		selectors = ",".join(f".rm-ff {s.strip()}" for s in match.group(1).split(",") if s.strip())
		out.append(f"{selectors}{{{match.group(2)}}}")
	return "".join(out)


@lru_cache(maxsize=1)
def _future_css() -> str:
	text = (HERE / "future_features.html").read_text(encoding="utf-8")
	start = text.index(".chip{")
	end = text.index(".wrap{")
	css = text[start:end]
	# The Future features page styled these for a full page; the roadmap draws them inside its own items.
	css = re.sub(r"\.cards4\{[^}]*\}", "", css)
	return _scope_css(css)


@lru_cache(maxsize=1)
def _future_main() -> str:
	text = (HERE / "future_features.html").read_text(encoding="utf-8")
	return text[text.index('<main class="wrap">') : text.index("</main>")]


def _future() -> str:
	main = _future_main()
	intro = re.search(r'<p class="intro">(.*?)</p>', main, re.S)
	note = re.search(r'<div class="note">(.*?)</div>', main, re.S)
	out = (
		f'<p class="lede">{intro.group(1) if intro else ""}</p>'
		f'<div class="note">{note.group(1) if note else ""}</div>'
		'<p class="small">Pictures inside each item are concept mock-ups with invented names and numbers, not screenshots of working features.</p>'
	)
	pattern = re.compile(r'(<div class="phase"><h3>(.*?)</h3><p>(.*?)</p></div>)|<section class="item" id="([^"]+)">(.*?)</section>', re.S)
	for match in pattern.finditer(main):
		if match.group(1):
			out += f'<div class="part"><h3>{match.group(2)}</h3><p class="small">{match.group(3)}</p></div>'
			continue
		anchor, inner = match.group(4), match.group(5)
		head = re.match(r'\s*<div class="ihead">(.*?)</div>', inner, re.S)
		if not head:
			continue
		title = re.search(r"<h2>(.*?)</h2>", head.group(1), re.S).group(1)
		number = re.search(r'<span class="num">(\d+)</span>', head.group(1))
		if number:
			title = f"{number.group(1)}. {title}"
		label = re.search(r'<span class="tag \w+">(.*?)</span>', head.group(1), re.S)
		body = inner[head.end() :].replace("exists in Coming soon", "exists behind the Experimental switch").replace("sit in Coming soon", "sit behind the Experimental switch")
		item = FF_TO_ITEM.get(anchor)
		tier = tier_of(item) if item else None
		chips = (_tier_chip(tier) if tier else "") + (f'<span class="tag ffl">{label.group(1)}</span>' if label else "")
		data = f' data-tier="{tier}"' if tier else ""
		out += (
			f'<details class="rm-item rm-ff-item" id="ff-{anchor}"{data}><summary><span class="rm-title">{title}</span>'
			f'<span class="rm-chips">{chips}</span></summary><div class="rm-body rm-ff">{body}</div></details>'
		)
	return out


def _argument() -> str:
	from .coming_soon_argument import _SECTIONS

	out = (
		'<p class="lede">A preview of work in progress. Each paragraph of a decision would show whose position it reports, so you can tell the Court’s own reasoning from a party’s argument, and in time check a draft argument against how the same issues were decided.</p>'
		'<div class="note"><strong>Preview.</strong> The reader preview “Show whose position” is live. The accuracy figures here come from earlier small tests graded by Claude, not by lawyers, and are being re-measured.</div>'
	)
	for anchor, heading, paragraphs in _SECTIONS:
		items, text = [], ""
		for para in paragraphs:
			if para.startswith("- "):
				items.append(para[2:])
			else:
				if items:
					text += "<ul>" + "".join(f"<li>{_e(i)}</li>" for i in items) + "</ul>"
					items = []
				text += f"<p>{_e(para)}</p>"
		if items:
			text += "<ul>" + "".join(f"<li>{_e(i)}</li>" for i in items) + "</ul>"
		tier = "tested" if anchor == "results" else None
		chip = _tier_chip("tested") if tier else ""
		out += (
			f'<details class="rm-item" id="arg-{anchor}"><summary><span class="rm-title">{_e(heading)}</span>'
			f'<span class="rm-chips">{chip}</span></summary><div class="rm-body">{text}</div></details>'
		)
	return out


def _demos() -> str:
	out = (
		'<p class="lede">Working demos on fixed, invented data, drawn in the site’s own look. They run in your browser. Nothing here reads the library, signs anyone in or calls an AI. Every demo says whether it is a mock-up or a future local-AI idea. All are Untested.</p>'
	)
	for key, name, chip, what in DEMOS:
		out += (
			f'<details class="rm-item" id="demo-{key}" data-lazy="1" data-tier="untested"><summary><span class="rm-title">{_e(name)}</span>'
			f'<span class="rm-chips">{_tier_chip("untested")}<span class="tag concept">{_e(chip)}</span></span>'
			f'<span class="rm-line">{_e(what)}</span></summary><div class="rm-body">'
			f'<iframe class="rm-frame" title="{_e(name)} demo" data-src="/coming-soon-demo#{key}" loading="lazy"></iframe></div></details>'
		)
	return out


def _tour() -> str:
	return (
		'<details class="rm-item" id="tour" data-lazy="1" data-tier="untested"><summary><span class="rm-title">Guided tour of what is coming</span>'
		f'<span class="rm-chips">{_tier_chip("untested")}<span class="tag concept">Mock-ups</span></span>'
		'<span class="rm-line">A short paced tour in three parts: better data, profiles and teams, and a future local AI layer.</span></summary>'
		'<div class="rm-body"><p>The screens use invented names and numbers. Some of what the tour shows is on the site now and says so on its own label.</p>'
		'<iframe class="rm-frame tall" title="Guided tour" data-src="/roadmap/tour" loading="lazy"></iframe></div></details>'
	)


def _meanings() -> str:
	return "".join(f'<div class="chiprow"><strong>{_status_chip(key)}</strong><span>{_e(text)}</span></div>' for key, text in STATUS_MEANING.items())


_CSS = """
.ilit-about .rm-controls{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 0;align-items:center}
.ilit-about .rm-controls button{font:600 12.5px/1 inherit;padding:9px 12px;border:1px solid var(--border);border-radius:5px;background:var(--surface);color:var(--text);cursor:pointer}
.ilit-about .rm-controls button[aria-pressed="true"]{background:var(--text);color:#fff;border-color:var(--text)}
.ilit-about .rm-controls .sep{flex:1}
.ilit-about .rm-tier{display:inline-block;padding:2px 9px;border-radius:999px;font-size:11px;font-weight:700;white-space:nowrap}
.ilit-about .rm-tier.live{background:var(--teal-soft);color:var(--teal)}
.ilit-about .rm-tier.tested{background:var(--blue-soft);color:var(--blue)}
.ilit-about .rm-tier.untested{background:#ecebe4;color:var(--muted)}
.ilit-about .tag.ffl{background:var(--amber-soft);color:var(--amber)}
.ilit-about .rm-legend{margin-top:16px}
.ilit-about .rm-legend div{grid-template-columns:140px minmax(0,1fr)!important}
.ilit-about details.rm-area,.ilit-about details.rm-item{margin-top:10px;border:1px solid var(--border);border-radius:6px;background:var(--surface)}
.ilit-about details.rm-item{margin:0;border-width:1px 0 0;border-radius:0;background:transparent}
.ilit-about details.rm-item:first-of-type{border-top:1px solid var(--border)}
.ilit-about summary{position:relative;cursor:pointer;list-style:none;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 14px;align-items:start;padding:13px 16px 13px 38px}
.ilit-about summary::-webkit-details-marker{display:none}
.ilit-about summary::before{content:"+";position:absolute;left:16px;top:12px;color:var(--muted);font-weight:700}
.ilit-about details[open]>summary::before{content:"\\2212"}
.ilit-about summary .rm-title{grid-column:1;font:600 17px/1.3 var(--serif)}
.ilit-about details.rm-item>summary .rm-title{font-family:inherit;font-size:15px;font-weight:600;line-height:1.35}
.ilit-about summary .rm-chips{grid-column:2;grid-row:1;display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}
.ilit-about summary .rm-chips .tag{margin:0}
.ilit-about summary .rm-line{grid-column:1 / -1;color:var(--muted);font-size:13px;font-weight:400}
.ilit-about summary:focus-visible{outline:2px solid var(--teal);outline-offset:-2px}
.ilit-about .rm-body{padding:2px 16px 16px 36px}
.ilit-about details.rm-item .rm-body{padding-left:36px}
.ilit-about .rm-frame{display:block;width:100%;height:640px;border:1px solid var(--border);border-radius:6px;background:#fff}
.ilit-about .rm-frame.tall{height:760px}
.ilit-about .rm-ff{--red:#9b2c2c;--red-soft:#f8e6e6;--serif:"Newsreader",Georgia,serif}
.ilit-about .rm-ff .lede{margin:6px 0 14px;font-size:15px}
.ilit-about .rm-ff .mock{border:1px dashed var(--amber);border-radius:8px;background:#fbf9f1;overflow:hidden;max-width:760px}
.ilit-about .rm-ff .mockbar{padding:5px 12px;background:var(--amber-soft);color:#5c4510;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.ilit-about .rm-ff .mockbody{padding:12px}
.ilit-about .rm-ff .facts{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:12px;margin-top:14px}
.ilit-about .rm-ff .facts>div{padding:12px 14px;border:1px solid var(--border);border-radius:6px;background:var(--surface)}
.ilit-about .rm-ff .facts h4{margin:0 0 6px;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.ilit-about .rm-ff .facts p,.ilit-about .rm-ff .facts li{font-size:13.5px;line-height:1.55}.ilit-about .rm-ff .facts p{margin:0}.ilit-about .rm-ff .facts ul{margin:0;padding-left:18px}
.ilit-about .rm-ff .grid2.even{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px}
.ilit-about .rm-ff .card{padding:12px 14px;border:1px solid var(--border);border-radius:6px;background:#fff}
.ilit-about .rm-ff .card h3{margin:0 0 4px;font:600 16px/1.25 var(--serif)}.ilit-about .rm-ff .card p{margin:0;font-size:13.5px;color:var(--muted)}
.ilit-about .rm-ff .mock{overflow-x:auto}
.ilit-about [hidden]{display:none!important}
.ilit-about .rm-top{display:none;margin:0 0 10px}
@media(max-width:760px){.ilit-about .rm-ff .facts,.ilit-about .rm-ff .grid2.even{grid-template-columns:1fr}.ilit-about summary{grid-template-columns:minmax(0,1fr)}.ilit-about summary .rm-chips{grid-column:1;grid-row:auto;justify-content:flex-start}.ilit-about .rm-body,.ilit-about details.rm-item .rm-body{padding-left:16px}}
"""

_JS = """
(function(){
var root=document.querySelector('.ilit-about');
function all(sel){return Array.prototype.slice.call(root.querySelectorAll(sel));}
function setAll(open){all('details').forEach(function(d){if(d.hasAttribute('data-lazy'))return;d.open=open;});}
document.getElementById('rmExpand').addEventListener('click',function(){setAll(true);});
document.getElementById('rmCollapse').addEventListener('click',function(){setAll(false);});
all('details[data-lazy]').forEach(function(d){d.addEventListener('toggle',function(){if(!d.open)return;var f=d.querySelector('iframe[data-src]');if(f&&!f.getAttribute('src'))f.setAttribute('src',f.getAttribute('data-src'));});});
var buttons=all('[data-tier-filter]');
function applyFilter(tier){
  buttons.forEach(function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-tier-filter')===tier));});
  all('details.rm-item[data-tier]').forEach(function(d){d.hidden=tier!=='all'&&d.getAttribute('data-tier')!==tier;});
  all('details.rm-area').forEach(function(a){var items=a.querySelectorAll('details.rm-item[data-tier]');if(!items.length){return;}var any=Array.prototype.some.call(items,function(i){return !i.hidden;});a.hidden=tier!=='all'&&!any;if(tier!=='all'&&any)a.open=true;});
}
buttons.forEach(function(b){b.addEventListener('click',function(){applyFilter(b.getAttribute('data-tier-filter'));});});
function openHash(){
  var id=decodeURIComponent((location.hash||'').slice(1));if(!id)return;
  var el=document.getElementById(id);if(!el)return;
  if(el.hidden){applyFilter('all');}
  for(var p=el;p&&p!==document.body;p=p.parentElement){if(p.tagName==='DETAILS')p.open=true;}
  if(el.scrollIntoView)el.scrollIntoView();
}
window.addEventListener('hashchange',openHash);openHash();
if(window.top===window.self){var top=document.querySelector('.rm-top');if(top)top.style.display='block';}
})();
"""


def _counts_line() -> str:
	slugs = [entry[0] for area in SECTIONS.values() for entry in area["items"]]
	total = len(slugs)
	return f"{total} items in {len(SECTIONS)} areas. " + ", ".join(f"{sum(1 for s in slugs if tier_of(s) == t)} {TIERS[t][0].lower()}" for t in TIERS) + "."


def render() -> str:
	legend = "".join(f'<div class="chiprow"><strong>{_tier_chip(t)}</strong><span>{_e(text)}</span></div>' for t, (_n, text) in TIERS.items())
	filters = "".join(
		f'<button type="button" data-tier-filter="{t}" aria-pressed="false">{label}</button>'
		for t, label in (("all", "All"), ("live", "Live"), ("tested", "Tested"), ("untested", "Untested"))
	).replace('data-tier-filter="all" aria-pressed="false"', 'data-tier-filter="all" aria-pressed="true"')
	body = (
		'<p class="rm-top"><a href="/data-explorer?tab=roadmap-overview&amp;group=roadmap">Open this inside the site &rarr;</a></p>'
		'<header><p class="eyebrow">Roadmap</p><h1>Where iLit is today and where it is going</h1>'
		'<p class="lede">iLit today is a library of Canadian immigration decisions with a formatted reader, search, citations and law links. This one page lists everything planned, built or imagined, in four parts: the eight areas of work, the tools that are built but off the main menu, the longer future-features write-up with concept pictures, and the demos and guided tour. Each item is open or closed with the arrow, and each carries one evidence tier.</p>'
		f'<div class="status-list rm-legend">{legend}</div>'
		f'<p class="small">{_e(_counts_line())} Other test results exist outside the repository; none is shown here until its source has been checked.</p>'
		f'<div class="note">{_RULE}</div>'
		'<div class="rm-controls"><button type="button" id="rmExpand">Expand all</button><button type="button" id="rmCollapse">Collapse all</button>'
		f'<span class="sep"></span><span class="small">Show:</span>{filters}</div></header>'
		'<section id="areas"><h2>1. The eight areas of work</h2>'
		'<p class="intro">Better data improves every page at once, new features sit on top of it, and the last part is the groundwork a deployment inside the Agency would need.</p>'
		f"{_areas()}</section>"
		f'<section id="tools"><h2>2. Built, but off the main menu</h2>{_built_tools()}</section>'
		f'<section id="future-features"><h2>3. Future features in depth</h2>{_future()}</section>'
		f'<section id="argument-breakdown"><h2>4. Whose position: breaking a decision into arguments</h2>{_argument()}</section>'
		f'<section id="demos"><h2>5. Demos</h2>{_demos()}</section>'
		f'<section id="tour-section"><h2>6. Guided tour</h2>{_tour()}</section>'
		'<section id="labels"><h2>How to read the labels</h2><p class="intro">The evidence tier says how far the claim is proven. The label beside it says how far the work has got.</p>'
		f'<div class="status-list">{_meanings()}</div></section>'
		"<footer>The Roadmap lists work that is not finished. “Concept only” means no part of it exists. Nothing here is a promise.</footer>"
	)
	return (
		'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
		"<title>iLit: roadmap</title>"
		'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
		'<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,600&display=swap" rel="stylesheet">'
		f"<style>{_about_css()}{_EXTRA_CSS}{_CSS}{_future_css()}</style></head>"
		f'<body><div class="ilit-about"><div class="wrap">{body}</div></div><script>{_JS}</script></body></html>'
	)


def tour_html() -> str:
	return (HERE / "coming_soon_preview.html").read_text(encoding="utf-8")


# Old address -> anchor on the Roadmap, so every earlier link still lands in the right place.
REDIRECT_ANCHORS = {"overview": "", "argument-breakdown": "#argument-breakdown", **{slug: f"#{slug}" for slug in SECTIONS}}
