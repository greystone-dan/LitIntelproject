"""Browser-independent responsive contract checks for generated HTML pages."""

from html.parser import HTMLParser
import os
from pathlib import Path
import re

from backend.pages.citation_map import citation_map_html
from backend.pages.citation_pass import citation_pass_page_html
from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.deidentify import deidentify_page_html
from backend.pages.discussion_units_sandbox import discussion_units_sandbox_page_html
from backend.pages.issue_brief import issue_brief_page_html
from backend.pages.judge_outcomes import judge_outcomes_page_html
from backend.pages.live_analysis import live_analysis_page_html
from backend.pages.memo_citation_check import memo_citation_check_page_html
from backend.pages.prototype import prototype_page_html
from backend.pages.quick_search import quick_search_page_html
from backend.pages.research import research_page_html
from backend.pages.saved_searches import saved_searches_page_html
from backend.pages.statute_viewer import statute_viewer_page_html
from backend.pages.tag_finder import tag_finder_page_html
from backend.pages.testing import testing_page_html
from backend.pages.theme_explorer import theme_explorer_page_html


def _issue_brief():
    return issue_brief_page_html(
        {
            "tag": "issue:responsive_test",
            "decision_count": 1,
            "decisions": [{"citation": "2025 FC 1", "court": "Federal Court"}],
            "years": [{"year": 2025, "decision_count": 1, "outcome_splits": []}],
            "courts": [{"court": "Federal Court", "decision_count": 1}],
            "top_authorities": [{"citation": "2024 FC 2", "citation_occurrences": 1}],
            "semantics": {},
        }
    )


PAGES = {
    "citation_map": (citation_map_html, ".shell"),
    "citation_pass": (citation_pass_page_html, ".main-grid"),
    "data_explorer": (data_explorer_page_html, ".workspace"),
    "deidentify": (deidentify_page_html, ".cols"),
    "discussion_units_sandbox": (discussion_units_sandbox_page_html, ".results"),
    "issue_brief": (_issue_brief, ".grid"),
    "judge_outcomes": (judge_outcomes_page_html, ".shell"),
    "live_analysis": (live_analysis_page_html, ".wrap"),
    "memo_citation_check": (memo_citation_check_page_html, ".wrap"),
    "prototype": (prototype_page_html, ".grid"),
    "quick_search": (quick_search_page_html, ".wrap"),
    "research": (research_page_html, ".grid2"),
    "saved_searches": (saved_searches_page_html, ".saved-search-head"),
    "statute_viewer": (statute_viewer_page_html, ".shell"),
    "tag_finder": (tag_finder_page_html, ".input-row"),
    "testing": (testing_page_html, ".search-layout"),
    "theme_explorer": (theme_explorer_page_html, ".main"),
}

VOID_ELEMENTS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class _PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.viewport = False
        self.styles = []
        self._in_style = False
        self._stack = []
        self.table_wrappers = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "meta" and attributes.get("name", "").lower() == "viewport":
            self.viewport = True
        if tag == "style":
            self._in_style = True
            self.styles.append("")
        if tag == "table":
            self.table_wrappers.append(
                [
                    (parent_tag, parent_attrs)
                    for parent_tag, parent_attrs in self._stack
                    if parent_attrs.get("class")
                ]
            )
        if tag not in VOID_ELEMENTS:
            self._stack.append((tag, attributes))

    def handle_endtag(self, tag):
        if tag == "style":
            self._in_style = False
        for index in range(len(self._stack) - 1, -1, -1):
            if self._stack[index][0] == tag:
                del self._stack[index:]
                break

    def handle_data(self, data):
        if self._in_style and self.styles:
            self.styles[-1] += data


def _media_blocks(css):
    offset = 0
    while match := re.search(r"@media\s*([^{]+)\{", css[offset:], re.IGNORECASE):
        start = offset + match.start()
        opening = offset + match.end() - 1
        depth = 0
        for end in range(opening, len(css)):
            if css[end] == "{":
                depth += 1
            elif css[end] == "}":
                depth -= 1
                if depth == 0:
                    break
        yield match.group(1).strip(), css[opening + 1 : end]
        offset = end + 1


