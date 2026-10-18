"""Court-specific correction of the paragraph roles, trained on paragraphs read by two independent readers.

``learned_roles`` was trained mostly on Federal Court and tribunal decisions, so on Supreme Court and Federal
Court of Appeal decisions it keeps calling legal tests "analysis" and whole fact sections "overview". This is a
second stage: a logistic model over the labeller's role and its scores for the paragraph and its neighbours, the court,
the place in the decision and in its opinion, the nearest heading, the paragraph's wording, how many citations it
carries and whose position it states; the roles are then decoded in order with learned transition scores. The weights
are a fixed file (``role_correction_weights.npz``) written by ``scripts/train_role_correction.py``; reading a decision
runs only regular expressions and numpy.

It needs the court and the decision's units, which the outline has, so it is called from the outline
(``correct_units``) and not from the bare labeller. With no court, a missing weights file or ILIT_ROLE_CORRECTION unset,
the roles pass through unchanged.
"""

from __future__ import annotations

import contextlib
import contextvars
import os
import re
import zlib
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterator, Sequence

import numpy as np

from backend.contextual_authority import case_structure as cs

WEIGHTS_PATH = Path(__file__).with_name("role_correction_weights.npz")
HASH_BUCKETS = 1 << 17
FORUMS = ("fc", "fca", "scc")
TRANSITION_WEIGHT = 0.5
_forum: contextvars.ContextVar[str] = contextvars.ContextVar("role_correction_forum", default="")
_text: contextvars.ContextVar[str] = contextvars.ContextVar("role_correction_text", default="")
_WORD_RE = re.compile(r"[a-z]+")
_CITE_RE = re.compile(r"\bv\.? |\bSCC\b|\bFCA\b|\bFC\b|\bat para|\bONCA\b|S\.C\.R|\[\d{4}\]")
_ISSUE_CUE_RE = re.compile(r"\b(?:issue|question|issues|questions)\b.*\b(?:is|are)\b|whether")
_FALLBACK_FORUMS = ((re.compile(r"Federal Court of Appeal|\b\d{4} FCA \d+"), "fca"), (re.compile(r"Federal Court Decisions|\b\d{4} FC \d+"), "fc"), (re.compile(r"Supreme Court of Canada|\b\d{4} SCC \d+"), "scc"))


def enabled() -> bool:
    return os.environ.get("ILIT_ROLE_CORRECTION") == "1"


def forum_of(text: str) -> str:
    """fc, fca or scc from the top of the stored decision; empty when it is none of them."""
    from backend.position_holder import detect_forum

    head = (text or "")[:600]
    forum = detect_forum(head)
    if forum in FORUMS:
        return forum
    for pattern, name in _FALLBACK_FORUMS:
        if pattern.search(head):
            return name
    return ""


@contextlib.contextmanager
def use_forum(forum: str, text: str = "") -> Iterator[None]:
    """Name the court (and give the decision's text, which the whose-position tags are read from) for the labelling inside."""
    token, text_token = _forum.set(forum or ""), _text.set(text or "")
    try:
        yield
    finally:
        _forum.reset(token)
        _text.reset(text_token)


@lru_cache(maxsize=1)
def _weights():
    if not WEIGHTS_PATH.exists():
        return None
    data = np.load(WEIGHTS_PATH)
    return data["coef"].astype(np.float32), data["bias"].astype(np.float32), data["transitions"].astype(np.float64)


def available() -> bool:
    return _weights() is not None


def _hash(term: str) -> int:
    return zlib.crc32(term.encode("utf-8")) % HASH_BUCKETS


def holders_by_number(text: str) -> dict[int, tuple[str, float]]:
    """Printed paragraph number -> (whose position the paragraph carries, its probability) from ``learned_positions``; empty when unavailable."""
    if not text:
        return {}
    from backend import learned_positions

    try:
        numbers, tags = learned_positions.tag_decision_text(text, "")
    except Exception:  # noqa: BLE001 - the correction is optional; never break the outline over it
        return {}
    return {n: (t["holder"], float(t["p"] or 0.0)) for n, t in zip(numbers, tags)}


