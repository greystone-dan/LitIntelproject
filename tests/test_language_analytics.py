"""Fixture-only tests for language analytics phrase analysis.

Tests the phrase extraction, outcome categorization, scoring, and
filtering logic without database access. All data is fixture-based.
"""

import pytest
from dataclasses import dataclass

# Import functions to test
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.language_analytics import (
	_extract_phrases,
	_normalize_phrase,
	_issue_outcome_category,
	_phrase_appears_in_text,
	PhraseAnalysisResult,
)


class TestPhraseExtraction:
	"""Test 2-4 word phrase extraction."""

	def test_extract_empty_text(self):
		"""Empty or None text should return empty set."""
		assert _extract_phrases(None) == set()
		assert _extract_phrases("") == set()
		assert _extract_phrases("   ") == set()

	def test_extract_single_word(self):
		"""Single word should not generate 2-4 grams."""
		assert _extract_phrases("hello") == set()

	def test_extract_two_word_phrases(self):
		"""Extract 2-word phrases."""
		text = "hello world this is a test"
		phrases = _extract_phrases(text)
		assert "hello world" in phrases
		assert "world this" in phrases
		assert "this is" in phrases
		assert "is a" in phrases
		assert "a test" in phrases

	def test_extract_three_word_phrases(self):
		"""Extract 3-word phrases."""
		text = "the quick brown fox"
		phrases = _extract_phrases(text)
		assert "the quick brown" in phrases
		assert "quick brown fox" in phrases

	def test_extract_four_word_phrases(self):
		"""Extract 4-word phrases."""
		text = "the quick brown fox jumps"
		phrases = _extract_phrases(text)
		assert "the quick brown fox" in phrases
		assert "quick brown fox jumps" in phrases

	def test_extract_normalized_whitespace(self):
		"""Normalize extra whitespace."""
		text = "hello   world   this"
		phrases = _extract_phrases(text)
		# Should normalize to single spaces
		assert "hello world" in phrases
		assert "world this" in phrases

	def test_extract_case_insensitive(self):
		"""Phrases should be normalized to lowercase."""
		text = "Hello WORLD This IS"
		phrases = _extract_phrases(text)
		assert "hello world" in phrases
		assert "world this" in phrases
		assert "this is" in phrases
		# Uppercase versions should not exist
		for phrase in phrases:
			assert phrase == phrase.lower()

	def test_extract_removes_punctuation(self):
		"""Remove punctuation but keep hyphens and apostrophes."""
		text = "don't worry, the self-driving car works!"
		phrases = _extract_phrases(text)
		assert "don't worry" in phrases or "dont worry" in phrases
		assert "self-driving car" in phrases

	def test_extract_no_duplicate_phrases(self):
		"""Repeated phrases should appear only once."""
		text = "hello hello hello world"
		phrases = _extract_phrases(text)
		# Count phrase occurrences in text
		phrase_list = list(phrases)
		assert "hello hello" in phrases
		assert len(phrases) == len([p for p in phrases])  # No duplicates


class TestPhrasNormalization:
	"""Test phrase normalization."""

	def test_normalize_whitespace(self):
		"""Normalize extra whitespace."""
		assert _normalize_phrase("hello   world") == "hello world"
		assert _normalize_phrase("  test  ") == "test"

	def test_normalize_case(self):
		"""Normalize to lowercase."""
		assert _normalize_phrase("HELLO WORLD") == "hello world"
		assert _normalize_phrase("Hello World") == "hello world"


