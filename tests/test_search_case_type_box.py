"""Search result cards show the stored case type as an info box; courts without labels show nothing."""

from backend.analytics_service import _page_case_types
from backend.case_types import TAXONOMY_VERSION


class _Result:
    def __init__(self, rows):
        self._rows = rows

    def mappings(self):
        return self

    def all(self):
        return self._rows


class _FakeDb:
    def __init__(self, rows):
        self.rows, self.calls = rows, []

    def execute(self, statement, params):
        self.calls.append((str(statement), params))
        return _Result(self.rows)


def _row(case_id, **kw):
    base = dict(case_id=case_id, taxonomy_version=TAXONOMY_VERSION, status="classified",
                primary_type="inadmissibility_security", primary_detail="34(1)(f)", second_type=None, second_detail=None)
    base.update(kw)
    return base


def test_one_batched_query_and_only_classified_rows_shown():
    db = _FakeDb([_row(1), _row(2, status="unclear", primary_type=None), _row(3, status="insufficient_text")])
    found = _page_case_types(db, [1, 2, 3, 4])
    assert list(found) == [1]
    assert found[1]["primary"]["provision"] == "s. 34(1)(f)"
    assert len(db.calls) == 1 and "IN" in db.calls[0][0] and db.calls[0][1]["ids"] == [1, 2, 3, 4]


def test_no_ids_no_query():
    db = _FakeDb([])
    assert _page_case_types(db, []) == {}
    assert db.calls == []


def test_v6_card_draws_box_only_when_a_type_exists():
    from pathlib import Path

    js = Path("backend/pages/search_v6.js").read_text(encoding="utf-8")
    assert "if(!t||!t.primary||!t.primary.label)return ''" in js
    assert "typeBox(item.case_type)" in js
    assert ".sp-bx.type" in Path("backend/pages/search_v6.css").read_text(encoding="utf-8")


def test_v6_reader_title_card_and_about_show_case_type_when_stored():
    from pathlib import Path

    js = Path("backend/pages/reader_v6.js").read_text(encoding="utf-8")
    assert "cell('Case type',caseTypeText(d))" in js
    assert "d.readerData.case_type" in js



def _search(case_type):
    from backend.analytics_service import fetch_analytics_search_cases

    db = _FakeDb([])
    fetch_analytics_search_cases(db, case_type=case_type, include_facets=False, include_citation_stats=False, sort_by="newest")
    sql, params = db.calls[0]
    return sql, params


def test_filter_accepts_several_case_types_as_bound_params():
    sql, params = _search("refugee_claim, detention ,refugee_claim")
    assert "ctl.primary_type IN (:case_type_0, :case_type_1)" in sql and "ctl.second_type IN (:case_type_0, :case_type_1)" in sql
    assert params["case_type_0"] == "refugee_claim" and params["case_type_1"] == "detention"
    assert "case_type_2" not in params


def test_filter_single_type_still_works_and_unknown_matches_nothing():
    sql, params = _search("detention")
    assert "IN (:case_type_0)" in sql and params["case_type_0"] == "detention"
    sql, _ = _search("not_a_type")
    assert "FALSE" in sql and "case_type_labels" not in sql
    sql, _ = _search("")
    assert "case_type_labels" not in sql


def test_advanced_rail_lists_every_type_grouped_with_a_hidden_value_field():
    from backend.case_types import CASE_TYPES
    from backend.pages.data_explorer import data_explorer_page_html

    html = data_explorer_page_html()
    assert 'id="caseTypeBoxes"' in html and '<input id="caseTypeFilter">' in html
    assert html.count('class="sp-ct-box"') == len(CASE_TYPES)
