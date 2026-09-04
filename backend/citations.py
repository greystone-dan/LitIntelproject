from __future__ import annotations

import hashlib
import os
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime

from sqlalchemy import delete, func, select, text
from sqlalchemy.orm import Session

from .database import A2AJCase, A2AJCaseMap, A2AJCitationEdge, Case, CaseChunk, Citation, CitationMetrics, StatuteReference
from .citation_pipeline import CanLiiApiClient, build_default_pipeline

try:
	from eyecite import get_citations as eyecite_get_citations
except Exception:  # pragma: no cover
	eyecite_get_citations = None

_V2_PIPELINE = None
_CANLII_CLIENT = None
CASE_CITATION_KINDS = {"neutral", "case", "case_short", "case_name"}
STATUTE_REFERENCE_KINDS = {"statute", "instrument"}
GENERIC_STATUTE_NOISE_NAMES = {
	"An Act",
	"Contempt Order",
	"Preliminary Order",
	"Show Cause Order",
	"Standing Order",
}

NEUTRAL_CIT_RE = re.compile(
	r"\b((?:19|20)\d{2})\s+(FC|FCA|SCC|TCC|IRB|RPD|RAD|IAD|ID)\s+(\d{1,5})\b",
	re.IGNORECASE,
)
CANLII_CIT_RE = re.compile(r"\b((?:19|20)\d{2})\s+CanLII\s+(\d{1,9})\s*\(([A-Za-z. ]{2,20})\)", re.IGNORECASE)
CASE_CIT_RE = re.compile(
	r"\b([A-Z][A-Za-z'’\-&,()\[\]. ]{1,90}?\s+v\.?\s+[A-Z][A-Za-z'’\-&,()\[\]. ]{1,90}?),?\s+((?:19|20)\d{2})\s+([A-Z]{2,})\s+(\d{1,6})\b"
)
REPORTED_CASE_CIT_RE = re.compile(
	r"\b([A-Z][A-Za-z'’\-&,()\[\]. ]{1,120}?\s+v\.?\s+[A-Z][A-Za-z'’\-&,()\[\]. ]{1,120}?),?\s+"
	r"(\[(?:19|20)\d{2}\]\s+\d+\s+[A-Z][A-Z. ]{1,20}\s+\d+)\b",
	re.IGNORECASE,
)
CASE_REPORTER_NEUTRAL_RE = re.compile(
	r"\b([A-Z][A-Za-z'’\-&,()\[\]. ]{1,90}?\s+v\.?\s+[A-Z][A-Za-z'’\-&,()\[\]. ]{1,90}?),\s+\[(?:19|20)\d{2}\][^,\n]{1,50},\s+((?:19|20)\d{2})\s+([A-Z]{2,})\s+(\d{1,6})\b",
	re.IGNORECASE,
)
STANDALONE_CASE_NAME_RE = re.compile(
	r"\b([A-Z][A-Za-z'’\-&,()\[\]. ]{1,120}?\s+v\.?\s+[A-Z][A-Za-z'’\-&,()\[\]. ]{1,120}?)(?=[,.;)\]]|\s|$)",
	re.IGNORECASE,
)
STATUTE_CIT_RE = re.compile(r"\b(IRPA|IRPR)\s*,?\s*(?:s\.?|section)\s*\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*", re.IGNORECASE)
LONG_STATUTE_CIT_RE = re.compile(
	r"\b(?:"
	r"Immigration and Refugee Protection Act(?:,\s*S\.C\.\s*\d{4},\s*c\.\s*[A-Z0-9.-]+(?:\s*\([^)]*\))?)?"
	r"|Immigration and Refugee Protection Regulations(?:,\s*SOR/\d{4}-\d+)?"
	r"|Canadian Charter of Rights and Freedoms(?:,?\s*Part I of the Constitution Act, 1982)?"
	r"|Criminal Code(?:,\s*R\.S\.C\.\s*\d{4},\s*c\.\s*C-\d+)?"
	r")\b(?:,?\s*(?:s\.|section)\s*\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)?",
	re.IGNORECASE,
)
SHORT_CHARTER_SECTION_RE = re.compile(
	r"\bCharter\b,?\s*(?:s\.|section)\s*\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*",
	re.IGNORECASE,
)
SECTION_OF_STATUTE_RE = re.compile(
	r"\b(?:s\.|section)\s*(\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)\s+of\s+(?:the\s+)?(IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations|Canadian Charter of Rights and Freedoms|Charter|Criminal Code)\b",
	re.IGNORECASE,
)
STATUTE_MULTI_SECTION_PREFIX_RE = re.compile(
	r"\b(IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations|Canadian Charter of Rights and Freedoms|Charter|Criminal Code)\s*,?\s*(?:ss?\.?|sections?)\s*((?:\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)(?:(?:(?:\s*,\s*(?:and|or)?\s*)|(?:\s+(?:and|or|to)\s+)|(?:\s*[-–]\s*))(?:\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*))+)",
	re.IGNORECASE,
)
IRPA_IRPR_NESTED_PROVISION_LIST_OF_STATUTE_RE = re.compile(
	r"\b(?:paragraphs?|paras?\.?|subparagraphs?|subparas?\.?|subsections?|subsecs?\.?)\s*"
	r"((?:\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))+)(?:(?:\s*,\s*(?:and|or)?\s*|\s+(?:and|or|to)\s+|\s*[-–]\s*)"
	r"(?:\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*|\(\s*[A-Za-z0-9]+\s*\)))+)\s+of\s+(?:the\s+)?"
	r"(IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations)\b",
	re.IGNORECASE,
)
GENERIC_SECTION_OF_STATUTE_RE = re.compile(
	r"\b(?:s\.|section)\s*(\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)\s+of\s+(?:the\s+)?((?:(?!The\b|This\b|That\b)(?-i:[A-Z])[A-Za-z'’\-]+(?:\s+(?:(?-i:[A-Z])[A-Za-z'’\-]+|of|and|the|for|de|du|des|la|le|les)){0,12}\s+(?-i:Act|Code|Regulations?|Rules|Order))(?:,\s*(?:(?:S\.?C\.?|R\.?S\.?C\.?)\s*,?\s*\d{4},\s*c\.?\s*[A-Z0-9.-]+(?:\s*\([^)]*\))?|SOR/\d{4}-\d+|S\.?I\.?/\d{2,4}-\d+))?)\b",
	re.IGNORECASE,
)
GENERIC_STATUTE_CIT_RE = re.compile(
	r"\b((?:(?!The\b|This\b|That\b)(?-i:[A-Z])[A-Za-z'’\-]+(?:\s+(?:(?-i:[A-Z])[A-Za-z'’\-]+|of|and|the|for|de|du|des|la|le|les)){0,12}\s+(?-i:Act|Code|Regulations?|Rules|Order))(?:,\s*(?:(?:S\.?C\.?|R\.?S\.?C\.?)\s*,?\s*\d{4},\s*c\.?\s*[A-Z0-9.-]+(?:\s*\([^)]*\))?|SOR/\d{4}-\d+|S\.?I\.?/\d{2,4}-\d+))?(?:,?\s*(?:s\.|section)\s*\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)?)",
	re.IGNORECASE,
)
FRENCH_PROVISION_OF_STATUTE_RE = re.compile(
	r"\b(article|articles|art\.|paragraphe|paragraphes|alinéa|alinéas)\s+"
	r"(\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)\s+"
	r"(?:de|du|des|de\s+la|de\s+l['’])\s+"
	r"((?:Loi|Code|Règlement|Règles|Charte|Constitution|Ordonnances)[^,.;\n\[]{1,120}?)"
	r"(?=,?\s*(?:LC|L[CR]C|DORS|SOR|\[|[.;]))",
	re.IGNORECASE,
)
SECTION_OF_STATUTE_DIRECT_RE = re.compile(
	r"\b(?:s\.|section)\s*(\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)\s+(IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations|Canadian Charter of Rights and Freedoms|Charter|Criminal Code)\b",
	re.IGNORECASE,
)
IRPA_IRPR_NESTED_PROVISION_OF_STATUTE_RE = re.compile(
	r"\b(?:paragraphs?|paras?\.?|subparagraphs?|subparas?\.?|subsections?|subsecs?\.?)\s*(\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\)){1,4})\s+of\s+(?:the\s+)?(IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations)\b",
	re.IGNORECASE,
)
IRPA_IRPR_NESTED_PROVISION_PREFIX_RE = re.compile(
	r"\b(IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations)\s*,?\s+(?:paragraphs?|paras?\.?|subparagraphs?|subparas?\.?|subsections?|subsecs?\.?)\s*(\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\)){1,4})(?=$|\s|[.,;:)\]])",
	re.IGNORECASE,
)
IRPA_IRPR_BARE_NESTED_PROVISION_OF_STATUTE_RE = re.compile(
	r"\b(\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\)){1,4})\s+of\s+(?:the\s+)?(IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations)\b",
	re.IGNORECASE,
)
SECTIONS_OF_STATUTE_RE = re.compile(
	r"\b(?:sections?|ss?\.)\s+((?:\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)(?:(?:(?:\s*,\s*(?:and|or)?\s*)|(?:\s+(?:and|or|to)\s+)|(?:\s*[-–]\s*))(?:\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*))+?)\s+of\s+(?:the\s+)?(IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations|Canadian Charter of Rights and Freedoms|Charter|Criminal Code)\b",
	re.IGNORECASE,
)
REFUGEE_CONVENTION_ARTICLE_RE = re.compile(
	r"\b(?:art\.|article)\s*(1[EF])(?:\s*\(\s*([A-Fa-f])\s*\)|\s*([A-Fa-f]))?(?!\w)",
	re.IGNORECASE,
)
CONVENTION_ARTICLE_LIST_RE = re.compile(
	r"\barticles?\s+(\d{1,3}(?:\s*(?:,|and|or|to|-|–)\s*\d{1,3})+)\s+of\s+(?:the\s+)?(Vienna Convention(?: on the Law of Treaties)?|Convention Relating to the Status of Refugees|Refugee Convention)\b",
	re.IGNORECASE,
)
REPORTER_PINPOINT_RE = re.compile(
	r"\[(19|20)\d{2}\]\s*\d+\s*S\.?C\.?R\.?\s*\d+(?:,\s*at\s*(?:p{1,2}\.\s*\d+(?:\s*[-–]\s*\d+)?|para(?:s)?\.\s*\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*))?",
	re.IGNORECASE,
)
INSTRUMENT_CIT_RE = re.compile(
	r"\b(?:"
	r"(?:(?:art\.|article)\s*\d+[A-Z]{0,2}(?:\s*\(\s*[A-Za-z0-9]+\s*\))*(?:\s+of\s+(?:the\s+)?)?)?"
	r"(?:Convention Relating to the Status of Refugees|Refugee Convention|Vienna Convention on the Law of Treaties|Vienna Convention)"
	r"(?:\s*,?\s*Can\.\s*T\.S\.\s*\d{4}\s*No\.\s*\d+)?"
	r"(?:\s*\([^)]*\))?"
	r"(?:,?\s*(?:art\.|article)\s*\d+[A-Z]{0,2}(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)?"
	r"|Can\.\s*T\.S\.\s*\d{4}\s*No\.\s*\d+"
	r")",
	re.IGNORECASE,
)
NAMED_INTERNATIONAL_INSTRUMENT_RE = re.compile(
	r"\b(?:"
	r"Protocol relating to the Status of Refugees(?:,\s*\d+\s+U\.?N\.?T\.?S\.?\s+\d+)?"
	r"|Constitution of the International Refugee Organization(?:,\s*\d+\s+U\.?N\.?T\.?S\.?\s+\d+(?:,\s*Ann\.\s*I,\s*Part\s+II)?)?"
	r"|Statute of the Office of the United Nations High Commissioner for Refugees(?:,\s*G\.?A\.?\s+Res\.?\s*\d+\([IVXLCDM]+\)\s*\(\d{4}\)(?:,\s*s\.\s*\d+)?)?"
	r"|Declaration of States Parties to the 1951 Convention and(?:\s+or|/)\s+its 1967 Protocol Relating to the Status of Refugees(?:,\s*HCR/[A-Z0-9/]+)?"
	r"|Charter of the United Nations"
	r"|Universal Declaration of Human Rights"
	r")\b",
	re.IGNORECASE,
)
STANDALONE_PROVISION_RE = re.compile(
	r"\b(articles?|arts?\.|sections?|subsections?|paragraphs?|subparagraphs?|ss?\.)\s*"
	r"(\d{1,3}(?:\.\d+)?[A-Z]{0,2}(?:\s*\(\s*[A-Za-z0-9]+\s*\))*"
	r"(?:(?:\s*,\s*(?:and|or)?\s*|\s+(?:and|or|to)\s+|\s*[-–]\s*)"
	r"\d{1,3}(?:\.\d+)?[A-Z]{0,2}(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)*)",
	re.IGNORECASE,
)
_SHORT_FORM_PARA_RE = re.compile(r"\b(?:at\s+)?para(?:s)?\.?\s+\d", re.IGNORECASE)
_PINPOINT_FRAGMENT_RE = re.compile(
	r"(?:at\s+)?(?:(?:para(?:s|graph(?:s)?)?\.?|paragraph(?:s)?)\s+\d+(?:\s*(?:[-–]|to)\s*\d+)?(?:\s*(?:,|;|and|or)\s*\d+(?:\s*(?:[-–]|to)\s*\d+)?)*|(?:pp?\.)\s*\d+(?:\s*[-–]\s*\d+)?)",
	re.IGNORECASE,
)
_TRAILING_PINPOINT_RE = re.compile(
	rf"^\s*[)\],;:\-]*\s*(?:\[\s*)?({_PINPOINT_FRAGMENT_RE.pattern})(?:\s*\])?\b",
	re.IGNORECASE,
)
_TRAILING_REPORTER_RE = re.compile(
	r"^\s*,?\s*(\[(?:19|20)\d{2}\]\s*\d+\s*[A-Z][A-Z. ]{0,14}\s*\d+|\((?:19|20)\d{2}\)\s*,?\s*\d+\s*[A-Z][A-Z. ]{0,14}\s*\d+)\b",
	re.IGNORECASE,
)
SULLIVAN_TREATISE_RE = re.compile(
	r"\b(?:cf\s+)?Ruth\s+Sullivan,\s+Sullivan on the Construction of Statutes,\s+\d+(?:st|nd|rd|th)\s+ed\s*\([^)]*\d{4}\)",
	re.IGNORECASE,
)
GENERIC_SHORT_AUTHORITY_RE = re.compile(
	r"\b([A-Z][A-Za-z'\-.]+(?:\s+[A-Z][A-Za-z'\-.]+){0,4}),\s+at\s+para(?:s)?\.?\s+\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*",
	re.IGNORECASE,
)
REFUGEE_CONVENTION_ARTICLE_33_RE = re.compile(
	r"\b(?:art\.|article)\s*(33(?:\s*\(\s*\d+\s*\))?)(?!\w)",
	re.IGNORECASE,
)
CASE_PARTIES_FRAGMENT_RE = re.compile(
	r"[A-Z][A-Za-z'’\-&,()\[\]. ]{0,90}?\s+v\.?\s+[A-Z][A-Za-z'’\-&,()\[\]. ]{0,90}?$"
)
CASE_CHAIN_FRAGMENT_RE = re.compile(
	r"([A-Z][A-Za-z'’\-&,()\[\]. ]{1,140}?\s+v\.?\s+[A-Z][A-Za-z'’\-&,()\[\]. ]{1,140}?)\s*,?\s*$",
	re.IGNORECASE,
)
_CASE_NOISE_START_TOKENS = {
	"as",
	"act",
	"board",
	"commissioner",
	"court",
	"in",
	"inc",
	"ltd",
	"limited",
	"corp",
	"corporation",
	"company",
	"co",
	"according",
	"citing",
	"justice",
	"judge",
	"minister",
	"quoting",
	"see",
	"the",
}
_ALLOWED_CASE_REPORTERS = {
	"FC",
	"FCA",
	"FCT",
	"SCC",
	"SCR",
	"DLR",
	"OR",
	"BCLR",
	"ALR",
	"ABCA",
	"ABQB",
	"ABKB",
	"ONCA",
	"ONSC",
	"QCCA",
	"QCCS",
	"BCCA",
	"BCSC",
	"NSCA",
	"NSSC",
	"MBCA",
	"MBKB",
	"NBCA",
	"NBBR",
	"PECA",
	"PESC",
	"SKCA",
	"SKKB",
	"YKSC",
	"YKCA",
	"NWTSC",
	"NUCJ",
	"TCC",
	"IRB",
	"RPD",
	"RAD",
	"IAD",
	"ID",
}
_CASE_NAME_NEUTRAL_MAX_GAP = 160
_BARE_CASE_ALIAS_NOISE = {
	"applicant",
	"appeal",
	"appellant",
	"board",
	"canada",
	"commission",
	"code",
	"criminal",
	"criminal code",
	"court",
	"decision",
	"department",
	"affairs",
	"general",
	"immigration",
	"justice",
	"law",
	"management",
	"minister",
	"reasons",
	"respondent",
	"communications",
}


