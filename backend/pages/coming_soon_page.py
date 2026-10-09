"""Coming soon: the roadmap as an overview page plus one full page per area.

Each page is served at ``/coming-soon/<slug>`` and shown in the Coming soon frame of the
main explorer. The layout reuses the About page's own stylesheet so every tab reads the
same way. Every item carries one honest status; nothing here is a promise, and nothing
needs AI when someone uses the site.
"""

from __future__ import annotations

import html
import re
from functools import lru_cache
from pathlib import Path

from .coming_soon_content import PARTS, SECTIONS

STATUSES = {
	"built": "Built",
	"partly": "Partly built",
	"progress": "In progress",
	"planned": "Planned",
	"concept": "Concept only",
}
STATUS_MEANING = {
	"built": "Finished and on the site today.",
	"partly": "Some of it works today. The page says what is missing.",
	"progress": "Being worked on now.",
	"planned": "Decided and described, not started.",
	"concept": "An idea only. Nothing is built, and it needs something the site does not have yet, such as an on-premises model or agency sign-in.",
}

ORDER = ["overview"] + [slug for _key, _label, _text, slugs in PARTS for slug in slugs]
PART_OF = {slug: label for _key, label, _text, slugs in PARTS for slug in slugs}
LABELS = {"overview": "Overview", **{key: value["label"] for key, value in SECTIONS.items()}}

_EXTRA_CSS = """
html,body{margin:0;background:#fffef9}
body{font-family:"IBM Plex Sans",system-ui,sans-serif;padding:14px 18px 28px}
.ilit-about .tag{margin:0 0 0 10px;vertical-align:3px;white-space:nowrap}
.ilit-about .glance th:nth-child(2),.ilit-about .glance td:nth-child(2){width:132px;white-space:nowrap}
.ilit-about .tag.built{background:var(--teal-soft);color:var(--teal)}
.ilit-about .tag.partly{background:var(--blue-soft);color:var(--blue)}
.ilit-about .tag.progress{background:var(--rust-soft);color:var(--rust)}
.ilit-about .tag.planned{background:var(--amber-soft);color:var(--amber)}
.ilit-about .tag.concept{background:#ecebe4;color:var(--muted)}
.ilit-about .status-list .tag{margin:0}
.ilit-about .tag{font-family:"IBM Plex Sans",system-ui,sans-serif;letter-spacing:0}
.ilit-about .status-list div.chiprow{grid-template-columns:200px minmax(0,1fr)}
.ilit-about .glance td:first-child{font-weight:600;white-space:nowrap}
.ilit-about .glance td:first-child a{color:var(--text);text-decoration:none;border-bottom:1px solid var(--border)}
.ilit-about .glance td:first-child a:hover{border-color:var(--text)}
.ilit-about .area h2 a{color:inherit;text-decoration:none}
.ilit-about .area h2 a:hover{text-decoration:underline}
.ilit-about .area .counts{margin-top:10px;display:flex;gap:6px;flex-wrap:wrap}
.ilit-about .area .counts .tag{margin:0}
.ilit-about .sub{margin:18px 0 0;font:600 11px/1.3 var(--sans, inherit);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.ilit-about .area-card .counts{margin-top:10px;display:flex;gap:6px;flex-wrap:wrap}
.ilit-about .area-card .counts .tag{margin:0}
.ilit-about .area-card{scroll-margin-top:12px}
.ilit-about .part{margin-top:22px}.ilit-about .part h3{margin:0;font:600 19px/1.3 var(--serif)}.ilit-about .part .small{margin:4px 0 0}.ilit-about .part .grid{margin-top:10px}
.ilit-about .pager{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:34px;padding-top:18px;border-top:1px solid var(--border);font-size:14px}
.ilit-about .pager a{color:var(--blue);text-decoration:none}.ilit-about .pager a:hover{text-decoration:underline}
.ilit-about .glance td:first-child{font-weight:600}
@media(max-width:760px){.ilit-about .glance thead{display:none}.ilit-about .glance,.ilit-about .glance tbody{display:block}.ilit-about .glance tr{display:block;padding:11px 14px;border-top:1px solid var(--border)}.ilit-about .glance tr:first-child{border-top:0}.ilit-about .glance td{display:block;width:auto!important;padding:2px 0;border:0;white-space:normal!important}.ilit-about .glance td:nth-child(2){margin:3px 0 4px}.ilit-about .glance td:first-child{white-space:normal}.ilit-about .status-list div.chiprow{grid-template-columns:minmax(0,1fr)}}
"""


