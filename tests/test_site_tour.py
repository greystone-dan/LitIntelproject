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


def _tour():
    return {step["id"]: step for step in tour_steps()["steps"]}


def test_explore_steps_hand_the_page_to_the_visitor_and_their_cards_stay_up():
    steps = _tour()
    for step in steps.values():
        if step.get("hint"):
            assert step.get("explore") and "Next" in step["hint"], step["id"]
        if step.get("explore") and not step.get("act"):
            assert not step.get("say"), step["id"]          # nothing is done for the visitor here
    # the explore cards no longer shrink to "click Next" when the visitor scrolls: they stay up (Daniel, 10-22)
    for key in ("sh-explore-reader", "sh-ci", "sh-judges", "sh-fc"):
        assert steps[key].get("explore") and not steps[key].get("hint"), key
    assert not steps["sh-ci"].get("target") and not steps["sh-judges"].get("target") and not steps["sh-fc"].get("target")   # nothing lit
    assert [steps[k]["cardPos"] for k in ("sh-ci", "sh-judges", "sh-fc")] == ["top-right"] * 3
    assert steps["sh-fc"]["cardSize"] == "large"            # the FC Activity card carries two cards' words


def test_every_card_is_a_step_of_its_own():
    # a step that "said" something and then showed its result used to be two cards with the same "Step 4 of 30"
    assert not [step["id"] for step in tour_steps()["steps"] if step.get("say") or step.get("lead")]


def test_tour_follows_daniels_step_list_in_order_and_in_his_words():
    steps = _tour()
    order = list(steps)
    text = json.dumps(list(steps.values()))
    assert len(order) == len(set(order)) == 31
    assert "decision reader" not in text.lower() and "full tour" not in text.lower() and "Ilit" not in text   # "the reader"; iLIT
    assert order[:7] == ["sh-what", "sh-about", "sh-begin", "sh-search", "sh-search-results", "sh-filters", "sh-results"]
    # the decision text comes before the side panel, then the side panel in the order of its tabs
    assert order[order.index("sh-reader"):order.index("sh-explore-reader") + 1] == [
        "sh-reader", "sh-text", "sh-cite-hover", "sh-cite-card", "sh-side-about", "sh-side-auth", "sh-side-cite", "sh-side-judge", "sh-explore-reader"]
    assert order[order.index("sh-judges"):] == ["sh-judges", "sh-fc-data", "sh-fc", "sh-next-wb", "sh-workbench", "sh-next-la", "sh-la-1",
                                               "sh-la-demo", "sh-la-drop", "sh-la-run", "sh-future", "sh-wrap"]
    assert steps["sh-what"]["text"].startswith("This short tour of iLIT will walk through some of the key features")
    assert steps["sh-about"]["target"] == "#homeAboutIntro" and steps["sh-about"]["title"] == "What is iLIT?"
    assert "Let's begin in the research tab." in steps["sh-begin"]["title"]
    assert "This is the search bar, where research starts" in steps["sh-search"]["text"] and "Vavilov" in json.dumps(steps["sh-search-results"]["act"])
    assert steps["sh-search-results"]["text"].endswith("Next, let's open some advanced search filters.")
    assert "7 case types" not in text and "seven case types" not in text
    assert steps["sh-cite-hover"].get("explore") and "Camayo" in steps["sh-cite-hover"]["text"]       # the visitor's own mouse hovers
    assert steps["sh-cite-card"].get("explore")
    for key in ("sh-side-about", "sh-side-auth", "sh-side-cite", "sh-side-judge"):
        assert steps[key]["target"] == ".reader-pane.target" and steps[key].get("explore") and steps[key]["cardPos"] == "bottom-right", key
    assert "Both default to the current case" in steps["sh-side-cite"]["text"]
    assert steps["sh-fc-data"]["text"] == "Let's continue to the FC Activity intelligence tab."
    assert steps["sh-fc"]["text"].startswith("This next tab sets iLIT apart") and "every single IMM case ever filed" in steps["sh-fc"]["text"]
    assert steps["sh-next-wb"]["title"] == "Let's continue to the last major section of the website, the Analyst Workbench Demo."
    assert "still in development" in steps["sh-workbench"]["text"]
    assert "target" not in steps["sh-workbench"] and steps["sh-workbench"]["cardPos"] == "top-right"          # no highlight, the card high on the screen
    assert steps["sh-next-la"]["title"].startswith("Finally, we will finish off by exploring the most impactful use case for iLIT")
    la1 = steps["sh-la-1"]
    assert la1["cardSize"] == "large" and not la1.get("target") and "**iLIT will work not just on court decisions, but on any inputted text.**" in la1["text"]
    assert "does not run on it" in la1["text"] and "without storing anything permanently" in la1["text"]
    assert "made up word document" in steps["sh-la-demo"]["text"] and steps["sh-la-drop"].get("auto")
    assert steps["sh-la-run"]["text"].endswith("This draft is not stored in the library, or added to the database in any way.")
    assert steps["sh-future"]["title"] == "Future use cases" and "just scratching the surface" in steps["sh-future"]["text"]
    assert steps["sh-wrap"]["text"].endswith("Feel free to check out the 'see what is coming' section, or spend more time using the site.")


