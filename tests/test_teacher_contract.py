import json

import pytest

from backend.contextual_authority.models import text_hash
from backend.contextual_authority.teacher_contract import (
    TeacherBatch,
    TeacherCitation,
    TeacherExample,
    build_teacher_messages,
    estimate_cost_usd,
    load_teacher_examples,
)
from scripts.build_treatment_teacher_fixture import build_fixture
from scripts.run_treatment_teacher_batch import parse_teacher_response
from scripts.build_treatment_distillation import build_distillation
from scripts.build_treatment_review_packet import build_packet, render_markdown


def make_example() -> TeacherExample:
    text = "The Court follows Smith v. Canada in this analysis."
    citation_text = "Smith v. Canada"
    start = text.index(citation_text)
    return TeacherExample(
        example_id="example-1",
        text=text,
        source_text_sha256=text_hash(text),
        citations=(TeacherCitation(0, citation_text, "smith", start, start + len(citation_text)),),
    )


def test_teacher_messages_include_context_citation_and_exact_offsets(tmp_path):
    batch = TeacherBatch("request-1", "cheap-model", 10.0, (make_example(),))

    messages = build_teacher_messages(batch)
    payload = json.loads(messages[1]["content"])

    assert payload["examples"][0]["text"] == make_example().text
    assert payload["examples"][0]["citations"][0]["citation_text"] == "Smith v. Canada"
    assert estimate_cost_usd(messages) < 10.0


def test_teacher_example_rejects_broken_source_span():
    with pytest.raises(ValueError, match="citation span"):
        TeacherExample(
            example_id="bad",
            text="Smith v. Canada",
            source_text_sha256=text_hash("Smith v. Canada"),
            citations=(TeacherCitation(0, "Wrong", None, 0, 5),),
        )


def test_teacher_batch_budget_is_hard_capped():
    with pytest.raises(ValueError, match="may not exceed"):
        TeacherBatch("request-1", "cheap-model", 10.01, (make_example(),))


