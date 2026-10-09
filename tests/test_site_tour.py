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
    assert {p["id"] for p in data["probes"]} >= {"cessation-tag", "sri-lanka-tag", "cessation-sri-lanka-won", "case-name-search", "tour-decision", "judge-brouwer"}
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
    assert order == ["Welcome", "Research", "Reading a decision", "Intelligence / Statistics", "Workbench", "Live analysis", "Summing up"]
    for name in order:                                   # each section is one unbroken run of steps
        first, last = sections.index(name), len(sections) - 1 - sections[::-1].index(name)
        assert set(sections[first:last + 1]) == {name}, name


def test_tour_is_calm_and_leaves_the_page_usable():
    css, js, steps = tour_css(), tour_js(), tour_steps()["steps"]
    assert "ilit-tour-tag" not in css                                        # no labels on the borders
    assert ".ilit-tour-block{position:fixed;inset:0;pointer-events:auto" in css   # Daniel 10-09: the page cannot be clicked or scrolled
    assert "lockPage(true)" in js and "'wheel','touchmove'" in js and "e.isTrusted" in js and "Exit tour" in js
    assert ".ilit-tour-dim path{fill:rgba(32,37,34,.14)}" in css             # a light shade, not a dark one
    assert "ilit-tour-cursor" in css and "pointAt(" in js                    # a pointer shows what the tour presses
    by_id = {step["id"]: step for step in steps}
    for name in ("search-page", "judges", "workbench-home", "la-safety"):  # each page is introduced before its parts
        assert by_id[name].get("top") and by_id[name].get("lead"), name
    data = tour_steps()                                                      # a feature tour for now: the About introduction
    assert data["introOn"] is False and data["intro"][0]["id"] == "welcome"  # is kept, switched off, until those pages are final
    assert steps[0]["id"] == "tour-welcome" and steps[0]["target"] is None and "DATA.introOn" in js
    assert "Please click Next at the bottom" in steps[0]["text"]
    la = by_id["la-private"]["text"]                                         # Live analysis: worded as the code behaves
    assert "never saved" in la and "never added to the library" in la and "AI model" in la
    assert by_id["la-coming"]["text"].startswith("Not built yet")
    for step in steps:                                                       # text first, then the action on Next
        assert bool(step.get("act")) == bool(step.get("say")), step["id"]
    assert by_id["reader-open"]["via"].startswith("#searchResults .case-result")  # Next clicks into the case
    typed = [a.get("text") for name in ("case-search", "plain-search") for a in by_id[name]["act"] if a.get("do") == "type"]
    assert typed == ["Vavilov", "best interests of the child"]                # a case, then plain words (marked a work in progress)
    assert "work in progress" in by_id["plain-search"]["text"] and "work in progress" in by_id["adv-case-type"]["text"]
    filters = json.dumps([by_id[n].get("act") for n in ("adv-tag", "adv-tag-country", "adv-won")])
    assert "cessation" in filters and "sri lanka" in filters and "citesFilter" not in json.dumps(steps)
    assert "Sri Lanka" in by_id["adv-tag-country"]["say"] and by_id["adv-sort"]["target"] == "#quickSort"
    pins = [s for s in steps if "v6-pinbtn" in json.dumps(s.get("act"))]
    assert [s["id"] for s in pins] == ["reader-cite-pin"]                     # the pin is shown once
    assert "v6-ibtn" in json.dumps(by_id["reader-cite-info"]["act"])          # and the i icon is pressed
    assert by_id["citation-intelligence"]["url"].endswith("case_id={vavilov}") and "Brouwer" in json.dumps(by_id["judge-open"]["act"])
    wrap = by_id["wrap"]
    assert wrap["url"] == "/data-explorer?tab=about" and "not rely on" in wrap["text"] and "public information" in wrap["text"]
    assert "French support" in by_id["done"]["text"] and "security settings" in by_id["done"]["text"]
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
    text = {step["id"]: step for step in tour_steps()["steps"]}["wrap"]["text"]
    assert "built" in text and "run by hand" in text and "not yet scheduled" in text


