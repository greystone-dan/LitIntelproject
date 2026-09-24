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