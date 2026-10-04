"""Task-first entry points; examples use existing inputs, never invented IDs."""

from html import escape

from .research_header import research_help_html


TASKS = (
    ("Find a case",
     "Search a case name or citation, open a result, and check its identity and source before relying on it.",
     "/data-explorer?tab=search", "/data-explorer?tab=search&query=2019%20SCC%2065", "Try 2019 SCC 65"),
    ("See how the Federal Court ruled on an issue",
     "Search full decision text for an issue, then read the decisions yourself rather than treating outcome labels as legal conclusions.",
     "/data-explorer?tab=search", "/data-explorer?tab=search&query=procedural%20fairness&court=FC&search_full_text=true", "Try procedural fairness with the FC filter"),
    ("Check a memo's citations",
     "Analyze a DOCX or text PDF for local authority matches and context leads, then verify them against the decisions.",
     "/memo-citation-check", "/memo-citation-check?example=vavilov", "Load a sample memo for analysis"),
    ("Look at a judge's record",
     "Search a judge by name to find linked decisions and recorded outcomes, not to infer bias or complete judicial coverage.",
     "/data-explorer?tab=judge-profile", "/data-explorer?tab=judge-profile&judge_query=Zinn", "Try judge name Zinn"),
    ("Export results",
     "Run a case search, then download its results as CSV or use Download Word after a successful nonempty search.",
     "/data-explorer?tab=search", "/data-explorer?tab=search&query=Vavilov", "Try a Vavilov search before exporting"),
)


def start_page_html() -> str:
    cards = "".join(
        f'<article class="task-card"><h2>{escape(title)}</h2><p>{escape(description)}</p>'
        f'<a class="task-button" href="{escape(route, quote=True)}">Open task</a> '
        f'<a class="task-example" href="{escape(example, quote=True)}">{escape(label)}</a></article>'
        for title, description, route, example, label in TASKS
    )
    return f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Start a research task | iLit</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#f5f7fb;color:#102038;font:16px/1.6 system-ui,sans-serif}}
header,main{{max-width:1100px;margin:auto;padding:24px}}header{{display:flex;gap:24px;align-items:center}}
main{{padding-top:0}}.tasks{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}}
.task-card{{background:white;border:1px solid #cbd5e1;border-radius:12px;padding:22px}}
h2{{font-size:1.2rem}}a{{color:#1e40af}}.task-button{{display:inline-block;padding:8px 14px;background:#1e3a8a;color:white;border-radius:6px;margin:0 8px 12px 0}}
:focus-visible{{outline:3px solid #b45309;outline-offset:3px}}
</style></head><body><header><strong>iLit</strong><a href="/data-explorer">Research</a>{research_help_html()}</header>
<main><h1>Start a research task</h1><p>Choose a task or try an example. Example searches are prefilled, not submitted; matches depend on the stored library.</p>
<div class="tasks">{cards}</div><p>iLit is a research aid, not a legal citator, official court record, or legal advice. Check important findings against authoritative sources. Stored mentions do not establish that an authority is good law.</p>
</main></body></html>"""