def _rules(css):
    return re.findall(r"([^{}]+)\{([^{}]*)\}", css)


def test_generated_pages_keep_mobile_responsive_layout_contracts():
    for name, (builder, layout_selector) in PAGES.items():
        html = builder()
        parser = _PageParser()
        parser.feed(html)
        css = "\n".join(parser.styles)

        assert parser.viewport, f"{name} is missing viewport metadata"

        responsive_blocks = [
            (query, body)
            for query, body in _media_blocks(css)
            if re.search(r"max-width\s*:\s*\d+px", query, re.IGNORECASE)
        ]
        assert responsive_blocks, f"{name} has no width-based media query"
        assert any(layout_selector in body for _, body in responsive_blocks), (
            f"{name} does not adapt its {layout_selector} layout in a media query"
        )

        for selector, declarations in _rules(css):
            if re.search(r"min-width\s*:\s*(\d+)px", declarations, re.IGNORECASE):
                value = int(re.search(r"min-width\s*:\s*(\d+)px", declarations, re.IGNORECASE).group(1))
                if value > 360:
                    table_rule = re.search(r"\btable\b", selector, re.IGNORECASE)
                    assert table_rule, (
                        f"{name} has a non-table container minimum width of {value}px: {selector.strip()}"
                    )

        overflow_selectors = [
            selector
            for selector, declarations in _rules(css)
            if re.search(r"overflow-x\s*:\s*auto", declarations, re.IGNORECASE)
        ]
        for ancestors in parser.table_wrappers:
            wrapper_keys = {
                key
                for _, attrs in ancestors
                for key in [
                    *(f".{class_name}" for class_name in attrs.get("class", "").split()),
                    *(f"#{element_id}" for element_id in attrs.get("id", "").split()),
                ]
            }
            assert any(
                key in selector
                for selector in overflow_selectors
                for key in wrapper_keys
            ), f"{name} has a table without an overflow-x:auto wrapper"


def test_dynamic_table_renderers_include_horizontal_scroll_wrappers():
    citation_pass = citation_pass_page_html()
    assert 'class=\\"table-wrap\\"' in citation_pass

    prototype = prototype_page_html()
    assert 'class="table-wrap"><table>' in prototype

    data_explorer = data_explorer_page_html()
    assert "overflow-x:auto" in data_explorer
    assert "class=\"table-wrap\"" in data_explorer

    # The analytics tabs use DOM-built tables rather than literal table markup.
    assert "class:'fcx-scroll'" in data_explorer
    assert "class:'table-wrap'" in data_explorer


def test_optional_responsive_browser_screenshots():
    """Capture every generated page at target widths when local Chromium exists."""
    import pytest

    browser_root = Path("/opt/pw-browsers")
    if not browser_root.is_dir():
        pytest.skip("optional Chromium browser directory /opt/pw-browsers is absent")
    executables = sorted(
        path
        for name in ("chrome", "chromium")
        for path in browser_root.rglob(name)
        if path.is_file() and os.access(path, os.X_OK)
    )
    if not executables:
        pytest.skip("no executable Chromium binary found under /opt/pw-browsers")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        pytest.skip("Playwright is not installed; no browser dependency is added")

    output_dir = Path("docs/reports/responsive")
    output_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            executable_path=str(executables[0]), headless=True, args=["--no-sandbox"]
        )
        try:
            page = browser.new_page()
            for name, (builder, _) in PAGES.items():
                html = builder()
                for width in (360, 768, 1280):
                    page.set_viewport_size({"width": width, "height": 900})
                    page.set_content(html, wait_until="domcontentloaded")
                    page.screenshot(
                        path=str(output_dir / f"{name}-{width}.png"),
                        full_page=True,
                    )
        finally:
            browser.close()
