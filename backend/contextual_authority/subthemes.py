from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import json
import re
from typing import Sequence

from .discussion_units import DiscussionUnit, ParagraphFeatures
from .models import text_hash


SUBTHEME_METHOD = "deterministic_subthemes_v1"
SUBTHEME_VERSION = "1.4"
_ARGUMENT_CUES: tuple[tuple[str, str, str], ...] = (
    ("issue", r"\b(?:issue|issues|question|whether)\b", "explicit issue/question cue"),
    ("party_position", r"\b(?:argue|argues|argued|submit|submits|submitted|claim|claims|claimed|contend|contends|assert|asserts)\b", "explicit party-position cue"),
    ("evidence_fact", r"\b(?:evidence|record|testimony|affidavit|found that|determined that)\b", "explicit evidence/fact cue"),
    ("governing_rule", r"\b(?:under|pursuant to|standard of review|legal test|jurisprudence|principles)\b", "explicit rule/doctrine cue"),
    ("reasoning_application", r"\b(?:because|therefore|accordingly|I find|we find|appl(?:y|ied|ies)|conclude|concludes)\b", "explicit reasoning/application cue"),
    ("counterargument_limitation", r"\b(?:however|although|but|nevertheless|notwithstanding|fails|cannot)\b", "explicit limitation/counterargument cue"),
    ("disposition", r"\b(?:dismissed|allowed|granted|denied|quashed|upheld|varied)\b", "operative disposition cue"),
)
_PARTY_ACTOR_RE = re.compile(r"\b(?:applicant|applicants|respondent|respondents|claimant|claimants|counsel|party|parties|court|tribunal|panel|member|rad|rpd|he|she|they)\b", re.IGNORECASE)
_PROCEDURAL_CLAIM_PREFIX_RE = re.compile(
    r"(?:refugee|asylum|protection|the|this|that|his|her|their|applicant['’]s|applicants['’])\s*$",
    re.IGNORECASE,
)
_PROCEDURAL_CLAIM_SUFFIX_RE = re.compile(
    r"^\s+(?:for|of|on|only\s+under|was|were|is|are)\b",
    re.IGNORECASE,
)
_PROCEDURAL_CLAIM_RELATION_RE = re.compile(
    r"(?:elements?\s+of|basis\s+of|support(?:ing)?|included\s+on)\s+(?:the|this|his|her|their|a)\s*$",
    re.IGNORECASE,
)
_NON_RULE_UNDER_RE = re.compile(
    r"^\s+(?:the\s+laws\s+of|their\s+own|his\s+own|her\s+own|its\s+own|an\s+agenda)\b",
    re.IGNORECASE,
)
_PROCEDURAL_CONTRAST_RE = re.compile(r"\balthough\s+(?:the\s+)?part(?:y|ies)(?:['’]s?)?\s+arguments?\b", re.IGNORECASE)
_METADATA_ONLY_RE = re.compile(
    r"(?:judgment\s+and\s+reasons|solicitors?\s+of\s+record|appearances?|style\s+of\s+cause|"
    r"place\s+of\s+hearing|date\s+of\s+hearing|certified\s+true\s+translation|"
    r"docket\s*:|record\s*:?)",
    re.IGNORECASE,
)
_DISPLAY_TERM_NOISE = frozenset(
    "applicant applicants respondent respondents claimant claimants defendant plaintiff counsel party parties "
    "found decision court tribunal board member panel evidence claim record test application appeal issue argued "
    "held immigration citizenship canada minister judgment reasons appearances attorney general docket cause".split()
)
_STOPWORDS = frozenset(
    "a about after again all also an and are as at be been being before between both but by can could did do does for from had has have he her here his how i if in into is it its may more most must no not of on one only or other our out over said same should so some such than that the their them then there these they this those through to under until was we were what when where which while who will with would you your".split()
)
_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9'-]{2,}")


@dataclass(frozen=True)
class ArgumentEvidence:
    case_id: int
    paragraph_index: int
    chunk_id: int
    start_offset: int
    end_offset: int
    text: str
    role: str
    cue: str
    rationale: str
    source_text_hash: str
    context_start_offset: int
    context_end_offset: int
    context_text: str
    method: str = SUBTHEME_METHOD
    version: str = SUBTHEME_VERSION

    def __post_init__(self) -> None:
        if self.start_offset < 0 or self.start_offset >= self.end_offset:
            raise ValueError("argument evidence offsets must be a non-empty span")
        if self.end_offset - self.start_offset != len(self.text):
            raise ValueError("argument evidence offsets must match text length")
        if len(self.source_text_hash) != 64:
            raise ValueError("argument evidence requires a source SHA-256 hash")
        if self.context_start_offset < 0 or self.context_start_offset >= self.context_end_offset:
            raise ValueError("argument context offsets must be a non-empty span")
        if self.context_end_offset - self.context_start_offset != len(self.context_text):
            raise ValueError("argument context offsets must match context text length")


