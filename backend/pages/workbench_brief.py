"""Printable Workbench briefs: one page of plain HTML with print styles (no scripts that send data anywhere)."""

from __future__ import annotations

from html import escape

_STYLE = """
:root{--text:#202522;--muted:#69726d;--border:#d8d5ca;--rust:#a4412b}
*{box-sizing:border-box}body{margin:0;background:#f1efe8;color:var(--text);font:14px/1.55 "IBM Plex Sans",Arial,sans-serif}
.sheet{max-width:860px;margin:18px auto;padding:28px 34px;background:#fffef9;border:1px solid var(--border)}
h1{margin:0 0 4px;font:700 28px/1.15 Georgia,"Newsreader",serif}h2{margin:24px 0 8px;font:700 17px Georgia,serif;border-bottom:1px solid var(--border);padding-bottom:4px}
.eyebrow{color:var(--rust);font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}.muted{color:var(--muted);font-size:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px}th,td{padding:6px 8px;border-bottom:1px solid var(--border);text-align:left;vertical-align:top}th{color:var(--muted);font-size:11px;letter-spacing:.05em;text-transform:uppercase}
.new td{background:#fff3ee}.flag{color:var(--rust);font-weight:700}.notes{white-space:pre-wrap;padding:8px 10px;border-left:3px solid var(--border);background:#f8f6ef}
.bar{display:flex;gap:10px;justify-content:space-between;align-items:center;max-width:860px;margin:14px auto 0;padding:0 4px}
.bar button,.bar a{padding:7px 14px;border:1px solid #202522;border-radius:5px;background:#202522;color:#fff;font:700 12px sans-serif;text-decoration:none;cursor:pointer}.bar a{background:#fff;color:#202522}
@media print{body{background:#fff}.bar{display:none}.sheet{margin:0;border:0;padding:0;max-width:none}a{color:inherit;text-decoration:none}}
"""


def brief_page(title: str, eyebrow: str, body_html: str) -> str:
	return (
		'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
		f"<title>{escape(title)} | iLIT Workbench</title><style>{_STYLE}</style></head><body>"
		'<div class="bar"><a href="/workbench">&larr; Back to the Workbench</a><button type="button" onclick="window.print()">Print or save as PDF</button></div>'
		f'<main class="sheet"><div class="eyebrow">{escape(eyebrow)}</div><h1>{escape(title)}</h1>{body_html}'
		'<p class="muted" style="margin-top:28px">Prepared from the stored iLIT data and your own notes. Docket figures are as of the last time the file was loaded; confirm against the Federal Court website before relying on them. Demo Workbench.</p>'
		"</main></body></html>"
	)


def esc(value: object) -> str:
	return escape("" if value is None else str(value))
