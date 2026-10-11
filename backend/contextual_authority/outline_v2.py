"""Reader outline, second version: four sections with sub-points, and the section a citation sits in (no AI).

``case_structure.structure_outline`` labels every formatted block with one of six roles and lists each run. On long
decisions that gave a flickering list (Analysis, Issues, Facts, Analysis again) and one huge "Analysis" row. This
version works on whole paragraphs (a numbered paragraph plus the unnumbered lines under it), forces the order a
decision really has, and reports four sections:

    Background (overview and facts)  ->  Issues  ->  Analysis  ->  Disposition

Inside the sections the decision's own headings become sub-points (level 2, or 3 for a sub-heading). Where the
analysis runs on with no printed heading, a sub-point starts where the subject changes (credibility, state
protection, standard of review ...) or where the court announces a new issue ("I turn now to ...").

Every row has ``start`` and ``end`` character offsets in the decision text, so ``section_for_offset`` can say which
section (and sub-point) a citation sits in. Enabled with ILIT_OUTLINE_V2=1 (default off).
"""

from __future__ import annotations

import os
import re
from collections import OrderedDict
from collections.abc import Sequence
from typing import Any

from . import case_structure as cs

OUTLINE_V2_VERSION = "case_structure_outline_v2"

SECTION_TITLES = {"background": "Background", "issues": "Issues", "analysis": "Analysis", "disposition": "Disposition"}
_ROLE_SECTION = {"overview": "background", "facts": "background", "issues": "issues", "analysis": "analysis", "disposition": "disposition"}
_SECTION_ROLE = {"background": "facts", "issues": "issues", "analysis": "analysis", "disposition": "disposition"}
_PICKED_TYPES = {"meta", "heading", "para", "text", "listitem", "footer", "signature"}
_CONTINUATION_TYPES = {"text", "listitem"}


def outline_v2_enabled() -> bool:
	return os.getenv("ILIT_OUTLINE_V2", "").strip().lower() in {"1", "true", "yes", "on"}


# --------------------------------------------------------------------------- topics for heading-less analysis

_TOPICS: tuple[tuple[str, re.Pattern[str]], ...] = (
	("Standard of review", re.compile(r"standard of review|presumption of reasonableness|reasonableness standard|correctness standard|\bVavilov\b|reviewed on a standard", re.I)),
	("Procedural fairness", re.compile(r"procedural fairness|natural justice|duty of fairness|right to be heard|reasonable apprehension of bias|impartial", re.I)),
	("Credibility", re.compile(r"credib|implausib|inconsisten|omission|contradict|embellish|not believ|trustworth|adverse (?:credibility )?finding", re.I)),
	("Identity", re.compile(r"\bidentity\b|identity documents?|passport|nationality|birth certificate", re.I)),
	("Delay in claiming", re.compile(r"delay in (?:claiming|making|seeking|leaving)|failure to claim|did not claim|subjective fear|delay in", re.I)),
	("State protection", re.compile(r"state protection|clear and convincing|operational adequacy|adequate protection|police (?:protection|were unable)", re.I)),
	("Internal flight alternative", re.compile(r"internal flight|\bIFA\b|\bIPA\b|internal protection alternative|relocate (?:to|within)", re.I)),
	("Well-founded fear and risk", re.compile(r"well[- ]founded fear|serious possibility|persecution|risk of (?:harm|torture|life)|section 97|section 96|personalized risk|forward-looking|objective basis", re.I)),
	("Convention ground (nexus)", re.compile(r"nexus|convention ground|particular social group|political opinion", re.I)),
	("Best interests of the child", re.compile(r"best interests? of the child|\bBIOC\b|children(?:’|')?s? interests", re.I)),
	("Humanitarian and compassionate factors", re.compile(r"humanitarian and compassionate|\bH&C\b|hardship|establishment in canada|unusual and undeserved|section 25", re.I)),
	("Inadmissibility and misrepresentation", re.compile(r"inadmissib|misrepresent|section 40\b|criminality|serious criminality|security grounds", re.I)),
	("Exclusion", re.compile(r"article 1[EF]|serious non-political|crimes against humanity|complicity|shared common purpose", re.I)),
	("Spousal, family and sponsorship", re.compile(r"sponsor|bona fide|genuine(?:ly)? (?:marriage|relationship)|common[- ]law|family class|dependent child|conjugal", re.I)),
	("Work and study permits", re.compile(r"work permit|study permit|temporary resident|dual intent|ties to (?:canada|home)|purpose of (?:visit|travel)", re.I)),
	("Medical and financial inadmissibility", re.compile(r"excessive demand|medical inadmissib|financial (?:means|resources)|ability to support", re.I)),
	("Country conditions and documents", re.compile(r"documentary evidence|national documentation package|\bNDP\b|country condition|country documentation|objective evidence|human rights (?:report|problems)|medical report|psychological report", re.I)),
	("Reasons and justification", re.compile(r"adequacy of reasons|justification, transparency|intelligib|reasons? (?:are|were) (?:inadequate|insufficient)|failed to (?:consider|address|engage)|ignored (?:evidence|the)", re.I)),
	("Costs and certified question", re.compile(r"\bcosts?\b|certif(?:y|ied|ication) (?:a |the )?question|question of general importance", re.I)),
	("Jurisdiction and mootness", re.compile(r"jurisdiction|\bmoot|time limit|extension of time|leave to appeal|\bstanding\b", re.I)),
)
_PARTY_POSITIONS = re.compile(
	r"^\s*(?:\[\d+\]\s*)?(?:the |both )?(?:applicants?|respondents?|appellants?|minister|claimants?|parties)(?:(?:’|')s?)? (?:submit|argue|contend|says?|maintain|assert|rel(?:y|ies))", re.I
)