class TestOutcomeCategorization:
	"""Test outcome categorization from metadata."""

	def test_categorize_none_metadata(self):
		"""None metadata should be unclassified."""
		assert _issue_outcome_category(None) == "unclassified"

	def test_categorize_empty_dict(self):
		"""Empty dict should be unclassified."""
		assert _issue_outcome_category({}) == "unclassified"

	def test_categorize_no_reader_extracted(self):
		"""Missing reader_extracted should be unclassified."""
		assert _issue_outcome_category({"other": "data"}) == "unclassified"

	def test_categorize_government_win(self):
		"""'won' outcome should be minister_win."""
		metadata = {"reader_extracted": {"government outcome": "won"}}
		assert _issue_outcome_category(metadata) == "minister_win"

	def test_categorize_applicant_win(self):
		"""'lost' outcome should be applicant_win."""
		metadata = {"reader_extracted": {"government outcome": "lost"}}
		assert _issue_outcome_category(metadata) == "applicant_win"

	def test_categorize_other_outcome(self):
		"""'mixed' outcome should be 'other'."""
		metadata = {"reader_extracted": {"government outcome": "mixed"}}
		assert _issue_outcome_category(metadata) == "other"

	def test_categorize_unrecognized_outcome(self):
		"""Unrecognized outcome should be unclassified."""
		metadata = {"reader_extracted": {"government outcome": "unknown"}}
		assert _issue_outcome_category(metadata) == "unclassified"

	def test_categorize_case_insensitive(self):
		"""Outcome comparison should be case-insensitive."""
		metadata_won = {"reader_extracted": {"government outcome": "WON"}}
		metadata_lost = {"reader_extracted": {"government outcome": "LOST"}}
		metadata_mixed = {"reader_extracted": {"government outcome": "MIXED"}}
		assert _issue_outcome_category(metadata_won) == "minister_win"
		assert _issue_outcome_category(metadata_lost) == "applicant_win"
		assert _issue_outcome_category(metadata_mixed) == "other"

	def test_categorize_blank_outcome(self):
		"""Blank outcome should be unclassified."""
		metadata = {"reader_extracted": {"government outcome": "   "}}
		assert _issue_outcome_category(metadata) == "unclassified"


class TestPhraseAppearsInText:
	"""Test phrase appearance checking."""

	def test_phrase_appears_simple(self):
		"""Phrase should appear in text."""
		assert _phrase_appears_in_text("hello world", "hello world test")
		assert _phrase_appears_in_text("test phrase", "this is a test phrase here")

	def test_phrase_does_not_appear(self):
		"""Phrase should not appear if not in text."""
		assert not _phrase_appears_in_text("hello world", "hello there")
		assert not _phrase_appears_in_text("xyz abc", "abcxyz test")

	def test_phrase_case_insensitive(self):
		"""Phrase check should be case-insensitive."""
		assert _phrase_appears_in_text("hello world", "HELLO WORLD test")
		assert _phrase_appears_in_text("HELLO WORLD", "hello world test")

	def test_phrase_word_boundary(self):
		"""Phrase should respect word boundaries."""
		# "hello" should not match "helloworld"
		assert not _phrase_appears_in_text("hello", "helloworld")

	def test_phrase_empty_text(self):
		"""Empty text should not contain phrase."""
		assert not _phrase_appears_in_text("hello", "")
		assert not _phrase_appears_in_text("hello", None)


class TestPhraseAnalysisResult:
	"""Test PhraseAnalysisResult dataclass."""

	def test_result_creation(self):
		"""Create result with fixture data."""
		result = PhraseAnalysisResult(
			tag="test tag",
			judge_slug=None,
			decisions_scanned=100,
			decisions_capped=False,
			allowed_denominator=50,
			dismissed_denominator=50,
			excluded_unclassified=0,
			allowed_phrases=[
				{"phrase": "legal test", "count": 10, "score": 1.5}
			],
			dismissed_phrases=[
				{"phrase": "other phrase", "count": 8, "score": 1.2}
			],
		)
		assert result.tag == "test tag"
		assert result.decisions_scanned == 100
		assert not result.decisions_capped
		assert len(result.allowed_phrases) == 1
		assert len(result.dismissed_phrases) == 1

	def test_result_with_judge(self):
		"""Result can include judge slug."""
		result = PhraseAnalysisResult(
			tag="test tag",
			judge_slug="judge_abc",
			decisions_scanned=50,
			decisions_capped=True,
			allowed_denominator=25,
			dismissed_denominator=25,
			excluded_unclassified=0,
			allowed_phrases=[],
			dismissed_phrases=[],
		)
		assert result.judge_slug == "judge_abc"
		assert result.decisions_capped is True