@dataclass(frozen=True)
class RawCitationMatch:
	kind: str
	citation_text: str
	normalized_citation: str
	offset_start: int
	offset_end: int
	pinpoint: str | None = None
	anchor_citation_text: str | None = None
	anchor_offset_start: int | None = None
	anchor_offset_end: int | None = None


@dataclass(frozen=True)
class LegislationCitation:
	instrument_key: str
	pinpoint: str
	legislation_url: str | None = None


LEGISLATION_REGISTRY: dict[str, dict[str, object]] = {
	"canada.irpa": {
		"aliases": ("IRPA", "Immigration and Refugee Protection Act"),
		"url": "https://laws-lois.justice.gc.ca/eng/acts/I-2.5/section-{section}.html",
	},
	"canada.irpr": {
		"aliases": ("IRPR", "Immigration and Refugee Protection Regulations"),
		"url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/section-{section}.html",
	},
}


def parse_legislation_citation(value: str | None) -> LegislationCitation | None:
	text = _normalize_whitespace(value or "")
	for key, definition in LEGISLATION_REGISTRY.items():
		aliases = definition["aliases"]
		if not any(re.search(rf"\b{re.escape(alias)}\b", text, re.IGNORECASE) for alias in aliases):
			continue
		match = re.search(r"\b(?:s|ss|sections?|paragraphs?|subsections?)\.?\s*(?=\d)([^,;]+?)(?=\s+of\s+|\s*$|[.;])", text, re.IGNORECASE)
		if match is None:
			match = re.search(r"\bsections?\s*([^,;]+)", text, re.IGNORECASE)
		if match is None:
			return None
		pinpoint = re.sub(r"\s+", "", match.group(1)).strip(".")
		section = re.match(r"\d{1,3}(?:\.\d+)?[A-Za-z]?", pinpoint)
		url_template = definition.get("url")
		url = url_template.format(section=section.group(0)) if section and isinstance(url_template, str) else None
		return LegislationCitation(key, pinpoint, url)
	return None


def is_self_case_name_match(case_title: str | None, match: RawCitationMatch) -> bool:
	"""Identify a bare short-form alias that belongs to the source case title."""
	if match.kind not in {"case_short", "case_name"}:
		return False
	alias = re.split(r"\s*,\s*(?:at\s+)?para", match.citation_text, maxsplit=1, flags=re.IGNORECASE)[0]
	alias = _normalize_whitespace(alias)
	if not re.fullmatch(r"[A-Za-z][A-Za-z'’-]{3,}", alias):
		return False
	parties = re.split(
		r"\s+(?:v\.?|c\.?|vs\.?)\s+",
		_normalize_whitespace(case_title or ""),
		maxsplit=1,
		flags=re.IGNORECASE,
	)[0]
	party_words = {
		word.strip("'’-\u2019").casefold()
		for word in re.findall(r"[A-Za-z][A-Za-z'’-]+", parties)
	}
	return alias.casefold() in party_words


def is_self_case_citation(case: Case | None, match: RawCitationMatch) -> bool:
	"""Identify an exact citation for the decision currently being processed."""
	if case is None or not match.normalized_citation:
		return False
	key = re.sub(r"[^a-z0-9]+", " ", match.normalized_citation.casefold()).strip()
	return any(
		key == re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()
		for value in (getattr(case, "citation", None), getattr(case, "secondary_citation", None))
		if value
	)


@dataclass(frozen=True)
class _CaseAnchor:
	alias: str
	citation_text: str
	normalized_citation: str
	case_start: int
	case_end: int


def _normalize_whitespace(value: str) -> str:
	return " ".join(value.split()).strip()


def _normalize_pinpoint_phrase(value: str) -> str:
	text = _normalize_whitespace(value).replace("–", "-")
	text = re.sub(r"^[,.;:\s]+", "", text)
	if not text:
		return ""
	body = re.sub(r"^at\s+", "", text, flags=re.IGNORECASE)
	body = _normalize_whitespace(body)
	lower = body.lower()
	if lower.startswith("pp."):
		label = "pp."
	elif lower.startswith("p."):
		label = "p."
	elif lower.startswith("paragraphs") or lower.startswith("paras"):
		label = "paras."
	elif lower.startswith("paragraph") or lower.startswith("para"):
		label = "para."
	else:
		label = "para."
	numbers = re.sub(r"^(?:paragraphs?|paras?\.?|para\.?|pp?\.)+\s*", "", body, flags=re.IGNORECASE)
	numbers = _normalize_whitespace(numbers)
	if not numbers:
		return ""
	return f"at {label} {numbers}"


def _extract_pinpoint_phrase(value: str) -> str | None:
	match = _PINPOINT_FRAGMENT_RE.search(value)
	if match is None:
		return None
	pinpoint = _normalize_pinpoint_phrase(match.group(0))
	return pinpoint or None


def _append_pinpoint_to_normalized(normalized_citation: str, pinpoint: str | None) -> str:
	if not pinpoint:
		return normalized_citation
	normalized_lower = normalized_citation.lower()
	if pinpoint.lower() in normalized_lower:
		return normalized_citation
	separator = ", " if not normalized_citation.rstrip().endswith(",") else " "
	return f"{normalized_citation}{separator}{pinpoint}"


def _extend_case_with_trailing_pinpoint(
	content: str,
	start: int,
	end: int,
	normalized_citation: str,
) -> tuple[int, str, str]:
	window = content[end : min(len(content), end + 120)]
	match = _TRAILING_PINPOINT_RE.match(window)
	if match is None:
		citation_text = content[start:end]
		return end, citation_text, normalized_citation
	new_end = end + match.end()
	citation_text = content[start:new_end].rstrip()
	pinpoint = _normalize_pinpoint_phrase(match.group(1))
	return new_end, citation_text, _append_pinpoint_to_normalized(normalized_citation, pinpoint)


def _extend_case_with_trailing_reporter(
	content: str,
	start: int,
	end: int,
	normalized_citation: str,
) -> tuple[int, str, str]:
	window = content[end : min(len(content), end + 180)]
	match = _TRAILING_REPORTER_RE.match(window)
	if match is None:
		return _extend_case_with_trailing_pinpoint(content, start, end, normalized_citation)
	reporter = _normalize_whitespace(match.group(1)).replace(" .", ".")
	normalized_with_reporter = f"{normalized_citation}, {reporter}"
	return _extend_case_with_trailing_pinpoint(
		content,
		start,
		end + match.end(),
		normalized_with_reporter,
	)


def _extend_case_layer_row(content: str, row: RawCitationMatch) -> RawCitationMatch:
	if row.kind not in CASE_CITATION_KINDS:
		return row
	if row.kind in {"case", "case_name"}:
		new_end, citation_text, normalized = _extend_case_with_trailing_reporter(
			content,
			row.offset_start,
			row.offset_end,
			row.normalized_citation,
		)
	else:
		new_end, citation_text, normalized = _extend_case_with_trailing_pinpoint(
			content,
			row.offset_start,
			row.offset_end,
			row.normalized_citation,
		)
	if new_end == row.offset_end and citation_text == row.citation_text and normalized == row.normalized_citation:
		return row
	return _raw_match(row.kind, citation_text, normalized, row.offset_start, new_end)


