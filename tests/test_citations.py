from types import SimpleNamespace

import pytest
from fastapi import HTTPException

from backend import citations
from backend import routes


class FakeDatabase:
	def __init__(self, rows=(), scalar_value=None):
		self.rows = list(rows)
		self.scalar_values = list(scalar_value) if isinstance(scalar_value, list) else [scalar_value]

	def execute(self, statement):
		self.statement = statement
		return self.rows

	def scalar(self, statement):
		self.statement = statement
		if self.scalar_values:
			return self.scalar_values.pop(0)
		return None


class FakeCitationSession:
	def __init__(self, target_case_id=7):
		self.target_case_id = target_case_id
		self.added = []

	def scalar(self, statement):
		return SimpleNamespace(id=self.target_case_id)

	def add_all(self, rows):
		self.added.extend(rows)


class QueuedScalarsSession:
	def __init__(self, scalar_batches):
		self.scalar_batches = iter(scalar_batches)
		self.commits = 0

	def scalars(self, statement):
		return next(self.scalar_batches)

	def commit(self):
		self.commits += 1


def test_extract_citations_from_text_normalizes_and_resolves(monkeypatch):
	monkeypatch.setattr(citations, "resolve_neutral_to_case_id", lambda session, neutral: 42 if neutral == "2024 FC 100" else None)
	session = FakeCitationSession()
	text = "See 2024 FC 100, Smith v. Jones, 2023 FCA 5, and IRPA s. 72(1)."

	rows = citations.extract_citations_from_text(session, source_case_id=11, text=text)

	assert len(rows) == 3
	assert rows[0].target_case_id == 42
	assert rows[0].normalized_citation == "2024 FC 100"
	assert rows[1].target_case_id is None
	assert rows[1].normalized_citation == "Smith v. Jones, 2023 FCA 5"
	assert rows[2].normalized_citation == "IRPA s. 72(1)"
	assert len(session.added) == 3


def test_citation_endpoints_return_rows_and_metrics():
	case = SimpleNamespace(id=10)
	citation = SimpleNamespace(
		id=1,
		source_case_id=10,
		target_case_id=20,
		citation_text="2024 FC 100",
		normalized_citation="2024 FC 100",
		chunk_id=None,
		offset_start=4,
		offset_end=14,
		unresolved=False,
	)
	metrics = SimpleNamespace(case_id=10, in_degree=2, out_degree=3, pagerank=0.25)

	outgoing_db = FakeDatabase(rows=[(citation,)], scalar_value=[case])
	outgoing = routes.get_case_outgoing_citations(10, outgoing_db)

	assert outgoing[0].source_case_id == 10
	assert outgoing[0].target_case_id == 20
	assert outgoing[0].normalized_citation == "2024 FC 100"

	metrics_db = FakeDatabase(scalar_value=[case, metrics])
	result = routes.get_case_citation_metrics(10, metrics_db)

	assert result.case_id == 10
	assert result.in_degree == 2
	assert result.out_degree == 3
	assert result.pagerank == 0.25


def test_citation_map_endpoints_delegate_with_bounded_parameters(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case, case, case])
	calls = {}

	monkeypatch.setattr(routes, "_citation_map_summary", lambda db: {"database": db})
	monkeypatch.setattr(
		routes,
		"_top_authorities",
		lambda db, limit: calls.update(authorities=(db, limit)) or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_neighborhood",
		lambda db, focus, limit: calls.update(neighborhood=(db, focus.id, limit)) or {},
	)
	monkeypatch.setattr(
		routes,
		"_similar_cases_by_authority",
		lambda db, case_id, limit, min_shared: calls.update(
			similar=(db, case_id, limit, min_shared)
		) or [],
	)
	monkeypatch.setattr(
		routes,
		"_co_cited_authorities",
		lambda db, case_id, limit: calls.update(co_cited=(db, case_id, limit)) or [],
	)

	assert routes.get_citation_map_summary(database) == {"database": database}
	routes.get_citation_map_authorities(limit=999, db=database)
	routes.get_citation_map_neighborhood(10, limit=999, db=database)
	routes.get_citation_map_similar_cases(10, limit=999, min_shared=999, db=database)
	routes.get_citation_map_co_cited_authorities(10, limit=999, db=database)

	assert calls["authorities"] == (database, 200)
	assert calls["neighborhood"] == (database, 10, 500)
	assert calls["similar"] == (database, 10, 100, 50)
	assert calls["co_cited"] == (database, 10, 100)


