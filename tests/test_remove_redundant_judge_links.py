"""scripts/remove_redundant_judge_links.py: selection rules, junk guard, checks, apply/undo round trip (fake DB)."""

import csv
from datetime import datetime, timedelta, timezone

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

STAMP = datetime(2026, 10, 20, 8, 12, 45, tzinfo=timezone(timedelta(hours=-4)))


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
	link(122, 7, 23, "Avvy Yao-Yao Go"), link(158704, 7, 24, "Justice Go"),  # two-letter surname overlaps: remove
	link(123, 8, 25, "EVANS J.A.", "FCA"), link(158705, 8, 26, "THE COURT", "FCA"),  # name differs: needs a look
	link(124, 9, 27, "Gagné J."), link(158706, 9, 28, "Roy J."),  # name differs: needs a look
	link(126, 11, 31, "Marc Noël", "FCA"), link(158708, 11, 32, "Marc Nadon", "FCA"),  # shared given name only: needs a look
	link(125, 10, 29, "Tabib J."),
	{**link(158707, 10, 30, "Tabib J."), "created_at": datetime(2026, 10, 21, 9, 0, tzinfo=timezone.utc)},  # outside the run window
]


def test_plan_removes_only_same_judge_or_junk_new_links_on_decisions_with_an_older_link():
	result = rrjl.plan(ROWS)
	assert sorted(r["id"] for r in result["removals"]) == [158700, 158701, 158703, 158704]
	assert sorted(r["id"] for r in result["needs_look"]) == [158705, 158706, 158708]
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


def test_two_letter_surname_overlaps():
	assert rrjl.surname("Justice Go") == rrjl.surname("Avvy Yao-Yao Go") == "go"
	assert rrjl.surname("J.A. ROTHSTEIN") != rrjl.surname("Roy J.")


def test_unicode_dashes_do_not_split_a_surname_match():
	assert rrjl.surname("Tremblay\u2011Lamer J.") == rrjl.surname("Tremblay-Lamer J.") == "lamer"
	assert rrjl.surname("Layden\u2212Stevenson J.A.") == rrjl.surname("LAYDEN-STEVENSON J.A.")
	assert rrjl.shared_surname("Tremblay\u2011Lamer J.", [{"display_name": "Tremblay-Lamer"}]) == "lamer"


def test_gate_compares_surnames_not_given_names():
	assert rrjl.surname("Marc Nadon") == "nadon" and rrjl.surname("NOËL J.A.") == "noel"
	assert rrjl.surname("Noël, Simon") == rrjl.surname("Simon Noël") == "noel"
	assert rrjl.surname("CHIEF JUSTICE BLAIS") == "blais" and rrjl.surname("THE COURT") == "court"
	kept = [{"display_name": "Marc Noël"}]
	assert rrjl.shared_surname("Marc Nadon", kept) == ""  # same given name, different judge
	assert rrjl.shared_surname("NOËL J.A.", kept) == "noel"


def test_surname_tokens_ignore_titles_and_accents():
	assert rrjl.surname_tokens("CHIEF JUSTICE BLAIS") == {"blais"}
	assert rrjl.surname_tokens("NOËL J.A.") == {"noel"}
	assert rrjl.surname_tokens("Simon Noël") & rrjl.surname_tokens("NOËL J.A.")


def test_projected_csv_lists_every_pair(tmp_path):
	result = rrjl.plan(ROWS)
	before, after = rrjl.group_by_case(ROWS), rrjl.projected_links(ROWS, result["removals"])
	path = tmp_path / "out.csv"
	assert rrjl.write_csv(path, rrjl.csv_rows(result["removals"], result["needs_look"], after, before)) == 7
	rows = list(csv.DictReader(open(path, encoding="utf-8")))
	assert {r["removed_link_id"] for r in rows if r["action"] == "remove"} == {"158700", "158701", "158703", "158704"}
	assert {r["removed_link_id"] for r in rows if r["action"] == "needs_human_look"} == {"158705", "158706", "158708"}
	assert next(r for r in rows if r["removed_link_id"] == "158700")["same_surname_as_a_kept_name"] == "True"
	assert next(r for r in rows if r["removed_link_id"] == "158700")["shared_surname"] == "noel"
	assert next(r for r in rows if r["removed_link_id"] == "158708")["shared_surname"] == ""
	assert next(r for r in rows if r["removed_link_id"] == "158701")["removed_is_junk"] == "True"
	with pytest.raises(FileExistsError):
		rrjl.write_csv(path, [])


