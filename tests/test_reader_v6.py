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
