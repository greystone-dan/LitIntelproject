from html.parser import HTMLParser
import importlib
import inspect
import re
from pathlib import Path
import pkgutil

from backend import pages
from backend.pages.citation_map import citation_map_html
from backend.pages.citation_pass import citation_pass_page_html
from backend.pages.discussion_units_sandbox import discussion_units_sandbox_page_html
from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.deidentify import deidentify_page_html
from backend.pages.fc_analytics import FC_ANALYTICS_CSS, FC_ANALYTICS_PANEL
from backend.pages.judge_outcomes import judge_outcomes_page_html
from backend.pages.live_analysis import live_analysis_page_html
from backend.pages.memo_citation_check import memo_citation_check_page_html
from backend.pages.prototype import prototype_page_html
from backend.pages.quick_search import quick_search_page_html
from backend.pages.research import research_page_html
from backend.pages.saved_searches import saved_searches_page_html
from backend.pages.statute_viewer import statute_viewer_page_html
from backend.pages.tag_finder import tag_finder_page_html
from backend.pages.testing import testing_page_html as build_testing_page_html


class _PageMarkupParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.tables = []
        self.table_stack = []
        self.main_landmarks = 0
        self.skip_targets = []
        self.ids = set()
        self.live_status_regions = 0

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        if tag == "main" or attributes.get("role") == "main":
            self.main_landmarks += 1
        if tag == "a" and "skip-link" in attributes.get("class", "").split():
            self.skip_targets.append(attributes.get("href"))
        if attributes.get("role") == "status" and attributes.get("aria-live") == "polite":
            self.live_status_regions += 1
        if tag == "img":
            self.images.append(attributes)
        elif tag == "table":
            table = {"headers": 0, "caption": False}
            self.tables.append(table)
            self.table_stack.append(table)
        elif tag == "th" and self.table_stack:
            self.table_stack[-1]["headers"] += 1
        elif tag == "caption" and self.table_stack:
            self.table_stack[-1]["caption"] = True

    def handle_endtag(self, tag):
        if tag == "table" and self.table_stack:
            self.table_stack.pop()


