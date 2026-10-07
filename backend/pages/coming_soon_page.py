"""Coming soon: the roadmap, one overview page plus one page per section.

Each page is served at ``/coming-soon/<slug>`` and shown in the Coming soon frame
of the main explorer. Every item carries one honest status; nothing here is a
promise, and nothing needs AI at site use time.
"""

from __future__ import annotations

import html

STATUSES = {
	"built": "Built",
	"partly": "Partly built",
	"progress": "In progress",
	"planned": "Planned",
	"concept": "Concept",
}

# slug -> (tab label, one-line summary, intro paragraph, [(title, status, what it is, where it stands, what it needs)])
SECTIONS = {
	"accuracy": (
		"Accuracy improvements",
		"Making what is already in the library more correct.",
		"Everything counsel sees is only as good as the extraction behind it. This section is about getting the citations, links, labels and names already in the library right, before adding more.",
		[
			("Citation extraction", "partly", "Finding every citation in a decision, including short forms such as “Baker, at para 44” and citations followed by a pinpoint.", "Cleaner rules are written and tested, and have been run into a separate set of tables for a first batch of decisions. The live site still shows the earlier citations.", "A checked rebuild across the whole library before the site switches over."),
			("Citation resolving", "partly", "Linking each citation to the right case and the right paragraph.", "Most links work today. Some short-form links point to the wrong case; the new rules fix a number of those.", "The rebuild above, then a spot check against a graded sample."),
			("Case types and outcomes", "partly", "Labelling each decision (for example a leave application or a refugee claim) and coding who won.", "Case types are live for the Federal Court, the RPD and the Supreme Court. Outcome coding is being rechecked against a hand-graded set because some well-known cases are coded the wrong way.", "Federal Court of Appeal types once their accuracy clears the bar, and a rerun of the outcome coding."),
			("Statute references", "progress", "Reading which sections of statutes and regulations each decision cites, so links land on the right section.", "A first batch of cases is being re-read and graded by hand. The rest waits on that grade.", "Grading of the first batch, then a decision on the remaining cases."),
			("Judges and parties", "partly", "Grouping spelling variants of judge and party names so profiles and statistics count each person once.", "Many variants are already merged. Some merges are wrong (two judges with the same surname) and French names are not covered.", "A prune of the wrong merges and more name rules."),
		],
	),
	"expansion": (
		"Expansion",
		"More cases, more tags, more laws and regulations.",
		"A bigger library makes every other feature more useful. This section lists what is being added and what is still only an idea.",
		[
			("More cases", "progress", "Adding Refugee Appeal Division and RPD decisions, and keeping the Federal Court current.", "RAD and RPD imports are under way. A daily intake of new Federal Court files is built, but it is run by hand and is not scheduled.", "Scheduling the daily intake, which needs sign-off on the computer that runs the site."),
			("More tags", "planned", "More labels on each case (issues, grounds, procedural features), so filters and statistics can go deeper.", "Tags work today and the rules that make them are deterministic. A wider set is planned.", "Agreement on the label list and a check against hand-graded cases."),
			("More laws and regulations", "partly", "The statutes and regulations that decisions cite, readable in the library.", "Federal immigration statutes and regulations are in. Quebec, Civil Code and other provincial material is left out for now.", "A decision on whether to widen the scope."),
			("French decisions", "planned", "French-language decisions and French counterparts to English ones.", "A few hundred French decisions are stored. One language is kept per decision, and RAD and RPD have none.", "Scoping which counterparts exist and how to link them."),
			("Immigration Division and Appeal Division", "concept", "Decisions of the ID and the IAD, which are not in any public dataset.", "Nothing is held.", "Agency data, supplied under the agency’s own rules."),
		],
	),
	"internal": (
		"Internal documentation",
		"The agency’s own materials, searched beside the public library.",
		"This is the part of the roadmap that matters most to the agency. The public library is the starting point; the larger value is the agency’s own memos, briefs and private decisions, searched and analysed on the agency’s own hardware with nothing leaving the building. All of it is concept except the first version of Live Analysis.",
		[
			("Internal documents, searchable", "concept", "Memos, hearing briefs, opinions and other work product searchable the way public decisions are, with the same reader, citations and statute links. Every result is labelled internal or public.", "Nothing internal is held. The reader, citation extraction and statute linking already work on any decision text.", "Agency network access and sign-in, an on-premises deployment, and approval from information security and privacy."),
			("Agency repositories and private ID decisions", "concept", "Private Immigration Division and Appeal Division decisions, and existing agency repositories, shown beside public cases.", "Nothing is held.", "Agency data and a way to bring it in."),
			("Argument identification on your own file", "partly", "Open a memo or brief and see the authorities it cites, with statute references and how each has been treated.", "Live Analysis in the Workbench does the citation and statute part today. It reads the file in memory and keeps nothing. Argument identification is not built.", "A decision on how arguments are identified without sending text outside the agency."),
			("Same tools as public cases", "concept", "Internal text read and tagged with the same rule-based tools as public decisions, with every link going back to the source paragraph.", "The tools exist for public decisions.", "Defining which document types are in scope."),
		],
	),
	"intelligence": (
		"Increased intelligence",
		"Features that read the decisions, not just list them.",
		"These features go from finding a case to understanding how cases relate and how arguments are made. Where AI would help, it is optional, runs only on an on-premises model, and its output is stored as data that links back to the source paragraph.",
		[
			("Citation treatment", "concept", "Show how a later case treated an earlier one: followed, distinguished, doubted.", "Prepared offline on a small labelled sample. Nothing is shown on the site.", "A human-reviewed set of examples before anything goes live."),
			("AI-backed citation enhancements", "concept", "Optional help on top of the rule-based citation links, such as the reason a case was cited.", "Not built. Any AI would run on the on-premises model described under Local private AI.", "That model, and the reviewed examples above."),
			("Discussion units, arguments and themes", "partly", "Split a decision into its argument sections and group them by theme, so a reader can jump to the analysis of one issue.", "A rule-based version exists as a report and a testing page. It is not stored in the library.", "Human review of its boundaries, then storing it."),
			("Citation neighbourhoods", "partly", "Start from one case and see what it cites, what cites it and which authorities it shares with another case.", "The Citation Map page works today in Development.", "Cleaner citation links."),
			("Case fingerprints and similar cases", "partly", "A short profile of what a case is about, used to find similar cases.", "Prototyped and tested on samples. Not on the site.", "A decision on which features go into the fingerprint."),
		],
	),
	"team": (
		"Team features",
		"Working on cases together.",
		"Today the site has no accounts: everyone sees the same thing and nothing is saved per person. Team features would change that.",
		[
			("Accounts", "planned", "Individual sign-in, so searches and notes belong to a person. On an agency network it would use the agency’s own accounts.", "None. The site has no sign-in.", "A deployment where sign-in makes sense."),
			("Teams", "planned", "Shared collections of cases and searches, with permissions for a unit.", "None.", "Accounts."),
			("Annotations in cases", "planned", "Notes and highlights on a decision, private to you or shared with your team.", "None. The Markup Reader in Development is a layout study, not saved notes.", "Accounts, and a place to store notes."),
			("Workbench and alerts", "partly", "A workspace for tools, and saved searches that flag new matching decisions.", "A first Workbench and a saved-searches page exist. Alerts are partly built.", "Accounts, so saved items belong to someone."),
		],
	),
	"local-ai": (
		"Local private AI",
		"Optional AI that runs only on the agency’s own computers.",
		"Concept only. It assumes the agency can run its own AI model on its own hardware, which does not exist yet. Normal search never uses AI, and nothing a person types is sent to an outside service.",
		[
			("On-premises model", "concept", "A language model running on agency computers, used only for the optional features on this page.", "Not set up.", "Agency hardware and approval."),
			("Embeddings and smart search", "concept", "Search by meaning as well as by words, using stored embeddings of paragraphs.", "Paused. A table exists but no embeddings are live.", "The on-premises model and a decision to resume."),
			("Data safety", "concept", "Nothing leaves the building: no internal text, question or upload goes to an outside service. Sign-in uses agency accounts.", "Today the site’s own uploads are read in memory and not stored.", "Security and privacy approval for a real deployment."),
			("AI work stored as data", "concept", "Where AI helps, it runs when documents are added, and the result is saved with a link to the source paragraph, so the site itself stays AI-free.", "Not built.", "The on-premises model."),
		],
	),
}