@lru_cache(maxsize=1)
def _about_css() -> str:
	"""The About page's stylesheet, so these pages match it exactly."""
	text = (Path(__file__).resolve().parent / "about_content.html").read_text(encoding="utf-8")
	match = re.search(r"<style>(.*?)</style>", text, re.S)
	return match.group(1) if match else ""


def _e(value: str) -> str:
	return html.escape(value, quote=False)


def _tag(status: str) -> str:
	return f'<span class="tag {status}">{STATUSES[status]}</span>'


def _doc(title: str, body: str) -> str:
	return (
		'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
		f"<title>iLit: coming soon, {_e(title)}</title>"
		'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
		'<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,600&display=swap" rel="stylesheet">'
		f"<style>{_about_css()}{_EXTRA_CSS}</style></head><body><div class=\"ilit-about\"><div class=\"wrap\">{body}</div></div></body></html>"
	)


def _tab_link(slug: str, label: str) -> str:
	return f'<a href="/data-explorer?tab=roadmap-{slug}&amp;group=roadmap" target="_top">{_e(label)}</a>'


def _first_sentence(text: str) -> str:
	match = re.match(r"(.+?[.!?])(?:\s|$)", text)
	return match.group(1) if match else text


_FOOTER = "<footer>Coming soon lists work that is not finished. A label says how far each item has got, and “Concept only” means no part of it exists. Nothing here is a promise.</footer>"
_RULE = "<b>The rule behind all of it.</b> Normal search uses no AI, and nothing a person types is sent to an outside AI service. Where AI would help, it would run on the agency’s own computers or when decisions are added, and its work would be stored as data that links back to the source paragraph."
_STATUS_ORDER = ["built", "partly", "progress", "planned", "concept"]


def _counts(items: list) -> str:
	found = [status for status in _STATUS_ORDER if any(item[2] == status for item in items)]
	return "".join(
		f'<span class="tag {status}">{sum(1 for item in items if item[2] == status)} {STATUSES[status].lower()}</span>' for status in found
	)


def _overview() -> str:
	parts = ""
	number = 0
	for key, label, text, slugs in PARTS:
		cards = ""
		for slug in slugs:
			number += 1
			area = SECTIONS[slug]
			cards += (
				f'<a class="card go area-card" id="{slug}" href="/data-explorer?tab=roadmap-{slug}&amp;group=roadmap" target="_top">'
				f'<span class="k">{number} · {_e(area["label"])}</span><p>{_e(area["summary"])}</p>'
				f'<div class="counts">{_counts(area["items"])}</div></a>'
			)
		parts += f'<div class="part" id="part-{key}"><h3>{_e(label)}</h3><p class="small">{_e(text)}</p><div class="grid three areas">{cards}</div></div>'
	now = "".join(
		f'<div class="chiprow"><strong>{_e(item[1])}</strong><span>{_tag(item[2])} {_e(item[5])} '
		f'<a href="/data-explorer?tab=roadmap-{slug}&amp;group=roadmap" target="_top">{_e(SECTIONS[slug]["label"])} &rarr;</a></span></div>'
		for slug in ORDER[1:]
		for item in SECTIONS[slug]["items"]
		if item[2] == "progress"
	)
	meanings = "".join(f'<div class="chiprow"><strong>{_tag(key)}</strong><span>{_e(text)}</span></div>' for key, text in STATUS_MEANING.items())
	return (
		'<header><p class="eyebrow">Coming soon</p><h1>Where iLit is going next</h1>'
		'<p class="lede">iLit today is a library of Canadian immigration decisions with a formatted reader, search, citations and law links. '
		'What comes next is in three parts: better data, which improves every page at once; new features built on that data; and the groundwork a deployment inside the Agency would need. '
		'Each item says honestly how far it has got and, where it helps, what existing tools offer today.</p>'
		'<div class="note"><strong>Take the guided preview.</strong> A short, paced tour of what is coming: a larger reference library, profiles and teams, and a future local AI layer, drawn in the site\'s own look. <a href="/coming-soon-preview" target="_top"><strong>Start the preview &rarr;</strong></a></div>',
		'<div class="note"><strong>Try the demos.</strong> Six working demos you can click through on fixed, invented data: the reference library, smarter tags, coverage, profiles and teams, and two future local-AI ideas (an argument breakdown and a live document reader). <a href="/data-explorer?tab=roadmap-demos&amp;group=roadmap" target="_top"><strong>Open the demos &rarr;</strong></a></div>'
		f'<div class="note">{_RULE}</div></header>'
		f'<section id="areas"><h2>{len(ORDER) - 1} areas in three parts</h2><p class="intro">Each area has its own tab above, with a full page on every item. The labels count how far its items have got.</p>'
		f'{parts}</section>'
		'<section id="now"><h2>Being worked on now</h2><p class="intro">The items labelled “In progress”, across every area.</p>'
		f'<div class="status-list">{now}</div></section>'
		'<section id="labels"><h2>How to read the labels</h2><p class="intro">Every item carries one of these five labels. “Built” appears only where the feature is on the site today.</p>'
		f'<div class="status-list">{meanings}</div></section>'
		'<section id="elsewhere"><h2>The longer roadmap</h2>'
		'<p>The original long roadmap, with its concept pictures, is still available as <a href="/future-features" target="_top">one page</a>. Some tools that already run but are not ready to rely on are kept in a separate development area, outside the main site.</p></section>'
		+ _FOOTER
	)


