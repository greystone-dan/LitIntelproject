"""Unit search: placing the best matching paragraph inside its discussion unit (no database)."""
from types import SimpleNamespace

from backend import unit_keyword_search as unit_search
from backend.unit_keyword_search import _term_sets, build_unit_result, locate_unit, snippet_around


def _report():
	texts = [
		"Reasons for judgment",
		"[1] The applicant seeks judicial review of a refusal.",
		"[2] The officer's credibility finding ignored the evidence on the record.",
		"[3] A credibility finding must be justified, intelligible and transparent.",
		"[4] The application is dismissed.",
	]
	return {
		"paragraphs": [
			{"paragraph_index": i, "source_paragraph_index": i, "text": t} for i, t in enumerate(texts)
		],
		"discussion_units": [
			{"discussion_unit_id": "c:0", "start_paragraph": 0, "end_paragraph": 1, "paragraph_count": 2},
			{"discussion_unit_id": "c:1", "start_paragraph": 2, "end_paragraph": 3, "paragraph_count": 2},
			{"discussion_unit_id": "c:2", "start_paragraph": 4, "end_paragraph": 4, "paragraph_count": 1},
		],
	}


def test_best_piece_inside_a_big_chunk_picks_the_right_unit():
	report = _report()
	for p in report["paragraphs"]:  # an SCC-style chunk: every piece comes from one stored chunk
		p["source_paragraph_index"] = 7
	terms = _term_sets("credibility finding transparent")
	found = locate_unit(report, 7, terms)
	assert found["position"] == 1 and found["piece"]["paragraph_index"] == 3


def test_build_unit_result_reports_printed_numbers_and_snippet():
	result = build_unit_result(_report(), 2, _term_sets("credibility finding evidence"))
	assert (result["unit_index"], result["start_number"], result["end_number"], result["paragraph_number"]) == (1, 2, 3, 2)
	assert "credibility" in result["snippet"] and result["match_score"] >= 2


def test_unknown_chunk_gives_none():
	assert build_unit_result(_report(), 99, _term_sets("credibility finding")) is None


def test_snippet_is_trimmed_around_the_match():
	text = "word " * 200 + "credibility finding " + "word " * 200
	out = snippet_around(text, _term_sets("credibility finding evidence"))
	assert "credibility" in out and len(out) < 500


def test_flag_is_off_by_default(monkeypatch):
	monkeypatch.delenv("ILIT_UNIT_SEARCH", raising=False)
	assert not unit_search.unit_search_enabled()
	monkeypatch.setenv("ILIT_UNIT_SEARCH", "1")
	assert unit_search.unit_search_enabled()


def test_endpoint_404_when_flag_off(monkeypatch):
	from fastapi.testclient import TestClient

	from backend.database import get_db
	from backend.main import app

	app.dependency_overrides[get_db] = lambda: None

	monkeypatch.delenv("ILIT_UNIT_SEARCH", raising=False)
	try:
		client = TestClient(app)  # no context manager: skips the startup that needs a database
		assert client.get("/unit-search", params={"q": "credibility finding evidence"}).status_code == 404
	finally:
		app.dependency_overrides.pop(get_db, None)


def test_phrase_and_whole_word_scoring():
	query = "internal flight alternative reasonable"
	terms = _term_sets(query)
	pairs = unit_search._query_pairs(query, terms)
	phrase = unit_search._piece_score("The internal flight alternative was reasonable.", terms, pairs)
	scattered = unit_search._piece_score("Internal affairs; the flight was an alternative that seemed reasonable.", terms, pairs)
	off_topic = unit_search._piece_score("International carriers and flight delays were not reasoned.", terms, pairs)
	assert phrase > scattered > off_topic


def test_ranking_puts_numbered_paragraphs_first_and_keeps_case_order_on_ties():
	rows = [
		{"paragraph_number": None, "match_score": 6, "case_score": 1.0, "id": "headnote"},
		{"paragraph_number": 5, "match_score": 4, "case_score": 0.5, "id": "low"},
		{"paragraph_number": 7, "match_score": 4, "case_score": 0.9, "id": "tie-high"},
		{"paragraph_number": 9, "match_score": 6, "case_score": 0.1, "id": "best"},
	]
	assert [r["id"] for r in unit_search.rank_results(rows)] == ["best", "tie-high", "low", "headnote"]


def test_search_units_filters_by_court_and_limit(monkeypatch):
	cases = {1: SimpleNamespace(id=1, court="SCC", title="a", citation="x", date=None, metadata_json={}),
		2: SimpleNamespace(id=2, court="FC", title="b", citation="y", date=None, metadata_json={"reader_extracted": {"judge": "J", "decision outcome": "allowed"}})}

	class DB:
		def get(self, model, key):
			return cases.get(key) if model is unit_search.Case else SimpleNamespace(chunk_index=2)

		def scalars(self, _):
			return []

	monkeypatch.setattr(unit_search, "search_paragraph_cases", lambda db, q: [
		{"case_id": 1, "best_chunk_id": 1, "score": 1.0}, {"case_id": 2, "best_chunk_id": 2, "score": 0.5}])
	monkeypatch.setattr(unit_search, "_cached_inspect_case", lambda db, cid, chunks: _report())
	out = unit_search.search_units(DB(), "credibility finding evidence", court="fc, fca")
	assert [r["case_id"] for r in out["results"]] == [2]
	assert out["results"][0]["judge"] == "J" and out["results"][0]["outcome"] == "allowed"
	assert unit_search.search_units(DB(), "credibility finding evidence", limit=1)["results"][0]["case_id"] in {1, 2}


def test_court_filter_accepts_codes_and_full_names():
	assert unit_search._court_filter("rad, FC") == {"RAD", "REFUGEE APPEAL DIVISION", "FC", "FEDERAL COURT"}
	assert unit_search._court_filter("") == set()