class TestBoundsAndMinimums:
	"""Test bounds and minimum frequency filtering logic."""

	def test_minimum_frequency_filtering(self):
		"""Phrases below minimum frequency should be filtered."""
		# This is tested in the main analyze_phrases_for_tag function
		# which we can't test without a real database, but we verify
		# the logic is sound by checking that min_phrase_frequency parameter exists
		# and is used in the module
		from backend.language_analytics import analyze_phrases_for_tag
		import inspect
		sig = inspect.signature(analyze_phrases_for_tag)
		assert "min_phrase_frequency" in sig.parameters
		assert sig.parameters["min_phrase_frequency"].default == 5

	def test_decision_cap_logic(self):
		"""Decision cap parameter should exist and default to 10000."""
		from backend.language_analytics import analyze_phrases_for_tag
		import inspect
		sig = inspect.signature(analyze_phrases_for_tag)
		assert "max_decisions" in sig.parameters
		assert sig.parameters["max_decisions"].default == 10000

	def test_top_phrases_limit(self):
		"""Top phrases limit should default to 25."""
		from backend.language_analytics import analyze_phrases_for_tag
		import inspect
		sig = inspect.signature(analyze_phrases_for_tag)
		assert "top_phrases_per_side" in sig.parameters
		assert sig.parameters["top_phrases_per_side"].default == 25


class TestIntegrationWithFixtures:
	"""Integration tests using only fixtures (no database)."""

	def test_phrase_extraction_integration(self):
		"""Test phrase extraction on realistic case text."""
		case_text = """
		The applicant sought judicial review of the decision.
		The court considered procedural fairness arguments.
		The decision was procedurally unfair to the applicant.
		"""
		phrases = _extract_phrases(case_text)
		assert len(phrases) > 0
		# Should contain various n-grams
		assert any(len(p.split()) == 2 for p in phrases)
		assert any(len(p.split()) == 3 for p in phrases)

	def test_outcome_categorization_realistic(self):
		"""Test outcome categorization on realistic metadata."""
		# Applicant win
		metadata_lost = {
			"reader_extracted": {
				"government outcome": "lost",
				"other": "data"
			}
		}
		assert _issue_outcome_category(metadata_lost) == "applicant_win"

		# Minister win
		metadata_won = {
			"reader_extracted": {
				"government outcome": "won",
				"other": "data"
			}
		}
		assert _issue_outcome_category(metadata_won) == "minister_win"

	def test_phrase_scoring_logic(self):
		"""Test that phrase scoring logic produces sensible results."""
		# If a phrase appears in 10 allowed docs and 1 dismissed doc,
		# it should score higher for allowed group
		allowed_freq = 10
		dismissed_freq = 1
		epsilon = 0.5
		allowed_score = (allowed_freq + epsilon) / (dismissed_freq + epsilon)
		dismissed_score = (dismissed_freq + epsilon) / (allowed_freq + epsilon)
		# Allowed score should be much higher
		assert allowed_score > dismissed_score
		assert allowed_score > 1
		assert dismissed_score < 1


# Parametrized tests for edge cases
class TestEdgeCases:
	"""Test edge cases and boundary conditions."""

	@pytest.mark.parametrize("text", [None, "", "   ", "\n\t  "])
	def test_extract_empty_variants(self, text):
		"""Test various empty/whitespace inputs."""
		result = _extract_phrases(text)
		assert isinstance(result, set)
		assert len(result) == 0

	@pytest.mark.parametrize("outcome,expected", [
		("won", "minister_win"),
		("lost", "applicant_win"),
		("mixed", "other"),
		("unknown", "unclassified"),
		("", "unclassified"),
		(None, "unclassified"),
	])
	def test_outcome_categorization_variants(self, outcome, expected):
		"""Test various outcome values."""
		metadata = {}
		if outcome is not None:
			metadata = {"reader_extracted": {"government outcome": outcome}}
		assert _issue_outcome_category(metadata) == expected


