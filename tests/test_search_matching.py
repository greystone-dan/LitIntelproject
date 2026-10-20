"""Offline identity fixtures and parameterized PostgreSQL query contracts."""

from datetime import date
from html.parser import HTMLParser
from types import SimpleNamespace
import json
import re
import shutil
import subprocess

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend import analytics_service, routes, search_service
from backend.models import CaseSearchRequest
from backend.search_matching import citation_query, identity_sql, identity_tier, match_details, matched_on
from backend.query_syntax import parse_query


def case(title="Baker v. Canada", **overrides):
	values = dict(id=1, title=title, citation="[1999] 2 SCR 817", secondary_citation=None,
		court="SCC", jurisdiction="Canada", date=date(1999, 7, 9), summary=None,
		full_text=None, issues=None, metadata_json={}, source_url=None, source_name=None)
	values.update(overrides)
	return SimpleNamespace(**values)


@pytest.mark.parametrize("separator", ["v", "v.", "vs", "vs.", "versus", "VERSUS"])
def test_party_names_are_case_insensitive_whole_contiguous_tokens(separator):
	assert identity_tier(case(f"  bAkEr   {separator}  Canada"), " BAKER ") == 1
	assert identity_tier(case(f"Bakery {separator} Canada"), "Baker") == 0
	assert identity_tier(case(f"New   Brunswick {separator} Canada"), "new BRUNSWICK") == 1
	assert identity_tier(case(f"New Other Brunswick {separator} Canada"), "New Brunswick") == 0
	assert identity_tier(case(f"New {separator} Brunswick"), "New Brunswick") == 0
	assert identity_tier(case("A judgment about Baker"), "Baker") == 0


def test_reader_party_metadata_and_body_mentions_are_distinct():
	assert identity_tier(case("Untitled", metadata_json={"reader_extracted": {
		"style of cause": "BAKER versus Canada"}}), "Baker") == 1
	assert identity_tier(case("Untitled", metadata_json={"reader_extracted": {
		"between": "New Brunswick Applicants and Canada Respondent"}}), "New Brunswick") == 1
	assert identity_tier(case("Untitled", metadata_json={"reader_extracted": {
		"between": "New Applicant and Brunswick Respondent"}}), "New Brunswick") == 0
	body = case("Other v Canada", full_text="Baker; procedural fairness; 2019 SCC 65")
	assert identity_tier(body, "Baker") == 0
	assert identity_tier(body, "procedural fairness") == 0
	assert identity_tier(body, "2019 SCC 65") == 0
	assert matched_on(body, "Baker", "lexical") == "Full text"


@pytest.mark.parametrize("malformed", [None, [], ["party"], "Baker", 1, True])
@pytest.mark.parametrize("field", ["metadata_json", "reader_extracted"])
def test_malformed_party_metadata_is_ignored(malformed, field):
	metadata = malformed if field == "metadata_json" else {"reader_extracted": malformed}
	assert match_details(case(metadata_json=metadata), "Baker", "lexical") == ("Party name", 3)
	assert match_details(case("Notes on Baker", metadata_json=metadata), "Baker", "lexical") == ("Title", 2)
	assert match_details(case("Other v Canada", metadata_json=metadata,
		full_text="Baker"), "Baker", "lexical") == ("Full text", 1)


@pytest.mark.parametrize("query", ["2019 SCC 65", "[2019] scc 65", " 2019   ScC   65 "])
def test_neutral_citation_normalization_and_token_boundaries(query):
	assert citation_query(query) == "2019 scc 65"
	assert identity_tier(case(citation="2019 SCC 65, [2019] 4 SCR 653"), query) == 2
	for citation in ["12019 SCC 65", "2019 SCC 650", "2019 SCC 165", "2018 SCC 65"]:
		assert identity_tier(case(citation=citation), query) == 0
	assert identity_tier(case(citation=None, secondary_citation="2019 SCC 65"), query) == 2


