import json
from pathlib import Path

from backend.i18n import MESSAGES, message, render_about_fragment
from backend.pages.data_explorer import data_explorer_page_html
from backend.routes import data_explorer_page
from scripts.inventory_ui_strings import (
    JSON_OUTPUT,
    REPORT_OUTPUT,
    build_inventory,
    extract_source_strings,
)


def test_catalog_keys_match_and_missing_french_messages_fall_back_to_english(monkeypatch):
    assert MESSAGES["en"].keys() == MESSAGES["fr"].keys()
    monkeypatch.delitem(MESSAGES["fr"], "about.title")
    assert message("about.title", "fr") == MESSAGES["en"]["about.title"]
    assert message("unknown.message", "fr") == "unknown.message"


def test_about_page_keeps_english_default_and_sets_french_language_attribute():
    english = data_explorer_page_html()
    french = data_explorer_page_html("fr")
    fragment_path = Path(__file__).resolve().parents[1] / "backend" / "pages" / "about_content.html"
    template = fragment_path.read_text(encoding="utf-8")
    expected_english_fragment = (
        template.replace("{{about.title}}", MESSAGES["en"]["about.title"])
        .replace("{{about.lede}}", MESSAGES["en"]["about.lede"])
        .replace("{{about.nav_today}}", MESSAGES["en"]["about.nav_today"])
        .replace("{{about.nav_how}}", MESSAGES["en"]["about.nav_how"])
        .replace("{{about.nav_files}}", MESSAGES["en"]["about.nav_files"])
    )

    assert '<html lang="en">' in english
    assert "iLit: where the project stands" in english
    assert "{{about." not in english
    assert render_about_fragment(template, "en") == expected_english_fragment
    assert "French preview" not in english
    assert '<html lang="fr">' in french
    assert "iLit : où en est le projet" in french
    assert "Aperçu français rédigé par machine" in french
    assert 'href="/data-explorer?tab=about">English</a>' in french
    assert data_explorer_page(lang="fr").body.decode("utf-8") == french


def test_inventory_extracts_context_placeholders_and_literal_route_errors(tmp_path):
    fixture = tmp_path / "sample.html"
    fixture.write_text(
        '<h1>Overview</h1><button>Save</button><label>Case {case_id}</label>'
        '<span title="More information" aria-label="Close panel">Text</span>',
        encoding="utf-8",
    )
    html_items = extract_source_strings(fixture, fixture.read_text(encoding="utf-8"), tmp_path)
    assert {(item["string"], item["context_kind"]) for item in html_items} >= {
        ("Overview", "heading"),
        ("Save", "button"),
        ("Case {case_id}", "label"),
        ("More information", "tooltip"),
        ("Close panel", "aria-label"),
    }
    assert next(item for item in html_items if item["string"] == "Case {case_id}")[
        "contains_placeholders"
    ]

    routes = tmp_path / "routes.py"
    routes.write_text(
        'raise HTTPException(status_code=404, detail="Record not found")\n',
        encoding="utf-8",
    )
    route_items = extract_source_strings(routes, routes.read_text(encoding="utf-8"), tmp_path)
    assert {
        (item["string"], item["context_kind"]) for item in route_items
    } == {("Record not found", "error")}


def test_inventory_script_builds_expected_machine_and_human_reports(tmp_path):
    fixture = tmp_path / "fixture.html"
    fixture.write_text("<h2>Fixture heading</h2>", encoding="utf-8")
    inventory = build_inventory([fixture], tmp_path)

    assert inventory["item_count"] == 1
    assert inventory["items"][0] == {
        "file": "fixture.html",
        "line": 1,
        "string": "Fixture heading",
        "context_kind": "heading",
        "contains_placeholders": False,
    }
    assert JSON_OUTPUT.name == "ui-strings.json"
    assert REPORT_OUTPUT.name == "french-ui-inventory.md"
    assert json.loads(json.dumps(inventory))["item_count"] == 1

    app_inventory = build_inventory()
    assert "backend/i18n.py" in app_inventory["sources"]
    assert any(
        item["file"] == "backend/i18n.py"
        and item["string"] == MESSAGES["en"]["about.title"]
        for item in app_inventory["items"]
    )
