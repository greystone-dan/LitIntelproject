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
# Matters of other regimes that only mention an immigration body or the Act in passing (the opening names the real subject).
_OTHER_REGIME_RE = re.compile(
    r"Public\s+(?:Service|Sector)\s+Labour\s+Relations|Public\s+Service\s+Staffing\s+Tribunal"
    r"|Access\s+to\s+Information\s+Act|Canadian\s+Human\s+Rights\s+(?:Commission|Tribunal)",
    re.IGNORECASE,
)
_AIR_TRAVEL_RE = re.compile(r"Secure\s+Air\s+Travel\s+Act|Passenger\s+Protect", re.IGNORECASE)
_CITIZENSHIP_TRIAL_STAY_RE = re.compile(r"stay\s+of\s+(?:a|the)\s+trial\s+under\s+section\s+18\s+of\s+the\s+Citizenship\s+Act", re.IGNORECASE)
_CONVERT_TO_ACTION_RE = re.compile(r"(?:convert|treat)\w*\s+(?:the\s+|their\s+)?(?:application\s+for\s+)?judicial\s+review\s+(?:in)?to\s+an\s+action|18\.4\(2\)", re.IGNORECASE)
_CRIMINAL_TITLE_RE = re.compile(r"^(?:R\.|Her Majesty|La Reine|Regina)\s+(?:v\.|c\.)", re.IGNORECASE)
_IMMIGRATION_TITLE_RE = re.compile(r"Citizenship|Immigration|Public Safety|Refugee|Minister of|Solicitor General|Canada Border|Council for", re.IGNORECASE)
CRIMINAL_CASE_MIN_HITS = 25
NON_IMMIGRATION_TITLE_MIN_HITS = 8
_PROCEDURAL_INTRO_RE = re.compile(
    r"(?:motion|application|request)\s+(?:\w+\s+){0,3}?(?:for\s+leave\s+)?to\s+(?:intervene|strike|quash)"
    r"|leave\s+to\s+intervene|for\s+an\s+order\s+striking|(?:motion|request)\s+for\s+an?\s+extension\s+of\s+time|costs\s+(?:against|awarded\s+against)"
    r"|\bRules?\s+(?:369|397|399)\b|dismiss\w*\s+(?:the\s+\w+\s+)?for\s+mootness|\bmoot(?:ness)?\b[^.]{0,40}\bmotion",
    re.IGNORECASE,
)
_VACATE_INTRO_RE = re.compile(r"application\s+(?:\w+\s+){0,4}?to\s+vacate|vacate\s+and\s+nullify|to\s+vacate\s+(?:the\s+)?(?:positive|refugee|Convention)", re.IGNORECASE)
VACATE_INTRO_BONUS = 12.0
_PRRA_OFFICER_HC_RE = re.compile(
    r"(?:pre-removal\s+risk\s+assessment|PRRA)\s+officer[^.]{0,160}?(?:humanitarian\s+and\s+compassionate|H&C)", re.IGNORECASE
)
_PRRA_DECISION_RE = re.compile(
    r"decision[^.]{0,200}?(?:pre-removal\s+risk\s+assessment|PRRA)\b", re.IGNORECASE
)
_IMMIGRATION_PARTY_RE = re.compile(
    r"Citizenship\s+and\s+Immigration|Immigration,\s+Refugees\s+and\s+Citizenship|Immigration\s+and\s+Refugee", re.IGNORECASE
)
_STAY_INTRO_RE = re.compile(
    r"(?:reasons (?:for|on) (?:the |a |my )?(?:stay|motion)|motion (?:for|to) (?:an? )?(?:order )?(?:staying|stay)|"
    r"(?:I|the Court) (?:have |has )?stayed|stay of (?:the |a |his |her |their )?removal|stay (?:the )?(?:execution|enforcement) of|"
    r"order (?:staying|prohibiting)[^.]{0,40}remov)",
    re.IGNORECASE,
)
_REFERRAL_44_RE = re.compile(r"admissibility\s+hearing|(?:subsection|section|s\.)\s?44\b", re.IGNORECASE)
_RAD_OPENING_RE = re.compile(r"Refugee\s+Appeal\s+Division|\bRAD\b", re.IGNORECASE)
_PRRA_NAMED_RE = re.compile(r"pre-removal\s+risk\s+assessment|\bPRRA\b", re.IGNORECASE)

