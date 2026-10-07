"""Bare short forms of landmark cases: "Vavilov at para 85" with no full citation in the decision.

Pass one only extracts a short form when the full citation appears earlier in the
same decision. Many decisions cite the most common authorities by name alone, so
this step knows a small, fixed list of landmark decisions whose name is
unambiguous in immigration and administrative-law decisions, and links
"<Name> at para N" (or French "au para N") to the case's neutral citation.

The list is deliberately short and explicit; add a name only when it is the one
well-known case a pinpoint after it can mean. A row is added only when nothing
else already covers that text.
"""

from __future__ import annotations

import re
from dataclasses import replace

from .models import ACTION_ADDED, RefinedCitation
from .pinpoints import TRAILING_PINPOINT_RE, parse_all_pinpoints, pinpoint_phrase

# name -> (full name for display, neutral citation, identifier keys)
LANDMARKS: dict[str, tuple[str, str, tuple[str, ...]]] = {
	"Vavilov": ("Canada (Minister of Citizenship and Immigration) v. Vavilov", "2019 SCC 65", ("2019 SCC 65",)),
	"Dunsmuir": ("Dunsmuir v. New Brunswick", "2008 SCC 9", ("2008 SCC 9",)),
	"Khosa": ("Canada (Citizenship and Immigration) v. Khosa", "2009 SCC 12", ("2009 SCC 12",)),
	"Kanthasamy": ("Kanthasamy v. Canada (Citizenship and Immigration)", "2015 SCC 61", ("2015 SCC 61",)),
	"Agraira": ("Agraira v. Canada (Public Safety and Emergency Preparedness)", "2013 SCC 36", ("2013 SCC 36",)),
	"Newfoundland Nurses": ("Newfoundland and Labrador Nurses' Union v. Newfoundland and Labrador (Treasury Board)", "2011 SCC 62", ("2011 SCC 62",)),
	"Doré": ("Doré v. Barreau du Québec", "2012 SCC 12", ("2012 SCC 12",)),
	"Mason": ("Mason v. Canada (Citizenship and Immigration)", "2023 SCC 21", ("2023 SCC 21",)),
	"Baker": ("Baker v. Canada (Minister of Citizenship and Immigration)", "1999 CanLII 699 (SCC)", ("1999 CANLII 699",)),
}

_NAME_RE = re.compile(
	r"(?<![\w’'.-])(?P<name>" + "|".join(re.escape(name) for name in sorted(LANDMARKS, key=len, reverse=True)) + r")\b(?!\s+(?:v\.?|c\.?)\s)"
)


def landmark_rows(content: str, existing: list[RefinedCitation]) -> list[RefinedCitation]:
	"""New rows for bare "<Landmark> at para N" mentions that no existing row covers."""
	added: list[RefinedCitation] = []
	for match in _NAME_RE.finditer(content):
		window = content[match.end() : match.end() + 160]
		pin = TRAILING_PINPOINT_RE.match(window)
		if pin is None or not re.match(r"\s*,?\s*(?:at|aux?|à)\s", window, re.IGNORECASE):
			continue
		start, end = match.start(), match.end() + pin.end()
		if any(not (end <= row.offset_start or start >= row.offset_end) for row in existing):
			continue
		text = content[start:end]
		pinpoints = tuple(parse_all_pinpoints(text))
		if not pinpoints:
			continue
		full_name, cite, keys = LANDMARKS[match.group("name")]
		added.append(
			RefinedCitation(
				kind="case_short",
				citation_text=text,
				normalized_citation=f"{full_name}, {cite}",
				offset_start=start,
				offset_end=end,
				step="C4b_landmarks",
				action=ACTION_ADDED,
				confidence=0.8,
				pinpoint=pinpoint_phrase(pinpoints[0]),
				pinpoints=pinpoints,
				declared_alias=match.group("name"),
				identifiers=keys,
				notes=("landmark_short_form",),
			)
		)
	return added
