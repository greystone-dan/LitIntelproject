"""Additive active-reader controls; the existing formatter and list stay intact."""

from pathlib import Path


def inject_paragraph_citation_counts(html: str) -> str:
    here = Path(__file__).resolve().parent
    controls = (
        '<div class="reader-paragraph-count-controls">'
        '<button type="button" class="reader-evidence-toggle" id="readerParagraphCountsToggle" '
        'aria-pressed="false" aria-controls="decisionBody" disabled>Show most-cited paragraphs</button>'
        '<p id="readerParagraphCountsCoverage" role="status" aria-live="polite"></p></div>'
    )
    html = html.replace('<details id="readerMostCited"', controls + '<details id="readerMostCited"', 1)
    css = (here / "paragraph_citation_counts.css").read_text(encoding="utf-8")
    js = (here / "paragraph_citation_counts.js").read_text(encoding="utf-8")
    html = html.replace("</head>", "<style>\n" + css + "</style>\n</head>", 1)
    return html.replace("</body>", "<script>\n" + js + "</script>\n</body>", 1)