@dataclass(frozen=True)
class SubTheme:
    case_id: int
    discussion_unit_id: str
    subtheme_index: int
    paragraph_indices: tuple[int, ...]
    key_terms: tuple[str, ...]
    display_key_terms: tuple[str, ...]
    argument_roles: tuple[str, ...]
    argument_evidence: tuple[ArgumentEvidence, ...]
    text: str
    text_sha256: str
    config_hash: str
    method: str = SUBTHEME_METHOD
    version: str = SUBTHEME_VERSION

    @property
    def subtheme_id(self) -> str:
        return f"{self.discussion_unit_id}:subtheme:{self.subtheme_index}"

    @property
    def explanation(self) -> str:
        roles = ", ".join(self.argument_roles) or "no explicit argument role cue"
        terms = ", ".join(self.display_key_terms) or "no filtered content terms"
        start = self.paragraph_indices[0]
        end = self.paragraph_indices[-1]
        statements = _evidence_contexts(self.argument_evidence, "party_position")
        authorities = _evidence_contexts(self.argument_evidence, "governing_rule")
        treatment = _evidence_contexts(self.argument_evidence, "reasoning_application")
        outcomes = _evidence_contexts(self.argument_evidence, "disposition")
        details = [f"Observed roles: {roles}", f"Display terms: {terms}"]
        if not self.argument_evidence:
            details.append(
                "No explicit argument evidence was detected in this span; "
                "review it as metadata or cue-free text"
            )
        if statements:
            details.append(f"Position/evidence statements: {statements}")
        if authorities:
            details.append(f"Rule/authority context: {authorities}")
        if treatment:
            details.append(f"Application context: {treatment}")
        if outcomes:
            details.append(f"Operative outcome context: {outcomes}")
        return (
            f"{' '.join(details)} Evidence spans paragraphs {start}-{end}. "
            "This is a deterministic evidence summary, not a legal conclusion."
        )


def _content_terms(text: str) -> frozenset[str]:
    return frozenset(
        word
        for word in _WORD_RE.findall(text.casefold())
        if word not in _STOPWORDS and len(word) > 3
    )


def _display_terms(terms: Sequence[str]) -> tuple[str, ...]:
    return tuple(term for term in terms if term not in _DISPLAY_TERM_NOISE)


def _compact_contexts(evidence: Sequence[ArgumentEvidence], role: str) -> tuple[str, ...]:
    contexts: list[str] = []
    for item in evidence:
        if item.role == role and item.context_text not in contexts:
            contexts.append(" ".join(item.context_text.split())[:220])
    return tuple(contexts[:2])


def _evidence_contexts(evidence: Sequence[ArgumentEvidence], role: str) -> str:
    contexts = _compact_contexts(evidence, role)
    return " | ".join(contexts)


def _sentence_bounds(text: str, position: int) -> tuple[int, int]:
    starts = [text.rfind(marker, 0, position) + 1 for marker in ".?!"]
    start = max(starts)
    while start < len(text) and text[start].isspace():
        start += 1
    endings = [index for marker in ".?!" if (index := text.find(marker, position)) >= 0]
    end = min(endings) + 1 if endings else len(text)
    return start, end


def _has_contrast_context(text: str, match: re.Match[str], *, soft_context_chars: int = 240) -> bool:
    before = text[:match.start()]
    cue = match.group(0).casefold()
    if cue in {"however", "although", "nevertheless", "notwithstanding"}:
        if cue == "although" and _PROCEDURAL_CONTRAST_RE.match(text[match.start():]):
            return False
        return bool(before.strip() and re.search(r"[.!?;:]", before))
    bounded_before = before[-soft_context_chars:]
    return bool(bounded_before.strip() and re.search(
        r"\b(?:argues?|submits?|claims?|found|concludes?|evidence|decision)\b",
        bounded_before,
        re.IGNORECASE,
    ))


def _is_procedural_claim_reference(sentence_text: str, start: int, end: int) -> bool:
    before = sentence_text[max(0, start - 60):start]
    after = sentence_text[end:end + 60]
    return bool(
        _PROCEDURAL_CLAIM_PREFIX_RE.search(before)
        or _PROCEDURAL_CLAIM_SUFFIX_RE.match(after)
        or _PROCEDURAL_CLAIM_RELATION_RE.search(before)
    )


def _is_metadata_only(paragraph: ParagraphFeatures) -> bool:
    text = " ".join(paragraph.text.split())
    if not text:
        return True
    if _METADATA_ONLY_RE.search(text) and not re.search(r"\[\d+\]", text):
        return True
    return paragraph.is_heading and not re.search(r"\[\d+\]", text) and len(text.split()) <= 12