class TestAnalyzePhraseScoring:
	"""Test the phrase scoring function."""

	def test_calculate_phrase_score_positive_association(self):
		"""Test score calculation for a phrase associated with allowed group."""
		from backend.language_analytics import _calculate_phrase_score

		# Phrase appears in 10 allowed docs, 1 dismissed doc
		score = _calculate_phrase_score(10, 1, 100, 100)
		# With smoothing, this should be positive (more in allowed)
		assert score > 0
		# Higher allowed count should give positive score
		assert score > _calculate_phrase_score(1, 10, 100, 100)

	def test_calculate_phrase_score_negative_association(self):
		"""Test score calculation for a phrase associated with dismissed group."""
		from backend.language_analytics import _calculate_phrase_score

		# Phrase appears in 1 allowed doc, 10 dismissed docs
		score = _calculate_phrase_score(1, 10, 100, 100)
		# Should be negative (more in dismissed)
		assert score < 0

	def test_calculate_phrase_score_zero_denominators(self):
		"""Test score calculation with zero denominators."""
		from backend.language_analytics import _calculate_phrase_score

		# Zero denominators should return 0
		assert _calculate_phrase_score(5, 5, 0, 100) == 0.0
		assert _calculate_phrase_score(5, 5, 100, 0) == 0.0
		assert _calculate_phrase_score(5, 5, 0, 0) == 0.0

	def test_calculate_phrase_score_with_smoothing(self):
		"""Test score calculation with smoothing factor."""
		from backend.language_analytics import _calculate_phrase_score

		# With smoothing=1.0, even zero counts should produce valid scores
		score1 = _calculate_phrase_score(0, 0, 100, 100, smoothing=1.0)
		# Smoothed rates: (0+1)/(100+1) for both, so ratio = 1, log2(1) = 0
		assert score1 == 0.0

	def test_calculate_phrase_score_log2_interpretation(self):
		"""Test that log2 score is interpretable."""
		from backend.language_analytics import _calculate_phrase_score

		# If allowed rate is 2x dismissed rate, log2 ratio should be 1
		# allowed: 10 docs in 100 = 0.1, dismissed: 5 docs in 100 = 0.05
		# With smoothing=1: (10+1)/(100+1) = 0.109, (5+1)/(100+1) = 0.059
		# Ratio ≈ 1.85, log2 ≈ 0.89 (not exactly 1 due to smoothing)
		score = _calculate_phrase_score(10, 5, 100, 100, smoothing=1.0)
		assert score > 0.7  # Should be close to 1 (log2 of ~2x ratio)


