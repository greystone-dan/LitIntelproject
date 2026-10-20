"""The scripts/fix_*.py database repair scripts: selection rules, undo files and apply/undo round trips (fake DB)."""

from types import SimpleNamespace

import pytest

from scripts import (
	fix_common,
	fix_french_metadata,
	fix_junk_judges,
	fix_non_immigration_report,
	fix_own_caption_links,
	fix_self_citations,
)


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


def test_undo_file_round_trip_and_never_overwrites(tmp_path):
	path = tmp_path / "sub" / "x.jsonl"
	assert fix_common.write_undo_file(path, [{"id": 1, "a": "é"}, {"id": 2, "a": None}]) == 2
	assert list(fix_common.read_undo_file(path)) == [{"id": 1, "a": "é"}, {"id": 2, "a": None}]
	with pytest.raises(FileExistsError):
		fix_common.write_undo_file(path, [])
	assert [list(c) for c in fix_common.chunked([1, 2, 3], 2)] == [[1, 2], [3]]


def test_self_citations_save_then_delete_in_batches(tmp_path):
	table = [{"id": i, "source_case_id": 5, "target_case_id": 5, "citation_text": f"t{i}"} for i in (1, 2, 3)]

	def handler(sql, params):
		if sql.startswith("SELECT * FROM citations"):
			return _Result([r for r in table if r["id"] > params["after"]][: params["limit"]])
		if sql.startswith("DELETE FROM citations"):
			assert "citations.source_case_id = citations.target_case_id" in sql
			return _Result(rowcount=2)

	db = FakeDB(handler)
	undo_path = tmp_path / "u.jsonl"
	ids = fix_self_citations.save_rows(db, undo_path, 2)
	assert ids == [1, 2, 3]
	assert [r["id"] for r in fix_common.read_undo_file(undo_path)] == [1, 2, 3]
	# nothing is deleted before the file is complete
	assert not any(sql.startswith("DELETE") for sql, _ in db.calls)
	assert fix_self_citations.delete_rows(db, ids, 2) == 4  # two batches, fake rowcount 2 each
	assert db.commits == 2


def test_self_citations_restore_uses_insert_do_nothing(tmp_path):
	path = tmp_path / "u.jsonl"
	fix_common.write_undo_file(path, [{"id": 1, "source_case_id": 5, "target_case_id": 5}])
	db = FakeDB(lambda sql, params: _Result(rowcount=1))
	assert fix_self_citations.restore_rows(db, path, 100) == 1
	assert "ON CONFLICT (id) DO NOTHING" in db.calls[0][0]


def test_self_citations_main_dry_run_writes_nothing(monkeypatch, capsys):
	def handler(sql, params):
		if "GROUP BY 1" in sql:
			return _Result([{"court": "FC", "n": 2}])
		if "LIMIT :limit" in sql or "LIMIT" in sql:
			return _Result([{"id": 9, "source_case_id": 5, "court": "FC", "source_citation": "2020 FC 1",
				"citation_kind": "case_name", "citation_text": "Singh v. Canada"}])
		return _Result(scalar=2)

	db = FakeDB(handler)
	monkeypatch.setattr(fix_self_citations, "SessionLocal", lambda: _Ctx(db))
	assert fix_self_citations.main([]) == 0
	out = capsys.readouterr().out
	assert "self_citations=2" in out and "FC" in out and "Dry run" in out
	assert not any(sql.startswith(("DELETE", "INSERT")) for sql, _ in db.calls)


def test_self_citations_apply_refuses_wrong_expected_count(monkeypatch):
	db = FakeDB(lambda sql, params: _Result(scalar=2))
	monkeypatch.setattr(fix_self_citations, "SessionLocal", lambda: _Ctx(db))
	assert fix_self_citations.main(["--apply", "--expected-count", "3"]) == 1
	assert not any(sql.startswith("DELETE") for sql, _ in db.calls)


def _caption_row(**overrides):
	row = {
		"id": 7389492, "source_case_id": 35899, "target_case_id": 36940, "citation_kind": "case_name",
		"citation_text": "Baker v. Canada", "normalized_citation": "Baker v Canada", "offset_start": 10,
		"offset_end": 25, "unresolved": False, "target_paragraph": None, "target_chunk_id": None,
		"source_title": "Baker v. Canada (Minister of Citizenship and Immigration)",
		"header": "Date: 1999\nIndexed as: Baker v. Canada (Minister of Citizenship and Immigration)\nHeld: appeal allowed",
	}
	return {**row, **overrides}


