import json

import pytest

from scripts.package_discussion_units_llm import _legal_paragraphs, _parse_response, build_request, render_markdown


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
    markdown = render_markdown(_report(), result, model="test-model")
    assert "Paragraphs 0-1: Procedural history" in markdown
    assert "This explains how the application reached the Court." in markdown


def test_response_rejects_gaps():
    with pytest.raises(ValueError, match="contiguous"):
        _parse_response('{"units": [{"start_paragraph": 0, "end_paragraph": 0}, {"start_paragraph": 2, "end_paragraph": 2}]}', _report()["paragraphs"])