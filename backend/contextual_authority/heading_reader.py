"""Printed headings of a court decision, read with plain rules (no model, no database).

Federal Court reasons print their own headings ("II. Background", "ANALYSIS", "A. Did the Officer err?"). The text
keeps them as short lines between numbered paragraphs, sometimes glued onto the start of a paragraph line
("II. Analysis A. What is the standard of review? [9] The questions raised..."). ``read_headings`` finds them and gives
each one a standard name, so the outline can start its sections where the court says they start.

Measured on 1,760 Federal Court decisions (docs/FC_DECISION_STRUCTURE.md): about 96% of detected headings were real.
Quoted statute notes, hearing transcripts, tables of contents and numbered issue lists are the usual false hits and
are filtered out here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

_PARA = re.compile(r"^\[\d+\]")
_ROMAN = r"(?:X{0,2}(?:IX|IV|V?I{0,3}))"
_PREFIX = re.compile(
    r"^\s*(?:(?P<rom>(?=[IVX])" + _ROMAN + r")|(?P<let>[A-Ha-h])|(?P<dig>\d{1,2})|\((?P<par>[a-h]|[ivx]{1,4}|\d{1,2})\))\s*[.)]?\s+(?P<title>\S.*)$"
)
_LIST_ITEM = re.compile(r"^\s*(?:[A-H]|\d{1,2}|\([a-z0-9]{1,4}\)|[•·\-–])[.)]?\s+\S")
_NOISE = re.compile(
    r"(emphasis|translation|^\.\.\.$|^…$|^\[…\]$|^\[EN BLANC\]|^notes?$|^exception$|^annex"
    r"|^(between|respondents?|applicants?|judgment|federal court|cour fédérale|appearances|and)\s*:?$|^for the |\bJ\.$"
    r"|^(date|docket|present|dated|style of cause|place of hearing|date of hearing)\b|^(order|reasons).{0,30}(order|judgment)"
    r"|^judgment and reasons|^reasons (for|and) |^solicitors|^names? of counsel|^\d+ ?\(|^\((?![a-hivx0-9]{1,4}\)\s)|^page\b|^\d+$"
    r"|^by (presiding member|claimant|counsel)|^(q|a)\.?\s|^(mr|ms|mrs|mme|me)\.? [a-z]+:|examination of|\s\d{1,3}$|\(\d+ votes?\)|^paras? \d)",
    re.I,
)
_TAIL = re.compile(
    r"^((JUDGMENT|ORDER)\s+in\s+(IMM|[A-Z]-)|THIS COURT|ORDER\s*$|JUDGMENT\s*$|SOLICITORS OF RECORD|NAMES? OF COUNSEL|FEDERAL COURT\s*$|COUR FÉDÉRALE\s*$|DOCKET\s*:)",
    re.I,
)
_BOILERPLATE = re.compile(
    r"^(decision content|judgment and reasons:?|reasons for (judgment|order)[ a-z]*:?|reasons and judgment|reasons for order and order:?)$", re.I
)
_GLUED = re.compile(r"^(?P<head>[^\[]{3,300}?)\s+\[\d+\]\s")
_SPLIT = re.compile(r"\s+(?=(?:[IVX]{1,5}|[A-H]|\d{1,2})[.)]\s+[A-Z])")
_PLAIN_GLUED = re.compile(
    r"^(issues?|analysis|background|overview|introduction|facts|conclusion|standard of review|discussion|decision|issues? and .*|analysis and .*)$", re.I
)
_STATUTE_LINE = re.compile(r"^(\d+\s*)?\(\d+\)\s|^\([a-z]\)\s|^\d+\s+\(")
_ADDRESS = re.compile(r"[A-Z]\d[A-Z] ?\d[A-Z]\d\b|,\s*(Ont|Que|B\.?C|Alta|Man|Sask|N\.?S|N\.?B)\b\.?$|^(Ottawa|Toronto|Vancouver|Montreal|Calgary)\b,?\s*(Ont|Que|B\.?C|Alta)?\.?$")
_CLOSING = re.compile(r"^(costs?|certif|conclusion|disposition|order|question)", re.I)

# Standard names. Order matters: the first pattern that matches wins.
_LABELS: tuple[tuple[str, re.Pattern[str]], ...] = tuple(
    (name, re.compile(pattern, re.I))
    for name, pattern in (
        ("issues_standard", r"(issues?|questions?).{0,15}(and|&).{0,15}standards? of review|standards? of review.{0,10}(and|&).{0,10}issues?"),
        ("issues_analysis", r"^(issues?|questions?)( at issue| in issue)?( and (analysis|discussion))|^(analysis|discussion) and (issues?|decision)"),
        ("standard", r"standards? of review"),
        ("issues", r"^(the )?(issues?|questions?( at issue| in issue| to be decided| raised)?|points? in issue)\b|^(the )?(following )?issues?\b"),
        ("overview", r"^(aperçu|introduction|contexte)|^(overview|nature of the (matter|application|proceeding|case|motion)|summary|synopsis|preliminary (statement|remarks)|the application|application|purpose of the (application|motion))\b"),
        ("background", r"^(the )?(background|facts|factual (background|context|matrix)|relevant facts|procedural (history|background)|history|context|chronology|summary of (the )?facts|background facts|statement of facts|the proceedings?|proceedings? below)"),
        ("decision_under_review", r"(decision|reasons?|determination|finding|ruling)s? (under review|challenged|at issue|impugned|being reviewed|of the (board|rpd|rad|iad|officer|delegate|minister|member|visa officer|citizenship judge|panel|tribunal|[a-z ]{0,25}(court|judge|justice)))|^(the )?(impugned|challenged|contested) (decision|reasons?)|^(the )?(board|rpd|rad|iad|officer|delegate|visa officer|tribunal|panel|member)[’' s]*(s )?(decision|reasons?|determination)|^decision (of|by)|^reasons of the"),
        ("legislation", r"(relevant|applicable|statutory|legislative|regulatory) (provisions?|framework|scheme|legislation|background|context)|^(statutes?|legislation|statutory provisions?|legislative scheme|the legislation|regulatory framework|the law|applicable law|legal framework|relevant law)"),
        ("submissions", r"\b(submissions?|arguments?|positions?|contentions|claims|representations)\b|^the (applicants?|respondents?|appellants?|minister|plaintiffs?|defendants?)$|^(applicants?|respondents?)[’' s]*$|^reply"),
        ("certified_question", r"certif(ied|ication)|question for certification|serious question|proposed question"),
        ("costs", r"^costs?\b|costs and|and costs|^remedy|^relief|^orders?$|^judgment$"),
        ("analysis", r"^(analysis|discussion|reasons?)( and (conclusions?|disposition))+$"),
        ("conclusion", r"^(conclusions?|disposition|result|outcome|final (disposition|conclusion)|summary of conclusions?|in conclusion)\b|conclusions?( and (disposition|costs|certification|order))?$|and (conclusion|disposition)$|^concluson"),
        ("analysis", r"^(analyse|discussion)|(analysis|discussion|consideration|reasoning|assessment|merits|findings|determination)\b|^(analysis|discussion|reasons)\b"),
    )
)

# The outline's four sections each standard name belongs to.
SECTION_OF = {
    "overview": "background",
    "background": "background",
    "decision_under_review": "background",
    "legislation": "issues",
    "issues": "issues",
    "standard": "issues",
    "issues_standard": "issues",
    "issues_analysis": "analysis",
    "analysis": "analysis",
    "conclusion": "disposition",
    "costs": "disposition",
    "certified_question": "disposition",
}


@dataclass(frozen=True)
class PrintedHeading:
    start: int  # character offset of the line that carries the heading
    kind: str  # roman, letter, digit, paren or plain
    numeral: str | None
    title: str
    label: str  # standard name, "question" for a question heading, "topic" for any other
    glued: bool  # printed on the same line as the start of a paragraph

    @property
    def top_level(self) -> bool:
        return self.kind in {"roman", "plain"}


def heading_label(title: str) -> str:
    """The standard name for a heading title ("Factual background" -> "background"), "question" or "topic"."""
    t = title.strip().lower().rstrip(":. ")
    if t.endswith("?") or t.startswith(("did ", "was ", "were ", "is ", "does ", "do ", "has ", "have ", "whether ", "should ", "what ", "who ", "can ", "would ", "will ")):
        return "question"
    if t in {"decision", "the decision"}:
        return "decision"  # resolved by position: before the analysis it is the decision under review, after it the conclusion
    for name, pattern in _LABELS:
        if pattern.search(t):
            return name
    return "topic"


def _roman_value(numeral: str) -> int:
    values = {"I": 1, "V": 5, "X": 10}
    total = 0
    for i, ch in enumerate(numeral):
        total += -values[ch] if i + 1 < len(numeral) and values[ch] < values[numeral[i + 1]] else values[ch]
    return total


def _is_roman(value: str | None) -> bool:
    return bool(value) and bool(re.fullmatch(_ROMAN, value))


def _form(line: str) -> tuple[str, str | None, str] | None:
    """(kind, numeral, title) when the line is shaped like a heading, else None."""
    if not line or _PARA.match(line) or len(line) > 130:
        return None
    match = _PREFIX.match(line)
    kind, numeral, body = "plain", None, line
    if match:
        body = match.group("title")
        if match.group("rom") and _is_roman(match.group("rom")):
            kind, numeral = "roman", match.group("rom")
        elif match.group("let"):
            kind, numeral = "letter", match.group("let")
        elif match.group("dig"):
            kind, numeral = "digit", match.group("dig")
        elif match.group("par"):
            kind, numeral = "paren", match.group("par")
    if _NOISE.search(body) and not (kind != "plain" and re.match(r"^(respondents?|applicants?|appellants?)$", body, re.I)):
        return None
    limit = 260 if kind in {"letter", "digit", "roman"} and body.endswith("?") else 110
    if len(body) > limit:
        return None
    if body.endswith(".") and len(body.split()) <= 4:
        body = body.rstrip(".")
    if body.rstrip().endswith((".", ",", ";")) and not body.isupper():
        return None
    if not re.match(r"^[A-Z0-9“\"]", body):
        return None
    if kind == "plain" and len(body.split()) > (26 if body.endswith("?") else 14):
        return None
    return kind, numeral, body.rstrip(":").strip()


def _body_span(lines: list[str]) -> tuple[int, int, int, int] | None:
    """(first line to read, first numbered paragraph, last numbered paragraph, end of the reasons) as line indexes."""
    numbered = [i for i, line in enumerate(lines) if _PARA.match(line)]
    if not numbered:
        return None
    first = numbered[0]
    start = 0
    for i in range(first):
        if _BOILERPLATE.match(lines[i]) or lines[i].lower().startswith("decision content"):
            start = i + 1
    end = len(lines)
    for i in range(first + 4, len(lines)):
        if _TAIL.match(lines[i]):
            end = i
            break
    inside = [i for i in numbered if i < end]
    return start, first, (inside[-1] if inside else first), end


def _glued_headings(line: str) -> list[tuple[str, str | None, str]]:
    """Headings run together at the start of a paragraph line, e.g. ``IV. Analysis A. Did the Officer err? [12] ...``."""
    match = _GLUED.match(line)
    if not match:
        return []
    parts = [p.strip() for p in _SPLIT.split(match.group("head").strip()) if p.strip()]
    found: list[tuple[str, str | None, str]] = []
    for part in parts:
        prefix = _PREFIX.match(part)
        if prefix and (prefix.group("rom") and _is_roman(prefix.group("rom")) or prefix.group("let") or prefix.group("dig")) and len(part) <= 270 and not part.endswith((".", ",", ";")):
            if prefix.group("rom"):
                found.append(("roman", prefix.group("rom"), prefix.group("title").strip()))
            elif prefix.group("let"):
                found.append(("letter", prefix.group("let"), prefix.group("title").strip()))
            else:
                found.append(("digit", prefix.group("dig"), prefix.group("title").strip()))
        elif len(parts) == 1 and _PLAIN_GLUED.match(part):
            found.append(("plain", None, part))
        else:
            return []
    return [] if found and found[0][0] == "digit" else found


def read_headings(text: str | None) -> list[PrintedHeading]:
    """Headings the court printed in the body of its reasons, in order. Empty when the text has no numbered paragraphs."""
    if not text:
        return []
    raw_lines = text.split("\n")
    lines = [line.strip() for line in raw_lines]
    offsets: list[int] = []
    position = 0
    for raw in raw_lines:
        offsets.append(position)
        position += len(raw) + 1
    span = _body_span(lines)
    if not span:
        return []
    start, first, last, end = span
    found: list[PrintedHeading] = []
    line_of: dict[int, int] = {}
    for i in range(start, end):
        line = lines[i]
        if not line:
            continue
        if not _PARA.match(line):
            glued = _glued_headings(line)
            if glued:
                for kind, numeral, title in glued:
                    found.append(PrintedHeading(offsets[i], kind, numeral, title, heading_label(title), True))
                continue
        form = _form(line)
        if not form:
            continue
        kind, numeral, title = form
        if _ADDRESS.search(title):
            continue
        nxt = i + 1
        while nxt < len(lines) and not lines[nxt]:
            nxt += 1
        following = lines[nxt] if nxt < len(lines) else ""
        # a heading is followed by a numbered paragraph, or by more headings or list lines that lead to one
        j = nxt
        reaches_paragraph = False
        while True:
            while j < len(lines) and not lines[j]:
                j += 1
            if j >= end or (j < len(lines) and _PARA.match(lines[j])):
                reaches_paragraph = True
                break
            glued_next = _glued_headings(lines[j]) if j < len(lines) else []
            if glued_next:
                reaches_paragraph = True
                break
            if _form(lines[j]) or _LIST_ITEM.match(lines[j]) or (lines[j][:1].islower() and len(lines[j]) < 200):
                j += 1
                continue
            break
        if not reaches_paragraph and kind != "roman":
            continue
        if kind in {"plain", "paren", "digit"} and _STATUTE_LINE.match(following) and len(following) > 70:
            continue
        if kind in {"plain", "paren"} and re.match(r"^\d{1,3}\.\s+\S", following) and len(following) > 70 and not _PLAIN_GLUED.match(title):
            continue
        if i < first and kind == "plain" and not _PLAIN_GLUED.match(title):
            continue
        if i > last and not _CLOSING.match(title):
            continue
        if kind == "digit":
            before = i - 1
            while before >= 0 and not lines[before]:
                before -= 1
            if before >= 0 and lines[before].rstrip().endswith(":"):
                continue  # item of a list the court introduced ("There are three issues:")
            if re.match(r"^\d{1,2}[.)]\s", following):
                continue  # one item of a numbered list
            if before >= 0 and re.match(r"^\d{1,2}[.)]\s", lines[before]):
                continue  # last item of a numbered list
        if kind == "letter":
            before = i - 1
            while before >= 0 and not lines[before]:
                before -= 1
            if before >= 0 and re.match(r"^(Q|MR\.?|MS\.?)[.:]\s", lines[before]):
                continue  # answer line of a transcript
        found.append(PrintedHeading(offsets[i], kind, numeral, title, heading_label(title), False))
        line_of[offsets[i]] = i
    # a numbered line straight under another heading is a list item, not a heading
    starts = {h.start for h in found}
    cleaned: list[PrintedHeading] = []
    for h in found:
        if h.kind == "digit" and not h.glued:
            before = line_of[h.start] - 1
            while before >= 0 and not lines[before]:
                before -= 1
            if before >= 0 and offsets[before] in starts:
                continue
        cleaned.append(h)
    return cleaned


def resolved_labels(headings: list[PrintedHeading]) -> list[str]:
    """Standard names with a bare "Decision" heading resolved by where it sits (before the analysis: the decision under review)."""
    labels: list[str] = []
    seen_analysis = False
    for h in headings:
        label = h.label
        if label == "decision":
            label = "conclusion" if seen_analysis else "decision_under_review"
        if label in {"analysis", "issues_analysis"} and h.top_level:
            seen_analysis = True
        labels.append(label)
    return labels