def _normalize_neutral_parts(year: str, court: str, number: str) -> str:
	return f"{year} {court.upper()} {int(number)}"


def _normalize_case_parties(parties: str) -> str:
	def strip_narrative_prefix(value: str) -> str:
		text = _normalize_whitespace(value)
		match = re.search(
			r"\b(?:in|see|cf\.?|contra|citing|quoting|according to)\s+([A-Z][A-Za-z'’\-&,()\[\]. ]{1,140}?\s+v\.?\s+[A-Z][A-Za-z'’\-&,()\[\]. ]{1,140})$",
			text,
			flags=re.IGNORECASE,
		)
		if match:
			candidate = _normalize_whitespace(match.group(1))
			if _is_plausible_case_parties(candidate):
				return candidate
		return text

	def trim_side(side: str) -> str:
		side = _normalize_whitespace(side)
		if "(" in side:
			prefix, _sep, suffix = side.rpartition("(")
			if suffix and re.search(r"\bv\.?\b", suffix, flags=re.IGNORECASE):
				side = _normalize_whitespace(suffix)
			elif suffix and re.fullmatch(r"[A-Z][A-Za-z'\-.]{2,}", suffix.strip()):
				side = _normalize_whitespace(suffix)
			elif suffix and re.search(r"\b[a-z]{3,}\b", prefix):
				side = _normalize_whitespace(suffix)
		side = re.sub(
			r"^(?:(?:See|In|Cf\.?|Contra|Particularly|Applying|Citing|According to|See also)\s+|Applied\s+in\s+)",
			"",
			side,
			flags=re.IGNORECASE,
		)
		if "(" in side:
			return side
		tokens = side.split(" ")
		if len(tokens) <= 1:
			return side
		connectors = {"and", "of", "the", "for", "to", "on", "in"}
		kept: list[str] = []
		for token in reversed(tokens):
			stripped = token.strip(",;:")
			if not stripped:
				continue
			if kept and stripped.lower() in connectors:
				kept.append(stripped)
				continue
			if re.match(r"^[A-Z][A-Za-z'.()\-]*$", stripped):
				kept.append(stripped)
				continue
			if not kept:
				continue
			break
		if kept:
			return " ".join(reversed(kept))
		return side

	normalized = strip_narrative_prefix(parties)
	parts = re.split(r"\bv\s*\.?\s+", normalized, maxsplit=1, flags=re.IGNORECASE)
	if len(parts) == 2:
		left = trim_side(parts[0])
		right = _normalize_whitespace(parts[1])
		normalized = f"{left} v. {right}"
	else:
		normalized = trim_side(normalized)
	return normalized


def _is_plausible_case_parties(parties: str) -> bool:
	sides = re.split(r"\bv\.?\b", parties, maxsplit=1, flags=re.IGNORECASE)
	if len(sides) != 2:
		return False

	allowed_lower_tokens = {
		"and",
		"or",
		"of",
		"the",
		"for",
		"to",
		"on",
		"in",
		"de",
		"du",
		"des",
		"la",
		"le",
		"les",
		"et",
		"al",
	}

	for side in sides:
		if "(" in side:
			prefix, _sep, suffix = side.rpartition("(")
			if suffix and re.search(r"\bv\.?\b", suffix, flags=re.IGNORECASE):
				side = suffix
			elif suffix and re.fullmatch(r"[A-Z][A-Za-z'\-.]{2,}", suffix.strip()):
				side = suffix
			elif suffix and re.search(r"\b[a-z]{3,}\b", prefix):
				side = suffix
		cleaned = _normalize_whitespace(re.sub(r"[()\[\],;:]", " ", side))
		if not cleaned:
			return False
		tokens = [token for token in cleaned.split(" ") if token]
		if not tokens:
			return False
		if len(tokens) > 18:
			return False

		has_party_token = False
		for token in tokens:
			alpha = re.sub(r"[^A-Za-z]", "", token)
			if not alpha:
				continue
			if alpha.islower() and alpha.lower() not in allowed_lower_tokens:
				return False
			if alpha[0].isupper() or alpha.isupper():
				has_party_token = True
		if not has_party_token:
			return False

	return True


def _raw_match(
	kind: str,
	citation_text: str,
	normalized_citation: str,
	start: int,
	end: int,
	anchor_citation_text: str | None = None,
	anchor_offset_start: int | None = None,
	anchor_offset_end: int | None = None,
) -> RawCitationMatch:
	return RawCitationMatch(
		kind=kind,
		citation_text=citation_text,
		normalized_citation=normalized_citation,
		offset_start=start,
		offset_end=end,
		pinpoint=_extract_pinpoint_phrase(citation_text) if kind in CASE_CITATION_KINDS else None,
		anchor_citation_text=anchor_citation_text,
		anchor_offset_start=anchor_offset_start,
		anchor_offset_end=anchor_offset_end,
	)


def _canonical_statute_name(name: str) -> str:
	lowered = _normalize_whitespace(name).lower()
	if lowered == "irpa":
		return "IRPA"
	if lowered == "irpr":
		return "IRPR"
	if lowered in {"charter", "canadian charter of rights and freedoms"}:
		return "Canadian Charter of Rights and Freedoms"
	if lowered == "immigration and refugee protection act":
		return "Immigration and Refugee Protection Act"
	if lowered == "immigration and refugee protection regulations":
		return "Immigration and Refugee Protection Regulations"
	if lowered == "criminal code":
		return "Criminal Code"
	return _normalize_whitespace(name)


def _full_statute_citation_name(name: str) -> str:
	lowered = _normalize_whitespace(name).lower()
	if lowered in {"irpa", "immigration and refugee protection act"}:
		return "Immigration and Refugee Protection Act, S.C. 2001, c. 27"
	if lowered in {"irpr", "immigration and refugee protection regulations"}:
		return "Immigration and Refugee Protection Regulations, SOR/2002-227"
	if lowered in {"charter", "canadian charter of rights and freedoms"}:
		return "Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982"
	if lowered == "criminal code":
		return "Criminal Code, R.S.C. 1985, c. C-46"
	return _normalize_whitespace(name)


def _normalize_long_statute_citation(text: str) -> str:
	normalized = _normalize_whitespace(text)
	normalized = re.sub(r"\bsection\b", "s.", normalized, flags=re.IGNORECASE)
	normalized = re.sub(
		r"\bImmigration and Refugee Protection Act(?:,?\s*S\.?C\.?\s*\d{4},?\s*c\.?\s*[A-Z0-9.-]+(?:\s*\([^)]*\))?)?\b",
		"Immigration and Refugee Protection Act, S.C. 2001, c. 27",
		normalized,
		flags=re.IGNORECASE,
	)
	normalized = re.sub(
		r"\bImmigration and Refugee Protection Regulations(?:,?\s*SOR/?\d{4}-\d+)?\b",
		"Immigration and Refugee Protection Regulations, SOR/2002-227",
		normalized,
		flags=re.IGNORECASE,
	)
	normalized = re.sub(
		r"\bCanadian Charter of Rights and Freedoms(?:,?\s*Part I of the Constitution Act, 1982)?\b",
		"Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982",
		normalized,
		flags=re.IGNORECASE,
	)
	normalized = re.sub(
		r"\bCriminal Code(?:,?\s*R\.?S\.?C\.?\s*1985,?\s*c\.?\s*C-46)?\b",
		"Criminal Code, R.S.C. 1985, c. C-46",
		normalized,
		flags=re.IGNORECASE,
	)
	return normalized


def _normalize_section_list(section_list: str) -> str:
	normalized = _normalize_whitespace(section_list).replace("–", "-")
	normalized = re.sub(r",\s*(?:and|or)\s+", ", ", normalized, flags=re.IGNORECASE)
	normalized = re.sub(r"\b(?:and|or)\b", ",", normalized, flags=re.IGNORECASE)
	normalized = re.sub(r"\s*,\s*", ", ", normalized)
	normalized = re.sub(r"\s*\bto\b\s*", " to ", normalized, flags=re.IGNORECASE)
	normalized = re.sub(r"\s*-\s*", "-", normalized)
	normalized = re.sub(r"\s+", " ", normalized).strip(" ,")
	return normalized


def _normalize_nested_provision(value: str) -> str:
	normalized = _normalize_whitespace(value)
	normalized = re.sub(r"\s*\(\s*", "(", normalized)
	normalized = re.sub(r"\s*\)\s*", ")", normalized)
	return normalized


def _normalize_refugee_convention_article(base: str, paren_letter: str | None, suffix_letter: str | None) -> str:
	article = base.upper()
	letter = (paren_letter or suffix_letter or "").strip().lower()
	if letter:
		return f"art. {article}({letter}) of Refugee Convention"
	return f"art. {article} of Refugee Convention"


def _normalize_refugee_convention_article_33(value: str) -> str:
	normalized = re.sub(r"\s+", "", _normalize_whitespace(value))
	return f"art. {normalized} of Refugee Convention"


def _normalize_convention_article_list(article_list: str, convention_name: str) -> str:
	norm_list = _normalize_whitespace(article_list).replace("–", "-")
	norm_list = re.sub(r"\b(?:and|or)\b", ",", norm_list, flags=re.IGNORECASE)
	norm_list = re.sub(r"\s*,\s*", ", ", norm_list)
	norm_list = re.sub(r"\s*\bto\b\s*", " to ", norm_list, flags=re.IGNORECASE)
	norm_list = re.sub(r"\s*-\s*", "-", norm_list)
	norm_list = re.sub(r"\s+", " ", norm_list).strip(" ,")
	name = _normalize_whitespace(convention_name)
	if re.search(r"refugee convention|convention relating to the status of refugees", name, re.IGNORECASE):
		name = "Refugee Convention"
	elif re.search(r"\bvienna convention(?: on the law of treaties)?\b", name, re.IGNORECASE):
		name = "Vienna Convention on the Law of Treaties"
	return f"arts. {norm_list} of {name}"


def _normalize_generic_statute_citation(text: str) -> str:
	normalized = _normalize_whitespace(text)
	normalized = re.sub(r"^(?:and|or|of)\s+(?:the\s+)?", "", normalized, flags=re.IGNORECASE)
	normalized = re.sub(r"\b(R\.?S\.?C\.?|S\.?C\.?)\s*,\s*(\d{4})\b", r"\1 \2", normalized, flags=re.IGNORECASE)
	normalized = re.sub(r"\bsection\b", "s.", normalized, flags=re.IGNORECASE)
	return normalized


def _extract_generic_short_authority_candidates(content: str) -> list[RawCitationMatch]:
	rows: list[RawCitationMatch] = []
	for match in GENERIC_SHORT_AUTHORITY_RE.finditer(content):
		normalized = _normalize_whitespace(match.group(0)).replace("–", "-")
		normalized = re.sub(r"^(?:and|or)\s+", "", normalized, flags=re.IGNORECASE)
		rows.append(_raw_match("secondary", match.group(0), normalized, match.start(), match.end()))
	return rows


def normalize_neutral_citation(match: re.Match[str]) -> str:
	year, court, number = match.groups()
	return _normalize_neutral_parts(year, court, number)


def normalize_case_citation(match: re.Match[str]) -> str:
	parties, year, reporter, number = match.groups()
	return f"{_normalize_case_parties(parties)}, {year} {reporter.strip().upper()} {int(number)}".strip()


def _normalize_case_citation_parts(parties: str, year: str, reporter: str, number: str) -> str:
	return f"{_normalize_case_parties(parties)}, {year} {reporter.strip().upper()} {int(number)}".strip()