# Overview tab first, then the sections in the order the owner asked for.
ORDER = ["overview", "accuracy", "expansion", "internal", "intelligence", "team", "local-ai"]
LABELS = {"overview": "Overview", **{key: value[0] for key, value in SECTIONS.items()}}

_CSS = """:root{--surface:#fffef9;--alt:#f8f6ef;--border:#d8d5ca;--text:#202522;--muted:#5f6863;--blue:#315d8d;--blue-soft:#e7eef6;--teal:#176c68;--teal-soft:#edf5f3;--amber:#8a6418;--amber-soft:#f8f0dc;--serif:"Newsreader",Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:#efede4;color:var(--text);font:14px/1.55 "IBM Plex Sans",system-ui,sans-serif}
.wrap{max-width:860px;margin:0 auto;padding:6px 20px 48px}
.eyebrow{margin:24px 0 6px;color:var(--teal);font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
h1{margin:0;font:600 30px/1.15 var(--serif)}.intro{max-width:68ch;font-size:15.5px;margin:12px 0}
h2{margin:0;font:600 20px/1.25 var(--serif)}
.tag{display:inline-block;padding:2px 10px;border-radius:999px;font-size:11px;font-weight:700;white-space:nowrap}
.s-built{background:var(--teal-soft);color:var(--teal)}.s-partly,.s-progress{background:var(--blue-soft);color:var(--blue)}.s-planned{background:var(--amber-soft);color:var(--amber)}.s-concept{background:#ecebe4;color:var(--muted)}
.legend{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:12px 0;font-size:12.5px;color:var(--muted)}
.note{margin:16px 0;padding:12px 16px;border:1px solid var(--text);border-radius:6px;background:var(--alt);font-size:14px}
.item{margin-top:26px;padding-top:20px;border-top:1px solid var(--border)}.ihead{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.item p.what{max-width:68ch;margin:8px 0 10px;font-size:15px}
dl{display:grid;grid-template-columns:130px 1fr;gap:6px 14px;margin:0;font-size:13.5px}dt{color:var(--muted);font-size:11px;letter-spacing:.07em;text-transform:uppercase;padding-top:2px}dd{margin:0}
table{width:100%;border-collapse:collapse;margin-top:12px;background:var(--surface);border:1px solid var(--border);font-size:13.5px}th{padding:8px 10px;text-align:left;font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);border-bottom:1px solid var(--border)}td{padding:9px 10px;border-bottom:1px solid #ecebe4;vertical-align:top}
a{color:var(--blue)}
@media(max-width:640px){dl{grid-template-columns:1fr}h1{font-size:26px}.wrap{padding:0 14px 40px}}
"""

