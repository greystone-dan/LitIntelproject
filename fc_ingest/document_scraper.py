from __future__ import annotations

import logging
import re
import time
import unicodedata
from datetime import date
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from .errors import HumanValidationRequired
from .models import DocumentData

logger = logging.getLogger(__name__)

_CANONICAL_FIELDS = (
    "date",
    "docket",
    "neutral citation",
    "judge",
    "style of cause",
    "place of hearing",
    "date of hearing",
    "dated",
    "counsel",
    "present",
    "between",
    "solicitors of record",
)
_CRITICAL_FIELDS = {"date", "docket", "neutral citation", "judge", "style of cause"}

_JUDGE_JUNK_RE = re.compile(
    r"^(?:FEDERAL\s+COURT(?:\s+OF\s+APPEAL)?|COUR\s+F[ÉE]D[ÉE]RALE|ANNEX\b.*|ANNEXE\b.*|"
    r"SCHEDULE|ANNEXE|T\.?R\.?\s*\b.*|JUDGE|JUSTICE|JUGE)$",
    re.IGNORECASE,
)


def _is_judge_junk(value: str | None) -> bool:
    """Return True when a captured judge value is a court name, annex, or bare label."""
    if not value:
        return False
    return bool(_JUDGE_JUNK_RE.fullmatch(value.strip()))


def _normalize_whitespace(value: str | None) -> str | None:
    if value is None:
        return None
    normalized = " ".join(value.split())
    return normalized or None


def _normalize_multiline_text(value: str | None) -> str:
    if value is None:
        return ""
    text = str(value).replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _extract_text(soup: BeautifulSoup) -> str:
    for selector in ("div.decision", "div#decision", "div#content"):
        container = soup.select_one(selector)
        if container is not None:
            return _normalize_multiline_text(container.get_text("\n", strip=True))
    return _normalize_multiline_text(soup.get_text("\n", strip=True))


def _normalize_metadata_key(key: str) -> str:
    decomposed = unicodedata.normalize("NFKD", key)
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    normalized = re.sub(r"[^a-z0-9 ]+", " ", stripped.lower())
    normalized = " ".join(normalized.split())
    aliases = {
        "date": "date",
        "date du jugement": "dated",
        "date of hearing": "date of hearing",
        "date de l audience": "date of hearing",
        "file number": "docket",
        "file numbers": "docket",
        "docket number": "docket",
        "court file no": "docket",
        "court file numbers": "docket",
        "numero de dossier": "docket",
        "no du dossier": "docket",
        "numero de dossier neutre": "neutral citation",
        "reference neutre": "neutral citation",
        "citation": "neutral citation",
        "reference": "neutral citation",
        "style": "style of cause",
        "style of cause": "style of cause",
        "entre": "between",
        "et": "between",
        "between": "between",
        "present": "present",
        "before": "present",
        "coram": "present",
        "en presence": "present",
        "en presence de": "present",
        "presente": "present",
        "date": "date",
        "decision date": "date",
        "judgment date": "dated",
        "date of judgment": "dated",
        "date du jugement": "dated",
        "place of hearing": "place of hearing",
        "lieu de l audience": "place of hearing",
        "date of hearing": "date of hearing",
        "reasons for judgment and judgment by": "judge",
        "reasons for judgment by": "judge",
        "judgment delivered by": "judge",
        "jugement rendu par": "judge",
        "en presence de": "present",
        "judge": "judge",
        "judges": "judge",
        "solicitors of record": "solicitors of record",
    }
    return aliases.get(normalized, normalized)


def _normalize_date_token(value: str) -> str | None:
    token = _normalize_whitespace(value)
    if not token:
        return None

    match = re.fullmatch(r"(\d{4})[-/]?(\d{2})[-/]?(\d{2})", token)
    if match:
        year, month, day = match.groups()
        try:
            return date(int(year), int(month), int(day)).isoformat()
        except ValueError:
            return token

    return token


def _normalize_neutral_citation(value: str | None) -> str | None:
    normalized = _normalize_whitespace(value)
    if not normalized:
        return None
    match = re.search(r"\b((?:19|20)\d{2})\s+([A-Za-z]{2,6})\s+(\d{1,6})\b", normalized)
    if not match:
        return normalized
    year, court, number = match.groups()
    return f"{year} {court.upper()} {int(number)}"


