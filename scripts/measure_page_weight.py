#!/usr/bin/env python3
"""Measure every HTML page template offline and write a Markdown baseline."""

from __future__ import annotations

import argparse
import gzip
from html.parser import HTMLParser
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "docs" / "reports" / "page-weight-baseline.md"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.case_reader_ui import (  # noqa: E402
    case_reader_with_statutes_html,
    statute_viewer_page_html as legacy_statute_viewer_page_html,
)
from backend.discussion_units_sandbox import (  # noqa: E402
    discussion_units_sandbox_page_html as sandbox_page_html,
)
from backend.main import _login_page  # noqa: E402
from backend.pages.citation_map import citation_map_html  # noqa: E402
from backend.pages.citation_pass import citation_pass_page_html  # noqa: E402
from backend.pages.data_explorer import data_explorer_page_html  # noqa: E402
from backend.pages.deidentify import deidentify_page_html  # noqa: E402
from backend.pages.discussion_units_sandbox import (  # noqa: E402
    discussion_units_sandbox_page_html as standalone_sandbox_page_html,
)
from backend.pages.issue_brief import issue_brief_page_html  # noqa: E402
from backend.pages.judge_outcomes import judge_outcomes_page_html  # noqa: E402
from backend.pages.live_analysis import live_analysis_page_html  # noqa: E402
from backend.pages.memo_citation_check import memo_citation_check_page_html  # noqa: E402
from backend.pages.prototype import prototype_page_html  # noqa: E402
from backend.pages.quick_search import quick_search_page_html  # noqa: E402
from backend.pages.research import research_page_html  # noqa: E402
from backend.pages.saved_searches import saved_searches_page_html  # noqa: E402
from backend.pages.statute_viewer import (  # noqa: E402
    statute_viewer_page_html as page_statute_viewer_page_html,
)
from backend.pages.tag_finder import tag_finder_page_html  # noqa: E402
from backend.pages.testing import testing_page_html  # noqa: E402
from backend.pages.theme_explorer import theme_explorer_page_html  # noqa: E402
from backend.routes import (  # noqa: E402
    _data_explorer_page_html,
    _quick_search_page_html,
    _research_page_html,
)


RESOURCE_ATTRIBUTES = {
    "audio": {"src"},
    "embed": {"src"},
    "iframe": {"src"},
    "img": {"src", "srcset"},
    "input": {"src"},
    "link": {"href"},
    "object": {"data"},
    "script": {"src"},
    "source": {"src", "srcset"},
    "track": {"src"},
    "video": {"poster", "src"},
}
RESOURCE_LINK_RELATIONS = {
    "alternate",
    "icon",
    "manifest",
    "modulepreload",
    "preload",
    "stylesheet",
}
CSS_URL = re.compile(r"""url\(\s*['"]?([^)'"]+)""", re.IGNORECASE)
CSS_IMPORT = re.compile(r"""@import\s+['"]([^'"]+)""", re.IGNORECASE)


