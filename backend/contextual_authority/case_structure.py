"""Case structure: label every paragraph of a decision with its structural role (no AI).

First step here is only the paragraph splitter used for decisions that do not come from
stored CaseChunk rows (evaluation texts). The labeller is added below.
"""

from __future__ import annotations

import re

_NUMBERED_RE = re.compile(r"^\s*\[\d+\]")


def split_decision_text(text: str) -> list[str]:
    """Split a decision's full text into paragraphs like the stored paragraph chunks.

    Everything before the ``Decision Content`` line is one metadata paragraph; after it,
    each non-empty line is a paragraph, except that the cover block (style of cause,
    parties, "REASONS FOR ...") before the first ``[1]`` is kept as a single paragraph
    when the decision uses numbered paragraphs.
    """
    lines = [line.strip() for line in text.replace("\r", "").split("\n")]
    paragraphs: list[str] = []
    try:
        marker = next(i for i, line in enumerate(lines) if line == "Decision Content")
    except StopIteration:
        marker = -1
    if marker >= 0:
        paragraphs.append("\n".join(line for line in lines[: marker + 1] if line))
        lines = lines[marker + 1 :]
    body = [line for line in lines if line]
    first_numbered = next((i for i, line in enumerate(body) if _NUMBERED_RE.match(line)), None)
    if first_numbered:
        paragraphs.append("\n".join(body[:first_numbered]))
        body = body[first_numbered:]
    paragraphs.extend(body)
    return paragraphs


# --------------------------------------------------------------------------- structural roles
#
# A decision has a fixed skeleton: header and cover block, an overview, the facts and the
# decision under review, the issues (with governing law and standard of review), the
# court's analysis, the disposition, and a footer (signature, counsel, solicitors).
# Every paragraph is scored for each of those six roles from deterministic cues, then the
# best path that keeps the skeleton in order is chosen (Viterbi). Units are the runs of
# one role, plus a split at each major heading inside the analysis.

from typing import Sequence

ROLES = ("metadata", "overview", "facts", "issues", "analysis", "disposition")

# states: header metadata, then the roles in order, then footer metadata
_STATES = ("head", "overview", "facts", "issues", "analysis", "disposition", "foot")
_STATE_ROLE = {"head": "metadata", "foot": "metadata"}

_NUM_PREFIX_RE = re.compile(r"^\s*(?:\[(\d+)\]|(\d{1,3})(?=\s+[A-Z“\"(]))\s*")
_HEADING_PREFIX_RE = re.compile(r"^\s*((?:[IVX]{1,5}|[A-H]|\d{1,2})[.)]\s+)?(?P<title>[A-Z][^\n\[\]]{2,90}?)\s*(?:\[\d+\]|$)")
_MAJOR_HEADING_RE = re.compile(r"^\s*(?:[IVX]{1,5}|[A-H])[.)]\s+[A-Z]")
_LEAD_HEADING_RE = re.compile(r"^\s*(?P<head>(?:[IVX]{1,5}|[A-H])[.)]\s+[A-Z][A-Za-z ,’'&\-:/()]{2,70}?)\s+\[\d+\]")