def _is_stay_intro(intro: str) -> bool:
    # The looser stay wording only counts in the first lines; deeper in, a stay motion is just procedural history.
    return bool(_STAY_INTRO_RE.search(intro) or _STAY_LOOSE_RE.search(intro[:800]))


_STAY_LOOSE_RE = re.compile(
    r"(?:interim |temporary )?stay[^.]{0,120}\bremoval\b|application (?:to|for) (?:an? )?stay|irreparable harm", re.IGNORECASE
)
REFERRAL_44_BONUS = 12.0
LEAD_MIN_SCORE = 8.0
LEAD_MIN_RATIO = 2.2
RAD_NO_PRRA_FACTOR = 0.2
STAY_INTRO_BONUS = 12.0
JR_SUBJECT_BONUS = 8.0
_JR_SENTENCE_RE = re.compile(r"[^.]{0,400}?(?:judicial\s+review|set\s+aside|leave\s+to\s+(?:appeal|commence))[^.]{0,400}", re.IGNORECASE)
_JR_SUBJECTS = (
    ("refugee_claim", re.compile(r"Refugee\s+(?:Protection|Appeal)\s+Division|\bRPD\b|\bRAD\b|refugee\s+(?:claim|protection|status)|Convention\s+refugee", re.IGNORECASE)),
    ("humanitarian_compassionate", re.compile(r"humanitarian\s+and\s+compassionate|\bH\s?&\s?C\b", re.IGNORECASE)),
    ("pre_removal_risk_assessment", re.compile(r"pre-removal\s+risk\s+assessment|\bPRRA\b", re.IGNORECASE)),
    ("study_permit", re.compile(r"student\s+visa|study\s+permit", re.IGNORECASE)),
    ("work_permit", re.compile(r"work\s+permit", re.IGNORECASE)),
    ("visitor_visa", re.compile(r"visitor\s+visa|temporary\s+resident\s+visa", re.IGNORECASE)),
)
_ACT_NAME_RE = re.compile(r"Immigration\s+and\s+Refugee\s+Protection\s+(?:Act|Regulations)|\bIRPA\b", re.IGNORECASE)
_DEFER_RE = re.compile(r"\bdefer|\bstay\b|mandamus|relief\s+from", re.IGNORECASE)
_IAD_RE = re.compile(r"Immigration\s+Appeal\s+Division|\bIAD\b", re.IGNORECASE)
_OPENING_RULES = (
    ("court_procedure_only", re.compile(r"\bmotion\b[^.]{0,120}(?:\brules?\b|non-disclosure|set aside the order|expedite|reconsider)|appeal[^.]{0,60}order of (?:the )?prothonotary|set aside the order of this court", re.IGNORECASE)),
    ("removal_deferral_stay", re.compile(r"\bdefer(?:ral)?\b[^.]{0,80}removal|refus\w+ to defer|stay of (?:a |the |an )?(?:removal|deportation|execution)|stay the execution|motion (?:for|to) (?:a )?stay|granted a stay|application for a stay|request(?:ing|s)? a stay", re.IGNORECASE)),
    ("pre_removal_risk_assessment", re.compile(r"risk assessment|\bPRRA\b|minister.s protection|protection of the minister|applications? for protection", re.IGNORECASE)),
    ("permanent_resident_status", re.compile(r"(?:Immigration Appeal Division|\bIAD\b)[^.]{0,300}residency obligation|residency obligation[^.]{0,300}(?:Immigration Appeal Division|\bIAD\b)", re.IGNORECASE)),
    ("family_class_sponsorship", re.compile(r"(?:Immigration Appeal Division|\bIAD\b)[^.]{0,300}(?:visa officer|sponsor|spous|marriage|husband|wife|family class|adopt)|(?:visa officer|sponsor|spous|marriage|husband|wife|family class)[^.]{0,200}(?:Immigration Appeal Division|\bIAD\b)", re.IGNORECASE)),
    ("removal_admissibility_proceedings", re.compile(r"(?:Immigration Appeal Division|\bIAD\b)[^.]{0,300}(?:removal order|deportation order|exclusion order|inadmissib)", re.IGNORECASE)),
    ("humanitarian_compassionate", re.compile(r"humanitarian\s+(?:and|or)\s+compassionate|\bH\s?&\s?C\b|(?:section|subsection|s\.)\s?25(?:\(1\))?\b", re.IGNORECASE)),
    ("study_permit", re.compile(r"study permit|student visa|study in canada|genuine student|permis d.études", re.IGNORECASE)),
    ("work_permit", re.compile(r"work permit|work authori[sz]ation|permis de travail", re.IGNORECASE)),
    ("visitor_visa", re.compile(r"visitor visa|temporary resident visa|visa de visiteur|visa de résident temporaire", re.IGNORECASE)),
    ("economic_immigration", re.compile(r"provincial nominee|express entry|skilled worker|skilled trades|canadian experience class", re.IGNORECASE)),
    ("refugee_claim", re.compile(r"section d.appel des réfugiés|section de la protection des réfugiés|section du statut|demande d.asile|(?:claimed|sought|claiming|made a claim for) (?:refugee )?(?:protection|status)|refugee claim|refugee protection claim|refugee division|refugee (?:protection|appeal) division|(?:panel|member) of the immigration and refugee board|\bRPD\b|\bRAD\b", re.IGNORECASE)),
)
OPENING_SUBJECT_WINDOW = 500


