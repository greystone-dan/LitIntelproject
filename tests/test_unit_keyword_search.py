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
