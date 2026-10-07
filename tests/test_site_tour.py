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


def test_tour_warms_only_its_own_read_only_data():
    for entry in tour_steps()["warm"]:
        if isinstance(entry, str):
            assert entry.startswith("/api/fc-activity/"), entry
        elif "post" in entry:                             # the fictional demo memo, read and not stored
            assert entry["post"] == "/live-analysis/reader" and entry["file"] == "/site-tour/sample-memo.docx"
        elif "years" in entry:                            # the same statistics for the "Last 5 years" step
            assert all(url.startswith("/api/fc-activity/") for url in [entry["url"], *entry["years"]["then"]])
        else:
            assert entry["url"].startswith("/api/judge-profiles") and entry["top"]["then"].startswith("/api/judge-profiles/")


def test_live_analysis_steps_read_the_document_once():
    for step in tour_steps()["steps"]:
        for action in step.get("before", []):
            if action.get("selector") in ("#laDrop", "#laAnalyze"):
                assert action.get("unless") == "#decisionBody span.citation-link", step["id"]


def test_only_the_demo_document_is_cached(monkeypatch):
    from backend.analytics_service import get_analytics_cache
    from backend.database import get_db

    calls = []
    monkeypatch.setattr(routes, "build_live_reader_payload", lambda text, paragraphs, title, db: calls.append(text) or {"n": len(calls)})
    app.dependency_overrides[get_db] = lambda: None
    get_analytics_cache().clear()
    try:
        demo = tour_steps()["texts"]["moa"]
        for text in (demo, demo, "A person's own memo.", "A person's own memo."):
            assert client.post("/live-analysis/reader-text", json={"text": text}).status_code == 200
    finally:
        app.dependency_overrides.clear()
        get_analytics_cache().clear()
    assert len(calls) == 3                                # the demo is read once; a person's text every time