def test_apply_writes_change_log_first_then_deletes_and_undo_reinserts(tmp_path):
	removals = rrjl.plan(ROWS)["removals"]
	db = FakeDB(lambda sql, params: _Result(rowcount=1) if sql.startswith(("DELETE", "INSERT")) else None)
	log = tmp_path / "log.jsonl"
	assert rrjl.apply_removals(db, removals, log, {"old_max_id": 158682}) == 4
	assert [p["id"] for s, p in db.calls if s.startswith("DELETE")] == [158700, 158701, 158703, 158704]
	assert db.commits == 1
	header, *logged = list(rrjl.read_undo_file(log))
	assert header == {"_header": True, "old_max_id": 158682}
	assert [r["id"] for r in logged] == [158700, 158701, 158703, 158704]
	assert set(logged[0]) == {"id", "case_id", "judge_profile_id", "raw_name", "created_at"}
	db2 = FakeDB(lambda sql, params: _Result(rowcount=1) if sql.startswith("INSERT") else None)
	assert rrjl.restore(db2, log) == (4, 4)
	assert db2.calls[0][1]["id"] == 158700 and db2.calls[0][1]["created_at"].startswith("2026-10-20T08:12:45-04:00")
	db3 = FakeDB(lambda sql, params: _Result(scalar=True) if sql.startswith("SELECT (EXISTS") else None)
	assert rrjl.restore(db3, log, apply=False) == (4, 4)
	assert not any(s.startswith("INSERT") for s, _ in db3.calls) and db3.commits == 0


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
			return _Result(rows=[{"court": "FC", "decisions": 5, "over_ceiling": 5}, {"court": "FCA", "decisions": 1, "over_ceiling": 0}])
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
	assert "redundant_links_to_remove=4 (FC 3, FCA 1)" in out
	assert "new_name_differs_needs_a_human_look=3 (FC 1, FCA 2)" in out
	assert "skipped_junk_old_link_decisions=1" in out
	assert "case_judge_profiles rows: before=50 after=46" in out
	assert "K7 (ceiling 1) FC: database now=5 projected=2" in out
	assert not any(s.startswith(("DELETE", "INSERT")) for s, _ in db.calls)
	assert db.calls[0][0] == "SET TRANSACTION READ ONLY"
	assert "old links: id <= 158682; new links: id 158683 to 187266" in out


def test_main_apply_needs_expected_count_and_refuses_a_wrong_one(monkeypatch, tmp_path):
	db = _fake_session(monkeypatch)
	with pytest.raises(SystemExit):
		rrjl.main(["--apply"])
	assert rrjl.main(["--apply", "--expected-count", "99", "--undo-file", str(tmp_path / "x.jsonl")]) == 1
	assert not any(s.startswith("DELETE") for s, _ in db.calls)
	assert not (tmp_path / "x.jsonl").exists()


def test_main_apply_refuses_overridden_id_ranges(monkeypatch):
	_fake_session(monkeypatch)
	with pytest.raises(SystemExit):
		rrjl.main(["--apply", "--expected-count", "4", "--old-max-id", "1"])


def test_main_apply_writes_in_a_writable_transaction_and_reports_failure(monkeypatch, tmp_path, capsys):
	db = _fake_session(monkeypatch)
	assert rrjl.main(["--apply", "--expected-count", "4", "--undo-file", str(tmp_path / "log.jsonl")]) == 1  # fake deletes 0 rows
	out = capsys.readouterr().out
	assert "Nothing was deleted" in out
	assert not any("READ ONLY" in s for s, _ in db.calls)
	header = next(rrjl.read_undo_file(tmp_path / "log.jsonl"))
	assert header["_header"] and header["old_max_id"] == 158682 and header["run_max_id"] == 187266


def test_main_undo_without_apply_is_a_read_only_dry_run(monkeypatch, tmp_path, capsys):
	db = _fake_session(monkeypatch)
	log = tmp_path / "log.jsonl"
	rrjl.write_undo_file(log, [{"_header": True}, {"id": 1, "case_id": 2, "judge_profile_id": 3, "raw_name": "x", "created_at": "2026-10-20T08:12:45-04:00"}])
	assert rrjl.main(["--undo", str(log)]) == 0
	assert db.calls[0][0] == "SET TRANSACTION READ ONLY"
	assert "Dry run of the undo" in capsys.readouterr().out
	assert not any(s.startswith("INSERT") for s, _ in db.calls)
