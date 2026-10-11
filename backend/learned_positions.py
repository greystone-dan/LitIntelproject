"""Whose-position tags from the cue rules plus a small learned model (numpy only, no model call).

``position_holder`` reads fixed cue phrases. This module adds a second reading learned from labelled decisions:
stage 1 is a logistic model over the paragraph's opening words and the rule results (which holder each sentence
named, the case frame, the paragraph's structural role, its place in the decision); stage 2 reads stage 1's guesses
for the neighbouring paragraphs as well, because a submission, a quotation or a tribunal's narrative runs over
several paragraphs. The weights are a fixed file (``learned_positions_weights.npz``) written by
``scripts/train_learned_positions.py``; reading a decision runs only regular expressions and numpy.

The holders are those of ``position_holder``: applicant, respondent, earlier_decision_maker, court,
prior_court_or_authority, witness_or_document. Each paragraph gets its main holder and the probability of it.
"""

from __future__ import annotations

import re
import zlib
from functools import lru_cache
from pathlib import Path
from typing import Sequence

import numpy as np

from backend.case_frame import build_frame
from backend.contextual_authority import case_structure as cs
from backend.position_holder import HOLDERS, detect_forum, split_numbered_paragraphs, tag_decision

WEIGHTS_PATH = Path(__file__).with_name("learned_positions_weights.npz")
HASH_BUCKETS = 1 << 15
TEXT_LIMIT = 600
FORUMS = ("fc", "fca", "scc", "rpd", "rad", "iad", "")
_FLOOR = float(np.log(1e-4))
_TOKEN_RE = re.compile(r"[a-z0-9’']+")
_DIGITS_RE = re.compile(r"\d+")
_NUMBER_RE = re.compile(r"^\s*\[\d+\]\s*")
_FIRST_PARA_RE = re.compile(r"(?:^|\n|\s)\[1\]\s")


def split_header(full_text: str) -> tuple[str, str]:
	"""The stored header (everything before paragraph [1]) and the body from [1] on."""
	full_text = full_text or ""
	m = _FIRST_PARA_RE.search(full_text)
	return (full_text[: m.start()], full_text[m.start():]) if m else (full_text[:1500], full_text)


def _hash(term: str) -> int:
	return zlib.crc32(term.encode("utf-8")) % HASH_BUCKETS


def text_features(text: str) -> dict[int, float]:
	"""L2-normalised hashed unigram + bigram counts of the paragraph's opening words."""
	words = _TOKEN_RE.findall(_DIGITS_RE.sub("0", _NUMBER_RE.sub("", text)[:TEXT_LIMIT].lower()))
	counts: dict[int, float] = {}
	for term in words + [f"{a} {b}" for a, b in zip(words, words[1:])]:
		key = _hash(term)
		counts[key] = counts.get(key, 0.0) + 1.0
	norm = sum(v * v for v in counts.values()) ** 0.5
	return {k: v / norm for k, v in counts.items()} if norm else {}


def dense_features(paragraphs: Sequence[str], title: str, header: str, body: str) -> tuple[np.ndarray, list[str]]:
	"""Rule results and context per paragraph; also returns the rules' own main holder for each paragraph."""
	frame = build_frame(header, body)
	forum = detect_forum(header)
	results = tag_decision(list(paragraphs), title, frame)
	roles = cs.label_paragraph_roles_rules(list(paragraphs))
	n = len(paragraphs)
	earlier_known = float(frame.earlier_decision_maker.known)
	minister_applicant = float(frame.applicant_is_minister.known and frame.applicant_is_minister.value in (True, "yes"))
	rows = []
	for i, (text, res) in enumerate(zip(paragraphs, results)):
		sentences = res.sentence_holders
		count = [sum(1 for h in sentences if h == k) for k in HOLDERS]
		per = max(1, len(sentences))
		row = [i / max(1, n - 1), min(len(text), 2500) / 2500]
		row += [c / per for c in count] + [float(c > 0) for c in count]
		row += [float(res.primary == k) for k in HOLDERS]
		explicit = [c.holder for c in res.cues if c.confidence == "explicit"]
		carried = [c.holder for c in res.cues if c.confidence == "carried"]
		row += [float(k in explicit) for k in HOLDERS] + [float(k in carried) for k in HOLDERS]
		row += [float(layer in res.layers) for layer in range(1, 7)] + [float(res.has_framework), float(res.mixed_layers)]
		row += [float(roles[i] == k) for k in cs.ROLES]
		row += [float(forum == k) for k in FORUMS]
		row += [earlier_known, minister_applicant]
		rows.append(row)
	return np.array(rows, dtype=np.float64).reshape(n, -1), [r.primary for r in results]


