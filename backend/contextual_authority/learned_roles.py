"""Paragraph roles from a small learned word/position model blended with the case-structure rules.

Deterministic and offline: the weights are a fixed file (learned_roles_weights.npz) trained by
scripts/train_learned_roles.py from labelled decisions. Reading a decision runs only numpy; no model call is made.
Two stages: a word + position model gives per-paragraph log-probabilities; a second small model reads those
together with the neighbouring paragraphs' log-probabilities, the rule scores and the position, and its
log-probabilities are added to the rule scores inside the same ordered (Viterbi) labeller that
`case_structure.label_paragraph_roles` uses.
"""

from __future__ import annotations

import re
import zlib
from functools import lru_cache
from pathlib import Path
from typing import Sequence

import numpy as np

from backend.contextual_authority import case_structure as cs

WEIGHTS_PATH = Path(__file__).with_name("learned_roles_weights.npz")
HASH_BUCKETS = 1 << 15
TEXT_LIMIT = 500
ALPHA = 1.0  # weight of the learned log-probabilities
BETA = 0.5  # weight of the rule scores
FALLBACK_WINDOW = 3  # paragraphs back from the last numbered one searched for an order cue
FALLBACK_MIN_SCORE = 2.5
_TOKEN_RE = re.compile(r"[a-z0-9’']+")
_DIGITS_RE = re.compile(r"\d+")
_FLOOR = np.log(1e-4)


def _tokens(text: str) -> list[str]:
    _, body = cs._strip_number(text)
    return _TOKEN_RE.findall(_DIGITS_RE.sub("0", body[:TEXT_LIMIT].lower()))


def _hash(term: str) -> int:
    return zlib.crc32(term.encode("utf-8")) % HASH_BUCKETS


def text_features(text: str) -> dict[int, float]:
    """L2-normalised hashed unigram + bigram counts for one paragraph."""
    tokens = _tokens(text)
    counts: dict[int, float] = {}
    for term in tokens + [f"{a} {b}" for a, b in zip(tokens, tokens[1:])]:
        key = _hash(term)
        counts[key] = counts.get(key, 0.0) + 1.0
    norm = sum(v * v for v in counts.values()) ** 0.5
    return {k: v / norm for k, v in counts.items()} if norm else {}


def body_positions(paragraphs: Sequence[str]) -> np.ndarray:
    """n x 2: position within the reasons (first to last numbered paragraph, clipped to 0..1) and a tail flag.

    A long counsel/solicitor block after the reasons makes plain position misleading for short decisions."""
    n = len(paragraphs)
    numbered = [i for i, text in enumerate(paragraphs) if cs._strip_number(text)[0] is not None]
    first = numbered[0] if numbered else min(n - 1, 2)
    last = numbered[-1] if numbered else n - 1
    idx = np.arange(n)
    pos = np.clip((idx - first) / max(1, last - first), 0.0, 1.0)
    return np.stack([pos, (idx > last).astype(np.float64)], axis=1)


def dense_features(paragraphs: Sequence[str], emissions: list[dict[str, float]]) -> np.ndarray:
    n = len(paragraphs)
    body = body_positions(paragraphs)
    rows = []
    for i, text in enumerate(paragraphs):
        pos = i / max(1, n - 1)
        row = [pos, pos * pos, float(cs._strip_number(text)[0] is not None), min(len(text), 1500) / 1500]
        row += [body[i][0], body[i][0] ** 2, body[i][1]]
        row += [emissions[i][state] for state in cs._STATES]
        row += [float(k / 10 <= pos < (k + 1) / 10) for k in range(10)]
        rows.append(row)
    return np.array(rows, dtype=np.float64)


def feature_matrix(paragraphs: Sequence[str], emissions: list[dict[str, float]]) -> tuple[list[dict[int, float]], np.ndarray]:
    return [text_features(text) for text in paragraphs], dense_features(paragraphs, emissions)


@lru_cache(maxsize=1)
def _weights():
    if not WEIGHTS_PATH.exists():
        return None
    data = np.load(WEIGHTS_PATH)
    stage2 = tuple(data[k].astype(np.float64) for k in ("s2_coef", "s2_bias", "s2_mean", "s2_scale"))
    return data["sparse"].astype(np.float32), data["dense"].astype(np.float32), data["bias"].astype(np.float32), stage2