def feature_terms(
    forum: str,
    units: Sequence[dict[str, Any]],
    roles: Sequence[str],
    log_p: np.ndarray,
    holders: dict[int, tuple[str, float]],
    opinion_starts: Sequence[int],
) -> tuple[list[int], list[dict[int, float]]]:
    """Unit indexes of the numbered paragraphs and their hashed features. ``holders`` maps a printed number to
    (holder, probability); ``opinion_starts`` are the unit indexes where each opinion begins."""
    f = forum
    n_all = len(units)
    numbered = [i for i, u in enumerate(units) if u["num"] is not None]
    n = len(numbered)
    first_of = sorted(opinion_starts)
    last_head, since, head_before = None, 0, []
    for u in units:
        if u["heading"]:
            last_head, since = u["text"], 0
        elif u["num"] is not None:
            since += 1
        head_before.append((last_head, since))
    next_head, dist, head_after = None, 0, [None] * n_all
    for i in range(n_all - 1, -1, -1):
        if units[i]["heading"]:
            next_head, dist = units[i]["text"], 0
        elif units[i]["num"] is not None:
            dist += 1
        head_after[i] = (next_head, dist)
    opinion_of = []
    for i in numbered:
        k = -1
        for j, start in enumerate(first_of):
            if i >= start:
                k = j
        opinion_of.append(max(k, 0))
    members: dict[int, list[int]] = {}
    for k, o in enumerate(opinion_of):
        members.setdefault(o, []).append(k)
    out: list[dict[int, float]] = []
    for k, i in enumerate(numbered):
        body = cs._strip_number(units[i]["text"])[1]
        low = body.lower()
        role = roles[i]
        o = opinion_of[k]
        group = members[o]
        kp = group.index(k)
        pos = k / max(1, n - 1)
        pop = kp / max(1, len(group) - 1)
        terms: dict[str, float] = {}

        def add(key: str, value: float = 1.0) -> None:
            terms[key] = terms.get(key, 0.0) + value

        add(f"r_{role}"), add(f"{f}_r_{role}")
        for j, name in enumerate(cs.ROLES):
            add(f"lp_{name}", float(log_p[i][j]) / 5), add(f"{f}_lp_{name}", float(log_p[i][j]) / 5)
        for shift in (-2, -1, 1, 2):
            kk = k + shift
            if 0 <= kk < n:
                ii = numbered[kk]
                for j, name in enumerate(cs.ROLES):
                    add(f"lp{shift:+d}_{name}", float(log_p[ii][j]) / 5)
                add(f"rr{shift:+d}_{roles[ii]}")
        add("pos", pos), add(f"{f}_pos", pos), add(f"{f}_pos2", pos * pos)
        add("pop", pop), add(f"{f}_pop", pop), add(f"{f}_pop2", pop * pop)
        add("first", float(k == 0)), add("n", n / 100)
        add(f"opi{min(o, 3)}"), add(f"{f}_opi{min(o, 3)}")
        add("opfirst", float(kp == 0)), add(f"{f}_opfirst", float(kp == 0))
        add("opfirst2", float(kp <= 2)), add(f"{f}_op_early", float(kp <= 2)), add("nops", min(len(first_of), 4))
        add("tail", float(n - 1 - k <= 2)), add(f"{f}_tail", float(n - 1 - k <= 2)), add("toend", min(n - 1 - k, 10) / 10)
        words = _WORD_RE.findall(low[:600])
        for w, word in enumerate(words[:3]):
            add(f"{f}_w{w}_{word}"), add(f"w_{word}")
        for a, b in zip(words[:8], words[1:9]):
            add(f"{f}_bg_{a}_{b}")
        for word in set(words[:80]):
            add(f"bow_{word}", 0.3), add(f"{f}_bow_{word}", 0.3)
        for word in set(_WORD_RE.findall(low[-120:])):
            add(f"tail_{word}", 0.5)
        cites = min(len(_CITE_RE.findall(body)), 8) / 8
        add("cite", cites), add(f"{f}_cite", cites)
        add("issue_cue", float(bool(_ISSUE_CUE_RE.search(low[:200]))))
        add("len", min(len(body), 2500) / 2500), add(f"{f}_len", min(len(body), 2500) / 2500)
        add("quote_start", float(body[:1] in "“\"")), add("colon_end", float(body.rstrip().endswith(":")))
        add("quotefrac", min(body.count("“") + body.count("\""), 10) / 10)
        number = cs._strip_number(units[i]["text"])[0]
        holder, prob = holders.get(number if number is not None else -1, ("none", 0.0))
        add(f"h_{holder}"), add(f"{f}_h_{holder}"), add("hp", prob or 0.0), add(f"{f}_h_{holder}_{role}")
        for shift in (-1, 1):
            kk = k + shift
            if 0 <= kk < n:
                number2 = cs._strip_number(units[numbered[kk]]["text"])[0]
                add(f"h{shift:+d}_{holders.get(number2 if number2 is not None else -1, ('none', 0.0))[0]}")
        head, passed = head_before[i]
        following, ahead = head_after[i]
        if head:
            kind = cs.heading_kind(head) or "unknown"
            add(f"hk_{kind}"), add(f"{f}_hk_{kind}"), add(f"{f}_hk_{kind}_{role}")
            for word in set(_WORD_RE.findall(head.lower())[:8]):
                add(f"hw_{word}"), add(f"{f}_hw_{word}")
            add("since_h", min(passed, 10) / 10), add("first_after_h", float(passed == 1)), add(f"{f}_first_after_h_{kind}", float(passed == 1))
        else:
            add("no_heading"), add(f"{f}_no_heading")
        if following:
            kind = cs.heading_kind(following) or "unknown"
            add(f"nhk_{kind}"), add(f"{f}_nhk_{kind}"), add("last_before_h", float(ahead == 1))
        row: dict[int, float] = {}
        for term, value in terms.items():
            key = _hash(term)
            row[key] = row.get(key, 0.0) + value
        out.append(row)
    return numbered, out


