from pathlib import Path
from html.parser import HTMLParser

from backend.pages.accessibility_statement import accessibility_page_html
from backend.case_reader_ui import case_reader_with_statutes_html
from backend.pages.citation_map import citation_map_html


ROOT = Path(__file__).resolve().parents[1]


class _StatementMarkup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.language = None
        self.title = []
        self.in_title = False
        self.viewport = False
        self.h1_count = 0
        self.skip_target = None
        self.main_ids = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "html":
            self.language = attributes.get("lang")
        elif tag == "title":
            self.in_title = True
        elif tag == "meta" and attributes.get("name") == "viewport":
            self.viewport = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "a" and "skip-link" in (attributes.get("class") or "").split():
            self.skip_target = attributes.get("href")
        elif tag == "main":
            self.main_ids.add(attributes.get("id"))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)


def test_accessibility_statement_is_candid_and_has_owner_placeholder():
    html = accessibility_page_html()
    markup = _StatementMarkup()
    markup.feed(html)

    assert "WCAG 2.1 Level AA" in html
    assert "This is not a conformance statement." in html
    assert "Our static checks cover the declared language, title, viewport" in html
    assert "have not tested with a screen reader" in html
    assert "have not tested browser zoom at 200%" in html
    assert "visual graph" in html
    assert "[PLACEHOLDER — site owner must set this contact before publication]" in html
    assert markup.language == "en"
    assert "".join(markup.title).strip()
    assert markup.viewport
    assert markup.h1_count == 1
    assert markup.skip_target and markup.skip_target.removeprefix("#") in markup.main_ids


def test_accessibility_route_and_about_link_are_wired_without_database():
    routes = (ROOT / "backend/routes.py").read_text(encoding="utf-8")
    about = (ROOT / "backend/pages/about_content.html").read_text(encoding="utf-8")

    assert '@router.get("/accessibility", response_class=HTMLResponse' in routes
    assert "accessibility_page_html()" in routes
    assert '<a href="/accessibility">Accessibility</a>' in about
    assert '<h2 class="about-title">iLit: where the project stands</h2>' in about
    assert (
        ".ilit-about .about-title{font:700 clamp(30px,5vw,42px)/1.1 var(--serif);"
        "margin:0 0 14px;text-wrap:balance;max-width:22ch}"
    ) in about


def test_case_reader_h1_retains_previous_h3_top_spacing():
    html = case_reader_with_statutes_html(
        1, "Example case", "2020 FC 1", "2020-01-01", "FC", "Example summary"
    )

    assert (
        '<h1 style="font-size: 16px; margin-top: 1em; margin-bottom: 8px;" '
        'id="main-content" tabindex="-1">Example case</h1>'
    ) in html


def test_citation_map_has_svg_name_description_and_dynamic_table_alternative():
    html = citation_map_html()

    assert 'aria-labelledby="mapSvgTitle mapSvgDescription"' in html
    assert '<title id="mapSvgTitle">Citation map</title>' in html
    assert '<desc id="mapSvgDescription">' in html
    assert "<summary>View as table</summary>" in html
    assert 'id="mapTableNodes"' in html
    assert 'id="mapTableEdges"' in html
    assert "Each directed link means the source decision cites the target authority" in html
    assert "function renderTableAlternative()" in html
    assert "const renderMapWithAlternatives=renderMap" in html
