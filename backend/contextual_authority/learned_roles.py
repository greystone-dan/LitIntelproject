"""Paragraph roles from a small learned word/position model blended with the case-structure rules.

Deterministic and offline: the weights are a fixed file (learned_roles_weights.npz) trained by
scripts/train_learned_roles.py from labelled decisions. Reading a decision runs only numpy; no model call is made.
The model's per-paragraph log-probabilities are added to the rule scores inside the same ordered (Viterbi)
labeller that `case_structure.label_paragraph_roles` uses.
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
ALPHA = 0.5  # weight of the learned log-probabilities
BETA = 1.0  # weight of the rule scores
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


def dense_features(paragraphs: Sequence[str], emissions: list[dict[str, float]]) -> np.ndarray:
    n = len(paragraphs)
    rows = []
    for i, text in enumerate(paragraphs):
        pos = i / max(1, n - 1)
        row = [pos, pos * pos, float(cs._strip_number(text)[0] is not None), min(len(text), 1500) / 1500]
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
    return data["sparse"].astype(np.float32), data["dense"].astype(np.float32), data["bias"].astype(np.float32)


def available() -> bool:
    return _weights() is not None


def log_probabilities(paragraphs: Sequence[str], emissions: list[dict[str, float]]) -> np.ndarray:
    """n x len(cs.ROLES) matrix of log-probabilities, columns in cs.ROLES order."""
    sparse, dense_w, bias = _weights()  # type: ignore[misc]
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


def label_paragraph_roles(paragraphs: Sequence[str]) -> list[str]:
    """Same ordered labeller as the rules, with the learned log-probabilities added to each paragraph's scores."""
    if not paragraphs:
        return []
    if not available():
        return cs.label_paragraph_roles_rules(paragraphs)
    emissions = cs._emissions(paragraphs)
    log_p = log_probabilities(paragraphs, emissions)
    combined = []
    for i, row in enumerate(emissions):
        combined.append({s: BETA * row[s] + ALPHA * float(log_p[i][cs.ROLES.index(cs._STATE_ROLE.get(s, s))]) for s in cs._STATES})
    return cs._viterbi_roles(combined)