_SUBORDINATE_TO_H_AND_C = {"court_procedure_only", "removal_deferral_stay", "permanent_resident_status", "family_class_sponsorship",
                           "removal_admissibility_proceedings"}


def opening_subject_type(intro: str) -> str | None:
    """The one decision subject the opening paragraphs name, used only to resolve unclear results.

    H&C is the subject only when nothing more specific is named (a deferral or an Immigration Appeal Division
    appeal "on H&C grounds" is about the deferral or the appeal), and a refugee claim only when nothing else is named
    (many other decisions recite a refugee claim as background). Two different subjects name none.
    """
    opening = _ACT_NAME_RE.sub(" ", intro[:OPENING_SUBJECT_WINDOW])
    hits = [key for key, pattern in _OPENING_RULES if pattern.search(opening)]
    if _SUBORDINATE_TO_H_AND_C.intersection(hits):
        hits = [key for key in hits if key != "humanitarian_compassionate"]
    if len(hits) > 1:
        hits = [key for key in hits if key != "refugee_claim"]
    return hits[0] if len(hits) == 1 else None


PRRA_OFFICER_HC_BONUS = 8.0
PRRA_DECISION_BONUS = 8.0
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


def jr_subject_type(intro: str) -> str | None:
    """The one subject named in the opening judicial review sentence, or None when it names none or several."""
    match = _JR_SENTENCE_RE.search(intro[:700])
    if not match or _IAD_RE.search(match.group(0)):
        return None
    sentence = _ACT_NAME_RE.sub(" ", match.group(0))
    subjects = [key for key, pattern in _JR_SUBJECTS if pattern.search(sentence)]
    return subjects[0] if len(subjects) == 1 and not _DEFER_RE.search(sentence) else None


