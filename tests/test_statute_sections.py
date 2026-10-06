from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend import statute_sections as sections
from backend.pages.statute_library import statute_library_page_html


def test_normalize_section_takes_base_number():
    assert sections.normalize_section("34(1)(f)") == "34"
    assert sections.normalize_section(" 98.03(4)") == "98.03"
    assert sections.normalize_section("20.01") == "20.01"
    assert sections.normalize_section("4T") == "4t"
    assert sections.normalize_section("abc") == ""


def test_provision_label_for_breakdown():
    assert sections.provision_label("34(1)(f)") == "(1)(f)"
    assert sections.provision_label("96") == "whole section"
    assert sections.provision_label("") == "whole section"


def test_routes_and_page_are_registered():
    app = FastAPI()
    app.include_router(sections.router)
    paths = {route.path for route in app.routes}
    assert "/api/statute-library/acts" in paths
    assert "/api/statute-library/{act}/sections/{section}" in paths
    response = TestClient(app).get("/statute-library")
    assert response.status_code == 200
    assert "Statute Library" in response.text


def test_section_pattern_has_no_capture_group():
    # Postgres substring(text, pattern) returns the first capture group when one exists.
    import re

    assert re.compile(sections._SECTION_PATTERN).groups == 0
