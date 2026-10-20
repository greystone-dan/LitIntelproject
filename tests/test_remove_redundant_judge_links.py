"""scripts/remove_redundant_judge_links.py: selection rules, junk guard, checks, apply/undo round trip (fake DB)."""

import csv
from datetime import datetime, timezone

import pytest

from scripts import remove_redundant_judge_links as rrjl

class _Result:
	def __init__(self, rows=None, rowcount=0, scalar=None):
		self._rows, self.rowcount, self._scalar = rows or [], rowcount, scalar

	def mappings(self):
		return self

	def all(self):
		return self._rows

	def scalar(self):
		return self._scalar


class FakeDB:
	"""Records statements; `handler(sql, params)` returns a _Result (or None for an empty one)."""

	def __init__(self, handler=None):
		self.handler = handler
		self.calls, self.commits = [], 0

	def execute(self, statement, params=None):
		sql = " ".join(str(statement).split())
		self.calls.append((sql, params))
		return (self.handler(sql, params) if self.handler else None) or _Result()

	def commit(self):
		self.commits += 1

	def rollback(self):
		pass


class _Ctx:
	def __init__(self, db):
		self.db = db

	def __enter__(self):
		return self.db

	def __exit__(self, *exc):
		return False

STAMP = datetime(2026, 10, 20, 8, 12, 45, tzinfo=timezone.utc)


def link(id, case_id, profile, name, court="FC", citation=None):
	return {"id": id, "case_id": case_id, "judge_profile_id": profile, "raw_name": name, "created_at": STAMP,
		"court": court, "citation": citation or f"2020 {court} {case_id}", "display_name": name}


ROWS = [
	link(100, 1, 10, "Simon Noël"), link(158700, 1, 11, "NOËL J."),  # same judge twice: remove the new one
	link(101, 2, 12, "Gagné J."), link(158701, 2, 13, "AND ORDER"),  # junk new link: remove
	link(102, 3, 14, "AND ORDER"), link(158702, 3, 15, "Gagné J."),  # junk OLD link: skip and report
	link(103, 4, 16, "ROTHSTEIN J.A.", "FCA"), link(104, 4, 17, "EVANS J.A.", "FCA"),
	link(105, 4, 18, "SHARLOW J.A.", "FCA"), link(158703, 4, 16, "ROTHSTEIN J.A.", "FCA"),
	link(158800, 5, 19, "Roy J.", "SCC"), link(120, 5, 20, "Roy J.", "SCC"),  # SCC is never touched
	link(200000, 6, 21, "Late J."), link(121, 6, 22, "Late J."),  # id above the run range is not a new link
]


def test_plan_removes_only_new_links_on_decisions_with_an_older_link():
	result = rrjl.plan(ROWS)
	assert sorted(r["id"] for r in result["removals"]) == [158700, 158701, 158703]
	assert [s["case_id"] for s in result["skipped"]] == [3]
	assert result["skipped"][0]["junk_old_names"] == ["AND ORDER"]
	assert all(r["kept"] for r in result["removals"])


def test_junk_pattern_matches_k3():
	for name in ("AND ORDER", "Schedule of exemplar documents", "March 13, 2001", "Smith �", "Reasons for judgment"):
		assert rrjl.is_junk_name(name)
	for name in ("Gagné J.", "Orderly J.", "NOËL J.A.", None):
		assert not rrjl.is_junk_name(name)


def test_checks_k7_k10_k11_before_and_after():
	result = rrjl.plan(ROWS)
	cases = rrjl.group_by_case(ROWS)
	after = rrjl.projected_links(ROWS, result["removals"])
	b = rrjl.link_stats({c: cases[c] for c in (1, 4)})
	a = rrjl.link_stats({c: after[c] for c in (1, 4)})
	assert (b["K7"]["FC"], a["K7"]["FC"]) == (1, 0)  # FC ceiling is 1
	assert (b["K10"]["FCA"], a["K10"]["FCA"]) == (1, 0)  # Rothstein twice
	assert (b["K11"]["FC"], a["K11"]["FC"]) == (1, 0)  # Simon Noël / NOËL J. share a surname
	assert a["K7"]["FCA"] == 0  # 3 judges on a panel is within the FCA ceiling of 5


def test_surname_tokens_ignore_titles_and_accents():
	assert rrjl.surname_tokens("CHIEF JUSTICE BLAIS") == {"blais"}
	assert rrjl.surname_tokens("NOËL J.A.") == {"noel"}
	assert rrjl.surname_tokens("Simon Noël") & rrjl.surname_tokens("NOËL J.A.")