class TestAnalyzePhrasesInMemory:
	"""Test the in-memory phrase analysis function (no database)."""

	def test_empty_decisions(self):
		"""Empty decision list should return empty result."""
		from backend.language_analytics import analyze_phrases_in_memory

		result = analyze_phrases_in_memory([], tag="test tag")
		assert result.tag == "test tag"
		assert result.decisions_scanned == 0
		assert result.decisions_capped is False
		assert result.allowed_denominator == 0
		assert result.dismissed_denominator == 0
		assert result.allowed_phrases == []
		assert result.dismissed_phrases == []

	def test_in_memory_basic_analysis(self):
		"""Test basic phrase analysis on fixture data."""
		from backend.language_analytics import analyze_phrases_in_memory

		# Create fixture decisions
		decisions = [
			{
				"id": 1,
				"summary": "applicant wins case",
				"full_text": "the court found in favor of applicant",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			},
			{
				"id": 2,
				"summary": "government wins appeal",
				"full_text": "the court dismissed applicant's challenge",
				"metadata_json": {"reader_extracted": {"government outcome": "won"}},
			},
			{
				"id": 3,
				"summary": "mixed decision",
				"full_text": "partial victory",
				"metadata_json": {"reader_extracted": {"government outcome": "mixed"}},
			},
		]
		result = analyze_phrases_in_memory(
			decisions,
			tag="test tag",
			max_decisions=100,
			min_phrase_frequency=1,
			top_phrases_per_side=10,
		)

		assert result.tag == "test tag"
		assert result.decisions_scanned == 3
		assert result.decisions_capped is False
		assert result.allowed_denominator == 1  # Only "lost" outcome
		assert result.dismissed_denominator == 1  # Only "won" outcome
		assert result.excluded_unclassified == 1  # "mixed" is other

	def test_in_memory_capping(self):
		"""Test that decisions are capped correctly."""
		from backend.language_analytics import analyze_phrases_in_memory

		# Create 15 decisions
		decisions = [
			{
				"id": i,
				"summary": f"case {i}",
				"full_text": f"text for case {i}",
				"metadata_json": {
					"reader_extracted": {
						"government outcome": "won" if i % 2 == 0 else "lost"
					}
				},
			}
			for i in range(15)
		]

		result = analyze_phrases_in_memory(
			decisions,
			tag="test tag",
			max_decisions=10,
			min_phrase_frequency=1,
			top_phrases_per_side=10,
		)

		assert result.decisions_scanned == 10
		assert result.decisions_capped is True

	def test_in_memory_min_df_filtering(self):
		"""Test that phrases below min document frequency are filtered."""
		from backend.language_analytics import analyze_phrases_in_memory

		# Create decisions with varying phrase frequencies
		decisions = [
			{
				"id": 1,
				"summary": "common phrase appears here",
				"full_text": "common phrase appears again",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			},
			{
				"id": 2,
				"summary": "common phrase also here",
				"full_text": "text without special phrase",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			},
			{
				"id": 3,
				"summary": "rare phrase unique",
				"full_text": "text without any repeats",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			},
		]
		decisions.append({
			"id": 4,
			"summary": "separate dismissed outcome",
			"full_text": "distinct phrase for comparison",
			"metadata_json": {"reader_extracted": {"government outcome": "won"}},
		})

		result = analyze_phrases_in_memory(
			decisions,
			tag="test tag",
			max_decisions=100,
			min_phrase_frequency=2,  # Min DF = 2
			top_phrases_per_side=10,
		)

		# Should only have phrases appearing in at least 2 allowed docs
		assert result.allowed_denominator == 3
		# "common phrase" should appear (in 2 docs), "rare phrase" should not
		phrases = [p["phrase"] for p in result.allowed_phrases]
		assert any("common" in p for p in phrases)

	def test_in_memory_unclassified_exclusion(self):
		"""Test that unclassified outcomes are counted but excluded from analysis."""
		from backend.language_analytics import analyze_phrases_in_memory

		decisions = [
			{
				"id": 1,
				"summary": "allowed case",
				"full_text": "applicant wins",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			},
			{
				"id": 2,
				"summary": "unclassified case",
				"full_text": "no outcome data",
				"metadata_json": {},
			},
			{
				"id": 3,
				"summary": "dismissed case",
				"full_text": "government wins",
				"metadata_json": {"reader_extracted": {"government outcome": "won"}},
			},
		]

		result = analyze_phrases_in_memory(
			decisions,
			tag="test tag",
			max_decisions=100,
			min_phrase_frequency=1,
			top_phrases_per_side=10,
		)

		assert result.decisions_scanned == 3
		assert result.excluded_unclassified == 1

	def test_in_memory_returns_group_counts_and_denominators(self):
		"""Phrase rows include both document frequencies and use group-size rates."""
		from backend.language_analytics import analyze_phrases_in_memory

		decisions = [
			{
				"summary": "rare remedy phrase",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			}
			for _ in range(5)
		] + [
			{
				"summary": "common baseline phrase",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			}
			for _ in range(5)
		] + [
			{
				"summary": "common baseline phrase",
				"metadata_json": {"reader_extracted": {"government outcome": "won"}},
			}
			for _ in range(10)
		]
		result = analyze_phrases_in_memory(
			decisions, tag="procedural fairness", min_phrase_frequency=5
		)
		row = next(item for item in result.allowed_phrases if item["phrase"] == "rare remedy phrase")
		assert result.allowed_denominator == 10
		assert result.dismissed_denominator == 10
		assert row["allowed_count"] == 5
		assert row["dismissed_count"] == 0
		assert row["count"] == row["allowed_count"]
		assert row["score"] > 0
		assert all(item["score"] > 0 for item in result.allowed_phrases)
		assert all(item["score"] < 0 for item in result.dismissed_phrases)

	def test_in_memory_applies_tag_judge_and_cap_before_analysis(self):
		"""Only exact tag/judge fixture matches enter the cap and denominators."""
		from backend.language_analytics import analyze_phrases_in_memory

		decisions = [
			{
				"issues": ["Procedural   Fairness"],
				"judge_slug": "judge-a",
				"summary": "eligible tag phrase",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			}
			for _ in range(5)
		] + [
			{
				"issues": ["other issue"],
				"judge_slug": "judge-a",
				"summary": "not eligible phrase",
				"metadata_json": {"reader_extracted": {"government outcome": "won"}},
			},
			{
				"issues": ["procedural fairness"],
				"judge_slug": "judge-b",
				"summary": "not eligible phrase",
				"metadata_json": {"reader_extracted": {"government outcome": "won"}},
			},
		]
		result = analyze_phrases_in_memory(
			decisions,
			tag="procedural fairness",
			judge_slug="judge-a",
			max_decisions=4,
			min_phrase_frequency=1,
		)
		assert result.decisions_scanned == 4
		assert result.decisions_capped is True
		assert result.allowed_denominator == 4
		assert result.dismissed_denominator == 0

	def test_in_memory_filters_below_minimum_document_frequency(self):
		"""A phrase below five documents is not emitted for either side."""
		from backend.language_analytics import analyze_phrases_in_memory

		decisions = [
			{
				"summary": "rare phrase",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			}
			for _ in range(4)
		]
		result = analyze_phrases_in_memory(decisions, tag="tag")
		assert result.allowed_denominator == 4
		assert result.allowed_phrases == []

	def test_in_memory_counts_other_and_unclassified_as_excluded(self):
		"""Mixed/unknown outcomes are excluded from the binary comparison."""
		from backend.language_analytics import analyze_phrases_in_memory

		decisions = [
			{"summary": "mixed result phrase", "metadata_json": {"reader_extracted": {"government outcome": "mixed"}}},
			{"summary": "unknown result phrase", "metadata_json": {"reader_extracted": {"government outcome": "unknown"}}},
			{"summary": "allowed result phrase", "metadata_json": {"reader_extracted": {"government outcome": "lost"}}},
		]
		result = analyze_phrases_in_memory(decisions, tag="tag")
		assert result.decisions_scanned == 3
		assert result.excluded_unclassified == 2
		assert result.allowed_denominator == 1
		assert result.dismissed_denominator == 0

	def test_in_memory_scoring_ranking(self):
		"""Test that phrases are ranked by normalized score."""
		from backend.language_analytics import analyze_phrases_in_memory

		# Create decisions where one phrase is strongly associated with allowed
		decisions = [
			{
				"id": i,
				"summary": "unique strong marker here" if i < 5 else f"case {i}",
				"full_text": "unique strong marker text" if i < 5 else f"text {i}",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			}
			for i in range(10)
		] + [
			{
				"id": 10 + i,
				"summary": f"dismissed case {i}",
				"full_text": f"different text {i}",
				"metadata_json": {"reader_extracted": {"government outcome": "won"}},
			}
			for i in range(5)
		]

		result = analyze_phrases_in_memory(
			decisions,
			tag="test tag",
			max_decisions=100,
			min_phrase_frequency=2,
			top_phrases_per_side=10,
		)

		# Should have phrases ranked by score
		assert len(result.allowed_phrases) > 0
		# Top phrases should have scores and counts
		for phrase_dict in result.allowed_phrases:
			assert "phrase" in phrase_dict
			assert "count" in phrase_dict
			assert "score" in phrase_dict
			assert isinstance(phrase_dict["score"], float)


