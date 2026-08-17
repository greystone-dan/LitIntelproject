from types import SimpleNamespace

from backend import routes


class ScalarDatabase:
    def __init__(self, scalar_values):
        self.scalar_values = iter(scalar_values)

    def scalar(self, statement):
        return next(self.scalar_values)


def test_about_stats_returns_library_counts():
    database = ScalarDatabase([10, 20, 15, 3])

    result = routes.about_stats(database)

    assert result == {
        "cases": 10,
        "citations": 20,
        "linked_citations": 15,
        "judge_profiles": 3,
    }


def test_citation_intelligence_routes_delegate_to_existing_helpers(monkeypatch):
    case = SimpleNamespace(id=7)
    database = object()
    monkeypatch.setattr(routes, "_get_case_or_404", lambda case_id, db: case)
    monkeypatch.setattr(routes, "_ci_overview", lambda db, case_id: {"case_id": case_id})
    monkeypatch.setattr(routes, "_ci_timeline", lambda db, case_id: [{"year": 2025}])

    assert routes.citation_intelligence_overview(7, database) == {"case_id": 7}
    assert routes.citation_intelligence_timeline(7, database) == [{"year": 2025}]


def test_compatibility_routes_select_tabs():
    assert routes.about_page().headers["location"] == "/data-explorer?tab=about"
    assert routes.citation_intelligence_page().headers["location"] == "/data-explorer?tab=citation-intelligence"
    assert routes.judges_page().headers["location"] == "/data-explorer?tab=judge-profile"


def test_rendered_shell_exposes_six_tabs_and_product_title():
    html = routes._data_explorer_page_html()

    for label in (
        "About",
        "Case search",
        "Citation Intelligence",
        "Judge outcomes",
        "Judge Profile",
        "Data explorer",
        "Immigration Litigation Intelligence Tool",
    ):
        assert label in html

    assert "Decision desk" not in html
    assert "Litigation workbench" not in html
    assert "Case search and analytics" not in html
