"""Static contracts for the complete standalone generated page builders.

The list inventories complete documents, including private access and the
discussion-unit route variant. ``fc_analytics`` and ``tag_analytics`` are HTML
fragment injectors called by Data Explorer, not standalone documents; their
rendered fragments are included in the Data Explorer shell check. Thin route
wrappers return these inventoried page outputs.

Image-alt coverage intentionally overlaps PR #136's generic check, which is
absent from this worktree. If #136 merges, consolidate the shared skip-link
helper and this overlapping alt assertion at that convergence point; do not
bring over its unrelated live-region, table, focus, or ARIA changes here.
There is no image-alt allow-list.
"""

from html.parser import HTMLParser

from backend.case_reader_ui import (
    case_reader_with_statutes_html,
    statute_viewer_page_html as case_reader_statute_viewer_page_html,
)
from backend.pages.case_compare import case_compare_page_html
from backend.pages.access_gate import access_login_page_html
from backend.pages.accessibility_statement import accessibility_page_html
from backend.pages.citation_map import citation_map_html
from backend.pages.citation_pass import citation_pass_page_html
from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.discussion_units_sandbox_route import (
    discussion_units_sandbox_page_html as discussion_units_route_page_html,
)
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
from backend.pages.skip_link import ensure_skip_link


PAGE_BUILDERS = (
    ("access_login_page_html", access_login_page_html),
    ("accessibility_page_html", accessibility_page_html),
    ("case_compare_page_html", case_compare_page_html),
    ("citation_map_html", citation_map_html),
    ("citation_pass_page_html", citation_pass_page_html),
    ("data_explorer_page_html", data_explorer_page_html),
    ("deidentify_page_html", deidentify_page_html),
    ("discussion_units_sandbox_page_html", discussion_units_sandbox_page_html),
    ("discussion_units_route_page_html", discussion_units_route_page_html),
    (
        "issue_brief_page_html",
        lambda: issue_brief_page_html({"tag": "issue:test", "decision_count": 0, "decisions": []}),
    ),
    ("judge_outcomes_page_html", judge_outcomes_page_html),
    ("live_analysis_page_html", live_analysis_page_html),
    ("memo_citation_check_page_html", memo_citation_check_page_html),
    ("prototype_page_html", prototype_page_html),
    ("quick_search_page_html", quick_search_page_html),
    ("research_page_html", research_page_html),
    ("saved_searches_page_html", saved_searches_page_html),
    ("statute_viewer_page_html", statute_viewer_page_html),
    ("tag_finder_page_html", tag_finder_page_html),
    ("testing_page_html", testing_page_html),
    ("theme_explorer_page_html", theme_explorer_page_html),
    (
        "case_reader_with_statutes_html",
        lambda: case_reader_with_statutes_html(
            1, "Example case", "2020 FC 1", "2020-01-01", "FC", "Example summary"
        ),
    ),
    ("case_reader_statute_viewer_page_html", case_reader_statute_viewer_page_html),
)


class _DocumentShell(HTMLParser):
    def __init__(self):
        super().__init__()
        self.language = None
        self.title_parts = []
        self.in_title = False
        self.viewport = False
        self.h1_count = 0
        self.skip_links = []
        self.targets = {}
        self.main_count = 0
        self.images_missing_alt = 0

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "html":
            self.language = attributes.get("lang")
        elif tag == "title":
            self.in_title = True
        elif tag == "meta" and (attributes.get("name") or "").lower() == "viewport":
            self.viewport = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "main":
            self.main_count += 1
        elif tag == "a" and "skip-link" in (attributes.get("class") or "").split():
            self.skip_links.append(attributes.get("href"))
        if attributes.get("id"):
            self.targets[attributes["id"]] = (tag, attributes.get("tabindex"))
        if tag == "img" and "alt" not in attributes:
            self.images_missing_alt += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)


class _CaseComparisonLandmark(HTMLParser):
    def __init__(self):
        super().__init__()
        self.main_depth = 0
        self.heading_inside_main = False
        self.explanation_inside_main = False
        self.form_inside_main = False
        self.back_link_inside_main = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "main":
            self.main_depth += 1
        elif tag == "h1" and self.main_depth:
            self.heading_inside_main = True
        elif tag == "form" and attributes.get("action") == "/case-compare":
            self.form_inside_main = bool(self.main_depth)
        elif tag == "a" and attributes.get("href") == "/data-explorer":
            self.back_link_inside_main = bool(self.main_depth)

    def handle_endtag(self, tag):
        if tag == "main":
            self.main_depth -= 1

    def handle_data(self, data):
        if self.main_depth and "Research aid only. No records are changed." in data:
            self.explanation_inside_main = True


def test_standalone_page_builders_have_document_shell_metadata():
    for name, builder in PAGE_BUILDERS:
        shell = _DocumentShell()
        shell.feed(builder())

        assert shell.language, f"{name}: missing html lang"
        assert "".join(shell.title_parts).strip(), f"{name}: missing title"
        assert shell.viewport, f"{name}: missing viewport meta"
        assert shell.h1_count == 1, f"{name}: expected one h1, got {shell.h1_count}"
        assert len(shell.skip_links) == 1, f"{name}: expected one skip link"
        href = shell.skip_links[0]
        assert href and href.startswith("#"), f"{name}: skip link has no target"
        assert href[1:] in shell.targets, f"{name}: skip target does not exist"
        target_tag, tabindex = shell.targets[href[1:]]
        assert tabindex is not None, f"{name}: skip target is not focusable"
        if shell.main_count:
            assert target_tag == "main", f"{name}: skip link bypasses the main landmark"
        else:
            assert target_tag == "h1", f"{name}: skip link has no main or heading target"
        assert shell.images_missing_alt == 0, (
            f"{name}: {shell.images_missing_alt} image(s) missing alt"
        )


def test_case_comparison_primary_workflow_is_inside_main():
    html = dict(PAGE_BUILDERS)["case_compare_page_html"]()
    page = _CaseComparisonLandmark()
    page.feed(html)

    assert page.heading_inside_main
    assert page.explanation_inside_main
    assert page.form_inside_main
    assert page.back_link_inside_main is False


def test_skip_link_helper_is_idempotent():
    builder = dict(PAGE_BUILDERS)["data_explorer_page_html"]
    html = builder()

    assert html.count('class="skip-link"') == 1
    assert ensure_skip_link(html) == html