def test_filters_are_opened_in_one_step_and_applied_in_the_next_by_the_pointer():
    steps = _tour()
    opening, applying = steps["sh-filters"], steps["sh-results"]
    assert opening["text"].startswith("Filters are used in combination to narrow search results.")
    assert "automatically search the library" in opening["text"] and "Sri Lanka tags" in opening["text"]
    assert [a["do"] for a in opening["act"] if a["do"] != "wait"] == ["click", "click"]      # Clear search, then Advanced
    assert opening["act"][0]["selector"] == "#clearSearchTop" and not any(a.get("quiet") for a in opening["act"])   # the pointer is seen doing it
    assert opening.get("early") and opening.get("auto")                       # the card explains while it happens
    # the filters themselves: Refugee protection, the two tags, and Government won last, because that click is what runs the search
    kinds = [(a["do"], a.get("text") or a["selector"]) for a in applying["act"] if a["do"] in ("check", "pickTag", "click")]
    assert [k[0] for k in kinds] == ["check", "pickTag", "pickTag", "click"]
    assert [a["text"] for a in applying["act"] if a["do"] == "pickTag"] == ["cessation", "sri lanka"]
    assert "data-value='won'" in kinds[-1][1] and applying["act"][-1]["selector"] == "#searchResults .case-result"
    assert applying["act"][-2]["selector"] == "#searchMeta[data-state='success']"          # the list is the finished search, not an older one
    assert "{count}" in applying["text"] and "16 cases" not in applying["text"]            # the figure is read from the page, never stale
    assert applying["text"].endswith("Let's continue and open the top result, Veerasingam v. Canada.")


def test_the_filter_searches_are_warmed_so_the_first_walk_is_not_slow():
    cache = tour_steps()["cache"]
    assert "/analytics/search/tags?q=cessation&limit=10" in cache and "/analytics/search/tags?q=sri+lanka&limit=10" in cache
    assert any(u.startswith("/analytics/search/cases?tags=cessation%2Csri_lanka&government_outcome=won&case_type=refugee_claim") for u in cache)
    assert any(u.startswith("/analytics/search/facets?tags=cessation%2Csri_lanka&government_outcome=won") for u in cache)
    assert cache.index("/analytics/search/tags?q=cessation&limit=10") < cache.index("/cases/{cessation}/reader-data?evidence=0")   # needed first, asked first


def test_the_tour_starts_at_once_and_a_next_pressed_early_is_not_undone():
    js = tour_js()
    start = js[js.index("function start(){"):js.index("/* ---------- keyboard ---------- */")]
    assert "async function start" not in js and "await" not in start          # the welcome card waits for nothing
    assert "show(0,1)" in start and "resetSite()" in start and ".then(function(){if(state===started&&ui)warm()})" in start


def test_every_step_that_needs_a_clean_search_resets_it_and_the_pick_of_a_tag_is_patient():
    js, steps = tour_js(), _tour()
    assert steps["sh-search"].get("reset") and steps["sh-search-results"].get("reset")
    assert "function resetSite(" in js and "#clearSearch" in js and "sp-adv" in js
    pick = js[js.index("async function pickTag("):js.index("// Scroll the panel that holds")]
    assert "attempt<2" in pick and "nudge" not in pick                          # one patient try and one more, never a pile of lookups
    assert all(a.get("seconds", 0) >= 45 for a in steps["sh-results"]["act"] if a["do"] == "pickTag")


def test_scrolling_is_planned_and_played_as_one_glide():
    js = tour_js()
    assert "function smoothly(" in js and "planning=true" in js
    assert js.count("await smoothly(") >= 4                                      # result, each action, the say card, the lit region
    assert "function stuckTop(" in js                                            # a bar that will pin counts before the page moves


def test_every_page_change_is_a_pointer_click_on_a_named_tab():
    short = tour_steps()["steps"]
    for before, step in zip(short, short[1:]):
        page = lambda url: re.sub(r"[?#].*", "", url) + (re.search(r"tab=[\w-]+", url) or [""])[0]   # noqa: E731
        if page(before["url"]) != page(step["url"]):
            assert step.get("via"), f"{step['id']} changes page without a tab for the pointer to press"


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
    for step in tour_steps()["steps"] + tour_steps()["steps"]:
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


def test_explorer_and_workbench_carry_the_tour_button():
    # the tour now plays in the recorded window (tests/test_tour_window.py); the old live tour is no longer put on a page
    for html in (routes._data_explorer_page_html(), workbench_page_html()):
        assert html.count("/tour-window.js") == 1 and "/site-tour.js" not in html
    assert inject_site_tour(inject_site_tour("<head></head><body></body>")).count("/tour-window.js") == 1


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


