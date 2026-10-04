import ast
from pathlib import Path

from backend.pages.data_explorer import data_explorer_page_html
from scripts.generate_ui_string_inventory import build_inventory, extract_source_strings


def test_static_ui_string_extractor_covers_literal_text_and_accessible_attributes():
    source = Path("backend/pages/example.html")
    found = extract_source_strings(
        source,
        '<button aria-label="Open menu">Open</button>'
        '<input placeholder="Find a case">'
        '<script>element.textContent = "runtime only"</script>'
        '<style>.label { color: red }</style>',
    )

    assert {(item["text"], item["kind"]) for item in found} == {
        ("Open menu", "aria-label"),
        ("Open", "text"),
        ("Find a case", "placeholder"),
    }


def test_inventory_source_lines_remain_accurate_after_style_exclusion():
    found = extract_source_strings(
        Path("backend/pages/example.html"),
        "\n<style>\n.hidden { color: red }\n</style>\n<button>Visible</button>",
    )

    assert [(item["text"], item["line"]) for item in found] == [("Visible", 5)]


def test_inventory_declares_static_source_coverage_and_includes_active_ui_sources():
    inventory = build_inventory()

    assert inventory["item_count"] == len(inventory["items"])
    assert "Dynamically generated JavaScript text" in inventory["coverage"]
    assert "data/API-derived labels" in inventory["coverage"]
    assert "backend/pages/about_content.html" in inventory["sources"]
    assert "backend/routes.py" in inventory["sources"]
    assert any(item["text"] == "iLit: where the project stands" for item in inventory["items"])


def test_about_page_has_scoped_english_default_and_french_preview():
    page = data_explorer_page_html()
    about_start = page.index('<section id="aboutPanel"')
    about_end = page.index('<section id="searchPanel"', about_start)
    about = page[about_start:about_end]

    assert '<html lang="en">' in page
    assert 'data-about-locale="en" aria-pressed="true"' in about
    assert 'data-about-locale="fr" aria-pressed="false"' in about
    assert "L’aperçu français couvre uniquement cette présentation" in about
    assert 'data-about-i18n="title"' in about
    assert 'document.querySelector(".ilit-about")?.setAttribute("lang", language)' in about
    assert "the remaining page is in English" in about
    assert "window.location" not in about


def test_start_route_is_absent_and_about_compatibility_route_is_present():
    paths = set()
    for source in (Path("backend/main.py"), Path("backend/routes.py")):
        tree = ast.parse(source.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            for decorator in getattr(node, "decorator_list", ()):
                if not isinstance(decorator, ast.Call) or not decorator.args:
                    continue
                path = decorator.args[0]
                if isinstance(path, ast.Constant) and isinstance(path.value, str):
                    paths.add(path.value)

    assert "/start" not in paths
    assert "/about" in paths
