"""Court-specific correction of the paragraph roles, trained on paragraphs read by two independent readers.

``learned_roles`` was trained mostly on Federal Court and tribunal decisions, so on Supreme Court and Federal
Court of Appeal decisions it keeps calling legal tests "analysis" and whole fact sections "overview". This is a small
third stage: a logistic model over the role the labeller gave (and the neighbours' roles), the court, the place in
the decision, the paragraph's opening words and how many citations it carries. The weights are a fixed file
(``role_correction_weights.npz``) written by ``scripts/train_role_correction.py``; reading a decision runs only
regular expressions and numpy.

It needs the court, which the paragraph list alone does not carry, so callers that have the decision's text set it with
``use_forum``. With no court, a missing weights file or ILIT_ROLE_CORRECTION unset, the roles pass through unchanged.
"""

from __future__ import annotations

import contextlib
import contextvars
import os
import re
import zlib
from functools import lru_cache
from pathlib import Path
from typing import Iterator, Sequence

import numpy as np

from backend.contextual_authority import case_structure as cs

WEIGHTS_PATH = Path(__file__).with_name("role_correction_weights.npz")
HASH_BUCKETS = 1 << 15
FORUMS = ("fc", "fca", "scc")
_forum: contextvars.ContextVar[str] = contextvars.ContextVar("role_correction_forum", default="")
_text: contextvars.ContextVar[str] = contextvars.ContextVar("role_correction_text", default="")
_WORD_RE = re.compile(r"[a-z]+")
_CITE_RE = re.compile(r"\bv\.? |\bSCC\b|\bFCA\b|\bFC\b|\bat para|\bONCA\b|S\.C\.R|\[\d{4}\]")
_ISSUE_CUE_RE = re.compile(r"\b(?:issue|question|issues|questions)\b.*\b(?:is|are)\b|whether")


def enabled() -> bool:
    return os.environ.get("ILIT_ROLE_CORRECTION") == "1"


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
    return data["coef"].astype(np.float32), data["bias"].astype(np.float32)


def available() -> bool:
    return _weights() is not None


def _hash(term: str) -> int:
    return zlib.crc32(term.encode("utf-8")) % HASH_BUCKETS


def holders_by_number(text: str) -> dict[int, str]:
    """Printed paragraph number -> whose position the paragraph carries (``learned_positions``); empty when unavailable."""
    if not text:
        return {}
    from backend import learned_positions

    try:
        numbers, tags = learned_positions.tag_decision_text(text, "")
    except Exception:  # noqa: BLE001 - the correction is optional; never break the outline over it
        return {}
    return {n: t["holder"] for n, t in zip(numbers, tags)}


def feature_terms(forum: str, texts: Sequence[str], roles: Sequence[str], numbered: Sequence[int], holders: dict[int, str] | None = None) -> list[dict[int, float]]:
    """Hashed features for each numbered paragraph (``numbered`` indexes into texts/roles), in that order."""
    holders = holders or {}
    n = len(numbered)
    out: list[dict[int, float]] = []
    for k, i in enumerate(numbered):
        role = roles[i]
        prev_role = roles[numbered[k - 1]] if k else "S"
        next_role = roles[numbered[k + 1]] if k + 1 < n else "E"
        pos = k / max(1, n - 1)
        body = cs._strip_number(texts[i])[1]
        words = _WORD_RE.findall(body[:200].lower())
        cites = min(len(_CITE_RE.findall(body[:200])), 6) / 6
        terms: dict[str, float] = {
            f"r_{role}": 1.0, f"{forum}_r_{role}": 1.0,
            "pos": pos, f"{forum}_pos": pos, f"{forum}_pos2": pos * pos,
            "first": float(k == 0), "n": n / 100,
            f"prev_{prev_role}": 1.0, f"next_{next_role}": 1.0, f"{forum}_prev_{prev_role}_{role}": 1.0,
            "cite": cites, f"{forum}_cite": cites,
            "issue_cue": float(bool(_ISSUE_CUE_RE.search(body[:200].lower()))),
        }
        holder = holders.get(cs._strip_number(texts[i])[0] or -1, "none")
        terms[f"h_{holder}"] = 1.0
        terms[f"{forum}_h_{holder}_{role}"] = 1.0
        for w, word in enumerate(words[:3]):
            terms[f"{forum}_w{w}_{word}"] = 1.0
            terms[f"w_{word}"] = 1.0
        for a, b in zip(words, words[1:]):
            terms[f"{forum}_bg_{a}_{b}"] = 1.0
        row: dict[int, float] = {}
        for term, value in terms.items():
            key = _hash(term)
            row[key] = row.get(key, 0.0) + value
        out.append(row)
    return out


def correct(texts: Sequence[str], roles: list[str]) -> list[str]:
    """The roles with the court-specific correction applied to numbered paragraphs; unchanged when it cannot run."""
    forum = _forum.get()
    if not (enabled() and forum in FORUMS and available()) or len(texts) != len(roles):
        return roles
    numbered = [i for i, text in enumerate(texts) if cs._strip_number(text)[0] is not None]
    if len(numbered) < 4:
        return roles
    coef, bias = _weights()  # type: ignore[misc]
    rows = feature_terms(forum, texts, roles, numbered, holders_by_number(_text.get()))
    out = list(roles)
    for i, row in zip(numbered, rows):
        idx = np.fromiter(row.keys(), dtype=np.int64)
        val = np.fromiter(row.values(), dtype=np.float64)
        scores = coef[:, idx] @ val + bias
        out[i] = cs.ROLES[int(scores.argmax())]
    return out
