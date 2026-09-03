from types import SimpleNamespace

from backend import routes
from backend.citation_map import _build_citation_intelligence_insights


class ScalarDatabase:
    def __init__(self, scalar_values):
        self.scalar_values = iter(scalar_values)

    def scalar(self, statement):
        return next(self.scalar_values)


def test_about_stats_returns_library_counts():
    database = ScalarDatabase([10, 11, 12, 13, 20, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    result = routes.about_stats(database)

    assert result == {
        "cases": 10,
        "case_chunks": 11,
        "case_sources": 12,
        "ingestion_runs": 13,
        "citations": 20,
        "linked_citations": 15,
        "judge_profiles": 3,
        "case_judge_profiles": 4,
        "citation_metrics": 5,
        "statute_references": 6,
        "case_tags": 7,
        "case_chunk_embeddings": 8,
        "fc_activity_cases": 9,
        "fc_activity_documents": 10,
        "fc_procedural_history": 11,
    }


def test_build_citation_intelligence_insights_are_actionable():
    insights = _build_citation_intelligence_insights(
        unique_citing_cases=12,
        total_occurrences=47,
        avg_mentions_per_case=3.9,
        max_mentions_in_single_case=12,
        top_citing_case={"title": "A v. Canada", "mention_count": 12},
        top_court={"court": "Federal Court", "case_count": 9},
        top_judge={"judge": "Justice Smith", "case_count": 4},
        top_statute={"provision": "IRPA s. 34(1)(f)", "case_count": 6},
    )

    assert len(insights) >= 4
    assert any(item["title"] == "Most active citing decision" for item in insights)
    assert any(item["title"] == "Top court" for item in insights)
    assert any("IRPA" in item["detail"] for item in insights)


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
    assert routes.fc_history_page().headers["location"] == "/data-explorer?tab=fc-history"


def test_rendered_shell_exposes_tabs_and_product_title():
    html = routes._data_explorer_page_html()

    for label in (
        "About",
        "Case search",
        "Site Architecture",
        "Citation Intelligence",
        "Judge outcomes",
        "Judge Profile",
        "Data explorer",
        "FC History",
        "Immigration Litigation Intelligence Tool",
    ):
        assert label in html

    assert "Decision desk" not in html
    assert "Litigation workbench" not in html
    assert "Case search and analytics" not in html
    assert 'id="aboutOutcomeChart"' not in html


def test_site_architecture_panel_lists_data_layers_and_feature_map():
    html = routes._data_explorer_page_html()

    for label in (
        "Data inventory",
        "Case records",
        "Citation records",
        "Judge profiles",
        "Federal Court activity",
        "Feature-to-data map",
    ):
        assert label in html


def test_citation_intelligence_case_search_is_title_scoped():
    case = SimpleNamespace(
        id=12,
        title="Vavilov v. Canada (Citizenship and Immigration)",
        citation="2019 SCC 65",
        court="SCC",
        date="2019-12-19",
    )

    class Database:
        def scalars(self, statement):
            return iter([case])

    result = routes.citation_intelligence_cases("Vavilov", 12, Database())

    assert result == [
        {
            "case_id": 12,
            "title": case.title,
            "citation": case.citation,
            "court": case.court,
            "date": case.date,
        }
    ]


def test_rendered_shell_exposes_focused_feature_searches():
    html = routes._data_explorer_page_html()

    assert 'id="citationCaseQuery"' in html
    assert 'Find a case by title' in html
    assert 'id="judgeProfileQuery"' in html
    assert 'Find a judge by name' in html
    assert '<option value="newest" selected>Newest decision</option>' in html

    for subtab in ("Overview", "Timeline", "Outcomes", "Courts", "Judges", "Companions", "Statutes", "Evidence"):
        assert subtab in html

    assert "Research readout" in html
    assert "Open citation evidence" in html
    assert "Compare use over time" in html


def test_judge_profiles_default_to_most_linked_profiles():
    class FakeProfile:
        def __init__(self, slug, display_name, case_link_count):
            self.slug = slug
            self.display_name = display_name
            self.primary_court = "Federal Court"
            self.aliases = []
            self.case_links = list(range(case_link_count))

    class Database:
        def scalars(self, statement):
            return iter([
                FakeProfile("judge-b", "Judge B", 2),
                FakeProfile("judge-a", "Judge A", 7),
                FakeProfile("judge-c", "Judge C", 4),
            ])

    result = routes.judge_profiles("", 10, Database())

    assert [item["slug"] for item in result] == ["judge-a", "judge-c", "judge-b"]


def test_rendered_shell_exposes_original_source_link_action():
    html = routes._data_explorer_page_html()

    assert 'Original source' in html


def test_rendered_shell_exposes_docket_to_fc_history_action():
    html = routes._data_explorer_page_html()

    assert 'Open FC History' in html
    assert 'data-fc-docket' in html
    assert 'fcHistoryForm' in html


def test_fc_history_tab_uses_full_entry_list_and_distinct_panel_mapping():
    html = routes._data_explorer_page_html()

    assert "'fc-history':'fcHistoryPanel'" in html
    assert 'const entries=(data.entries_json||[])' in html
    assert 'const entries=(data.entries_json||[]).map' in html
    assert 'slice(0,8)' not in html.split('const entries=', 1)[1].split('results.innerHTML', 1)[0]


def test_rendered_shell_exposes_case_reader_tag_tabs():
    html = routes._data_explorer_page_html()

    assert 'Case information' in html
    assert 'Header metadata' in html
    assert 'Extracted metadata' in html
    assert 'Case information' in html
    assert 'Tags' in html