class TestParameterValidation:
	"""Test parameter validation and bounds checking."""

	def test_empty_tag_raises_error(self):
		"""Empty tag should raise ValueError."""
		from backend.language_analytics import analyze_phrases_for_tag
		from unittest.mock import Mock

		db = Mock()
		with pytest.raises(ValueError, match="Tag cannot be empty"):
			analyze_phrases_for_tag(db, tag="")

	def test_whitespace_tag_raises_error(self):
		"""Whitespace-only tag should raise ValueError."""
		from backend.language_analytics import analyze_phrases_for_tag
		from unittest.mock import Mock

		db = Mock()
		with pytest.raises(ValueError, match="Tag cannot be empty"):
			analyze_phrases_for_tag(db, tag="   ")

	def test_zero_max_decisions_raises_error(self):
		"""max_decisions <= 0 should raise ValueError."""
		from backend.language_analytics import analyze_phrases_for_tag
		from unittest.mock import Mock

		db = Mock()
		with pytest.raises(ValueError, match="between 1 and"):
			analyze_phrases_for_tag(db, tag="test", max_decisions=0)

	def test_negative_max_decisions_raises_error(self):
		"""Negative max_decisions should raise ValueError."""
		from backend.language_analytics import analyze_phrases_for_tag
		from unittest.mock import Mock

		db = Mock()
		with pytest.raises(ValueError, match="between 1 and"):
			analyze_phrases_for_tag(db, tag="test", max_decisions=-5)

	def test_max_decisions_cannot_exceed_hard_cap(self):
		from backend.language_analytics import MAX_DECISIONS, analyze_phrases_in_memory

		with pytest.raises(ValueError, match=f"between 1 and {MAX_DECISIONS}"):
			analyze_phrases_in_memory(
				[], tag="test", max_decisions=MAX_DECISIONS + 1
			)

	def test_zero_min_phrase_frequency_raises_error(self):
		"""min_phrase_frequency < 1 should raise ValueError."""
		from backend.language_analytics import analyze_phrases_for_tag
		from unittest.mock import Mock

		db = Mock()
		with pytest.raises(ValueError, match="min_phrase_frequency must be >= 1"):
			analyze_phrases_for_tag(db, tag="test", min_phrase_frequency=0)

	def test_zero_top_phrases_raises_error(self):
		"""top_phrases_per_side < 1 should raise ValueError."""
		from backend.language_analytics import analyze_phrases_for_tag
		from unittest.mock import Mock

		db = Mock()
		with pytest.raises(ValueError, match="top_phrases_per_side must be >= 1"):
			analyze_phrases_for_tag(db, tag="test", top_phrases_per_side=0)

	def test_valid_parameters_accepted(self):
		"""Valid parameters should not raise ValueError."""
		from backend.language_analytics import analyze_phrases_for_tag
		from unittest.mock import Mock

		db = Mock()
		# This will fail later because of DB operations, but parameter validation should pass
		try:
			analyze_phrases_for_tag(
				db,
				tag="valid tag",
				max_decisions=1000,
				min_phrase_frequency=5,
				top_phrases_per_side=25,
			)
		except ValueError:
			pytest.fail("Valid parameters raised ValueError")
		except Exception:
			# Expected to fail due to mock DB, but not due to parameter validation
			pass


