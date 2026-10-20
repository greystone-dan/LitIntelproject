from backend.analytics_service import _search_facets
from backend.pages.data_explorer import data_explorer_page_html


class _Result:
    def __init__(self, rows):
        self._rows = rows

    def mappings(self):
        return self

    def all(self):
        return self._rows


class _FakeDb:
    def __init__(self):
        self.statements = []

    def execute(self, statement, params):
        sql = str(statement)
        self.statements.append((sql, params))
        if sql.startswith("SELECT c.id FROM cases c WHERE"):
            return _Result([{"id": 11}, {"id": 12}, {"id": 13}])
        if "case_type_labels" in sql:
            return _Result([{"label": "refugee_claim", "n": 4}])
        if "c.court" in sql:
            return _Result([{"label": "FC", "n": 3}])
        return _Result([{"label": 2024, "n": 2}])


def test_facets_are_plain_sql_counts_without_paging_params():
    db = _FakeDb()
    facets = _search_facets(db, "c.title ILIKE :q", {"q": "%x%", "limit": 50, "offset": 0}, None)
    assert facets == {
        "court": [{"value": "FC", "count": 3}],
        "year": [{"value": "2024", "count": 2}],
        "case_type": [{"value": "refugee_claim", "label": "Refugee / protection claim (ss. 96-97)", "count": 4}],
        "total": 3,
    }
    first_sql, first_params = db.statements[0]
    assert "c.title ILIKE :q" in first_sql
    # The filter runs once; every count then reads the matching ids.
    assert sum("c.title ILIKE :q" in sql for sql, _ in db.statements) == 1
    for sql, params in db.statements[1:]:
        assert "GROUP BY" in sql and "c.id = ANY(CAST(:facet_match_ids AS integer[]))" in sql
        assert params["facet_match_ids"] == [11, 12, 13]
    for _sql, params in db.statements:
        assert "limit" not in params and "offset" not in params


def test_facets_for_no_matches_are_empty_without_further_queries():
    class Empty(_FakeDb):
        def execute(self, statement, params):
            self.statements.append((str(statement), params))
            return _Result([])

    db = Empty()
    assert _search_facets(db, "FALSE", {}, None) == {"court": [], "year": [], "case_type": [], "total": 0}
    assert len(db.statements) == 1


def test_results_page_has_sort_bar_and_facet_chips():
    html = data_explorer_page_html()
    assert 'id="quickSort"' in html and 'id="searchFacets"' in html
    assert "paintSearchRefine(data.facets,values,results.length)" in html
    assert "#searchFacets .facet-chip" in html
    assert "/analytics/search/facets?" in html and "params.set('facets','0')" in html


def test_citation_stats_load_after_results():
    html = data_explorer_page_html()
    assert "params.set('citation_stats','0')" in html and '/analytics/search/citation-stats?ids=' in html


def test_search_page_has_no_full_text_checkbox():
    html = data_explorer_page_html()
    assert "searchFullText" not in html and "Search the full decision text" not in html
    assert "Searching case names, citations and decision text..." in html


def test_court_filter_accepts_several_courts_and_page_reports_total_hook():
    class Db(_FakeDb):
        def execute(self, statement, params):
            self.last = (str(statement), params)
            return _Result([])

    from backend.analytics_service import fetch_analytics_search_cases

    db = Db()
    fetch_analytics_search_cases(db, court="FC, SCC,rpd")
    sql, params = db.last
    assert "UPPER(c.court) IN ('FC', 'FEDERAL COURT')" in sql
    assert params["court_1"] == "%SCC%" and params["court_2"] == "%rpd%"
    assert " OR " in sql.split("WHERE", 1)[1]
    html = data_explorer_page_html()
    assert "__spShowTotal(f.facets&&f.facets.total)" in html
    assert 'id="decisionOutcome"' not in html and "Decision result" not in html
    assert 'id="clearSearchTop"' in html and 'id="recentCases"' in html and 'id="mostCitedCases"' in html


def test_case_type_groups_have_a_select_all_box_and_clear_collapses_them():
    html = data_explorer_page_html()
    assert 'class="sp-ct-all"' in html and "window.__ctCollapse" in html and 'class="sp-cols"' in html
    assert html.index('class="sp-ct"') < html.index('for="citesFilter"')