def test_citation_map_case_search_and_authority_map_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case])
	calls = {}

	monkeypatch.setattr(
		routes,
		"_search_citation_cases",
		lambda db, query, limit: calls.update(search=(db, query, limit)) or [],
	)
	monkeypatch.setattr(
		routes,
		"_case_authority_map",
		lambda db, focus, limit: calls.update(authority_map=(db, focus.id, limit)) or {},
	)

	routes.search_citation_map_cases(q="Vavilov", limit=999, db=database)
	routes.get_case_authority_map(10, limit=999, db=database)

	assert calls["search"] == (database, "Vavilov", 30)
	assert calls["authority_map"] == (database, 10, 12)
	assert "Search and read the corpus" in routes.case_reader_page()
	assert "item.title" in routes.case_reader_page()
	assert "item.citation||item.title" not in routes.case_reader_page()


def test_citation_map_issue_and_evidence_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case, case, case, case])
	calls = {}
	context = {
		"citation_id": 1,
		"source_case_id": 10,
		"source_title": "Source",
		"source_citation": "2024 FC 10",
		"target_case_id": 20,
		"target_title": "Target",
		"target_citation": "2019 SCC 65",
		"chunk_id": 3,
		"chunk_index": 0,
		"citation_text": "Vavilov",
		"normalized_citation": "2019 SCC 65",
		"offset_start": 4,
		"offset_end": 12,
		"context_start": 0,
		"context_end": 18,
		"context": "See Vavilov here.",
	}

	monkeypatch.setattr(routes, "_citation_map_topics", lambda db, query, limit: calls.update(topics=(db, query, limit)) or [])
	monkeypatch.setattr(routes, "_citation_issue_map", lambda db, category, value, limit: calls.update(issue=(db, category, value, limit)) or {})
	monkeypatch.setattr(routes, "_case_legal_tags", lambda db, case_id, limit: calls.update(tags=(db, case_id, limit)) or [])
	monkeypatch.setattr(routes, "_common_citing_cases", lambda db, case_ids, limit: calls.update(common=(db, case_ids, limit)) or [])
	monkeypatch.setattr(routes, "_citation_contexts", lambda db, source, target, limit: calls.update(context=(db, source, target, limit)) or [context])

	routes.get_citation_map_topics(q="fairness", limit=999, db=database)
	routes.get_citation_issue_map(category="issue", value="procedural_fairness", limit=999, db=database)
	routes.get_citation_map_case_tags(10, limit=999, db=database)
	routes.get_common_citing_cases(case_ids="10,20,10", limit=999, db=database)
	response = routes.export_citation_contexts(10, 20, db=database)

	assert calls["topics"] == (database, "fairness", 250)
	assert calls["issue"] == (database, "issue", "procedural_fairness", 200)
	assert calls["tags"] == (database, 10, 250)
	assert calls["common"] == (database, [10, 20], 200)
	assert calls["context"] == (database, 10, 20, 200)
	assert response.media_type == "text/csv; charset=utf-8"
	assert response.headers["content-disposition"] == 'attachment; filename="citation-context-10-to-20.csv"'
	assert b"See Vavilov here." in response.body

	with pytest.raises(HTTPException) as unsupported:
		routes.get_citation_issue_map(category="outcome", value="allowed", db=database)
	assert unsupported.value.status_code == 422

	with pytest.raises(HTTPException) as too_few:
		routes.get_common_citing_cases(case_ids="10", db=database)
	assert too_few.value.status_code == 422