@pytest.mark.parametrize("query", ["[1999] 2 SCR 817", "1999 2 scr 817", "[1999]   2   ScR   817", "[1999] 2 S.C.R. 817"])
def test_reported_citations_can_share_primary_citation_field(query):
	hit = case(citation="1999 SCC 1; [1999] 2 SCR 817")
	assert identity_tier(hit, query) == 2
	assert matched_on(hit, query, "lexical") == "Citation"
	assert identity_tier(case(citation="[1999] 2 SCR 8170"), query) == 0
	assert identity_tier(case(citation="[1999] 2 S.C.R. 817"), query) == 2
	assert citation_query("1999") == citation_query("procedural fairness") == ""
	assert citation_query("1999 2 S.C.C. 817") == ""


@pytest.mark.parametrize(("value", "query", "mode", "label"), [
	(case(), "Baker", "lexical", "Party name"),
	(case("Notes on Baker"), "Baker", "lexical", "Title"),
	(case("Bakery v Canada"), "Baker", "lexical", "Title"),
	(case("Other v Canada"), "unrelated", "semantic", "Semantic"),
	(case("Other v Canada", metadata_json={"docket": "IMM-123"}), "IMM-123", "metadata", "Metadata"),
])
def test_labels_do_not_invent_identity_matches(value, query, mode, label):
	assert matched_on(value, query, mode) == label


class SearchDB:
	def __init__(self, rows):
		self.rows = rows

	def execute(self, statement):
		self.statement = statement
		return self.rows


@pytest.fixture(autouse=True)
def _enable_hosted_search_mode(monkeypatch):
	"""Keep retrieval-mode characterization tests explicit about opt-in."""
	monkeypatch.setenv("ENHANCED_AI_MODE", "hosted")


def test_case_search_ranks_identity_before_score_and_then_paginates():
	# Party > title > body > fallback, even with opposing legacy scores.
	rows = [(case("Bakery v Canada", id=3, citation="2020 SCC 3"), 1.0),
		(case(id=2, citation="2020 SCC 2"), .1),
		(case("Other v Canada", id=4, citation="2020 SCC 4", full_text="Baker"), .9),
		(case("Notes on Baker", id=7, citation="2020 SCC 7"), .01),
		(case("Unrelated", id=8, citation="2020 SCC 8"), 2.0)]
	db = SearchDB(rows)
	first = search_service.execute_search_cases(CaseSearchRequest(
		query="Baker", search_mode="lexical", page_size=1), db)
	second = search_service.execute_search_cases(CaseSearchRequest(
		query="Baker", search_mode="lexical", page_size=1, page=2), db)
	assert [(hit.id, hit.matched_on) for hit in first] == [(2, "Party name")]
	assert second[0].id == 3
	all_hits = search_service.execute_search_cases(CaseSearchRequest(
		query="Baker", search_mode="lexical"), db)
	assert [hit.id for hit in all_hits] == [2, 3, 7, 4, 8]
	citation_rows = [(case("Other v Canada", id=5, citation=None, full_text="2019 SCC 65"), 1),
		(case("Vavilov v Canada", id=6, citation="2019 SCC 65"), .01),
		(case("2019 SCC 65 v Canada", id=9, citation=None), .9),
		(case("Notes on 2019 SCC 65", id=10, citation=None), .001)]
	result = search_service.execute_search_cases(CaseSearchRequest(
		query="[2019] scc 65", search_mode="lexical"), SearchDB(citation_rows))
	assert [hit.id for hit in result] == [6, 9, 10, 5]
	assert result[0].matched_on == "Citation"
	# Citation shape alone enables hierarchy even if no candidate has identity.
	result = search_service.execute_search_cases(CaseSearchRequest(
		query="2019 SCC 65", search_mode="lexical"), SearchDB([citation_rows[0], citation_rows[3]]))
	assert [hit.id for hit in result] == [10, 5]


def test_topic_phrase_keeps_existing_python_score_order():
	db = SearchDB([(case("Other v Canada", id=1, full_text="procedural fairness"), .2),
		(case("Procedural fairness overview", id=2), .01),
		(case("Another v Canada", id=3, full_text="procedural fairness"), .6)])
	hits = search_service.execute_search_cases(CaseSearchRequest(
		query="procedural fairness", search_mode="lexical"), db)
	assert [hit.id for hit in hits] == [3, 1, 2]
	assert [hit.matched_on for hit in hits] == ["Full text", "Full text", "Title"]


