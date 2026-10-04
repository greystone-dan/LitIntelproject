"""Pure, conservative experimental rules over exact paragraph citation spans.

These are unreviewed evidence events, never permanent labels on decisions.
No persistence, target resolution, model calls, or runtime teacher artifacts.
"""

import re
from collections import defaultdict
from itertools import pairwise
from typing import Any

VERSION = "citation-treatment-rules-v1"
CLASSES = (
    "followed_applied", "distinguished", "criticised_not_followed",
    "considered_neutral", "unknown",
)

# More specific negative forms precede their positive substrings.
RULES = tuple(
    (rule_id, label, re.compile(pattern, re.IGNORECASE))
    for rule_id, label, pattern in (
        ("not-follow", "criticised_not_followed",
         (r"\b(?:(?:do|does|did)\s+not\s+(?:follow|apply|accept)|"
          r"cannot(?:\s+possibly)?\s+follow|(?:decline|declines|refuse|refuses)\s+to\s+(?:follow|apply))\b")),
        ("not-distinguishable", "followed_applied", r"\bnot distinguishable\b"),
        # Past cues are deliberately separate, with a direct judicial subject
        # required below; do not broaden every rule to historical narration.
        ("past-not-follow", "criticised_not_followed", r"\bdeclined to follow\b"),
        ("past-criticism", "criticised_not_followed", r"\bcriticised\b"),
        ("past-distinguish", "distinguished", r"\bdistinguished\b"),
        ("past-follow-apply", "followed_applied", r"\b(?:followed|applied)\b"),
        ("criticism", "criticised_not_followed",
         r"\b(?:critic(?:ise|ize)s?|question|questions|unsound|problematic)\b"),
        ("distinguish", "distinguished", r"\b(?:distinguish|distinguishes|distinguishable)\b"),
        ("follow-apply", "followed_applied",
         (r"\b(?:follow|follows|following|apply|applies|adopt|adopts|"
          r"rely(?:\s+directly)?\s+on|governs|am bound by|must follow)\b")),
        ("consider", "considered_neutral",
         (r"\b(?:consider|considers|discuss|discusses|note|notes|mention|mentions|"
          r"refer to|reference is made to|examines|address|provides relevant context)\b")),
    )
)
_ACTOR = re.compile(r"\b(?:I|we|this court|the court|this case)\b", re.IGNORECASE)
_ATTRIBUTION = re.compile(
    r"\b(?:applicant|appellant|respondent|minister|counsel|party|parties|"
    r"prior court|lower court|superior court|another court|court [A-Z]|judge|justice|tribunal|board|"
    r"historically|previously|historical|prior decision|earlier decision)\b|"
    r"\b(?:he|she|they)\s+(?:said|says|argued|submitted|held|wrote)\b|"
    r"\b(?:said|says|stated|states|wrote|writes|held|holds|argued|submits|submitted|"
    r"recall|recount|report|reports)\s*(?:that|:)",
    re.IGNORECASE,
)
_HYPOTHETICAL = re.compile(r"\b(?:if|would|could|might|may|can be|should|were to)\b", re.IGNORECASE)
_NEGATION = re.compile(r"\b(?:not|never|no|neither|without|cannot|can't|don't|doesn't|didn't)\b", re.IGNORECASE)
_POST_CUE_NEGATION = re.compile(r"\b(?:not|never|no|neither|nothing)\b", re.IGNORECASE)
_CLAUSE = re.compile(
    r";|\b(?:but|whereas|while|however|yet|unlike)\b|"
    r"\band\s+(?=(?:I\s+|we\s+)?(?:apply|follow|distinguish|consider|decline|refuse|criticise|question)\b)",
    re.IGNORECASE,
)
_NEUTRAL_CITE = re.compile(r"\b\d{4}\s+(?:FC|FCA|SCC|CanLII|ONCA|BCCA)\s+\d+\b", re.IGNORECASE)
_BRIDGE = re.compile(
    r"\s*(?:(?:the\s+)?(?:reasoning|principle|approach|analysis|holding|authority)"
    r"\s+(?:in|of|offered in|established in|laid down in)|"
    r"whether|both|is|in|of|from)?\s*", re.IGNORECASE,
)


def _bound_to_authority(text, phrase_start, phrase_end, citation):
    """Require a narrow grammatical bridge, not a cue anywhere in the clause."""
    if phrase_end <= citation["start"]:
        bridge = text[phrase_end:citation["start"]]
    elif citation["end"] <= phrase_start:
        bridge = text[citation["end"]:phrase_start]
    else:
        return False
    return _BRIDGE.fullmatch(bridge) is not None


