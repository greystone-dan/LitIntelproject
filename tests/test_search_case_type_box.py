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
    assert "['Case type',caseTypeText(d)]" in js
    assert "d.readerData.case_type" in js