def decode(scores: np.ndarray, transitions: np.ndarray, weight: float = TRANSITION_WEIGHT) -> list[int]:
    """Best role sequence: per-paragraph log-probabilities plus ``weight`` times the learned transition scores."""
    n = len(scores)
    best = np.zeros((n, scores.shape[1]))
    back = np.zeros((n, scores.shape[1]), dtype=int)
    best[0] = scores[0]
    for t in range(1, n):
        cand = best[t - 1][:, None] + weight * transitions
        back[t] = cand.argmax(0)
        best[t] = cand.max(0) + scores[t]
    path = [int(best[-1].argmax())]
    for t in range(n - 1, 0, -1):
        path.append(int(back[t][path[-1]]))
    return path[::-1]


def log_probabilities(row_features: Sequence[dict[int, float]], coef: np.ndarray, bias: np.ndarray) -> np.ndarray:
    scores = np.zeros((len(row_features), len(cs.ROLES)))
    for r, row in enumerate(row_features):
        idx = np.fromiter(row.keys(), dtype=np.int64)
        val = np.fromiter(row.values(), dtype=np.float64)
        scores[r] = coef[:, idx] @ val + bias
    scores -= scores.max(axis=1, keepdims=True)
    return np.maximum(scores - np.log(np.exp(scores).sum(axis=1, keepdims=True)), -14.0)


SECTION_OF_ROLE = {"metadata": 0, "overview": 0, "facts": 0, "issues": 1, "analysis": 2, "disposition": 3}


def correct_units(units: Sequence[dict[str, Any]], roles: list[str], log_p: np.ndarray | None, opinion_starts: Sequence[int] = ()) -> tuple[list[str], np.ndarray | None]:
    """The roles with the court-specific correction applied to numbered paragraphs, and a len(units) x 4 matrix of
    log-probabilities of Background / Issues / Analysis / Disposition for them (NaN rows elsewhere).
    Unchanged roles and None when the correction cannot run."""
    forum = _forum.get()
    if log_p is None or not (enabled() and forum in FORUMS and available()) or len(units) != len(roles):
        return roles, None
    numbered = [i for i, u in enumerate(units) if u["num"] is not None]
    if len(numbered) < 4:
        return roles, None
    coef, bias, transitions = _weights()  # type: ignore[misc]
    numbered, rows = feature_terms(forum, units, roles, log_p, holders_by_number(_text.get()), opinion_starts)
    scores = log_probabilities(rows, coef, bias)
    path = decode(scores, transitions)
    out = list(roles)
    for i, k in zip(numbered, path):
        out[i] = cs.ROLES[k]
    sections = np.full((len(units), 4), np.nan)
    for i, row in zip(numbered, scores):
        for role, k in SECTION_OF_ROLE.items():
            column = cs.ROLES.index(role)
            sections[i, k] = row[column] if np.isnan(sections[i, k]) else np.logaddexp(sections[i, k], row[column])
    return out, sections


def monotone_sections(scores: np.ndarray, switch_cost: float = 1.0) -> list[int]:
    """Best Background <= Issues <= Analysis <= Disposition assignment (0..3) for a run of paragraphs."""
    n = len(scores)
    best = np.full((n, 4), -1e18)
    back = np.zeros((n, 4), dtype=int)
    best[0] = scores[0]
    for t in range(1, n):
        for s in range(4):
            options = [(best[t - 1][q] - (switch_cost if q != s else 0.0), q) for q in range(s + 1)]
            value, q = max(options)
            best[t][s], back[t][s] = value + scores[t][s], q
    path = [int(best[-1].argmax())]
    for t in range(n - 1, 0, -1):
        path.append(int(back[t][path[-1]]))
    return path[::-1]


def label_units(units: Sequence[dict[str, Any]]) -> tuple[list[str], np.ndarray | None, list[int]]:
    """The roles for the outline's units: the labeller's, with the court-specific correction when it is on.
    The second value is the section score matrix of ``correct_units`` (None without the correction), the third the units where opinions begin."""
    texts = [u["text"] for u in units]
    forum = _forum.get()
    if not (enabled() and forum in FORUMS and available() and os.environ.get("ILIT_LEARNED_ROLES") == "1"):
        return cs.label_paragraph_roles(texts), None, []
    from backend.contextual_authority import learned_roles, opinions

    roles, log_p = learned_roles.label_paragraph_roles_scored(texts)
    try:
        starts = [o.first_unit for o in opinions.find_opinions(_text.get(), units)]
    except Exception:  # noqa: BLE001 - optional context; the correction still runs without it
        starts = []
    corrected, sections = correct_units(units, roles, log_p, starts)
    return corrected, sections, starts