_HEAD_KEYWORDS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("overview", re.compile(r"^(?:overview|introduction|nature of the (?:application|matter|proceeding|appeal|motion)|the application|summary)\b")),
    ("disposition", re.compile(r"^(?:conclusions?|disposition|judgment|order|costs|certified questions?|question[s]? (?:for|of general)|result|final (?:words|disposition))\b|^(?:orders?|judgments?) in\b")),
    ("issues", re.compile(
        r"^(?:(?:the )?issues?|preliminary (?:issue|matter)s?|standard of review|legal framework|legislat\w+|(?:relevant |applicable |statutory )+(?:legislat\w+|provisions?|framework|law)|statutory (?:framework|provisions?|scheme)|governing (?:law|principles)|analytical framework|the law)\b")),
    ("facts", re.compile(
        r"^(?:(?:the )?background|(?:the )?facts?|factual (?:background|context|matrix|overview)|(?:procedural |judicial |litigation )?history|(?:the )?decisions? (?:under review|below|at issue|of the \w+)|(?:the )?(?:impugned|challenged) decision|(?:the )?(?:rpd|rad|officer|board|tribunal)(?:’s|'s)? decisions?|lower court decisions?|decisions? of the (?:rpd|rad|officer|board|tribunal)|(?:the )?proceedings below|(?:the )?decision|facts and (?:proceedings|background)|overview of facts)\b")),
    ("analysis", re.compile(r"^(?:analysis|discussion|reasons|positions? of the parties|(?:the )?(?:parties(?:’|')? )?(?:arguments|submissions|positions)|application to the facts|(?:the )?(?:applicant|respondent|appellant|minister)(?:’s|'s)? (?:position|arguments?|submissions?))\b")),
)