def test_only_the_sample_word_file_is_cached(monkeypatch):
    from backend.analytics_service import get_analytics_cache
    from backend.database import get_db
    from backend.site_tour import tour_sample_docx

    calls = []
    monkeypatch.setattr(routes, "build_live_reader_payload", lambda text, paragraphs, title, db: calls.append(title) or {"n": len(calls)})
    app.dependency_overrides[get_db] = lambda: None
    get_analytics_cache().clear()
    sample = tour_sample_docx()
    other = sample.replace(b"word/document.xml", b"word/document.xml", 1) + b"\0"     # same content, different bytes
    try:
        for content in (sample, sample, other, other):
            files = {"file": ("memo.docx", content, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")}
            client.post("/live-analysis/reader", files=files)
    finally:
        app.dependency_overrides.clear()
        get_analytics_cache().clear()
    assert len(calls) == 3                                # the sample is read once; any other file every time


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


def test_tour_css_covers_reduced_motion_and_a_separate_control_bar():
    css = tour_css()
    assert "prefers-reduced-motion" in css
    assert ".ilit-tour-dock" in css and ".ilit-tour-card" in css   # Next/Back/Skip sit apart from the speech card


@pytest.mark.skipif(not shutil.which("node"), reason="node is needed to syntax-check the script")
def test_tour_script_parses(tmp_path):
    target = tmp_path / "tour.js"
    target.write_text(tour_js(), encoding="utf-8")
    result = subprocess.run(["node", "--check", str(target)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_steps_that_write_say_so_and_the_tour_never_moves_on_by_itself():
    steps = tour_steps()["steps"]
    for step in steps:
        clicks_save = any(a.get("selector") in ("#v6SaveWb", "#laPinAll") for a in step.get("before", []))
        assert not clicks_save or step.get("writes"), step["id"]
    # The only automatic move is skipping a step whose target is missing; a button never calls go().
    assert "btn.onclick=function(){var node=qs(b.click);if(node)node.click();btn.disabled=true}" in tour_js()


def test_fc_activity_has_its_own_walkthrough_and_example_data_is_probed():
    data = tour_steps()
    fc_steps = [s for s in data["steps"] if s["id"].startswith("fc-")]
    assert 4 <= len(fc_steps) <= 6                        # a few narrative steps, not every chart
    assert all(not s.get("also") for s in fc_steps)    # one box per statistics step
    assert {"la-safety", "la-drop", "la-run", "la-table"} <= {s["id"] for s in data["steps"]}
    assert data["texts"]["moa"].startswith("MEMORANDUM OF ARGUMENT (FICTIONAL")
    assert {p["id"] for p in data["probes"]} >= {"cessation-tag", "india-tag", "cessation-india-won", "plain-search-2", "tour-decision"}
    assert "/analytics/search/cases" in tour_steps()["probes"][0]["url"]


def test_card_follows_the_highlight_and_controls_stay_in_the_dock():
    js = tour_js()
    assert "function placeCard(" in js and "ilit-tour-dock" in js


def test_future_features_is_a_static_page_linked_from_about_and_coming_soon():
    page = client.get("/future-features")
    assert page.status_code == 200
    assert "/site-tour.js" not in page.text and "<script" not in page.text
    assert "Future state, not built yet" in page.text and "Concept mock-up, not built yet" in page.text
    assert page.text.count('class="facts"') >= 8
    html = routes._data_explorer_page_html()
    assert html.count('href="/future-features"') >= 2


def test_sections_follow_the_header_tabs_without_going_back():
    sections = [step["section"] for step in tour_steps()["steps"]]
    order = list(dict.fromkeys(sections))
    assert order == ["Welcome", "Research", "Reading a decision", "Intelligence / Statistics", "Workbench", "Live analysis", "Keeping it current"]
    for name in order:                                   # each section is one unbroken run of steps
        first, last = sections.index(name), len(sections) - 1 - sections[::-1].index(name)
        assert set(sections[first:last + 1]) == {name}, name


def test_tour_is_calm_and_leaves_the_page_usable():
    css, js, steps = tour_css(), tour_js(), tour_steps()["steps"]
    assert "ilit-tour-block" not in css and "ilit-tour-tag" not in css      # no click blocker, no labels on the borders
    assert ".ilit-tour-dim path{fill:rgba(32,37,34,.14)}" in css             # a light shade, not a dark one
    assert "ilit-tour-cursor" in css and "pointAt(" in js                    # a pointer shows what the tour presses
    by_id = {step["id"]: step for step in steps}
    for name in ("search-page", "judges", "workbench-home", "la-safety"):  # each page is introduced before its parts
        assert by_id[name].get("top") and by_id[name].get("lead"), name
    assert steps[0]["url"].startswith("/data-explorer?tab=about")          # the tour starts on About
    for step in steps:                                                       # text first, then the action on Next
        assert bool(step.get("act")) == bool(step.get("say")), step["id"]
    assert by_id["reader-open"]["via"].startswith("#searchResults .case-result")  # Next clicks into the case
    typed = {a.get("text") for name in ("plain-search", "plain-search-2") for a in by_id[name]["act"] if a.get("do") == "type"}
    assert typed == {"best interests of the child", "non-refoulement statutory interpretation"}
    filters = json.dumps([by_id[n].get("act") for n in ("adv-tag", "adv-tag-india", "adv-cites")])
    assert "cessation" in filters and "india" in filters and "2019 SCC 65" in filters
    assert not any(a.get("do") in ("type", "fill") and a.get("selector") == "#searchQuery"   # filters only, no typed query
                   for step in steps if step["id"].startswith("adv-") for a in step.get("before", []) + (step.get("act") or []))
    click = by_id["reader-cite-card"]["act"][0]                              # clicks a citation that has a pinpoint
    assert click["do"] == "click" and any(isinstance(t, dict) and t.get("pin") for t in click["selector"])
    readers = [s for s in steps if s["section"] == "Reading a decision"]
    assert all("{cessation}" in s.get("url", "") for s in readers)            # one cessation decision throughout


def test_live_analysis_drops_the_fictional_word_file():
    drops = [a for step in tour_steps()["steps"] for a in step.get("before", []) if a.get("do") == "drop"]
    assert drops and all(a["file"] == "/site-tour/sample-memo.docx" for a in drops)
    response = client.get("/site-tour/sample-memo.docx")
    assert response.status_code == 200 and response.content[:2] == b"PK"
    from backend.live_analysis import extract_document
    text, _ = extract_document(response.content, "memo.docx", None)
    assert text.startswith("MEMORANDUM OF ARGUMENT (FICTIONAL") and "Baker" in text


def test_freshness_section_does_not_claim_the_intake_runs_on_its_own():
    text = {step["id"]: step for step in tour_steps()["steps"]}["fresh"]["text"]
    assert "built" in text and "run by hand" in text and "being rolled out" in text
