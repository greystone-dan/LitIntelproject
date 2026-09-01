from __future__ import annotations

import re
from dataclasses import dataclass

from fc_ingest.document_scraper import _extract_metadata_with_quality
from backend.legal_tagger import LegalTagger


METADATA_FIELDS = (
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
	"decision outcome",
	"government role",
	"government outcome",
	"case type",
	"case challenge",
	"case issue",
	"case topic",
)

_GOVERNMENT_PARTY_RE = re.compile(
	r"\b(?:minister|attorney\s+general|public\s+safety|citizenship\s+and\s+immigration|canada\s+border\s+services\s+agency|\bcbsa\b|\bircc\b|government\s+of\s+canada)\b",
	re.IGNORECASE,
)

_OUTCOME_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
	(
		"dismissed",
		re.compile(
			r"\b(?:application|appeal|judicial\s+review|motion|proceeding|claim|complaint|action)\b[^\n\.]{0,140}\b(?:is|are|be|hereby)?\s*(?:dismissed|denied|refused)\b",
			re.IGNORECASE,
		),
	),
	(
		"allowed",
		re.compile(
			r"\b(?:application|appeal|judicial\s+review|motion|proceeding|claim|complaint|action)\b[^\n\.]{0,140}\b(?:is|are|be|hereby)?\s*(?:allowed|granted)\b",
			re.IGNORECASE,
		),
	),
	(
		"granted",
		re.compile(
			r"\b(?:application|appeal|judicial\s+review|motion|proceeding|claim|complaint|action)\b[^\n\.]{0,140}\b(?:is|are|be|hereby)?\s*granted\b",
			re.IGNORECASE,
		),
	),
	(
		"set_aside",
		re.compile(r"\b(?:is|are|be|hereby)?\s*(?:set aside|quashed|annulled|vacated)\b", re.IGNORECASE),
	),
	(
		"remitted",
		re.compile(r"\b(?:is|are|be|hereby)?\s*(?:remitted|referred back|sent back)\b", re.IGNORECASE),
	),
)


@dataclass(frozen=True)
class MetadataMatch:
	field: str
	text: str
	value: str
	offset_start: int
	offset_end: int
	confidence: float
	source: str


@dataclass(frozen=True)
class MetadataObservation:
	field: str
	text: str
	value: str
	offset_start: int | None
	offset_end: int | None
	confidence: float
	source: str
	span_matched: bool


def _find_value_span(text: str, value: str) -> tuple[int, int] | None:
	parts = value.split()
	if not parts:
		return None
	pattern = r"\s+".join(re.escape(part) for part in parts)
	match = re.search(pattern, text, re.IGNORECASE)
	if not match:
		return None
	return match.start(), match.end()


def _field_source_label(field_sources: dict[str, str]) -> str:
	has_text = bool(str(field_sources.get("text") or "").strip())
	has_table = bool(str(field_sources.get("table") or "").strip())
	if has_text and has_table:
		return "text+table"
	if has_table:
		return "table"
	if has_text:
		return "text"
	return "derived"


def _operative_blocks(content: str) -> list[str]:
	if not content:
		return []
	tail = content[-12000:]
	markers = list(re.finditer(r"\b(?:ORDER|JUDGMENT|DISPOSITION|CONCLUSION)\b", tail, re.IGNORECASE))
	if not markers:
		return [tail]
	blocks: list[str] = []
	for index, marker in enumerate(markers):
		end = markers[index + 1].start() if index + 1 < len(markers) else len(tail)
		block = tail[marker.start() : end].strip()
		if block:
			blocks.append(block)
	return blocks


def _outcome_window(content: str) -> str:
	blocks = _operative_blocks(content)
	if not blocks:
		return ""
	best_block = max(
		blocks,
		key=lambda block: (
			sum(bool(pattern.search(block)) for _label, pattern in _OUTCOME_PATTERNS),
			len(block),
		),
	)
	return best_block


