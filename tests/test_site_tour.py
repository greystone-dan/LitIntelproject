"""The "Take a tour" walkthrough: the step list is valid, the assets are served, and the pages carry the tour."""

import importlib.util
import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from backend import routes
from backend.main import app
from backend.pages.workbench import workbench_page_html
from backend.site_tour import inject_site_tour, tour_css, tour_js, tour_steps

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("check_site_tour", ROOT / "scripts" / "check_site_tour.py")
check_site_tour = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_site_tour)

client = TestClient(app)


def test_steps_file_is_valid():
    assert check_site_tour.validate_steps(tour_steps()) == []


def test_every_step_url_is_a_real_page():
    for path in {re.sub(r"[?#].*", "", step["url"]) for step in tour_steps()["steps"]}:
        assert client.get(path, follow_redirects=False).status_code == 200, path


def test_example_cases_have_a_citation_to_look_up():
    for name, spec in tour_steps()["cases"].items():
        assert spec.get("citation") or spec.get("search"), name


def test_validation_catches_mistakes():
    broken = {"cases": {}, "steps": [{"id": "a", "section": "S", "url": "http://elsewhere/x", "title": "T", "text": "x",
                                       "before": [{"do": "explode", "selector": "#x"}], "buttons": [{"label": "L", "click": "#b"}]},
                                      {"id": "a", "section": "S", "url": "/x/{missing}", "title": "T", "text": "x"}]}
    problems = " | ".join(check_site_tour.validate_steps(broken))
    for fragment in ("path on this site", "unknown action", "must say what it writes", "duplicate id", "unknown case"):
        assert fragment in problems


def test_tour_assets_are_served_without_the_database():
    script = client.get("/site-tour.js")
    assert script.status_code == 200 and "javascript" in script.headers["content-type"]
    assert script.text.startswith("window.ILIT_TOUR=")
    payload = script.text.split("\n", 1)[0][len("window.ILIT_TOUR="):-1]
    assert json.loads(payload)["steps"]
    styles = client.get("/site-tour.css")
    assert styles.status_code == 200 and ".ilit-tour-card" in styles.text


def test_tour_makes_no_outside_or_ai_calls():
    source = tour_js()
    assert "fetch(" in source
    for call in re.findall(r"fetch\(([^)]*)", source):
        assert "http" not in call, call               # only the site's own search
    assert "openai" not in source.lower() and "XMLHttpRequest" not in source


def test_explorer_and_workbench_carry_the_tour():
    for html in (routes._data_explorer_page_html(), workbench_page_html()):
        assert html.count("/site-tour.js") == 1 and html.count("/site-tour.css") == 1
    assert inject_site_tour(inject_site_tour("<head></head><body></body>")).count("/site-tour.js") == 1


def test_about_page_has_the_tour_button():
    html = routes._data_explorer_page_html()
    assert 'data-ilit-tour-start' in html and "Take a tour" in html


def test_tour_css_covers_phone_and_reduced_motion():
    css = tour_css()
    assert "prefers-reduced-motion" in css and "max-width:639px" in css and ".sheet" in css


@pytest.mark.skipif(not shutil.which("node"), reason="node is needed to syntax-check the script")
def test_tour_script_parses(tmp_path):
    target = tmp_path / "tour.js"
    target.write_text(tour_js(), encoding="utf-8")
    result = subprocess.run(["node", "--check", str(target)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_steps_that_write_say_so_and_the_tour_never_moves_on_by_itself():
    steps = tour_steps()["steps"]
    for step in steps:
        clicks_save = any(a.get("selector") == "#v6SaveWb" for a in step.get("before", []))
        assert not clicks_save or step.get("writes"), step["id"]
    # The only automatic move is skipping a step whose target is missing; a button never calls go().
    assert "btn.onclick=function(){var node=qs(b.click);if(node)node.click();btn.disabled=true}" in tour_js()


def test_fc_activity_has_its_own_walkthrough_and_example_data_is_probed():
    data = tour_steps()
    assert len([s for s in data["steps"] if s["id"].startswith("fc-")]) >= 12
    assert {"la-paste", "la-run", "la-table"} <= {s["id"] for s in data["steps"]}
    assert data["texts"]["moa"].startswith("MEMORANDUM OF ARGUMENT (FICTIONAL")
    assert {p["id"] for p in data["probes"]} >= {"cessation-india-minister-won"}
    assert "/analytics/search/cases" in tour_steps()["probes"][0]["url"]


def test_card_stays_in_one_place_on_desktop():
    assert "card.style.right='20px';card.style.bottom='20px'" in tour_js()


def test_future_features_tour_is_valid_and_served():
    from backend.site_tour import future_tour_js, future_tour_steps

    data = future_tour_steps()
    assert check_site_tour.validate_steps(data) == []
    assert {s["url"] for s in data["steps"]} == {"/future-features"}
    page = client.get("/future-features")
    assert page.status_code == 200 and "/future-tour.js" in page.text and "/site-tour.js" not in page.text
    assert "Concept mock-ups, not built yet" in page.text
    for step in data["steps"]:
        target = step["target"]
        assert target.startswith("#") and f'id="{target[1:]}"' in page.text, step["id"]
    script = client.get("/future-tour.js")
    assert script.status_code == 200 and script.text.startswith("window.ILIT_TOUR=")
    assert '"key": "ilit.tour.future.v1"' in future_tour_js() and "fetch(" in future_tour_js()


def test_future_tour_is_reachable_from_about_and_coming_soon():
    html = routes._data_explorer_page_html()
    assert html.count('href="/future-features?tour=1"') >= 2
