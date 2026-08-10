import json
from types import SimpleNamespace

from scripts.verify_citation_extraction import (
	build_openai_audit_messages,
	build_sample_report,
	evaluate_fixtures,
	load_fixtures,
	_dict_to_raw_match,
	run_openai_audit,
	validate_actual_spans,
)
from backend.citations import RawCitationMatch


def test_evaluate_fixtures_reports_exact_matches():
	fixtures = [
		{
			"id": "exact",
			"text": "See 2024 FC 100 and IRPA s. 72(1).",
			"expected": [
				{
					"kind": "neutral",
					"citation_text": "2024 FC 100",
					"normalized_citation": "2024 FC 100",
					"offset_start": 4,
					"offset_end": 15,
				},
				{
					"kind": "statute",
					"citation_text": "IRPA s. 72(1)",
					"normalized_citation": "Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 72(1)",
					"offset_start": 20,
					"offset_end": 33,
				},
			],
		},
	]
	report = evaluate_fixtures(fixtures)

	assert report["summary"]["matched"] == 2
	assert report["summary"]["missing"] == 0
	assert report["summary"]["unexpected"] == 0
	assert report["summary"]["span_errors"] == 0
	assert report["summary"]["precision"] == 1.0
	assert report["summary"]["recall"] == 1.0


def test_evaluate_fixtures_reports_missing_and_unexpected_matches():
	fixtures = [
		{
			"id": "mismatch",
			"text": "See 2024 FC 100 and IRPA s. 72(1).",
			"expected": [
				{
					"kind": "neutral",
					"citation_text": "2024 FC 100",
					"normalized_citation": "2024 FC 100",
					"offset_start": 4,
					"offset_end": 15,
				},
			],
		}
	]

	report = evaluate_fixtures(fixtures)

	assert report["summary"]["matched"] == 1
	assert report["summary"]["missing"] == 0
	assert report["summary"]["unexpected"] == 1
	assert report["results"][0]["unexpected"][0]["kind"] == "statute"


def test_validate_actual_spans_flags_incorrect_offsets():
	text = "See 2024 FC 100."
	matches = [
		RawCitationMatch(
			kind="neutral",
			citation_text="2024 FC 100",
			normalized_citation="2024 FC 100",
			offset_start=5,
			offset_end=16,
		)
	]

	errors = validate_actual_spans(text, matches)

	assert len(errors) == 1
	assert errors[0]["span_text"] == "024 FC 100."


def test_load_fixtures_supports_jsonl(tmp_path):
	fixture_path = tmp_path / "fixtures.jsonl"
	fixture_path.write_text(
		"\n".join(
			[
				json.dumps({"id": "one", "text": "See 2024 FC 100.", "expected": []}),
				json.dumps({"id": "two", "text": "See IRPA s. 72(1).", "expected": []}),
			]
		)
		+ "\n",
		encoding="utf-8",
	)

	fixtures = load_fixtures(fixture_path)

	assert [fixture["id"] for fixture in fixtures] == ["one", "two"]


def test_build_sample_report_includes_summary_and_context():
	report = build_sample_report(
		[
			{
				"id": "case:11",
				"case_id": 11,
				"title": "Example Case",
				"text": "See 2024 FC 100 and IRPA s. 72(1).",
			}
		],
		source="cases",
		rows_scanned=3,
	)

	assert report["summary"]["mode"] == "sample_canonical"
	assert report["summary"]["source"] == "cases"
	assert report["summary"]["rows_scanned"] == 3
	assert report["summary"]["sampled"] == 1
	assert report["summary"]["citations"] == 2
	assert report["results"][0]["case_id"] == 11
	assert "2024 FC 100" in report["results"][0]["actual"][0]["context_snippet"]


def test_build_sample_report_uses_provided_actual_rows():
	report = build_sample_report(
		[
			{
				"id": "stored:1",
				"case_id": 11,
				"text": "Full case text that does not share chunk-relative offsets.",
				"actual": [
					{
						"kind": "neutral",
						"citation_text": "2024 FC 100",
						"normalized_citation": "2024 FC 100",
						"offset_start": 4,
						"offset_end": 15,
						"citation_id": 99,
					}
				],
			}
		],
		source="stored_chunks",
		rows_scanned=1,
	)

	assert report["summary"]["citations"] == 1
	assert report["summary"]["span_errors"] == 0
	assert report["results"][0]["actual"][0]["citation_id"] == 99


