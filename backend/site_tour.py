"""The "Take a tour" walkthrough: a small self-contained script, style sheet and step list.

The steps are plain data in ``pages/site_tour_steps.json``. ``/site-tour.js`` serves the steps and the
script together, ``/site-tour.css`` the styles; ``inject_site_tour`` adds both to a page. The tour only
points at the real site; it makes no AI calls and no outside requests, and writes nothing unless a step
has a button that says so.
"""

from __future__ import annotations

import hashlib
import json
from functools import lru_cache
from pathlib import Path

_PAGES = Path(__file__).resolve().parent / "pages"


@lru_cache(maxsize=1)
def tour_steps() -> dict:
    return json.loads((_PAGES / "site_tour_steps.json").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def tour_css() -> str:
    return (_PAGES / "site_tour.css").read_text(encoding="utf-8")


@lru_cache(maxsize=1)
def tour_js() -> str:
    data = {key: value for key, value in tour_steps().items() if not key.startswith("_")}
    # "</" never appears in the payload as written, but escape it so no step text can end a script early.
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    script = (_PAGES / "site_tour.js").read_text(encoding="utf-8")
    return f"window.ILIT_TOUR={payload};\n{script}"


@lru_cache(maxsize=1)
def tour_version() -> str:
    return hashlib.sha1((tour_js() + tour_css()).encode("utf-8")).hexdigest()[:10]


def inject_site_tour(html: str) -> str:
    """Add the tour's style sheet and script to a page (once)."""
    if "/site-tour.js" in html:
        return html
    version = tour_version()
    html = html.replace("</head>", f'<link rel="stylesheet" href="/site-tour.css?v={version}">\n</head>', 1)
    return html.replace("</body>", f'<script src="/site-tour.js?v={version}" defer></script>\n</body>', 1)