def available() -> bool:
    return _weights() is not None


def log_probabilities(paragraphs: Sequence[str], emissions: list[dict[str, float]]) -> np.ndarray:
    """n x len(cs.ROLES) matrix of log-probabilities, columns in cs.ROLES order."""
    sparse, dense_w, bias, _ = _weights()  # type: ignore[misc]
    texts, dense = feature_matrix(paragraphs, emissions)
    scores = dense @ dense_w.T + bias
    for i, feats in enumerate(texts):
        if feats:
            idx = np.fromiter(feats.keys(), dtype=np.int64)
            val = np.fromiter(feats.values(), dtype=np.float64)
            scores[i] += sparse[:, idx] @ val
    scores -= scores.max(axis=1, keepdims=True)
    log_p = scores - np.log(np.exp(scores).sum(axis=1, keepdims=True))
    return np.maximum(log_p, _FLOOR)


def stack_features(log_p: np.ndarray, emissions: list[dict[str, float]], paragraphs: Sequence[str]) -> np.ndarray:
    """Second-stage inputs: own and neighbouring log-probabilities, rule scores, position, length of the decision."""
    n = len(log_p)
    scores = np.array([[row[s] for s in cs._STATES] for row in emissions], dtype=np.float64)
    pos = np.arange(n) / max(1, n - 1)
    parts = [log_p, scores, pos[:, None], np.full((n, 1), n / 100.0), body_positions(paragraphs)]
    for shift in (-2, -1, 1, 2):
        moved = np.roll(log_p, shift, axis=0)
        if shift > 0:
            moved[:shift] = _FLOOR
        else:
            moved[shift:] = _FLOOR
        parts.append(moved)
    parts.append(np.cumsum(log_p, axis=0) / np.arange(1, n + 1)[:, None])
    return np.hstack(parts)


def stage_two(log_p: np.ndarray, emissions: list[dict[str, float]], paragraphs: Sequence[str]) -> np.ndarray:
    """Second-stage log-probabilities (n x len(cs.ROLES))."""
    coef, intercept, mean, scale = _weights()[3]  # type: ignore[index]
    x = (stack_features(log_p, emissions, paragraphs) - mean) / scale
    scores = x @ coef.T + intercept
    scores -= scores.max(axis=1, keepdims=True)
    out = scores - np.log(np.exp(scores).sum(axis=1, keepdims=True))
    return np.maximum(out, _FLOOR)


def label_paragraph_roles(paragraphs: Sequence[str]) -> list[str]:
    """Same ordered labeller as the rules, with the learned log-probabilities added to each paragraph's scores."""
    if not paragraphs:
        return []
    if not available():
        return cs.label_paragraph_roles_rules(paragraphs)
    emissions = cs._emissions(paragraphs)
    log_p = stage_two(log_probabilities(paragraphs, emissions), emissions, paragraphs)
    combined = []
    for i, row in enumerate(emissions):
        combined.append({s: BETA * row[s] + ALPHA * float(log_p[i][cs.ROLES.index(cs._STATE_ROLE.get(s, s))]) for s in cs._STATES})
    roles = cs._viterbi_roles(combined)
    return _ensure_disposition(roles, paragraphs, emissions)


def _ensure_disposition(roles: list[str], paragraphs: Sequence[str], emissions: list[dict[str, float]]) -> list[str]:
    """Every decision ends in an order. When the blend found none, take the last strong order cue in the final reasons."""
    if "disposition" in roles:
        return roles
    numbered = [i for i, text in enumerate(paragraphs) if cs._strip_number(text)[0] is not None]
    if not numbered:
        return roles
    last = numbered[-1]
    window = [i for i in range(max(0, last - FALLBACK_WINDOW), last + 1) if emissions[i]["disposition"] >= FALLBACK_MIN_SCORE]
    if not window:
        return roles
    start = window[0]
    return [("disposition" if start <= i <= last else role) for i, role in enumerate(roles)]
