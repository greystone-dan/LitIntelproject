"""The Lab home: one page that lists every experimental tool as a card, under five headings.

It replaces the five section pills and the seventeen tool tabs the Lab used to have. Each card opens
the same tool as before, at the same address (``/data-explorer?tab=soon-<tool>&group=lab``). Served at
``/lab`` and shown inside the explorer as the Lab's first view. Nothing here needs AI.
"""

from __future__ import annotations

from .coming_soon_page import _EXTRA_CSS, _about_css, _doc, _e

# What the card says about how far each tool is proven. None of the tools has a measured accuracy yet.
_PROOF = {
	"status": ("Evidence", "The board that says how well each feature is proven."),
	"checks": ("Internal check", "Used to check the data and the tools; not a feature."),
}
_DEFAULT_PROOF = ("Not yet measured", "Built and reachable, but no accuracy figure has been measured for it.")

_CSS = """
.ilit-about .lab-head{margin:0 0 6px}
.ilit-about .lab-jump{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 4px}
.ilit-about .lab-jump a{padding:6px 12px;border:1px solid var(--border);border-radius:999px;background:var(--surface);color:var(--text);font-size:13px;text-decoration:none}
.ilit-about .lab-jump a:hover{border-color:var(--teal);color:var(--teal)}
.ilit-about .lab-sec{margin-top:26px;scroll-margin-top:12px}.ilit-about .lab-sec h2{margin:0;font:600 20px/1.3 var(--serif)}.ilit-about .lab-sec>p{margin:4px 0 0;color:var(--muted);font-size:14px}
.ilit-about .lab-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;margin-top:12px}
.ilit-about a.lab-card{display:flex;flex-direction:column;gap:6px;padding:14px;border:1px solid var(--border);border-radius:6px;background:#fff;color:var(--text);text-decoration:none}
.ilit-about a.lab-card:hover{border-color:var(--teal)}.ilit-about a.lab-card:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
.ilit-about .lab-card strong{font:600 16px/1.3 var(--serif)}.ilit-about .lab-card span.t{font-size:13.5px;color:var(--muted);flex:1}
.ilit-about .lab-card em{align-self:flex-start;font-style:normal;font-size:11px;font-weight:700;padding:2px 9px;border-radius:999px;border:1px solid var(--border);background:var(--surface);color:var(--muted)}
.ilit-about .lab-foot{margin-top:28px;color:var(--muted);font-size:13px}
"""


def _cards() -> str:
	from .pitch_nav import LAB, _lab_names

	names = _lab_names()
	out = []
	for cat, label, blurb, keys in LAB:
		proof = _PROOF.get(cat, _DEFAULT_PROOF)
		cards = "".join(
			f'<a class="lab-card" href="/data-explorer?tab=soon-{key}&amp;group=lab" target="_top">'
			f'<strong>{_e(names[key][0])}</strong><span class="t">{_e(names[key][1])}</span><em title="{_e(proof[1])}">{proof[0]}</em></a>'
			for key in keys
		)
		out.append(f'<section class="lab-sec" id="lab-{cat}"><h2>{_e(label)}</h2><p>{_e(blurb)}</p><div class="lab-cards">{cards}</div></section>')
	return "".join(out)


def render() -> str:
	from .pitch_nav import LAB

	jump = "".join(f'<a href="#lab-{cat}">{_e(label)}</a>' for cat, label, _b, _k in LAB)
	body = (
		'<header class="lab-head"><p class="eyebrow">Lab · private</p><h1>The Lab</h1>'
		'<p class="lede">Built and reachable, but not yet proven. Each card opens a tool as it is; none has a measured accuracy yet.</p>'
		f'<nav class="lab-jump" aria-label="Lab sections">{jump}</nav></header>'
		f"{_cards()}"
		'<p class="lab-foot">The public view of the same work is on the Coming soon tab.</p>'
	)
	return _doc("the Lab", body).replace("</style></head>", _CSS + "</style></head>", 1).replace("<title>iLit: coming soon, the Lab</title>", "<title>iLit: the Lab</title>")