def test_dict_to_raw_match_preserves_offsets():
	match = _dict_to_raw_match(
		{
			"kind": "statute",
			"citation_text": "IRPA s. 72(1)",
			"normalized_citation": "Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 72(1)",
			"offset_start": 10,
			"offset_end": 23,
		}
	)

	assert match.kind == "statute"
	assert match.offset_start == 10
	assert match.offset_end == 23


def test_build_openai_audit_messages_truncates_long_text():
	messages = build_openai_audit_messages(
		{
			"id": "case:1",
			"text": "A" * 800,
			"actual": [],
		},
		max_chars=300,
	)

	assert len(messages) == 2
	assert "truncated for audit" in messages[1]["content"]


class _FakeChatCompletions:
	def __init__(self, responses):
		self.responses = list(responses)

	def create(self, **kwargs):
		return self.responses.pop(0)


class _FakeClient:
	def __init__(self, responses):
		self.chat = SimpleNamespace(completions=_FakeChatCompletions(responses))


def test_run_openai_audit_respects_budget_and_parses_json():
	report = build_sample_report(
		[
			{"id": "case:1", "case_id": 1, "text": "See 2024 FC 100 and IRPA s. 72(1)."},
			{"id": "case:2", "case_id": 2, "text": "Brown v. Canada, 2019 FC 12 was followed."},
		],
		source="cases",
		rows_scanned=2,
	)
	responses = [
		SimpleNamespace(
			choices=[
				SimpleNamespace(
					message=SimpleNamespace(
						content=json.dumps(
							{
								"missing_citations": [{"citation_text": "IRPA s. 72(1)", "kind": "statute", "reason": "Subsection reference present."}],
								"mischaracterized_citations": [],
								"notes": "Looks plausible.",
								"confidence": "medium",
							}
						)
					)
				)
			],
			usage=SimpleNamespace(prompt_tokens=120, completion_tokens=40),
		)
	]

	audit = run_openai_audit(
		report,
		client=_FakeClient(responses),
		model="gpt-4.1-nano",
		budget_usd=0.00008,
		input_cost_per_1m=0.10,
		output_cost_per_1m=0.40,
		max_output_tokens=80,
		max_chars=500,
	)

	assert audit["summary"]["processed"] == 1
	assert audit["summary"]["flagged_missing"] == 1
	assert audit["results"][0]["audit"]["confidence"] == "medium"


def test_run_openai_audit_records_malformed_response_and_continues():
	report = build_sample_report(
		[
			{"id": "case:1", "case_id": 1, "text": "See 2024 FC 100."},
			{"id": "case:2", "case_id": 2, "text": "See 2025 FC 101."},
		],
		source="cases",
		rows_scanned=2,
	)
	responses = [
		SimpleNamespace(
			choices=[SimpleNamespace(message=SimpleNamespace(content="{bad json"))],
			usage=SimpleNamespace(prompt_tokens=100, completion_tokens=20),
		),
		SimpleNamespace(
			choices=[
				SimpleNamespace(
					message=SimpleNamespace(
						content=json.dumps(
							{
								"missing_citations": [],
								"mischaracterized_citations": [],
								"notes": "ok",
								"confidence": "low",
							}
						)
					)
				)
			],
			usage=SimpleNamespace(prompt_tokens=100, completion_tokens=20),
		),
	]

	audit = run_openai_audit(
		report,
		client=_FakeClient(responses),
		model="gpt-4.1-nano",
		budget_usd=0.01,
		input_cost_per_1m=0.10,
		output_cost_per_1m=0.40,
		max_output_tokens=80,
		max_chars=500,
	)

	assert audit["summary"]["processed"] == 1
	assert audit["summary"]["failed"] == 1
	assert "error" in audit["results"][0]
	assert audit["results"][1]["audit"]["confidence"] == "low"