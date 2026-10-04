"""Offline, read-only phrase analysis for tag-specific decision outcomes.

This module extracts 2-4 word phrases from case text and analyzes their
association with allowed (applicant wins) vs. dismissed (minister wins)
decisions for a specific legal tag. The analysis uses document frequency
and is capped to a bounded set of decisions.

**Important caution**: Phrase associations describe wording patterns
observed in decisions, not causes of outcomes. Correlation is not causation.
"""

from __future__ import annotations

import math
import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Any

from sqlalchemy import cast, select
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Session

from .database import Case, CaseJudgeProfile, JudgeProfile

MAX_DECISIONS = 10_000
LANGUAGE_ANALYTICS_CAUTION = (
	"Phrases describe wording patterns in decisions, not causes of outcomes."
)

def _issue_outcome_category(metadata_json: Any) -> str:
	"""Determine outcome category from metadata.

	Returns 'minister_win' for "won", 'applicant_win' for "lost",
	'other' for "mixed", 'unclassified' otherwise.
	"""
	metadata = metadata_json if isinstance(metadata_json, dict) else {}
	reader = metadata.get("reader_extracted")
	reader = reader if isinstance(reader, dict) else {}
	outcome = reader.get("government outcome")
	if not isinstance(outcome, str) or not outcome.strip():
		return "unclassified"
	normalized = outcome.strip().casefold()
	if normalized == "won":
		return "minister_win"
	if normalized == "lost":
		return "applicant_win"
	if normalized == "mixed":
		return "other"
	return "unclassified"


def _normalize_phrase(phrase: str) -> str:
	"""Normalize phrase for comparison: lowercase, strip whitespace."""
	return " ".join(phrase.split()).casefold()


def _extract_phrases(text: str | None, min_words: int = 2, max_words: int = 4) -> set[str]:
	"""Extract normalized n-grams (2-4 word phrases) from text.

	Args:
		text: Text to extract phrases from.
		min_words: Minimum phrase length in words.
		max_words: Maximum phrase length in words.

	Returns:
		Set of normalized phrases (no duplicates).
	"""
	if not text or not isinstance(text, str):
		return set()

	# Tokenize rather than stripping punctuation from whitespace-delimited words:
	# otherwise a sentence boundary such as "court.The" would merge two tokens.
	words = re.findall(r"[^\W_]+(?:['’][^\W_]+|-[^\W_]+)*", text.casefold(), re.UNICODE)

	phrases = set()
	for n in range(min_words, max_words + 1):
		for i in range(len(words) - n + 1):
			phrase = " ".join(words[i : i + n])
			if phrase:
				phrases.add(phrase)

	return phrases


def _phrase_appears_in_text(phrase: str, text: str | None) -> bool:
	"""Check if phrase appears in text (case-insensitive word boundary check)."""
	if not text or not isinstance(text, str):
		return False
	# Simple substring check - phrase appears as consecutive words
	pattern = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
	return bool(pattern.search(text))


def _calculate_phrase_score(
	allowed_count: int,
	dismissed_count: int,
	allowed_denominator: int,
	dismissed_denominator: int,
	smoothing: float = 1.0,
) -> float:
	"""Calculate a normalized, interpretable group-rate score using log2-smoothed rate ratio.

	A phrase's score reflects how much more frequently it appears in one group
	versus the other, adjusted for group size and using smoothing to avoid
	extreme values when document frequencies are low.

	Args:
		allowed_count: Number of allowed (applicant_win) documents containing phrase
		dismissed_count: Number of dismissed (minister_win) documents containing phrase
		allowed_denominator: Total allowed documents in corpus
		dismissed_denominator: Total dismissed documents in corpus
		smoothing: Smoothing factor (default 1.0 for log2-smoothed Laplace smoothing)

	Returns:
		log2-smoothed rate ratio. Positive values indicate association with allowed group;
		negative values indicate association with dismissed group. Magnitude indicates strength.
	"""
	# Avoid zero denominators
	if allowed_denominator <= 0 or dismissed_denominator <= 0:
		return 0.0

	# Beta-binomial smoothing: one pseudo-observation of each outcome.
	allowed_rate = (allowed_count + smoothing) / (allowed_denominator + 2 * smoothing)
	dismissed_rate = (dismissed_count + smoothing) / (dismissed_denominator + 2 * smoothing)

	# Avoid log(0) or log(negative): ensure rates > 0
	if allowed_rate <= 0 or dismissed_rate <= 0:
		return 0.0

	# Log2 rate ratio: positive for allowed, negative for dismissed
	return math.log2(allowed_rate / dismissed_rate)


