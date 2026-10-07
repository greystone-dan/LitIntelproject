"""Paragraph keyword search: query building, safe fallback, and wiring into the case search box."""

import pytest

from backend import analytics_service, paragraph_search
from backend.paragraph_search import query_slots, search_paragraph_cases, tier_queries
from backend.search_thesaurus import THESAURUS, synonyms_for
from tests.test_search_matching import AnalyticsDB


def test_slots_pair_each_content_word_with_synonyms_and_quote_phrases():
	slots = query_slots("officer ignored my medical evidence")
	assert len(slots) == 4
	joined = " ".join(slots)
	assert "psychological" in joined and "(failed <-> to <-> consider)" in joined
	assert "(visa <-> officer)" in joined
	assert all(slot.startswith("(") and slot.endswith(")") for slot in slots)


def test_slot_text_is_sanitized_to_letters_and_digits():
	for slot in query_slots("claimant said 'x'; DROP TABLE cases -- (medical) & evidence | ignored"):
		assert not set(slot) & set("';\"\\$%")


def test_two_word_queries_are_not_handled_here():
	assert query_slots("procedural fairness") == []


def test_tiers_go_from_all_slots_to_all_but_two_and_stop_at_two_slots():
	slots = ["(a)", "(b)", "(c)", "(d)"]
	tiers = tier_queries(slots)
	assert tiers[0] == "((a) & (b) & (c) & (d))"
	assert tiers[1].count("|") == 3 and tiers[1].count("&") == 8
	assert len(tiers) == 3 and "((a) & (b)) | ((a) & (c))" in tiers[2]
	assert len(tier_queries(["(a)", "(b)", "(c)"])) == 2  # never down to a single slot
	assert tier_queries(["(a)"]) == []


def test_thesaurus_is_clean_data():
	assert len(THESAURUS) >= 150
	for word, values in THESAURUS.items():
		assert word == word.lower() and word.strip() == word
		assert values and all(isinstance(value, str) and value for value in values)
	assert synonyms_for("Doctors") == THESAURUS["doctor"] and synonyms_for("zebra") == ()


class FakeResult:
	def __init__(self, rows):
		self.rows = rows

	def scalar(self):
		return True

	def mappings(self):
		return self

	def all(self):
		return self.rows


class FakeDB:
	def __init__(self, tiers):
		self.tiers, self.calls, self.rolled_back = tiers, [], False

	def execute(self, statement, params=None):
		if params is None:
			return FakeResult([])
		self.calls.append(params["match_query"])
		return FakeResult(self.tiers.pop(0) if self.tiers else [])

	def rollback(self):
		self.rolled_back = True


def reset_cache(ready=True):
	paragraph_search._TABLE_CACHE.update(checked=0.0, ready=False)


def row(case_id, score, paragraphs, chunk):
	return {"case_id": case_id, "best_score": score, "paragraphs": paragraphs, "best_chunk_id": chunk}


def test_search_loosens_until_enough_paragraphs_match():
	reset_cache()
	db = FakeDB([[row(1, 1.0, 2, 10)], [row(1, 1.0, 2, 10), row(2, 0.5, 30, 20)]])
	hits = search_paragraph_cases(db, "officer ignored my medical evidence")
	assert [hit["case_id"] for hit in hits] == [1, 2]
	assert len(db.calls) == 2  # stopped after the second tier had 32 paragraphs


def test_search_returns_none_when_nothing_matches_or_query_too_short():
	reset_cache()
	assert search_paragraph_cases(FakeDB([]), "officer ignored my medical evidence") is None
	assert search_paragraph_cases(FakeDB([]), "procedural fairness") is None


def test_search_can_be_switched_off(monkeypatch):
	reset_cache()
	monkeypatch.setenv("ILIT_PARAGRAPH_SEARCH", "0")
	db = FakeDB([[row(1, 1.0, 50, 10)]])
	assert search_paragraph_cases(db, "officer ignored my medical evidence") is None
	assert db.calls == []


def test_missing_index_falls_back_without_error():
	reset_cache()

	class Broken:
		rolled_back = False

		def execute(self, *args, **kwargs):
			raise RuntimeError("relation paragraph_search does not exist")

		def rollback(self):
			self.rolled_back = True

	db = Broken()
	assert search_paragraph_cases(db, "officer ignored my medical evidence") is None
	assert db.rolled_back


def test_case_search_uses_paragraph_hits_for_filter_order_and_label(monkeypatch):
	hits = [
		{"case_id": 7, "score": 2.0, "paragraphs": 3, "best_chunk_id": 70},
		{"case_id": 3, "score": 1.0, "paragraphs": 1, "best_chunk_id": 30},
	]
	monkeypatch.setattr(analytics_service, "search_paragraph_cases", lambda db, query: hits)
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="officer ignored my medical evidence")
	where, order = db.sql.split("WHERE", 1)[1].split("ORDER BY", 1)
	assert db.params["para_ids"] == [7, 3]
	assert "c.id = ANY(CAST(:para_ids AS integer[]))" in where
	assert "sentence_word_" not in db.sql  # the slower word-count scan is skipped
	assert "THEN 'Paragraph match'" in db.sql
	assert order.index("array_position(CAST(:para_ids") < order.index("c.date DESC")
	assert "officer ignored" not in db.sql


def test_case_search_keeps_word_count_fallback_without_the_index(monkeypatch):
	monkeypatch.setattr(analytics_service, "search_paragraph_cases", lambda db, query: None)
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="officer ignored my medical evidence")
	assert "para_ids" not in db.params and ":sentence_word_0" in db.sql


def test_short_and_operator_queries_never_touch_the_paragraph_index(monkeypatch):
	def boom(db):
		raise AssertionError("paragraph index should not be consulted")

	monkeypatch.setattr(paragraph_search, "_index_ready", boom)
	for query in ["Baker", "procedural fairness", '"officer ignored my medical evidence"', "fairness AND delay"]:
		analytics_service.fetch_analytics_search_cases(AnalyticsDB(), query=query)