@pytest.mark.parametrize("mode", ["semantic", "hybrid", "metadata"])
def test_identity_precedes_each_case_search_mode_without_live_embeddings(mode, monkeypatch):
	monkeypatch.setenv("QUERY_EMBEDDING_PROVIDER", "openai")
	party = case(id=1, citation="2020 SCC 1")
	other = case("Bakery v Canada", id=2, citation="2020 SCC 2")
	rows = [(other, .01, 1), (party, .9, .01)] if mode != "metadata" else [(other, 1), (party, .01)]
	hits = search_service.execute_search_cases(
		CaseSearchRequest(query="Baker", search_mode=mode), SearchDB(rows),
		embed_fn=lambda _: [0.0] * 1536)
	assert [hit.id for hit in hits] == [1, 2]
	assert hits[0].matched_on == "Party name"


class AnalyticsDB:
	"""Records both statements of a search: the id page (filters, ORDER BY, LIMIT) and the card fields for those ids."""

	def __init__(self):
		self.sql, self.compiled_sql, self.params, self.bindparams = "", "", {}, set()

	def execute(self, statement, params):
		self.page_stats = "FROM cases" not in str(statement)
		self.id_page = "LIMIT :limit" in str(statement)
		if not self.page_stats:
			self.sql += str(statement)
			self.params.update(params)
			self.bindparams |= set(statement._bindparams)
			self.compiled_sql += str(statement.compile())
		return self

	def mappings(self):
		return self

	def all(self):
		if self.page_stats:
			return []
		if self.id_page:
			return [dict(id=7)]
		return [dict(id=7, title="Baker v Canada", citation="[1999] 2 SCR 817", court="SCC",
			date="1999-07-09", judge=None, minister=None, decision_outcome=None,
			government_outcome=None, matching_citations=0, citation_mentions=0,
			unique_cited_authorities=0, resolved_target_cases=0, cited_by_cases=0, matched_on="Party name")]


def test_active_route_parameterizes_matches_and_ranks_before_sql_pagination():
	db = AnalyticsDB()
	result = routes.search_analytics_cases(query="  BAKER  ", search_full_text=True,
		court="FC", cites="2019 SCC 65", government_outcome="lost", judge="Smith",
		year="2020", limit=1, offset=2, db=db)
	citation, party, _ = identity_sql("Baker")
	# The regex matchers are no longer in WHERE (title/citation ILIKE only, index-friendly): label + ORDER BY.
	assert db.sql.count(citation) == 2
	assert db.sql.count(party) == 2
	assert db.sql.index("ORDER BY") < db.sql.index("LIMIT :limit OFFSET :offset")
	assert "CASE WHEN " + citation + " THEN 2 WHEN " + party + " THEN 1" in db.sql
	assert "REGEXP_SPLIT_TO_TABLE" in db.sql
	assert "c.secondary_citation" in db.sql
	assert "UPPER(c.court) IN" in db.sql
	assert "government outcome" in db.sql and "EXISTS (SELECT 1 FROM citations" in db.sql
	assert db.params["match_tokens"] == "baker"
	assert db.params["match_citation"] == ""
	assert db.params["query"] == "%BAKER%"
	assert (db.params["limit"], db.params["offset"]) == (1, 2)
	assert db.bindparams == set(db.params)
	assert "alnum" not in db.bindparams
	assert db.params["match_normalization"] == "[^[:alnum:]]+"
	assert ":match_normalization" in db.compiled_sql
	assert result["results"][0]["matched_on"] == "Party name"


def test_active_http_api_exposes_label_and_preserves_paging():
	app = FastAPI()
	app.include_router(routes.router)
	db = AnalyticsDB()
	app.dependency_overrides[routes.get_db] = lambda: db
	with TestClient(app) as client:
		response = client.get("/analytics/search/cases", params={
			"query": "BAKER", "limit": 1, "offset": 2, "sort_by": "relevance"})
	assert response.status_code == 200
	assert response.json()["results"][0]["matched_on"] == "Party name"
	assert (response.json()["limit"], response.json()["offset"]) == (1, 2)
	assert db.params["match_tokens"] == "baker"


