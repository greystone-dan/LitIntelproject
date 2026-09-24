from types import SimpleNamespace

from scripts.dry_run_paragraph_evidence_bridge import build_report, map_case


def test_map_case_preserves_evidence_layers_and_missing_assessments(monkeypatch):
	chunks = [
		SimpleNamespace(id=10, paragraph_start=1, paragraph_end=1, chunk_index=0, text="one", text_hash="wrong"),
		SimpleNamespace(id=11, paragraph_start=2, paragraph_end=2, chunk_index=1, text="two", text_hash="3fc4ccfe745870e2c9b6c6d7e0c2f4a9f0d3d7f1a7e8d4f4b1d5d9d5f5e4c3b2"),
	]
	monkeypatch.setattr(
		"scripts.dry_run_paragraph_evidence_bridge.load_paragraph_assessments",
		lambda case_id, enforce_cohort=False: {
			"case_id": case_id,
			"available": True,
			"assessments": {"1": {"topic": "Topic", "role": "Factual", "confidence": 0.8, "explanation": "Text."}},
		},
	)

	class ScalarResult:
		def __init__(self, values):
			self.values = values
		def all(self):
			return self.values

	class Session:
		def scalars(self, query):
			query_text = str(query)
			if "case_chunks" in query_text:
				return ScalarResult(chunks)
			if "citations" in query_text:
				return ScalarResult([SimpleNamespace(id=20, chunk_id=10, offset_start=1, offset_end=4, citation_kind="case", normalized_citation="2020 FC 1", target_case_id=99)])
			return ScalarResult([SimpleNamespace(id=30, chunk_id=10, offset_start=5, offset_end=9, instrument_key="irpa", normalized_reference="IRPA 34(1)(f)", provision_section="34", provision_subsection="1", provision_paragraph="f")])

	records = map_case(Session(), 62)

	assert records[0]["status"] == "exact"
	assert records[0]["citations"][0]["id"] == 20
	assert records[0]["statute_references"][0]["id"] == 30
	assert records[1]["status"] == "missing_assessment"


def test_build_report_counts_statuses(monkeypatch):
	monkeypatch.setattr(
		"scripts.dry_run_paragraph_evidence_bridge.load_paragraph_assessments",
		lambda case_id, enforce_cohort=False: {
			"case_id": case_id,
			"available": False,
			"assessments": {},
		},
	)

	class Session:
		def scalars(self, query):
			return type("Result", (), {"all": lambda self: []})()

	result = build_report(Session(), [62])

	assert result["mode"] == "read_only"
	assert result["case_count"] == 1
	assert result["record_count"] == 0