def _bound_actor(clause, phrase_start, citation, base, inherited):
    actors = [actor for actor in _ACTOR.finditer(clause) if actor.end() <= phrase_start]
    if actors:
        actor = actors[-1]
        bridge = clause[actor.end():phrase_start]
        a, b = citation["start"] - base - actor.end(), citation["end"] - base - actor.end()
        if 0 <= a < b <= len(bridge):
            bridge = bridge[:a] + bridge[b:]
        if re.match(r"(?:problematic|unsound)\b", clause[phrase_start:], re.IGNORECASE):
            return re.fullmatch(r"\s*(?:find(?:\s+the reasoning of)?|consider)\s*", bridge, re.IGNORECASE) is not None
        return re.fullmatch(r"\s*(?:find(?:\s+the reasoning of)?|must)?\s*", bridge, re.IGNORECASE) is not None
    if inherited and not _ACTOR.search(clause):
        return not clause[:phrase_start].strip(" \t\n,")
    # Explicit judicial gerund: "Following A, I conclude ..." (not another actor).
    return (not clause[:phrase_start].strip()
            and re.match(r"following\b", clause[phrase_start:], re.IGNORECASE) is not None
            and re.search(r"\bI conclude\b", clause, re.IGNORECASE) is not None)


def unknown_event(citation: dict[str, Any], reason: str) -> dict[str, Any]:
    return {
        "citation_id": citation.get("citation_id"),
        "target_case_id": citation.get("target_case_id"),
        "citation_text": citation.get("citation_text", ""),
        "citation_start": citation.get("start"),
        "citation_end": citation.get("end"),
        "class": "unknown", "rule_id": "abstain", "matched_phrase": "",
        "phrase_start": None, "phrase_end": None,
        "how_assigned": f'rule_id=abstain | phrase="" | reason={reason}',
        "reason": reason, "method": VERSION, "review_status": "unreviewed",
    }


def _ranges(text: str, delimiter: re.Pattern) -> list[tuple[int, int]]:
    boundaries = [0] + [match.end() for match in delimiter.finditer(text)] + [len(text)]
    return list(pairwise(boundaries))