@pytest.mark.parametrize("year_range", ["2020..2024", "2020-2024"])
def test_operator_search_builds_parameterized_boolean_filters_and_echo(year_range):
	query = (
		f'Vavilov AND court:SCC AND year:{year_range} AND '
		'judge:"Justice Zinn" AND cites:"2019 SCC 65" AND outcome:allowed'
	)
	db = AnalyticsDB()
	result = analytics_service.fetch_analytics_search_cases(db, query=query)

	assert query not in db.sql
	assert "c.court ILIKE" in db.sql
	assert "reader_extracted'->>'judge' ILIKE" in db.sql
	assert "SUBSTRING(COALESCE" in db.sql and "BETWEEN" in db.sql
	assert "EXISTS (SELECT 1 FROM citations cited" in db.sql
	assert "decision outcome" in db.sql and "LOWER(:operator_query_" in db.sql
	assert " AND " in db.sql
	assert ":query_match_label AS matched_on" in db.sql
	assert db.params["query_match_label"] == "Query operators"
	assert "%Vavilov%" in db.params.values()
	assert "%SCC%" in db.params.values()
	assert "%Justice Zinn%" in db.params.values()
	assert "%2019 SCC 65%" in db.params.values()
	assert 2020 in db.params.values() and 2024 in db.params.values()
	assert "allowed" in db.params.values()
	assert "court: SCC" in result["query_echo"]


def test_operator_sql_keeps_hostile_values_in_bind_parameters():
	query = 'cites:"%\' OR TRUE --"'
	db = AnalyticsDB()

	analytics_service.fetch_analytics_search_cases(db, query=query)

	assert query not in db.sql
	assert "%%' OR TRUE --%" in db.params.values()
	assert "OR TRUE" not in db.sql


@pytest.mark.parametrize(
	("query", "uses_operators"),
	[
		("procedural fairness", False),
		("O'Connor", False),
		("custom:value", False),
		('"procedural fairness"', True),
		("fairness AND delay", True),
		("-delay", True),
		("court:SCC", True),
		("year:invalid", True),
	],
)
def test_plain_query_detection_preserves_legacy_multiword_search(query, uses_operators):
	assert analytics_service._query_uses_operators(parse_query(query)) is uses_operators


@pytest.mark.parametrize("query", ["[1999] 2 SCR 817", "[1999] 2 S.C.R. 817", "2019 SCC 65", "Baker%' OR TRUE --"])
def test_sql_values_are_bound_not_interpolated(query):
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query=query)
	assert query not in db.sql
	assert db.params["match_citation"] == citation_query(query)
	assert ":match_tokens" in db.sql and ":match_citation" in db.sql
	# Legacy order supplies query_like even when body matching is disabled.
	assert db.bindparams == set(db.params) - {"query_like"}
	assert "alnum" not in db.bindparams
	assert db.params["match_normalization"] == "[^[:alnum:]]+"
	assert ":match_normalization" in db.compiled_sql


@pytest.mark.parametrize("sort_by", ["newest", "oldest", "minister"])
def test_explicit_sorts_ignore_identity_but_keep_labels(sort_by):
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="Baker", sort_by=sort_by)
	order = db.sql.split("ORDER BY", 1)[1].split("LIMIT :limit", 1)[0]
	assert ":match_tokens" not in order and "THEN 2" not in order
	assert "AS matched_on" in db.sql