def _normalize_docket_value(value: str | None) -> str | None:
    normalized = _normalize_whitespace(value)
    if not normalized:
        return None
    shaped_dockets = re.findall(r"\b[A-Z]{1,6}-\d{1,6}-\d{1,4}\b", normalized, flags=re.IGNORECASE)
    if shaped_dockets:
        return "; ".join(dict.fromkeys(item.upper() for item in shaped_dockets))
    parts = [chunk.strip() for chunk in re.split(r"[;,]", normalized) if chunk.strip()]
    if not parts:
        return normalized
    deduped: list[str] = []
    seen: set[str] = set()
    for part in parts:
        marker = part.casefold()
        if marker in seen:
            continue
        seen.add(marker)
        deduped.append(part)
    return "; ".join(deduped)


def _normalize_style_of_cause(value: str | None) -> str | None:
    normalized = _normalize_whitespace(value)
    if not normalized:
        return None
    normalized = normalized.replace(" c. ", " v. ").replace(" c ", " v ")
    normalized = re.split(r"\b(?:Heard at|Dated|Date of hearing|En présence de|JUGEMENT ET MOTIFS|JUGEMENT ET RAISONS)\b", normalized, maxsplit=1, flags=re.IGNORECASE)[0]
    normalized = _normalize_whitespace(normalized)
    if not normalized:
        return None
    return normalized


def _has_neutral_citation_shape(value: str | None) -> bool:
    if not value:
        return False
    return bool(re.search(r"\b(?:19|20)\d{2}\s+[A-Z]{2,6}\s+\d{1,6}\b", value))


def _has_docket_shape(value: str | None) -> bool:
    if not value:
        return False
    return bool(re.search(r"\b[A-Z]{1,6}-\d{1,6}-\d{2}\b", value))


def _has_judge_shape(value: str | None) -> bool:
    if not value:
        return False
    # Explicit judicial title markers.
    if re.search(r"\b(?:J\.|C\.J\.|JJ\.|Justice|Judge|Juge)\b", value, re.IGNORECASE):
        return True
    # Name-plausible: at least one capitalized word, no leading lowercase token.
    if _JUDGE_JUNK_RE.fullmatch(value.strip()):
        return False
    words = value.split()
    has_capitalized = any(re.match(r"^[A-ZÀ-Þ]", word) for word in words)
    return has_capitalized and bool(re.match(r"^[A-ZÀ-Þ]", words[0]))


def _has_style_shape(value: str | None) -> bool:
    if not value:
        return False
    return bool(re.search(r"\bv\.?\b", value, re.IGNORECASE))


def _field_valid(field: str, value: str | None) -> bool:
    if not value:
        return False
    if field == "neutral citation":
        return _has_neutral_citation_shape(value)
    if field == "docket":
        return _has_docket_shape(value)
    if field == "judge":
        return _has_judge_shape(value)
    if field == "style of cause":
        return _has_style_shape(value)
    return True


def _text_label_present(field: str, full_text: str) -> bool:
    patterns = {
        "date": r"\b(?:Date|Date\s+du\s+jugement)\s*:?\s*",
        "docket": r"\b(?:Docket|Court\s+file\s+no\.?|File\s+numbers?|Dossier|Num[eé]ro\s+de\s+dossier)\s*:?\s*",
        "neutral citation": r"\b(?:Citation|Reference|Neutral\s+citation|R[eé]f[eé]rence(?:\s+neutre)?)\s*:?\s*",
        "judge": r"\b(?:(?:REASONS\s+FOR\s+JUDGMENT(?:\s+AND\s+JUDGMENT)?\s+BY|JUDGMENT\s+DELIVERED\s+BY|PRESENT|CORAM|BEFORE)\s*:|En\s+pr[eé]sence\s+de|En\s+presence\s+de)\s*",
        "style of cause": r"\b(?:(?:BETWEEN|ENTRE|STYLE\s+OF\s+CAUSE)\s*:|ENTRE)\s*",
        "place of hearing": r"\b(?:PLACE\s+OF\s+HEARING|Lieu\s+de\s+l[’']audience):\s*",
        "date of hearing": r"\b(?:DATE\s+OF\s+HEARING|Date\s+de\s+l[’']audience):\s*",
        "dated": r"\b(?:DATED|Date\s+du\s+jugement):\s*",
        "counsel": r"\b(?:APPEARANCES|SOLICITORS\s+OF\s+RECORD|COUNSEL|Avocats|Procureurs):\s*",
        "present": r"\b(?:(?:PRESENT|CORAM|BEFORE)\s*:|En\s+pr[eé]sence\s+de|En\s+presence\s+de)\s*",
        "between": r"\b(?:(?:BETWEEN|ENTRE)\s*:|ENTRE)\s*",
        "solicitors of record": r"\b(?:SOLICITORS\s+OF\s+RECORD|AVOCATS|PROCUREURS):\s*",
    }
    pattern = patterns.get(field)
    if not pattern:
        return False
    return bool(re.search(pattern, full_text, re.IGNORECASE))