def test_own_caption_candidate_requires_indexed_as_by_default():
	assert fix_own_caption_links.is_candidate(_caption_row())
	assert not fix_own_caption_links.is_candidate(_caption_row(header="Baker v. Canada was argued in 1998."))
	assert fix_own_caption_links.is_candidate(_caption_row(header="no header"), any_own_caption=True)


def test_own_caption_candidate_rejects_other_cases_and_self_links():
	assert not fix_own_caption_links.is_candidate(_caption_row(citation_text="Singh v. Canada"))
	assert not fix_own_caption_links.is_candidate(_caption_row(source_title="Baker v. Canada Border Services Agency"))
	assert not fix_own_caption_links.is_candidate(_caption_row(target_case_id=35899))
	assert not fix_own_caption_links.is_candidate(_caption_row(target_case_id=None))
	assert not fix_own_caption_links.is_candidate(_caption_row(citation_text="Baker"), any_own_caption=True)  # surname only


def test_own_caption_where_clause_is_narrow():
	sql = " ".join(str(fix_own_caption_links.SELECT_SQL).split())
	assert "c.citation_kind IN ('case_name', 'case_short')" in sql
	assert "c.target_case_id IS NOT NULL AND c.target_case_id <> c.source_case_id" in sql
	assert "WHERE id = :id AND target_case_id = :target_case_id" in str(fix_own_caption_links.UNLINK_SQL)


def test_own_caption_unlink_saves_undo_first_and_restores(tmp_path):
	row = _caption_row(target_paragraph=12, target_chunk_id=99)
	db = FakeDB(lambda sql, params: _Result(rowcount=len(params)))
	undo_path = tmp_path / "u.jsonl"
	assert fix_own_caption_links.apply_unlink(db, [row], undo_path, 10) == 1
	assert list(fix_common.read_undo_file(undo_path)) == [{
		"id": 7389492, "source_case_id": 35899, "target_case_id": 36940, "unresolved": False,
		"target_paragraph": 12, "target_chunk_id": 99,
	}]
	assert db.calls[0][1] == [{"id": 7389492, "target_case_id": 36940}]
	db2 = FakeDB(lambda sql, params: _Result(rowcount=len(params)))
	assert fix_own_caption_links.undo(db2, undo_path, 10) == 1
	assert db2.calls[0][1][0] == {"id": 7389492, "target_case_id": 36940, "unresolved": False,
		"target_paragraph": 12, "target_chunk_id": 99}


def test_resolver_skips_own_caption_names():
	from scripts.resolve_citation_targets import _names_own_caption

	citation = SimpleNamespace(source_case_id=1, citation_kind="case_name", citation_text="Baker v. Canada",
		normalized_citation="Baker v Canada", offset_start=0, offset_end=15)
	assert _names_own_caption(citation, {1: "Baker v. Canada (Minister of Citizenship and Immigration)"})
	assert not _names_own_caption(citation, {1: "Singh v. Canada"})


def test_junk_judge_detection_matches_extractor():
	assert fix_junk_judges.is_junk_judge("FEDERAL COURT")
	assert fix_junk_judges.is_junk_judge("\nFEDERAL COURT OF APPEAL\n")
	assert fix_junk_judges.is_junk_judge("Solicitors of record")
	assert not fix_junk_judges.is_junk_judge("Gleeson J.")
	assert not fix_junk_judges.is_junk_judge("Gleeson; Roy; Fothergill")
	assert not fix_junk_judges.is_junk_judge(None)


def test_junk_judge_set_judge_only_touches_judge_key():
	meta = {"a": 1, "reader_extracted": {"judge": "FEDERAL COURT", "docket": "IMM-1-20"}}
	fixed = fix_junk_judges._set_judge(meta, "Gleeson J.")
	assert fixed["reader_extracted"] == {"judge": "Gleeson J.", "docket": "IMM-1-20"} and fixed["a"] == 1
	assert fix_junk_judges._set_judge(meta, None)["reader_extracted"] == {"docket": "IMM-1-20"}
	assert meta["reader_extracted"]["judge"] == "FEDERAL COURT"  # input not mutated


class _StoreDB(FakeDB):
	"""Holds metadata_json per case id; reads via scalar(), writes via execute(update)."""

	def __init__(self, store):
		super().__init__()
		self.store = store

	def scalar(self, statement):
		return self.store[next(iter(statement.compile().params.values()))]

	def execute(self, statement, params=None):
		compiled = statement.compile().params
		self.store[compiled["id_1"]] = compiled["metadata_json"]
		return _Result(rowcount=1)