def test_teacher_fixture_loader_preserves_contract(tmp_path):
    path = tmp_path / "fixture.jsonl"
    example = make_example()
    path.write_text(
        json.dumps(
            {
                "example_id": example.example_id,
                "text": example.text,
                "source_text_sha256": example.source_text_sha256,
                "citations": [example.citations[0].__dict__],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    loaded = load_teacher_examples(str(path))

    assert loaded == (example,)


def test_fixture_builder_prioritizes_second_half_citations():
    class Citation:
        def __init__(self, offset_start, offset_end):
            self.offset_start = offset_start
            self.offset_end = offset_end
            self.normalized_citation = "authority"
            self.source_case_id = 1

    class Chunk:
        text = "a" * 100

        def __init__(self, chunk_index):
            self.chunk_index = chunk_index

    class Result:
        def __init__(self):
            self.rows = [(Citation(10, 20), Chunk(1)), (Citation(70, 80), Chunk(3))]

        def __iter__(self):
            return iter(self.rows)

    class Session:
        def execute(self, _statement):
            return Result()

    rows = build_fixture(Session(), case_ids=[], limit=1, context_chars=10)

    assert len(rows) == 1
    assert rows[0]["citations"][0]["start_offset"] == 10


def test_fixture_builder_marks_richer_legal_context_signals_without_labeling_treatment():
    class Citation:
        offset_start = 70
        offset_end = 85
        normalized_citation = "authority"
        source_case_id = 1

    class Chunk:
        chunk_index = 3
        text = "The Court applies the governing test because the authority is binding. Smith v. Canada"

    class Result:
        def __iter__(self):
            return iter([(Citation(), Chunk())])

    class Session:
        def execute(self, _statement):
            return Result()

    rows = build_fixture(Session(), case_ids=[], limit=1, context_chars=100)

    assert rows[0]["candidate_label"] == "review_required"
    assert rows[0]["signal_flags"]["application_language"] is True
    assert rows[0]["signal_flags"]["authority_strength"] is True
    assert rows[0]["signal_flags"]["explanation_language"] is True
    assert rows[0]["signal_terms"]["application_language"] == ["applies"]


def test_fixture_builder_gives_post_citation_treatment_more_context():
    class Citation:
        offset_start = 50
        offset_end = 59
        normalized_citation = "authority"
        source_case_id = 1

    class Chunk:
        chunk_index = 3
        text = "A" * 50 + "authority" + "B" * 20 + "The Court applies the authority to the facts and explains why the argument fails."

    class Result:
        def __iter__(self):
            return iter([(Citation(), Chunk())])

    class Session:
        def execute(self, _statement):
            return Result()

    rows = build_fixture(Session(), case_ids=[], limit=1, context_chars=10)
    row = rows[0]

    assert row["context_before_chars"] == 10
    assert row["context_after_chars"] == 20
    assert row["citations"][0]["start_offset"] == 10
    assert row["text"][row["citations"][0]["start_offset"] : row["citations"][0]["end_offset"]] == "authority"


def test_teacher_response_parser_keeps_only_source_backed_labels():
    example = {
        "example_id": "example-1",
        "text": "The Court follows Smith v. Canada in this analysis.",
        "citations": [{"citation_text": "Smith v. Canada"}],
    }
    response = {
        "labels": [
            {
                "example_id": "example-1",
                "citation_ordinal": 0,
                "treatment": "supportive",
                "phrase": "follows",
                "phrase_start": 10,
                "phrase_end": 17,
            },
            {
                "example_id": "example-1",
                "citation_ordinal": 0,
                "treatment": "negative",
                "phrase": "invented",
                "phrase_start": 0,
                "phrase_end": 8,
            },
        ]
    }

    parsed = parse_teacher_response(json.dumps(response), [example])

    assert len(parsed["labels"]) == 1
    assert parsed["labels"][0]["phrase"] == "follows"
    assert len(parsed["invalid_labels"]) == 1


def test_teacher_response_parser_accepts_json_fences():
    example = {
        "example_id": "example-1",
        "text": "The Court follows Smith v. Canada in this analysis.",
        "citations": [{"citation_text": "Smith v. Canada"}],
    }

    parsed = parse_teacher_response("```json\n{\"labels\": []}\n```", [example])

    assert parsed == {"labels": [], "invalid_labels": []}


def test_teacher_response_parser_repairs_unique_phrase_offset():
    example = {
        "example_id": "example-1",
        "text": "The Court follows Smith v. Canada in this analysis.",
        "citations": [{"citation_text": "Smith v. Canada"}],
    }
    response = {
        "labels": [
            {
                "example_id": "example-1",
                "citation_ordinal": 0,
                "treatment": "supportive",
                "phrase": "follows",
                "phrase_start": 0,
                "phrase_end": 7,
            }
        ]
    }

    parsed = parse_teacher_response(json.dumps(response), [example])

    assert parsed["labels"][0]["phrase_start"] == 10
    assert parsed["labels"][0]["offsets_repaired"] is True


def test_teacher_response_parser_rejects_duplicate_citation_labels():
    example = {
        "example_id": "example-1",
        "text": "The Court follows Smith v. Canada in this analysis.",
        "citations": [{"citation_text": "Smith v. Canada"}],
    }
    label = {
        "example_id": "example-1",
        "citation_ordinal": 0,
        "treatment": "supportive",
        "phrase": "follows",
        "phrase_start": 10,
        "phrase_end": 17,
    }

    parsed = parse_teacher_response(json.dumps({"labels": [label, label]}), [example])

    assert len(parsed["labels"]) == 1
    assert "duplicate label" in parsed["invalid_labels"][0]


def test_teacher_response_parser_requires_empty_phrase_for_absent():
    example = {
        "example_id": "example-1",
        "text": "The Court follows Smith v. Canada in this analysis.",
        "citations": [{"citation_text": "Smith v. Canada"}],
    }
    response = {
        "labels": [
            {
                "example_id": "example-1",
                "citation_ordinal": 0,
                "treatment": "absent",
                "phrase": "Smith v. Canada",
                "phrase_start": 20,
                "phrase_end": 34,
            }
        ]
    }

    parsed = parse_teacher_response(json.dumps(response), [example])

    assert not parsed["labels"]
    assert "absent treatment" in parsed["invalid_labels"][0]


def test_teacher_response_parser_validates_argument_level_treatment_context():
    text = "The applicant relies on Smith v. Canada to support the argument. The Court rejects that argument."
    example = {
        "example_id": "example-1",
        "text": text,
        "citations": [{"citation_text": "Smith v. Canada"}],
    }

    def field(status, phrase="", label=None):
        start = text.index(phrase) if phrase else 0
        value = {"status": status, "text": phrase, "start": start, "end": start + len(phrase)}
        if label is not None:
            value["label"] = label
        return value

    context = {
        "actor": field("stated", "applicant", "party"),
        "reason_raised": field("stated", "to support the argument"),
        "argument_supported": field("stated", "the argument"),
        "argument_addressed": field("stated", "that argument"),
        "court_response": field("stated", "rejects that argument", "negative"),
        "argument_conclusion": field("stated", "that argument", "rejected"),
    }
    response = {
        "labels": [{
            "example_id": "example-1",
            "citation_ordinal": 0,
            "treatment": "negative",
            "phrase": "rejects that argument",
            "phrase_start": text.index("rejects that argument"),
            "phrase_end": text.index("rejects that argument") + len("rejects that argument"),
            "treatment_context": context,
        }]
    }

    parsed = parse_teacher_response(json.dumps(response), [example])

    assert not parsed["invalid_labels"]
    assert parsed["labels"][0]["treatment_context"]["actor"]["text"] == "applicant"
    assert parsed["labels"][0]["treatment_context"]["court_response"]["label"] == "negative"


def test_teacher_response_parser_rejects_inferred_argument_context():
    example = {
        "example_id": "example-1",
        "text": "Smith v. Canada is mentioned.",
        "citations": [{"citation_text": "Smith v. Canada"}],
    }
    phrase_start = example["text"].index("mentioned")
    response = {
        "labels": [{
            "example_id": "example-1",
            "citation_ordinal": 0,
            "treatment": "neutral",
            "phrase": "mentioned",
            "phrase_start": phrase_start,
            "phrase_end": phrase_start + len("mentioned"),
            "treatment_context": {
                "actor": {"status": "stated", "text": "the applicant", "start": 0, "end": 13},
            },
        }]
    }

    parsed = parse_teacher_response(json.dumps(response), [example])

    assert not parsed["labels"]
    assert "actor span mismatch" in parsed["invalid_labels"][0]


def test_distillation_revalidates_labels_and_requires_repeated_phrases(tmp_path):
    fixture = tmp_path / "fixture.jsonl"
    example = make_example()
    fixture.write_text(
        json.dumps(
            {
                "example_id": example.example_id,
                "text": example.text,
                "source_text_sha256": example.source_text_sha256,
                "citations": [example.citations[0].__dict__],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    result = tmp_path / "result.json"
    label = {
        "example_id": "example-1",
        "citation_ordinal": 0,
        "treatment": "supportive",
        "phrase": "follows",
        "phrase_start": 10,
        "phrase_end": 17,
        "confidence": 0.95,
        "offsets_repaired": False,
    }
    conflicting_label = {**label, "treatment": "distinguishing", "phrase": "follows"}
    result.write_text(json.dumps({"results": [{"labels": [label, conflicting_label]}]}), encoding="utf-8")

    report = build_distillation(fixture, [result], min_confidence=0.85, min_count=1)

    assert report["runtime_publishable"] is False
    assert report["summary"]["valid_labels"] == 1
    assert report["summary"]["proposed_rule_count"] == 1
    assert report["rules"][0]["evidence"][0]["evidence_text"] == "follows"
    assert report["summary"]["rejected_counts"]["duplicate_label"] == 1


def test_review_packet_is_pending_and_keeps_evidence_trace(tmp_path):
    source = tmp_path / "candidate.json"
    fixture = tmp_path / "fixture.jsonl"
    fixture.write_text(
        json.dumps(
            {
                "example_id": "example-1",
                "text": "The Court follows Smith v. Canada because the facts are materially similar.",
                "citations": [
                    {
                        "ordinal": 0,
                        "citation_text": "Smith v. Canada",
                        "start_offset": 19,
                        "end_offset": 34,
                    }
                ],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    source.write_text(
        json.dumps(
            {
                "summary": {"eligible_labels": 1},
                "eligible_labels": [
                    {
                        "example_id": "example-1",
                        "citation_ordinal": 0,
                        "citation_text": "Smith v. Canada",
                        "treatment": "distinguishing",
                        "phrase": "the Court follows",
                        "phrase_start": 0,
                        "phrase_end": 16,
                        "confidence": 0.9,
                        "offsets_repaired": False,
                        "source_text_sha256": "hash",
                        "evidence_text": "the Court follows",
                    }
                ],
                "rules": [
                    {
                        "rule_id": "teacher-phrase-supportive-0001",
                        "treatment": "supportive",
                        "phrase": "the Court follows",
                        "support_count": 1,
                        "mean_confidence": 0.9,
                        "evidence": [
                            {
                                "example_id": "example-1",
                                "citation_text": "Smith v. Canada",
                                "source_text_sha256": "hash",
                                "evidence_text": "the Court follows",
                                "phrase_start": 0,
                                "phrase_end": 16,
                                "citation_ordinal": 0,
                                "offsets_repaired": True,
                                "confidence": 0.9,
                            }
                        ],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    packet = build_packet(source, packet_id="review-1", fixture_path=fixture)

    assert packet["status"] == "human_review_required"
    assert packet["runtime_publishable"] is False
    assert packet["review_summary"]["rules_with_repaired_spans"] == 1
    assert packet["review_summary"]["priority_label_count"] == 1
    assert packet["priority_labels"][0]["treatment"] == "distinguishing"
    assert "materially similar" in packet["priority_labels"][0]["decision_context"]
    assert packet["rules"][0]["review_status"] == "pending_review"
    assert packet["rules"][0]["evidence"][0]["evidence_text"] == "the Court follows"
    assert "How To Review" in render_markdown(packet)