def test_topic_sql_legacy_tier_is_unchanged_and_full_text_is_opt_in():
	order, params = analytics_service._analytics_case_order_sql("procedural fairness", "relevance")
	legacy = order.split("ELSE 0 END DESC, ", 1)[1]
	assert "LIKE LOWER(:query_exact_like) THEN 1000" in legacy
	assert "LIKE LOWER(:query_exact_like) THEN 900" in legacy
	assert legacy.index("THEN 1000") < legacy.index("THEN 900") < legacy.index("THEN 850")
	assert "c.full_text" not in order
	assert params["match_citation"] == ""
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="procedural fairness")
	assert "c.full_text" not in db.sql
	full_order, _ = analytics_service._analytics_case_order_sql(
		"procedural fairness", "relevance", search_full_text=True)
	assert full_order.index("THEN 1000") < full_order.index("THEN 700")


class ScriptParser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.scripts = []
		self.chunks = None

	def handle_starttag(self, tag, attrs):
		if tag == "script":
			self.chunks = []

	def handle_data(self, data):
		if self.chunks is not None:
			self.chunks.append(data)

	def handle_endtag(self, tag):
		if tag == "script" and self.chunks is not None:
			self.scripts.append("".join(self.chunks))
			self.chunks = None


def test_script_parser_handles_uppercase_and_whitespace_closing_tags():
	parser = ScriptParser()
	parser.feed("outside<SCRIPT>const value = '<tag>';</SCRIPT\t\n >outside")
	parser.close()
	assert parser.scripts == ["const value = '<tag>';"]


def test_active_result_card_executes_and_escapes_matched_on():
	node = shutil.which("node")
	if not node:
		pytest.skip("Node required for active renderer execution")
	html = routes._data_explorer_page_html()
	card = re.search(r"function resultCard\(item\).*", html).group()
	esc = re.search(r"const esc=.*", html).group()
	num = re.search(r"const num=.*", html).group()
	script = esc + "\n" + num + "\n" + card + "\n"
	script += """
const assert=require('node:assert/strict');
const rendered=resultCard({case_id:7,title:'Baker v Canada',matched_on:'Party name'});
assert.ok(rendered.includes('Matched on: Party name'));
assert.ok(rendered.includes('data-case-id="7"'));
assert.ok(!resultCard({case_id:7,title:'old response'}).includes('Matched on:'));
assert.ok(!resultCard({case_id:7,matched_on:'<img src=x>'}).includes('<img'));
"""
	result = subprocess.run([node, "-"], input=script, text=True, capture_output=True, timeout=15)
	assert result.returncode == 0, result.stderr
	# Compile the complete edited Case Search script. Other feature scripts have
	# separate owners; baseline compilation defects there are not this slice.
	parser = ScriptParser()
	parser.feed(html)
	parser.close()
	source = next(source for source in parser.scripts if "function resultCard(item)" in source)
	result = subprocess.run([node, "-"], input="new Function(" + json.dumps(source) + ");",
		text=True, capture_output=True, timeout=15)
	assert result.returncode == 0, result.stderr


@pytest.mark.parametrize("query", ["procedural fairness", "Baker", "", "the of and", "O'Connor"])
def test_short_or_stopword_queries_keep_legacy_phrase_search(query):
	from backend.search_matching import sentence_words
	assert sentence_words(query) == []
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query=query)
	assert "sentence_word_" not in db.sql


def test_sentence_words_drop_filler_and_keep_longest_distinct_words():
	from backend.search_matching import sentence_words
	words = sentence_words("The officer ignored my medical evidence and ignored the doctor")
	assert words == ["evidence", "officer", "ignored", "medical", "doctor"]
	assert len(sentence_words("one two three " * 3 + "alpha bravo charlie delta echo foxtrot golf")) <= 6


@pytest.mark.parametrize("full_text", [False, True])
def test_sentence_query_accepts_most_words_and_ranks_by_word_count(full_text):
	query = "officer ignored my medical evidence"
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query=query, search_full_text=full_text)
	where, order = db.sql.split("WHERE", 1)[1].split("ORDER BY", 1)
	assert "c.title ILIKE :query" in where  # exact phrase still accepted
	assert ":sentence_word_0" in where and ">= 3" in where  # 4 words -> at least 3
	assert (":sentence_word_0" in order) and order.index("sentence_word_0") < order.index("c.date DESC")
	assert ("c.full_text" in where) is full_text
	assert query not in db.sql
	assert {db.params[f"sentence_word_{i}"] for i in range(4)} == {"%medical%", "%evidence%", "%ignored%", "%officer%"}