def test_junk_judge_apply_and_undo_round_trip(tmp_path):
	store = {1: {"reader_extracted": {"judge": "ANNEX A", "docket": "x"}}, 2: {"reader_extracted": {"judge": "Roy J."}}}
	plan = [{"id": 1, "judge": "ANNEX A", "new_judge": None, "court": "FC", "citation": "c"}]
	db = _StoreDB(store)
	undo_path = tmp_path / "u.jsonl"
	assert fix_junk_judges.apply_plan(db, plan, undo_path, 10) == 1
	assert store[1] == {"reader_extracted": {"docket": "x"}} and store[2]["reader_extracted"]["judge"] == "Roy J."
	assert list(fix_common.read_undo_file(undo_path)) == [{"id": 1, "old_judge": "ANNEX A", "new_judge": None}]
	assert fix_junk_judges.undo(db, undo_path, 10) == (1, 0)
	assert store[1] == {"reader_extracted": {"judge": "ANNEX A", "docket": "x"}}


def test_junk_judge_apply_skips_rows_edited_since_scan(tmp_path):
	db = _StoreDB({1: {"reader_extracted": {"judge": "Roy J."}}})
	plan = [{"id": 1, "judge": "ANNEX A", "new_judge": None, "court": "FC", "citation": "c"}]
	assert fix_junk_judges.apply_plan(db, plan, tmp_path / "u.jsonl", 10) == 0
	assert db.store[1] == {"reader_extracted": {"judge": "Roy J."}}


def test_non_immigration_rates_and_impact():
	assert fix_non_immigration_report.win_rate(3, 1) == 75.0
	assert fix_non_immigration_report.win_rate(0, 0) is None
	impact = fix_non_immigration_report.judge_impact({
		"slug": "judge-stratas", "name": "Stratas", "court": "FCA", "total": 40, "non_immigration": 10,
		"won_all": 26, "lost_all": 9, "won_imm": 12, "lost_imm": 9,
	})
	assert impact["rate_all"] == 74.3 and impact["rate_immigration_only"] == 57.1 and impact["delta"] == 17.2


def test_non_immigration_report_is_read_only_sql():
	for statement in (fix_non_immigration_report.COVERAGE_SQL, fix_non_immigration_report.JUDGE_SQL,
			fix_non_immigration_report.CANDIDATES_SQL):
		assert str(statement).lstrip().upper().startswith("SELECT")


FRENCH_TEXT = """Date : 20260924
Dossier : A-127-25
Référence : 2026 CAF 160
CORAM : LE JUGE LOCKE
LA JUGE GOYETTE
ENTRE :
MAXIME FORTIN
appelant
et
SA MAJESTÉ LE ROI
intimé
MOTIFS DU JUGEMENT DE LA COUR
[13] Dans ces circonstances, l’appel sera rejeté sans dépens.
« Nathalie Goyette »
j.c.a.
"""


def test_french_metadata_plan_changes_judge_docket_and_missing_outcome_only():
	row = {"id": 5, "court": "FCA", "citation": "2026 CAF 160",
		"extracted": {"judge": "LOCKE", "docket": "A-127-25 Contenu de la décision"}}
	judge_only = fix_french_metadata.plan_row(row, FRENCH_TEXT)
	assert set(judge_only) == {"judge", "docket"}
	changes = fix_french_metadata.plan_row(row, FRENCH_TEXT, include_outcomes=True)
	assert changes["judge"] == ("LOCKE", "Nathalie Goyette")
	assert changes["docket"] == ("A-127-25 Contenu de la décision", "A-127-25")
	assert changes["decision outcome"] == (None, "dismissed") and changes["government outcome"][1] == "won"
	kept = fix_french_metadata.plan_row({**row, "extracted": {**row["extracted"], "decision outcome": "allowed"}}, FRENCH_TEXT, include_outcomes=True)
	assert "decision outcome" not in kept and "government outcome" not in kept
	assert fix_french_metadata.plan_row(row, None) is None


def test_french_metadata_apply_needs_expected_count_and_round_trips(tmp_path):
	store = {1: {"reader_extracted": {"judge": "LOCKE", "x": 1}}}
	plan = [{"id": 1, "court": "FCA", "citation": "c", "changes": {"judge": ("LOCKE", "Nathalie Goyette")}}]
	db = _StoreDB(store)
	undo_path = tmp_path / "u.jsonl"
	assert fix_french_metadata.apply_plan(db, plan, undo_path, 10) == 1
	assert store[1]["reader_extracted"] == {"judge": "Nathalie Goyette", "x": 1}
	assert fix_french_metadata.undo(db, undo_path, 10) == (1, 0)
	assert store[1]["reader_extracted"] == {"judge": "LOCKE", "x": 1}
	with pytest.raises(SystemExit):
		fix_french_metadata.main(["--apply"])