def test_projected_csv_lists_every_pair(tmp_path):
	result = rrjl.plan(ROWS)
	before, after = rrjl.group_by_case(ROWS), rrjl.projected_links(ROWS, result["removals"])
	path = tmp_path / "out.csv"
	assert rrjl.write_csv(path, rrjl.csv_rows(result["removals"], after, before)) == 3
	rows = list(csv.DictReader(open(path, encoding="utf-8")))
	assert {r["removed_link_id"] for r in rows} == {"158700", "158701", "158703"}
	assert next(r for r in rows if r["removed_link_id"] == "158700")["same_surname_as_a_kept_name"] == "True"
	assert next(r for r in rows if r["removed_link_id"] == "158701")["removed_is_junk"] == "True"
	with pytest.raises(FileExistsError):
		rrjl.write_csv(path, [])


def test_apply_writes_change_log_first_then_deletes_and_undo_reinserts(tmp_path):
	removals = rrjl.plan(ROWS)["removals"]
	db = FakeDB(lambda sql, params: _Result(rowcount=1) if sql.startswith(("DELETE", "INSERT")) else None)
	log = tmp_path / "log.jsonl"
	assert rrjl.apply_removals(db, removals, log) == 3
	assert [p["id"] for s, p in db.calls if s.startswith("DELETE")] == [158700, 158701, 158703]
	assert db.commits == 1
	logged = list(rrjl.read_undo_file(log))
	assert [r["id"] for r in logged] == [158700, 158701, 158703]
	assert set(logged[0]) == {"id", "case_id", "judge_profile_id", "raw_name", "created_at"}
	db2 = FakeDB(lambda sql, params: _Result(rowcount=1) if sql.startswith("INSERT") else None)
	assert rrjl.restore(db2, log) == (3, 3)
	assert db2.calls[0][1]["id"] == 158700 and db2.calls[0][1]["created_at"].startswith("2026-10-20T08:12:45")


def test_apply_rolls_back_when_a_row_was_already_gone(tmp_path):
	removals = rrjl.plan(ROWS)["removals"]
	db = FakeDB(lambda sql, params: _Result(rowcount=0) if sql.startswith("DELETE") else None)
	rolled = []
	db.rollback = lambda: rolled.append(1)
	with pytest.raises(RuntimeError):
		rrjl.apply_removals(db, removals, tmp_path / "log.jsonl")
	assert rolled and db.commits == 0


def _fake_session(monkeypatch):
	def handler(sql, params):
		if sql.startswith("SELECT l.id"):
			return _Result(rows=ROWS)
		if sql.startswith("SELECT court, count(*) AS decisions, count(*) FILTER"):
			return _Result(rows=[{"court": "FC", "decisions": 5, "over_ceiling": 2}, {"court": "FCA", "decisions": 1, "over_ceiling": 0}])
		if sql.startswith("SELECT court, count(*) AS decisions FROM"):
			return _Result(rows=[{"court": "FCA", "decisions": 1}])
		if sql.startswith("SELECT count(*) FROM case_judge_profiles"):
			return _Result(scalar=50)
	db = FakeDB(handler)
	monkeypatch.setattr(rrjl, "SessionLocal", lambda: _Ctx(db))
	return db


def test_main_dry_run_writes_nothing_and_prints_count(monkeypatch, capsys):
	db = _fake_session(monkeypatch)
	assert rrjl.main([]) == 0
	out = capsys.readouterr().out
	assert "redundant_links_to_remove=3 (FC 2, FCA 1)" in out
	assert "skipped_junk_old_link_decisions=1" in out
	assert "case_judge_profiles rows: before=50 after=47" in out
	assert "K7 (ceiling 1) FC: database now=2 projected=0" in out
	assert not any(s.startswith(("DELETE", "INSERT")) for s, _ in db.calls)


def test_main_apply_needs_expected_count_and_refuses_a_wrong_one(monkeypatch, tmp_path):
	db = _fake_session(monkeypatch)
	with pytest.raises(SystemExit):
		rrjl.main(["--apply"])
	assert rrjl.main(["--apply", "--expected-count", "99", "--undo-file", str(tmp_path / "x.jsonl")]) == 1
	assert not any(s.startswith("DELETE") for s, _ in db.calls)
	assert not (tmp_path / "x.jsonl").exists()