def classify_paragraph(text: str, citations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return all observed rule events per occurrence, or an explicit abstention.

    Citation and phrase spans are paragraph-local Unicode code-point [start,end).
    Callers must supply *all* authorities in the paragraph, not only the target.
    Multi-authority clauses and implicit pronoun references deliberately abstain.
    """
    valid = []
    result = []
    for citation in citations:
        start, end = citation.get("start"), citation.get("end")
        if (not isinstance(start, int) or not isinstance(end, int)
                or not 0 <= start < end <= len(text)
                or text[start:end] != citation.get("citation_text")):
            result.append(unknown_event(citation, "invalid_citation_span"))
        else:
            valid.append(citation)
    # Mask citations/abbreviations for boundaries without changing code-point offsets.
    masked = list(text)
    for citation in valid:
        masked[citation["start"]:citation["end"]] = "x" * (citation["end"] - citation["start"])
    for abbreviation in re.finditer(r"\b(?:v|para|paras|J)\.", text):
        masked[abbreviation.end() - 1] = "x"
    sentences = _ranges("".join(masked), re.compile(r"""[.!?]["”’']?(?=\s|$)"""))
    quotes = list(re.finditer(r'"[^"]*"|“[^”]*”|‘[^’]*’|(?<!\w)\'[^\']*\'(?!\w)', text))
    # Unbalanced opening quotes also block the remainder rather than leaking cues.
    covered = {i for quote in quotes for i in range(quote.start(), quote.end())}
    for i, char in enumerate(text):
        opening_single = char == "'" and (i == 0 or not text[i - 1].isalnum())
        if (char in '"“‘' or opening_single) and i not in covered:
            covered.update(range(i, len(text)))
    for sentence_start, sentence_end in sentences:
        sentence = text[sentence_start:sentence_end]
        for local_start, local_end in _ranges(sentence, _CLAUSE):
            start, end = sentence_start + local_start, sentence_start + local_end
            scoped = [c for c in valid if start <= c["start"] < c["end"] <= end]
            if not scoped:
                continue
            clause = text[start:end]
            prefix = text[sentence_start:start]
            governing = prefix.rsplit(";", 1)[-1]
            reason = None
            if len(scoped) != 1 or len(list(_NEUTRAL_CITE.finditer(clause))) > 1:
                reason = "multiple_authorities_in_clause"
            elif any(i in covered for i in range(start, end)):
                reason = "quoted_or_uncertain_speaker"
            elif _ATTRIBUTION.search(clause) or _ATTRIBUTION.search(governing):
                reason = "party_or_historical_attribution"
            elif _HYPOTHETICAL.search(clause) or _HYPOTHETICAL.search(governing):
                reason = "hypothetical_or_modal_scope"
            elif re.search(r"\band\s*$", prefix, re.IGNORECASE) and _NEGATION.search(governing):
                reason = "governing_negation_in_coordination"
            if reason:
                result.extend(unknown_event(c, reason) for c in scoped)
                continue
            citation = scoped[0]
            # An explicit subject can carry through a contrasting clause, but
            # never through a sentence or semicolon/party narrative.
            inherited = (
                ";" not in prefix and not _ATTRIBUTION.search(prefix) and _ACTOR.search(prefix)
            )
            matches = []
            occupied = []
            for rule_id, label, pattern in RULES:
                for match in pattern.finditer(clause):
                    a, b = match.span()
                    if any(a < y and b > x for x, y in occupied):
                        continue
                    # Do not treat cue words inside the authority name as evidence.
                    if start + a < citation["end"] and start + b > citation["start"]:
                        continue
                    if not _bound_to_authority(text, start + a, start + b, citation):
                        continue
                    negations = list(_NEGATION.finditer(clause[:b]))
                    if rule_id in ("not-follow", "not-distinguishable"):
                        required = 1 if re.search(r"\bnot\b|\bcannot\b", match.group(), re.IGNORECASE) else 0
                        if len(negations) != required:
                            continue
                    elif negations:
                        continue
                    # A predicate may deny applicability after its cue (e.g.
                    # "A governs neither ..."). Keep this within the clause;
                    # supported negation inside a rule phrase stays intact.
                    if _POST_CUE_NEGATION.search(clause[b:]):
                        continue
                    if rule_id.startswith("past-") and not re.search(
                        r"\b(?:I|we|this court|the court)\s*$", clause[:a], re.IGNORECASE
                    ):
                        continue
                    if rule_id == "not-distinguishable" and not re.search(r"\b(?:I|we|this court)\s+find\b", clause, re.IGNORECASE):
                        continue
                    if not _bound_actor(clause, a, citation, start, inherited):
                        if _ACTOR.search(clause):
                            continue
                        # Narrow current declarative formulas, not past/passive narration.
                        declarative = (
                            (rule_id == "distinguish" and re.search(r"\bis distinguishable\b|"
                             r"\b(?:these circumstances|the facts)\b.*\bdistinguish\b", clause, re.IGNORECASE))
                            or (rule_id == "follow-apply" and match.group().lower() == "governs")
                            or (rule_id == "criticism" and re.search(r"\breasoning\b.*\bis problematic\b", clause, re.IGNORECASE))
                            or (rule_id == "consider" and match.group().lower() in
                                ("reference is made to", "provides relevant context"))
                        )
                        if not declarative:
                            continue
                    occupied.append((a, b))
                    phrase = match.group()
                    matches.append({
                        **unknown_event(citation, ""),
                        "class": label, "rule_id": rule_id, "matched_phrase": phrase,
                        "phrase_start": start + a, "phrase_end": start + b,
                        "how_assigned": f'rule_id={rule_id} | phrase="{phrase}" | speaker=current_court',
                        "reason": None,
                    })
            result.extend(matches or [unknown_event(citation, "no_classifiable_current_court_evidence")])
    seen = {event["citation_id"] for event in result}
    result.extend(unknown_event(c, "citation_crosses_scope_boundary") for c in valid if c["citation_id"] not in seen)
    return result


def summarize_treatment(case_id: int, evidence: list[dict[str, Any]]) -> dict[str, Any]:
    """Distinct citing decisions per observed class; unknown only if none known."""
    observed = defaultdict(set)
    for event in evidence:
        if event["class"] != "unknown":
            observed[event["source_case_id"]].add(event["class"])
        else:
            observed[event["source_case_id"]]  # retain decisions without evidence
    denominator = len(observed)
    classes = {}
    for label in CLASSES:
        ids = {source_id for source_id, labels in observed.items()
               if label in labels or (label == "unknown" and not labels)}
        examples, seen = [], set()
        for event in evidence:
            key = (event["source_case_id"], event.get("paragraph_start"), event.get("paragraph_end"))
            if (event["class"] == label and event["source_case_id"] in ids
                    and event.get("paragraph_text") and key not in seen and len(examples) < 5):
                examples.append(event)
                seen.add(key)
        classes[label] = {
            "count": len(ids), "denominator": denominator,
            "percentage": round(100 * len(ids) / denominator, 2) if denominator else 0.0,
            "examples": examples,
        }
    return {
        "case_id": case_id, "status": "experimental", "experimental": True, "read_only": True,
        "method": VERSION, "total_distinct_citing_decisions": denominator,
        "counting_policy": "Each distinct citing decision counts once per observed class; "
                           "classes overlap. Unknown counts only decisions with no classifiable evidence.",
        "classes": classes, "evidence": evidence,
    }
