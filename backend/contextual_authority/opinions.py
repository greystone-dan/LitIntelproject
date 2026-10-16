"""Separate opinions inside one decision (majority, concurring, dissenting reasons), found with plain rules.

Supreme Court of Canada decisions list their opinions in the header ("Dissenting Reasons: (paras. 46 to 123)", then the
judge and who concurs). Older ones, and Federal Court of Appeal decisions, do not, so the reasons' own opening lines are
the fallback: "The judgment of ... was delivered by", "Abella J. (dissenting) —", "SEXTON, J.A. (Dissenting)".
On a sample of 784 indexed SCC decisions the opening lines gave the same opinion count as the index in 768 (98%).
See docs/FC_DECISION_STRUCTURE.md. No model and no database.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Sequence

_INDEX = re.compile(r"(?im)^(?P<kind>[A-Za-z ,]{0,50}?):?[ \t]*\n?\(paras?\. ?(?P<a>\d+)(?:(?: to |-|–| and )(?P<b>\d+))?\)")
_NAME = (
    r"(?:The Chief Justice|(?:Chief )?Justice [A-Z][\w'’\-]+|"
    r"[A-ZÀ-Ý][\w'’\-]+(?:[ ‑\-][A-ZÀ-Ý][\w'’\-]+)*,?(?: [A-Z]\.)?,? (?:C\.J\.|J\.A\.|J\.|JJ\.A\.|JJ\.)(?: and [A-ZÀ-Ý][\w'’\-]+ J\.)?)"
)
# "Rothstein J. —", "Bastarache J. (dissenting) —", "SEXTON, J.A. (Dissenting)"
_AUTHOR = re.compile(
    r"(?m)^(?:\[?\d{1,3}\]?\s+)?(?P<who>" + _NAME + r")(?:\s*\((?P<role>[^)\n]{3,80})\)\s*(?:[—–]|--|-|:)?|\s*(?:[—–]|--))[ \t]*(?=\S|$)"
)
_DELIVERED = re.compile(
    r"(?mi)^(?:(?:the )?(?:following (?:is|are) the |english version of the )?)?(?:unanimous )?(?:judgment|reasons?|opinion)s?(?: of (?P<who>[^\n]{2,200}?))? (?:was|were|is|are)? ?(?:delivered|read|rendered)(?: orally)?(?: in english)? by\s*:?$"
)
_CONCURRING_LINE = re.compile(r"^(?P<who>.{3,60}?(?:C\.J\.|J\.A\.|J\.))(?:\s*\((?P<conc>[^)]*concurring[^)]*)\))?\s*$")
_CLUSTER_GAP = 300
_MAX_ROLE_WORDS = 8
_MIN_OPINION_UNITS = 3


@dataclass
class Opinion:
    kind: str  # lead, concurring, dissenting
    label: str  # the court's own wording, e.g. "dissenting reasons"
    author: str | None
    concurring: str | None
    first_unit: int
    para: int | None
    source: str  # index, openers or cover
    extra: dict[str, Any] = field(default_factory=dict)


def _kind(label: str) -> str:
    low = label.lower()
    if "dissent" in low:
        return "dissenting"
    if "concur" in low:
        return "concurring"
    return "lead"


def _header(text: str) -> str:
    start = text.find("Decision Content")
    segment = text[start : start + 5000] if start >= 0 else text[:5000]
    end = re.search(r"\n_{5,}\n|\nIndexed as", segment)
    return segment[: end.start()] if end else segment


def _index_authors(header: str, after: int) -> list[tuple[str, str | None]]:
    """Judge lines listed under the paragraph ranges, in order."""
    found = []
    for line in header[after:].split("\n"):
        match = _CONCURRING_LINE.match(line.strip())
        if match:
            conc = re.sub(r"[,;]?\s*concurring.*$", "", (match.group("conc") or "").strip())
            found.append((match.group("who").strip(), conc or None))
    return found


def _by_index(text: str, units: Sequence[dict]) -> list[Opinion]:
    header = _header(text)
    ranges = [(m.group("kind").strip().rstrip(":"), int(m.group("a")), m.end()) for m in _INDEX.finditer(header)]
    if not ranges:
        return []
    authors = _index_authors(header, ranges[-1][2])
    by_number: dict[int, int] = {}
    for i, u in enumerate(units):
        if u.get("body") and u.get("num") is not None:
            by_number.setdefault(u["num"], i)
    found: list[Opinion] = []
    for n, (label, first_para, _end) in enumerate(ranges):
        unit = by_number.get(first_para)
        if unit is None:
            return []  # the index and the text disagree: do not guess
        author, conc = authors[n] if n < len(authors) else (None, None)
        found.append(Opinion(_kind(label) if n else "lead", label.lower(), author, conc, unit, first_para, "index"))
    starts = [o.first_unit for o in found]
    return found if starts == sorted(set(starts)) else []


def _by_openers(text: str, units: Sequence[dict]) -> list[Opinion]:
    body = [i for i, u in enumerate(units) if u.get("body")]
    if len(body) < 5:
        return []
    lo = units[body[0]]["start"] - 400
    hits: list[tuple[int, str, str | None, str | None]] = []  # offset, source, author, role
    for m in _DELIVERED.finditer(text, max(lo, 0)):
        hits.append((m.start(), "delivered", None, None))
    for m in _AUTHOR.finditer(text, max(lo, 0)):
        role = (m.group("role") or "").strip()
        if role and (len(role.split()) > _MAX_ROLE_WORDS or not re.search(r"(?i)dissent|concur|result|part", role)):
            continue  # "(Cromwell J. concurring)" style asides and citations are not openers
        # the rest of the line must be reasons, not a sentence about someone else
        hits.append((m.start(), "author", m.group("who").strip(), role or None))
    hits.sort()
    clusters: list[list[tuple[int, str, str | None, str | None]]] = []
    for hit in hits:
        if clusters and hit[0] - clusters[-1][-1][0] < _CLUSTER_GAP:
            clusters[-1].append(hit)
        else:
            clusters.append([hit])
    if len(clusters) < 2:
        return []
    found: list[Opinion] = []
    for cluster in clusters:
        offset = cluster[-1][0] if any(h[1] == "author" for h in cluster) else cluster[0][0]
        unit = next((i for i in body if units[i]["start"] >= offset), None)
        if unit is None:
            continue
        who = next((h[2] for h in cluster if h[2]), None)
        role = next((h[3] for h in cluster if h[3]), "") or ""
        if found and sum(1 for i in body if found[-1].first_unit <= i < unit) < _MIN_OPINION_UNITS:
            continue  # two openers a paragraph apart are one opinion (a translation note and its author line)
        found.append(Opinion(_kind(role) if found else "lead", role.lower() or "reasons", who, None, unit, units[unit].get("num"), "openers"))
    if not found:
        return []
    if sum(1 for i in body if body[0] <= i < found[0].first_unit) >= _MIN_OPINION_UNITS:
        # the lead reasons have no opening line of their own (Court of Appeal: the judge's name stands alone): they run up to the first opener
        found.insert(0, Opinion("lead", "reasons", None, None, body[0], units[body[0]].get("num"), "openers"))
        found[1].kind = _kind(found[1].label)
    else:
        found[0].first_unit = min(found[0].first_unit, body[0])
        found[0].kind = "lead"
    return found if len(found) >= 2 else []


_COVER_BY = re.compile(r"(?m)^(?:PUBLIC )?REASONS FOR (?:JUDGMENT|ORDER)S?(?P<court> OF THE COURT)?:?(?: BY:?)?[ \t]*(?P<who>[^\n]*)$")
_COVER_CONCURRED = re.compile(r"(?m)^CONCURRED IN BY:?[ \t]*(?P<who>[^\n]*(?:\n[A-ZÀ-Ý][^\n]*J\.A\.[^\n]*)*)")


def cover_author(text: str) -> dict[str, str | None]:
    """Federal Court of Appeal cover block: who wrote the reasons and who concurred."""
    start = text.find("Decision Content")
    cover = text[start : start + 2500] if start >= 0 else text[:2500]
    match = _COVER_BY.search(cover)
    if not match:
        return {}
    court = bool(match.group("court"))
    who = match.group("who").strip()
    if not who:  # the name sits on the next line
        rest = cover[match.end() :].lstrip("\n").split("\n", 1)[0].strip()
        who = rest if re.search(r"J\.A\.|C\.J\.|J\.", rest) else ""
    conc = _COVER_CONCURRED.search(cover)
    concurring = None
    if conc:
        names = [n.strip() for n in re.findall(r"[^\n]+?(?:J\.A\.|C\.J\.|J\.)", " ".join(conc.group("who").split()))]
        concurring = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1] if names else None
    return {"author": None if court else (who or None), "court": "the Court" if court else None, "concurring": concurring}


_FCA = re.compile(r"Federal Court of Appeal|\b\d{4} FCA \d+")


def find_opinions(text: str, units: Sequence[dict]) -> list[Opinion]:
    """Opinions in reading order (lead first), each with the unit it starts at. Empty when the decision is a single set of
    reasons with nothing to tell the opinions apart."""
    found = _by_index(text, units) or _by_openers(text, units)
    if found and found[0].author is None and _FCA.search(text[:1500]):
        cover = cover_author(text)  # Court of Appeal: the cover block names the lead author
        found[0].author = cover.get("author") or cover.get("court")
        found[0].concurring = found[0].concurring or cover.get("concurring")
    return found


def _short(name: str | None) -> str:
    plain = re.sub(r"\s+", " ", re.sub(r",\s+(?=C\.J\.|J\.A\.|JJ?\.)", " ", name or "")).strip()
    return re.sub(r"[A-ZÀ-Ý]{3,}", lambda m: m.group().title(), plain)


def opinion_title(op: Opinion, total: int) -> str:
    who = _short(op.author)
    tail = f" ({_short(op.concurring)} concurring)" if op.concurring else ""
    if op.kind == "dissenting":
        base = "Dissenting reasons" if "part" not in op.label else "Reasons dissenting in part"
    elif op.kind == "concurring":
        base = "Concurring reasons" if "result" not in op.label else "Reasons concurring in the result"
    else:
        base = "Reasons for judgment" if total == 1 else "Joint reasons" if "joint" in op.label else "Majority reasons"
    return f"{base}, {who}{tail}" if who else base