def _latest_outcome_label(content: str) -> str | None:
	latest: tuple[int, str] | None = None
	search_content = _outcome_window(content)
	for label, pattern in _OUTCOME_PATTERNS:
		for match in pattern.finditer(search_content):
			if latest is None or match.start() > latest[0]:
				latest = (match.start(), label)
	if latest is None:
		return None
	return latest[1]


def _government_role(style_or_between: str) -> str | None:
	if not style_or_between:
		return None
	text = " ".join(style_or_between.split())
	lower = text.lower()
	if not _GOVERNMENT_PARTY_RE.search(lower):
		return None

	applicant_matches = list(re.finditer(r"\bapplicants?\b", lower))
	respondent_matches = list(re.finditer(r"\brespondents?\b", lower))
	gov_matches = list(_GOVERNMENT_PARTY_RE.finditer(lower))
	if not gov_matches:
		return None

	def nearest_distance(a: int, positions: list[re.Match[str]]) -> int:
		if not positions:
			return 10**9
		best = 10**9
		for pos in positions:
			distance = abs(a - pos.start())
			# In captions, the role token commonly appears after the party name.
			if pos.start() < a:
				distance += 40
			if distance < best:
				best = distance
		return best

	best_role: str | None = None
	best_distance = 10**9
	for match in gov_matches:
		idx = match.start()
		d_app = nearest_distance(idx, applicant_matches)
		d_res = nearest_distance(idx, respondent_matches)
		if min(d_app, d_res) > 120:
			continue
		if d_app < d_res and d_app < best_distance:
			best_distance = d_app
			best_role = "applicant"
		elif d_res < d_app and d_res < best_distance:
			best_distance = d_res
			best_role = "respondent"

	if best_role is not None:
		return best_role

	vs_split = re.split(r"\bv\.?\b", lower, maxsplit=1)
	if len(vs_split) == 2:
		left, right = vs_split
		if _GOVERNMENT_PARTY_RE.search(left):
			return "applicant"
		if _GOVERNMENT_PARTY_RE.search(right):
			return "respondent"
	return None


def _first_numbered_paragraphs(content: str, limit: int = 10) -> list[str]:
	paragraphs: list[str] = []
	for line in re.split(r"\n+", content):
		candidate = line.strip()
		if not candidate:
			continue
		if re.match(r"^(?:\d+|[ivxlcdm]+|[A-Z])(?:[\.)]|\s+[\.)])\s+", candidate, flags=re.IGNORECASE):
			paragraphs.append(candidate)
		if len(paragraphs) >= limit:
			break
	if paragraphs:
		return paragraphs
	return [segment.strip() for segment in re.split(r"\n\s*\n+", content) if segment.strip()][:limit]