_NUMBERING_RE = re.compile(r"^\s*(?P<num>(?:[IVX]{1,5}|[A-H]|\d{1,2})[.)])\s+")
_ROMAN_RE = re.compile(r"^\s*[IVX]{1,5}[.)]\s")
_PREFIX_CLEAN_RE = re.compile(r"^\s*(?:[IVX]{1,5}|[A-H]|\d{1,2})[.)]\s+")

_UNNUMBERED_BODY_CHARS = 160
_MIN_POINT_PARAS = 3
_TOPIC_RUN = 2  # paragraphs in a row needed to start a topic sub-point
_LONG_STRETCH = 8  # numbered paragraphs without a printed heading before topics are looked for


_SECTION_REF_RE = re.compile(r"\b(?:sections?|s\.|ss\.)\s*(\d{1,3}(?:\.\d+)?)(?:\(\d+\))?", re.I)
_TOPIC_RANK = {label: n for n, (label, _p) in enumerate(_TOPICS)}


def _topic_scores(text: str) -> dict[str, int]:
	"""Subject hits in a paragraph's opening: the fixed topics above, plus the statutory section it keeps coming back to."""
	sample = text[:700]
	scores: dict[str, int] = {}
	for label, pattern in _TOPICS:
		hits = len(pattern.findall(sample))
		if hits:
			scores[label] = hits
	counts: dict[str, int] = {}
	for number in _SECTION_REF_RE.findall(text[:900]):
		counts[number] = counts.get(number, 0) + 1
	if counts:
		top = max(counts, key=counts.get)
		if counts[top] >= 2 or len(counts) == 1:
			scores[f"Section {top}"] = counts[top] + 1  # a named section outranks one passing keyword
	return scores


# --------------------------------------------------------------------------- paragraph units from blocks


def _short_heading(text: str) -> bool:
	"""A short unpunctuated title line between numbered paragraphs ("Identity", "State protection")."""
	t = text.strip()
	return 2 < len(t) <= 70 and len(t.split()) <= 8 and t[:1].isupper() and not t.endswith((".", ";", ",", ":", ")")) and not cs._NUM_PREFIX_RE.match(t)


def _units(text: str, blocks: Sequence[dict]) -> list[dict[str, Any]]:
	"""Whole paragraphs: a numbered paragraph with the unnumbered lines under it; headings and short title lines apart."""
	picked = [b for b in blocks if b.get("type") in _PICKED_TYPES and text[b["start"] : b["end"]].strip()]
	units: list[dict[str, Any]] = []
	seen_numbered = False
	numbered_doc = any(b["type"] == "para" for b in picked)
	for i, b in enumerate(picked):
		raw = text[b["start"] : b["end"]].strip()
		kind = b["type"]
		if kind == "para":
			seen_numbered = True
			units.append({"start": b["start"], "end": b["end"], "text": raw, "num": b.get("num"), "type": "para", "heading": False, "body": True})
			continue
		is_heading = kind == "heading"
		if not is_heading and kind == "text" and seen_numbered:
			prev_para = i > 0 and picked[i - 1]["type"] in {"para", "text", "listitem"}
			next_para = i + 1 < len(picked) and picked[i + 1]["type"] == "para"
			is_heading = prev_para and next_para and _short_heading(raw)
		if not numbered_doc and kind == "text":
			# decisions with no [n] numbering (older RPD reasons): a long line is a paragraph, a short title line a heading
			if len(raw) >= _UNNUMBERED_BODY_CHARS:
				units.append({"start": b["start"], "end": b["end"], "text": raw, "num": None, "type": "para", "heading": False, "body": True})
				continue
			next_long = i + 1 < len(picked) and picked[i + 1]["type"] == "text" and len(text[picked[i + 1]["start"] : picked[i + 1]["end"]].strip()) >= _UNNUMBERED_BODY_CHARS
			if _short_heading(raw) and next_long and any(u.get("body") for u in units):
				is_heading = True
		if is_heading:
			units.append({"start": b["start"], "end": b["end"], "text": raw, "num": None, "type": "heading", "heading": True, "body": False})
		elif kind in _CONTINUATION_TYPES and units and units[-1]["type"] == "para":
			units[-1]["end"] = b["end"]
			units[-1]["text"] += "\n" + raw
		else:
			units.append({"start": b["start"], "end": b["end"], "text": raw, "num": None, "type": kind, "heading": False, "body": False})
	return units


