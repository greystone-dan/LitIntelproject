import json
from pathlib import Path

import pytest

from scripts.package_discussion_units_llm import (
    _legal_paragraphs,
    _parse_paragraph_assessment,
    _parse_response,
    build_paragraph_assessment_request,
    build_request,
    render_markdown,
)
from scripts.run_model_paragraph_experiment import build_model_report, parse_segments


def _report():
    return {
        "case_id": 7,
        "paragraph_count": 3,
        "discussion_unit_count": 2,
        "paragraphs": [
            {"paragraph_index": 0, "text": "The application was filed.", "citation_ids": [], "statute_ids": [], "tag_ids": [], "is_heading": False},
            {"paragraph_index": 1, "text": "The parties made submissions.", "citation_ids": [1], "statute_ids": [], "tag_ids": [], "is_heading": False},
            {"paragraph_index": 2, "text": "The Court applies the test.", "citation_ids": [], "statute_ids": [2], "tag_ids": [], "is_heading": False},
        ],
        "discussion_units": [
            {"start_paragraph": 0, "end_paragraph": 1, "generation_method": "deterministic"},
            {"start_paragraph": 2, "end_paragraph": 2, "generation_method": "deterministic"},
        ],
    }


def test_request_contains_numbered_paragraphs_and_baseline():
    request = build_request(_report())
    payload = __import__("json").loads(request["messages"][1]["content"])
    assert [item["paragraph_index"] for item in payload["paragraphs"]] == [0, 1, 2]
    assert payload["deterministic_baseline"]["discussion_unit_count"] == 2
    assert "final unit ends at the last_allowed index" in request["messages"][0]["content"]


def test_text_only_request_excludes_deterministic_signals():
    request = build_request(_report(), text_only=True)
    payload = json.loads(request["messages"][1]["content"])
    assert "deterministic_baseline" not in payload
    assert payload["paragraphs"] == [
        {"paragraph_index": 0, "text": "The application was filed."},
        {"paragraph_index": 1, "text": "The parties made submissions."},
        {"paragraph_index": 2, "text": "The Court applies the test."},
    ]


def test_numbered_paragraph_expansion_omits_unnumbered_case_header():
    paragraphs = _legal_paragraphs([
        {"paragraph_index": 0, "text": "Case name\nDecision Content"},
        {"paragraph_index": 1, "text": "[1] The application was filed."},
    ])
    assert [item["paragraph_index"] for item in paragraphs] == [1]
    assert paragraphs[0]["text"].startswith("[1]")


def test_response_requires_contiguous_full_coverage():
    result = _parse_response(
        json.dumps({"units": [
            {"start_paragraph": 0, "end_paragraph": 1, "label": "History", "explanation": "", "transition_from_previous": "start", "confidence": 0.8},
            {"start_paragraph": 2, "end_paragraph": 2, "label": "Analysis", "explanation": "", "transition_from_previous": "new legal task", "confidence": 0.8},
        ]}),
        _report()["paragraphs"],
    )
    assert result["units"][0]["start_paragraph"] == 0


def test_response_accepts_discussion_units_alias():
    result = _parse_response(
        '{"discussion_units": [{"start_paragraph": 0, "end_paragraph": 2, "label": "Analysis"}]}',
        _report()["paragraphs"],
    )
    assert result["units"][0]["label"] == "Analysis"


def test_markdown_uses_plain_language_span_headings():
    result = {"units": [{"start_paragraph": 0, "end_paragraph": 1, "label": "Procedural history", "explanation": "This explains how the application reached the Court.", "transition_from_previous": "start", "confidence": 0.9}]}
    markdown = render_markdown(
        _report(),
        result,
        model="test-model",
        usage={"prompt_tokens": 100, "completion_tokens": 25, "total_tokens": 125, "estimated_cost_usd": 0.00002},
    )
    assert "Paragraphs 0-1: Procedural history" in markdown
    assert "This explains how the application reached the Court." in markdown
    assert "Prompt tokens: `100`" in markdown
    assert "Total tokens: `125`" in markdown
    assert "Estimated billing (USD): `$2e-05`" in markdown


def test_response_rejects_gaps():
    with pytest.raises(ValueError, match="contiguous"):
        _parse_response('{"units": [{"start_paragraph": 0, "end_paragraph": 0}, {"start_paragraph": 2, "end_paragraph": 2}]}', _report()["paragraphs"])