_FOOT_RE = re.compile(
    r"SOLICITORS OF RECORD|NAMES OF COUNSEL|STYLE OF CAUSE|PLACE OF HEARING|DATE OF HEARING|APPEARANCES|^DOCKET:?\s*$|^FEDERAL COURT( OF APPEAL)?\s*$"
    r"|(?i:^(?:Solicitors?|Counsel|Attorney General)\b[^.\n]{0,60}\b(?:for the|of Canada)|^for the (?:applicant|respondent|appellant)s?\b|^Certified true translation)"
    r"|^REASONS FOR (?:JUDGMENT|ORDER)\b.*\bBY\b|^DELIVERED FROM THE BENCH",
    re.M,
)
_SIGNATURE_RE = re.compile(r"^[\"“”']?[A-Z][\w.’' -]{2,40}[\"“”']?\s*$")
_SIGNATURE_TITLE_RE = re.compile(r"^(?:Judge|Chief Justice|(?:[A-Z]\.){1,3}[A-Z]?\.?|J\.A\.|J\.|C\.J\.?|Associate Judge|Prothonotary)\s*$")
_HEAD_BLOCK_RE = re.compile(
    r"^(?:Date|Docket|Citation|CORAM|BETWEEN|Between|File No|Neutral citation|Indexed as|Present|Court \(s\) Database|Collection|SUPREME COURT OF CANADA|REASONS FOR (?:JUDGMENT|ORDER)|ORDER AND REASONS|JUDGMENT AND REASONS|[A-Z ,.'’-]{4,40}\bJ\.A?\.?)\s*[:\n]?",
    re.M,
)
_DISPOSITION_RE = re.compile(
    r"\bTHIS COURT(?:’|')?S? (?:JUDGMENT|ORDER)\b|\bTHE COURT (?:ORDERS|THEREFORE ORDERS)\b|\bIT IS (?:HEREBY )?(?:ORDERED|ADJUDGED)\b"
    r"|\bI would (?:therefore |accordingly |also )?(?:allow|dismiss|grant|set aside|deny|quash)\b"
    r"|\b(?:this|the) (?:application|appeal|motion|judicial review|cross-appeal)\b[^.]{0,60}\b(?:is|will be|must be|should be|are)\s+(?:therefore |accordingly |hereby )?(?:allowed|dismissed|granted|denied)\b"
    r"|\b(?:application|appeal|motion)s?\s+(?:for judicial review\s+)?(?:is|are)\s+(?:therefore |accordingly )?(?:allowed|dismissed|granted|denied)\b"
    r"|\bin the result\b|\bfor (?:all )?(?:of )?(?:these|the foregoing|the above|those) reasons\b|\bno (?:serious )?question[s]?\b[^.]{0,60}\bcertif|\bcertif(?:y|ied|ication)\b[^.]{0,60}\bquestion"
    r"|^(?:Appeal|Application|Motion)s? (?:allowed|dismissed|granted)\b|\bwith costs\b"
    r"|\btherefore (?:rejects?|accepts?)\b|\b(?:rejects?|accepts?) the (?:refugee )?(?:claim|appeal)s?\b|\bis neither a convention refugee\b|\bare neither convention refugees\b|\bthat concludes my reasons\b",
    re.I,
)
_OVERVIEW_RE = re.compile(
    r"\b(?:application|motion|appeal)s? (?:for|to|under|pursuant|from|against)\b|\bjudicial review of\b|\bseek(?:s|ing)? (?:leave|judicial review|an order)\b"
    r"|\bthis (?:appeal|case|matter|motion|application|proceeding) (?:concerns|raises|is about|involves|arises)\b|\bI (?:will|would|have concluded|conclude) (?:allow|dismiss|that)\b|\bfor the reasons (?:that follow|below|set out)\b",
    re.I,
)
_ISSUES_RE = re.compile(
    r"\b(?:the|two|three|four|following|sole|only|primary|main|determinative|central|key|first|second) (?:issues?|questions?)\b[^.]{0,60}\b(?:is|are|raised?|whether|before)\b"
    r"|\braises? (?:\w+ ){0,3}(?:issues?|questions?)\b|\bfollowing (?:issues?|questions?)\b|\bproposes? the following\b|\bstandard of review\b|\bpresumption of reasonableness\b|\breviewed (?:on|against) a standard\b|\bVavilov\b[^.]{0,80}\b(?:standard|presumption)"
    r"|\bis reviewable on (?:the|a) standard\b|\bwhether\b[^.]{0,120}\?\s*$",
    re.I,
)
_FACTS_RE = re.compile(
    r"\b(?:is|was) (?:a )?(?:citizen|national|native|resident) of\b|\bwas born\b|\barrived in canada\b|\bclaimed (?:refugee )?protection\b|\bcame to canada\b"
    r"|\bin (?:january|february|march|april|may|june|july|august|september|october|november|december)(?: \d{1,2},)? (?:of )?\d{4}\b|\b(?:in|by|since|until|from) (?:19|20)\d{2}\b|\bon (?:january|february|march|april|may|june|july|august|september|october|november|december) \d{1,2}, \d{4}\b"
    r"|\balleges? (?:that|he|she|they)\b|\bclaimants? (?:is|are|was|were) (?:a |an )?(?:citizens?|nationals?)\b|\bfled (?:to|from)\b"
    r"|\b(?:the|The) (?:RAD|RPD|IAD|ID|SST|SST-GD|SST-AD|Board|officer|Officer|panel|Panel|Member|Tribunal|tribunal|delegate|decision-maker|senior immigration officer|judge|trial judge|chambers judge|Court of Appeal|adjudicator|Minister(?:’s|'s) delegate|visa officer)\b[^.]{0,60}\b(?:found|concluded|determined|held|rejected|refused|noted|commented|stated|considered|acknowledged|accepted|observed|indicated|said|wrote|explained|relied|dismissed|allowed|granted|issued|reviewed|assessed|identified|drew|gave|made|then|also)\b",
    re.I,
)
_ANALYSIS_RE = re.compile(
    r"\bI (?:find|agree|disagree|accept|reject|am (?:not )?(?:satisfied|persuaded|convinced)|do not (?:agree|accept|think|see)|cannot (?:accept|agree))\b|\bin my (?:view|opinion)\b|\bit was (?:not )?(?:un)?reasonable\b"
    r"|\bwas (?:not )?(?:un)?reasonable\b|\bthe (?:applicants?|appellants?|respondents?|minister|parties|intervener)(?:’s|'s|s’)?\s+(?:argue|submit|contend|say|maintain|assert|rely|relies|argues|submits|contends|says|maintains|asserts)\b"
    r"|\bwith respect\b|\bin (?:this|that) (?:case|regard|respect)\b|\bmoreover\b|\bhowever\b|\bI turn (?:now )?to\b|\bfirst(?:ly)?,|\bsecond(?:ly)?,|\bfinally,|\b[Rr]eading the\b",
    re.I,
)
_ORDER_START_RE = re.compile(r"(?:JUDGMENT|ORDER)\b(?:\s+IN\b|\s*$|\s*\n)|THIS COURT(?:’|')?S? (?:JUDGMENT|ORDER)|THE COURT(?:’|')?S? JUDGMENT|IT IS (?:THE JUDGMENT|ORDERED)", re.I)
_ORDER_ITEM_RE = re.compile(r"^\s*(?:\d{1,2}[.)]|[a-z][.)]|[-•])\s+\S")
_CITE_RE = re.compile(r"\b(?:\d{4} (?:SCC|FCA|FC|ONCA|BCCA|ABCA|SCR)|\[\d{4}\] \d+ [A-Z.]+ \d+|v\.\s+[A-Z])")


