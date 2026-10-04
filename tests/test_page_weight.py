"""Coverage for offline page-weight and transient UI states."""

import ast
from pathlib import Path

from backend.pages.citation_map import citation_map_html
from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.research import research_page_html
from scripts.measure_page_weight import _PageMetricsParser, _builders, measure_page

ROOT = Path(__file__).resolve().parents[1]


def test_research_page_is_bounded_and_valid_html() -> None:
    html = research_page_html()
    assert 1_000 < len(html.encode("utf-8")) < 50_000
    assert html.startswith("<!doctype html")
    assert "</html>" in html


def test_citation_map_page_is_bounded_and_valid_html() -> None:
    html = citation_map_html()
    assert 1_000 < len(html.encode("utf-8")) < 100_000
    assert html.startswith("<!doctype html")
    assert "</html>" in html


def test_data_explorer_page_is_bounded_and_valid_html() -> None:
    html = data_explorer_page_html()
    assert 100_000 < len(html.encode("utf-8")) < 1_000_000
    assert html.startswith("<!doctype html")
    assert "</html>" in html


def test_every_page_builder_has_offline_fixture_measurements() -> None:
    builders = _builders()
    assert len(builders) == 25
    assert len({name for name, _, _ in builders}) == len(builders)

    for name, source, build_html in builders:
        page = measure_page(name, source, build_html)
        assert page["status"] == "ok"
        assert page["size_bytes"] > 0
        assert 0 < page["gzip_bytes"] < page["size_bytes"]
        assert page["inline_script_bytes"] >= 0
        assert page["inline_style_bytes"] >= 0
        assert page["external_request_count"] >= 0


def test_measurement_inventory_covers_every_named_html_builder() -> None:
    source_files = [
        *sorted((ROOT / "backend" / "pages").glob("*.py")),
        ROOT / "backend" / "routes.py",
        ROOT / "backend" / "case_reader_ui.py",
        ROOT / "backend" / "discussion_units_sandbox.py",
        ROOT / "backend" / "main.py",
    ]
    expected: set[str] = set()
    for source_file in source_files:
        module = ".".join(source_file.relative_to(ROOT).with_suffix("").parts)
        tree = ast.parse(source_file.read_text(encoding="utf-8"))
        expected.update(
            f"{module}.{node.name}"
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and ("html" in node.name.lower() or node.name == "_login_page")
        )

    assert {source for _, source, _ in _builders()} == expected


def test_page_metrics_count_inline_style_attributes_and_non_inline_resources() -> None:
    parser = _PageMetricsParser()
    parser.feed(
        '<style>body{background:url(/img/bg.png)}</style>'
        '<div style="color:red">fixture</div>'
        '<link rel="stylesheet" href="/static/site.css">'
        '<script src="https://cdn.example.test/app.js"></script>'
        '<img src="data:image/gif;base64,AAAA">'
    )
    parser.close()

    assert parser.inline_style_bytes == len(
        'body{background:url(/img/bg.png)}color:red'.encode("utf-8")
    )
    assert parser.inline_script_bytes == 0
    assert parser.external_requests == [
        "/img/bg.png",
        "/static/site.css",
        "https://cdn.example.test/app.js",
    ]


def test_markdown_baseline_contains_measured_builder_inventory() -> None:
    baseline_path = ROOT / "docs" / "reports" / "page-weight-baseline.md"
    baseline = baseline_path.read_text(encoding="utf-8")
    assert "offline" in baseline.lower()
    assert "Raw HTML (bytes)" in baseline
    assert "Inline script (bytes)" in baseline
    assert "Inline style (bytes)" in baseline
    assert "External requests" in baseline
    assert "Measured builders: 25; skipped: 0." in baseline
    for name, _, _ in _builders():
        assert f"| {name} |" in baseline
    explorer = next(page for page in _builders() if page[0] == "data_explorer")
    measurement = measure_page(*explorer)
    assert measurement["external_request_count"] >= 2


def test_research_bench_has_loading_error_and_retry_states() -> None:
    html = research_page_html()

    assert 'id="loadingSection"' in html
    assert 'id="errorSection"' in html
    assert 'role="status"' in html
    assert 'role="alert"' in html
    assert "loading-spinner" in html
    assert "Retry Research" in html
    assert "async function runResearch()" in html


def test_data_explorer_search_retries_current_filters_after_failure() -> None:
    html = data_explorer_page_html()

    assert 'id="searchMeta"' in html
    assert 'id="retryCaseSearch"' in html
    assert "retryButton.hidden=false" in html
    assert "retryButton.hidden=true" in html
    assert "addEventListener('click',runProfessionalSearch)" in html
    assert "Your filters have been preserved" in html
    assert "runProfessionalSearch();" in html
