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
    }
    for sql, params in db.statements:
        assert "GROUP BY" in sql and "c.title ILIKE :q" in sql
        assert "limit" not in params and "offset" not in params


def test_results_page_has_sort_bar_and_facet_chips():
    html = data_explorer_page_html()
    assert 'id="quickSort"' in html and 'id="searchFacets"' in html
    assert "paintSearchRefine(data.facets,values,results.length)" in html
    assert "#searchFacets .facet-chip" in html
    assert "/analytics/search/facets?" in html and "params.set('facets','0')" in html


def test_citation_stats_load_after_results():
    html = data_explorer_page_html()
    assert "params.set('citation_stats','0')" in html and '/analytics/search/citation-stats?ids=' in html