def test_sentence_query_with_operators_is_left_to_the_operator_compiler():
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="officer AND ignored medical evidence")
	assert "sentence_word_" not in db.sql


def test_case_type_filter_reads_stored_labels_with_bound_params():
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="Baker", case_type="refugee_claim")
	assert "case_type_labels" in db.sql and "ctl.second_type IN (:case_type_0)" in db.sql
	assert db.params["case_type_0"] == "refugee_claim"
	assert db.params["case_type_version"]
	assert "refugee_claim" not in db.sql


def test_unknown_case_type_matches_nothing_and_is_not_interpolated():
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="Baker", case_type="x'; DROP TABLE cases;--")
	assert "DROP TABLE" not in db.sql
	assert "case_type_0" not in db.params


def test_case_type_facet_uses_stored_labels_and_labels_known_keys():
	class FacetDB:
		def __init__(self):
			self.statements = []

		def execute(self, statement, params):
			self.statements.append(str(statement))
			self.last = str(statement)
			return self

		def mappings(self):
			return self

		def all(self):
			if "case_type_labels" in self.last:
				return [dict(label="refugee_claim", n=5), dict(label="bogus", n=1)]
			return []

	db = FacetDB()
	rows = analytics_service._case_type_facet(db, "1=1", {}, None)
	assert [r["value"] for r in rows] == ["refugee_claim"] and rows[0]["count"] == 5
	assert rows[0]["label"]


@pytest.mark.parametrize("params", [
	{"year": "abcd"}, {"sort_by": "bogus"}, {"limit": -1}, {"offset": -5},
])
def test_search_rejects_values_it_used_to_ignore(params):
	app = FastAPI()
	app.include_router(routes.router)
	app.dependency_overrides[routes.get_db] = lambda: AnalyticsDB()
	with TestClient(app) as client:
		assert client.get("/analytics/search/cases", params=params).status_code == 422
		ok = client.get("/analytics/search/cases", params={"year": "2019", "sort_by": "newest", "limit": 5})
	assert ok.status_code == 200


def test_year_hint_accent_and_loose_caption_matching():
	from backend.search_matching import fold_accents, loose_title_pattern, split_year_hint

	assert split_year_hint("Baker v Canada 1999") == ("Baker v Canada", "1999")
	assert split_year_hint("Baker 1999") == ("Baker 1999", "")
	assert split_year_hint("standard of review 2019") == ("standard of review 2019", "")
	assert split_year_hint("2019 SCC 65") == ("2019 SCC 65", "")
	assert split_year_hint("Smith v Canada 2012 FC") == ("Smith v Canada 2012 FC", "")
	assert split_year_hint("1999") == ("1999", "")
	assert loose_title_pattern("Baker v Canada") == "%baker%v%canada%"
	assert loose_title_pattern("Baker") == ""
	assert loose_title_pattern("a b") == "" and loose_title_pattern("ab v cd") == ""
	assert fold_accents("Doré Québec") == "dore quebec"


def test_search_picks_ids_first_and_year_hint_filters_by_date():
	db = AnalyticsDB()
	result = analytics_service.fetch_analytics_search_cases(db, query="Baker v Canada 1999", include_facets=False)
	assert db.params["year_start"] == "1999-01-01" and db.params["query"] == "%Baker v Canada%"
	assert db.params["query_loose"] == "%baker%v%canada%" and db.params["query_folded"] == "%baker v canada%"
	assert db.sql.index("LIMIT :limit") < db.sql.index("WHERE c.id IN")
	assert result["results"][0]["case_id"] == 7


def test_short_query_skips_the_caption_regexes_in_the_sort():
	order, params = analytics_service._analytics_case_order_sql("a", "relevance")
	assert "match_tokens" not in order and "match_tokens" not in params
	order, _ = analytics_service._analytics_case_order_sql("ba", "relevance")
	assert "match_tokens" not in order
	order, _ = analytics_service._analytics_case_order_sql("bak", "relevance")
	assert ":match_tokens" in order


