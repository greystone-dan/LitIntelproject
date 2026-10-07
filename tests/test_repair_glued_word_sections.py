import csv

import pytest

from scripts import repair_glued_word_sections as script
from scripts.repair_glued_word_sections import corrected_section, section_from_reference


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("section 20.1", "20.1"),
        ("S. 2d", "2"),
        ("s.40(1)(a)", "40"),
        ("paragraph 186(s)", "186"),
        ("sections 34, 35 and 37", "34"),
        ("s. 97of", "97"),
        ("Criminal Code", None),
        (None, None),
    ],
)
def test_section_is_read_from_the_cited_text(reference, expected):
    assert section_from_reference(reference) == expected


def test_glued_rows_are_repaired_from_the_cited_text():
    assert corrected_section("25s", "section 20.1", "25s") == "20.1"
    assert corrected_section("2d", "S. 2d", "2d") == "2"
    assert corrected_section("97of", "s. 97of", "97o") == "97"
    assert corrected_section("30para", "paragraph 186(s)", "30p") == "186"


def test_legitimate_or_unreadable_rows_are_left_alone():
    assert corrected_section("224A", "s. 224A", "224a") is None  # uppercase pinpoint
    assert corrected_section("224a(1)(a)", "s. 224a(1) (a)", "224a") is None  # a bracket follows the letter
    assert corrected_section("25s", "the Act", "25s") is None  # no section in the text
    assert corrected_section("96s", "s.96", "96") is None  # already the same


def test_select_excludes_old_lettered_instruments():
    assert "canada.criminal_code" in script.SELECT_SQL.text and "canada.income_tax_act" in script.SELECT_SQL.text


def test_apply_writes_undo_then_undo_restores(monkeypatch, tmp_path):
    rows = [
        (1, "canada.irpa", "25s", "section 20.1", "25s"),
        (2, "canada.charter", "2d", "S. 2d", "2d"),
        (3, "canada.irpa", "96s", "the Act", "96s"),
    ]
    updates = []

    class Result:
        def __init__(self, data=None, rowcount=0):
            self._data, self.rowcount = data or [], rowcount

        def all(self):
            return self._data

    class Session:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def execute(self, statement, params=None):
            sql = str(statement)
            if sql.startswith("SELECT"):
                return Result([r for r in rows if r[0] > params["after"]][: params["limit"]])
            updates.append((sql.split()[3], params))
            return Result(rowcount=len(params))

        def commit(self):
            pass

    monkeypatch.setattr(script, "SessionLocal", lambda: Session())
    undo_file = tmp_path / "undo.csv"
    result = script.run(True, 10, undo_file)
    assert result["stats"]["updated"] == 2 and result["stats"]["left_alone"] == 1
    assert [(r["id"], r["old_section"], r["new_section"]) for r in csv.DictReader(open(undo_file))] == [
        ("1", "25s", "20.1"),
        ("2", "2d", "2"),
    ]
    assert script.undo(undo_file) == 2