def test_citation_paths_and_edge_summary_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case, case, case, case])
	calls = {}
	summary = {
		"source_case": {
			"case_id": 10,
			"title": "Source",
			"citation": "2024 FC 10",
			"court": "FC",
			"date": "2024-01-01",
			"in_degree": 1,
			"out_degree": 2,
			"pagerank": None,
		},
		"target_case": {
			"case_id": 20,
			"title": "Target",
			"citation": "2019 SCC 65",
			"court": "SCC",
			"date": "2019-01-01",
			"in_degree": 5,
			"out_degree": 0,
			"pagerank": None,
		},
		"occurrence_count": 3,
		"distinct_chunks": 2,
		"first_chunk_index": 1,
		"last_chunk_index": 4,
		"top_normalized_citations": [{"normalized_citation": "2019 SCC 65", "occurrences": 3}],
		"sample_contexts": [],
	}

	monkeypatch.setattr(
		routes,
		"_citation_paths",
		lambda db, source_case_id, target_case_id, max_hops, limit, per_node_limit: calls.update(
			paths=(db, source_case_id, target_case_id, max_hops, limit, per_node_limit)
		) or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_edge_summary",
		lambda db, source_case_id, target_case_id, context_limit, variant_limit: calls.update(
			summary=(db, source_case_id, target_case_id, context_limit, variant_limit)
		) or summary,
	)

	routes.get_citation_paths(source_case_id=10, target_case_id=20, max_hops=999, limit=999, per_node_limit=1, db=database)
	routes.get_citation_edge_summary(source_case_id=10, target_case_id=20, context_limit=999, variant_limit=0, db=database)

	assert calls["paths"] == (database, 10, 20, 6, 25, 5)
	assert calls["summary"] == (database, 10, 20, 20, 1)


def test_advanced_citation_analytics_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case, case, case, case, case])
	calls = {}

	replacement = {
		"old_authority": {
			"case_id": 10,
			"title": "Old",
			"citation": "2002 SCC 1",
			"court": "SCC",
			"date": "2002-01-01",
			"in_degree": 1,
			"out_degree": 1,
			"pagerank": None,
		},
		"new_authority": {
			"case_id": 20,
			"title": "New",
			"citation": "2019 SCC 65",
			"court": "SCC",
			"date": "2019-01-01",
			"in_degree": 5,
			"out_degree": 1,
			"pagerank": None,
		},
		"replacement_score": 1.1,
		"status": "replacement_likely",
		"series": [],
	}

	monkeypatch.setattr(
		routes,
		"_citation_contextual_paths",
		lambda db, source_case_id, target_case_id, max_hops, limit, per_node_limit, hop_context_limit: calls.update(
			contextual_paths=(db, source_case_id, target_case_id, max_hops, limit, per_node_limit, hop_context_limit)
		) or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_authority_signals",
		lambda db, case_id, limit, context_limit: calls.update(signals=(db, case_id, limit, context_limit)) or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_replacement_trend",
		lambda db, old_case_id, new_case_id, start_year, end_year: calls.update(
			replacement=(db, old_case_id, new_case_id, start_year, end_year)
		) or replacement,
	)
	monkeypatch.setattr(
		routes,
		"_citation_landmark_candidates",
		lambda db, limit, recent_years, baseline_years, min_recent: calls.update(
			landmarks=(db, limit, recent_years, baseline_years, min_recent)
		) or [],
	)

	routes.get_contextual_citation_paths(
		source_case_id=10,
		target_case_id=20,
		max_hops=999,
		limit=999,
		per_node_limit=1,
		hop_context_limit=99,
		db=database,
	)
	routes.get_citation_authority_signals(case_id=10, limit=999, context_limit=0, db=database)
	routes.get_citation_replacement_trend(old_case_id=10, new_case_id=20, start_year=2010, end_year=2020, db=database)
	routes.get_citation_landmark_candidates(limit=999, recent_years=99, baseline_years=99, min_recent=0, db=database)

	assert calls["contextual_paths"] == (database, 10, 20, 6, 25, 5, 5)
	assert calls["signals"] == (database, 10, 80, 1)
	assert calls["replacement"] == (database, 10, 20, 2010, 2020)
	assert calls["landmarks"] == (database, 100, 10, 20, 1)

	with pytest.raises(HTTPException) as same_case:
		routes.get_citation_replacement_trend(old_case_id=10, new_case_id=10, db=database)
	assert same_case.value.status_code == 422

	with pytest.raises(HTTPException) as bad_years:
		routes.get_citation_replacement_trend(old_case_id=10, new_case_id=20, start_year=2025, end_year=2020, db=database)
	assert bad_years.value.status_code == 422


