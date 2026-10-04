"""Small shared help fragment for existing research headers."""


def research_help_html() -> str:
    return '<a class="research-help" href="/start" aria-label="Help: start a research task" title="Start a research task" style="display:inline-block;padding:6px 12px;border:1px solid currentColor;border-radius:50%;font-weight:bold;text-decoration:none">?</a>'


def inject_research_help(html: str) -> str:
    return html.replace("</header>", research_help_html() + "</header>", 1)