def test_card_follows_the_highlight_and_controls_stay_in_the_dock():
    js = tour_js()
    assert "function placeCard(" in js and "ilit-tour-dock" in js


def test_future_features_now_lives_on_the_roadmap_page():
    page = client.get("/future-features", follow_redirects=False)
    assert page.status_code == 307 and page.headers["location"] == "/roadmap#future-features"
    roadmap = client.get("/roadmap")
    assert roadmap.status_code == 200
    assert "/site-tour.js" not in roadmap.text
    assert "Concept mock-up, not built yet" in roadmap.text
    assert roadmap.text.count('class="facts"') >= 8
    assert "future-features" in routes._data_explorer_page_html()


def test_live_analysis_drops_the_fictional_word_file():
    drops = [a for step in tour_steps()["steps"] for a in step.get("before", []) if a.get("do") == "drop"]
    assert drops and all(a["file"] == "/site-tour/sample-memo.docx" for a in drops)
    response = client.get("/site-tour/sample-memo.docx")
    assert response.status_code == 200 and response.content[:2] == b"PK"
    from backend.live_analysis import extract_document
    text, _ = extract_document(response.content, "memo.docx", None)
    assert text.startswith("MEMORANDUM OF ARGUMENT (FICTIONAL") and "Baker" in text


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


def test_opening_fc_analytics_drops_another_tab_s_judge():
    # a judge profile's ?judge=slug used to carry into Federal Court Analytics as a judge filter, showing 0 files;
    # the other tabs that read judge (the Testing tabs) keep it
    assert "if(selected==='fc-analytics'&&from!=='fc-analytics')url.searchParams.delete('judge')" in routes._data_explorer_page_html()


def test_filter_demo_is_checked_to_put_the_tour_decision_first():
    data = tour_steps()
    probe = next(p for p in data["probes"] if p["id"] == "cessation-sri-lanka-won")
    assert probe["first"] == "cessation" and "sri%20lanka" in probe["url"] and "sort_by=newest" in probe["url"]
    assert "case_type=refugee_cessation" in probe["url"]          # without it a non-cessation decision comes first
    assert next(p for p in data["probes"] if p["id"] == "case-name-search")["first"] == "vavilov"
    script = (Path(__file__).resolve().parents[1] / "scripts" / "check_site_tour.py").read_text(encoding="utf-8")
    assert "NOT the first result of the filter demo" in script and "WRONG FIRST" in script


def test_guided_tour_is_a_section_of_the_roadmap():
    client = TestClient(app)
    assert client.get("/coming-soon-preview", follow_redirects=False).headers["location"] == "/roadmap#tour"
    page = client.get("/roadmap/tour")
    assert page.status_code == 200
    assert "Future local AI" in page.text and 'id="next"' in page.text
    assert 'id="tour"' in client.get("/roadmap").text and 'data-src="/roadmap/tour"' in client.get("/roadmap").text
    assert 'id="comingSoonPreviewStart"' in client.get("/data-explorer").text
    assert client.get("/coming-soon-preview/img/reader.webp").status_code == 200
    assert client.get("/coming-soon-preview/img/secret.webp").status_code == 404


def test_coming_soon_demo_page_is_served_linked_and_makes_no_requests():
    client = TestClient(app)
    page = client.get("/coming-soon-demo")
    assert page.status_code == 200
    for label in ("Reference library", "Smarter tags", "Profiles and teams", "Argument breakdown", "Live document reader", "Future local AI"):
        assert label in page.text
    # demos run on fixed data in the browser: no network calls of any kind
    for call in ("fetch(", "XMLHttpRequest", "sendBeacon", "WebSocket"):
        assert call not in page.text
    explorer = client.get("/data-explorer").text
    assert "roadmap-demos" in explorer and "/roadmap/coming-soon#demos" in explorer
    roadmap = client.get("/roadmap").text
    assert 'id="demos"' in roadmap and 'data-src="/coming-soon-demo#ai"' in roadmap and 'href="#demo-ai"' in roadmap


def test_control_bar_keeps_next_and_exit_on_screen_on_phones():
    css = (Path(__file__).resolve().parent.parent / "backend" / "pages" / "site_tour.css").read_text(encoding="utf-8")
    phone = css[css.index("@media (max-width:560px)"):]
    assert ".ilit-tour-dock{left:12px;right:12px" in phone and "flex-wrap:wrap" in phone


def test_tour_hides_the_experimental_whose_position_bar():
    css = (Path(__file__).resolve().parent.parent / "backend" / "pages" / "site_tour.css").read_text(encoding="utf-8")
    assert "html.ilit-tour-on [data-pos-bar]{display:none!important}" in css


def test_phone_reader_puts_the_side_panel_above_the_text_and_lets_the_page_scroll_in_the_tour():
    css = (Path(__file__).resolve().parent.parent / "backend" / "pages" / "site_tour.css").read_text(encoding="utf-8")
    assert "@media(max-width:760px){html.ilit-tour-on .inline-case-reader{height:auto!important}html.ilit-tour-on .reader-pane.target{order:-1}}" in css