"""Printable, source-linked legal issue brief page."""

from __future__ import annotations

from html import escape
from typing import Any

from ..issue_brief_analytics import minister_win_rate_label


MAX_PRINT_DECISIONS = 12


def issue_brief_page_html(brief: dict[str, Any]) -> str:
	"""Render a compact printable view of an issue brief JSON payload."""
	tag = escape(str(brief.get("tag") or ""))
	decision_count = int(brief.get("decision_count") or 0)
	decisions = brief.get("decisions", [])
	semantics = brief.get("semantics") or {}

	if not decision_count:
		empty = '<p class="empty">No decisions are tagged with this issue.</p>'
		year_rows = court_rows = authority_rows = decision_rows = empty
	else:
		year_rows = "".join(
			"<tr>"
			f"<td>{escape(str(row.get('year') if row.get('year') is not None else 'Unknown'))}</td>"
			f"<td>{int(row.get('decision_count') or 0)}</td>"
			f"<td>Unclassified: {int(row.get('unclassified_count') or 0)}</td>"
			f"<td>{escape(minister_win_rate_label(row.get('minister_win_rate')))}</td>"
			"</tr>"
			+ "".join(
				"<tr class=\"split\">"
				f"<td>{escape(str(outcome.get('outcome') or 'unclassified'))}</td>"
				f"<td>{int(outcome.get('count') or 0)}</td>"
				f"<td>{float(outcome.get('percentage') or 0):.1f}%"
				f" (unclassified {int(outcome.get('unclassified_count') or 0)};"
				f" denominator {int(outcome.get('denominator') or 0)})</td>"
				"<td></td></tr>"
				for outcome in row.get("outcome_splits", [])
			)
			for row in brief.get("years", [])
		)
		court_rows = "".join(
			f"<tr><td>{escape(str(row.get('court') or 'Unspecified'))}</td>"
			f"<td>{int(row.get('decision_count') or 0)}</td></tr>"
			for row in brief.get("courts", [])
		)
		authority_rows = "".join(
			"<tr>"
			f"<td><a href=\"{escape(str(row.get('url') or '#'), quote=True)}\">"
			f"{escape(str(row.get('citation') or row.get('title') or 'Linked authority'))}</a></td>"
			f"<td>{int(row.get('citation_occurrences') or 0)}</td>"
			f"<td>{int(row.get('citing_decisions') or 0)}</td></tr>"
			for row in brief.get("top_authorities", [])
		) or '<tr><td colspan="3">No resolved case citations found.</td></tr>'
		decision_parts = []
		for row in decisions[:MAX_PRINT_DECISIONS]:
			outcome = f" · {escape(str(row['outcome']))}" if row.get("outcome") else ""
			decision_parts.append(
				f"<li><a href=\"{escape(str(row.get('url') or '#'), quote=True)}\">"
				f"{escape(str(row.get('citation') or row.get('title') or 'Decision'))}</a>"
				f" — {escape(str(row.get('court') or 'Unspecified'))}{outcome}</li>"
			)
		decision_rows = "".join(decision_parts) or '<li>No linked decisions.</li>'
		decision_disclosure = (
			f'<p class="note decision-disclosure">Showing {len(decision_parts)} of '
			f'{decision_count} decisions; see JSON brief for the complete list.</p>'
		)

	empty_state = not decision_count
	return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Issue brief: {tag}</title>
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#f2f1ec;color:#202522;font:13px/1.4 system-ui,sans-serif}}
main{{max-width:1000px;margin:24px auto;padding:28px;background:white;border:1px solid #d8d5ca}}
h1{{font-size:24px;margin:0 0 4px}}h2{{font-size:15px;margin:18px 0 6px;border-bottom:1px solid #d8d5ca;padding-bottom:4px}}
.meta,.note{{color:#535b56;font-size:11px}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:8px 20px}}
table{{width:100%;border-collapse:collapse;font-size:11px}}th,td{{padding:4px 6px;border-bottom:1px solid #e7e4da;text-align:left;vertical-align:top}}
th{{background:#f5f4ef}}.split td:first-child{{padding-left:18px}}ul{{margin:4px 0;padding-left:20px;columns:2}}li{{break-inside:avoid;margin-bottom:3px}}
a{{color:#164b73}}.empty{{padding:16px;border:1px dashed #aaa;color:#535b56}}
@media(max-width:650px){{main{{margin:0;padding:16px}}.grid{{grid-template-columns:1fr}}ul{{columns:1}}}}
@media print{{@page{{size:auto;margin:8mm}}body{{background:white;font-size:7.5pt;line-height:1.2}}main{{max-width:none;margin:0;padding:0;border:0}}
h1{{font-size:15pt;margin-bottom:2pt}}h2{{font-size:9pt;margin:5pt 0 2pt;padding-bottom:2pt}}
.grid{{grid-template-columns:1fr 1fr;gap:4pt 10pt}}table{{font-size:7pt}}th,td{{padding:1.5pt 3pt}}
ul{{columns:3;margin:2pt 0;padding-left:12pt}}li{{margin-bottom:1pt;break-inside:avoid}}
a{{color:inherit;text-decoration:none}}a[href]::after{{content:""}}.meta,.note{{font-size:6.5pt}}}}
</style></head>
<body><main>
<h1>Legal issue brief: {tag or "(empty tag)"}</h1>
<p class="meta">{decision_count} tagged decisions · exact active-taxonomy tag match</p>
{('<p class="empty">Enter a tag in category:value form, for example <code>issue:procedural_fairness</code>, then reload <code>/issue-brief-ui?tag=…</code>.</p>' if not tag else '')}
{('<p class="empty">No decisions are tagged with this issue.</p>' if empty_state and tag else '')}
{'' if empty_state else f'''<div class="grid">
<section><h2>Decisions by year and outcome</h2><table><thead><tr><th>Year / outcome</th><th>Decisions</th><th>Unclassified / outcome share</th><th>Minister win rate</th></tr></thead><tbody>{year_rows}</tbody></table>
<p class="note">Outcome percentages use all tagged decisions in the year. Minister win rates use classified government outcomes only; total n and unclassified counts are shown for every year.</p></section>
<section><h2>Courts</h2><table><thead><tr><th>Court</th><th>Decisions</th></tr></thead><tbody>{court_rows}</tbody></table>
<h2>Top cited authorities</h2><table><thead><tr><th>Authority</th><th>Citation occurrences</th><th>Tagged citing decisions</th></tr></thead><tbody>{authority_rows}</tbody></table></section>
</div><h2>Tagged decisions</h2>{decision_disclosure}<ul>{decision_rows}</ul>'''}
<p class="note">Outcome source: {escape(str(semantics.get("outcomes") or ""))}</p>
<p class="note">Citation scope: {escape(str(semantics.get("citations") or ""))}</p>
<p class="note">Minister outcomes: {escape(str(semantics.get("minister_outcomes") or ""))}</p>
</main></body></html>"""