class _ControlNameParser(HTMLParser):
    """Collect static form controls and their visible text/label associations."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.controls = []
        self.labels = {}
        self.label_stack = []
        self.button_stack = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "label":
            self.label_stack.append(
                {
                    "for": attributes.get("for"),
                    "text": [],
                    "controls": [],
                }
            )
        if tag in {"input", "select", "textarea", "button"}:
            index = len(self.controls)
            self.controls.append(
                {
                    "tag": tag,
                    "type": attributes.get("type", "").lower(),
                    "id": attributes.get("id"),
                    "aria-label": attributes.get("aria-label"),
                    "aria-labelledby": attributes.get("aria-labelledby"),
                    "title": attributes.get("title"),
                    "value": attributes.get("value"),
                    "hidden": "hidden" in attributes or attributes.get("aria-hidden") == "true",
                    "text": [],
                }
            )
            if self.label_stack:
                self.label_stack[-1]["controls"].append(index)
            if tag == "button":
                self.button_stack.append(index)

    def handle_data(self, data):
        for label in self.label_stack:
            label["text"].append(data)
        for index in self.button_stack:
            self.controls[index]["text"].append(data)

    def handle_endtag(self, tag):
        if tag == "label" and self.label_stack:
            label = self.label_stack.pop()
            name = " ".join(" ".join(label["text"]).split())
            if label["for"]:
                self.labels[label["for"]] = name
            for index in label["controls"]:
                self.controls[index]["nested-label"] = name
        elif tag == "button" and self.button_stack:
            self.button_stack.pop()


def _unnamed_controls(html):
    parser = _ControlNameParser()
    parser.feed(html)
    unnamed = []
    for control in parser.controls:
        if control["hidden"]:
            continue
        if control["tag"] == "input" and control["type"] == "hidden":
            continue
        label = parser.labels.get(control["id"], "") or control.get("nested-label", "")
        name = (
            control["aria-label"]
            or control["aria-labelledby"]
            or control["title"]
            or label
            or " ".join(control["text"])
        )
        if not name.strip() and control["tag"] == "input" and control["type"] in {
            "button",
            "reset",
            "submit",
        }:
            name = control["value"] or ""
        if not name.strip():
            unnamed.append(control)
    return unnamed


def _all_page_builder_html():
    page_directory = Path(pages.__file__).parent
    for module_info in pkgutil.iter_modules([str(page_directory)]):
        module = importlib.import_module(f"{pages.__name__}.{module_info.name}")
        builders = [
            function
            for name, function in inspect.getmembers(module, inspect.isfunction)
            if function.__module__ == module.__name__
            and (name.endswith("_page_html") or name == "citation_map_html")
        ]
        for builder in builders:
            brief = {
                "tag": "issue:test",
                "decision_count": 1,
                "years": [{"year": 2025, "decision_count": 1, "unclassified_count": 0}],
                "courts": [{"court": "Federal Court", "decision_count": 1}],
                "top_authorities": [],
            }
            html = builder(brief) if builder.__name__ == "issue_brief_page_html" else builder()
            yield f"{module_info.name}.{builder.__name__}", html


def _css_variables(css):
    return {
        name: value
        for name, value in re.findall(
            r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})",
            css,
        )
    }


def _css_scope_variables(css, selector=":root"):
    block = re.search(rf"{re.escape(selector)}\s*\{{([^{{}}]*)\}}", css, re.IGNORECASE)
    assert block, f"CSS scope {selector} was not found"
    return _css_variables(block.group(1))


def _relative_luminance(color):
    value = color.lstrip("#")
    if len(value) == 3:
        value = "".join(channel * 2 for channel in value)
    channels = [int(value[index : index + 2], 16) / 255 for index in (0, 2, 4)]
    linear = [
        channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
        for channel in channels
    ]
    return sum(channel * weight for channel, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def _contrast_ratio(first, second):
    light, dark = sorted(
        (_relative_luminance(first), _relative_luminance(second)), reverse=True
    )
    return (light + 0.05) / (dark + 0.05)


def test_research_searches_and_profiles_have_keyboard_visible_focus():
    html = data_explorer_page_html()

    assert (
        "html body .search-form input:focus-visible,html body .search-form select:focus-visible,"
        "html body .primary-query input:focus-visible,html body .case-result:focus-visible,"
        "html body .reader-info-tabs button:focus-visible{outline:3px solid var(--blue);outline-offset:2px}"
    ) in html
    assert "html body .global-search:focus-within{outline:3px solid var(--blue);outline-offset:2px}" in html
    assert "Find a case by title" in html
    assert "Find a judge by name" in html
    assert 'role="combobox"' in html
    assert 'role="tab" class="rs-tab' in html
    assert "aria-selected=" in html
    assert html.count("button.setAttribute('aria-pressed',String(button.dataset.readerTab===activeTab))") == 2


def test_citation_map_search_is_named_and_controls_have_visible_focus():
    html = citation_map_html()

    assert 'aria-label="Find a case by citation or case name"' in html
    assert ".search input:focus-visible{outline:3px solid var(--blue);outline-offset:2px}" in html
    assert "button:focus-visible,a:focus-visible,select:focus-visible{outline:3px solid var(--blue);outline-offset:2px}" in html
    assert '<svg id="mapSvg" role="img" aria-label="Citation map"></svg>' in html
    assert '<button class="mode-button active" data-mode="case" aria-pressed="true">' in html
    assert 'b.setAttribute(\'aria-pressed\',String(b.dataset.mode===state.mode))' in html
    assert '<button class="tab active" data-tab="links" aria-pressed="true">' in html
    assert 'x.setAttribute(\'aria-pressed\',String(x===t))' in html


def test_second_pass_pages_have_names_for_static_form_controls():
    pages = {
        "De-identify": deidentify_page_html(),
        "Memo Citation Check": memo_citation_check_page_html(),
        "Tag Finder": tag_finder_page_html(),
        "Saved Searches": saved_searches_page_html(),
        "Research": research_page_html(),
        "Prototype Explorer": prototype_page_html(),
        "FC Analytics": FC_ANALYTICS_PANEL,
    }
    for page_name, html in pages.items():
        assert not _unnamed_controls(html), f"{page_name} has unnamed controls: {_unnamed_controls(html)}"


def test_second_pass_pages_expose_explicit_visible_focus_styles():
    pages = {
        "De-identify": deidentify_page_html(),
        "Memo Citation Check": memo_citation_check_page_html(),
        "Tag Finder": tag_finder_page_html(),
        "Saved Searches": saved_searches_page_html(),
        "Research": research_page_html(),
        "Prototype Explorer": prototype_page_html(),
        "FC Analytics": FC_ANALYTICS_CSS,
    }
    for page_name, html in pages.items():
        assert ":focus-visible" in html, f"{page_name} is missing a focus-visible style"
        assert "outline:" in html, f"{page_name} focus style does not draw an outline"


def test_fc_analytics_focus_outline_contrasts_against_emitted_surface_token():
    css = FC_ANALYTICS_CSS
    variables = _css_variables(css)
    assert "fcx-ink" in variables
    assert "fcx-surface" in variables
    assert re.search(
        r"\.fcx \.fcx-hit:focus-visible\{[^}]*outline:3px solid var\(--fcx-ink\)",
        css,
    )
    assert _contrast_ratio(variables["fcx-ink"], variables["fcx-surface"]) >= 3.0


def test_page_theme_text_and_focus_tokens_meet_contrast_thresholds():
    themes = {
        "Data Explorer": (
            _css_scope_variables(data_explorer_page_html()),
            [
                ("text", "bg"),
                ("text", "surface"),
                ("text", "surface-alt"),
                ("muted", "bg"),
                ("muted", "surface"),
                ("muted", "surface-alt"),
                ("muted-2", "bg"),
                ("muted-2", "surface"),
                ("muted-2", "surface-alt"),
            ],
        ),
        "Data Explorer About": (
            _css_scope_variables(data_explorer_page_html(), ".ilit-about"),
            [
                ("text", "bg"),
                ("text", "surface"),
                ("muted", "bg"),
                ("muted", "surface"),
            ],
        ),
        "Citation Map": (
            _css_scope_variables(citation_map_html()),
            [("ink", "paper"), ("muted", "paper")],
        ),
        "De-identify": (
            _css_scope_variables(deidentify_page_html()),
            [("ink", "paper"), ("muted", "paper")],
        ),
        "Live Analysis": (
            _css_scope_variables(live_analysis_page_html()),
            [("ink", "paper"), ("muted", "paper")],
        ),
        "Memo Citation Check": (
            _css_scope_variables(memo_citation_check_page_html()),
            [("ink", "paper"), ("muted", "paper")],
        ),
        "Discussion Units": (
            _css_scope_variables(discussion_units_sandbox_page_html()),
            [("ink", "paper"), ("muted", "paper")],
        ),
        "Citation Pass": (
            _css_scope_variables(citation_pass_page_html()),
            [("text", "bg"), ("muted", "bg"), ("muted", "panel")],
        ),
        "Judge Outcomes": (
            _css_scope_variables(judge_outcomes_page_html()),
            [("ink", "paper"), ("muted", "paper"), ("muted", "panel")],
        ),
        "Statute Viewer": (
            _css_scope_variables(statute_viewer_page_html()),
            [("ink", "paper"), ("muted", "paper"), ("muted", "panel")],
        ),
        "Quick Search": (
            _css_scope_variables(quick_search_page_html()),
            [("ink", "bg"), ("muted", "bg"), ("muted", "card")],
        ),
        "Tag Finder": (
            _css_scope_variables(tag_finder_page_html()),
            [("ink", "bg"), ("muted", "bg"), ("muted", "card")],
        ),
        "Research": (
            _css_scope_variables(research_page_html()),
            [("ink", "bg"), ("muted", "bg"), ("muted", "panel")],
        ),
        "Prototype Explorer": (
            _css_scope_variables(prototype_page_html()),
            [("ink", "bg"), ("muted", "bg"), ("muted", "panel")],
        ),
        "API Tester": (
            _css_scope_variables(build_testing_page_html()),
            [("ink", "bg"), ("muted", "bg"), ("muted", "panel")],
        ),
    }
    for page_name, (variables, pairs) in themes.items():
        for foreground, background in pairs:
            assert _contrast_ratio(
                variables[foreground], variables[background]
            ) >= 4.5, f"{page_name} {foreground} on {background} is below 4.5:1"

    focus_pairs = [
        (_css_scope_variables(data_explorer_page_html()), "blue", "surface"),
        (_css_scope_variables(citation_map_html()), "blue", "paper"),
        (_css_scope_variables(deidentify_page_html()), "teal", "surface"),
    ]
    for variables, foreground, background in focus_pairs:
        assert _contrast_ratio(variables[foreground], variables[background]) >= 3.0
    shared_focus_color = _css_variables(data_explorer_page_html())["a11y-focus"]
    assert _contrast_ratio(shared_focus_color, "#ffffff") >= 3.0


def test_deidentify_paste_textareas_are_programmatically_named_and_file_inputs_focusable():
    html = deidentify_page_html()
    assert '<label class="or" for="deidText">or paste text</label>' in html
    assert '<label class="or" for="restoreText">or paste text</label>' in html
    assert ".drop input{position:absolute" in html
    assert ".drop:focus-within{outline:3px solid var(--teal)" in html
    assert 'aria-describedby="deidError"' in html
    assert 'aria-describedby="restoreError"' in html
    assert 'id="deidError" role="alert"' in html
    assert 'id="restoreError" role="alert"' in html
    for upload_page in (live_analysis_page_html(), memo_citation_check_page_html()):
        assert re.search(
            r'<input\b[^>]*id="file"[^>]*aria-describedby="error"', upload_page
        )
        assert 'id="error" role="alert" aria-live="assertive"' in upload_page


def test_all_page_builders_have_accessible_static_images_controls_and_tables():
    pages_html = list(_all_page_builder_html())
    assert pages_html

    findings = []
    for page_name, html in pages_html:
        parser = _PageMarkupParser()
        parser.feed(html)
        assert parser.main_landmarks, f"{page_name} has no main landmark"
        assert parser.skip_targets, f"{page_name} has no skip-to-content link"
        assert all(
            target and target.startswith("#") and target[1:] in parser.ids
            for target in parser.skip_targets
        ), f"{page_name} has a broken skip-to-content target"
        assert "prefers-reduced-motion:reduce" in html, (
            f"{page_name} has no reduced-motion accommodation"
        )
        assert "data-accessibility-table-labels" in html, (
            f"{page_name} does not label its dynamically rendered tables"
        )
        assert ":focus-visible{outline:3px solid var(--a11y-focus)" in html
        missing_alt = [image for image in parser.images if "alt" not in image]
        missing_headers = [
            index for index, table in enumerate(parser.tables, start=1) if not table["headers"]
        ]
        missing_captions = [
            index for index, table in enumerate(parser.tables, start=1) if not table["caption"]
        ]
        unnamed = _unnamed_controls(html)
        if missing_alt or missing_headers or missing_captions or unnamed:
            findings.append(
                f"{page_name}: images without alt={missing_alt}, "
                f"unnamed controls={unnamed}, tables without headers={missing_headers}, "
                f"tables without captions={missing_captions}"
            )

    assert not findings, "\n".join(findings)


def test_async_result_pages_announce_status_updates():
    pages_html = dict(_all_page_builder_html())
    for page_name in (
        "data_explorer.data_explorer_page_html",
        "discussion_units_sandbox.discussion_units_sandbox_page_html",
        "live_analysis.live_analysis_page_html",
        "memo_citation_check.memo_citation_check_page_html",
        "quick_search.quick_search_page_html",
        "saved_searches.saved_searches_page_html",
        "tag_finder.tag_finder_page_html",
    ):
        parser = _PageMarkupParser()
        parser.feed(pages_html[page_name])
        assert parser.live_status_regions, f"{page_name} has no polite live status region"
