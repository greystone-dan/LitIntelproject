from backend import analytics_service
from tests.test_search_matching import AnalyticsDB


def test_cites_case_id_filters_on_resolved_citation_with_bound_param():
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, cites_case_id=35874)
	assert "picked.target_case_id = :cites_case_id" in db.sql
	assert db.params["cites_case_id"] == 35874
	assert "35874" not in db.sql


def test_tags_filter_requires_every_selected_tag_and_matches_both_spellings():
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, tags="Removal Order, reasonableness,removal_order")
	assert db.sql.count("FROM case_tags") == 2
	assert db.params["tag_0"] == "removal_order" and db.params["tag_0_sp"] == "removal order"
	assert db.params["tag_1"] == "reasonableness"
	assert db.params["tag_version"] == analytics_service.ACTIVE_TAG_TAXONOMY_VERSION
	assert "reasonableness" not in db.sql


def test_tags_are_capped_and_hostile_text_is_never_interpolated():
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, tags="a,b,c,d,e,f,x'; DROP TABLE cases;--")
	assert db.sql.count("FROM case_tags") == 5
	assert "DROP TABLE" not in db.sql


def test_no_tag_or_picked_case_adds_no_filter():
	db = AnalyticsDB()
	analytics_service.fetch_analytics_search_cases(db, query="Baker")
	assert "case_tags" not in db.sql and "picked" not in db.sql


class VocabDB:
	calls = 0

	def execute(self, statement, params):
		VocabDB.calls += 1
		return self

	def mappings(self):
		return self

	def all(self):
		return [
			dict(value="reasonableness", category="issue", n=900),
			dict(value="removal_order", category="issue", n=300),
			dict(value="unreasonable_delay", category="issue", n=50),
		]


def test_tag_suggestions_match_substring_prefix_first_and_cache_the_vocabulary():
	analytics_service._TAG_VOCABULARY_CACHE.update({"at": 0.0, "rows": []})
	VocabDB.calls = 0
	rows = analytics_service.fetch_tag_suggestions(VocabDB(), "reason")
	assert rows[0]["value"] == "reasonableness" and rows[0]["count"] == 900
	assert [r["label"] for r in analytics_service.fetch_tag_suggestions(VocabDB(), "removal order")] == ["removal order"]
	assert VocabDB.calls == 1