def test_case_batch_extraction_advances_by_primary_key(monkeypatch):
	cases = [SimpleNamespace(id=4), SimpleNamespace(id=9)]
	session = QueuedScalarsSession([cases, []])
	processed = []
	monkeypatch.setattr(
		citations,
		"rebuild_citations_for_case",
		lambda _session, case, chunks=None: processed.append(case.id) or 1,
	)

	inserted = citations.batch_extract_citations_from_cases(session, batch_size=2)

	assert inserted == 2
	assert processed == [4, 9]
	assert session.commits == 1


def test_chunk_batch_rebuilds_each_case_with_all_chunks(monkeypatch):
	case_4 = SimpleNamespace(id=4)
	case_9 = SimpleNamespace(id=9)
	chunks = [
		SimpleNamespace(id=1, case_id=4, chunk_index=0),
		SimpleNamespace(id=2, case_id=4, chunk_index=1),
		SimpleNamespace(id=3, case_id=9, chunk_index=0),
	]
	session = QueuedScalarsSession([[4, 9], chunks, [case_4, case_9], []])
	processed = []
	monkeypatch.setattr(
		citations,
		"rebuild_citations_for_case",
		lambda _session, case, case_chunks=None: processed.append(
			(case.id, [chunk.id for chunk in case_chunks or []])
		) or len(case_chunks or []),
	)

	inserted = citations.batch_extract_citations_from_chunks(session, batch_size=2)

	assert inserted == 3
	assert processed == [(4, [1, 2]), (9, [3])]
	assert session.commits == 1


def test_surprise_feed_endpoints_are_bounded(monkeypatch):
	database = FakeDatabase()
	calls = {}

	monkeypatch.setattr(
		routes,
		"_citation_surprise_feed",
		lambda db, category, value, start_year, end_year, limit, min_occurrences: calls.update(
			surprises=(db, category, value, start_year, end_year, limit, min_occurrences)
		)
		or [],
	)

	routes.get_citation_surprises(
		category="issue",
		value="Detention",
		start_year=2010,
		end_year=2024,
		limit=999,
		min_occurrences=0,
		db=database,
	)

	assert calls["surprises"] == (database, "issue", "Detention", 2010, 2024, 250, 1)

	with pytest.raises(HTTPException) as missing_pair:
		routes.get_citation_surprises(category="issue", value=None, db=database)
	assert missing_pair.value.status_code == 422

	with pytest.raises(HTTPException) as unsupported:
		routes.get_citation_surprises(category="procedure", value="x", db=database)
	assert unsupported.value.status_code == 422

	with pytest.raises(HTTPException) as bad_years:
		routes.get_citation_surprises(start_year=2025, end_year=2020, db=database)
	assert bad_years.value.status_code == 422


def test_doctrine_shift_endpoints_are_bounded(monkeypatch):
	database = FakeDatabase()
	calls = {}

	monkeypatch.setattr(
		routes,
		"_citation_doctrine_shifts",
		lambda db, category, value, limit, candidate_limit, start_year, end_year: calls.update(
			shifts=(db, category, value, limit, candidate_limit, start_year, end_year)
		)
		or [],
	)

	routes.get_citation_doctrine_shifts(
		category="issue",
		value="Detention",
		limit=999,
		candidate_limit=1,
		start_year=2005,
		end_year=2024,
		db=database,
	)

	assert calls["shifts"] == (database, "issue", "Detention", 50, 4, 2005, 2024)

	with pytest.raises(HTTPException) as unsupported:
		routes.get_citation_doctrine_shifts(category="outcome", value="Allowed", db=database)
	assert unsupported.value.status_code == 422

	with pytest.raises(HTTPException) as bad_years:
		routes.get_citation_doctrine_shifts(category="issue", value="Detention", start_year=2024, end_year=2020, db=database)
	assert bad_years.value.status_code == 422