def _normalize_field_value(field: str, value: str | None) -> str | None:
    if field in {"date", "date of hearing", "dated"}:
        return _normalize_date_token(value) or _normalize_whitespace(value)
    if field == "neutral citation":
        return _normalize_neutral_citation(value)
    if field == "docket":
        return _normalize_docket_value(value)
    if field == "style of cause":
        return _normalize_style_of_cause(value)
    if field == "judge":
        normalized = _normalize_whitespace(value)
        if not normalized:
            return None
        normalized = re.sub(r"^(?:En présence de|En presence de|PRESENT:|Present:|Before:|BEFORE:)\s*", "", normalized, flags=re.IGNORECASE)
        normalized = re.sub(
            r"^(?:The\s+)?(?:(?:Right\s+)?Honourable|Honorable|L['’]honorable)\s+",
            "",
            normalized,
            flags=re.IGNORECASE,
        )
        normalized = re.sub(
            r"^(?:(?:monsieur|madame)\s+)?(?:le|la)\s+juge(?:\s+en\s+chef(?:\s+par\s+int[ée]rim)?)?\s+",
            "",
            normalized,
            flags=re.IGNORECASE,
        )
        normalized = re.sub(r"^(?:Madame|Mme|M\.|Mme\.|Mr\.?|Mrs\.?|Madam|Mr\.? Justice|Madame Justice|madame la juge en chef par intérim)\s+", "", normalized, flags=re.IGNORECASE)
        return _dedupe_multiline_value(normalized) or _normalize_whitespace(normalized)
    return _dedupe_multiline_value(value) or _normalize_whitespace(value)


def _dedupe_multiline_value(value: str | None) -> str | None:
    text = _normalize_whitespace(value) if value and "\n" not in value else value
    if text is None:
        return None
    lines = [line.strip() for line in str(text).splitlines() if line.strip()]
    if not lines:
        return None
    deduped: list[str] = []
    seen: set[str] = set()
    for line in lines:
        marker = line.casefold()
        if marker in seen:
            continue
        seen.add(marker)
        deduped.append(line)
    if len(deduped) == 1:
        return deduped[0]
    return "\n".join(deduped)


def _looks_like_body_text(line: str) -> bool:
    if not line:
        return False
    if re.match(r"^\[?\d+\]?\s", line):
        return True
    if re.match(r"^(reasons|judgment|decision)\b", line, re.IGNORECASE):
        return True
    if re.match(r"^(heard at|heard on|on appeal from)\b", line, re.IGNORECASE):
        return True
    if len(line) > 140 and re.search(r"\b(the|and|of|to|that|is|was)\b", line, re.IGNORECASE):
        return True
    return False


