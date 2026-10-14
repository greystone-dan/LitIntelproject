"""The feature inventory is the one list behind the Coming soon page and the Lab status board."""

import json

from backend.pages import coming_soon_preview_page as preview
from backend.pages import roadmap_page
from backend.pages.coming_soon_content import SECTIONS
from backend.pages.feature_inventory import inventory

SLUGS = [entry[0] for area in SECTIONS.values() for entry in area["items"]]


def test_every_feature_has_an_inventory_entry_and_nothing_extra():
    assert sorted(SLUGS) == sorted(inventory()["items"])


def test_inventory_keys_are_valid_and_timing_matches_where_the_item_stands():
    inv = inventory()
    workflows = {w["key"] for w in inv["workflows"]}
    horizons = {h["key"] for h in inv["horizons"]}
    ais = {a["key"] for a in inv["ai"]}
    passes = {p["key"] for p in json.loads(preview.EXAMPLES_FILE.read_text(encoding="utf-8"))["passes"]}
    for slug, info in inv["items"].items():
        assert info["workflow"] in workflows and info["horizon"] in horizons and info["ai"] in ais
        assert info["audience"] in inv["audiences"] and info["purpose"].strip()
        assert not info.get("evidence") or info["evidence"] in passes  # an evidence link points at a real card
        place = roadmap_page.place_of(slug)
        assert (info["horizon"] == "now") == (place == "live"), slug  # "Now" means on the site today, nothing else


def test_coming_soon_and_the_status_board_list_the_same_features_with_the_same_labels():
    page = preview.render()
    board = roadmap_page.render()
    inv = inventory()["items"]
    for slug, info in inv.items():
        assert f'id="f-{slug}"' in page and f'id="{slug}"' in board
        assert f'data-when="{info["horizon"]}"' in board.split(f'id="{slug}"', 1)[1][:400]
    assert f"{len(inv)} features" in page


def test_a_feature_with_a_test_number_shows_it_on_its_row():
    page = preview.render()
    row = page.split('id="f-whose-position"', 1)[1].split("</li>", 1)[0]
    assert "76% tested" in row and 'href="#pass-position"' in row


def test_workflows_open_with_reading_a_case():
    keys = [w["key"] for w in inventory()["workflows"]]
    assert keys[:2] == ["read", "find"]