def test_hidden_bridge_and_inheritance_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	other_case = SimpleNamespace(id=20)
	database = FakeDatabase(scalar_value=[case, other_case, case])
	calls = {}

	monkeypatch.setattr(
		routes,
		"_citation_hidden_bridges",
		lambda db, source_case_id, target_case_id, max_hops, path_limit, per_node_limit, bridge_limit: calls.update(
			hidden=(db, source_case_id, target_case_id, max_hops, path_limit, per_node_limit, bridge_limit)
		)
		or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_inheritance_chains",
		lambda db, case_id, max_depth, limit, per_node_limit, min_occurrences: calls.update(
			inheritance=(db, case_id, max_depth, limit, per_node_limit, min_occurrences)
		)
		or [],
	)

	routes.get_hidden_citation_bridges(
		source_case_id=10,
		target_case_id=20,
		max_hops=999,
		path_limit=999,
		per_node_limit=1,
		limit=999,
		db=database,
	)
	routes.get_citation_inheritance_chains(
		case_id=10,
		max_depth=99,
		limit=999,
		per_node_limit=0,
		min_occurrences=0,
		db=database,
	)

	assert calls["hidden"] == (database, 10, 20, 8, 40, 5, 60)
	assert calls["inheritance"] == (database, 10, 6, 60, 1, 1)

	with pytest.raises(HTTPException) as same_case:
		routes.get_hidden_citation_bridges(source_case_id=10, target_case_id=10, db=database)
	assert same_case.value.status_code == 422


def test_missing_authority_lifecycle_and_court_flow_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case])
	calls = {}

	monkeypatch.setattr(
		routes,
		"_citation_missing_authorities",
		lambda db, case_id, peer_limit, result_limit, min_peer_share, min_peer_citations: calls.update(
			missing=(db, case_id, peer_limit, result_limit, min_peer_share, min_peer_citations)
		)
		or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_authority_lifecycle",
		lambda db, category, value, start_year, end_year, limit, recent_years, prior_years: calls.update(
			lifecycle=(db, category, value, start_year, end_year, limit, recent_years, prior_years)
		)
		or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_cross_court_flow",
		lambda db, start_year, end_year, limit: calls.update(flow=(db, start_year, end_year, limit)) or [],
	)

	routes.get_citation_missing_authorities(
		case_id=10,
		peer_limit=999,
		limit=999,
		min_peer_share=0.25,
		min_peer_citations=0,
		db=database,
	)
	routes.get_citation_authority_lifecycle(
		category="issue",
		value="Detention",
		start_year=2001,
		end_year=2024,
		limit=999,
		recent_years=99,
		prior_years=99,
		db=database,
	)
	routes.get_citation_cross_court_flow(start_year=2010, end_year=2024, limit=999, db=database)

	assert calls["missing"] == (database, 10, 200, 100, 0.25, 1)
	assert calls["lifecycle"] == (database, "issue", "Detention", 2001, 2024, 120, 10, 10)
	assert calls["flow"] == (database, 2010, 2024, 200)

	with pytest.raises(HTTPException) as invalid_share:
		routes.get_citation_missing_authorities(case_id=10, min_peer_share=1.2, db=database)
	assert invalid_share.value.status_code == 422

	with pytest.raises(HTTPException) as invalid_pair:
		routes.get_citation_authority_lifecycle(category="issue", value=None, db=database)
	assert invalid_pair.value.status_code == 422

	with pytest.raises(HTTPException) as invalid_flow_years:
		routes.get_citation_cross_court_flow(start_year=2025, end_year=2020, db=database)
	assert invalid_flow_years.value.status_code == 422