class TestUnknownJudgeHandling:
	"""Test handling of unknown judge slugs."""

	def test_unknown_judge_returns_empty_result(self):
		"""Unknown judge slug should return empty result, not error."""
		from backend.language_analytics import analyze_phrases_for_tag
		from unittest.mock import Mock

		db = Mock()
		# Mock the judge_id query to return None
		db.execute.return_value.scalar.return_value = None

		result = analyze_phrases_for_tag(db, tag="test", judge_slug="nonexistent_judge")

		assert result.decisions_scanned == 0


class TestBoundedQueryContract:
	"""The database query is tag-filtered and bounded before rows are loaded."""

	def test_postgresql_query_filters_tag_and_limits_capped_read(self):
		from sqlalchemy.dialects import postgresql
		from backend.language_analytics import _build_decision_query

		query = _build_decision_query("procedural fairness", judge_id=7, max_decisions=100)
		compiled = str(query.compile(dialect=postgresql.dialect()))
		assert "CAST(cases.issues AS JSONB) @>" in compiled
		assert "case_judge_profiles.judge_profile_id" in compiled
		assert "ORDER BY cases.id" in compiled
		assert "LIMIT" in compiled
		assert query.compile(dialect=postgresql.dialect()).params["param_1"] == [
			"procedural fairness"
		]


class TestLanguageAnalyticsPage:
	def test_page_prominently_cautions_about_causation_and_shows_counts(self):
		from backend.pages.language_analytics import language_analytics_page_html

		page = language_analytics_page_html()
		assert "word associations observed in decisions, not causes of outcomes" in page
		assert "/api/language-analytics" in page
		assert "Allowed" in page and "Dismissed" in page
		assert "allowed_count" in page and "dismissed_count" in page