def _moment(card, ring, full=None, cursor=None):
    box = lambda x, y, w, h: {"x": x, "y": y, "w": w, "h": h}  # noqa: E731
    return {"vw": 1440, "vh": 900, "focus": 0, "card": box(*card), "dock": box(500, 830, 440, 56),
            "cursor": box(*cursor) if cursor else None,
            "items": [{"full": box(*(full or ring)), "seen": box(*(full or ring)), "ring": box(*ring)}]}


def test_geometry_checks_catch_what_looks_wrong():
    problems = check_site_tour.geometry_problems
    good = _moment(card=(900, 100, 400, 220), ring=(94, 94, 412, 312), full=(100, 100, 400, 300))
    assert problems(good) == []
    cut = _moment(card=(900, 100, 400, 220), ring=(94, 94, 412, 200), full=(100, 100, 400, 300))
    assert any("ring cuts target" in p for p in problems(cut))
    covered = _moment(card=(300, 100, 400, 220), ring=(94, 94, 412, 312))
    assert any("card covers target" in p for p in problems(covered))
    over_dock = _moment(card=(500, 700, 400, 220), ring=(94, 94, 412, 312))
    assert any("control bar" in p for p in problems(over_dock))
    pointer = _moment(card=(900, 100, 400, 220), ring=(94, 94, 412, 312), cursor=(950, 150, 26, 26))
    assert any("pointer on the card" in p for p in problems(pointer))
    # moving when the old place was still clear is a jump; moving because the old place now covers the target is not
    assert any("jumped" in p for p in problems(good, previous_card={"x": 600, "y": 400, "w": 400, "h": 220}))
    far_away = {"x": 1000, "y": 560, "w": 400, "h": 220}   # clear, but too far from what it explains: moving closer is right
    assert not any("jumped" in p for p in problems(good, previous_card=far_away))
    target_moved_under_it = _moment(card=(300, 100, 400, 220), ring=(894, 94, 412, 312))
    assert not any("jumped" in p for p in problems(target_moved_under_it, previous_card={"x": 900, "y": 100, "w": 400, "h": 220}))


def test_tall_result_lists_are_ringed_from_their_top():
    # The real library's results run to thousands of pixels: a ring round their first rows is right, as long as it
    # starts at the list's top, spans its width and shows a real part of it.
    problems = check_site_tour.geometry_problems
    box = lambda x, y, w, h: {"x": x, "y": y, "w": w, "h": h}  # noqa: E731

    def tall(ring, under=0):
        g = _moment(card=(900, 560, 400, 220), ring=ring, full=(30, 210, 1380, 5200))
        g["items"][0].update(seen=box(30, 210, 1380, 620), room=box(0, 12, 1440, 804), underBar=under)
        return g

    assert problems(tall((24, 204, 1392, 330))) == []                       # its first whole rows, the card below
    assert any("misses the top" in p for p in problems(tall((24, 400, 1392, 300))))
    assert any("too little" in p for p in problems(tall((24, 204, 1392, 90))))
    assert any("under a bar pinned" in p for p in problems(tall((24, 204, 1392, 330), under=40)))
    # one that would fit on the screen is still a cut
    fits = _moment(card=(900, 100, 400, 220), ring=(94, 94, 412, 200), full=(100, 100, 400, 300))
    fits["items"][0]["room"] = box(0, 12, 1440, 804)
    assert any("ring cuts target" in p for p in problems(fits))


