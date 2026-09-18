from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Any

from .models import text_hash

TEACHER_CONTRACT_VERSION = "treatment_teacher_v1"
DEFAULT_MODEL = "gpt-4.1-nano"


@dataclass(frozen=True)
class TeacherCitation:
    ordinal: int
    citation_text: str
    normalized_citation: str | None
    start_offset: int
    end_offset: int

    def __post_init__(self) -> None:
        if self.start_offset < 0 or self.start_offset >= self.end_offset:
            raise ValueError("citation offsets must be a non-empty span")
        if self.end_offset > 100_000:
            raise ValueError("citation span is unreasonably large")


@dataclass(frozen=True)
class TeacherExample:
    example_id: str
    text: str
    citations: tuple[TeacherCitation, ...]
    source_text_sha256: str

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("teacher example text must not be empty")
        if text_hash(self.text) != self.source_text_sha256:
            raise ValueError("source_text_sha256 must match text")
        for citation in self.citations:
            if self.text[citation.start_offset : citation.end_offset] != citation.citation_text:
                raise ValueError("citation span does not reconstruct from example text")


@dataclass(frozen=True)
class TeacherBatch:
    request_id: str
    model: str
    budget_usd: float
    examples: tuple[TeacherExample, ...]
    contract_version: str = TEACHER_CONTRACT_VERSION

    def __post_init__(self) -> None:
        if self.budget_usd <= 0:
            raise ValueError("budget_usd must be positive")
        if self.budget_usd > 10.0:
            raise ValueError("teacher batch budget may not exceed 10 USD")
        if not self.examples:
            raise ValueError("teacher batch must contain at least one example")


def build_teacher_messages(batch: TeacherBatch) -> list[dict[str, str]]:
    system = (
        "You label legal authority treatment in short public legal-text excerpts. "
        "Only identify treatment of the listed citations, not legal merits or case outcome. "
        "Return a JSON object with a labels array. Each label must contain example_id, "
        "citation_ordinal, treatment (supportive, distinguishing, negative, neutral, "
        "absent, or ambiguous), phrase, phrase_start, phrase_end, confidence, and rationale. "
        "Offsets are character offsets in the supplied example text. Use absent when the "
        "citation is present but no treatment language is supported. Use ambiguous when "
        "the wording is uncertain. Never invent a citation or phrase. Before returning each "
        "label, verify that supplied_text[phrase_start:phrase_end] exactly equals phrase; "
        "phrase offsets are not citation offsets. Return exactly one label for each listed "
        "citation, never duplicate an example_id/citation_ordinal pair. For absent, use an "
        "empty phrase with phrase_start 0 and phrase_end 0. For non-absent labels, phrase "
        "must be the treatment or reasoning clause, not the citation text or a generic noun."
    )
    payload = {
        "request_id": batch.request_id,
        "contract_version": batch.contract_version,
        "examples": [
            {
                "example_id": example.example_id,
                "text": example.text,
                "source_text_sha256": example.source_text_sha256,
                "citations": [
                    {
                        "ordinal": citation.ordinal,
                        "citation_text": citation.citation_text,
                        "normalized_citation": citation.normalized_citation,
                        "start_offset": citation.start_offset,
                        "end_offset": citation.end_offset,
                    }
                    for citation in example.citations
                ],
            }
            for example in batch.examples
        ],
    }
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": json.dumps(payload, ensure_ascii=True, sort_keys=True)},
    ]


def estimate_tokens(messages: list[dict[str, str]]) -> int:
    return max(1, sum(len(message["content"]) for message in messages) // 4)


def estimate_cost_usd(
    messages: list[dict[str, str]],
    *,
    output_tokens: int = 800,
    input_cost_per_1m: float = 0.10,
    output_cost_per_1m: float = 0.40,
) -> float:
    input_tokens = estimate_tokens(messages)
    return (input_tokens / 1_000_000 * input_cost_per_1m) + (
        output_tokens / 1_000_000 * output_cost_per_1m
    )


def load_teacher_examples(path: str) -> tuple[TeacherExample, ...]:
    examples: list[TeacherExample] = []
    with open(path, encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            payload: dict[str, Any] = json.loads(line)
            citations = tuple(TeacherCitation(**item) for item in payload["citations"])
            examples.append(
                TeacherExample(
                    example_id=str(payload["example_id"]),
                    text=str(payload["text"]),
                    citations=citations,
                    source_text_sha256=str(payload["source_text_sha256"]),
                )
            )
    if not examples:
        raise ValueError(f"no teacher examples found in {path}")
    return tuple(examples)
