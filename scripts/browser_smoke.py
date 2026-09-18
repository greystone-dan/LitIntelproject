"""Bounded browser smoke checks for the active Data Explorer workflow."""

from __future__ import annotations

import argparse
import sys
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright


def run_smoke(base_url: str, query: str) -> dict[str, object]:
    """Check the primary Data Explorer and inline reader journeys."""
    result: dict[str, object] = {"base_url": base_url, "query": query}
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            desktop = browser.new_page(viewport={"width": 1440, "height": 1000})
            desktop.goto(f"{base_url}/data-explorer?tab=search", wait_until="networkidle", timeout=30_000)
            desktop.get_by_role("heading", name="Immigration Litigation Intelligence Tool").wait_for()
            desktop.locator("#searchQuery").fill(query)
            desktop.locator("#caseSearch").press("Enter")
            desktop.locator(".case-result").first.wait_for(timeout=30_000)
            desktop.locator(".case-result").first.click()
            desktop.locator("#decisionTitle").wait_for(timeout=30_000)
            desktop.locator("#decisionTarget .reader-info-tabs").wait_for(timeout=30_000)
            tabs = desktop.locator("#decisionTarget .reader-info-tabs button").all_text_contents()
            required_tabs = {"Citations", "Tags", "Acts / Regs", "Precedents"}
            missing_tabs = sorted(required_tabs.difference(tabs))
            if missing_tabs:
                raise AssertionError(f"Missing reader tabs: {missing_tabs}")
            desktop.locator('#decisionTarget [data-reader-tab="tags"]').evaluate("button => button.click()")
            desktop.locator(".reader-tag-summary").wait_for(timeout=10_000)
            desktop.locator("#decisionBody [data-authority]").first.wait_for(timeout=10_000)
            evidence = desktop.locator("#decisionBody [data-authority]").first
            evidence.hover()
            tooltip = desktop.locator(".reader-hover-tooltip.is-visible")
            tooltip.wait_for(timeout=5_000)
            tooltip_text = tooltip.inner_text()
            if not tooltip_text.strip():
                raise AssertionError("Evidence hover tooltip was empty")
            desktop.locator("#readerViewToggle").click()
            desktop.locator("#decisionBody .tag-highlight").first.wait_for(timeout=10_000)
            chunk_tag_highlight_count = desktop.locator("#decisionBody .tag-highlight").count()
            desktop.locator("#readerViewToggle").click()
            desktop.locator("#decisionBody .tag-highlight").first.wait_for(timeout=10_000)
            full_text_tag_highlight_count = desktop.locator("#decisionBody .tag-highlight").count()
            if full_text_tag_highlight_count != chunk_tag_highlight_count:
                raise AssertionError(
                    f"Tag highlight mismatch between chunk ({chunk_tag_highlight_count}) "
                    f"and full text ({full_text_tag_highlight_count}) modes"
                )
            citation_color = desktop.locator("#decisionBody .chunk-citation").first.evaluate("element => getComputedStyle(element).backgroundColor")
            statute_color = desktop.locator("#decisionBody .chunk-statute").first.evaluate("element => getComputedStyle(element).backgroundColor")
            if citation_color == statute_color:
                raise AssertionError("Citation and statute highlights use the same color")
            highlight_counts = {
                "tags": full_text_tag_highlight_count,
                "chunk_tags": chunk_tag_highlight_count,
                "citations": desktop.locator("#decisionBody .chunk-citation, #decisionBody .citation-link").count(),
                "statutes": desktop.locator("#decisionBody .chunk-statute").count(),
            }
            result["case_title"] = desktop.locator("#decisionTitle").inner_text()
            result["reader_tabs"] = tabs
            result["tag_groups"] = desktop.locator(".reader-tag-group").count()
            result["tag_occurrences"] = desktop.locator(".reader-tag-occurrence").count()
            result["layer_legend"] = desktop.locator(".reader-layer-legend").inner_text()
            result["highlight_counts"] = highlight_counts
            result["highlight_colors"] = {"citation": citation_color, "statute": statute_color}
            result["hover_tooltip"] = tooltip_text[:240]

            mobile = browser.new_page(viewport={"width": 390, "height": 844})
            mobile.goto(f"{base_url}/data-explorer?tab=themes", wait_until="networkidle", timeout=30_000)
            mobile.get_by_role("heading", name="Legal Themes & Statutory Affinities").wait_for()
            result["mobile_themes_loaded"] = True
        finally:
            browser.close()
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Run bounded Data Explorer browser smoke checks.")
    parser.add_argument("--base-url", default="http://127.0.0.1:8000", help="Running AI CaseLibrary base URL")
    parser.add_argument("--query", default="Vavilov", help="Case query used for the reader journey")
    args = parser.parse_args()
    try:
        result = run_smoke(args.base_url.rstrip("/"), args.query)
    except (AssertionError, PlaywrightError) as error:
        print(f"Browser smoke failed: {error}", file=sys.stderr)
        return 1
    print("Browser smoke passed")
    for key, value in result.items():
        print(f"{key}={value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