def _select_case_parties_span(parties: str) -> tuple[int, str]:
	best_start = 0
	best_value = parties
	best_score = -10**9

	for idx, ch in enumerate(parties):
		if not ch.isupper():
			continue
		candidate_match = CASE_PARTIES_FRAGMENT_RE.match(parties, idx)
		if candidate_match is None:
			continue
		candidate = candidate_match.group(0).strip()
		if not _is_plausible_case_parties(candidate):
			continue
		parts = re.split(r"\bv\.?\b", candidate, maxsplit=1, flags=re.IGNORECASE)
		if len(parts) != 2:
			continue
		left = parts[0]
		prefix = parties[:idx]
		start_token_match = re.match(r"[A-Z][A-Za-z'’\-.]*", candidate)
		start_token = start_token_match.group(0).lower() if start_token_match else ""
		paren_balance = left.count("(") - left.count(")")
		score = 0
		if idx == 0:
			score += 3
		if start_token in _CASE_NOISE_START_TOKENS:
			score -= 6
		if "[" in left or "]" in left:
			score -= 5
		if paren_balance != 0:
			score -= 4 * abs(paren_balance)
		if left.strip().startswith((")", "]", ",", ";", ":")):
			score -= 6
		if re.search(r"\b(?:and|or)\s+[A-Z][A-Za-z'’\-.]+\s*$", left):
			score -= 3
		if prefix.strip():
			if re.search(r"[\[\]]", prefix):
				score += 2
			if re.search(r"\b(?:Justice|Judge|Court|Commissioner|Act|citing|described\s+in|according\s+to|hardship|found)\b", prefix, flags=re.IGNORECASE):
				score += 2
			if re.search(r"\b[a-z]{3,}\b", prefix):
				score += 1

		if score > best_score or (score == best_score and len(candidate) > len(best_value)):
			best_score = score
			best_start = idx
			best_value = candidate

	return best_start, best_value


def _extract_case_chain_candidates(content: str) -> list[tuple[int, int, RawCitationMatch]]:
	"""Extract case cites in chained lists by anchoring around neutral citations."""
	candidates: list[tuple[int, int, RawCitationMatch]] = []
	for neutral_match in NEUTRAL_CIT_RE.finditer(content):
		year, court, number = neutral_match.groups()
		window_start = max(0, neutral_match.start() - 240)
		prelude = content[window_start : neutral_match.start()]
		fragment_match = None
		for maybe in CASE_CHAIN_FRAGMENT_RE.finditer(prelude):
			fragment_match = maybe
		if fragment_match is None:
			continue

		parties_raw = fragment_match.group(1)
		parties_start, selected_parties = _select_case_parties_span(parties_raw)
		if not _is_plausible_case_parties(selected_parties):
			continue
		if not _is_allowed_case_reporter(court):
			continue

		global_parties_start = window_start + fragment_match.start(1) + parties_start
		global_end = neutral_match.end()
		normalized = _normalize_case_citation_parts(selected_parties, year, court, number)
		global_end, citation_text, normalized = _extend_case_with_trailing_reporter(
			content,
			global_parties_start,
			global_end,
			normalized,
		)
		candidates.append(
			(
				global_parties_start,
				global_end,
				_raw_match(
					"case",
					citation_text,
					normalized,
					global_parties_start,
					global_end,
				),
			)
		)

	return candidates


def _candidate_rank(start: int, end: int, citation: RawCitationMatch) -> tuple[int, int]:
	"""Higher rank wins when spans overlap."""
	text = citation.citation_text.strip()
	norm = citation.normalized_citation
	score = 0
	if citation.kind == "case":
		score += 120
		if " v. " in norm:
			score += 40
		if re.search(r"\b(?:19|20)\d{2}\s+[A-Z]{2,}\s+\d{1,6}\b", norm):
			score += 20
	elif citation.kind == "case_name":
		score += 85
		if " v. " in norm:
			score += 20
	elif citation.kind == "neutral":
		score += 90
	elif citation.kind == "statute":
		score += 80
	elif citation.kind == "case_short":
		score += 70
		if " v. " in norm:
			score += 15
	else:
		score += 60

	if re.match(r"^(?:As|In|See|The|Act|Court|Justice|Judge|Commissioner)\b", text, flags=re.IGNORECASE):
		score -= 30
	if citation.kind == "case" and (
		re.search(r"\]\s+(?:and|or)\s+[^,;]{0,80}\bv\.?\s", text, flags=re.IGNORECASE)
		or re.match(r"^(?:and|or)\s+", norm, flags=re.IGNORECASE)
	):
		score -= 40
	if text.startswith((")", "]", ",", ";", ":")):
		score -= 20
	if text.count("(") != text.count(")"):
		score -= 12

	# Prefer tighter spans once quality score is tied.
	return score, -(end - start)


def _is_allowed_case_reporter(reporter: str) -> bool:
	reporter_clean = reporter.strip().upper().rstrip(".")
	if reporter_clean in _ALLOWED_CASE_REPORTERS:
		return True
	if len(reporter_clean) >= 2 and reporter_clean.endswith(("CA", "SC")):
		return True
	return False


def _clean_case_side(value: str) -> str:
	cleaned = re.sub(r"\([^)]*\)", "", value)
	cleaned = re.sub(r"[^A-Za-z'\-\s]", " ", cleaned)
	return _normalize_whitespace(cleaned)


def _extract_short_alias(parties: str) -> str | None:
	aliases = _extract_short_aliases(parties)
	return aliases[0] if aliases else None


def _extract_short_aliases(parties: str) -> list[str]:
	def aliases_from_side(side: str) -> list[str]:
		cleaned = _clean_case_side(side)
		if not cleaned:
			return []
		tokens = [token for token in cleaned.split(" ") if len(token) >= 3]
		if not tokens:
			return []
		lead_noise = {"see", "in", "re", "cf", "contra"}
		while tokens and tokens[0].lower() in lead_noise:
			tokens = tokens[1:]
		if not tokens:
			return []
		stopwords = {
			"appellant",
			"the",
			"and",
			"minister",
			"canada",
			"attorney",
			"general",
			"citizenship",
			"immigration",
			"inc",
			"ltd",
			"limited",
			"corporation",
			"corp",
			"company",
			"co",
		}
		filtered = [token for token in tokens if token.lower() not in stopwords]
		if not filtered:
			return []
		is_company = bool(
			re.search(
				r"\b(?:inc|ltd|limited|corp|corporation|company|co)\b",
				cleaned,
				flags=re.IGNORECASE,
			)
		)
		candidates: list[str] = [filtered[-1]]
		if is_company and filtered[0].lower() != filtered[-1].lower():
			candidates.append(filtered[0])
		if 2 <= len(filtered) <= 4:
			candidates.append(" ".join(filtered))
		# Preserve order and uniqueness.
		deduped: list[str] = []
		seen: set[str] = set()
		for value in candidates:
			key = value.lower()
			if key in seen:
				continue
			seen.add(key)
			deduped.append(value)
		return deduped

	sides = re.split(r"\bv\.?\b", parties, maxsplit=1, flags=re.IGNORECASE)
	aliases: list[str] = []
	for side in sides[:2]:
		aliases.extend(aliases_from_side(side))

	# Preserve order and uniqueness.
	deduped: list[str] = []
	seen: set[str] = set()
	for alias in aliases:
		key = alias.lower()
		if key in seen:
			continue
		seen.add(key)
		deduped.append(alias)
	return deduped


def _extract_short_form_case_candidates(content: str, base_matches: list[RawCitationMatch]) -> list[RawCitationMatch]:
	anchors: list[_CaseAnchor] = []
	ordered = sorted(base_matches, key=lambda item: (item.offset_start, item.offset_end))

	def _emit_alias_anchors(
		aliases: list[str],
		normalized_case: str,
		case_start: int,
		case_end: int,
		trailing_anchor_end: int,
	) -> None:
		# Include bracket aliases declared near the full citation, e.g. [Vavilov].
		trailing_window = content[trailing_anchor_end : min(len(content), trailing_anchor_end + 96)]
		for bracket_alias in re.findall(r"^\s*\[\s*([A-Za-z][A-Za-z .\-']{1,60})\s*\]", trailing_window):
			alias_clean = _normalize_whitespace(bracket_alias)
			if alias_clean:
				aliases.append(alias_clean)

		seen_alias: set[str] = set()
		for alias in aliases:
			alias = _normalize_whitespace(alias)
			if len(alias) < 3:
				continue
			key = alias.lower()
			if key in seen_alias:
				continue
			seen_alias.add(key)
			anchors.append(
				_CaseAnchor(
					alias=alias,
					citation_text=content[case_start:case_end],
					normalized_citation=normalized_case,
					case_start=case_start,
					case_end=case_end,
				)
			)

	for idx, match in enumerate(ordered):
		if match.kind == "case":
			embedded = CASE_CIT_RE.search(match.normalized_citation)
			if embedded is None:
				continue
			normalized_case = normalize_case_citation(embedded)
			aliases = _extract_short_aliases(embedded.group(1))
			_emit_alias_anchors(
				aliases=aliases,
				normalized_case=normalized_case,
				case_start=match.offset_start,
				case_end=match.offset_end,
				trailing_anchor_end=match.offset_end,
			)
			continue

		if match.kind != "case_name":
			continue

		parties = re.sub(
			r"^(?:and|or)\s+",
			"",
			_normalize_whitespace(match.normalized_citation),
			flags=re.IGNORECASE,
		)
		if not _is_plausible_case_parties(parties):
			continue
		aliases = _extract_short_aliases(parties)

		candidate_neutral: RawCitationMatch | None = None
		for next_row in ordered[idx + 1 : idx + 4]:
			if next_row.kind != "neutral":
				continue
			gap = next_row.offset_start - match.offset_end
			if 0 <= gap <= _CASE_NAME_NEUTRAL_MAX_GAP:
				candidate_neutral = next_row
				break

		normalized_case = f"{parties}, {candidate_neutral.normalized_citation}" if candidate_neutral else parties
		case_end = candidate_neutral.offset_end if candidate_neutral else match.offset_end
		_emit_alias_anchors(
			aliases=aliases,
			normalized_case=normalized_case,
			case_start=match.offset_start,
			case_end=case_end,
			trailing_anchor_end=case_end,
		)

	if not anchors:
		return []

	alias_to_anchors: dict[str, list[_CaseAnchor]] = defaultdict(list)
	for anchor in anchors:
		alias_to_anchors[anchor.alias.lower()].append(anchor)
	for alias_key in alias_to_anchors:
		alias_to_anchors[alias_key].sort(key=lambda item: item.case_end)

	def nearest_anchor(alias: str, at_position: int) -> _CaseAnchor | None:
		rows = alias_to_anchors.get(alias.lower()) or []
		if not rows:
			return None
		prior = [row for row in rows if row.case_end <= at_position]
		if prior:
			return prior[-1]
		return rows[0]

	def expand_parenthetical(start: int, end: int) -> tuple[int, int]:
		left = content.rfind("(", max(0, start - 24), start)
		if left < 0:
			return start, end
		prefix = _normalize_whitespace(content[left + 1:start]).lower()
		if prefix not in {
			"",
			"cf.",
			"see",
			"also see",
			"see also",
			"citing",
			"quoted in",
			"quoting",
			"e.g.",
			"e.g.,",
			"see, e.g.,",
		}:
			return start, end
		right = content.find(")", end, min(len(content), end + 160))
		if right < 0:
			return start, end
		tail = content[end:right]
		if ";" in tail or re.search(
			r"\b[A-Z][A-Za-z'’.-]{3,}\s+(?:at\s+)?para(?:s|graphs?)?\.?\s+\d",
			tail,
			re.IGNORECASE,
		):
			return start, end
		return left, right + 1

	existing_spans = [
		(item.offset_start, item.offset_end, item.kind)
		for item in base_matches
	]
	short_matches: list[RawCitationMatch] = []
	seen: set[tuple[int, int, str]] = set()
	for anchor in anchors:
		para_index = r"\d+(?:\s*(?:[-–]|to)\s*\d+)?"
		para_list = rf"{para_index}(?:\s*(?:,|;|and|or)\s*{para_index})*"
		pattern = re.compile(
			rf"\b{re.escape(anchor.alias)}\b(?:,?\s+above)?\s*,?\s+(?:at\s+)?(?:para(?:s|graph(?:s)?)?\.?|pp?\.)\s+{para_list}\b",
			re.IGNORECASE,
		)
		for alias_match in pattern.finditer(content):
			start = alias_match.start()
			end = alias_match.end()
			best_anchor = nearest_anchor(anchor.alias, start)
			if best_anchor is None or best_anchor.normalized_citation != anchor.normalized_citation:
				continue
			if start <= anchor.case_end and end >= anchor.case_start:
				continue
			start, end = expand_parenthetical(start, end)
			if any(
				kind != "secondary" and not (end <= span_start or start >= span_end)
				for span_start, span_end, kind in existing_spans
			):
				continue
			key = (start, end, anchor.normalized_citation)
			if key in seen:
				continue
			seen.add(key)
			citation_text = content[start:end]
			short_matches.append(
				_raw_match(
					"case_short",
					citation_text,
					_append_pinpoint_to_normalized(anchor.normalized_citation, _extract_pinpoint_phrase(citation_text)),
					start,
					end,
					anchor_citation_text=best_anchor.citation_text,
					anchor_offset_start=best_anchor.case_start,
					anchor_offset_end=best_anchor.case_end,
				)
			)

	para_index = r"\d+(?:\s*(?:[-–]|to)\s*\d+)?"
	para_list = rf"{para_index}(?:\s*(?:,|;|and|or)\s*{para_index})*"
	generic_pattern = re.compile(
		rf"\b(?:(?:In|See|Cf\.?|Contra|Citing|Quoting|According to)\s+)?([A-Z][A-Za-z'\-.]+(?:\s+(?:and\s+)?[A-Z][A-Za-z'\-.]+){{0,3}})\b,?\s+(?:at\s+)?(?:para(?:s|graph(?:s)?)?\.?|pp?\.)\s+{para_list}\b",
		re.IGNORECASE,
	)
	for generic_match in generic_pattern.finditer(content):
		alias = _normalize_whitespace(generic_match.group(1))
		best_anchor = nearest_anchor(alias, generic_match.start(1))
		if best_anchor is None:
			continue
		normalized = best_anchor.normalized_citation
		start = generic_match.start(1)
		end = generic_match.end()
		start, end = expand_parenthetical(start, end)
		if any(
			kind != "secondary" and not (end <= span_start or start >= span_end)
			for span_start, span_end, kind in existing_spans
		):
			continue
		key = (start, end, normalized)
		if key in seen:
			continue
		seen.add(key)
		citation_text = content[start:end]
		short_matches.append(
			_raw_match(
				"case_short",
				citation_text,
				_append_pinpoint_to_normalized(normalized, _extract_pinpoint_phrase(citation_text)),
				start,
				end,
				anchor_citation_text=best_anchor.citation_text,
				anchor_offset_start=best_anchor.case_start,
				anchor_offset_end=best_anchor.case_end,
			)
		)

	for alias_key, alias_anchors in sorted(
		alias_to_anchors.items(),
		key=lambda item: (-len(item[0]), item[0]),
	):
		alias = alias_anchors[0].alias
		if len(alias) < 4 or alias_key in _BARE_CASE_ALIAS_NOISE:
			continue
		pattern = re.compile(rf"(?<![\w'’-]){re.escape(alias)}(?![\w'’-])", re.IGNORECASE)
		for alias_match in pattern.finditer(content):
			start, end = alias_match.span()
			if any(
				kind != "secondary" and not (end <= span_start or start >= span_end)
				for span_start, span_end, kind in existing_spans
			):
				continue
			best_anchor = nearest_anchor(alias, start)
			if best_anchor is None:
				continue
			key = (start, end, best_anchor.normalized_citation)
			if key in seen:
				continue
			seen.add(key)
			end, citation_text, normalized_with_pinpoint = _extend_case_with_trailing_pinpoint(
				content,
				start,
				end,
				best_anchor.normalized_citation,
			)
			short_matches.append(
				_raw_match(
					"case_short",
					citation_text,
					normalized_with_pinpoint,
					start,
					end,
					anchor_citation_text=best_anchor.citation_text,
					anchor_offset_start=best_anchor.case_start,
					anchor_offset_end=best_anchor.case_end,
				)
			)

	return sorted(
		short_matches,
		key=lambda match: (-(match.offset_end - match.offset_start), match.offset_start),
	)


