"""The recorded tour window: its pages and pictures are served, the step data is sound, and pages open it."""

import json
import shutil
import subprocess
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from backend import routes
from backend.main import app
from backend.pages.workbench import workbench_page_html
from backend.site_tour import inject_site_tour
from backend.tour_window import referenced_images, window_data, window_loader, window_steps

client = TestClient(app)
IMG_DIR = Path(__file__).resolve().parent.parent / "site_assets" / "tour_window" / "img"


def test_window_page_data_and_opener_are_served_without_the_database():
    page = client.get("/tour-window/")
    assert page.status_code == 200 and "text/html" in page.headers["content-type"] and 'id="stage"' in page.text
    data = client.get("/tour-window/tour_data.json")
    assert data.status_code == 200 and json.loads(data.text)["moments"]
    script = client.get("/tour-window.js")
    assert script.status_code == 200 and "javascript" in script.headers["content-type"] and "ilitTour" in script.text


def test_the_card_stays_in_one_place_for_judge_profiles_to_the_workbench():
    cards = {step["id"]: step["card"] for step in window_steps()}
    for key in ("sh-judges", "sh-judge-open", "sh-judge-charts", "sh-fc-data", "sh-workbench"):
        assert cards[key] == cards["sh-judges"], key      # the same spot as the Judge Profiles card, so it does not jump


def test_every_picture_the_data_names_is_served_and_none_is_left_over():
    names = referenced_images()
    assert names
    for name in sorted(names):
        response = client.get(f"/tour-window/img/{name}")
        assert response.status_code == 200 and response.headers["content-type"] == "image/webp", name
    assert {path.name for path in IMG_DIR.glob("*.webp")} == names      # a picture nobody shows is dead weight


@pytest.mark.parametrize("name", ["x.png", "..%2Ftour_data.json", "a/b.webp", "missing.webp"])
def test_only_plain_webp_files_of_the_tour_are_served(name):
    assert client.get(f"/tour-window/img/{name}").status_code in (404, 405)


def test_steps_are_numbered_in_order_with_words_and_a_screen_each():
    steps = window_steps()
    assert [step["step"] for step in steps] == list(range(1, len(steps) + 1))
    assert len({step["id"] for step in steps}) == len(steps)
    for step in steps:
        assert step["title"].strip() and step["final"].endswith(".webp"), step["id"]
        assert step["text"].strip() or step["id"] == "sh-about", step["id"]     # the About card is a question and a picture
    assert steps[-1]["buttons"] and "Explore the site yourself" in steps[-1]["buttons"][0]["label"]


def test_highlights_cards_and_pointer_stay_on_the_screen():
    for step in window_steps():
        for ring in step["rings"]:
            assert ring["x"] >= 0 and ring["y"] >= -20 and ring["x"] + ring["w"] <= 1440 and ring["w"] > 0 and ring["h"] > 0, step["id"]
        assert 0 <= step["card"]["x"] <= 1040, step["id"]
        for action in step["actions"]:
            if action["do"] == "move":
                assert 0 <= action["x"] <= 1440 and 0 <= action["y"] <= 900, step["id"]
            if action["do"] == "type":
                assert action["text"].strip() and action["field"]["w"] > 0, step["id"]
            if action["do"] in ("scroll", "seq"):
                assert len(action["frames"]) > 4, step["id"]


def test_no_step_invites_the_visitor_to_click_or_scroll():
    text = " ".join(f"{step['title']} {step['text']}" for step in window_steps()).lower()
    for phrase in ("feel free", "try for yourself", "try hovering", "live site walkthrough", "not a pre-recorded"):
        assert phrase not in text, phrase
    assert "well known decision" in text and "popular decision" not in text


def test_tour_makes_no_outside_calls_and_no_ai():
    source = (window_loader() + routes.tour_window_page().body.decode()).lower()
    assert "openai" not in source and "xmlhttprequest" not in source
    assert "/tour-window/" in source and "http://" not in source


def test_explorer_and_workbench_open_the_window_once():
    for html in (routes._data_explorer_page_html(), workbench_page_html()):
        assert html.count("/tour-window.js") == 1 and "/site-tour.js" not in html and "/site-tour.css" not in html
    assert inject_site_tour(inject_site_tour("<head></head><body></body>")).count("/tour-window.js") == 1


@pytest.mark.skipif(not shutil.which("node"), reason="node is needed to syntax-check the script")
def test_opener_script_parses(tmp_path):
    script = tmp_path / "loader.js"
    script.write_text(window_loader(), encoding="utf-8")
    assert subprocess.run(["node", "--check", str(script)], capture_output=True).returncode == 0


def test_data_is_one_file_the_player_reads():
    assert json.loads(window_data())["config"]["timing"]["typeMs"] > 0


def test_data_carries_a_version_so_a_recapture_skips_the_picture_cache():
    assert json.loads(window_data())["config"]["version"]