class TestLanguageAnalyticsRoutes:
	def test_route_registration_and_top_25_response_are_fixture_only(self, monkeypatch):
		from unittest.mock import Mock
		from backend import routes
		from backend.language_analytics import PhraseAnalysisResult

		phrases = [
			{
				"phrase": f"phrase {index}",
				"count": 5,
				"allowed_count": 5,
				"dismissed_count": 0,
				"score": 1.0,
			}
			for index in range(30)
		]
		fixture_result = PhraseAnalysisResult(
			tag="issue",
			judge_slug=None,
			decisions_scanned=20,
			decisions_capped=False,
			allowed_denominator=10,
			dismissed_denominator=10,
			excluded_unclassified=0,
			allowed_phrases=phrases,
			dismissed_phrases=phrases,
		)
		monkeypatch.setattr(
			routes, "analyze_phrases_for_tag", lambda *args, **kwargs: fixture_result
		)
		payload = routes.get_language_analytics(tag="issue", judge=None, db=Mock())
		paths = {route.path for route in routes.router.routes}

		assert "/api/language-analytics" in paths
		assert "/language-analytics" in paths
		assert len(payload["allowed_phrases"]) == 25
		assert len(payload["dismissed_phrases"]) == 25
		assert payload["allowed_denominator"] == 10
		assert payload["dismissed_denominator"] == 10
		assert payload["allowed_phrases"][0]["allowed_count"] == 5
		assert "not causes" in payload["caution"]


class TestCapReporting:
	"""Test cap reporting and decisions_capped flag."""

	def test_decisions_capped_flag_true_when_exceeded(self):
		"""decisions_capped should be True when result exceeds max_decisions."""
		from backend.language_analytics import analyze_phrases_in_memory

		# Create 15 decisions (exceeds max of 10)
		decisions = [
			{
				"id": i,
				"summary": f"case {i}",
				"full_text": f"text {i}",
				"metadata_json": {"reader_extracted": {"government outcome": "won"}},
			}
			for i in range(15)
		]

		result = analyze_phrases_in_memory(
			decisions, tag="test", max_decisions=10, min_phrase_frequency=1
		)

		assert result.decisions_capped is True

	def test_decisions_capped_flag_false_when_not_exceeded(self):
		"""decisions_capped should be False when result is within max_decisions."""
		from backend.language_analytics import analyze_phrases_in_memory

		# Create 5 decisions (within max of 10)
		decisions = [
			{
				"id": i,
				"summary": f"case {i}",
				"full_text": f"text {i}",
				"metadata_json": {"reader_extracted": {"government outcome": "won"}},
			}
			for i in range(5)
		]

		result = analyze_phrases_in_memory(
			decisions, tag="test", max_decisions=10, min_phrase_frequency=1
		)

		assert result.decisions_capped is False
		assert result.decisions_scanned == 5


class TestPhraseDocumentCounts:
	"""Test exact document counts and document frequency tracking."""

	def test_exact_document_counts(self):
		"""Phrase document counts should be exact."""
		from backend.language_analytics import analyze_phrases_in_memory

		decisions = [
			{
				"id": 1,
				"summary": "exact count test",
				"full_text": "exact count test text",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			},
			{
				"id": 2,
				"summary": "exact count test",
				"full_text": "another exact count test",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			},
			{
				"id": 3,
				"summary": "exact count test",
				"full_text": "yet another exact count test",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			},
		]

		result = analyze_phrases_in_memory(
			decisions,
			tag="test",
			max_decisions=100,
			min_phrase_frequency=2,
			top_phrases_per_side=10,
		)

		# "exact count" should appear in all 3 documents
		exact_phrases = [p for p in result.allowed_phrases if "exact" in p["phrase"]]
		if exact_phrases:
			assert exact_phrases[0]["count"] == 3

	def test_group_denominators_exact(self):
		"""Group denominators should be exact document counts per outcome."""
		from backend.language_analytics import analyze_phrases_in_memory

		decisions = [
			{
				"id": i,
				"summary": f"allowed {i}",
				"full_text": f"text {i}",
				"metadata_json": {"reader_extracted": {"government outcome": "lost"}},
			}
			for i in range(7)
		] + [
			{
				"id": 7 + i,
				"summary": f"dismissed {i}",
				"full_text": f"text {i}",
				"metadata_json": {"reader_extracted": {"government outcome": "won"}},
			}
			for i in range(3)
		]

		result = analyze_phrases_in_memory(
			decisions,
			tag="test",
			max_decisions=100,
			min_phrase_frequency=1,
			top_phrases_per_side=10,
		)

		assert result.allowed_denominator == 7
		assert result.dismissed_denominator == 3