# --------------------------------------------------------------------------- sections


def _runs(values: Sequence[str]) -> list[tuple[int, int, str]]:
	runs: list[tuple[int, int, str]] = []
	for i, value in enumerate(values):
		if runs and runs[-1][2] == value:
			runs[-1] = (runs[-1][0], i, value)
		else:
			runs.append((i, i, value))
	return runs


_ORDER = {"background": 0, "issues": 1, "analysis": 2, "disposition": 3}
_SPLIT_SUBHEADING_RE = re.compile(r"\s+(?=[A-H][.)]\s+[A-Z])")


def _heading_parts(text: str) -> tuple[str, str | None]:
	"""A heading block can carry two headings run together ("IV. Analysis A. Did the Officer ..."): (main, sub)."""
	parts = _SPLIT_SUBHEADING_RE.split(" ".join(text.split()), maxsplit=1)
	return parts[0], parts[1] if len(parts) > 1 else None


_PRELIMINARY_RE = re.compile(r"^\s*(?:(?:[IVX]{1,5}|[A-H]|\d{1,2})[.)]\s+)?(?:(?:admissibility of )?new evidence|request for an oral hearing|oral hearing|role of the (?:rad|refugee appeal division)|scope of the rad review|preliminary (?:matters?|issues?))\b", re.I)


_PREFIX = r"^\s*(?:(?:[IVX]{1,5}|[A-H]|\d{1,2})[.)]\s+)?"
_ISSUES_HEAD_RE = re.compile(_PREFIX + r"(?:(?:errors|grounds|issues) (?:alleged|raised|on appeal|of appeal)|grounds of (?:appeal|review)|standard of review|errors alleged)\b", re.I)
_BELOW_HEAD_RE = re.compile(_PREFIX + r"(?:reasons|decision|judgment|findings|determination) (?:of|by) the (?!court|appeal division|board)|the decision (?:under review|under appeal|appealed from|below)|decision under (?:review|appeal)|impugned decision", re.I)
_DISP_HEAD_RE = re.compile(_PREFIX + r"(?:proposed )?disposition\b", re.I)


def _heading_section(text: str) -> str | None:
	"""The section a heading announces ("Issues", "Analysis", "Conclusion"), None for an ordinary heading.

	RAD preliminary matters (new evidence, oral hearing, role of the RAD) come before the merits, so they count as Issues.
	"""
	if _PRELIMINARY_RE.match(_heading_parts(text)[0]):
		return "issues"
	head = _heading_parts(text)[0]
	if _DISP_HEAD_RE.match(head):
		return "disposition"
	if _ISSUES_HEAD_RE.match(head):
		return "issues"
	if _BELOW_HEAD_RE.match(head):
		return "background"
	kind = cs.heading_kind(head)
	return _ROLE_SECTION.get(kind) if kind else None