def test_junk_judge_profiles_are_found_only_when_every_raw_name_is_junk(tmp_path):
	from scripts import fix_junk_judge_profiles as fjp

	def profile(pid, name):
		return dict(id=pid, slug=f"judge-{pid}", display_name=name, normalized_name=name.lower(), primary_court="FC", aliases=[name])

	rows = [
		{**profile(1, "Justice And Order"), "raw_name": "AND ORDER", "n": 5},
		{**profile(2, "Justice Heneghan"), "raw_name": "Heneghan J.", "n": 40},
		{**profile(2, "Justice Heneghan"), "raw_name": "SOLICITORS OF RECORD", "n": 3},
		{**profile(3, "Justice Orphan"), "raw_name": None, "n": 0},
	]
	db = FakeDB(lambda sql, params: _Result(rows=rows) if "FROM judge_profiles p" in sql else None)
	found = fjp.find_junk_profiles(db)
	assert [p["id"] for p in found] == [1] and found[0]["cases"] == 5

	db = FakeDB()
	path = tmp_path / "undo.jsonl"
	assert fjp.apply_deletes(db, found, path, 10) == 1
	assert len(list(fix_common.read_undo_file(path))) == 1
	assert any("DELETE FROM judge_profiles" in sql for sql, _ in db.calls) and db.commits == 1


def test_junk_judge_profiles_dry_run_report_apply_needs_expected_count_and_undo_restores_in_order(tmp_path, monkeypatch, capsys):
	from scripts import fix_junk_judge_profiles as fjp

	def profile(pid, name, court="FC"):
		return dict(id=pid, slug=f"judge-{pid}", display_name=name, normalized_name=name.lower(), primary_court=court, aliases=[name])

	rows = [
		{**profile(1, "Justice And Order"), "raw_name": "AND ORDER", "n": 5},
		{**profile(2, "Justice Heneghan"), "raw_name": "Heneghan J.", "n": 40},
		{**profile(2, "Justice Heneghan"), "raw_name": "SOLICITORS OF RECORD", "n": 3},
	]

	def handler(sql, params):
		if "FROM judge_profiles p JOIN case_judge_profiles l" in sql:
			return _Result()  # no review-only profiles
		if "FROM judge_profiles p" in sql:
			return _Result(rows=rows)
		if "FROM case_judge_profiles WHERE" in sql:
			return _Result(rows=[dict(id=11, case_id=7, raw_name="AND ORDER")])
		if "FROM judge_profile_aliases" in sql:
			return _Result(rows=[dict(id=21, alias_profile_id=1, canonical_profile_id=2, source="rule")])

	db = FakeDB(handler)
	monkeypatch.setattr(fjp, "SessionLocal", lambda: _Ctx(db))
	assert fjp.main([]) == 0
	out = capsys.readouterr().out
	assert "junk_judge_profiles=1 linked_cases=5" in out and "mixed" in out and "1 profiles" in out
	assert not any("DELETE" in sql for sql, _ in db.calls)
	with pytest.raises(SystemExit):
		fjp.main(["--apply"])
	assert fjp.main(["--apply", "--expected-count", "9"]) == 1
	undo = tmp_path / "u.jsonl"
	assert fjp.main(["--apply", "--expected-count", "1", "--undo-file", str(undo)]) == 0
	assert any("DELETE FROM judge_profiles" in sql for sql, _ in db.calls)

	db.calls.clear()
	assert fjp.restore(db, undo) == 1
	kinds = [("judge_profiles" if "INTO judge_profiles " in sql else "links" if "INTO case_judge_profiles" in sql else "aliases")
		for sql, _ in db.calls if sql.startswith("INSERT")]
	assert kinds == ["judge_profiles", "links", "aliases"]





def test_junk_judge_profiles_raw_names_query_does_not_group_by_the_json_aliases_column():
	from scripts import fix_junk_judge_profiles as fjp

	sql = " ".join(str(fjp.RAW_NAMES_SQL).split())
	assert "aliases" not in sql.split("GROUP BY", 1)[1]  # json has no equality operator in Postgres, so it cannot be grouped on
	assert "p.aliases" in sql.split("FROM", 1)[0]  # but it is still selected (it depends on the primary key p.id)


