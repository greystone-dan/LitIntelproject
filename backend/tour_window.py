"""The "Take a tour" window: a recorded walk through the real site.

The tour plays from pictures of the live site taken once, with the highlights, the pointer and the
cards drawn on top. Every step (its words, highlight boxes, card position, pointer path and which
picture to show) is plain data in ``site_assets/tour_window/tour_data.json`` (the recorded screens sit
beside it in ``img/``). The window reads only that data and those pictures: no database query, no
outside request, no AI call, and nothing is written. The visitor only presses Next, Back or Exit.
``/tour-window.js`` is the small script that opens the window over any page; the window itself is the
page at ``/tour-window/``. After a re-capture, bump ``config.version`` in the data so browsers fetch the
new pictures.
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

_PAGES = Path(__file__).resolve().parent / "pages"
_ASSETS = Path(__file__).resolve().parent.parent / "site_assets" / "tour_window"
_IMAGE_NAME = re.compile(r"^[A-Za-z0-9_]+\.webp$")


@lru_cache(maxsize=1)
def window_html() -> str:
    return (_PAGES / "tour_window.html").read_text(encoding="utf-8")


@lru_cache(maxsize=1)
def window_data() -> str:
    from .judge_feature import filter_window_data, judge_profiles_enabled

    text = (_ASSETS / "tour_data.json").read_text(encoding="utf-8")
    return text if judge_profiles_enabled() else json.dumps(filter_window_data(json.loads(text)), ensure_ascii=False)


@lru_cache(maxsize=1)
def window_steps() -> list[dict]:
    return json.loads(window_data())["moments"]


@lru_cache(maxsize=1)
def window_loader() -> str:
    return (_PAGES / "tour_window_loader.js").read_text(encoding="utf-8")


def window_image(name: str) -> bytes | None:
    """One recorded screen, or None for a name that is not a plain .webp in the tour's own folder."""
    if not _IMAGE_NAME.match(name):
        return None
    path = _ASSETS / "img" / name
    return path.read_bytes() if path.is_file() else None


def referenced_images() -> set[str]:
    """Every picture the data names (used by the tests to catch a missing or an unused file)."""
    data = json.loads(window_data())
    names = {data["config"]["intro"]["frame"]}
    for step in data["moments"]:
        names.add(step["final"])
        for action in step["actions"]:
            names.update([action["src"]] if "src" in action else [])
            names.update(action.get("frames", []))
    return {Path(name).name for name in names}