def extract_argument_evidence(paragraph: ParagraphFeatures) -> tuple[ArgumentEvidence, ...]:
    if _is_metadata_only(paragraph):
        return ()
    evidence: list[ArgumentEvidence] = []
    for role, pattern, rationale in _ARGUMENT_CUES:
        match = re.search(pattern, paragraph.text, re.IGNORECASE)
        if not match:
            continue
        context_start, context_end = _sentence_bounds(paragraph.text, match.start())
        sentence_text = paragraph.text[context_start:context_end]
        if role == "party_position" and not _PARTY_ACTOR_RE.search(sentence_text[: match.end() - context_start]):
            continue
        if role == "party_position" and match.group(0).casefold().startswith("claim"):
            if _is_procedural_claim_reference(sentence_text, match.start() - context_start, match.end() - context_start):
                continue
        if role == "governing_rule" and match.group(0).casefold() == "under":
            if _NON_RULE_UNDER_RE.match(paragraph.text[match.end():]):
                continue
        if role == "counterargument_limitation" and not _has_contrast_context(paragraph.text, match):
            continue
        evidence.append(
            ArgumentEvidence(
                case_id=paragraph.case_id,
                paragraph_index=paragraph.paragraph_index,
                chunk_id=paragraph.chunk_id,
                start_offset=paragraph.start_offset + match.start(),
                end_offset=paragraph.start_offset + match.end(),
                text=match.group(0),
                role=role,
                cue=match.group(0),
                rationale=rationale,
                source_text_hash=paragraph.source_sha256,
                context_start_offset=paragraph.start_offset + context_start,
                context_end_offset=paragraph.start_offset + context_end,
                context_text=paragraph.text[context_start:context_end],
            )
        )
    return tuple(evidence)


def _similarity(left: frozenset[str], right: frozenset[str]) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def _config_hash(threshold: float, consecutive_low_similarity: int) -> str:
    payload = {
        "threshold": threshold,
        "consecutive_low_similarity": consecutive_low_similarity,
        "method": SUBTHEME_METHOD,
        "version": SUBTHEME_VERSION,
    }
    return text_hash(json.dumps(payload, sort_keys=True, separators=(",", ":")))


def segment_subthemes(
    unit: DiscussionUnit,
    *,
    threshold: float = 0.08,
    consecutive_low_similarity: int = 2,
) -> tuple[SubTheme, ...]:
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    if consecutive_low_similarity < 1:
        raise ValueError("consecutive_low_similarity must be positive")

    paragraphs = unit.paragraphs
    if not paragraphs:
        return ()
    config_hash = _config_hash(threshold, consecutive_low_similarity)
    terms = tuple(_content_terms(paragraph.text) for paragraph in paragraphs)
    observations = tuple(extract_argument_evidence(paragraph) for paragraph in paragraphs)
    groups: list[tuple[int, int]] = []
    start = 0
    anchor_terms = terms[0]
    low_similarity = 0
    for index in range(1, len(paragraphs)):
        similarity = _similarity(anchor_terms, terms[index])
        previous_roles = {item.role for item in observations[index - 1]}
        current_roles = {item.role for item in observations[index]}
        role_shift = bool(previous_roles and current_roles and previous_roles.isdisjoint(current_roles))
        if similarity < threshold and role_shift:
            low_similarity += 1
        else:
            low_similarity = 0
        explicit_issue_boundary = "issue" in current_roles and index > start + 1
        if explicit_issue_boundary or low_similarity >= consecutive_low_similarity:
            boundary = index if explicit_issue_boundary else index - consecutive_low_similarity + 1
            groups.append((start, boundary))
            start = boundary
            anchor_terms = terms[start]
            low_similarity = 0
    groups.append((start, len(paragraphs)))

    results: list[SubTheme] = []
    for subtheme_index, (group_start, group_end) in enumerate(groups, 1):
        selected = paragraphs[group_start:group_end]
        selected_observations = tuple(item for observations_slice in observations[group_start:group_end] for item in observations_slice)
        term_counts = Counter(term for paragraph_terms in terms[group_start:group_end] for term in paragraph_terms)
        key_terms = tuple(term for term, _ in sorted(term_counts.items(), key=lambda item: (-item[1], item[0]))[:8])
        roles = tuple(sorted({item.role for item in selected_observations}))
        text = "\n\n".join(paragraph.text for paragraph in selected)
        results.append(
            SubTheme(
                case_id=unit.case_id,
                discussion_unit_id=unit.discussion_unit_id,
                subtheme_index=subtheme_index,
                paragraph_indices=tuple(paragraph.paragraph_index for paragraph in selected),
                key_terms=key_terms,
                display_key_terms=_display_terms(key_terms),
                argument_roles=roles,
                argument_evidence=selected_observations,
                text=text,
                text_sha256=text_hash(text),
                config_hash=config_hash,
            )
        )
    return tuple(results)
