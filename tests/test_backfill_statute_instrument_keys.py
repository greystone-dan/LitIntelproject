import csv

from scripts import backfill_statute_instrument_keys as script


class _Result:
    def __init__(self, rows=None, rowcount=0):
        self._rows = rows or []
        self.rowcount = rowcount

    def all(self):
        return self._rows


class _FakeSession:
    def __init__(self, rows):
        self._rows = rows
        self.updates = []
        self.committed = 0

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def execute(self, statement, params=None):
        sql = str(statement)
        if sql.startswith("SELECT"):
            after = params["after"]
            batch = [r for r in self._rows if r[0] > after][: params["limit"]]
            return _Result(batch)
        if "SET instrument_key = :key" in sql and "IS NULL" in sql.split("WHERE")[1]:
            self.updates.extend(params)
            return _Result(rowcount=len(params))
        return _Result(rowcount=len(params))

    def commit(self):
        self.committed += 1


ROWS = [
    (1, "Patent Act s. 27(3)", "FC"),
    (2, "Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the Act)", "FC"),
    (3, "Privacy Act", "SCC"),
    (4, "Motor Vehicle Act", "FC"),
    (5, "Privacy Act", "FC"),
]


def test_dry_run_counts_and_writes_nothing(monkeypatch, tmp_path):
    session = _FakeSession(ROWS)
    monkeypatch.setattr(script, "SessionLocal", lambda: session)
    result = script.run(False, 10, None, tmp_path / "undo.csv")
    assert result["stats"] == {"seen": 5, "resolved": 3, "unresolved": 2}
    assert dict(result["per_key"]) == {"canada.patent_act": 1, "canada.irpa": 1, "canada.privacy_act": 1}
    assert session.updates == []
    assert not (tmp_path / "undo.csv").exists()


def test_apply_writes_undo_file_before_updating(monkeypatch, tmp_path):
    session = _FakeSession(ROWS)
    monkeypatch.setattr(script, "SessionLocal", lambda: session)
    undo = tmp_path / "undo.csv"
    result = script.run(True, 2, None, undo)
    assert result["stats"]["updated"] == 3
    assert {(u["id"], u["key"]) for u in session.updates} == {
        (1, "canada.patent_act"),
        (2, "canada.irpa"),
        (5, "canada.privacy_act"),
    }
    rows = list(csv.DictReader(open(undo, encoding="utf-8")))
    assert [(int(r["id"]), r["instrument_key"]) for r in rows] == [(1, "canada.patent_act"), (2, "canada.irpa"), (5, "canada.privacy_act")]


def test_undo_reads_the_file(monkeypatch, tmp_path):
    undo = tmp_path / "undo.csv"
    undo.write_text("id,instrument_key\n1,canada.patent_act\n2,canada.irpa\n", encoding="utf-8")
    session = _FakeSession([])
    monkeypatch.setattr(script, "SessionLocal", lambda: session)
    assert script.undo(undo) == 2
