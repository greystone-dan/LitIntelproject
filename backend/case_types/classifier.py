"""Deterministic "what type of case is this" classifier.

Inputs are the decision text (plus optional court, title and docket). The evidence is
(1) which statutory provisions the decision discusses, counted more when they appear in
the opening where the court says what the case is about and ignoring the trailing annex
that merely reproduces legislation, and (2) a short list of plain-language cues.
Nothing here calls a model, a network service or a database.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import asdict, dataclass, field
from typing import Any, Iterable

from .claim_issues import issues_by_anchor
from .taxonomy import (
    CASE_TYPES,
    IMMIGRATION_INSTRUMENTS,
    IRPA,
    ALLOWED_GROUPS_BY_PROCEEDING,
    CONVENTION,
    SPECIFIC_PROTECTION_TYPES,
    TAXONOMY_VERSION,
    TYPES_BY_KEY,
    CaseType,
)

STATUS_CLASSIFIED = "classified"
STATUS_UNCLEAR = "unclear"
STATUS_NOT_IMMIGRATION = "not_immigration"
STATUS_INSUFFICIENT = "insufficient_text"

MIN_TEXT_CHARS = 1500
MIN_PRIMARY_SCORE = 6.0
MIN_LEAD_RATIO = 1.4
MIN_SECONDARY_SCORE = 6.0
SECONDARY_FRACTION = 0.5
GENERIC_SECOND_TYPES = frozenset({"refugee_claim", "protected_person_permanent_residence"})
SECOND_MAIN_INTRO_SCORE = 5.0  # the opening names the second type
SECOND_MAIN_FRACTION = 0.75  # or its evidence nearly matches the primary
INTRO_PROVISION_WEIGHT = 3.0
INTRO_CUE_WEIGHT = 5.0
BODY_CUE_WEIGHT = 0.5
PROVISION_CAP = 14.0
CUE_CAP = 10.0
INTRO_WINDOW_CHARS = 5000
DEMOTE_GENERAL_FACTOR = 0.35
MIN_PRIMARY_SCORE_KNOWN_FORUM = 4.0
CHUNK_CHARS = 30000
PREGATE_RE = re.compile(r"Immigration and Refugee Protection Act|Immigration Act|Citizenship Act|\bIRPA\b|\bIRPR\b|\bIMM-\d|Refugee Protection Division|Immigration and Refugee Board", re.IGNORECASE)

_ANNEX_RE = re.compile(
    r"^\s*(?:annex|appendix|schedule|annexe|relevant (?:legislat\w+|statutory provisions|provisions)|"
    r"legislative provisions|statutory provisions|dispositions (?:législatives|pertinentes))\b[^\n]{0,60}$",
    re.IGNORECASE | re.MULTILINE,
)
_DECISION_CONTENT_RE = re.compile(r"Decision Content|Contenu de la décision", re.IGNORECASE)
_FIRST_PARA_RE = re.compile(r"(?:^|\n)\s*\[1\]")
_EIGHTH_PARA_RE = re.compile(r"(?:^|\n)\s*\[8\]")
_IMMIGRATION_VOCAB_RE = re.compile(r"Minister of (?:Citizenship|Immigration|Public Safety|Employment and Immigration)|Immigration,? Refugees|Immigration and Refugee Board|Immigration Division|Immigration Appeal Division|Refugee (?:Protection|Appeal) Division|permanent resident|foreign national|Convention refugee|refugee (?:claim|status|protection)|deportation|removal order|visa officer|immigration (?:officer|consequence)", re.IGNORECASE)
_CRIMINAL_TITLE_RE = re.compile(r"^(?:R\.|Her Majesty|La Reine|Regina)\s+(?:v\.|c\.)", re.IGNORECASE)
_IMMIGRATION_TITLE_RE = re.compile(r"Citizenship|Immigration|Public Safety|Refugee|Minister of|Solicitor General|Canada Border|Council for", re.IGNORECASE)
CRIMINAL_CASE_MIN_HITS = 25
NON_IMMIGRATION_TITLE_MIN_HITS = 8
_PROCEDURAL_INTRO_RE = re.compile(
    r"(?:motion|application|request)\s+(?:\w+\s+){0,3}?(?:for\s+leave\s+)?to\s+(?:intervene|strike|quash)"
    r"|leave\s+to\s+intervene|for\s+an\s+order\s+striking|(?:motion|request)\s+for\s+an?\s+extension\s+of\s+time|costs\s+(?:against|awarded\s+against)",
    re.IGNORECASE,
)
_PRRA_OFFICER_HC_RE = re.compile(
    r"(?:pre-removal\s+risk\s+assessment|PRRA)\s+officer[^.]{0,160}?(?:humanitarian\s+and\s+compassionate|H&C)", re.IGNORECASE
)
_STAY_INTRO_RE = re.compile(
    r"(?:reasons (?:for|on) (?:the |a |my )?(?:stay|motion)|motion (?:for|to) (?:an? )?(?:order )?(?:staying|stay)|"
    r"(?:I|the Court) (?:have |has )?stayed|stay of (?:the |his |her |their )?removal|stay (?:the )?(?:execution|enforcement) of|"
    r"order (?:staying|prohibiting)[^.]{0,40}remov)",
    re.IGNORECASE,
)
STAY_INTRO_BONUS = 12.0
PRRA_OFFICER_HC_BONUS = 8.0
PROCEDURAL_INTRO_BONUS = 5.0
PROCEDURAL_INTRO_WINDOW = 250  # the first sentence or two, where the court says what it is deciding
APPEAL_COURT_CUE_ONLY_MIN_SCORE = 15.0
_ACT_NAME_RE = re.compile(r"Immigration and Refugee Protection Act|Immigration Act|Citizenship Act|\bIRPA\b", re.IGNORECASE)
_DOCKET_IMM_RE = re.compile(r"\bIMM-\d+-\d+\b|\bIMM-\d+\b")


@dataclass
class Evidence:
    kind: str  # "provision" or "cue"
    detail: str
    count: int
    in_intro: bool


@dataclass
class CaseTypeResult:
    taxonomy_version: str
    status: str
    primary_type: str | None
    primary_detail: str | None
    secondary_types: list[str]
    confidence: float
    scores: dict[str, float]
    candidates: list[str]
    proceeding: str | None
    evidence: list[dict[str, Any]] = field(default_factory=list)
    reason: str = ""
    issues: list[str] = field(default_factory=list)
    second_type: str | None = None
    second_detail: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# --------------------------------------------------------------------------------------
# Text windows
# --------------------------------------------------------------------------------------

def split_regions(text: str) -> tuple[str, str, int]:
    """Return (reasons_text, intro_text, intro_end_offset_in_reasons_text).

    The A2AJ and CanLII exports put a metadata header before the reasons; the trailing
    annex that reproduces legislation is cut off when it sits in the last half.
    """
    body = text or ""
    header = _DECISION_CONTENT_RE.search(body[:3000])
    start = header.end() if header else 0
    reasons = body[start:]
    cut = None
    for match in _ANNEX_RE.finditer(reasons):
        if match.start() > len(reasons) * 0.5:
            cut = match.start()
            break
    if cut is not None:
        reasons = reasons[:cut]
    first = _FIRST_PARA_RE.search(reasons)
    intro_start = first.start() if first else 0
    eighth = _EIGHTH_PARA_RE.search(reasons, intro_start)
    intro_end = min(intro_start + INTRO_WINDOW_CHARS, eighth.start() if eighth else len(reasons))
    intro_end = max(intro_end, min(len(reasons), intro_start + 1200))
    return reasons, reasons[intro_start:intro_end], intro_end


# --------------------------------------------------------------------------------------
# Provision handling
# --------------------------------------------------------------------------------------

def _section_number(section: str | None) -> float | None:
    if not section:
        return None
    match = re.match(r"(\d+)(?:\.(\d+))?", section)
    if not match:
        return None
    return float(f"{match.group(1)}.{match.group(2)}") if match.group(2) else float(match.group(1))


def provision_path(section: str | None, subsection: str | None, paragraph: str | None) -> str | None:
    if not section:
        return None
    parts = [section]
    for piece in (subsection, paragraph):
        if piece:
            piece = piece.strip()
            parts.append(piece if piece.startswith("(") else f"({piece.rstrip(')')})")
    return "".join(parts)


@dataclass(frozen=True)
class ProvisionHit:
    instrument: str | None
    section: str
    number: float
    subsection: str | None
    path: str
    offset: int
    confidence: float


def extract_law_rows(reasons: str, source_citations: list[str | None]) -> list[Any]:
    """Statute rows with offsets into ``reasons``. Long decisions are scanned in chunks: the shared
    second-pass scanner can take minutes on a single 130,000-character Supreme Court judgment."""
    from dataclasses import replace

    from ..citation_refine import refine_document

    if len(reasons) <= CHUNK_CHARS * 1.5:
        return list(refine_document(reasons, source_citations=source_citations).laws.rows)
    rows: list[Any] = []
    position = 0
    while position < len(reasons):
        end = min(len(reasons), position + CHUNK_CHARS)
        if end < len(reasons):
            boundary = reasons.rfind("\n[", position + CHUNK_CHARS // 2, end)
            end = boundary if boundary > position else end
        chunk = reasons[position:end]
        for row in refine_document(chunk, source_citations=source_citations).laws.rows:
            rows.append(replace(row, offset_start=row.offset_start + position, offset_end=row.offset_end + position))
        position = end
    return rows


def provision_hits(
    law_rows: Iterable[Any],
    *,
    cutoff: int | None = None,
    assume_irpa: bool = False,
) -> list[ProvisionHit]:
    hits: list[ProvisionHit] = []
    for row in law_rows:
        section = getattr(row, "section", None)
        number = _section_number(section)
        if number is None:
            continue
        instrument = getattr(row, "instrument_key", None)
        if instrument == CONVENTION and section:
            instrument = f"{CONVENTION}:{section.upper()}"
        confidence = float(getattr(row, "confidence", 1.0) or 0.0)
        if instrument is None:
            # A bare "section 44" with no instrument: only credit it to the IRPA in a decision
            # that is clearly about the IRPA, and at reduced weight.
            if not assume_irpa:
                continue
            instrument = IRPA
            confidence *= 0.5
        if confidence < 0.4:
            continue
        offset = int(getattr(row, "offset_start", 0) or 0)
        if cutoff is not None and offset >= cutoff:
            continue
        subsection = getattr(row, "subsection", None)
        if subsection and not subsection.startswith("("):
            subsection = f"({subsection})"
        path = provision_path(section, getattr(row, "subsection", None), getattr(row, "paragraph", None)) or section
        hits.append(ProvisionHit(instrument, section, number, subsection, path, offset, confidence))
    return hits


def _hit_matches(hit: ProvisionHit, case_type: CaseType) -> bool:
    for instrument, first, last, subsection in case_type.provisions:
        if hit.instrument != instrument:
            continue
        if not (first <= hit.number <= last):
            continue
        if subsection is not None and (hit.subsection or "") != subsection:
            continue
        return True
    return False


# --------------------------------------------------------------------------------------
# Proceeding (what is being reviewed)
# --------------------------------------------------------------------------------------

_PROCEEDING_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = tuple(
    (name, re.compile(pattern, re.IGNORECASE))
    for name, pattern in (
        ("jr_refugee_appeal_division", r"judicial review of (?:a |the )?(?:decision|determination)[^.]{0,120}Refugee Appeal Division"),
        ("jr_refugee_protection_division", r"judicial review of (?:a |the )?(?:decision|determination)[^.]{0,120}Refugee Protection Division"),
        ("jr_immigration_appeal_division", r"judicial review of (?:a |the )?(?:decision|determination)[^.]{0,120}Immigration Appeal Division"),
        ("jr_immigration_division", r"judicial review of (?:a |the )?(?:decision|determination)[^.]{0,120}Immigration Division"),
        ("jr_prra_officer", r"judicial review of (?:a |the )?(?:decision|determination)[^.]{0,120}(?:PRRA|pre-removal risk)"),
        ("jr_citizenship_judge", r"(?:appeal|judicial review)[^.]{0,80}citizenship judge"),
        ("jr_officer", r"judicial review of (?:a |the )?(?:decision|determination)[^.]{0,120}(?:officer|delegate|visa|IRCC|CBSA)"),
        ("stay_motion", r"motion (?:for|to) (?:a )?(?:stay|stay of removal)|stay of (?:the )?removal"),
        ("appeal_federal_court_of_appeal", r"appeal from (?:a |the )?(?:judgment|decision|order) of the Federal Court"),
    )
)


def detect_proceeding(intro: str, court: str | None = None) -> str | None:
    court_key = (court or "").strip().upper()
    if court_key in {"RPD", "RAD", "IAD", "ID"}:
        return f"tribunal_decision_{court_key.lower()}"
    for name, pattern in _PROCEEDING_PATTERNS:
        if pattern.search(intro):
            return name
    return None


# --------------------------------------------------------------------------------------
# Scoring
# --------------------------------------------------------------------------------------

def _cue_counts(case_type: CaseType, intro: str, reasons: str) -> tuple[Counter, Counter]:
    intro_hits: Counter = Counter()
    body_hits: Counter = Counter()
    for pattern in case_type.compiled_cues:
        intro_count = len(pattern.findall(intro))
        total = len(pattern.findall(reasons))
        if intro_count:
            intro_hits[pattern.pattern] = intro_count
        if total - intro_count > 0:
            body_hits[pattern.pattern] = total - intro_count
    return intro_hits, body_hits


def is_immigration_decision(
    hits: list[ProvisionHit],
    *,
    docket: str | None,
    title: str | None,
    court: str | None,
    intro: str,
) -> bool:
    court_key = (court or "").strip().upper()
    if court_key in {"RPD", "RAD", "IAD", "ID"}:
        return True
    if docket and _DOCKET_IMM_RE.search(docket):
        return True
    if _DOCKET_IMM_RE.search(intro[:2000]):
        return True
    return bool(_ACT_NAME_RE.search(intro) or _IMMIGRATION_VOCAB_RE.search(intro))


def classify_text(
    text: str | None,
    *,
    court: str | None = None,
    title: str | None = None,
    docket: str | None = None,
    source_citations: Iterable[str | None] = (),
) -> CaseTypeResult:
    """Classify one decision from its text."""
    content = text or ""
    if len(content) < MIN_TEXT_CHARS:
        return CaseTypeResult(TAXONOMY_VERSION, STATUS_INSUFFICIENT, None, None, [], 0.0, {}, [], None,
                              reason="decision text too short to classify")

    reasons, intro, intro_end = split_regions(content)
    if not PREGATE_RE.search(content):
        return CaseTypeResult(TAXONOMY_VERSION, STATUS_NOT_IMMIGRATION, None, None, [], 0.0, {}, [], None,
                              reason="no immigration statute, tribunal or IMM docket named anywhere in the text")
    law_rows = extract_law_rows(reasons, list(source_citations))
    irpa_mentions = sum(1 for row in law_rows if getattr(row, "instrument_key", None) in {IRPA, "canada.irpr"})
    hits = provision_hits(law_rows, cutoff=None, assume_irpa=irpa_mentions >= 3)

    proceeding = detect_proceeding(intro, court)
    if not is_immigration_decision(hits, docket=docket, title=title, court=court, intro=intro):
        return CaseTypeResult(TAXONOMY_VERSION, STATUS_NOT_IMMIGRATION, None, None, [], 0.0, {}, [], proceeding,
                              reason="no immigration or citizenship statute, IMM docket or immigration respondent")

    court_key = (court or "").strip().upper()
    if court_key not in {"FC", "RPD", "RAD", "IAD", "ID"} and title is not None:
        immigration_hits = sum(1 for hit in hits if hit.instrument in IMMIGRATION_INSTRUMENTS)
        if _CRIMINAL_TITLE_RE.match(title.strip()) and immigration_hits < CRIMINAL_CASE_MIN_HITS:
            return CaseTypeResult(TAXONOMY_VERSION, STATUS_NOT_IMMIGRATION, None, None, [], 0.0, {}, [], proceeding,
                                  reason="criminal appeal that mentions immigration only as a consequence")
        if not _IMMIGRATION_TITLE_RE.search(title) and immigration_hits < NON_IMMIGRATION_TITLE_MIN_HITS:
            return CaseTypeResult(TAXONOMY_VERSION, STATUS_UNCLEAR, None, None, [], 0.0, {}, [], proceeding,
                                  reason="title and statute density do not show an immigration case")

    scores: dict[str, float] = {}
    intro_scores: dict[str, float] = {}
    evidence: dict[str, list[Evidence]] = {}
    matched_hits: dict[str, list[ProvisionHit]] = {}
    for case_type in CASE_TYPES:
        provision_score = 0.0
        type_hits = [hit for hit in hits if _hit_matches(hit, case_type)]
        if type_hits:
            matched_hits[case_type.key] = type_hits
            by_path: Counter = Counter()
            intro_paths: set[str] = set()
            for hit in type_hits:
                in_intro = hit.offset < intro_end and hit.offset >= (intro_end - len(intro))
                weight = (INTRO_PROVISION_WEIGHT if in_intro else 1.0) * hit.confidence
                provision_score += weight
                by_path[hit.path] += 1
                if in_intro:
                    intro_paths.add(hit.path)
            provision_score = min(PROVISION_CAP, provision_score)
            evidence.setdefault(case_type.key, []).extend(
                Evidence("provision", path, count, path in intro_paths) for path, count in by_path.most_common(6)
            )
        intro_hits, body_hits = _cue_counts(case_type, intro, reasons)
        cue_score = min(CUE_CAP, min(sum(1 for _ in intro_hits), 2) * INTRO_CUE_WEIGHT
                        + BODY_CUE_WEIGHT * min(sum(body_hits.values()) + sum(intro_hits.values()), 8))
        for pattern, count in list(intro_hits.items())[:3]:
            evidence.setdefault(case_type.key, []).append(Evidence("cue", pattern, count, True))
        for pattern, count in body_hits.most_common(2):
            evidence.setdefault(case_type.key, []).append(Evidence("cue", pattern, count, False))
        intro_provision = sum(
            INTRO_PROVISION_WEIGHT * hit.confidence for hit in matched_hits.get(case_type.key, [])
            if intro_end - len(intro) <= hit.offset < intro_end
        )
        intro_scores[case_type.key] = intro_provision + min(2, len(intro_hits)) * INTRO_CUE_WEIGHT
        total = provision_score + cue_score
        if total > 0:
            scores[case_type.key] = round(total, 2)

    # A decision written to explain a stay of removal is about the stay, whatever risk grounds it discusses.
    if _STAY_INTRO_RE.search(intro):
        scores["removal_deferral_stay"] = round(scores.get("removal_deferral_stay", 0.0) + STAY_INTRO_BONUS, 2)
        intro_scores["removal_deferral_stay"] = intro_scores.get("removal_deferral_stay", 0.0) + STAY_INTRO_BONUS

    # A specific protection type outranks the generic ss. 96-97 vocabulary it is decided in.
    specific_present = any(scores.get(key, 0.0) >= MIN_PRIMARY_SCORE for key in SPECIFIC_PROTECTION_TYPES)
    if specific_present and "refugee_claim" in scores:
        scores["refugee_claim"] = round(scores["refugee_claim"] * DEMOTE_GENERAL_FACTOR, 2)
    # A procedural label never beats a substantive one.
    substantive = [key for key, value in scores.items() if not TYPES_BY_KEY[key].general and value >= MIN_PRIMARY_SCORE]
    if substantive:
        for key in ("court_procedure_only",):
            if key in scores:
                scores[key] = round(scores[key] * DEMOTE_GENERAL_FACTOR, 2)

    # A PRRA officer who decided an H&C application: the case is about the H&C decision.
    prra_hc = bool(_PRRA_OFFICER_HC_RE.search(intro[:800]))
    if prra_hc:
        scores["humanitarian_compassionate"] = round(scores.get("humanitarian_compassionate", 0.0) + PRRA_OFFICER_HC_BONUS, 2)
        intro_scores["humanitarian_compassionate"] = intro_scores.get("humanitarian_compassionate", 0.0) + PRRA_OFFICER_HC_BONUS
        if "pre_removal_risk_assessment" in scores:
            scores["pre_removal_risk_assessment"] = round(scores["pre_removal_risk_assessment"] * DEMOTE_GENERAL_FACTOR, 2)

    # A motion about the court's own process (intervention, extension, striking or quashing an appeal, costs) is
    # procedural whatever statute the underlying case concerns.
    if _PROCEDURAL_INTRO_RE.search(intro[:PROCEDURAL_INTRO_WINDOW]):
        scores["court_procedure_only"] = round(max(scores.values(), default=0.0) + PROCEDURAL_INTRO_BONUS, 2)
        intro_scores["court_procedure_only"] = scores["court_procedure_only"]

    # A removal order that follows from an upstream finding (residency breach, an inadmissibility ground)
    # is labelled by the upstream finding.
    upstream = [key for key, value in scores.items()
                if (key.startswith("inadmissibility_") or key in {"permanent_resident_status", "removal_deferral_stay", "detention"})
                and value >= MIN_PRIMARY_SCORE]
    if upstream and "removal_admissibility_proceedings" in scores:
        scores["removal_admissibility_proceedings"] = round(scores["removal_admissibility_proceedings"] * 0.6, 2)

    allowed_groups = ALLOWED_GROUPS_BY_PROCEEDING.get(proceeding or "")
    if allowed_groups:
        scores = {key: value for key, value in scores.items()
                  if TYPES_BY_KEY[key].group in allowed_groups or key == "removal_deferral_stay"
                  or (prra_hc and key == "humanitarian_compassionate")}
    min_primary = MIN_PRIMARY_SCORE_KNOWN_FORUM if allowed_groups else MIN_PRIMARY_SCORE

    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    evidence_dicts = lambda key: [asdict(item) for item in evidence.get(key, [])]  # noqa: E731
    if not ranked or ranked[0][1] < min_primary:
        return CaseTypeResult(TAXONOMY_VERSION, STATUS_UNCLEAR, None, None, [], 0.0, dict(ranked[:6]),
                              [key for key, _ in ranked[:3]], proceeding,
                              reason="no case type reached the minimum evidence score")

    top_key, top_score = ranked[0]
    if (court_key in {"FCA", "SCC"} and top_key not in matched_hits and top_score < APPEAL_COURT_CUE_ONLY_MIN_SCORE
            and top_key != "court_procedure_only"):
        # An appeal-court decision labelled from wording alone, with no statute provision behind it, is not safe.
        return CaseTypeResult(TAXONOMY_VERSION, STATUS_UNCLEAR, None, None, [], 0.0, dict(ranked[:6]),
                              [key for key, _ in ranked[:3]], proceeding,
                              reason="only wording, no statute provision, supports the leading case type")
    second_score = ranked[1][1] if len(ranked) > 1 else 0.0
    tie_broken_by_intro = False
    if second_score and top_score < MIN_LEAD_RATIO * second_score:
        # The opening is where the court says what the case is about: accept a close winner only if
        # the opening points clearly at it and not at the runner-up.
        intro_top = intro_scores.get(top_key, 0.0)
        intro_second = intro_scores.get(ranked[1][0], 0.0)
        intro_ranked = sorted(((intro_scores.get(key, 0.0), key) for key, _ in ranked[:4]), reverse=True)
        second_key = ranked[1][0]
        if (intro_top >= SECOND_MAIN_INTRO_SCORE and intro_second >= SECOND_MAIN_INTRO_SCORE
                and top_key in matched_hits and second_key in matched_hits
                and not (second_key in GENERIC_SECOND_TYPES and TYPES_BY_KEY[top_key].group != TYPES_BY_KEY[second_key].group)):
            # Two provisions are both named in the opening with similar weight: two main types, not "unclear".
            return CaseTypeResult(TAXONOMY_VERSION, STATUS_CLASSIFIED, top_key, _primary_detail(matched_hits[top_key]), [second_key],
                                  0.4, dict(ranked[:6]), [], proceeding, evidence=evidence_dicts(top_key),
                                  reason="two case types are both named in the opening",
                                  second_type=second_key, second_detail=_primary_detail(matched_hits[second_key]))
        if intro_ranked[0][1] != top_key or intro_top < 5.0 or intro_top < 2.0 * max(intro_second, 0.01):
            return CaseTypeResult(TAXONOMY_VERSION, STATUS_UNCLEAR, None, None, [], 0.0, dict(ranked[:6]),
                              [key for key, _ in ranked[:3]], proceeding,
                              evidence=evidence_dicts(top_key),
                              reason="two or more case types have similar evidence")
        tie_broken_by_intro = True

    secondary = [key for key, score in ranked[1:4]
                 if score >= max(MIN_SECONDARY_SCORE, SECONDARY_FRACTION * top_score)
                 and not (key == "refugee_claim" and top_key in SPECIFIC_PROTECTION_TYPES)]
    # A second MAIN type: a secondary type that the opening names, or whose evidence nearly matches the primary's.
    # Generic protection vocabulary is never a second main type for a non-protection case, and the second type
    # must rest on a statutory provision, not on wording alone.
    second_type = next((key for key in secondary
                        if key in matched_hits
                        and not (key in GENERIC_SECOND_TYPES and TYPES_BY_KEY[top_key].group != TYPES_BY_KEY[key].group)
                        and (intro_scores.get(key, 0.0) >= SECOND_MAIN_INTRO_SCORE
                             or scores.get(key, 0.0) >= SECOND_MAIN_FRACTION * top_score)), None)
    second_detail = _primary_detail(matched_hits.get(second_type, [])) if second_type else None
    lead = 1.0 - (second_score / top_score) * 0.5 if top_score else 0.0
    confidence = round(min(1.0, top_score / 14.0) * lead, 2)
    if tie_broken_by_intro:
        confidence = min(confidence, 0.4)
    detail = _primary_detail(matched_hits.get(top_key, []))
    issues = issues_by_anchor(reasons) if top_key == "refugee_claim" else []
    return CaseTypeResult(TAXONOMY_VERSION, STATUS_CLASSIFIED, top_key, detail, secondary, confidence,
                          dict(ranked[:6]), [], proceeding, evidence=evidence_dicts(top_key), issues=issues,
                          second_type=second_type, second_detail=second_detail)


def _primary_detail(type_hits: list[ProvisionHit]) -> str | None:
    """Most specific provision path the decision keeps returning to, e.g. ``34(1)(f)``."""
    if not type_hits:
        return None
    counts = Counter(hit.path for hit in type_hits)
    # Prefer the deepest path that appears at least twice, else the most common path.
    repeated = [(path, count) for path, count in counts.items() if count >= 2]
    pool = repeated or list(counts.items())
    pool.sort(key=lambda item: (item[1] * (1 + 0.25 * item[0].count("(")), item[0].count("(")), reverse=True)
    return pool[0][0]