@dataclass
class PhraseAnalysisResult:
	"""Result of phrase analysis for a tag."""

	tag: str
	judge_slug: str | None
	decisions_scanned: int
	"""Number of case decisions examined during phrase analysis.
	A decision scan means one case decision document was loaded from the corpus,
	examined for phrases, and classified by outcome. Scanned count includes
	unclassified decisions but is capped at max_decisions parameter."""
	decisions_capped: bool
	allowed_denominator: int
	"""Exact count of decisions classified as applicant_win (allowed) in the analyzed corpus."""
	dismissed_denominator: int
	"""Exact count of decisions classified as minister_win (dismissed) in the analyzed corpus."""
	excluded_unclassified: int
	"""Count of scanned decisions excluded from analysis due to unclassified/other outcome."""
	allowed_phrases: list[dict[str, Any]]  # [{"phrase": str, "count": int, "score": float}, ...]
	dismissed_phrases: list[dict[str, Any]]

	def to_dict(self, top_phrases_per_side: int = 25) -> dict[str, Any]:
		"""Serialize the shared response contract for the CLI and API."""
		return {
			"tag": self.tag,
			"judge_slug": self.judge_slug,
			"decisions_scanned": self.decisions_scanned,
			"decisions_capped": self.decisions_capped,
			"allowed_denominator": self.allowed_denominator,
			"dismissed_denominator": self.dismissed_denominator,
			"excluded_unclassified": self.excluded_unclassified,
			"caution": LANGUAGE_ANALYTICS_CAUTION,
			"allowed_phrases": self.allowed_phrases[:top_phrases_per_side],
			"dismissed_phrases": self.dismissed_phrases[:top_phrases_per_side],
		}


def analyze_phrases_in_memory(
	decisions: list[dict[str, Any]],
	tag: str,
	judge_slug: str | None = None,
	max_decisions: int = MAX_DECISIONS,
	min_phrase_frequency: int = 5,
	top_phrases_per_side: int = 25,
) -> PhraseAnalysisResult:
	"""Analyze fixture decisions without opening a database connection.

	When ``issues`` is present, a decision must match the requested tag after
	whitespace and case normalization. Inputs without an ``issues`` key are
	treated as an already tag-filtered corpus, which is useful for small fixtures.
	"""
	if not tag or not tag.strip():
		raise ValueError("Tag cannot be empty or whitespace-only")
	_validate_analysis_bounds(max_decisions, min_phrase_frequency, top_phrases_per_side)
	normalized_tag = _normalize_phrase(tag)
	filtered = []
	for decision in decisions:
		issues = decision.get("issues")
		if issues is not None and normalized_tag not in {
			_normalize_phrase(issue) for issue in issues if isinstance(issue, str)
		}:
			continue
		if judge_slug and decision.get("judge_slug") != judge_slug.strip():
			continue
		filtered.append(decision)
	return _analyze_decisions(
		filtered, tag, judge_slug, max_decisions, min_phrase_frequency, top_phrases_per_side
	)


def _validate_analysis_bounds(
	max_decisions: int, min_phrase_frequency: int, top_phrases_per_side: int
) -> None:
	if max_decisions <= 0 or max_decisions > MAX_DECISIONS:
		raise ValueError(f"max_decisions must be between 1 and {MAX_DECISIONS}, got {max_decisions}")
	if min_phrase_frequency < 1:
		raise ValueError(f"min_phrase_frequency must be >= 1, got {min_phrase_frequency}")
	if top_phrases_per_side < 1:
		raise ValueError(f"top_phrases_per_side must be >= 1, got {top_phrases_per_side}")


def _build_decision_query(tag: str, judge_id: int | None, max_decisions: int):
	"""Build an exact-tag, optional-judge query capped before row materialization."""
	query = select(Case.summary, Case.full_text, Case.metadata_json).where(
		cast(Case.issues, JSONB).contains([tag.strip()])
	)
	if judge_id is not None:
		query = query.join(
			CaseJudgeProfile, Case.id == CaseJudgeProfile.case_id
		).where(CaseJudgeProfile.judge_profile_id == judge_id)
	return query.order_by(Case.id).limit(max_decisions + 1)