def _strip_number(text: str) -> tuple[int | None, str]:
    match = _NUM_PREFIX_RE.match(text)
    if not match:
        return None, text
    number = int(match.group(1) or match.group(2))
    return number, text[match.end():]


def heading_kind(text: str) -> str | None:
    """Return the structural role a heading paragraph announces, "heading" for an unknown heading, else None."""
    stripped = text.strip()
    lead = _LEAD_HEADING_RE.match(stripped)
    candidate = lead.group("head") if lead else stripped
    if len(candidate) > 100 or "\n" in candidate or _NUM_PREFIX_RE.match(candidate):
        return None
    if not lead and (candidate.endswith((".", ";", ",", ":")) or len(candidate.split()) > 12):
        return None
    match = _HEADING_PREFIX_RE.match(candidate)
    if not match:
        return None
    title = match.group("title").strip().lower().rstrip(":")
    title = re.sub(r"^(?:[ivx]{1,5}|[a-h]|\d{1,2})[.)]\s+", "", title)
    for role, pattern in _HEAD_KEYWORDS:
        if pattern.match(title):
            return role
    prefixed = bool(match.group(1)) or bool(lead)
    if prefixed or (stripped[:1].isupper() and len(stripped.split()) <= 9 and stripped == stripped.title() or stripped.isupper()):
        return "heading"
    return None


