from html.parser import HTMLParser
import importlib
import inspect
import re
from pathlib import Path
import pkgutil

from backend import pages
from backend.pages.citation_map import citation_map_html
from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.deidentify import deidentify_page_html
from backend.pages.fc_analytics import FC_ANALYTICS_CSS, FC_ANALYTICS_PANEL
from backend.pages.memo_citation_check import memo_citation_check_page_html
from backend.pages.prototype import prototype_page_html
from backend.pages.research import research_page_html
from backend.pages.saved_searches import saved_searches_page_html
from backend.pages.tag_finder import tag_finder_page_html


class _PageMarkupParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.tables = []
        self.table_stack = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
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
            html = builder({}) if builder.__name__ == "issue_brief_page_html" else builder()
            yield f"{module_info.name}.{builder.__name__}", html


def _css_variables(css):
    return {
        name: value
        for name, value in re.findall(
            r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})",
            css,
        )
    }


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


def test_deidentify_paste_textareas_are_programmatically_named_and_file_inputs_focusable():
    html = deidentify_page_html()
    assert '<label class="or" for="deidText">or paste text</label>' in html
    assert '<label class="or" for="restoreText">or paste text</label>' in html
    assert ".drop input{position:absolute" in html
    assert ".drop:focus-within{outline:3px solid var(--teal)" in html


def test_all_page_builders_have_accessible_static_images_controls_and_tables():
    pages_html = list(_all_page_builder_html())
    assert pages_html

    findings = []
    for page_name, html in pages_html:
        parser = _PageMarkupParser()
        parser.feed(html)
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
