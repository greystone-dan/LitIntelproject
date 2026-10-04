from types import SimpleNamespace

from scripts import check_saved_searches


class _Query:
	def __init__(self, rows):
		self.rows = rows

	def filter(self, *_criteria):
		return self

	def all(self):
		return self.rows


class _Session:
	def __init__(self, alerts=()):
		self.alerts = list(alerts)
		self.added = []
		self.commits = 0

	def query(self, model):
		return _Query(self.alerts)

	def add(self, value):
		self.added.append(value)

	def commit(self):
		self.commits += 1


def test_build_search_arguments_preserves_saved_query_filters_and_bounds():
	search = SimpleNamespace(
		query="inadmissibility",
		filters={"court": "FC", "search_full_text": "true", "limit": 500},
	)

	args = check_saved_searches.build_search_arguments(search, result_limit=500)

	assert args["query"] == "inadmissibility"
	assert args["court"] == "FC"
	assert args["search_full_text"] is True
	assert args["limit"] == 100
	assert args["offset"] == 0


def test_check_saved_search_dry_run_deduplicates_without_writing(monkeypatch):
	search = SimpleNamespace(id=7, query="Mason", filters={}, last_alert_check=None)
	db = _Session(alerts=[SimpleNamespace(case_id=1)])
	monkeypatch.setattr(
		check_saved_searches,
		"_fetch_analytics_search_cases",
		lambda *_args, **_kwargs: {"results": [{"case_id": 1}, {"case_id": 2}]},
	)

	result = check_saved_searches.check_saved_search(db, search, apply=False)

	assert result == {"search_id": 7, "matched_cases": 2, "new_alerts": 1}
	assert db.added == []
	assert db.commits == 0
	assert search.last_alert_check is None


def test_check_saved_search_apply_records_only_new_alerts(monkeypatch):
	search = SimpleNamespace(id=7, query="Mason", filters={}, last_alert_check=None)
	db = _Session(alerts=[SimpleNamespace(case_id=1)])
	monkeypatch.setattr(
		check_saved_searches,
		"_fetch_analytics_search_cases",
		lambda *_args, **_kwargs: {"results": [{"case_id": 1}, {"case_id": 2}]},
	)

	result = check_saved_searches.check_saved_search(db, search, apply=True)

	assert result["new_alerts"] == 1
	assert db.added[0].case_id == 2
	assert db.commits == 1
	assert search.last_alert_check is not None