class _PageMetricsParser(HTMLParser):
    """Collect inline code bytes and declared external resource references."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.inline_script_bytes = 0
        self.inline_style_bytes = 0
        self.external_requests: list[str] = []
        self._capture: str | None = None
        self._captured: list[str] = []

    @staticmethod
    def _external(url: str) -> bool:
        url = url.strip()
        if not url or url.startswith("#"):
            return False
        scheme = urlsplit(url).scheme.lower()
        return scheme not in {"data", "blob", "javascript", "mailto", "tel"}

    def _add_external(self, url: str) -> None:
        if self._external(url):
            self.external_requests.append(url.strip())

    def _add_srcset(self, value: str) -> None:
        for candidate in value.split(","):
            self._add_external(candidate.strip().split(" ", 1)[0])

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {name.lower(): value or "" for name, value in attrs}
        if tag == "script" and "src" not in attributes:
            self._capture, self._captured = "script", []
        elif tag == "style":
            self._capture, self._captured = "style", []

        resource_attrs = RESOURCE_ATTRIBUTES.get(tag, set())
        if tag == "link":
            relations = set(attributes.get("rel", "").lower().split())
            if not relations.intersection(RESOURCE_LINK_RELATIONS):
                resource_attrs = set()
        for name in resource_attrs:
            if name not in attributes:
                continue
            if name == "srcset":
                self._add_srcset(attributes[name])
            else:
                self._add_external(attributes[name])

        style = attributes.get("style", "")
        self.inline_style_bytes += len(style.encode("utf-8"))
        self._scan_css(style)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._captured.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._capture == tag:
            inline_bytes = len("".join(self._captured).encode("utf-8"))
            if tag == "script":
                self.inline_script_bytes += inline_bytes
            else:
                self.inline_style_bytes += inline_bytes
            if tag == "style":
                self._scan_css("".join(self._captured))
            self._capture, self._captured = None, []

    def _scan_css(self, css: str) -> None:
        for pattern in (CSS_URL, CSS_IMPORT):
            for match in pattern.finditer(css):
                self._add_external(match.group(1))


def measure_page(name: str, source: str, build_html: Callable[[], str]) -> dict[str, Any]:
    """Build a deterministic fixture page and measure its delivered HTML."""
    html = build_html()
    if not isinstance(html, str):
        raise TypeError(f"{source} returned {type(html).__name__}, not HTML text")
    html_bytes = html.encode("utf-8")
    gzip_bytes = gzip.compress(html_bytes, compresslevel=6, mtime=0)
    parser = _PageMetricsParser()
    parser.feed(html)
    parser.close()
    return {
        "name": name,
        "source": source,
        "status": "ok",
        "size_bytes": len(html_bytes),
        "gzip_bytes": len(gzip_bytes),
        "inline_script_bytes": parser.inline_script_bytes,
        "inline_style_bytes": parser.inline_style_bytes,
        "external_request_count": len(parser.external_requests),
    }


def _builders() -> list[tuple[str, str, Callable[[], str]]]:
    """The full template inventory; dynamic builders get safe fixed fixtures."""
    empty_brief: dict[str, Any] = {"tag": "fixture", "decision_count": 0, "decisions": []}
    return [
        ("access_login", "backend.main._login_page", lambda: _login_page().body.decode("utf-8")),
        ("case_reader", "backend.case_reader_ui.case_reader_with_statutes_html", lambda: case_reader_with_statutes_html(
            case_id=1,
            case_title="Fixture Case",
            case_citation="2026 FC 1",
            case_date="2026-01-01",
            case_court="Federal Court",
            case_summary="Deterministic page-weight fixture.",
        )),
        ("citation_map", "backend.pages.citation_map.citation_map_html", citation_map_html),
        ("citation_pass", "backend.pages.citation_pass.citation_pass_page_html", citation_pass_page_html),
        ("data_explorer", "backend.pages.data_explorer.data_explorer_page_html", data_explorer_page_html),
        ("data_explorer_route_builder", "backend.routes._data_explorer_page_html", _data_explorer_page_html),
        ("deidentify", "backend.pages.deidentify.deidentify_page_html", deidentify_page_html),
        ("discussion_sandbox", "backend.discussion_units_sandbox.discussion_units_sandbox_page_html", sandbox_page_html),
        ("discussion_sandbox_standalone", "backend.pages.discussion_units_sandbox.discussion_units_sandbox_page_html", standalone_sandbox_page_html),
        ("issue_brief_empty_fixture", "backend.pages.issue_brief.issue_brief_page_html", lambda: issue_brief_page_html(empty_brief)),
        ("judge_outcomes", "backend.pages.judge_outcomes.judge_outcomes_page_html", judge_outcomes_page_html),
        ("live_analysis", "backend.pages.live_analysis.live_analysis_page_html", live_analysis_page_html),
        ("memo_citation_check", "backend.pages.memo_citation_check.memo_citation_check_page_html", memo_citation_check_page_html),
        ("prototype", "backend.pages.prototype.prototype_page_html", prototype_page_html),
        ("quick_search", "backend.pages.quick_search.quick_search_page_html", quick_search_page_html),
        ("quick_search_route_builder", "backend.routes._quick_search_page_html", _quick_search_page_html),
        ("research", "backend.pages.research.research_page_html", research_page_html),
        ("research_route_builder", "backend.routes._research_page_html", _research_page_html),
        ("saved_searches", "backend.pages.saved_searches.saved_searches_page_html", saved_searches_page_html),
        ("statute_viewer_legacy", "backend.case_reader_ui.statute_viewer_page_html", legacy_statute_viewer_page_html),
        ("statute_viewer_page", "backend.pages.statute_viewer.statute_viewer_page_html", page_statute_viewer_page_html),
        ("tag_finder", "backend.pages.tag_finder.tag_finder_page_html", tag_finder_page_html),
        ("testing", "backend.pages.testing.testing_page_html", testing_page_html),
        ("theme_explorer", "backend.pages.theme_explorer.theme_explorer_page_html", theme_explorer_page_html),
    ]


def render_report(measurements: list[dict[str, Any]]) -> str:
    """Render the required Markdown baseline from measured values."""
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    rows = [
        "# Page weight baseline",
        "",
        f"Generated: {timestamp}",
        "",
        "All HTML is produced offline by calling the listed builder directly. "
        "Argument-taking builders use fixed, non-sensitive fixtures; no database, "
        "server, browser, or external network access is used. UTF-8 byte counts "
        "measure the complete returned HTML; gzip uses level 6 with a fixed "
        "timestamp. Inline byte columns count script/style text only (excluding "
        "tags, including style attributes). External requests count non-inline "
        "resource references declared by "
        "resource attributes and CSS `url()`/`@import`; duplicate references are "
        "counted individually. This is a template inventory, not a runtime waterfall.",
        "",
        "| Page / fixture | Builder | Raw HTML (bytes) | Gzip (bytes) | Inline script (bytes) | Inline style (bytes) | External requests |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for page in measurements:
        rows.append(
            f"| {page['name']} | `{page['source']}` | {page['size_bytes']} | "
            f"{page['gzip_bytes']} | {page['inline_script_bytes']} | "
            f"{page['inline_style_bytes']} | {page['external_request_count']} |"
        )
    rows.extend(
        [
            "",
            f"Measured builders: {len(measurements)}; skipped: 0.",
            "",
            "## Static asset serving",
            "",
            "Data Explorer's `explorer_snapshots.css` and `.js` are served from "
            "the `/static/` mount with `Cache-Control: public, max-age=3600`. "
            "Starlette `FileResponse` supplies ETag and Last-Modified validators. "
            "No-store and attachment responses remain excluded.",
            "",
        ]
    )
    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Markdown baseline path (default: docs/reports/page-weight-baseline.md)",
    )
    output = parser.parse_args().output
    measurements = [
        measure_page(name, source, build_html) for name, source, build_html in _builders()
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(measurements), encoding="utf-8")
    print(f"Measured {len(measurements)} HTML builders; skipped: 0.")
    print(f"Markdown baseline written to: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
