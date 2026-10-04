"""Coverage for offline page-weight and transient UI states."""

import json
from pathlib import Path

from backend.pages.citation_map import citation_map_html
from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.research import research_page_html

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


def test_baseline_report_has_offline_html_measurements() -> None:
    baseline_path = ROOT / "docs" / "page_weight_baseline.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))

    assert {"version", "timestamp", "methodology", "pages", "summary"} <= baseline.keys()
    assert "offline" in baseline["methodology"].lower()
    pages = {page["name"]: page for page in baseline["pages"]}
    assert {"research", "citation_map", "data_explorer"} <= pages.keys()
    for page in pages.values():
        assert page["status"] == "ok"
        assert 0 < page["size_gzip_bytes"] < page["size_bytes"]
        assert 15 < page["compression_ratio"] < 60


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

