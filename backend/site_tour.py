"""The "Take a tour" button: ``inject_site_tour`` adds the small opener script to a page, and the tour plays in
the recorded window (see ``tour_window.py``).

The old live tour (``/site-tour.js``, ``/site-tour.css`` and its step list in ``pages/site_tour_steps.json``) is no
longer put on any page. Its files stay for now because the demo-memo cache in Live analysis still reads the sample
text and the sample Word file from here; they can be removed in a follow-up.
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


def is_tour_sample(text: str) -> bool:
    """True only for the tour's own fictional demo document, the one pasted text the server may cache."""
    return any(" ".join(text.split()) == " ".join(sample.split()) for sample in tour_steps().get("texts", {}).values())


SAMPLE_DOCX_NAME = "Memorandum of Argument (fictional).docx"


@lru_cache(maxsize=1)
def tour_sample_docx() -> bytes:
    """The tour's fictional Memorandum of Argument as a Word file, dropped on Live analysis like a real upload."""
    return (_PAGES / "site_tour_sample_moa.docx").read_bytes()


def is_tour_sample_file(content: bytes) -> bool:
    return content == tour_sample_docx()


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
def tour_window_version() -> str:
    from .tour_window import window_loader

    return hashlib.sha1(window_loader().encode("utf-8")).hexdigest()[:10]


@lru_cache(maxsize=1)
def tour_version() -> str:
    return hashlib.sha1((tour_js() + tour_css()).encode("utf-8")).hexdigest()[:10]


def inject_site_tour(html: str) -> str:
    """Add the tour window's opener script to a page (once). The tour itself plays in /tour-window/."""
    if "/tour-window.js" in html:
        return html
    version = tour_window_version()
    return html.replace("</body>", f'<script src="/tour-window.js?v={version}" defer></script>\n</body>', 1)
