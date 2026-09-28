import pytest
from fastapi import HTTPException

from backend import discussion_units_sandbox as sandbox


def test_manifest_has_exactly_300_unique_cases():
	cohort = sandbox.load_discussion_unit_cohort()

	assert len(cohort) == 300
	assert len(set(cohort)) == 300
	assert 62 in cohort


def test_non_cohort_case_is_rejected_before_reader_access():
	with pytest.raises(HTTPException) as error:
		sandbox.require_discussion_unit_case(1)

	assert error.value.status_code == 404


def test_search_scopes_query_to_manifest_ids(monkeypatch):
	captured = {}

	def fake_search(db, **kwargs):
		captured.update(kwargs)
		return {"results": [], "limit": kwargs["limit"], "offset": kwargs["offset"]}

	monkeypatch.setattr(sandbox, "fetch_analytics_search_cases", fake_search)
	result = sandbox.search_discussion_unit_cases(object(), query="Figurado")

	assert result["cohort_size"] == 300
	assert result["results"] == []
	assert captured["query"] == "Figurado"
	assert set(captured["cohort_ids"]) == set(sandbox.load_discussion_unit_cohort())


def test_page_reuses_full_reader_surface_with_sandbox_endpoints():
	html = sandbox.discussion_units_sandbox_page_html()

	assert "<title>Sandbox | iLIT</title>" in html
	assert "Advanced options" in html
	assert "readerViewToggle" in html
	assert "reader-info-tabs" in html
	assert "/discussion-units-sandbox/search?" in html
	assert "/discussion-units-sandbox/cases/${caseId}/reader-data" in html
	assert "/discussion-units-sandbox/cases/${caseId}" in html
	assert "sandboxAssessmentToggle" in html
	assert "/discussion-units-sandbox/cases/" in html
	assert "paragraph-assessments" in html
	assert "assessment" in html
	assert 'id="cohortSearchForm"' in html
	assert 'id="cohortQuery"' in html
	assert "limit:'100'" in html
	assert "cohort-assessments/compare" in html
	assert "assessment-citation" in html
	assert "Compare topic/role" in html


def test_paragraph_assessments_parse_report_table(tmp_path, monkeypatch):
	(monkeypatch.setattr(sandbox, "PARAGRAPH_ASSESSMENT_DIR", tmp_path))
	monkeypatch.setattr(sandbox, "load_discussion_unit_cohort", lambda: {62: {}})
	(tmp_path / "case_62_paragraph_assessment.md").write_text(
		"| Paragraph | Topic | Role | Confidence | Explanation |\n"
		"| ---: | --- | --- | ---: | --- |\n"
		"| 1 | Topic | Role | High | Useful explanation. |\n",
		encoding="utf-8",
	)

	result = sandbox.load_paragraph_assessments(62)

	assert result["available"] is True
	assert result["assessments"]["1"]["topic"] == "Topic"
	assert result["assessments"]["1"]["confidence"] == "High"


def test_paragraph_assessments_are_empty_when_report_is_missing(tmp_path, monkeypatch):
	monkeypatch.setattr(sandbox, "PARAGRAPH_ASSESSMENT_DIR", tmp_path)
	monkeypatch.setattr(sandbox, "load_discussion_unit_cohort", lambda: {62: {}})

	result = sandbox.load_paragraph_assessments(62)

	assert result["available"] is False
	assert result["assessments"] == {}


def test_cohort_assessment_search_ranks_topic_and_keeps_cohort_scope(monkeypatch):
	monkeypatch.setattr(sandbox, "load_discussion_unit_cohort", lambda: {62: {}, 126: {}})
	monkeypatch.setattr(sandbox, "load_cohort_assessment_records", lambda: (
		{"case_id": 62, "paragraph": "1", "assessment": {"topic": "Standard of review", "role": "Legal reasoning", "confidence": 0.9, "explanation": "Explains judicial review."}, "text": "The standard of review applies.", "citations": [{"id": 7, "chunk_id": 8, "normalized_citation": "2019 SCC 65"}]},
		{"case_id": 126, "paragraph": "2", "assessment": {"topic": "Costs", "role": "Disposition", "confidence": 0.8, "explanation": "Explains costs."}, "text": "The application is dismissed.", "citations": []},
	))

	result = sandbox.search_cohort_assessments("standard of review")

	assert [item["case_id"] for item in result["results"]] == [62]
	assert "topic" in result["results"][0]["match_reasons"]
	assert result["results"][0]["citations"][0]["id"] == 7
	assert result["results"][0]["citations"][0]["paragraph"] == "1"
	assert result["results"][0]["citations"][0]["assessment_key"]["topic"] == "Standard of review"
	assert result["results"][0]["citations"][0]["target_case_id"] is None


def test_cohort_assessment_comparison_preserves_paragraph_citation_identity(monkeypatch):
	monkeypatch.setattr(sandbox, "search_cohort_assessments", lambda query, limit: {"results": [
		{"case_id": 62, "paragraph": "1", "topic": "Standard of review", "role": "Legal reasoning", "score": 0.9, "explanation": "A", "text": "A", "citations": [{"id": 7, "case_id": 62, "paragraph": "1", "chunk_id": 8, "normalized_citation": "2019 SCC 65", "assessment_key": {"topic": "Standard of review", "role": "Legal reasoning"}}], "bridge_status": "exact"},
		{"case_id": 126, "paragraph": "4", "topic": "Standard of review", "role": "Legal reasoning", "score": 0.8, "explanation": "B", "text": "B", "citations": [], "bridge_status": "exact"},
	]})

	result = sandbox.compare_cohort_assessments("review")

	assert len(result["groups"]) == 1
	assert [(item["case_id"], item["paragraph"]) for item in result["groups"][0]["cases"]] == [(62, "1"), (126, "4")]
	assert result["groups"][0]["citations"][0]["case_id"] == 62


def test_cohort_assessment_comparison_scans_full_topic_role_cohort(monkeypatch):
	monkeypatch.setattr(sandbox, "search_cohort_assessments", lambda query, limit: {"results": []})
	monkeypatch.setattr(sandbox, "load_cohort_assessment_records", lambda: (
		{"case_id": 62, "paragraph": "1", "status": "exact", "assessment": {"topic": "Mootness", "role": "Legal reasoning", "explanation": "A"}, "text": "A", "citations": []},
		{"case_id": 126, "paragraph": "4", "status": "exact", "assessment": {"topic": "Mootness", "role": "Legal reasoning", "explanation": "B"}, "text": "B", "citations": []},
	))

	result = sandbox.compare_cohort_assessments("mootness", topic="Mootness", role="Legal reasoning")

	assert [(item["case_id"], item["paragraph"]) for item in result["groups"][0]["cases"]] == [(62, "1"), (126, "4")]