def test_relevance_tie_break_is_stored_citation_count_then_date():
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="Kanthasamy", include_facets=False)
	order = db.sql.split("ORDER BY", 1)[1].split("LIMIT :limit", 1)[0]
	assert "COALESCE(cm.in_degree, 0) DESC, c.date DESC NULLS LAST" in order
	assert "LEFT JOIN citation_metrics cm ON cm.case_id = c.id" in db.sql
	assert "cited_by_ids" not in db.params  # no id arrays are sent along with a name search


def test_most_cited_sort_uses_the_cached_counts_with_an_inner_join(monkeypatch):
	monkeypatch.setattr(analytics_service, "_cited_by_arrays", lambda db: ([5], [9]))
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, sort_by="most_cited", include_facets=False)
	assert "\n\t\tJOIN (SELECT * FROM unnest" in db.sql and "LEFT JOIN" not in db.sql
	assert db.params["cited_by_ids"] == [5] and db.params["cited_by_counts"] == [9]


def test_cited_by_counts_are_built_once_and_reused():
	class CountingDB:
		runs = 0

		def execute(self, statement):
			CountingDB.runs += 1
			return type("R", (), {"all": lambda self: [(1, 2), (3, 4)]})()

	analytics_service._CITED_BY_CACHE.update(at=0.0, ids=[], counts=[])
	assert analytics_service._cited_by_arrays(CountingDB()) == ([1, 3], [2, 4])
	assert analytics_service._cited_by_arrays(CountingDB()) == ([1, 3], [2, 4]) and CountingDB.runs == 1
	analytics_service._CITED_BY_CACHE.update(at=0.0, ids=[], counts=[])


def test_slow_results_have_their_own_lock_and_expired_copies_refresh_in_the_background(monkeypatch):
	import threading

	analytics_service.clear_analytics_cache()
	analytics_service.set_analytics_cache_enabled(True)
	builds = []
	assert analytics_service.cached_slow_result("t1", lambda db: builds.append(db) or "v1", "db") == "v1"
	assert analytics_service.cached_slow_result("t1", lambda db: "other", "db") == "v1" and builds == ["db"]
	assert analytics_service._SLOW_LOCKS["t1"] is not analytics_service._SLOW_LOCKS.get("t2")
	# Expired: the old copy is returned at once and the next one is built off-thread with its own session.
	analytics_service._SLOW_RESULTS["t1"] = (analytics_service.time.monotonic() - 99999, "old")
	done = threading.Event()
	import backend.database as database

	monkeypatch.setattr(database, "SessionLocal", lambda: type("S", (), {"__enter__": lambda s: "bg", "__exit__": lambda s, *a: False})())

	def build(session):
		done.set()
		return f"new-{session}"

	assert analytics_service.cached_slow_result("t1", build, "request-db") == "old"
	assert done.wait(2)
	for _ in range(50):
		if analytics_service._SLOW_RESULTS["t1"][1] == "new-bg":
			break
		analytics_service.time.sleep(0.02)
	assert analytics_service._SLOW_RESULTS["t1"][1] == "new-bg"
	analytics_service.clear_analytics_cache()


def test_year_hint_and_cap_notices():
	db = AnalyticsDB()
	result = analytics_service.fetch_analytics_search_cases(db, query="Baker v Canada 1999", include_facets=False)
	assert "from 1999" in result["notice"]
	assert analytics_service.fetch_analytics_search_cases(AnalyticsDB(), query="Baker", include_facets=False)["notice"] is None


def test_accent_list_in_the_migration_matches_the_search_code():
	import importlib.util
	from pathlib import Path

	from backend.search_matching import ACCENTED, UNACCENTED

	path = Path(__file__).resolve().parents[1] / "alembic" / "versions" / "0050_search_speed_indexes.py"
	spec = importlib.util.spec_from_file_location("migration_0050", path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	assert f"'{ACCENTED}', '{UNACCENTED}'" in module.FOLDED and len(ACCENTED) == len(UNACCENTED)
