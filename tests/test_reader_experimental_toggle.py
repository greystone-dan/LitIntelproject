"""Unfinished reader tools are hidden by default behind a remembered 'Show experimental' switch."""

import re

from backend.pages.data_explorer import data_explorer_page_html


def test_unfinished_tools_hidden_until_experimental_switch_is_on():
    html = data_explorer_page_html()
    rule = re.search(r"body:not\(\.reader-experimental\) :is\(([^)]*)\)\{display:none!important\}", html)
    assert rule, "hide rule missing"
    hidden = rule.group(1)
    for selector in ("#readerSummaryToggle", "#readerCaseSummaryToggle", "#readerAssessmentToggle",
                     ".reader-quick-summary", ".reader-extracted-summary", ".reader-extractive-summary", "[data-paragraph-similar]"):
        assert selector in hidden
    assert 'id="readerExperimentalToggle"' in html and "Show experimental" in html
    assert "ilit.reader.experimental" in html  # remembered per browser
    assert "experimentalState={on:false}" in html  # off by default


def test_summary_cards_are_closed_by_default():
    html = data_explorer_page_html()
    assert "const extractedSummaryState={open:false}" in html
    assert "controller:null,open:false" in html


def test_markup_toolbar_has_the_same_switch():
    from pathlib import Path
    js = (Path(__file__).resolve().parents[1] / "backend" / "pages" / "markup_mode.js").read_text(encoding="utf-8")
    assert 'data-mk-act="experimental"' in js and "setReaderExperimental" in js


def test_similar_paragraphs_button_is_never_added_to_the_formatted_view():
    html = data_explorer_page_html()
    assert "button.dataset.paragraphSimilar=''" not in html
    assert "#readerOverrulingRisk,#readerOverrulingRisk[hidden]{display:none!important}" in html


def test_admin_toggle_replaces_welcome_page():
    from fastapi.testclient import TestClient

    from backend.main import app
    from backend.pages.live_analysis import live_analysis_page_html

    client = TestClient(app, follow_redirects=False)
    for path in ("/", "/welcome"):
        response = client.get(path)
        assert response.status_code == 307 and response.headers["location"] == "/data-explorer"
    for html in (data_explorer_page_html(), live_analysis_page_html()):
        assert 'id="siteExperimentalToggle"' in html and ">Admin</button>" in html
        assert "!=='1')document.documentElement.classList.add('ilit-demo')" in html  # normal mode unless switched on
        assert "classList.toggle('ilit-demo',!experimentalState.on)" in html  # one switch governs tabs and reader tools
        assert 'href="/welcome"' not in html and 'id="modeSwitch"' not in html