def test_position_completion_and_shift_dashboard_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	other_case = SimpleNamespace(id=20)
	database = FakeDatabase(scalar_value=[case, case, other_case])
	calls = {}

	monkeypatch.setattr(
		routes,
		"_citation_position_profiles",
		lambda db, case_id, limit, min_occurrences: calls.update(
			positions=(db, case_id, limit, min_occurrences)
		)
		or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_completion_suggestions",
		lambda db, case_id, peer_limit, limit, min_peer_share, min_peer_citations: calls.update(
			completion=(db, case_id, peer_limit, limit, min_peer_share, min_peer_citations)
		)
		or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_shift_dashboard",
		lambda db, category, value, start_year, end_year, replacement_limit, lifecycle_limit, surprise_limit: calls.update(
			dashboard=(db, category, value, start_year, end_year, replacement_limit, lifecycle_limit, surprise_limit)
		)
		or {
			"category": category,
			"value": value,
			"replacement_candidates": [],
			"emerging_authorities": [],
			"declining_authorities": [],
			"surprises": [],
		},
	)

	routes.get_citation_position_profiles(case_id=10, limit=999, min_occurrences=0, db=database)
	routes.get_citation_completion_suggestions(case_id=10, peer_limit=999, limit=999, min_peer_share=0.4, min_peer_citations=0, db=database)
	routes.get_citation_shift_dashboard(
		category="issue",
		value="Detention",
		start_year=2001,
		end_year=2024,
		replacement_limit=999,
		lifecycle_limit=1,
		surprise_limit=999,
		db=database,
	)

	assert calls["positions"] == (database, 10, 120, 1)
	assert calls["completion"] == (database, 10, 200, 100, 0.4, 1)
	assert calls["dashboard"] == (database, "issue", "Detention", 2001, 2024, 30, 5, 200)

	with pytest.raises(HTTPException) as invalid_share:
		routes.get_citation_completion_suggestions(case_id=10, min_peer_share=-0.2, db=database)
	assert invalid_share.value.status_code == 422

	with pytest.raises(HTTPException) as bad_category:
		routes.get_citation_shift_dashboard(category="outcome", value="Allowed", db=database)
	assert bad_category.value.status_code == 422

	with pytest.raises(HTTPException) as bad_years:
		routes.get_citation_shift_dashboard(category="issue", value="Detention", start_year=2025, end_year=2020, db=database)
	assert bad_years.value.status_code == 422


