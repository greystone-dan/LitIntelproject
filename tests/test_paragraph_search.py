"""Paragraph keyword search: query building, safe fallback, and wiring into the case search box."""

import pytest

from backend import analytics_service, paragraph_search
from backend.paragraph_search import query_slots, search_paragraph_cases, tier_queries
from backend.search_thesaurus import THESAURUS, synonyms_for


class AnalyticsDB:
	"""Records the case-search SQL and parameters; returns one canned row."""

	def execute(self, statement, params):
		self.page_stats = "FROM cases" not in str(statement)
		if not self.page_stats:
			self.sql, self.params = str(statement), params
			self.bindparams = set(statement._bindparams)
		return self

	def mappings(self):
		return self

	def all(self):
		if self.page_stats:
			return []
		return [dict(id=7, title="Baker v Canada", citation="[1999] 2 SCR 817", court="SCC",
			date="1999-07-09", judge=None, minister=None, decision_outcome=None,
			government_outcome=None, matching_citations=0, citation_mentions=0,
			unique_cited_authorities=0, resolved_target_cases=0, cited_by_cases=0, matched_on="Party name")]


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
	analytics_service.fetch_analytics_search_cases(db, query="officer ignored my medical evidence", search_full_text=True)
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


def test_full_text_box_with_paragraph_hits_skips_the_whole_text_scan(monkeypatch):
	hits = [{"case_id": 7, "score": 2.0, "paragraphs": 3, "best_chunk_id": 70}]
	monkeypatch.setattr(analytics_service, "search_paragraph_cases", lambda db, query: hits)
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="officer ignored my medical evidence", search_full_text=True)
	where = db.sql.split("WHERE TRUE", 1)[1].split("ORDER BY", 1)[0]
	assert "c.full_text ILIKE" not in where and "c.summary ILIKE" not in where
	assert "c.id = ANY(CAST(:para_ids AS integer[]))" in where


def test_full_text_box_without_paragraph_hits_keeps_the_scan_with_a_timeout(monkeypatch):
	monkeypatch.setattr(analytics_service, "search_paragraph_cases", lambda db, query: None)
	statements = []

	class TimedDB(AnalyticsDB):
		def execute(self, statement, params=None):
			statements.append(str(statement))
			return super().execute(statement, params)

	db = TimedDB()
	analytics_service.fetch_analytics_search_cases(db, query="officer ignored my medical evidence", search_full_text=True)
	assert "c.full_text ILIKE" in db.sql
	assert any(sql.startswith("SET LOCAL statement_timeout") for sql in statements)


def test_scan_timeout_becomes_a_friendly_503(monkeypatch):
	from fastapi import HTTPException
	from sqlalchemy.exc import OperationalError

	monkeypatch.setattr(analytics_service, "search_paragraph_cases", lambda db, query: None)

	class SlowDB(AnalyticsDB):
		rolled_back = False

		def execute(self, statement, params=None):
			if params is not None and "FROM cases" in str(statement):
				raise OperationalError("SELECT", {}, Exception("canceling statement due to statement timeout"))
			return super().execute(statement, params)

		def rollback(self):
			self.rolled_back = True

	db = SlowDB()
	try:
		analytics_service.fetch_analytics_search_cases(db, query="officer ignored my medical evidence", search_full_text=True)
	except HTTPException as error:
		assert error.status_code == 503 and "too broad" in error.detail and db.rolled_back
	else:
		raise AssertionError("expected a 503")


SENTENCE = "the officer ignored medical evidence about the applicant's child and refused humanitarian and compassionate relief"


def test_a_sentence_with_lowercase_and_is_a_plain_sentence_not_an_all_words_operator_query(monkeypatch):
	hits = [{"case_id": 7, "score": 2.0, "paragraphs": 3, "best_chunk_id": 70}]
	monkeypatch.setattr(analytics_service, "search_paragraph_cases", lambda db, query: hits)
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query=SENTENCE, search_full_text=True)
	where = db.sql.split("WHERE TRUE", 1)[1].split("ORDER BY", 1)[0]
	assert "c.id = ANY(CAST(:para_ids AS integer[]))" in where
	assert "c.full_text ILIKE" not in where


def test_a_sentence_without_paragraph_hits_matches_most_words_not_all(monkeypatch):
	monkeypatch.setattr(analytics_service, "search_paragraph_cases", lambda db, query: None)
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query=SENTENCE, search_full_text=True)
	assert "sentence_word_0" in db.sql and ">=" in db.sql


def test_capital_operators_quotes_filters_and_minus_still_use_operator_search(monkeypatch):
	monkeypatch.setattr(analytics_service, "search_paragraph_cases", lambda db, query: None)
	for query in ["officer fairness AND delay procedural", '"officer ignored" medical evidence child',
			"court:FC officer ignored medical evidence", "officer ignored medical evidence -costs", "damages and liability"]:
		db = AnalyticsDB()
		analytics_service.fetch_analytics_search_cases(db, query=query)
		assert "sentence_word_0" not in db.sql, query


def test_paragraph_index_is_not_searched_when_the_full_text_box_is_off(monkeypatch):
	def boom(db, query):
		raise AssertionError("the paragraph index holds decision text; it needs the full-text box")

	monkeypatch.setattr(analytics_service, "search_paragraph_cases", boom)
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="best interests of the child")
	assert "para_ids" not in db.params and "c.full_text ILIKE" not in db.sql