def _emissions(paragraphs: Sequence[str]) -> list[dict[str, float]]:
    n = len(paragraphs)
    numbers = [_strip_number(p)[0] for p in paragraphs]
    numbered = [i for i, v in enumerate(numbers) if v is not None]
    first_body = numbered[0] if numbered else min(n - 1, 2)
    last_numbered = numbered[-1] if numbered else n - 1
    out: list[dict[str, float]] = []
    seen_numbers = 0
    for i, text in enumerate(paragraphs):
        pos = i / max(1, n - 1)
        number, body = _strip_number(text)
        score = {state: 0.0 for state in _STATES}
        kind = heading_kind(text)
        head_len = len(text)
        if number is not None:
            seen_numbers += 1
        # header block
        if i == 0:
            score["head"] += 6
        if i < first_body:
            score["head"] += 2.5 if kind is None else 0.0
            if _HEAD_BLOCK_RE.search(text[:200]) or head_len > 600:
                score["head"] += 1.5
        # footer block
        tail = i > last_numbered
        if _FOOT_RE.match(text.lstrip()):
            score["foot"] += 4
        elif _FOOT_RE.search(text):
            score["foot"] += 1.5
        if _ORDER_START_RE.match(text.lstrip()):
            score["disposition"] += 3.5
        if tail and head_len < 60 and number is None and kind is None:
            score["foot"] += 0.8
        if tail and _ORDER_ITEM_RE.match(text):
            score["disposition"] += 2.5
        if tail and (_SIGNATURE_TITLE_RE.match(text.strip()) or (_SIGNATURE_RE.match(text.strip()) and head_len < 40)):
            score["foot"] += 2.0
        if tail:
            score["foot"] += 0.8
        # headings are strong anchors
        if kind and kind != "heading" and i >= first_body - 1 and not tail:
            score[{"overview": "overview", "facts": "facts", "issues": "issues", "analysis": "analysis", "disposition": "disposition"}[kind]] += 5
        elif kind == "heading" and i >= first_body:
            pass  # an unnamed heading keeps whatever section it sits in
        # content cues
        sample = body[:900]
        if _DISPOSITION_RE.search(sample) and pos > 0.45:
            weight = 3.0 if (pos > 0.7 or i >= last_numbered - 2) else 1.2
            score["disposition"] += weight
            if len(body) < 400:
                score["disposition"] += 0.8
        if tail and not _FOOT_RE.search(text) and head_len >= 60:
            score["disposition"] += 1.0
        if _OVERVIEW_RE.search(sample) and seen_numbers <= 3 and number is not None:
            score["overview"] += 3.0
        if number is not None and seen_numbers == 1:
            score["overview"] += 1.5
        if _ISSUES_RE.search(sample) and pos < 0.75:
            score["issues"] += 3.0
        if number is None and kind is None and first_body <= i <= last_numbered and head_len < 400 and pos < 0.5:
            score["issues"] += 1.0  # quoted statutory text and lists between numbered paragraphs
        facts_hits = len(_FACTS_RE.findall(sample))
        if facts_hits and pos < 0.75:
            score["facts"] += min(3.0, 0.8 * facts_hits)
        if sample.count("XXXX") >= 2 and pos < 0.6 and number is not None:
            score["facts"] += 0.8  # anonymised RPD decisions mask names and dates in the narrative
        analysis_hits = len(_ANALYSIS_RE.findall(sample))
        if analysis_hits:
            score["analysis"] += min(3.0, 0.9 * analysis_hits)
        if len(_CITE_RE.findall(body)) >= 2:
            score["analysis"] += 1.0
        if number is not None and 0.2 < pos < 0.92:
            score["analysis"] += 0.8
        out.append(score)
    return out


_ORDER = {state: i for i, state in enumerate(_STATES)}


def _transition_cost(prev: str, cur: str) -> float:
    if prev == cur:
        return 0.0
    a, b = _ORDER[prev], _ORDER[cur]
    if cur == "head" or prev == "foot":
        return 50.0
    if b > a:
        return 0.6 + 0.5 * (b - a - 1) if cur != "foot" else (0.8 if prev in ("analysis", "disposition") else 2.5)
    # backward moves: facts and issues swap freely, others are rare
    if {prev, cur} == {"facts", "issues"}:
        return 1.2
    if prev == "analysis" and cur in ("facts", "issues"):
        return 3.0
    if prev == "disposition":
        return 6.0
    return 4.0


def label_paragraph_roles(paragraphs: Sequence[str]) -> list[str]:
    """Label every paragraph with one of ROLES. Deterministic, no AI, reads only the text."""
    if not paragraphs:
        return []
    emissions = _emissions(paragraphs)
    n = len(paragraphs)
    best = [{s: (-emissions[0][s] if s in ("head", "overview", "facts") else 1e9, None) for s in _STATES}]
    for i in range(1, n):
        row: dict[str, tuple[float, str | None]] = {}
        for cur in _STATES:
            cost, prev_state = min(
                ((best[i - 1][prev][0] + _transition_cost(prev, cur), prev) for prev in _STATES), key=lambda item: item[0]
            )
            row[cur] = (cost - emissions[i][cur], prev_state)
        best.append(row)
    state = min(_STATES, key=lambda s: best[-1][s][0])
    path = [state]
    for i in range(n - 1, 0, -1):
        state = best[i][state][1]  # type: ignore[assignment]
        path.append(state)
    path.reverse()
    return [_STATE_ROLE.get(s, s) for s in path]