def test_a_region_that_cannot_share_the_screen_with_the_target_is_a_note():
    problems = check_site_tour.geometry_problems
    box = lambda x, y, w, h: {"x": x, "y": y, "w": w, "h": h}  # noqa: E731
    g = _moment(card=(1000, 80, 400, 200), ring=(553, 299, 837, 482), full=(559, 305, 825, 470))
    g["items"][0]["room"] = box(0, 293, 900, 489)
    g["items"].append({"full": box(800, 263, 160, 20), "seen": None, "ring": None, "room": box(0, 293, 900, 489)})
    assert all(p.startswith("note:") for p in problems(g))      # the cited passage fills the panel; its citation sits above
    g["items"][1]["full"] = box(800, 330, 160, 20)
    assert "also[1] has no ring" in problems(g)                   # it would fit beside the target, so a missing ring is a fault


def test_walk_runs_the_geometry_checks_at_every_card():
    source = (ROOT / "scripts" / "check_site_tour.py").read_text(encoding="utf-8")
    assert "geometry_problems(g, previous_card)" in source and "MOTION_RECORDER" in source
    assert "geometry:geometry" in tour_js()


def test_card_and_rings_follow_the_layout_rules():
    js, css = tour_js(), tour_css()
    for rule in ("function showWhole(", "function makeRoom(", "function steady(", "function keepClear(", "HOLD=", "NEAR=",
                 "function rowsEnd(", "function roomBelow(", "function boxView(", "function underBar(", "function glidesOverPointer(", "function shownBox("):
        assert rule in js, rule                                   # whole regions in view; the card stays unless it must move
    assert "html.ilit-tour-on .inline-case-reader{height:calc(100vh - 124px)!important}" in css   # the reader fits above the bar
    assert ".ilit-tour-card{transition:transform" in css           # it glides when it moves, never jumps
    assert "u.skip.style.visibility" in js                          # Next keeps its place when Skip section is not offered


def test_cards_state_what_is_shown_and_the_decision_is_a_cessation_case():
    data = tour_steps()
    for step in data["steps"]:                      # no narration of the tour's own buttons ("Next clicks it", "I'll...")
        for key in ("text", "say", "lead", "leadText"):
            words = step.get(key) or ""
            if step["id"] != "tour-welcome":           # the welcome card asks for Next, in Daniel's words
                assert "Next " not in words and "click next" not in words.lower(), (step["id"], key)
            assert "I'll" not in words and "I will" not in words, (step["id"], key)
    cessation = data["cases"]["cessation"]
    assert cessation["citation"] == "2024 FC 639" and "case_type=refugee_cessation" in cessation["search"]   # Veerasingam (Daniel, 10-09)
    assert "sri%20lanka" in cessation["search"] and "cites_case_id" not in cessation["search"]
    tour_decision = next(p for p in data["probes"] if p["id"] == "tour-decision")
    assert "case_type=refugee_cessation" in tour_decision["url"]


def test_tour_never_opens_the_outline():
    assert "outl" not in json.dumps(tour_steps()["steps"])   # Daniel: the tour should not click on the Outline at all


def test_filter_demo_is_checked_to_put_the_tour_decision_first():
    data = tour_steps()
    probe = next(p for p in data["probes"] if p["id"] == "cessation-sri-lanka-won")
    assert probe["first"] == "cessation" and "sri%20lanka" in probe["url"] and "sort_by=newest" in probe["url"]
    assert "case_type=refugee_cessation" in probe["url"]          # without it a non-cessation decision comes first
    assert next(p for p in data["probes"] if p["id"] == "case-name-search")["first"] == "vavilov"
    script = (Path(__file__).resolve().parents[1] / "scripts" / "check_site_tour.py").read_text(encoding="utf-8")
    assert "NOT the first result of the filter demo" in script and "WRONG FIRST" in script


def test_coming_soon_preview_page_is_served_and_linked():
    client = TestClient(app)
    page = client.get("/coming-soon-preview")
    assert page.status_code == 200
    assert "Future local AI" in page.text and 'id="next"' in page.text
    assert 'href="/coming-soon-preview"' in client.get("/data-explorer").text