def _promote_case_name_neutral_pairs(content: str, rows: list[RawCitationMatch]) -> list[RawCitationMatch]:
	"""Promote adjacent case_name + neutral rows into a full case citation span."""
	ordered = sorted(rows, key=lambda item: (item.offset_start, item.offset_end))
	promoted: list[RawCitationMatch] = []
	for idx, match in enumerate(ordered):
		if match.kind != "case_name":
			continue

		candidate_neutral: RawCitationMatch | None = None
		for next_row in ordered[idx + 1 : idx + 4]:
			if next_row.kind != "neutral":
				continue
			gap = next_row.offset_start - match.offset_end
			if 0 <= gap <= _CASE_NAME_NEUTRAL_MAX_GAP:
				candidate_neutral = next_row
				break
		if candidate_neutral is None:
			continue

		between = content[match.offset_start : candidate_neutral.offset_start]
		parties_match = None
		for maybe in re.finditer(
			r"([A-Z][A-Za-z'’\-&,()\[\]. ]{1,160}?\s+v\.?\s+[A-Z][A-Za-z'’\-&,()\[\]. ]{1,160}?)(?=,?\s*$)",
			between,
			re.IGNORECASE,
		):
			parties_match = maybe
		if parties_match is None:
			continue

		parties = _normalize_case_parties(parties_match.group(1))
		if not _is_plausible_case_parties(parties):
			continue

		case_start = match.offset_start + parties_match.start(1)
		case_end = candidate_neutral.offset_end
		normalized = f"{parties}, {candidate_neutral.normalized_citation}"
		case_end, citation_text, normalized = _extend_case_with_trailing_reporter(
			content,
			case_start,
			case_end,
			normalized,
		)
		promoted.append(
			_raw_match("case", citation_text, normalized, case_start, case_end)
		)

	return promoted