def _parse_labeled_sections(full_text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current_key: str | None = None
    lines = [line.strip() for line in full_text.splitlines()]
    label_pattern = re.compile(r"^([^:\n]{2,80}):\s*(.*)$")

    for line in lines:
        if not line:
            continue

        judge_match = re.match(r"^En\s+présence\s+de\s+(.+)$", line, flags=re.IGNORECASE)
        if judge_match:
            sections["judge"] = judge_match.group(1).strip()
            current_key = None
            continue

        standalone_key = _normalize_metadata_key(line)
        if standalone_key in {
            "date",
            "docket",
            "neutral citation",
            "judge",
            "place of hearing",
            "date of hearing",
            "dated",
        }:
            sections.setdefault(standalone_key, "")
            current_key = standalone_key
            continue

        label_match = label_pattern.match(line)
        if label_match:
            key = _normalize_metadata_key(label_match.group(1))
            value = _normalize_whitespace(label_match.group(2))
            if value:
                sections[key] = f"{sections[key]}\n{value}".strip() if key in sections else value
            elif key not in sections:
                sections[key] = ""
            current_key = key
            continue

        if current_key and current_key in {
            "between",
            "present",
            "docket",
            "neutral citation",
            "judge",
            "place of hearing",
            "date of hearing",
            "dated",
            "solicitors of record",
            "appearances",
            "counsel",
        }:
            if _looks_like_body_text(line):
                current_key = None
                continue
            existing = sections.get(current_key, "")
            sections[current_key] = f"{existing}\n{line}".strip() if existing else line

    cleaned: dict[str, str] = {}
    for key, value in sections.items():
        deduped = _dedupe_multiline_value(value)
        if deduped:
            cleaned[key] = deduped
    return cleaned


def _extract_heard_at_fallback(full_text: str) -> dict[str, str]:
    match = re.search(
        r"\bHeard at\s+(.+?),\s+on\s+([A-Za-z]+\s+\d{1,2},\s+\d{4})\b",
        full_text,
        re.IGNORECASE,
    )
    if not match:
        match = re.search(
            r"(?m)^\s*(.+?\([^\n]+\)),\s+le\s+\d{1,2}\s+[A-Za-zéû]+\s+\d{4}\s*$",
            full_text,
            re.IGNORECASE,
        )
    if not match:
        return {}
    place = _normalize_whitespace(match.group(1))
    hearing_date = _normalize_whitespace(match.group(2)) if len(match.groups()) > 1 else None
    out: dict[str, str] = {}
    if place:
        out["place of hearing"] = place
        out["place_of_hearing"] = place
    if hearing_date:
        out["date of hearing"] = hearing_date
        out["date_of_hearing"] = hearing_date
    return out


def _derive_style_from_between(between_value: str) -> str | None:
    role_words = {
        "appellant",
        "appellants",
        "applicant",
        "applicants",
        "respondent",
        "respondents",
        "intervener",
        "interveners",
        "plaintiff",
        "defendant",
        "demandeur",
        "demandeuse",
        "demandeurs",
        "demandeuses",
        "défendeur",
        "défenderesse",
        "défendeurs",
        "défenderesses",
        "requérant",
        "requérante",
        "requérants",
        "requérantes",
        "appelant",
        "appelante",
        "appelants",
        "appelantes",
        "intimé",
        "intimée",
        "intimés",
        "intimées",
    }

    def finalize(candidate: str | None) -> str | None:
        value = _normalize_whitespace(candidate)
        if not value:
            return None
        value = re.split(r"\bHeard at\b", value, maxsplit=1, flags=re.IGNORECASE)[0].strip()
        value = _normalize_whitespace(value)
        if not value:
            return None
        if not re.search(r"\bv(?:\.?\s+|\s)\b", value, re.IGNORECASE):
            return None
        value = re.sub(
            r"\s+(?:Applicant|Applicants|Appellant|Appellants|Respondent|Respondents|demandeur|demandeuse|demandeurs|demandeuses|défendeur|défenderesse|défendeurs|défenderesses|requérant|requérante|requérants|requérantes|appelant|appelante|appelants|appelantes|intimé|intimée|intimés|intimées)\b.*$",
            "",
            value,
            flags=re.IGNORECASE,
        )
        if re.search(r"\b(?:of|and|the|de|du|des|la|le)$", value, re.IGNORECASE):
            return None
        return value

    lines: list[str] = []
    for raw in between_value.splitlines():
        line = _normalize_whitespace(raw)
        if not line:
            continue
        if re.fullmatch(r"[-_=]{5,}", line):
            break
        if re.match(r"^(heard at|dated|date of hearing|date du jugement|reasons|jugement|motifs)\b", line, re.IGNORECASE):
            break
        if line.casefold() in role_words:
            continue
        lines.append(line)

    if not lines:
        return None

    for line in lines:
        inline_match = re.search(r"([A-Z].{1,220}?\bv\.?\s+.{1,220})", line, re.IGNORECASE)
        if inline_match:
            style = finalize(inline_match.group(1))
            if style:
                return style

    left: list[str] = []
    right: list[str] = []
    target = left
    for line in lines:
        if line.lower() == "and":
            if target is left and left:
                target = right
            continue
        if line.lower() == "et":
            if target is left and left:
                target = right
            continue
        target.append(line)

    left_text = _normalize_whitespace(" ".join(left))
    right_text = _normalize_whitespace(" ".join(right))
    if left_text and right_text:
        return finalize(f"{left_text} v. {right_text}")
    return None


def _extract_metadata(full_text: str) -> dict[str, Any]:
    metadata: dict[str, Any] = {}
    sections = _parse_labeled_sections(full_text)
    for key, value in sections.items():
        metadata[key] = value

    # Fallbacks for decisions where labels are not in fully uppercase sections.
    date_match = re.search(r"\bDate:\s*(\d{4}[-/]?\d{2}[-/]?\d{2}|\d{8})\b", full_text, re.IGNORECASE)
    if date_match:
        normalized_date = _normalize_date_token(date_match.group(1))
        if normalized_date:
            metadata.setdefault("date", normalized_date)

    docket_match = re.search(r"\bDocket:\s*([A-Za-z0-9\-/, ]{3,100})\b", full_text, re.IGNORECASE)
    if docket_match:
        docket = _normalize_whitespace(docket_match.group(1))
        if docket:
            metadata.setdefault("docket", docket)
    else:
        file_no_match = re.search(r"\b(?:Court\s+file\s+no\.?|File\s+numbers?)\s*:\s*([^\n]{3,100})", full_text, re.IGNORECASE)
        if file_no_match:
            docket = _normalize_whitespace(file_no_match.group(1))
            if docket:
                metadata.setdefault("docket", docket)

    neutral_match = re.search(r"\b(?:Citation|Reference|Neutral citation):\s*((?:19|20)\d{2}\s+[A-Z]{2,5}\s+\d{1,5})\b", full_text, re.IGNORECASE)
    if neutral_match:
        neutral = _normalize_whitespace(neutral_match.group(1))
        if neutral:
            metadata.setdefault("neutral citation", neutral)

    metadata.update({k: v for k, v in _extract_heard_at_fallback(full_text).items() if k not in metadata})

    counsel_parts = [
        metadata.get("counsel"),
        metadata.get("appearances"),
        metadata.get("solicitors of record"),
    ]
    counsel_lines: list[str] = []
    for part in counsel_parts:
        if not part:
            continue
        for line in str(part).splitlines():
            normalized_line = _normalize_whitespace(line)
            if normalized_line:
                counsel_lines.append(normalized_line)
    deduped_counsel = []
    seen_counsel: set[str] = set()
    for line in counsel_lines:
        marker = line.casefold()
        if marker in seen_counsel:
            continue
        seen_counsel.add(marker)
        deduped_counsel.append(line)
    counsel_summary = " | ".join(deduped_counsel)
    if counsel_summary:
        metadata["counsel"] = counsel_summary

    for date_key in ("date", "date of hearing", "dated"):
        if date_key in metadata:
            normalized = _normalize_date_token(metadata[date_key])
            if normalized:
                metadata[date_key] = normalized

    if "style of cause" not in metadata and "between" in metadata:
        style = _derive_style_from_between(metadata["between"])
        if style:
            metadata["style of cause"] = style
    elif "style of cause" in metadata:
        lines = [line.strip() for line in str(metadata["style of cause"]).splitlines() if line.strip()]
        if lines:
            preferred = next((line for line in lines if re.search(r"\bv\.?\b", line, re.IGNORECASE)), lines[0])
            normalized_style = _normalize_whitespace(preferred)
            if normalized_style:
                metadata["style of cause"] = normalized_style
        if not re.search(r"\bv\.?\b", str(metadata.get("style of cause") or ""), re.IGNORECASE) and "between" in metadata:
            # Truncated capture (e.g. end-of-decision STYLE OF CAUSE block lost the versus form):
            # prefer the BETWEEN-derived style when it reconstructs one.
            derived_style = _derive_style_from_between(metadata["between"])
            if derived_style:
                metadata["style of cause"] = derived_style

    if "judge" not in metadata and "present" in metadata:
        first_line = next((line.strip() for line in metadata["present"].splitlines() if line.strip()), "")
        if first_line:
            metadata["judge"] = first_line

    if "judge" in metadata:
        judge_first_line = next((line.strip() for line in str(metadata["judge"]).splitlines() if line.strip()), "")
        if judge_first_line:
            metadata["judge"] = judge_first_line

    present_first_line = next((line.strip() for line in str(metadata.get("present") or "").splitlines() if line.strip()), "")
    present_candidate = (
        _normalize_field_value("judge", present_first_line) if present_first_line else None
    )
    judge_value = metadata.get("judge")
    judge_raw = next((line.strip() for line in str(judge_value or "").splitlines() if line.strip()), "")
    if judge_raw and _is_judge_junk(judge_raw):
        # Junk capture (court name, annex, or bare role label): prefer the title-page judge.
        if present_candidate:
            metadata["judge"] = present_candidate
        else:
            metadata.pop("judge", None)

    signature_match = re.search(
        r'"([^"\n]{3,120})"\s*\n\s*(?:The\s+)?Judge\b',
        full_text,
        re.IGNORECASE,
    )
    signature_name = (
        _normalize_whitespace(signature_match.group(1))
        if signature_match and not _is_judge_junk(signature_match.group(1))
        else None
    )

    if "judge" not in metadata:
        if signature_name:
            metadata["judge"] = signature_name
        elif present_candidate and not _is_judge_junk(present_candidate):
            metadata["judge"] = present_candidate
    elif signature_name:
        # Prefer the full signature name when it corroborates the current surname.
        current_surname = next(
            (token for token in reversed(str(metadata["judge"]).split()) if re.search(r"[A-Za-zÀ-þ]", token)),
            "",
        ).casefold().rstrip(".")
        if current_surname and current_surname in signature_name.casefold():
            metadata["judge"] = signature_name

    # Preserve snake_case aliases for compatibility with existing downstream usage.
    if "place of hearing" in metadata:
        metadata["place_of_hearing"] = metadata["place of hearing"]
    if "date of hearing" in metadata:
        metadata["date_of_hearing"] = metadata["date of hearing"]

    for key, value in list(metadata.items()):
        if not isinstance(value, str):
            continue
        deduped = _dedupe_multiline_value(value)
        if deduped:
            metadata[key] = deduped

    return metadata


def _style_from_title(title: str | None) -> str | None:
    if not title:
        return None
    candidate = _normalize_whitespace(title)
    if not candidate:
        return None
    candidate = candidate.replace(" c. ", " v. ").replace(" c ", " v ")
    candidate = re.split(r"\b(?:Judgment|Reasons|Motifs|JUGEMENT|MOTIFS|DECISION)\b", candidate, maxsplit=1, flags=re.IGNORECASE)[0]
    candidate = _normalize_whitespace(candidate)
    if not candidate or not re.search(r"\bv(?:\.?\s+|\s)\b", candidate, re.IGNORECASE):
        return None
    return candidate


def _extract_metadata_with_quality(full_text: str, table_metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    text_metadata = _extract_metadata(full_text)
    table_metadata = dict(table_metadata or {})

    table_normalized: dict[str, str] = {}
    for raw_key, raw_value in table_metadata.items():
        key = _normalize_metadata_key(str(raw_key))
        normalized_value = _normalize_whitespace(str(raw_value)) if raw_value is not None else None
        if key and normalized_value:
            table_normalized[key] = normalized_value

    metadata: dict[str, Any] = {}
    field_sources: dict[str, dict[str, str]] = {}
    field_confidence: dict[str, float] = {}
    quality_flags: list[str] = []

    for field in _CANONICAL_FIELDS:
        source_values: dict[str, str] = {}
        text_value = _normalize_field_value(field, text_metadata.get(field))
        table_value = _normalize_field_value(field, table_normalized.get(field))
        if text_value:
            source_values["text"] = text_value
        if table_value:
            source_values["table"] = table_value

        if not source_values:
            if field in _CRITICAL_FIELDS:
                quality_flags.append(f"missing_critical:{field}")
            continue

        chosen = source_values.get("table") or source_values.get("text")
        confidence = 0.72

        if "table" in source_values:
            confidence = 0.94
        elif "text" in source_values:
            confidence = 0.92 if _text_label_present(field, full_text) else 0.78
        if "text" in source_values and "table" in source_values:
            if source_values["text"].casefold() == source_values["table"].casefold():
                confidence = 0.99
            else:
                confidence = 0.83
                quality_flags.append(f"conflict:{field}")

        if _field_valid(field, chosen):
            confidence = min(0.999, confidence + 0.05)
        else:
            confidence = max(0.45, confidence - 0.2)
            quality_flags.append(f"invalid_shape:{field}")

        if field in _CRITICAL_FIELDS and confidence < 0.9:
            quality_flags.append(f"low_confidence_critical:{field}")

        metadata[field] = chosen
        field_sources[field] = source_values
        field_confidence[field] = round(confidence, 3)

    # Preserve useful non-canonical text fields for debugging and downstream display.
    for key, value in text_metadata.items():
        if key in metadata:
            continue
        metadata[key] = value

    # Preserve snake_case aliases for compatibility with existing downstream usage.
    if "place of hearing" in metadata:
        metadata["place_of_hearing"] = metadata["place of hearing"]
    if "date of hearing" in metadata:
        metadata["date_of_hearing"] = metadata["date of hearing"]

    metadata["_field_sources"] = field_sources
    metadata["_field_confidence"] = field_confidence
    metadata["_quality_flags"] = sorted(set(quality_flags))
    metadata["_needs_review"] = any(
        field in _CRITICAL_FIELDS and field_confidence.get(field, 0.0) < 0.9
        for field in _CRITICAL_FIELDS
    )

    return metadata


def _extract_table_metadata(soup: BeautifulSoup) -> dict[str, Any]:
    metadata: dict[str, Any] = {}
    for row in soup.select("tr"):
        cells = row.select("th, td")
        if len(cells) < 2:
            continue
        key = _normalize_whitespace(cells[0].get_text(" ", strip=True).rstrip(":"))
        value = _normalize_whitespace(cells[1].get_text(" ", strip=True))
        if key and value:
            metadata[key.lower()] = value
    return metadata


def _extract_pdf_url(document_url: str, soup: BeautifulSoup) -> str:
    for anchor in soup.find_all("a", href=True):
        href = anchor.get("href", "")
        text = anchor.get_text(" ", strip=True).lower()
        href_lower = href.lower()
        if (
            href_lower.endswith(".pdf")
            or "/document.do" in href_lower
            or "pdf" in text
            or "download" in text
        ):
            return urljoin(document_url, href)
    return ""


def fetch_document_page(document_url: str, timeout: float = 60.0, retries: int = 3, backoff_seconds: float = 1.0) -> str:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(document_url, headers={"User-Agent": "AI-CaseLibrary-FCIngest/1.0"}, timeout=timeout)
            if response.status_code == 403 and "captcha" in response.text.lower():
                raise HumanValidationRequired(
                    "Lexum requires human CAPTCHA validation before Federal Court judgment ingestion can resume"
                )
            response.raise_for_status()
            return response.text
        except HumanValidationRequired:
            raise
        except requests.RequestException as exc:  # pragma: no cover - exercised in runtime
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(backoff_seconds * attempt)
    raise RuntimeError(f"Failed to fetch document page: {document_url}") from last_error


def parse_document_page(document_url: str, html: str) -> DocumentData:
    soup = BeautifulSoup(html, "html.parser")
    heading = soup.select_one("h1, h2")
    title = _normalize_whitespace(heading.get_text(" ", strip=True)) if heading else "Untitled decision"
    full_text = _extract_text(soup)
    table_metadata = _extract_table_metadata(soup)
    metadata = _extract_metadata_with_quality(full_text, table_metadata)
    for key, value in table_metadata.items():
        metadata.setdefault(key, value)

    title_style = _style_from_title(title)
    if title_style:
        metadata["style of cause"] = title_style
        metadata.setdefault("_field_sources", {})["style of cause"] = {"title": title_style}
        metadata.setdefault("_field_confidence", {})["style of cause"] = 0.88 if metadata.get("between") else 0.8
        metadata.setdefault("_quality_flags", [])
    pdf_url = _extract_pdf_url(document_url, soup)
    if pdf_url:
        metadata.setdefault("pdf_url", pdf_url)
    metadata.setdefault("document_url", document_url)
    return DocumentData(title=title, full_text=full_text, metadata=metadata)


def scrape_document_page(document_url: str, timeout: float = 60.0, retries: int = 3, backoff_seconds: float = 1.0) -> DocumentData:
    html = fetch_document_page(document_url, timeout=timeout, retries=retries, backoff_seconds=backoff_seconds)
    return parse_document_page(document_url, html)