def _classify_text(
    text: str | None,
    *,
    court: str | None = None,
    title: str | None = None,
    docket: str | None = None,
    source_citations: Iterable[str | None] = (),
    jr_bonus: float = 0.0,
) -> CaseTypeResult:
    """Classify one decision from its text."""
    content = text or ""
    if len(content) < MIN_TEXT_CHARS:
        return CaseTypeResult(TAXONOMY_VERSION, STATUS_INSUFFICIENT, None, None, [], 0.0, {}, [], None,
                              reason="decision text too short to classify")

    if not (docket and _DOCKET_IMM_RE.search(docket)):
        # Stored docket missing or truncated: the Federal Court header names it near the top of the text.
        header_docket = _DOCKET_IMM_RE.search(content[:1500])
        docket = header_docket.group(0) if header_docket else docket

    reasons, intro, intro_end = split_regions(content)
    if (court or "").strip().upper() == "FCA" and ((title and _IMMIGRATION_PARTY_RE.search(title)) or PREGATE_RE.search(content)):
        for pattern, key in ((_CITIZENSHIP_TRIAL_STAY_RE, "citizenship_other"), (_CONVERT_TO_ACTION_RE, "court_procedure_only")):
            if pattern.search(content[:4000]):
                return CaseTypeResult(TAXONOMY_VERSION, STATUS_CLASSIFIED, key, None, [], 0.4, {}, [], None,
                                      reason="typed from the motion named in the opening")
    if (court or "").strip().upper() in {"FCA", "SCC"} and (_OTHER_REGIME_RE.search(intro[:800]) or _AIR_TRAVEL_RE.search(content[:6000])) \
            and not _DOCKET_IMM_RE.search(content[:2500]):
        return CaseTypeResult(TAXONOMY_VERSION, STATUS_NOT_IMMIGRATION, None, None, [], 0.0, {}, [], None,
                              reason="the opening names another regime (air travel, public service labour, access to information, human rights)")
    if not PREGATE_RE.search(content) and (court or "").strip().upper() not in {"RPD", "RAD", "IAD", "ID"}:
        if title and _IMMIGRATION_PARTY_RE.search(title):
            return CaseTypeResult(TAXONOMY_VERSION, STATUS_UNCLEAR, None, None, [], 0.0, {}, [], None,
                                  reason="an immigration department is a party but no immigration statute is named in the text")
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
    if _is_stay_intro(intro):
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
    # A judicial review of a PRRA decision is a PRRA case, unless it is a stay motion or the officer decided H&C.
    if (not _is_stay_intro(intro) and not _PRRA_OFFICER_HC_RE.search(intro[:800])
            and _PRRA_DECISION_RE.search(intro[:500])):
        scores["pre_removal_risk_assessment"] = round(scores.get("pre_removal_risk_assessment", 0.0) + PRRA_DECISION_BONUS, 2)
        intro_scores["pre_removal_risk_assessment"] = intro_scores.get("pre_removal_risk_assessment", 0.0) + PRRA_DECISION_BONUS
    # A referral to an admissibility hearing (s. 44) is a removal-proceedings case even when H&C factors were weighed.
    if _REFERRAL_44_RE.search(intro[:600]) and not _is_stay_intro(intro):
        scores["removal_admissibility_proceedings"] = round(scores.get("removal_admissibility_proceedings", 0.0) + REFERRAL_44_BONUS, 2)
        intro_scores["removal_admissibility_proceedings"] = intro_scores.get("removal_admissibility_proceedings", 0.0) + REFERRAL_44_BONUS
    # A review of a Refugee Appeal Division decision that never names a PRRA is not a PRRA case (RAD new-evidence
    # provisions read like the PRRA ones).
    if (_RAD_OPENING_RE.search(intro[:500]) and not _PRRA_NAMED_RE.search(intro[:800])
            and "pre_removal_risk_assessment" in scores):
        scores["pre_removal_risk_assessment"] = round(scores["pre_removal_risk_assessment"] * RAD_NO_PRRA_FACTOR, 2)
    # The Minister's application to vacate a positive refugee decision (s. 109) says so in its opening.
    if _VACATE_INTRO_RE.search(intro[:700]):
        scores["refugee_vacation"] = round(scores.get("refugee_vacation", 0.0) + VACATE_INTRO_BONUS, 2)
        intro_scores["refugee_vacation"] = intro_scores.get("refugee_vacation", 0.0) + VACATE_INTRO_BONUS
    # The opening sentence that names the judicial review says what decision is under review: when it names
    # exactly one subject (refugee claim, H&C, PRRA, study or work permit, visitor visa), that subject leads.
    jr_subject = None
    if jr_bonus:
        jr_subject = jr_subject_type(intro) or opening_subject_type(intro)
    if jr_subject:
        scores[jr_subject] = round(scores.get(jr_subject, 0.0) + jr_bonus, 2)
        intro_scores[jr_subject] = intro_scores.get(jr_subject, 0.0) + jr_bonus
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