_OPENER_RE = re.compile(
    r"^(?:(?:the )?(?:first|second|third|fourth|fifth|final|next|remaining|other)\b[^.]{0,50}\b(?:issue|ground|argument|question|error|challenge|submission)s?\b"
    r"|(?:issue|ground|question)\s+(?:\d|[ivx]+\b)|i (?:now |will now |will first |first )?turn(?:ing)? (?:(?:now|first) )?to\b|turning (?:now )?to\b"
    r"|(?:next|finally|second|third),?\s+(?:i|the|we|turning)\b)",
    re.I,
)


def is_issue_opener(text: str) -> bool:
    """True when a paragraph opens the discussion of a new issue or ground ("I turn first to...")."""
    return bool(_OPENER_RE.match(_strip_number(text.strip())[1].strip()))


def structural_unit_starts(
    paragraphs: Sequence[str],
    roles: Sequence[str] | None = None,
    *,
    split_analysis_headings: bool = True,
    split_issue_openers: bool = False,
    min_unit: int = 3,
) -> list[int]:
    """Unit starts: every change of role, plus each major heading (and optionally each issue opener) inside the analysis."""
    roles = list(roles) if roles is not None else label_paragraph_roles(paragraphs)
    starts = [0] if paragraphs else []
    for i in range(1, len(paragraphs)):
        if roles[i] != roles[i - 1]:
            starts.append(i)
        elif roles[i] == "analysis":
            heading = split_analysis_headings and _MAJOR_HEADING_RE.match(paragraphs[i].strip()) and heading_kind(paragraphs[i]) is not None
            opener = split_issue_openers and i - starts[-1] >= min_unit and is_issue_opener(paragraphs[i])
            if heading or opener:
                starts.append(i)
    return starts


# --------------------------------------------------------------------------- reader outline

STRUCTURE_OUTLINE_VERSION = "case_structure_outline_v1"
_OUTLINE_BLOCK_TYPES = {"meta", "heading", "para", "text", "listitem", "footer", "signature"}
_ROLE_TITLES = {
    "metadata": "Header",
    "overview": "Overview",
    "facts": "Facts",
    "issues": "Issues",
    "analysis": "Analysis",
    "disposition": "Disposition",
}


def structure_outline(text: str | None, blocks: Sequence[dict]) -> list[dict]:
    """Outline rows for the formatted reader, built from the reader's own blocks (no AI, nothing stored).

    Each row is ``{"title", "role", "start", "para", "count", "level"}``: ``start`` is the block start
    offset the reader scrolls to, ``para`` the first numbered paragraph, ``count`` the paragraphs in the
    section. A major heading printed inside the analysis starts its own row at level 2. Header and
    footer metadata are left out. Returns ``[]`` when there is too little text to label.
    """
    if not text:
        return []
    picked = [b for b in blocks if b.get("type") in _OUTLINE_BLOCK_TYPES and text[b["start"]:b["end"]].strip()]
    if sum(1 for b in picked if b["type"] in {"para", "text"}) < 4:
        return []
    paragraphs = [text[b["start"]:b["end"]].strip() for b in picked]
    roles = label_paragraph_roles(paragraphs)
    starts = structural_unit_starts(paragraphs, roles)
    rows: list[dict] = []
    for n, first in enumerate(starts):
        last = (starts[n + 1] if n + 1 < len(starts) else len(paragraphs)) - 1
        role = roles[first]
        if role == "metadata":
            continue
        members = picked[first : last + 1]
        numbered = [b for b in members if b.get("num") is not None and b["type"] == "para"]
        head = " ".join(paragraphs[first].split())
        heading_row = role == "analysis" and picked[first]["type"] == "heading" or (
            role == "analysis" and bool(rows) and rows[-1]["role"] == "analysis" and heading_kind(paragraphs[first]) is not None
        )
        title = head[:90] if heading_row else _ROLE_TITLES[role]
        rows.append({
            "title": title,
            "role": role,
            "start": picked[first]["start"],
            "para": numbered[0]["num"] if numbered else None,
            "count": len(numbered),
            "level": 2 if heading_row and rows and rows[-1]["role"] == "analysis" else 1,
        })
    return rows