def _analyze_decisions(
	decisions: list[dict[str, Any]],
	tag: str,
	judge_slug: str | None,
	max_decisions: int,
	min_phrase_frequency: int,
	top_phrases_per_side: int,
) -> PhraseAnalysisResult:
	"""Analyze an already tag/judge-filtered, stably ordered decision corpus."""
	capped = len(decisions) > max_decisions
	scanned = decisions[:max_decisions]
	allowed_docs: dict[str, set[int]] = defaultdict(set)
	dismissed_docs: dict[str, set[int]] = defaultdict(set)
	allowed_denominator = dismissed_denominator = excluded_unclassified = 0

	for doc_index, decision in enumerate(scanned):
		outcome = _issue_outcome_category(decision.get("metadata_json"))
		if outcome not in {"applicant_win", "minister_win"}:
			excluded_unclassified += 1
			continue
		text = f"{decision.get('summary') or ''} {decision.get('full_text') or ''}"
		group = allowed_docs if outcome == "applicant_win" else dismissed_docs
		if outcome == "applicant_win":
			allowed_denominator += 1
		else:
			dismissed_denominator += 1
		for phrase in _extract_phrases(text):
			group[phrase].add(doc_index)

	allowed_counts = {
		phrase: len(documents)
		for phrase, documents in allowed_docs.items()
		if len(documents) >= min_phrase_frequency
	}
	dismissed_counts = {
		phrase: len(documents)
		for phrase, documents in dismissed_docs.items()
		if len(documents) >= min_phrase_frequency
	}
	phrases = allowed_counts.keys() | dismissed_counts.keys()
	scores = {
		phrase: _calculate_phrase_score(
			len(allowed_docs.get(phrase, set())),
			len(dismissed_docs.get(phrase, set())),
			allowed_denominator,
			dismissed_denominator,
		)
		for phrase in phrases
	}
	allowed_top = sorted(
		(
			(phrase, score) for phrase, score in scores.items()
			if phrase in allowed_counts and score > 0
		),
		key=lambda item: (-item[1], item[0]),
	)[:top_phrases_per_side]
	dismissed_top = sorted(
		(
			(phrase, score) for phrase, score in scores.items()
			if phrase in dismissed_counts and score < 0
		),
		key=lambda item: (item[1], item[0]),
	)[:top_phrases_per_side]

	def phrase_row(phrase: str, score: float) -> dict[str, Any]:
		allowed_count = len(allowed_docs.get(phrase, set()))
		dismissed_count = len(dismissed_docs.get(phrase, set()))
		return {
			"phrase": phrase,
			"count": allowed_count if score > 0 else dismissed_count,
			"allowed_count": allowed_count,
			"dismissed_count": dismissed_count,
			"score": score,
		}

	return PhraseAnalysisResult(
		tag=tag,
		judge_slug=judge_slug,
		decisions_scanned=len(scanned),
		decisions_capped=capped,
		allowed_denominator=allowed_denominator,
		dismissed_denominator=dismissed_denominator,
		excluded_unclassified=excluded_unclassified,
		allowed_phrases=[phrase_row(phrase, score) for phrase, score in allowed_top],
		dismissed_phrases=[phrase_row(phrase, score) for phrase, score in dismissed_top],
	)


def analyze_phrases_for_tag(
	db: Session,
	tag: str,
	judge_slug: str | None = None,
	max_decisions: int = MAX_DECISIONS,
	min_phrase_frequency: int = 5,
	top_phrases_per_side: int = 25,
) -> PhraseAnalysisResult:
	"""Analyze 2-4 word phrases for a tag, comparing allowed vs. dismissed decisions.

	The tag match is exact against the stored ``cases.issues`` array. SQL filters
	tag and optional judge before applying the deterministic scan cap; at most
	``max_decisions + 1`` rows are materialized to determine whether capped.
	A scanned decision is one matching case loaded from that bounded query,
	including decisions later excluded for unclassified outcomes.

	Args:
		db: SQLAlchemy session.
		tag: Legal tag to filter decisions. Empty or whitespace-only tags raise ValueError.
		judge_slug: Optional judge profile slug to filter decisions.
				   If provided but not found, returns empty result (no fallback to all judges).
		max_decisions: Maximum decisions to scan (cap). Must be > 0.
		min_phrase_frequency: Minimum document frequency for phrases (>= 1).
		top_phrases_per_side: Number of top phrases to return per side (>= 1).

	Returns:
		PhraseAnalysisResult with phrase counts and group denominators.

	Raises:
		ValueError: If tag is empty/whitespace or parameters are invalid.

	**Caution**: Results describe word associations in decisions, not causes
	of outcomes.
	"""
	if not tag or not tag.strip():
		raise ValueError("Tag cannot be empty or whitespace-only")
	_validate_analysis_bounds(max_decisions, min_phrase_frequency, top_phrases_per_side)

	# Resolve judge_slug to judge_id if provided
	judge_id = None
	if judge_slug and judge_slug.strip():
		judge_id = db.execute(
			select(JudgeProfile.id).where(JudgeProfile.slug == judge_slug.strip())
		).scalar()
		if not judge_id:
			return _analyze_decisions(
				[], tag, judge_slug, max_decisions, min_phrase_frequency, top_phrases_per_side
			)

	# The JSON array tag predicate runs before the bounded result limit.
	rows = db.execute(_build_decision_query(tag, judge_id, max_decisions)).fetchall()
	decisions = [
		{"summary": summary, "full_text": full_text, "metadata_json": metadata}
		for summary, full_text, metadata in rows
	]
	return _analyze_decisions(
		decisions, tag, judge_slug, max_decisions, min_phrase_frequency, top_phrases_per_side
	)