_NOTE = "<b>The rule behind all of it.</b> Normal search uses no AI, and nothing a person types is sent to an outside AI service. Where AI would help, it runs on an on-premises model or when cases are added, and its work is stored as data linked to the source paragraph."


def _tag(status: str) -> str:
	return f'<span class="tag s-{status}">{STATUSES[status]}</span>'


def _legend() -> str:
	return '<div class="legend">' + " ".join(_tag(key) for key in STATUSES) + "<span>Concept means an idea only; nothing is built.</span></div>"


def _frame(title: str, body: str) -> str:
	return (
		'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
		f"<title>iLit: coming soon, {html.escape(title)}</title>"
		'<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,600&display=swap" rel="stylesheet">'
		f"<style>{_CSS}</style></head><body><main class=\"wrap\">{body}</main></body></html>"
	)


def _link(slug: str, text: str) -> str:
	return f'<a href="/data-explorer?tab=roadmap-{slug}&amp;group=roadmap" target="_top">{html.escape(text)}</a>'


def render(slug: str) -> str | None:
	if slug == "overview":
		rows = ""
		for key in ORDER[1:]:
			label, summary, _intro, items = SECTIONS[key]
			counts = " ".join(
				f"{_tag(status)} {sum(1 for item in items if item[1] == status)}" for status in STATUSES if any(item[1] == status for item in items)
			)
			rows += f"<tr><td><b>{_link(key, label)}</b><br>{html.escape(summary)}</td><td>{counts}</td></tr>"
		body = (
			'<p class="eyebrow">Coming soon</p><h1>Where iLit is going next</h1>'
			'<p class="intro">Six areas of work, from correcting what is already in the library to features that do not exist yet. Each has its own tab above, with what it is, where it stands and what it needs. Pieces that already run but are not ready to rely on are under Development.</p>'
			f'<div class="note">{_NOTE}</div>{_legend()}'
			f'<table><thead><tr><th>Section</th><th>Where it stands</th></tr></thead><tbody>{rows}</tbody></table>'
		)
		return _frame("overview", body)
	section = SECTIONS.get(slug)
	if not section:
		return None
	label, _summary, intro, items = section
	parts = ""
	for title, status, what, stands, needs in items:
		parts += (
			f'<section class="item"><div class="ihead"><h2>{html.escape(title)}</h2>{_tag(status)}</div>'
			f'<p class="what">{html.escape(what)}</p><dl><dt>Where it stands</dt><dd>{html.escape(stands)}</dd><dt>What it needs</dt><dd>{html.escape(needs)}</dd></dl></section>'
		)
	body = f'<p class="eyebrow">Coming soon</p><h1>{html.escape(label)}</h1><p class="intro">{html.escape(intro)}</p>{_legend()}{parts}'
	return _frame(label, body)
