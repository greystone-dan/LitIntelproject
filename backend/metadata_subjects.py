"""Subject-field derivation for case metadata.

Derives case type, challenge, issue, and topic from the first numbered
paragraphs and the opening of the decision using the legal tagger. Imported by
`backend.metadata`; nothing else should depend on these helpers.
"""

from __future__ import annotations

import re

from backend.legal_tagger import LegalTagger


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


def _derive_case_subject_fields(content: str, metadata: dict[str, object]) -> dict[str, tuple[str, float]]:
	derived: dict[str, tuple[str, float]] = {}
	if not content.strip():
		return derived

	candidate_text = "\n".join(
		[*_first_numbered_paragraphs(content, limit=10), content[:4000]]
	)
	tags = LegalTagger().tag(candidate_text)

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
	derived["challenged issue"] = (issue_value, 0.75)
	if issue_candidates:
		derived["challenged issues"] = (", ".join(list(dict.fromkeys(issue_candidates))[:8]), 0.72)
	derived["case topic"] = (case_topic, 0.7)
	return derived