def _assign_sections(units: list[dict[str, Any]]) -> list[str | None]:
	"""A section per unit (None for the header and footer), forced into Background > Issues > Analysis > Disposition order.

	Headings that name a section are the anchors; text before the first anchor, and decisions with no such heading,
	use the ordered paragraph labeller.
	"""
	texts = [u["text"] for u in units]
	roles = cs.label_paragraph_roles(texts)
	numbered = [i for i, u in enumerate(units) if u["body"]]
	if len(numbered) < 3:
		return [None] * len(units)
	first_num, last_num = numbered[0], numbered[-1]
	closing = max(6, len(numbered) // 5)

	def numbered_from(i: int) -> int:
		return sum(1 for n in numbered if n >= i)

	model: list[str | None] = [_ROLE_SECTION.get(r) for r in roles]
	for i in range(0, first_num):
		if not (units[i]["heading"] and i == first_num - 1):
			model[i] = None

	# anchors: headings naming a section, kept in order (a "Background" heading after the analysis began is just a sub-heading)
	anchors: list[tuple[int, str]] = []
	high = -1
	for i in range(max(0, first_num - 1), last_num + 2 if last_num + 1 < len(units) else len(units)):
		if i >= len(units) or not units[i]["heading"]:
			continue
		name = _heading_section(units[i]["text"])
		if name is None or _ORDER[name] < high:
			continue
		if name == "disposition" and numbered_from(i) > closing:
			continue
		anchors.append((i, name))
		high = _ORDER[name]

	section: list[str | None] = [None] * len(units)
	if anchors:
		first_anchor = anchors[0][0]
		cap = _ORDER[anchors[0][1]]
		for i in range(first_num - 1 if first_num else 0, first_anchor):
			m = model[i]
			section[i] = m if m and _ORDER[m] < cap else (None if m is None else {0: "background", 1: "issues"}.get(max(0, cap - 1), "background"))
		current = None
		pointer = 0
		for i in range(first_anchor, len(units)):
			while pointer < len(anchors) and anchors[pointer][0] <= i:
				current = anchors[pointer][1]
				pointer += 1
			section[i] = current
	# no heading names the analysis: the labeller finds where it starts and where the order is, from the last anchor on
	# (a "Role of the RAD" heading must not carry its section to the end of the decision)
	if not any(name == "analysis" for _i, name in anchors):
		pre = [i for i, name in anchors if _ORDER[name] < _ORDER["analysis"]]
		fill_from = max(pre[-1] + 1 if pre else 0, first_num - 1, 0)
		fill_to = next((i for i, name in anchors if _ORDER[name] > _ORDER["analysis"] and i >= fill_from), len(units))
		analysis_start = next(
			(i for i in range(max(first_num, fill_from), last_num + 1) if model[i] == "analysis" and any(model[j] == "analysis" for j in range(i + 1, min(i + 4, last_num + 1)))),
			None,
		)
		disp_runs = [r for r in _runs([m or "-" for m in model]) if r[2] == "disposition"]
		disposition_start = next((a for a, _b, _s in reversed(disp_runs) if a > first_num and numbered_from(a) <= closing), None)
		for i in range(fill_from, fill_to):
			m = model[i]
			if disposition_start is not None and i >= disposition_start:
				section[i] = "disposition"
			elif analysis_start is not None and i >= analysis_start:
				section[i] = "analysis"
			elif not anchors:
				section[i] = ("issues" if i > first_num else "background") if m == "disposition" else m  # a stray order cue before the analysis
	# before the analysis a section never moves backwards by a lone paragraph: facts after issues fold into issues
	high = 0
	for i in range(first_num, len(units)):
		s = section[i]
		if s is None:
			continue
		if _ORDER[s] < high:
			section[i] = next(name for name, rank in _ORDER.items() if rank == high)
		high = max(high, _ORDER[section[i] or s])
	# no analysis found: a long "issues" run (the labeller's catch-all) is the analysis
	if "analysis" not in section:
		for a, b, name in _runs([x or "-" for x in section]):
			if name == "issues" and sum(1 for i in range(a, b + 1) if units[i]["body"]) > 8:
				for i in range(a, b + 1):
					section[i] = "analysis"
	# short reasons that the labeller read as all background: the analysis starts at the first paragraph that argues
	if "analysis" not in section and len(numbered) >= 5:
		floor = numbered[min(2, len(numbered) - 1)]
		body_idx = [i for i in numbered if i >= floor and section[i] in {"background", "issues", None}]
		start = next((i for i in body_idx if len(cs._ANALYSIS_RE.findall(units[i]["text"][:900])) >= 1), None)
		if start is not None and numbered_from(start) >= 2:
			for i in range(start, last_num + 1):
				if section[i] in {"background", "issues"}:
					section[i] = "analysis"
	# no order found: the closing paragraphs that read like one (dismissed, allowed, no question certified) are the disposition
	if "disposition" not in section:
		tail = [i for i in numbered if i >= last_num - 2]
		cut = None
		for i in reversed(tail):
			t = units[i]["text"]
			if cs._DISPOSITION_RE.search(t[:900]) or (len(t) < 400 and re.search(r"\bcertif|\bcosts?\b", t, re.I)):
				cut = i
			else:
				break
		if cut is not None and (cut > first_num + 2):
			for i in range(cut, last_num + 1):
				section[i] = "disposition"
	# no Issues section: the opening paragraphs of the analysis that state the issues or the standard of review are the Issues
	if "issues" not in section and "analysis" in section:
		start = section.index("analysis")
		taken = 0
		for i in range(start, last_num + 1):
			if not units[i]["body"]:
				continue
			t = units[i]["text"][:900]
			if section[i] == "analysis" and cs._ISSUES_RE.search(t) and len(cs._ANALYSIS_RE.findall(t)) < 2 and taken < 3:
				section[i] = "issues"
				taken += 1
			else:
				break
		if taken and any(section[j] == "background" for j in range(start)):
			pass
	# a bare order block ("JUDGMENT ... is dismissed") with numbered closing paragraphs before it: those paragraphs are the disposition
	if "disposition" in section and not any(units[i]["body"] and section[i] == "disposition" for i in range(len(units))):
		cut = None
		for i in reversed([j for j in numbered if j > first_num][-3:]):
			t = units[i]["text"]
			if roles[i] == "disposition" or cs._DISPOSITION_RE.search(t[:900]) or (len(t) < 400 and re.search(r"\bcertif|\bcosts?\b", t, re.I)):
				cut = i
			else:
				break
		if cut is not None:
			for i in range(cut, last_num + 1):
				section[i] = "disposition"
	# a heading that announces the disposition keeps the short unnumbered order printed under it
	kept_tail = set()
	for i, name in anchors:
		if name == "disposition" and i > last_num:
			kept_tail.update(j for j in range(i, min(i + 4, len(units))) if len(units[j]["text"]) < 600)
	# after the last numbered paragraph only the order itself is kept (not counsel lists, signatures or file numbers)
	for i in range(last_num + 1, len(units)):
		if units[i]["type"] in {"footer", "signature", "meta"} or section[i] != "disposition":
			section[i] = None
		elif roles[i] != "disposition" and not (i in kept_tail):
			section[i] = None
	return section


def _fold_thin_sections(units: list[dict[str, Any]], section: list[str | None]) -> None:
	"""A pre-analysis section with fewer than two numbered paragraphs that sits between two others folds into the earlier one."""
	runs = [r for r in _runs([s or "-" for s in section]) if r[2] != "-"]
	for idx in range(1, len(runs)):
		a, b, name = runs[idx]
		if name in {"analysis", "disposition"}:
			continue
		count = sum(1 for i in range(a, b + 1) if units[i]["body"])
		if count < 2 and not any(units[i]["body"] and cs._ISSUES_RE.search(units[i]["text"][:900]) for i in range(a, b + 1)):
			previous = runs[idx - 1][2]
			for i in range(a, b + 1):
				section[i] = previous


# --------------------------------------------------------------------------- sub-points


def _heading_title(text: str) -> str:
	"""The heading as printed, without a roman or letter prefix ("A. Credibility" -> "Credibility"); issue numbers stay."""
	title = re.sub(r"^(?:[IVX]{1,5}|[A-H])[.)]\s+", "", " ".join(text.split()))
	return title if len(title) <= 90 else title[:88].rsplit(" ", 1)[0] + "…"


def _heading_rank(text: str) -> int:
	"""2 for a top heading (roman numeral, upper case, unnumbered), 3 for a sub-heading (A., 1.)."""
	t = text.strip()
	if _ROMAN_RE.match(t):
		return 2
	if _NUMBERING_RE.match(t):
		return 3
	return 2


def _opener_title(text: str) -> str | None:
	body = cs._strip_number(text.strip())[1].strip()
	match = re.match(r"(?:i (?:now |will now |will first |first )?turn(?:ing)? (?:(?:now|first) )?to|turning (?:now )?to)\s+(?:the |whether |my )?(.{6,80}?)(?:[.,;:]|$)", body, re.I)
	if match:
		return match.group(1).strip().capitalize()
	match = re.match(r"((?:the )?(?:first|second|third|fourth|fifth|final|next|remaining)\b[^.,;:]{0,60}?\b(?:issue|ground|argument|question|error|challenge|submission)s?\b)", body, re.I)
	if match:
		return match.group(1).strip().capitalize()
	return None


_NOISE_HEADING_RE = re.compile(r"^\s*(?:(?:IMM|[TA])-\d|(?:division|section|part|subdivision|chapter|schedule|article|rule)\s+\d+\s*$)", re.I)


def _heading_point(unit: dict[str, Any], *, opens_section: bool) -> dict[str, Any] | None:
	"""The sub-point a heading makes, or None when the heading is just the section's own title (a sub-heading run into it counts)."""
	main, sub = _heading_parts(unit["text"])
	if _NOISE_HEADING_RE.match(unit["text"]):
		return None  # file numbers and quoted statute headings ("DIVISION 3") are not the court's own headings
	if re.match(r"\s*Q\.\s", unit["text"]):
		return None  # a transcript question quoted in the reasons
	generic = _heading_section(unit["text"])
	if generic == "issues" and re.sub(r"^(?:[IVX]{1,5}|[A-H]|\d{1,2})[.)]\s+", "", _heading_parts(unit["text"])[0]).strip().lower() in {"issue", "issues", "the issues", "the issue"}:
		generic = "issues-title"
	if generic == "issues-title":
		return None
	if opens_section and generic:
		return {"title": _heading_title(sub), "level": 3 if _ROMAN_RE.match(main) else 2, "source": "heading"} if sub else None
	if generic and generic != "issues":
		return None  # "I. Background" inside Background, "JUDGMENT" inside the Disposition: the section's own title again
	return {"title": _heading_title(main), "level": _heading_rank(main), "source": "heading"}


def _topic_in_title(topic: str, title: str) -> bool:
	"""True when a heading already names the topic ("IFA" for "Internal flight alternative"; "Section 10" for "Section 10 ...")."""
	if topic.startswith("Section "):
		return topic.lower() in title.lower()
	pattern = next((p for label, p in _TOPICS if label == topic), None)
	return bool(pattern and pattern.search(title))


def _analysis_points(units: list[dict[str, Any]], indices: list[int]) -> list[dict[str, Any]]:
	"""Sub-point starts inside the analysis: printed headings first, then openers and subject changes where headings are missing."""
	points: dict[int, dict[str, Any]] = {}
	for i in indices:
		if units[i]["heading"]:
			made = _heading_point(units[i], opens_section=i == indices[0])
			if made:
				points[i] = made
	# stretches between headings that run long get topic / opener points
	boundaries = [indices[0] - 1] + sorted(points) + [indices[-1] + 1]
	for lo, hi in zip(boundaries, boundaries[1:]):
		stretch = [i for i in indices if lo < i < hi and units[i]["body"]]
		if len(stretch) < _LONG_STRETCH:
			continue
		last_title = None
		since = 0
		scores = {i: _topic_scores(units[i]["text"]) for i in stretch}
		for pos, i in enumerate(stretch):
			since += 1
			opener = _opener_title(units[i]["text"]) if since >= _MIN_POINT_PARAS else None
			if opener:
				points[i] = {"title": opener, "level": 2 if lo < 0 or lo not in points else min(3, points[lo]["level"] + 1), "source": "opener"}
				since, last_title = 0, None
				continue
			if since < _MIN_POINT_PARAS:
				continue
			# a topic starts a point when it leads this paragraph and the next one, and differs from the running topic
			nxt = scores.get(stretch[pos + 1]) if pos + 1 < len(stretch) else None
			cur = scores[i]
			if not cur or not nxt:
				continue
			shared = [t for t in cur if t in nxt and (cur[t] + nxt[t] >= 3 or t.startswith('Section '))]
			if not shared:
				continue
			topic = max(shared, key=lambda t: (cur[t] + nxt[t], -_TOPIC_RANK.get(t, 99)))
			parent = points.get(lo)
			if parent and (_topic_in_title(topic, parent["title"])):
				continue
			if topic != last_title:
				points[i] = {"title": topic, "level": 2 if lo not in points else min(3, points[lo]["level"] + 1), "source": "topic"}
				last_title, since = topic, 0
		# the opening topic of the stretch, so the first sub-point is named too
		if stretch and stretch[0] not in points:
			first_scores = scores[stretch[0]]
			opening = max(first_scores, key=first_scores.get) if first_scores else None
			if opening and lo not in points and (stretch[1:2] and opening in scores.get(stretch[1], {})):
				points[stretch[0]] = {"title": opening, "level": 2 if lo not in points else min(3, points[lo]["level"] + 1), "source": "topic"}
	ordered = sorted(points.items())
	kept: list[tuple[int, dict[str, Any]]] = []
	for i, p in ordered:
		# a topic that repeats the sub-point just before it (same words as a heading, or the same topic again) adds nothing
		if kept and p["source"] != "heading" and kept[-1][1]["title"].strip().lower() == p["title"].strip().lower():
			continue
		kept.append((i, p))
	return [{"unit": i, **p} for i, p in kept]


# --------------------------------------------------------------------------- outline


_CACHE: "OrderedDict[tuple, list[dict]]" = OrderedDict()
_CACHE_SIZE = 256


def _number_range(units: Sequence[dict[str, Any]]) -> tuple[int | None, int | None]:
	"""First and last printed paragraph number, ignoring numbers that run backwards (a quoted or restarted numbering)."""
	first = last = None
	for u in units:
		n = u.get("num")
		if n is None or not u["body"]:
			continue
		if first is None:
			first = last = n
		elif last <= n <= last + 12:  # a far jump is a quoted paragraph number, not the next paragraph
			last = n
	return first, last


def outline_v2(text: str | None, blocks: Sequence[dict]) -> list[dict]:
	"""Outline rows for the reader. ``[]`` when the decision is too short or has too few numbered paragraphs to label.

	Labelling a long decision takes a fifth of a second, so repeat opens reuse the rows.
	"""
	if not text:
		return []
	key = (hash(text), len(text), tuple((b.get("type"), b.get("start"), b.get("end")) for b in blocks), os.getenv("ILIT_LEARNED_ROLES", ""))
	hit = _CACHE.get(key)
	if hit is None:
		hit = _outline_v2_uncached(text, blocks)
		_CACHE[key] = hit
		if len(_CACHE) > _CACHE_SIZE:
			_CACHE.popitem(last=False)
	else:
		_CACHE.move_to_end(key)
	return [dict(row) for row in hit]


_INLINE_NOTE_RE = re.compile(r"(?<![\d\[])\b\d{1,3} (?:Exhibit|Ibid|[Ss]upra)\b")
_FOOTNOTE_LINE_RE = re.compile(r"(?m)^(\d{1,3})[ \t]+\S")


def footnote_start(text: str, after: int) -> int | None:
	"""Offset where the notes printed after the reasons begin ("1 Exhibit 3 ...", "2 Ibid."), found as a 1, 2, ... run."""
	lines = [(m.start(), int(m.group(1))) for m in _FOOTNOTE_LINE_RE.finditer(text, after)]
	for i, (offset, number) in enumerate(lines):
		if number == 1 and (i + 1 == len(lines) or lines[i + 1][1] == 2):
			return offset
	# notes run together on one line ("19 Exhibit 3, item 2.4. 20 Ibid. 21 Ibid. ...")
	for match in re.finditer(r"(?m)^.+$", text[after:]):
		if len(_INLINE_NOTE_RE.findall(match.group(0))) >= 3:
			return after + match.start()
	return None


def footnote_markers(text: str, start: int) -> list[tuple[int, int, int | None]]:
	"""(note number, note offset, offset of its marker in the reasons) for each note after ``start``."""
	notes: list[tuple[int, int]] = []
	expected = 1
	for match in _FOOTNOTE_LINE_RE.finditer(text, start):
		if int(match.group(1)) == expected:
			notes.append((expected, match.start()))
			expected += 1
	out: list[tuple[int, int, int | None]] = []
	cursor = 0
	for number, offset in notes:
		found = re.compile(rf"(?<=[^\d\s\[])(?<!\d){number}(?!\d)(?=[\s.,;)]|$)").search(text, cursor, start)
		out.append((number, offset, found.start() if found else None))
		if found:
			cursor = found.end()
	return out


def _outline_v2_uncached(text: str, blocks: Sequence[dict]) -> list[dict]:
	units = _units(text, blocks)
	if sum(1 for u in units if u["body"]) < 4:
		return []
	last_numbered = [u for u in units if u["num"] is not None]
	# notes can be glued to the last numbered paragraph as unnumbered lines, so look from that paragraph's second line on
	last_body = (last_numbered[-1]["start"] + len(last_numbered[-1]["text"].split("\n", 1)[0]) + 1) if last_numbered else 0
	notes_at = footnote_start(text, last_body) if last_body else None
	if notes_at is not None:
		units = [u for u in units if u["start"] < notes_at]
		for u in units:
			if u["end"] > notes_at:  # notes glued to the last paragraph
				u["end"] = notes_at
				u["text"] = text[u["start"] : notes_at].strip()
	section = _assign_sections(units)
	_fold_thin_sections(units, section)
	if not any(u["num"] is not None for u in units):
		# no [n] numbering: only trust the result when the analysis and one other section were found
		found = {s for s in section if s}
		if "analysis" not in found or len(found) < 3:
			return []
	rows: list[dict] = []
	for a, b, name in [r for r in _runs([s or "-" for s in section]) if r[2] != "-"]:
		members = units[a : b + 1]
		numbered = [u for u in members if u["body"]]
		if not numbered and (name != "disposition" or any(r["section"] == "disposition" for r in rows)):
			continue
		rows.append(
			{
				"title": SECTION_TITLES[name],
				"role": _SECTION_ROLE[name],
				"section": name,
				"start": members[0]["start"],
				"end": members[-1]["end"],
				"para": _number_range(numbered)[0],
				"para_end": _number_range(numbered)[1],
				"count": len(numbered),
				"level": 1,
				"kind": "section",
			}
		)
		# the decision's own headings become sub-points in any section; analysis also gets topic / opener points
		indices = list(range(a, b + 1))
		if name == "analysis":
			starts = _analysis_points(units, indices)
		else:
			starts = []
			for i in indices:
				made = _heading_point(units[i], opens_section=i == a) if units[i]["heading"] else None
				if made:
					starts.append({"unit": i, **made})
		starts = _drop_thin_points(units, starts, b, name)
		for n, point in enumerate(starts):
			first = point["unit"]
			stop = (starts[n + 1]["unit"] if n + 1 < len(starts) else b + 1) - 1
			span = units[first : stop + 1]
			nums = [u for u in span if u["body"]]
			rows.append(
				{
					"title": point["title"],
					"role": _SECTION_ROLE[name],
					"section": name,
					"start": span[0]["start"],
					"end": span[-1]["end"],
					"para": _number_range(nums)[0],
					"para_end": _number_range(nums)[1],
					"count": len(nums),
					"level": point["level"],
					"kind": "point",
					"source": point["source"],
				}
			)
	_normalise_levels(rows)
	_clamp_section_ranges(rows)
	return rows


def _clamp_section_ranges(rows: list[dict]) -> None:
	"""Top-level sections never overlap: a section's last paragraph stays below the next section's first."""
	tops = [r for r in rows if r["kind"] == "section"]
	for a, b in zip(tops, tops[1:]):
		if a["para_end"] is not None and b["para"] is not None and a["para_end"] >= b["para"]:
			a["para_end"] = max(a["para"] or 0, b["para"] - 1)
			if a["para"] is not None and a["para"] > a["para_end"]:
				a["para"] = a["para_end"]
	for r in rows:
		if r["kind"] == "point" and r["para_end"] is not None and r["para"] is not None and r["para_end"] < r["para"]:
			r["para_end"] = r["para"]


def _drop_thin_points(units: list[dict[str, Any]], starts: list[dict[str, Any]], end: int, section: str) -> list[dict[str, Any]]:
	"""Topic and opener points under three paragraphs are noise; headings with no paragraph of their own stay only in Issues."""
	changed = True
	while changed:
		changed = False
		for n, point in enumerate(starts):
			stop = starts[n + 1]["unit"] if n + 1 < len(starts) else end + 1
			body = sum(1 for u in units[point["unit"] : stop] if u["body"])
			thin = point["source"] != "heading" and body < _MIN_POINT_PARAS and n + 1 < len(starts)
			empty_heading = point["source"] == "heading" and body == 0 and (section != "issues" or units[point["unit"]]["text"][:1] not in "123456789")
			if thin or empty_heading:
				starts = starts[:n] + starts[n + 1 :]
				changed = True
				break
	return starts


def _normalise_levels(rows: list[dict]) -> None:
	"""In a section whose headings are all sub-headings (A., 1.), they are the top sub-points: level 3 becomes 2."""
	for name in _ORDER:
		points = [r for r in rows if r["section"] == name and r["kind"] == "point"]
		if points and min(r["level"] for r in points) == 3:
			for r in points:
				r["level"] -= 1


# --------------------------------------------------------------------------- where a citation sits


def section_for_offset(outline: Sequence[dict], offset: int | None) -> dict[str, str | None] | None:
	"""The section (and the narrowest sub-point) holding a character offset; None when it is in the header or footer."""
	if offset is None or not outline:
		return None
	section_row = next((r for r in outline if r.get("level") == 1 and r["start"] <= offset <= r["end"]), None)
	if section_row is None:
		return None
	point = None
	for row in outline:
		if row.get("kind") == "point" and row["section"] == section_row["section"] and row["start"] <= offset <= row["end"]:
			if point is None or row["level"] >= point["level"]:
				point = row
	return {"section": section_row["section"], "section_title": section_row["title"], "point": point["title"] if point else None}


def tag_citation_sections(citations: Sequence[Any], outline: Sequence[dict], offset_of, text: str | None = None) -> None:
	"""Set ``section``, ``section_title`` and ``section_point`` on each citation row (dicts or objects) from its offset.

	With ``text``, a citation printed in the notes after the reasons takes the section of its note's marker.
	"""
	notes: list[tuple[int, int, int | None]] = []
	notes_start = None
	if text and outline:
		notes_start = footnote_start(text, max(r["end"] for r in outline))
		if notes_start is not None:
			notes = footnote_markers(text, notes_start)
	for row in citations:
		offset = offset_of(row)
		if notes and offset is not None and offset >= notes_start:
			holder = None
			for number, note_offset, marker in notes:
				if note_offset <= offset:
					holder = marker
			offset = holder
		found = section_for_offset(outline, offset)
		for key, value in (
			("section", found["section"] if found else None),
			("section_title", found["section_title"] if found else None),
			("section_point", found["point"] if found else None),
		):
			if isinstance(row, dict):
				row[key] = value
			else:
				setattr(row, key, value)


def citation_offset(row: Any) -> int | None:
	"""Character offset of a citation in the decision text: the paragraph-layer span when mapped, else its own offset."""
	spans = row.get("layer_spans") if isinstance(row, dict) else getattr(row, "layer_spans", None)
	if spans:
		for layer in ("paragraph", *spans):
			span = spans.get(layer)
			if span and span.get("absolute_start") is not None:
				return span["absolute_start"]
	chunk_id = row.get("chunk_id") if isinstance(row, dict) else getattr(row, "chunk_id", None)
	start = row.get("offset_start") if isinstance(row, dict) else getattr(row, "offset_start", None)
	return start if chunk_id is None else None

