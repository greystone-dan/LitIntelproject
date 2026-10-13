"""The reader's "Where each piece comes from" strip.

One closed line above the decision text (Experimental view only) that says how each extra block in the reader
was made: a stored AI pass, the learned position tagger, or fixed rules. It only describes; every block keeps its own data.
Numbers come from ``coming_soon_examples.json`` so this strip and the Coming soon page never disagree. Nothing here
calls a model, and nothing is sent anywhere.
"""

from __future__ import annotations

import html

from .coming_soon_preview_page import examples

# (kind, label, what it is, ((pass key, short name), ...) for the measured numbers)
GROUPS = [
	("ai", "Layers: summary, issues, paragraph notes", "Written once by a model when the decision was added, then stored and shown. Not run when you open the page.", (("frame", "summary"), ("issues", "issue results"), ("notes", "notes faithful"))),
	("learned", "Show whose position", "Cue phrases plus a small trained model, stored for the decision.", (("position", "match to labelled paragraphs"),)),
	("rules", "Quick summary, selected passages, extracted summary", "Built by fixed rules from stored header facts, tags and outcome, each tied to exact source text. No prose is written.", ()),
	("rules", "Header, tags, case details, headings", "The decision's own header, the court, the outcome badge, the Citations, Statutes and Tags toggles, and the headings in the text, all read by fixed rules.", ()),
]
KINDS = {"ai": "Stored AI pass", "learned": "Learned", "rules": "Rules only"}

CSS = """<style>
.src-strip{margin:0 0 10px;border:1px solid #dde3ec;border-radius:8px;background:#f8fafc;font-size:13px;color:#33465f}
.src-strip>summary{display:flex;flex-wrap:wrap;align-items:center;gap:6px 8px;padding:6px 10px;cursor:pointer;list-style:none;min-height:34px}
.src-strip>summary::-webkit-details-marker{display:none}
.src-strip>summary::after{content:"\\25BE";margin-left:auto;color:#5b6779}.src-strip[open]>summary::after{content:"\\25B4"}
.src-strip>summary:focus-visible{outline:2px solid #2563eb;outline-offset:2px}
.src-title{font-weight:600;color:#1f3350}
.src-tag{display:inline-block;padding:0 8px;border-radius:999px;border:1px solid;font-size:11.5px;font-weight:700;letter-spacing:.02em;line-height:20px}
.src-ai{background:#fff1c9;color:#6b4a00;border-color:#f0d49a}.src-learned{background:#efe5f5;color:#5a2f74;border-color:#d9c3e6}.src-rules{background:#e3e9f7;color:#25407a;border-color:#c5d1ec}
.src-list{margin:0;padding:2px 12px 10px;list-style:none;display:grid;gap:8px;border-top:1px solid #dde3ec}
.src-list li{padding-top:8px}.src-list b{color:#1f3350}.src-list p{margin:2px 0 0;color:#46536d}
.src-note{margin:0;padding:0 12px 10px;color:#5b6779;font-size:12px}
body:not(.reader-experimental) .src-strip{display:none!important}
</style>"""


def _numbers(keys: tuple[tuple[str, str], ...]) -> str:
	passes = {item["key"]: item for item in examples()["passes"]}
	parts = []
	for key, short in keys:
		item = passes.get(key)
		if item and item.get("number"):
			parts.append(f"{html.escape(short)} {html.escape(item['number'])}")
	return ", ".join(parts)


def strip_html() -> str:
	rows = []
	for kind, label, text, keys in GROUPS:
		measured = _numbers(keys)
		measured_html = f' <span class="src-measured">Tested: {measured}.</span>' if measured else ""
		rows.append(f'<li><span class="src-tag src-{kind}">{KINDS[kind]}</span> <b>{html.escape(label)}</b><p>{html.escape(text)}{measured_html}</p></li>')
	tags = "".join(f'<span class="src-tag src-{k}">{v}</span>' for k, v in KINDS.items())
	return (
		CSS
		+ '<details class="src-strip" id="readerSourceStrip" aria-label="Where each piece comes from"><summary><span class="src-title">Where each piece comes from</span>' + tags + "</summary>"
		+ '<ul class="src-list">' + "".join(rows) + "</ul>"
		+ '<p class="src-note">Nothing here calls a model when the page opens. Figures were graded by a model on small samples, not by a lawyer.</p></details>'
	)
