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

from .coming_soon_content import SECTIONS

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

ORDER = ["overview", "accuracy", "expansion", "internal", "intelligence", "team", "local-ai"]
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


_FOOTER = "<footer>Coming soon lists work that is not finished. A label says how far each item has got, and “Concept only” means no part of it exists. Things that already run but are not ready to rely on are under Development.</footer>"
_RULE = "<b>The rule behind all of it.</b> Normal search uses no AI, and nothing a person types is sent to an outside AI service. Where AI would help, it would run on the agency’s own computers or when decisions are added, and its work would be stored as data that links back to the source paragraph."


def _overview() -> str:
	areas = ""
	for slug in ORDER[1:]:
		area = SECTIONS[slug]
		rows = "".join(
			f'<div class="chiprow"><strong>{_e(item[1])}</strong><span>{_tag(item[2])} {_e(_first_sentence(item[5]))}</span></div>' for item in area["items"]
		)
		areas += (
			f'<section class="area" id="{slug}"><h2>{_tab_link(slug, area["label"])}</h2>'
			f'<p>{_e(area["lede"])}</p><div class="status-list">{rows}</div>'
			f'<p class="small"><a href="/data-explorer?tab=roadmap-{slug}&amp;group=roadmap" target="_top">Read the full {_e(area["label"].lower())} page &rarr;</a></p></section>'
		)
	meanings = "".join(f'<div class="chiprow"><strong>{_tag(key)}</strong><span>{_e(text)}</span></div>' for key, text in STATUS_MEANING.items())
	return (
		'<header><p class="eyebrow">Coming soon</p><h1>Where iLit is going next</h1>'
		'<p class="lede">iLit today is a library of Canadian immigration decisions with a formatted reader, search, citations and statute links. This section describes what comes next, in six areas, and is honest about how far each piece has got. Each area has its own tab above, with a full page of detail.</p>'
		f'<div class="note">{_RULE}</div></header>'
		f"{areas}"
		'<section id="labels"><h2>How to read the labels</h2><p class="intro">Every item carries one of these five labels. “Built” appears only where the feature is on the site today.</p>'
		f'<div class="status-list">{meanings}</div></section>'
		'<section id="elsewhere"><h2>Other places to look</h2>'
		'<p>Tools that already run but are not ready to rely on are under the <b>Development</b> tab at the top. The original long roadmap, with its concept pictures, is still available as <a href="/future-features" target="_top">one page</a>. The case for funding the project is not on this list for now.</p></section>'
		+ _FOOTER
	)


def _section_page(slug: str) -> str:
	area = SECTIONS[slug]
	rows = "".join(
		f'<tr><td><a href="#{item[0]}">{_e(item[1])}</a></td><td>{_tag(item[2])}</td><td>{_e(_first_sentence(item[5]))}</td></tr>'
		for item in area["items"]
	)
	note = f'<div class="note">{_e(area["note"])}</div>' if area.get("note") else ""
	body = (
		f'<header><p class="eyebrow">Coming soon</p><h1>{_e(area["label"])}</h1><p class="lede">{_e(area["lede"])}</p>'
		f'<p>{_e(area["why"])}</p>{note}</header>'
		'<section id="glance"><h2>At a glance</h2><div class="table-wrap"><table class="glance"><thead><tr><th>Item</th><th>Where it stands</th><th>On the site today</th></tr></thead>'
		f"<tbody>{rows}</tbody></table></div></section>"
	)
	for anchor, title, status, paragraphs, example, today, needs in area["items"]:
		paras = "".join(f"<p>{_e(text)}</p>" for text in paragraphs)
		body += (
			f'<section id="{anchor}"><h2>{_e(title)}{_tag(status)}</h2>{paras}'
			'<div class="status-list">'
			f'<div><strong>What you could do</strong><span>{_e(example)}</span></div>'
			f'<div><strong>What exists today</strong><span>{_e(today)}</span></div>'
			f'<div><strong>What it needs</strong><span>{_e(needs)}</span></div>'
			"</div></section>"
		)
	return body + _FOOTER


def render(slug: str) -> str | None:
	if slug == "overview":
		return _doc("overview", _overview())
	if slug in SECTIONS:
		return _doc(SECTIONS[slug]["label"], _section_page(slug))
	return None
