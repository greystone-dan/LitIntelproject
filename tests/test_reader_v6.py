"""Formatted reader redesign (left panel, title card, click cards, in-text search)."""
from pathlib import Path

from backend.pages.data_explorer import data_explorer_page_html

PAGES = Path(__file__).resolve().parents[1] / "backend" / "pages"


def test_reader_v6_assets_are_injected_before_phone_layout():
    html = data_explorer_page_html()
    css = (PAGES / "reader_v6.css").read_text(encoding="utf-8")
    js = (PAGES / "reader_v6.js").read_text(encoding="utf-8")
    assert css in html and js in html
    assert html.index(css) < html.index((PAGES / "mobile_layout.css").read_text(encoding="utf-8"))


def test_reader_v6_panel_has_three_tabs_and_search():
    js = (PAGES / "reader_v6.js").read_text(encoding="utf-8")
    assert "[['about','About'],['auth','Authorities'],['intel','Intelligence']]" in js
    assert "Search this decision" in js
    assert "Double-click" in js


def test_reader_v6_makes_no_model_calls_on_user_text():
    js = (PAGES / "reader_v6.js").read_text(encoding="utf-8")
    for forbidden in ("semantic", "/rag", "openai", "ollama", "embedding"):
        assert forbidden not in js.lower()


def test_reader_v6_css_is_desktop_scoped_and_hides_old_controls():
    css = (PAGES / "reader_v6.css").read_text(encoding="utf-8")
    assert "@media(min-width:761px)" in css
    assert '[data-reader-splitter="linked"]' in css
    assert ".reader-evidence-bar>.reader-evidence-toggle{display:none" in css


def test_reader_v6_layer_toggles_beat_the_reader_highlight_rules():
    css = (PAGES / "reader_v6.css").read_text(encoding="utf-8")
    # The base highlight rules are keyed on #decisionBody with !important, so the hide rules need the id too.
    for rule in ("#decisionBody.hide-cites .citation-link", "#decisionBody.hide-laws mark.chunk-statute", "#decisionBody.hide-tags mark.tag-highlight"):
        assert rule in css


def test_reader_v6_side_panel_changes():
    js = (PAGES / "reader_v6.js").read_text(encoding="utf-8")
    assert "['intel','Citation intelligence']" in js
    assert "Judges who cite it most" not in js and "judges?limit" not in js
    assert "Open full citation intelligence" in js and 'target="_blank"' in js
    # Outline is a button that expands the list and carries the Coming soon tape.
    assert "data-v6-outl-toggle" in js and "COMING SOON" in js
    # Each authority shows its actions up front, with previous and next arrows on Find.
    assert 'data-v6-dir="-1"' in js and 'data-v6-dir="1"' in js
    assert "Citation intelligence</button>" in js and "Full case" in js
    # Full FC activity opens in a new window.
    assert "Full FC activity ↗" in js and 'target="_blank" rel="noopener">Full FC activity' in js


def test_reader_v6_citation_cards_have_an_i_button_and_statutes_say_coming_soon():
    js = (PAGES / "reader_v6.js").read_text(encoding="utf-8")
    assert 'data-v6-i="case"' in js and 'data-v6-i="stat"' in js and "v6-pinbtn" in js
    assert "function statuteHtml" in js and "Coming soon." in js
    assert "if(body.classList.contains('hide-'" in js  # a hidden layer does not open cards


def test_reader_v6_discussion_units_section_is_experimental_and_data_only():
    import json
    import re
    import shutil
    import subprocess

    import pytest

    js = (PAGES / "reader_v6.js").read_text(encoding="utf-8")
    css = (PAGES / "reader_v6.css").read_text(encoding="utf-8")
    assert "body:not(.reader-experimental) .v6-exp{display:none!important}" in css
    assert "data-v6-units-toggle" in js and "unitsSectionHtml(d)" in js
    node = shutil.which("node")
    if node is None:
        pytest.skip("node is not installed")
    snippet = re.search(r"/\* unit-rows:start \*/(.*?)/\* unit-rows:end \*/", js, re.S).group(1)
    data = {
        "chunks": [{"text": "Header"}, {"text": "[1] Overview."}, {"text": "[2] The applicant argues."}, {"text": "[3] I find."}],
        "format_blocks": [{"type": "para", "num": 2, "start": 40}, {"type": "para", "num": 3, "start": 70}],
        "evidence_summary": {
            "role_note": "R", "party_note": "P",
            "units": [
                {"unit_index": 1, "start_paragraph": 2, "end_paragraph": 3, "role": "analysis",
                 "party_arguments": [{"paragraph_index": 2, "party": "applicant"}]},
                {"unit_index": 2, "start_paragraph": 0, "end_paragraph": 0},  # no printed number: skipped
            ],
        },
    }
    probe = snippet + "\nconsole.log(JSON.stringify([unitOutlineRows(JSON.parse(process.argv[1])), unitOutlineRows(null)]));"
    out = subprocess.run([node, "-e", probe, json.dumps(data)], capture_output=True, text=True, check=True).stdout
    with_units, empty = json.loads(out)
    assert with_units["rows"] == [{
        "index": 1, "first": 2, "last": 3, "start": 40, "role": "analysis", "roleName": "Analysis",
        "parties": [{"party": "applicant", "label": "Applicant", "nums": [2]}],
    }]
    assert with_units["roleNote"] == "R" and with_units["partyNote"] == "P"
    assert empty == {"rows": [], "roleNote": "", "partyNote": ""}


def test_reader_v6_units_use_the_servers_printed_numbers_when_present():
    import json
    import re
    import shutil
    import subprocess

    import pytest

    node = shutil.which("node")
    if node is None:
        pytest.skip("node is not installed")
    js = (PAGES / "reader_v6.js").read_text(encoding="utf-8")
    snippet = re.search(r"/\* unit-rows:start \*/(.*?)/\* unit-rows:end \*/", js, re.S).group(1)
    data = {
        "chunks": [{"text": "[1] One big chunk of many paragraphs."}],
        "format_blocks": [{"type": "para", "num": 88, "start": 500}],
        "evidence_summary": {"units": [{
            "unit_index": 3, "start_paragraph": 0, "end_paragraph": 0, "start_number": 88, "end_number": 95,
            "party_arguments": [{"paragraph_index": 0, "paragraph_number": 90, "party": "respondent"}],
        }]},
    }
    probe = snippet + "\nconsole.log(JSON.stringify(unitOutlineRows(JSON.parse(process.argv[1])).rows));"
    rows = json.loads(subprocess.run([node, "-e", probe, json.dumps(data)], capture_output=True, text=True, check=True).stdout)
    assert rows[0]["first"] == 88 and rows[0]["last"] == 95 and rows[0]["start"] == 500
    assert rows[0]["parties"] == [{"party": "respondent", "label": "Respondent", "nums": [90]}]