def _pager(slug: str) -> str:
	index = ORDER.index(slug)
	links = []
	if index > 1:
		prev = ORDER[index - 1]
		links.append(f'<a href="/data-explorer?tab=roadmap-{prev}&amp;group=roadmap" target="_top">&larr; {_e(LABELS[prev])}</a>')
	links.append('<a href="/data-explorer?tab=roadmap-overview&amp;group=roadmap" target="_top">All areas</a>')
	if index < len(ORDER) - 1:
		nxt = ORDER[index + 1]
		links.append(f'<a href="/data-explorer?tab=roadmap-{nxt}&amp;group=roadmap" target="_top">{_e(LABELS[nxt])} &rarr;</a>')
	return f'<nav class="pager" aria-label="Coming soon areas">{"".join(links)}</nav>'


_DEMO_LINKS = {
	"accuracy": [("tags", "Smarter tags", "pick a tag and see the exact words it matched")],
	"expansion": [("library", "Reference library", "search the law and see the decisions and guidance tied to a paragraph"), ("coverage", "Coverage", "choose sources and years and run a pretend daily update")],
	"intelligence": [("tags", "Smarter tags", "pick a tag and see the exact words it matched"), ("ai", "Argument breakdown", "a decision split into positions, issues and citations")],
	"fc-files": [("coverage", "Coverage", "choose sources and years and run a pretend daily update")],
	"team": [("teams", "Profiles and teams", "sign in, join a team, share an insight, comment on a draft")],
	"local-ai": [("ai", "Argument breakdown", "a decision split into positions, issues and citations"), ("reader", "Live document reader", "a memo read beside its authorities")],
}


def _demo_note(slug: str) -> str:
	links = _DEMO_LINKS.get(slug)
	if not links:
		return ""
	items = "; ".join(f'<a href="/coming-soon-demo#{key}" target="_top"><strong>{_e(label)}</strong></a> ({_e(what)})' for key, label, what in links)
	return f'<div class="note"><strong>See it working.</strong> Click through a demo on fixed, invented data: {items}.</div>'


def _section_page(slug: str) -> str:
	area = SECTIONS[slug]
	rows = "".join(
		f'<tr><td><a href="#{item[0]}">{_e(item[1])}</a></td><td>{_tag(item[2])}</td><td>{_e(_first_sentence(item[5]))}</td></tr>'
		for item in area["items"]
	)
	note = f'<div class="note">{_e(area["note"])}</div>' if area.get("note") else ""
	body = (
		f'<header><p class="eyebrow">Coming soon · {_e(PART_OF[slug])}</p><h1>{_e(area["label"])}</h1><p class="lede">{_e(area["lede"])}</p>'
		f'<p>{_e(area["why"])}</p>{note}{_demo_note(slug)}</header>'
		'<section id="glance"><h2>At a glance</h2><div class="table-wrap"><table class="glance"><thead><tr><th>Item</th><th>Where it stands</th><th>On the site today</th></tr></thead>'
		f"<tbody>{rows}</tbody></table></div></section>"
	)
	for anchor, title, status, paragraphs, example, today, needs, *rest in area["items"]:
		paras = "".join(f"<p>{_e(text)}</p>" for text in paragraphs)
		elsewhere = f'<div><strong>What exists elsewhere</strong><span>{_e(rest[0])}</span></div>' if rest else ""
		body += (
			f'<section id="{anchor}"><h2>{_e(title)}{_tag(status)}</h2>{paras}'
			'<div class="status-list">'
			f'<div><strong>What you could do</strong><span>{_e(example)}</span></div>'
			f'<div><strong>What exists today</strong><span>{_e(today)}</span></div>'
			f'<div><strong>What it needs</strong><span>{_e(needs)}</span></div>'
			f"{elsewhere}"
			"</div></section>"
		)
	return body + _pager(slug) + _FOOTER


def render(slug: str) -> str | None:
	if slug == "overview":
		return _doc("overview", _overview())
	if slug in SECTIONS:
		return _doc(SECTIONS[slug]["label"], _section_page(slug))
	return None