_COSTS_INTRO_RE = re.compile(r"bill\s+of\s+costs|assessment\s+of\s+(?:the\s+)?costs|assessment\s+officer|costs\s+pursuant\s+to\s+the\s+judgment", re.IGNORECASE)
_MOOT_OR_QUASH_RE = re.compile(r"\bmoot(?:ness)?\b|(?:to\s+quash|quashing)\s+(?:the\s+|this\s+|an\s+)?appeal|without\s+jurisdiction|summary\s+(?:dismissal|judgment)|\brule\s+22\b", re.IGNORECASE)
_CITIZENSHIP_REVOCATION_RE = re.compile(r"revok\w+\s+(?:the\s+)?(?:appellant'?s?\s+|his\s+|her\s+)?citizenship|citizenship[^.]{0,40}revo", re.IGNORECASE)


def _opening_fallback(text: str, court: str | None, title: str | None) -> CaseTypeResult | None:
    """Type a still-unclear immigration-court decision from its opening alone, or call it not immigration.

    Appeal-court motions, costs assessments and short reasons often name no provision the scorer can use, but the
    opening still says what the matter is. Returns None when the opening does not settle it."""
    if (court or "").strip().upper() != "FCA":
        return None
    _reasons, intro, _end = split_regions(text)
    head = intro[:800]
    party = bool(title and _IMMIGRATION_PARTY_RE.search(title))
    if not party:
        if _CITIZENSHIP_REVOCATION_RE.search(intro[:1500]):
            key = "citizenship_revocation"
            return CaseTypeResult(TAXONOMY_VERSION, STATUS_CLASSIFIED, key, None, [], 0.4, {}, [], None,
                                  reason="typed from the opening of the decision only")
        if not (_IMMIGRATION_VOCAB_RE.search(intro[:1500]) or _ACT_NAME_RE.search(intro[:1500])
                or _DOCKET_IMM_RE.search(text[:2500])
                or re.search(r"citizenship|removal|deport", intro[:1500], re.IGNORECASE)):
            return CaseTypeResult(TAXONOMY_VERSION, STATUS_NOT_IMMIGRATION, None, None, [], 0.0, {}, [], None,
                                  reason="no immigration subject in the opening of an appeal-court decision")
        if _COSTS_INTRO_RE.search(head) or _PROCEDURAL_INTRO_RE.search(head) or _MOOT_OR_QUASH_RE.search(head):
            return CaseTypeResult(TAXONOMY_VERSION, STATUS_CLASSIFIED, "court_procedure_only", None, [], 0.4, {}, [], None,
                                  reason="typed from the opening of the decision only")
        return None
    if _CITIZENSHIP_REVOCATION_RE.search(intro[:1500]):
        key = "citizenship_revocation"
    elif _COSTS_INTRO_RE.search(head):
        key = "court_procedure_only"
    elif _PROCEDURAL_INTRO_RE.search(head) or _MOOT_OR_QUASH_RE.search(head):
        key = "court_procedure_only"
    elif _STAY_INTRO_RE.search(head):
        key = "removal_deferral_stay"
    else:
        key = jr_subject_type(intro) or opening_subject_type(intro)
    if not key:
        return None
    return CaseTypeResult(TAXONOMY_VERSION, STATUS_CLASSIFIED, key, None, [], 0.4, {}, [], None,
                          reason="typed from the opening of the decision only")


def classify_text(text: str | None, **kwargs) -> CaseTypeResult:
    """Classify one decision. A decision that stays unclear is retried once with the subject named in the
    judicial review sentence leading, so the bonus only ever resolves unclear results and never changes a clear one."""
    result = _classify_text(text, **kwargs)
    if result.status == STATUS_UNCLEAR:
        retry = _classify_text(text, jr_bonus=JR_SUBJECT_BONUS, **kwargs)
        if retry.status == STATUS_CLASSIFIED:
            return retry
        fallback = _opening_fallback(text or "", kwargs.get("court"), kwargs.get("title"))
        if fallback is not None:
            return fallback
        ranked = sorted(result.scores.items(), key=lambda item: -item[1])
        if ranked and ranked[0][1] >= LEAD_MIN_SCORE and (len(ranked) < 2 or ranked[0][1] >= LEAD_MIN_RATIO * ranked[1][1]):
            return CaseTypeResult(TAXONOMY_VERSION, STATUS_CLASSIFIED, ranked[0][0], None, [], 0.3, dict(ranked[:6]), [], result.proceeding,
                                  reason="leading case type only; low confidence")
    return result