def test_junk_judge_profiles_csv_lists_junk_and_review_only_profiles(tmp_path, monkeypatch, capsys):
	import csv

	from scripts import fix_junk_judge_profiles as fjp

	def profile(pid, name, court="FC"):
		return dict(id=pid, slug=f"judge-{pid}", display_name=name, normalized_name=name.lower(), primary_court=court, aliases=[name])

	rows = [
		{**profile(1, "I HEREBY CERTIFY that the above document"), "raw_name": "I HEREBY CERTIFY that the above document", "n": 11},
		{**profile(2, "Justice Heneghan"), "raw_name": "Heneghan J.", "n": 40},
		{**profile(3, "THE COURT"), "raw_name": "THE COURT", "n": 48},
	]

	def handler(sql, params):
		if "FROM judge_profiles p JOIN case_judge_profiles l" in sql:
			assert params["names"] == ["THE COURT"]
			return _Result(rows=[dict(id=3, slug="judge-3", display_name="THE COURT", primary_court="FC", links=48, only_attribution=5)])
		if "FROM judge_profiles p" in sql:
			return _Result(rows=rows)

	db = FakeDB(handler)
	monkeypatch.setattr(fjp, "SessionLocal", lambda: _Ctx(db))
	path = tmp_path / "names.csv"
	assert fjp.main(["--csv", str(path)]) == 0
	out = capsys.readouterr().out
	assert "junk_judge_profiles=1 linked_cases=11" in out and "5 decisions have no other judge link" in out
	assert db.calls[0][0] == "SET TRANSACTION READ ONLY"
	got = list(csv.DictReader(open(path, encoding="utf-8")))
	assert [(r["status"], r["display_name"]) for r in got] == [("junk", "I HEREBY CERTIFY that the above document"), ("review_only", "THE COURT")]
	assert got[1]["only_attribution_cases"] == "5" and got[0]["linked_cases"] == "11"
	with pytest.raises(FileExistsError):
		fjp.write_names_csv(path, [], [])


def _unlink_candidate(cid, target):
	# id, source, court, kind, target, unresolved, text, source_date, target_date, cite, secondary, title
	return (cid, 5, "FC", "case_name", target, False, "Patel v. Canada", "2003-10-31", "2020-01-27", None, None, "Patel")


def test_unlink_apply_logs_then_updates_and_undo_restores(tmp_path):
	from scripts import unlink_impossible_citation_targets as unlink

	state = {1: 10, 2: 11}  # citation id -> target

	def handler(sql, params):
		if sql.startswith("UPDATE citations SET target_case_id = NULL"):
			hit = state.get(params["id"]) == params["t"]
			if hit:
				state[params["id"]] = None
			return _Result(rowcount=int(hit))
		if sql.startswith("UPDATE citations SET target_case_id = :t"):
			hit = state.get(params["id"]) is None
			if hit:
				state[params["id"]] = params["t"]
			return _Result(rowcount=int(hit))

	db = FakeDB(handler)
	log = tmp_path / "log.csv"
	candidates = [_unlink_candidate(1, 10), _unlink_candidate(2, 11)]
	state[2] = 99  # row 2 was changed after the scan
	assert unlink.apply_unlink(db, candidates, log, 1) == 1
	assert state == {1: None, 2: 99}
	rows = unlink.read_undo_rows(log)
	assert [r["citation_id"] for r in rows] == ["1", "2"]  # logged before the update, whatever the outcome
	assert rows[0]["previous_target_case_id"] == "10" and rows[0]["previous_unresolved"] == "False"
	assert unlink.undo_unlink(db, rows) == (1, 1)  # row 1 restored, row 2 (changed in between) skipped
	assert state == {1: 10, 2: 99}
	restore_sql = [sql for sql, p in db.calls if sql.startswith("UPDATE citations SET target_case_id = :t")]
	assert all("unresolved = :u" in sql for sql in restore_sql)


def test_unlink_apply_refuses_wrong_expected_count(monkeypatch, tmp_path):
	from scripts import unlink_impossible_citation_targets as unlink
	import backend.database as database

	def handler(sql, params):
		if sql.startswith("SELECT ci.id"):
			return _Result([_unlink_candidate(1, 10)])

	db = FakeDB(handler)
	monkeypatch.setattr(database, "SessionLocal", lambda: _Ctx(db))
	assert unlink.main(["--apply", "--expected-count", "5", "--change-log", str(tmp_path / "l.csv")]) == 1
	assert not any(sql.startswith("UPDATE") for sql, _ in db.calls)
	with pytest.raises(SystemExit):
		unlink.main(["--apply", "--change-log", str(tmp_path / "l.csv")])