def _derive_case_subject_fields(content: str, metadata: dict[str, object]) -> dict[str, tuple[str | float, float]]:
	derived: dict[str, tuple[str | float, float]] = {}
	if not content.strip():
		return derived

	name_filter = lambda value: " ".join(str(value).split()).strip()
	candidate_text = "\n".join(
		[*_first_numbered_paragraphs(content, limit=10), content[:4000]]
	)
	tags = LegalTagger().tag(candidate_text)
	all_tags = [tag for tag in tags if tag.category in {"proceeding", "issue", "legal_area", "statute", "regulation"}]
	scored: dict[str, int] = {}
	for tag in all_tags:
		scored[tag.value] = scored.get(tag.value, 0) + max(1, int(round(tag.score * 10)))

	case_type_rank = {
		"judicial_review": 90,
		"appeal": 88,
		"detention_review": 86,
		"prra": 82,
		"admissibility_hearing": 80,
		"humanitarian_compassionate": 75,
		"immigration_refugee": 60,
	}
	selected_type = "general_immigration_litigation"
	for tag in tags:
		if tag.category != "proceeding":
			continue
		priority = case_type_rank.get(tag.value, 10)
		if priority > case_type_rank.get(selected_type, 0):
			selected_type = tag.value
	if selected_type == "general_immigration_litigation":
		for tag in tags:
			if tag.category == "legal_area" and tag.value in {"immigration_refugee", "constitutional_charter", "criminal"}:
				selected_type = tag.value
				break
	if "judicial review" in content.lower() or "application for judicial review" in content.lower():
		selected_type = "judicial_review"
	elif re.search(r"\bappeal\b", content, flags=re.IGNORECASE):
		selected_type = "appeal"
	elif re.search(r"\bdetention review\b", content, flags=re.IGNORECASE):
		selected_type = "detention_review"
	elif re.search(r"\bPRRA\b|\bpre[- ]removal risk assessment\b", content, flags=re.IGNORECASE):
		selected_type = "prra"
	elif re.search(r"\b(admissibility hearing|admissibility)\b", content, flags=re.IGNORECASE):
		selected_type = "admissibility_hearing"

	case_challenge = selected_type
	if re.search(r"\b(?:RPD|Refugee Protection Division)\b", content, flags=re.IGNORECASE):
		case_challenge = "refugee_protection_decision"
	elif re.search(r"\b(?:removal order|departure order|deportation order|exclusion order)\b", content, flags=re.IGNORECASE):
		case_challenge = "removal_or_deportation_order"
	elif re.search(r"\b(?:inadmissib|security grounds|serious criminality)\b", content, flags=re.IGNORECASE):
		case_challenge = "inadmissibility_decision"
	elif re.search(r"\b(?:detention|release|bondsperson|community case management)\b", content, flags=re.IGNORECASE):
		case_challenge = "detention_or_release_decision"
	elif re.search(r"\b(?:PRRA|pre[- ]removal risk assessment)\b", content, flags=re.IGNORECASE):
		case_challenge = "prra_decision"
	elif re.search(r"\b(?:humanitarian and compassionate|HC\b|H&C\b)\b", content, flags=re.IGNORECASE):
		case_challenge = "humanitarian_compassionate_application"
	elif re.search(r"\b(?:Convention|refugee convention|Article 1F|Article 1E|state protection)\b", content, flags=re.IGNORECASE):
		case_challenge = "refugee_protection_basis"
	if case_challenge == selected_type and selected_type == "general_immigration_litigation":
		case_challenge = "general_immigration_legal_issue"

	issue_candidates = [tag.value for tag in tags if tag.category == "issue"]
	issue_value = "general_immigration_issue"
	priority_issues = {
		"credibility": 90,
		"procedural_fairness": 88,
		"state_protection": 86,
		"internal_flight_alternative": 84,
		"nexus": 82,
		"exclusion_article_1f": 80,
		"detention": 79,
		"cessation": 78,
		"medical_exception": 76,
		"sur_place_claim": 74,
		"non_refoulement": 72,
		"best_interests_child": 70,
		"sogiesc": 68,
	}
	for tag in sorted(tags, key=lambda item: priority_issues.get(item.value, 0), reverse=True):
		if tag.category == "issue":
			issue_value = tag.value
			break
	if not issue_candidates:
		issue_value = selected_type if selected_type != "general_immigration_litigation" else "immigration_litigation"

	topic_values = []
	for tag in tags:
		if tag.category in {"issue", "proceeding", "legal_area"} and tag.value:
			topic_values.append(tag.value)
	for token in ["judicial_review", "immigration_refugee", "credibility", "procedural_fairness", "refugee_protection"]:
		if token in topic_values and token not in {"judicial_review"}:
			topic_values.insert(0, token)
	topic_values = list(dict.fromkeys(topic_values))[:5]
	case_topic = ", ".join(topic_values) if topic_values else selected_type

	derived["case type"] = (selected_type, 0.82)
	derived["case challenge"] = (case_challenge, 0.8)
	derived["case issue"] = (issue_value, 0.75)
	derived["case topic"] = (case_topic, 0.7)
	return derived