def stack_features(log_p: np.ndarray, dense: np.ndarray) -> np.ndarray:
	"""Stage-2 inputs: stage-1 log-probabilities, the dense features, and the log-probabilities two paragraphs each way."""
	parts = [log_p, dense]
	for shift in (-2, -1, 1, 2):
		moved = np.roll(log_p, shift, axis=0)
		if shift > 0:
			moved[:shift] = _FLOOR
		else:
			moved[shift:] = _FLOOR
		parts.append(moved)
	return np.hstack(parts)


@lru_cache(maxsize=1)
def _weights():
	if not WEIGHTS_PATH.exists():
		return None
	data = np.load(WEIGHTS_PATH)
	stage1 = (data["sparse"].astype(np.float32), data["dense"].astype(np.float32), data["bias"].astype(np.float64))
	stage2 = tuple(data[k].astype(np.float64) for k in ("s2_coef", "s2_bias", "s2_mean", "s2_scale"))
	return stage1, stage2


def available() -> bool:
	return _weights() is not None


def _log_softmax(scores: np.ndarray) -> np.ndarray:
	scores = scores - scores.max(axis=1, keepdims=True)
	return np.maximum(scores - np.log(np.exp(scores).sum(axis=1, keepdims=True)), _FLOOR)


def stage_one(paragraphs: Sequence[str], dense: np.ndarray) -> np.ndarray:
	sparse, dense_w, bias = _weights()[0]  # type: ignore[index]
	scores = dense @ dense_w.T + bias
	for i, text in enumerate(paragraphs):
		feats = text_features(text)
		if feats:
			idx = np.fromiter(feats.keys(), dtype=np.int64)
			val = np.fromiter(feats.values(), dtype=np.float64)
			scores[i] += sparse[:, idx] @ val
	return _log_softmax(scores)


def probabilities(paragraphs: Sequence[str], title: str = "", header: str = "", body: str = "") -> np.ndarray:
	"""n x len(HOLDERS) probabilities, columns in ``HOLDERS`` order."""
	dense, _ = dense_features(paragraphs, title, header, body)
	log_p = stage_one(paragraphs, dense)
	coef, intercept, mean, scale = _weights()[1]  # type: ignore[index]
	x = (stack_features(log_p, dense) - mean) / scale
	return np.exp(_log_softmax(x @ coef.T + intercept))


def tag_paragraphs(paragraphs: Sequence[str], title: str = "", header: str = "", body: str = "") -> list[dict]:
	"""Main holder and its probability for each paragraph. Falls back to the rules when the weights are missing."""
	if not paragraphs:
		return []
	if not available():
		_, rule_holders = dense_features(paragraphs, title, header, body)
		return [{"holder": h, "p": None, "source": "rules"} for h in rule_holders]
	probs = probabilities(paragraphs, title, header, body)
	return [{"holder": HOLDERS[int(row.argmax())], "p": round(float(row.max()), 3), "source": "learned"} for row in probs]


def tag_decision_text(full_text: str, title: str = "") -> tuple[list[int], list[dict]]:
	"""Printed paragraph numbers and a tag for each, from a decision's stored text."""
	header, body = split_header(full_text)
	numbered = split_numbered_paragraphs(full_text)
	numbers = sorted(numbered)
	return numbers, tag_paragraphs([numbered[n] for n in numbers], title, header, body)