def _extract_regex_candidates(content: str) -> list[tuple[int, int, RawCitationMatch]]:
	candidates: list[tuple[int, int, RawCitationMatch]] = []

	for match in NEUTRAL_CIT_RE.finditer(content):
		normalized = normalize_neutral_citation(match)
		citation_end, citation_text, normalized = _extend_case_with_trailing_pinpoint(
			content,
			match.start(),
			match.end(),
			normalized,
		)
		candidates.append(
			(
				match.start(),
				citation_end,
				_raw_match("neutral", citation_text, normalized, match.start(), citation_end),
			)
		)

	for match in CANLII_CIT_RE.finditer(content):
		year, number, court = match.groups()
		normalized = f"{year} CanLII {int(number)} ({_normalize_whitespace(court)})"
		citation_end, citation_text, normalized = _extend_case_with_trailing_pinpoint(
			content,
			match.start(),
			match.end(),
			normalized,
		)
		candidates.append(
			(
				match.start(),
				citation_end,
				_raw_match("neutral", citation_text, normalized, match.start(), citation_end),
			)
		)

	for match in CASE_CIT_RE.finditer(content):
		parties_start, selected_parties = _select_case_parties_span(match.group(1))
		if not _is_plausible_case_parties(selected_parties):
			continue
		reporter = match.group(3)
		if not _is_allowed_case_reporter(reporter):
			continue
		citation_start = match.start(1) + parties_start
		normalized = _normalize_case_citation_parts(selected_parties, match.group(2), reporter, match.group(4))
		citation_end, citation_text, normalized = _extend_case_with_trailing_reporter(
			content,
			citation_start,
			match.end(),
			normalized,
		)
		candidates.append(
			(
				citation_start,
				citation_end,
				_raw_match("case", citation_text, normalized, citation_start, citation_end),
			)
		)

	for match in REPORTED_CASE_CIT_RE.finditer(content):
		parties_start, selected_parties = _select_case_parties_span(match.group(1))
		if not _is_plausible_case_parties(selected_parties):
			continue
		citation_start = match.start(1) + parties_start
		reported = _normalize_whitespace(match.group(2)).replace(" .", ".")
		normalized = f"{_normalize_case_parties(selected_parties)}, {reported}"
		citation_end, citation_text, normalized = _extend_case_with_trailing_reporter(
			content,
			citation_start,
			match.end(),
			normalized,
		)
		candidates.append(
			(
				citation_start,
				citation_end,
				_raw_match("case", citation_text, normalized, citation_start, citation_end),
			)
		)

	for match in CASE_REPORTER_NEUTRAL_RE.finditer(content):
		parties_start, selected_parties = _select_case_parties_span(match.group(1))
		if not _is_plausible_case_parties(selected_parties):
			continue
		reporter = match.group(3)
		if not _is_allowed_case_reporter(reporter):
			continue
		citation_start = match.start(1) + parties_start
		normalized = _normalize_case_citation_parts(selected_parties, match.group(2), reporter, match.group(4))
		citation_end, citation_text, normalized = _extend_case_with_trailing_reporter(
			content,
			citation_start,
			match.end(),
			normalized,
		)
		candidates.append(
			(
				citation_start,
				citation_end,
				_raw_match("case", citation_text, normalized, citation_start, citation_end),
			)
		)

	for match in STANDALONE_CASE_NAME_RE.finditer(content):
		parties_start, selected_parties = _select_case_parties_span(match.group(1))
		if not _is_plausible_case_parties(selected_parties):
			continue
		citation_start = match.start(1) + parties_start
		normalized = _normalize_case_parties(selected_parties)
		citation_end, citation_text, normalized = _extend_case_with_trailing_reporter(
			content,
			citation_start,
			match.end(1),
			normalized,
		)
		candidates.append(
			(
				citation_start,
				citation_end,
				_raw_match("case_name", citation_text, normalized, citation_start, citation_end),
			)
		)

	for match in STATUTE_CIT_RE.finditer(content):
		normalized = _normalize_whitespace(match.group(0))
		normalized = re.sub(r"\bsection\b", "s.", normalized, flags=re.IGNORECASE)
		normalized = re.sub(r"\b(irpa|irpr)\b,?", lambda m: _full_statute_citation_name(m.group(0).rstrip(",")), normalized, flags=re.IGNORECASE)
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in LONG_STATUTE_CIT_RE.finditer(content):
		normalized = _normalize_long_statute_citation(match.group(0))
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in SHORT_CHARTER_SECTION_RE.finditer(content):
		normalized = _normalize_whitespace(match.group(0))
		normalized = re.sub(
			r"\bcharter\b",
			"Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982",
			normalized,
			flags=re.IGNORECASE,
		)
		normalized = re.sub(r"\bsection\b", "s.", normalized, flags=re.IGNORECASE)
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in SECTION_OF_STATUTE_RE.finditer(content):
		section, statute_name = match.groups()
		normalized = f"{_full_statute_citation_name(statute_name)} s. {section}"
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in STATUTE_MULTI_SECTION_PREFIX_RE.finditer(content):
		statute_name, section_list = match.groups()
		normalized = f"{_full_statute_citation_name(statute_name)} ss. {_normalize_section_list(section_list)}"
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in SECTIONS_OF_STATUTE_RE.finditer(content):
		section_list, statute_name = match.groups()
		normalized = f"{_full_statute_citation_name(statute_name)} ss. {_normalize_section_list(section_list)}"
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in SECTION_OF_STATUTE_DIRECT_RE.finditer(content):
		section, statute_name = match.groups()
		normalized = f"{_full_statute_citation_name(statute_name)} s. {section}"
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in IRPA_IRPR_NESTED_PROVISION_OF_STATUTE_RE.finditer(content):
		section, statute_name = match.groups()
		normalized = f"{_full_statute_citation_name(statute_name)} s. {_normalize_nested_provision(section)}"
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in IRPA_IRPR_NESTED_PROVISION_LIST_OF_STATUTE_RE.finditer(content):
		section_list, statute_name = match.groups()
		normalized = f"{_full_statute_citation_name(statute_name)} ss. {_normalize_section_list(section_list)}"
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in IRPA_IRPR_NESTED_PROVISION_PREFIX_RE.finditer(content):
		statute_name, section = match.groups()
		normalized = f"{_full_statute_citation_name(statute_name)} s. {_normalize_nested_provision(section)}"
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in IRPA_IRPR_BARE_NESTED_PROVISION_OF_STATUTE_RE.finditer(content):
		section, statute_name = match.groups()
		normalized = f"{_full_statute_citation_name(statute_name)} s. {_normalize_nested_provision(section)}"
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in GENERIC_SECTION_OF_STATUTE_RE.finditer(content):
		section, statute_name = match.groups()
		normalized = _normalize_generic_statute_citation(f"{_normalize_whitespace(statute_name)} s. {section}")
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in FRENCH_PROVISION_OF_STATUTE_RE.finditer(content):
		prefix, section, statute_name = match.groups()
		normalized = _normalize_whitespace(f"{statute_name} {prefix} {section}")
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in GENERIC_STATUTE_CIT_RE.finditer(content):
		normalized = _normalize_generic_statute_citation(match.group(0))
		if normalized in GENERIC_STATUTE_NOISE_NAMES:
			continue
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("statute", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in NAMED_INTERNATIONAL_INSTRUMENT_RE.finditer(content):
		normalized = _normalize_whitespace(match.group(0))
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("instrument", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in INSTRUMENT_CIT_RE.finditer(content):
		normalized = _normalize_whitespace(match.group(0))
		normalized = re.sub(r"\barticle\b", "art.", normalized, flags=re.IGNORECASE)
		normalized = re.sub(
			r"\bart\.\s*(\d+)([A-Z])([A-Z])\b",
			lambda m: f"art. {m.group(1)}{m.group(2)}({m.group(3).lower()})",
			normalized,
			flags=re.IGNORECASE,
		)
		normalized = re.sub(r"\(([A-Z])\)", lambda m: f"({m.group(1).lower()})", normalized)
		normalized = re.sub(
			r"\bart\.\s*(\d+[A-Z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)\s+of\s+(?:the\s+)?",
			r"art. \1 of ",
			normalized,
			flags=re.IGNORECASE,
		)
		normalized = re.sub(r"\bCan\.\s*T\.S\.\s*", "Can. T.S. ", normalized, flags=re.IGNORECASE)
		normalized = re.sub(r"\s+No\.\s*", " No. ", normalized, flags=re.IGNORECASE)
		normalized = re.sub(
			r"\bconvention relating to the status of refugees\b",
			"Convention Relating to the Status of Refugees",
			normalized,
			flags=re.IGNORECASE,
		)
		normalized = re.sub(r"\brefugee convention\b", "Refugee Convention", normalized, flags=re.IGNORECASE)
		normalized = re.sub(
			r"\bvienna convention on the law of treaties\b",
			"Vienna Convention on the Law of Treaties",
			normalized,
			flags=re.IGNORECASE,
		)
		normalized = re.sub(
			r"\bvienna convention\b(?!\s+on the law of treaties)",
			"Vienna Convention on the Law of Treaties",
			normalized,
			flags=re.IGNORECASE,
		)
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("instrument", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in REFUGEE_CONVENTION_ARTICLE_RE.finditer(content):
		normalized = _normalize_refugee_convention_article(match.group(1), match.group(2), match.group(3))
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("instrument", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in REFUGEE_CONVENTION_ARTICLE_33_RE.finditer(content):
		normalized = _normalize_refugee_convention_article_33(match.group(1))
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("instrument", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in CONVENTION_ARTICLE_LIST_RE.finditer(content):
		normalized = _normalize_convention_article_list(match.group(1), match.group(2))
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("instrument", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in REPORTER_PINPOINT_RE.finditer(content):
		normalized = _normalize_whitespace(match.group(0)).replace("–", "-")
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("secondary", match.group(0), normalized, match.start(), match.end()),
			)
		)

	for match in SULLIVAN_TREATISE_RE.finditer(content):
		normalized = _normalize_whitespace(match.group(0))
		candidates.append(
			(
				match.start(),
				match.end(),
				_raw_match("secondary", match.group(0), normalized, match.start(), match.end()),
			)
		)

	return candidates


def _anchored_authority_name(citation: RawCitationMatch) -> str | None:
	normalized = citation.normalized_citation
	if citation.kind == "instrument":
		if "Vienna Convention on the Law of Treaties" in normalized:
			return "Vienna Convention on the Law of Treaties"
		if "Refugee Convention" in normalized or "Convention Relating to the Status of Refugees" in normalized:
			return "Refugee Convention"
		return None
	if citation.kind != "statute":
		return None
	return re.split(r"\s+(?:s|ss)\.\s+", normalized, maxsplit=1, flags=re.IGNORECASE)[0].strip()


def _extract_anchored_provision_candidates(
	content: str,
	anchors: list[RawCitationMatch],
) -> list[RawCitationMatch]:
	rows: list[RawCitationMatch] = []
	context_anchors = list(anchors)
	for match in re.finditer(r"\b(IRPA|IRPR|Criminal Code)\b", content, re.IGNORECASE):
		instrument = _full_statute_citation_name(match.group(1))
		context_anchors.append(_raw_match("statute", match.group(0), instrument, match.start(), match.end()))
	for match in STANDALONE_PROVISION_RE.finditer(content):
		start, end = match.span()
		if any(not (end <= anchor.offset_start or start >= anchor.offset_end) for anchor in anchors):
			continue

		prefix = match.group(1).lower()
		if "para" in prefix and "(" not in match.group(2):
			continue
		kind = "instrument" if prefix.startswith("art") else "statute"
		eligible = [
			anchor
			for anchor in context_anchors
			if anchor.kind == kind
			and anchor.offset_end <= start
			and start - anchor.offset_end <= 1500
			and _anchored_authority_name(anchor)
		]
		if not eligible:
			continue
		sentence_start = max(content.rfind(".", 0, start), content.rfind("!", 0, start), content.rfind("?", 0, start)) + 1
		sentence_end_candidates = [position for mark in (".", "!", "?") if (position := content.find(mark, end)) >= 0]
		sentence_end = min(sentence_end_candidates, default=len(content))
		following_authority = re.search(r"\bof\s+(?:the\s+)?(IRPA|IRPR|Criminal Code)\b", content[end : min(len(content), end + 180)], re.IGNORECASE)
		if following_authority:
			authority_start = end + following_authority.start(1)
			anchor = _raw_match(
				"statute",
				following_authority.group(1),
				_full_statute_citation_name(following_authority.group(1)),
				authority_start,
				authority_start + len(following_authority.group(1)),
			)
		else:
			sentence_anchors = [
				anchor
				for anchor in context_anchors
				if sentence_start <= anchor.offset_start < sentence_end
				and not (end <= anchor.offset_start or start >= anchor.offset_end)
				and _anchored_authority_name(anchor)
			]
			anchor = min(sentence_anchors, key=lambda item: abs(item.offset_start - start)) if sentence_anchors else max(eligible, key=lambda item: item.offset_end)
		authority = _anchored_authority_name(anchor)
		if not authority:
			continue

		provisions = _normalize_section_list(match.group(2))
		plural = prefix.endswith("s") or prefix.startswith("arts") or prefix.startswith("ss")
		if prefix.startswith("art"):
			label = "arts." if plural else "art."
		elif prefix.startswith("para"):
			label = "paras." if plural else "para."
		elif prefix.startswith("subpara"):
			label = "subparas." if plural else "subpara."
		else:
			label = "ss." if plural else "s."
		normalized = f"{label} {provisions} of {authority}" if kind == "instrument" else f"{authority} {label} {provisions}"
		rows.append(_raw_match(kind, match.group(0), normalized, start, end))

	return rows


def _extract_eyecite_candidates(content: str) -> list[tuple[int, int, RawCitationMatch]]:
	if eyecite_get_citations is None:
		return []

	candidates: list[tuple[int, int, RawCitationMatch]] = []
	for citation in eyecite_get_citations(content):
		start = getattr(citation, "span_start", None)
		end = getattr(citation, "span_end", None)
		if not isinstance(start, int) or not isinstance(end, int):
			maybe_span = getattr(citation, "span", None)
			if callable(maybe_span):
				result = maybe_span()
				if isinstance(result, tuple) and len(result) == 2:
					start, end = result
		if not isinstance(start, int) or not isinstance(end, int) or start < 0 or end <= start:
			continue

		matched = getattr(citation, "matched_text", None)
		if callable(matched):
			matched = matched()
		if not isinstance(matched, str) or not matched:
			matched = content[start:end]

		corrected = getattr(citation, "corrected_citation", None)
		if callable(corrected):
			corrected = corrected()
		normalized = _normalize_whitespace(corrected or matched)
		if not normalized:
			continue

		kind = "case"
		if NEUTRAL_CIT_RE.search(normalized):
			kind = "neutral"
		elif "canlii" in normalized.lower():
			kind = "neutral"
		elif re.search(r"\bIRPA\b|\bIRPR\b", normalized, flags=re.IGNORECASE):
			kind = "statute"
		elif kind == "case":
			embedded = CASE_CIT_RE.search(normalized) or CASE_CIT_RE.search(matched)
			if embedded is None:
				continue
			if not _is_allowed_case_reporter(embedded.group(3)):
				continue
			parties_start, selected_parties = _select_case_parties_span(embedded.group(1))
			if not _is_plausible_case_parties(selected_parties):
				continue
			normalized = _normalize_case_citation_parts(selected_parties, embedded.group(2), embedded.group(3), embedded.group(4))

		candidates.append((start, end, _raw_match(kind, matched, normalized, start, end)))

	return candidates


def _citation_pipeline_v2_enabled() -> bool:
	value = (os.getenv("CASELIBRARY_CITATION_PIPELINE") or "v2").strip().lower()
	return value in {"v2", "next", "pipeline"}


def _extract_raw_citation_matches_v2(content: str) -> list[RawCitationMatch]:
	global _V2_PIPELINE
	if _V2_PIPELINE is None:
		_V2_PIPELINE = build_default_pipeline()

	rows = _V2_PIPELINE.extract(content)
	return [
		_raw_match(
			kind=row.kind,
			citation_text=row.citation_text,
			normalized_citation=row.normalized_citation,
			start=row.offset_start,
			end=row.offset_end,
		)
		for row in rows
	]


def _select_best_non_overlapping(candidates: list[RawCitationMatch]) -> list[RawCitationMatch]:
	"""Keep best-ranked citations when spans overlap."""
	selected: list[RawCitationMatch] = []
	occupied: list[tuple[int, int]] = []
	for citation in sorted(
		candidates,
		key=lambda item: (
			-_candidate_rank(item.offset_start, item.offset_end, item)[0],
			_candidate_rank(item.offset_start, item.offset_end, item)[1],
			item.offset_start,
		),
	):
		start, end = citation.offset_start, citation.offset_end
		if any(not (end <= occupied_start or start >= occupied_end) for occupied_start, occupied_end in occupied):
			continue
		occupied.append((start, end))
		selected.append(citation)

	selected.sort(key=lambda item: (item.offset_start, item.offset_end))
	return selected


def extract_raw_citation_matches_v2(text: str | None) -> list[RawCitationMatch]:
	content = text or ""
	if not content.strip():
		return []
	v2_rows = [
		_extend_case_layer_row(content, row)
		for row in _extract_raw_citation_matches_v2(content)
		if row.kind != "case_name"
	]
	v2_rows.extend(
		citation
		for _start, _end, citation in _extract_regex_candidates(content)
		if citation.kind in CASE_CITATION_KINDS | STATUTE_REFERENCE_KINDS
	)
	v2_rows.extend(_promote_case_name_neutral_pairs(content, v2_rows))
	v2_rows = _select_best_non_overlapping(v2_rows)
	if not v2_rows:
		return []

	occupied = [(row.offset_start, row.offset_end) for row in v2_rows]
	short_rows = _extract_short_form_case_candidates(content, v2_rows)
	for row in short_rows:
		overlaps = [
			existing
			for existing in v2_rows
			if not (row.offset_end <= existing.offset_start or row.offset_start >= existing.offset_end)
		]
		if overlaps and any(existing.kind != "secondary" for existing in overlaps):
			continue
		if overlaps:
			v2_rows = [existing for existing in v2_rows if existing not in overlaps]
			occupied = [
				(span_start, span_end)
				for span_start, span_end in occupied
				if not any(span_start == o.offset_start and span_end == o.offset_end for o in overlaps)
			]
		occupied.append((row.offset_start, row.offset_end))
		v2_rows.append(row)
	v2_rows.sort(key=lambda citation: (citation.offset_start, citation.offset_end))
	return v2_rows


def extract_raw_citation_matches_legacy(text: str | None) -> list[RawCitationMatch]:
	content = text or ""
	if not content.strip():
		return []

	candidates = _extract_regex_candidates(content)
	candidates.extend(_extract_case_chain_candidates(content))
	candidates.extend(_extract_eyecite_candidates(content))

	selected: list[RawCitationMatch] = []
	occupied: list[tuple[int, int]] = []
	for start, end, citation in sorted(
		candidates,
		key=lambda item: (
			-_candidate_rank(item[0], item[1], item[2])[0],
			_candidate_rank(item[0], item[1], item[2])[1],
			item[0],
		),
	):
		if any(not (end <= occupied_start or start >= occupied_end) for occupied_start, occupied_end in occupied):
			continue
		occupied.append((start, end))
		selected.append(citation)

	short_form_candidates = _extract_short_form_case_candidates(content, selected)
	for citation in short_form_candidates:
		start, end = citation.offset_start, citation.offset_end
		if any(not (end <= occupied_start or start >= occupied_end) for occupied_start, occupied_end in occupied):
			continue
		occupied.append((start, end))
		selected.append(citation)

	generic_short_candidates = _extract_generic_short_authority_candidates(content)
	for citation in generic_short_candidates:
		start, end = citation.offset_start, citation.offset_end
		if any(not (end <= occupied_start or start >= occupied_end) for occupied_start, occupied_end in occupied):
			continue
		occupied.append((start, end))
		selected.append(citation)

	selected.sort(key=lambda citation: (citation.offset_start, citation.offset_end))
	return selected


def extract_raw_citation_matches(text: str | None) -> list[RawCitationMatch]:
	if _citation_pipeline_v2_enabled():
		rows = extract_raw_citation_matches_v2(text)
		if rows:
			return rows

	return extract_raw_citation_matches_legacy(text)


def extract_case_citation_matches(text: str | None) -> list[RawCitationMatch]:
	"""Return only case-citation layer matches.

	This keeps case-layer callers isolated from statute/convention extraction.
	"""
	return [row for row in extract_raw_citation_matches(text) if row.kind in CASE_CITATION_KINDS]


def extract_statute_reference_matches(text: str | None) -> list[RawCitationMatch]:
	"""Return only statute and legal-instrument matches from deterministic law rules."""
	content = text or ""
	if not content.strip():
		return []

	candidates = [
		citation
		for _start, _end, citation in _extract_regex_candidates(content)
		if citation.kind in STATUTE_REFERENCE_KINDS
	]
	candidates.extend(_extract_anchored_provision_candidates(content, candidates))
	return _select_best_non_overlapping(candidates)


def _canlii_client() -> CanLiiApiClient | None:
	global _CANLII_CLIENT
	if _CANLII_CLIENT is None:
		_CANLII_CLIENT = CanLiiApiClient.from_env()
	return _CANLII_CLIENT


def _resolve_neutral_via_canlii(session: Session, neutral_citation: str) -> int | None:
	client = _canlii_client()
	if client is None:
		return None
	payload = client.lookup_by_neutral(neutral_citation)
	if not payload:
		return None

	candidates: list[str] = []
	for key in ("citation", "neutralCitation", "neutral_citation"):
		value = payload.get(key)
		if isinstance(value, str) and value.strip():
			candidates.append(value.strip())

	for list_key in ("results", "cases", "items", "data"):
		rows = payload.get(list_key)
		if isinstance(rows, list):
			for row in rows:
				if not isinstance(row, dict):
					continue
				for key in ("citation", "neutralCitation", "neutral_citation"):
					value = row.get(key)
					if isinstance(value, str) and value.strip():
						candidates.append(value.strip())

	seen: set[str] = set()
	for candidate in candidates:
		norm = _normalize_whitespace(candidate)
		if not norm or norm in seen:
			continue
		seen.add(norm)
		resolved = _resolve_neutral_to_case_id_local(session, norm)
		if resolved is not None:
			return resolved
	return None


def _resolve_neutral_to_case_id_local(session: Session, neutral_citation: str) -> int | None:
	normalized = _normalize_whitespace(neutral_citation).upper()
	variants: list[str] = [normalized]
	if " FCT " in f" {normalized} ":
		variants.append(normalized.replace(" FCT ", " FC "))
	if " FC " in f" {normalized} ":
		variants.append(normalized.replace(" FC ", " FCT "))

	seen: set[str] = set()
	ordered_variants: list[str] = []
	for variant in variants:
		if variant in seen:
			continue
		seen.add(variant)
		ordered_variants.append(variant)

	case = session.scalar(
		select(Case).where(
			func.upper(func.regexp_replace(func.coalesce(Case.citation, ""), r"\s+", " ", "g"))
			.in_(ordered_variants)
		)
	)
	if case is not None:
		return case.id

	case = session.scalar(
		select(Case).where(
			func.upper(func.regexp_replace(func.coalesce(Case.secondary_citation, ""), r"\s+", " ", "g"))
			.in_(ordered_variants)
		)
	)
	return case.id if case is not None else None


def resolve_neutral_to_case_id(session: Session, neutral_citation: str) -> int | None:
	resolved = _resolve_neutral_to_case_id_local(session, neutral_citation)
	if resolved is not None:
		return resolved
	return _resolve_neutral_via_canlii(session, neutral_citation)


def _resolve_case_alias_to_case_id(session: Session, raw_match: RawCitationMatch) -> int | None:
	if raw_match.kind not in {"case_short", "case_name"}:
		return None
	terms: list[str] = []
	for source in (raw_match.citation_text, raw_match.normalized_citation):
		clean = re.split(r"\s*,\s*(?:at\s+)?para", source or "", maxsplit=1, flags=re.IGNORECASE)[0]
		clean = _normalize_whitespace(clean)
		if not clean:
			continue
		parts = re.split(r"\s+(?:v\.?|vs\.?|c\.?|versus)\s+", clean, maxsplit=1, flags=re.IGNORECASE)
		choices = [clean]
		if len(parts) == 2:
			choices.extend((_normalize_whitespace(parts[0]), _normalize_whitespace(parts[1])))
		for choice in choices:
			term = re.sub(r"[^A-Za-z0-9\s]", " ", choice).strip().lower()
			term = _normalize_whitespace(term)
			if len(term) >= 3 and term not in terms:
				terms.append(term)
	for term in sorted(terms, key=len, reverse=True):
		pattern = f"%{term}%"
		result = session.execute(
			select(Case.id).where(
				Case.title.ilike(pattern)
				| Case.citation.ilike(pattern)
				| Case.secondary_citation.ilike(pattern)
			),
			{"pattern": pattern},
		)
		case_ids: list[int] = []
		if result is not None:
			if hasattr(result, "scalars"):
				case_ids = [int(case_id) for case_id in result.scalars().all()]
			elif hasattr(result, "scalar_one_or_none"):
				case_id = result.scalar_one_or_none()
				if case_id is not None:
					case_ids = [int(case_id)]
		if len(set(case_ids)) > 1:
			return None
		if len(set(case_ids)) == 1:
			return case_ids[0]
		if result is None and hasattr(session, "scalar"):
			case = session.scalar(
				select(Case).prefix_with(f"/* alias lookup: {term.replace('*/', '')} */")
				.where(
					Case.title.ilike(pattern)
					| Case.citation.ilike(pattern)
					| Case.secondary_citation.ilike(pattern)
				)
			)
			if case is not None:
				return int(getattr(case, "id", case))
	return None


def extract_citations_from_text(
	session: Session,
	source_case_id: int,
	text: str | None,
	chunk_id: int | None = None,
	exclude_citations: set[str] | None = None,
) -> list[Citation]:
	selected = []
	for raw_match in extract_raw_citation_matches(text):
		if raw_match.kind not in CASE_CITATION_KINDS:
			continue
		if exclude_citations and raw_match.normalized_citation in exclude_citations:
			continue
		target_case_id = None
		if raw_match.kind == "neutral":
			target_case_id = resolve_neutral_to_case_id(session, raw_match.normalized_citation)
		elif raw_match.kind in {"case", "case_short", "case_name"}:
			if raw_match.kind in {"case_short", "case_name"}:
				target_case_id = _resolve_case_alias_to_case_id(session, raw_match)
			embedded = NEUTRAL_CIT_RE.search(raw_match.normalized_citation)
			if target_case_id is None and embedded is not None:
				target_case_id = resolve_neutral_to_case_id(session, normalize_neutral_citation(embedded))
		selected.append(
			Citation(
				source_case_id=source_case_id,
				target_case_id=target_case_id,
				citation_kind=raw_match.kind,
				citation_text=raw_match.citation_text,
				normalized_citation=raw_match.normalized_citation,
				chunk_id=chunk_id,
				offset_start=raw_match.offset_start,
				offset_end=raw_match.offset_end,
				unresolved=target_case_id is None,
			)
		)

	if selected:
		session.add_all(selected)
	return selected


def extract_statute_references_from_text(
	session: Session,
	source_case_id: int,
	text: str | None,
	chunk_id: int | None = None,
) -> list[StatuteReference]:
	selected: list[StatuteReference] = []
	for raw_match in extract_statute_reference_matches(text):
		parsed = parse_legislation_citation(raw_match.normalized_citation or raw_match.citation_text)
		selected.append(
			StatuteReference(
				source_case_id=source_case_id,
				chunk_id=chunk_id,
				offset_start=raw_match.offset_start,
				offset_end=raw_match.offset_end,
				reference_text=raw_match.citation_text,
				normalized_reference=raw_match.normalized_citation,
				instrument_key=parsed.instrument_key if parsed else None,
				pinpoint=parsed.pinpoint if parsed else None,
				legislation_url=parsed.legislation_url if parsed else None,
				reference_kind=raw_match.kind,
			)
		)

	if selected:
		session.add_all(selected)
	return selected


def _preferred_case_chunks(chunks: list[CaseChunk]) -> list[CaseChunk]:
	if not chunks:
		return []
	by_set: dict[str, list[CaseChunk]] = defaultdict(list)
	for chunk in chunks:
		by_set[getattr(chunk, "chunk_set", "legacy") or "legacy"].append(chunk)
	for chunk_set in ("section", "legacy", "paragraph"):
		if chunk_set in by_set:
			return sorted(by_set[chunk_set], key=lambda item: (item.chunk_index, item.id or 0))
	return sorted(chunks, key=lambda item: (item.chunk_index, item.id or 0))


def rebuild_citations_for_case(session: Session, case: Case, chunks: list[CaseChunk] | None = None) -> int:
	session.execute(delete(Citation).where(Citation.source_case_id == case.id))
	selected_chunks = _preferred_case_chunks(chunks or [])
	case_text = case.full_text or case.summary or ""
	if not selected_chunks:
		excluded = {
			value
			for value in (getattr(case, "citation", None), getattr(case, "secondary_citation", None))
			if value
		}
		return len(extract_citations_from_text(session, case.id, case_text, None, excluded))

	chunk_locations: list[tuple[CaseChunk, int, int]] = []
	search_start = 0
	for chunk in selected_chunks:
		chunk_text = chunk.text or ""
		if not chunk_text:
			continue
		chunk_start = case_text.find(chunk_text, search_start)
		if chunk_start < 0:
			chunk_start = case_text.find(chunk_text)
		if chunk_start < 0:
			continue
		chunk_end = chunk_start + len(chunk_text)
		chunk_locations.append((chunk, chunk_start, chunk_end))
		search_start = max(search_start, chunk_end)

	rows: list[Citation] = []
	for raw_match in extract_case_citation_matches(case_text):
		if is_self_case_name_match(getattr(case, "title", None), raw_match) or is_self_case_citation(case, raw_match):
			continue
		containing = next(
			(
				(chunk, chunk_start)
				for chunk, chunk_start, chunk_end in chunk_locations
				if chunk_start <= raw_match.offset_start < chunk_end
			),
			None,
		)
		chunk_id = containing[0].id if containing is not None else None
		offset_base = containing[1] if containing is not None else 0
		target_case_id = _resolve_case_alias_to_case_id(session, raw_match) if not selected_chunks else None
		rows.append(
			Citation(
				source_case_id=case.id,
				target_case_id=target_case_id,
				citation_kind=raw_match.kind,
				citation_text=raw_match.citation_text,
				normalized_citation=raw_match.normalized_citation,
				chunk_id=chunk_id,
				offset_start=raw_match.offset_start - offset_base,
				offset_end=raw_match.offset_end - offset_base,
				unresolved=target_case_id is None,
			)
		)

	if rows:
		session.add_all(rows)
	return len(rows)


def rebuild_statute_references_for_case(session: Session, case: Case, chunks: list[CaseChunk] | None = None) -> int:
	session.execute(delete(StatuteReference).where(StatuteReference.source_case_id == case.id))
	inserted = 0
	selected_chunks = _preferred_case_chunks(chunks or [])
	if selected_chunks:
		for chunk in selected_chunks:
			inserted += len(extract_statute_references_from_text(session, case.id, chunk.text, chunk.id))
	else:
		inserted += len(extract_statute_references_from_text(session, case.id, case.full_text or case.summary, None))
	return inserted


def batch_extract_citations_from_cases(
	session: Session,
	batch_size: int = 500,
	start_after_case_id: int = 0,
) -> int:
	inserted = 0
	last_case_id = start_after_case_id
	while True:
		cases = list(
			session.scalars(
				select(Case)
				.where(Case.id > last_case_id)
				.order_by(Case.id)
				.limit(batch_size)
			)
		)
		if not cases:
			break
		for case in cases:
			inserted += rebuild_citations_for_case(session, case)
		last_case_id = cases[-1].id
		session.commit()
	return inserted


def batch_extract_citations_from_chunks(session: Session, batch_size: int = 1000) -> int:
	inserted = 0
	last_case_id = 0
	while True:
		case_ids = list(
			session.scalars(
				select(CaseChunk.case_id)
				.where(CaseChunk.case_id > last_case_id)
				.distinct()
				.order_by(CaseChunk.case_id)
				.limit(batch_size)
			)
		)
		if not case_ids:
			break
		chunks = list(
			session.scalars(
				select(CaseChunk)
				.where(CaseChunk.case_id.in_(case_ids))
				.order_by(CaseChunk.case_id, CaseChunk.chunk_index)
			)
		)
		cases_by_id = {
			case.id: case
			for case in session.scalars(select(Case).where(Case.id.in_(case_ids)))
		}
		chunks_by_case: dict[int, list[CaseChunk]] = defaultdict(list)
		for chunk in chunks:
			chunks_by_case[chunk.case_id].append(chunk)
		for case_id, chunk_rows in chunks_by_case.items():
			case = cases_by_id.get(case_id)
			if case is None:
				continue
			inserted += rebuild_citations_for_case(session, case, chunk_rows)
		last_case_id = case_ids[-1]
		session.commit()
	return inserted


def batch_extract_statute_references_from_cases(
	session: Session,
	batch_size: int = 500,
	start_after_case_id: int = 0,
) -> int:
	inserted = 0
	last_case_id = start_after_case_id
	while True:
		cases = list(
			session.scalars(
				select(Case)
				.where(Case.id > last_case_id)
				.order_by(Case.id)
				.limit(batch_size)
			)
		)
		if not cases:
			break
		for case in cases:
			inserted += rebuild_statute_references_for_case(session, case)
		last_case_id = cases[-1].id
		session.commit()
	return inserted


def batch_extract_statute_references_from_chunks(session: Session, batch_size: int = 1000) -> int:
	inserted = 0
	last_case_id = 0
	while True:
		case_ids = list(
			session.scalars(
				select(CaseChunk.case_id)
				.where(CaseChunk.case_id > last_case_id)
				.distinct()
				.order_by(CaseChunk.case_id)
				.limit(batch_size)
			)
		)
		if not case_ids:
			break
		chunks = list(
			session.scalars(
				select(CaseChunk)
				.where(CaseChunk.case_id.in_(case_ids))
				.order_by(CaseChunk.case_id, CaseChunk.chunk_index)
			)
		)
		cases_by_id = {
			case.id: case
			for case in session.scalars(select(Case).where(Case.id.in_(case_ids)))
		}
		chunks_by_case: dict[int, list[CaseChunk]] = defaultdict(list)
		for chunk in chunks:
			chunks_by_case[chunk.case_id].append(chunk)
		for case_id, chunk_rows in chunks_by_case.items():
			case = cases_by_id.get(case_id)
			if case is None:
				continue
			inserted += rebuild_statute_references_for_case(session, case, chunk_rows)
		last_case_id = case_ids[-1]
		session.commit()
	return inserted


def compute_citation_metrics(session: Session) -> int:
	resolved_edges = list(
		session.execute(
			select(Citation.source_case_id, Citation.target_case_id).where(Citation.target_case_id.is_not(None))
		)
	)
	out_degree: dict[int, int] = defaultdict(int)
	in_degree: dict[int, int] = defaultdict(int)
	for source_case_id, target_case_id in resolved_edges:
		if source_case_id is None or target_case_id is None:
			continue
		out_degree[int(source_case_id)] += 1
		in_degree[int(target_case_id)] += 1

	updated = 0
	for case_id, in session.execute(select(Case.id)):
		metrics = session.get(CitationMetrics, case_id)
		if metrics is None:
			metrics = CitationMetrics(case_id=case_id)
			session.add(metrics)
		metrics.in_degree = in_degree.get(case_id, 0)
		metrics.out_degree = out_degree.get(case_id, 0)
		updated += 1

	session.commit()
	return updated


def _a2aj_value(record: dict, *names: str):
	for name in names:
		value = record.get(name)
		if value not in (None, ""):
			return value
	return None


def _as_date(value: object) -> date | None:
	if isinstance(value, datetime):
		return value.date()
	if isinstance(value, date):
		return value
	if value:
		return date.fromisoformat(str(value)[:10])
	return None


def _a2aj_case_key(record: dict) -> str:
	neutral = _a2aj_value(record, "neutral_citation", "citation_en", "citation_fr")
	title = _a2aj_value(record, "name_en", "name_fr")
	document_date = _a2aj_value(record, "document_date_en", "document_date_fr")
	raw_id = _a2aj_value(record, "id", "case_id", "a2aj_case_id")
	if raw_id:
		return str(raw_id)
	parts = [str(neutral or ""), str(title or ""), str(document_date or "")]
	return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:24]


def ingest_a2aj_cases_from_rows(session: Session, rows: list[dict]) -> int:
	inserted = 0
	for record in rows:
		a2aj_case_id = _a2aj_case_key(record)
		neutral_citation = _a2aj_value(record, "neutral_citation", "citation_en", "citation_fr")
		court = _a2aj_value(record, "court", "dataset")
		decision_date = _as_date(_a2aj_value(record, "decision_date", "document_date_en", "document_date_fr"))
		cases_cited = _a2aj_value(record, "cases_cited", "cases_cited_en", "cases_cited_fr")
		cases_citing = _a2aj_value(record, "cases_citing", "cases_citing_en", "cases_citing_fr")
		citing_cases_count = _a2aj_value(record, "citing_cases_count")
		existing = session.scalar(select(A2AJCase).where(A2AJCase.a2aj_case_id == a2aj_case_id))
		if existing is None:
			session.add(
				A2AJCase(
					a2aj_case_id=a2aj_case_id,
					neutral_citation=neutral_citation,
					court=court,
					decision_date=decision_date,
					cases_cited=cases_cited,
					cases_citing=cases_citing,
					citing_cases_count=citing_cases_count if isinstance(citing_cases_count, int) else None,
				)
			)
			inserted += 1
		else:
			existing.neutral_citation = neutral_citation
			existing.court = court
			existing.decision_date = decision_date
			existing.cases_cited = cases_cited
			existing.cases_citing = cases_citing
			existing.citing_cases_count = citing_cases_count if isinstance(citing_cases_count, int) else existing.citing_cases_count
	session.commit()
	return inserted


def build_a2aj_case_map(session: Session) -> int:
	inserted = 0
	for a2aj_case in session.scalars(select(A2AJCase).where(A2AJCase.neutral_citation.is_not(None))):
		local_case = session.scalar(select(Case).where(Case.citation == a2aj_case.neutral_citation))
		if local_case is None:
			continue
		mapping = session.get(A2AJCaseMap, a2aj_case.a2aj_case_id)
		if mapping is None:
			session.add(A2AJCaseMap(a2aj_case_id=a2aj_case.a2aj_case_id, local_case_id=local_case.id))
			inserted += 1
		else:
			mapping.local_case_id = local_case.id
	session.commit()
	return inserted


def ingest_a2aj_citation_edges_from_rows(session: Session, rows: list[dict]) -> int:
	inserted = 0
	for record in rows:
		source_a2aj_case_id = _a2aj_case_key(record)
		cases_cited = _a2aj_value(record, "cases_cited", "cases_cited_en", "cases_cited_fr") or []
		if isinstance(cases_cited, str):
			cases_cited = [cases_cited]
		for cited in cases_cited:
			if cited in (None, ""):
				continue
			existing = session.scalar(
				select(A2AJCitationEdge).where(
					A2AJCitationEdge.source_a2aj_case_id == source_a2aj_case_id,
					A2AJCitationEdge.normalized_citation == str(cited),
				)
			)
			if existing is None:
				session.add(
					A2AJCitationEdge(
						source_a2aj_case_id=source_a2aj_case_id,
						target_a2aj_case_id=None,
						normalized_citation=str(cited),
					)
				)
				inserted += 1
	session.commit()
	return inserted


def convert_a2aj_edges_to_local(session: Session, dedupe: bool = True) -> int:
	maps = {mapping.a2aj_case_id: mapping.local_case_id for mapping in session.scalars(select(A2AJCaseMap))}
	inserted = 0
	for edge in session.scalars(select(A2AJCitationEdge)):
		source_local = maps.get(edge.source_a2aj_case_id)
		if source_local is None:
			continue
		target_local = maps.get(edge.target_a2aj_case_id) if edge.target_a2aj_case_id else None
		if target_local is None and edge.normalized_citation:
			target_local = resolve_neutral_to_case_id(session, edge.normalized_citation)
		if target_local is None:
			continue
		if dedupe:
			existing = session.scalar(
				select(Citation).where(
					Citation.source_case_id == source_local,
					Citation.target_case_id == target_local,
					Citation.normalized_citation == edge.normalized_citation,
					Citation.provenance == "a2aj",
				)
			)
			if existing is not None:
				continue
		session.add(
			Citation(
				source_case_id=source_local,
				target_case_id=target_local,
				citation_text=edge.normalized_citation,
				normalized_citation=edge.normalized_citation,
				chunk_id=None,
				offset_start=None,
				offset_end=None,
				unresolved=False,
				provenance="a2aj",
			)
		)
		inserted += 1
	session.commit()
	return inserted


def merge_local_and_a2aj_graph(session: Session) -> dict[str, int]:
	"""Recompute local graph metrics after any A2AJ merge pass."""
	return {
		"citation_metrics_updated": compute_citation_metrics(session),
	}