def test_new_csv_exports_include_expected_headers(monkeypatch):
	database = FakeDatabase(scalar_value=[SimpleNamespace(id=1), SimpleNamespace(id=1), SimpleNamespace(id=2), SimpleNamespace(id=1), SimpleNamespace(id=1), SimpleNamespace(id=1), SimpleNamespace(id=1), SimpleNamespace(id=1), SimpleNamespace(id=1)])

	monkeypatch.setattr(
		routes,
		"_citation_authority_signals",
		lambda db, case_id, limit, context_limit: [
			{
				"authority": {
					"case_id": 2,
					"title": "Authority",
					"citation": "2019 SCC 65",
					"court": "SCC",
					"date": "2019-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"occurrence_count": 3,
				"distinct_chunks": 2,
				"gravity_share": 0.2,
				"global_citing_cases": 4,
				"surprise_score": 0.3,
				"originality_score": 0.4,
				"boilerplate_hits": 1,
				"first_chunk_index": 0,
				"last_chunk_index": 2,
				"sample_contexts": [],
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_surprise_feed",
		lambda db, category, value, start_year, end_year, limit, min_occurrences: [
			{
				"source_case": {
					"case_id": 1,
					"title": "Source",
					"citation": "2024 FC 10",
					"court": "FC",
					"date": "2024-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"authority": {
					"case_id": 2,
					"title": "Authority",
					"citation": "2019 SCC 65",
					"court": "SCC",
					"date": "2019-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"occurrence_count": 2,
				"global_citing_cases": 3,
				"gravity_share": 0.5,
				"surprise_score": 0.2,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_landmark_candidates",
		lambda db, limit, recent_years, baseline_years, min_recent: [
			{
				"case": {
					"case_id": 3,
					"title": "Landmark",
					"citation": "2020 SCC 1",
					"court": "SCC",
					"date": "2020-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"recent_citing_cases": 5,
				"baseline_citing_cases": 1,
				"emergence_score": 4.0,
				"lift_ratio": 5.0,
				"recent_window": {"start_year": 2022, "end_year": 2024},
				"baseline_window": {"start_year": 2017, "end_year": 2021},
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_doctrine_shifts",
		lambda db, category, value, limit, candidate_limit, start_year, end_year: [
			{
				"old_authority": {
					"case_id": 4,
					"title": "Old",
					"citation": "2001 SCC 1",
					"court": "SCC",
					"date": "2001-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"new_authority": {
					"case_id": 5,
					"title": "New",
					"citation": "2019 SCC 65",
					"court": "SCC",
					"date": "2019-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"replacement_score": 1.2,
				"status": "replacement_likely",
				"series": [],
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_hidden_bridges",
		lambda db, source_case_id, target_case_id, max_hops, path_limit, per_node_limit, bridge_limit: [
			{
				"bridge_case": {
					"case_id": 6,
					"title": "Bridge",
					"citation": "2017 FC 22",
					"court": "FC",
					"date": "2017-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"path_count": 2,
				"weighted_support": 6.5,
				"average_relative_position": 0.5,
				"average_path_hops": 3.0,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_inheritance_chains",
		lambda db, case_id, max_depth, limit, per_node_limit, min_occurrences: [
			{
				"chain_case_ids": [1, 2, 3],
				"depth": 2,
				"total_occurrences": 7,
				"nodes": [],
				"edge_occurrences": [4, 3],
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_missing_authorities",
		lambda db, case_id, peer_limit, result_limit, min_peer_share, min_peer_citations: [
			{
				"authority": {
					"case_id": 7,
					"title": "Missing",
					"citation": "2018 SCC 9",
					"court": "SCC",
					"date": "2018-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"peer_citing_cases": 9,
				"peer_coverage": 0.45,
				"peer_occurrences": 13,
				"rarity_boost": 0.33,
				"priority_score": 1.7,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_authority_lifecycle",
		lambda db, category, value, start_year, end_year, limit, recent_years, prior_years: [
			{
				"authority": {
					"case_id": 8,
					"title": "Lifecycle",
					"citation": "2015 FC 100",
					"court": "FC",
					"date": "2015-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"recent_citing_cases": 15,
				"prior_citing_cases": 10,
				"total_citing_cases": 40,
				"velocity": 5.0,
				"decay": 0.0,
				"lifecycle_stage": "emerging",
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_cross_court_flow",
		lambda db, start_year, end_year, limit: [
			{
				"source_court": "FC",
				"target_court": "SCC",
				"citing_case_count": 20,
				"citation_occurrences": 45,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_position_profiles",
		lambda db, case_id, limit, min_occurrences: [
			{
				"authority": {
					"case_id": 9,
					"title": "Positioned",
					"citation": "2014 FC 99",
					"court": "FC",
					"date": "2014-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"occurrence_count": 4,
				"avg_chunk_index": 2.5,
				"first_chunk_index": 1,
				"last_chunk_index": 4,
				"first_half_hits": 2,
				"second_half_hits": 2,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_completion_suggestions",
		lambda db, case_id, peer_limit, limit, min_peer_share, min_peer_citations: [
			{
				"authority": {
					"case_id": 10,
					"title": "Suggested",
					"citation": "2016 SCC 3",
					"court": "SCC",
					"date": "2016-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"peer_citing_cases": 8,
				"peer_coverage": 0.4,
				"rarity_boost": 0.3,
				"expected_occurrences": 12,
				"recommendation_score": 1.5,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_shift_dashboard",
		lambda db, category, value, start_year, end_year, replacement_limit, lifecycle_limit, surprise_limit: {
			"category": category,
			"value": value,
			"replacement_candidates": [
				{
					"old_authority": {
						"case_id": 4,
						"title": "Old",
						"citation": "2001 SCC 1",
						"court": "SCC",
						"date": "2001-01-01",
						"in_degree": 0,
						"out_degree": 0,
						"pagerank": None,
					},
					"new_authority": {
						"case_id": 5,
						"title": "New",
						"citation": "2019 SCC 65",
						"court": "SCC",
						"date": "2019-01-01",
						"in_degree": 0,
						"out_degree": 0,
						"pagerank": None,
					},
					"replacement_score": 1.2,
					"status": "replacement_likely",
					"series": [],
				}
			],
			"emerging_authorities": [
				{
					"authority": {
						"case_id": 8,
						"title": "Lifecycle",
						"citation": "2015 FC 100",
						"court": "FC",
						"date": "2015-01-01",
						"in_degree": 0,
						"out_degree": 0,
						"pagerank": None,
					},
					"recent_citing_cases": 15,
					"prior_citing_cases": 10,
					"total_citing_cases": 40,
					"velocity": 5.0,
					"decay": 0.0,
					"lifecycle_stage": "emerging",
				}
			],
			"declining_authorities": [],
			"surprises": [
				{
					"source_case": {
						"case_id": 1,
						"title": "Source",
						"citation": "2024 FC 10",
						"court": "FC",
						"date": "2024-01-01",
						"in_degree": 0,
						"out_degree": 0,
						"pagerank": None,
					},
					"authority": {
						"case_id": 2,
						"title": "Authority",
						"citation": "2019 SCC 65",
						"court": "SCC",
						"date": "2019-01-01",
						"in_degree": 0,
						"out_degree": 0,
						"pagerank": None,
					},
					"occurrence_count": 2,
					"global_citing_cases": 3,
					"gravity_share": 0.5,
					"surprise_score": 0.2,
				}
			],
		},
	)

	authority_csv = routes.export_citation_authority_signals(case_id=1, db=database)
	assert authority_csv.media_type == "text/csv; charset=utf-8"
	assert authority_csv.headers["content-disposition"] == 'attachment; filename="authority-signals-1.csv"'
	assert b"originality_score" in authority_csv.body

	surprises_csv = routes.export_citation_surprises(category="issue", value="Detention", db=database)
	assert surprises_csv.media_type == "text/csv; charset=utf-8"
	assert surprises_csv.headers["content-disposition"] == 'attachment; filename="citation-surprises.csv"'
	assert b"surprise_score" in surprises_csv.body

	landmarks_csv = routes.export_citation_landmark_candidates(db=database)
	assert landmarks_csv.media_type == "text/csv; charset=utf-8"
	assert landmarks_csv.headers["content-disposition"] == 'attachment; filename="landmark-candidates.csv"'
	assert b"emergence_score" in landmarks_csv.body

	shifts_csv = routes.export_citation_doctrine_shifts(category="issue", value="Detention", db=database)
	assert shifts_csv.media_type == "text/csv; charset=utf-8"
	assert shifts_csv.headers["content-disposition"] == 'attachment; filename="doctrine-shifts.csv"'
	assert b"replacement_score" in shifts_csv.body

	hidden_csv = routes.export_hidden_citation_bridges(source_case_id=1, target_case_id=2, db=database)
	assert hidden_csv.media_type == "text/csv; charset=utf-8"
	assert hidden_csv.headers["content-disposition"] == 'attachment; filename="hidden-bridges-1-to-2.csv"'
	assert b"weighted_support" in hidden_csv.body

	inheritance_csv = routes.export_citation_inheritance_chains(case_id=1, db=database)
	assert inheritance_csv.media_type == "text/csv; charset=utf-8"
	assert inheritance_csv.headers["content-disposition"] == 'attachment; filename="inheritance-chains-1.csv"'
	assert b"chain_case_ids" in inheritance_csv.body

	missing_csv = routes.export_citation_missing_authorities(case_id=1, db=database)
	assert missing_csv.media_type == "text/csv; charset=utf-8"
	assert missing_csv.headers["content-disposition"] == 'attachment; filename="missing-authorities-1.csv"'
	assert b"priority_score" in missing_csv.body

	lifecycle_csv = routes.export_citation_authority_lifecycle(db=database)
	assert lifecycle_csv.media_type == "text/csv; charset=utf-8"
	assert lifecycle_csv.headers["content-disposition"] == 'attachment; filename="authority-lifecycle.csv"'
	assert b"lifecycle_stage" in lifecycle_csv.body

	flow_csv = routes.export_citation_cross_court_flow(db=database)
	assert flow_csv.media_type == "text/csv; charset=utf-8"
	assert flow_csv.headers["content-disposition"] == 'attachment; filename="cross-court-flow.csv"'
	assert b"source_court" in flow_csv.body

	position_csv = routes.export_citation_position_profiles(case_id=1, db=database)
	assert position_csv.media_type == "text/csv; charset=utf-8"
	assert position_csv.headers["content-disposition"] == 'attachment; filename="position-profiles-1.csv"'
	assert b"avg_chunk_index" in position_csv.body

	completion_csv = routes.export_citation_completion_suggestions(case_id=1, db=database)
	assert completion_csv.media_type == "text/csv; charset=utf-8"
	assert completion_csv.headers["content-disposition"] == 'attachment; filename="completion-suggestions-1.csv"'
	assert b"recommendation_score" in completion_csv.body

	dashboard_csv = routes.export_citation_shift_dashboard(category="issue", value="Detention", db=database)
	assert dashboard_csv.media_type == "text/csv; charset=utf-8"
	assert dashboard_csv.headers["content-disposition"] == 'attachment; filename="shift-dashboard.csv"'
	assert b"replacement_candidate" in dashboard_csv.body