def test_paragraph_assessment_returns_one_entry_per_paragraph():
    report = _report()
    request = build_paragraph_assessment_request(report, report["paragraphs"])
    payload = json.loads(request["messages"][1]["content"])
    assert [item["paragraph_index"] for item in payload["paragraphs"]] == [0, 1, 2]
    result = _parse_paragraph_assessment(
        json.dumps({"assessments": [
            {"paragraph_index": 0, "topic": "history", "role": "procedural"},
            {"paragraph_index": 1, "topic": "history", "role": "party position"},
            {"paragraph_index": 2, "topic": "reasonableness", "role": "legal test"},
        ]}),
        report["paragraphs"],
    )
    assert [item["topic"] for item in result["assessments"]] == ["history", "history", "reasonableness"]


def test_paragraph_assessment_keeps_valid_partial_results_in_source_order():
    result = _parse_paragraph_assessment(
        '{"assessments": [{"paragraph_index": 2, "topic": "law"}, {"paragraph_index": 0, "topic": "history"}]}',
        _report()["paragraphs"],
    )
    assert [item["paragraph_index"] for item in result["assessments"]] == [0, 1, 2]
    assert result["assessments"][1]["topic"] == "Not found"
    assert result["missing_paragraph_indices"] == [1]


def test_paragraph_assessment_keeps_placeholders_for_duplicate_or_unknown_indices():
    result = _parse_paragraph_assessment(
        '{"assessments": [{"paragraph_index": 0}, {"paragraph_index": 0}, {"paragraph_index": 99}]}',
        _report()["paragraphs"],
    )
    assert result["returned_assessment_count"] == 1
    assert result["unmatched_assessment_count"] == 2
    assert all(item["paragraph_index"] in {0, 1, 2} for item in result["assessments"])


def test_paragraph_assessment_recovers_complete_objects_from_truncated_json():
    result = _parse_paragraph_assessment(
        '{"assessments": [{"paragraph_index": 0, "topic": "history"}, {"paragraph_index": 1, "topic": "law"}',
        _report()["paragraphs"],
    )
    assert result["returned_assessment_count"] == 2
    assert result["response_complete"] is False
    assert result["assessments"][2]["topic"] == "Not found"


def test_package_cli_creates_nested_output_directories_for_replay(tmp_path: Path):
    input_path = tmp_path / "input.json"
    response_path = tmp_path / "response.json"
    request_path = tmp_path / "nested" / "request.json"
    markdown_path = tmp_path / "nested" / "reviews" / "case.md"
    input_path.write_text(json.dumps(_report()), encoding="utf-8")
    response_path.write_text(json.dumps({"units": [{"start_paragraph": 0, "end_paragraph": 2, "label": "Analysis"}]}), encoding="utf-8")

    from scripts.package_discussion_units_llm import main
    import sys
    original = sys.argv
    sys.argv = ["package", "--input-json", str(input_path), "--output-request", str(request_path), "--output-markdown", str(markdown_path), "--response-file", str(response_path)]
    try:
        assert main() == 0
    finally:
        sys.argv = original

    assert markdown_path.exists()


def test_model_segmentation_requires_exact_contiguous_source_offsets():
    source = "Intro\n[1] First\n[2] Second\nOutro"
    parsed = parse_segments(
        json.dumps({"segments": [
            {"kind": "intro", "start_offset": 0, "end_offset": 6, "text": "Intro\n"},
            {"kind": "paragraph", "paragraph_number": 1, "start_offset": 6, "end_offset": 15, "text": "[1] First"},
            {"kind": "paragraph", "paragraph_number": 2, "start_offset": 15, "end_offset": 26, "text": "\n[2] Second"},
            {"kind": "outro", "start_offset": 26, "end_offset": len(source), "text": "\nOutro"},
        ]}),
        source,
    )
    assert [item["paragraph_index"] for item in parsed if item["kind"] == "paragraph"] == [0, 1]
    with pytest.raises(ValueError, match="gap, overlap"):
        parse_segments(
            '{"segments": [{"kind": "paragraph", "start_offset": 1, "end_offset": 4, "text": "ntr"}]}',
            source,
        )


def test_model_report_uses_model_paragraphs_without_deterministic_baseline():
    source = "[1] First\n[2] Second"
    segments = parse_segments(
        json.dumps({"segments": [
            {"kind": "paragraph", "paragraph_number": 1, "start_offset": 0, "end_offset": 10, "text": "[1] First\n"},
            {"kind": "paragraph", "paragraph_number": 2, "start_offset": 10, "end_offset": len(source), "text": "[2] Second"},
        ]}),
        source,
    )
    report = build_model_report(7, source, segments)
    request = build_request(report, text_only=True, normalize_legal_paragraphs=False)
    payload = json.loads(request["messages"][1]["content"])
    assert payload["paragraph_window"] == {"first_allowed": 0, "last_allowed": 1}
    assert "deterministic_baseline" not in payload