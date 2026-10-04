"""Optional axe scan; requires Playwright, axe-playwright-python, and Chromium."""

import json

import pytest

from backend.pages.accessibility_statement import accessibility_page_html


def test_accessibility_statement_has_no_axe_violations():
    playwright_api = pytest.importorskip("playwright.sync_api")
    axe_module = pytest.importorskip("axe_playwright_python.sync_playwright")
    sync_playwright = playwright_api.sync_playwright
    axe = axe_module.Axe()

    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch()
        except playwright_api.Error as exc:
            pytest.skip(f"Playwright Chromium is unavailable: {exc}")
        page = browser.new_page()
        page.set_content(accessibility_page_html())
        results = axe.run(page)
        browser.close()

    violations = results.get("violations", [])
    assert not violations, json.dumps(violations, indent=2)
