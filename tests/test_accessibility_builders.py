from backend.pages.citation_map import citation_map_html
from backend.pages.quick_search import quick_search_page_html
from backend.pages.research import research_page_html
from backend.pages.data_explorer import data_explorer_page_html


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


def test_standalone_search_builders_keep_visible_focus_and_mobile_targets():
    for html in (research_page_html(), quick_search_page_html()):
        assert "<main " in html and "</main>" in html
        assert ":focus-visible" in html
        assert "min-height: 44px" in html or "min-height: 44px;" in html
    assert 'aria-label="Prototype navigation"' in research_page_html()
    quick_search_html = quick_search_page_html()
    assert 'id="status" class="status" role="status" aria-live="polite"' in quick_search_html
    assert 'id="results" aria-label="Search results"' in quick_search_html