def _derive_outcome_fields(content: str, metadata: dict[str, object]) -> dict[str, tuple[str, float]]:
	derived: dict[str, tuple[str, float]] = {}
	outcome = _latest_outcome_label(content)
	if outcome:
		derived["decision outcome"] = (outcome, 0.78)

	style_text = str(metadata.get("style of cause") or "").strip()
	between_text = str(metadata.get("between") or "").strip()
	role_source_text = "\n".join(part for part in (style_text, between_text, content[:1200]) if part)
	gov_role = _government_role(role_source_text)
	if gov_role:
		derived["government role"] = (gov_role, 0.74)

	if outcome and gov_role:
		if outcome == "dismissed":
			government_outcome = "lost" if gov_role == "applicant" else "won"
		elif outcome in {"allowed", "granted", "set_aside", "remitted"}:
			government_outcome = "won" if gov_role == "applicant" else "lost"
		else:
			government_outcome = "undetermined"
		derived["government outcome"] = (government_outcome, 0.76)

	derived.update(_derive_case_subject_fields(content, metadata))
	return derived


def extract_case_metadata(text: str | None) -> dict[str, object]:
	"""Extract the complete metadata payload stored once on a case."""
	content = text or ""
	if not content.strip():
		return {}

	extracted = dict(_extract_metadata_with_quality(content))
	confidence = dict(extracted.get("_field_confidence") or {})
	sources = dict(extracted.get("_field_sources") or {})
	for field, (value, score) in _derive_outcome_fields(content, extracted).items():
		extracted[field] = value
		confidence[field] = score
		sources[field] = {"derived": value}

	payload = {
		field: extracted[field]
		for field in METADATA_FIELDS
		if extracted.get(field)
	}
	payload["_field_confidence"] = confidence
	payload["_field_sources"] = sources
	payload["_quality_flags"] = list(extracted.get("_quality_flags") or [])
	payload["_needs_review"] = bool(extracted.get("_needs_review"))
	return payload


def extract_metadata_observations(text: str | None) -> list[MetadataObservation]:
	"""Return metadata captures, including fields without exact text-span matches."""
	content = text or ""
	if not content.strip():
		return []

	metadata = extract_case_metadata(content)
	confidence = dict(metadata.get("_field_confidence") or {})
	sources = dict(metadata.get("_field_sources") or {})
	rows: list[MetadataObservation] = []
	for field in METADATA_FIELDS:
		value = str(metadata.get(field) or "").strip()
		if not value:
			continue
		field_sources = sources.get(field) or {}
		source_value = str(field_sources.get("text") or value).strip()
		span = _find_value_span(content, source_value) if source_value else None
		source_label = _field_source_label(field_sources)
		if span:
			start, end = span
			rows.append(
				MetadataObservation(
					field=field,
					text=content[start:end],
					value=value,
					offset_start=start,
					offset_end=end,
					confidence=float(confidence.get(field) or 0.0),
					source=source_label,
					span_matched=True,
				)
			)
			continue
		rows.append(
			MetadataObservation(
				field=field,
				text=source_value or value,
				value=value,
				offset_start=None,
				offset_end=None,
				confidence=float(confidence.get(field) or 0.0),
				source=source_label,
				span_matched=False,
			)
		)

	return rows


def extract_metadata_matches(text: str | None) -> list[MetadataMatch]:
	"""Return deterministic metadata fields that map to exact source spans."""
	matches: list[MetadataMatch] = []
	for row in extract_metadata_observations(text):
		if not row.span_matched or row.offset_start is None or row.offset_end is None:
			continue
		matches.append(
			MetadataMatch(
				field=row.field,
				text=row.text,
				value=row.value,
				offset_start=row.offset_start,
				offset_end=row.offset_end,
				confidence=row.confidence,
				source=row.source,
			)
		)
	return matches