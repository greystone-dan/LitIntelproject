from datetime import datetime, timezone
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from backend import routes
from backend.database import Case, SavedSearch, SearchAlert


class _Query:
	def __init__(self, rows):
		self.rows = list(rows)

	def filter(self, *_criteria):
		return self

	def order_by(self, *_ordering):
		return self

	def all(self):
		return self.rows

	def first(self):
		return self.rows[0] if self.rows else None

	def count(self):
		return len(self.rows)

	def limit(self, _count):
		return self


class _MockSession:
	def __init__(self):
		self.saved_searches = []
		self.alerts = []
		self.commits = 0

	def query(self, model, *columns):
		if columns:
			assert model is Case.id
			assert len(columns) == 5
			return _Query(getattr(self, "cases", []))
		if model is SavedSearch:
			return _Query(self.saved_searches)
		if model is SearchAlert:
			return _Query(self.alerts)
		raise AssertionError(f"Unexpected query model: {model}")

	def add(self, value):
		self.saved_searches.append(value)

	def commit(self):
		self.commits += 1

	def refresh(self, value):
		value.id = len(self.saved_searches)
		value.created_at = datetime.now(timezone.utc)
		value.updated_at = value.created_at

	def delete(self, value):
		self.saved_searches.remove(value)


def _client(session):
	app = FastAPI()
	app.include_router(routes.router)
	app.dependency_overrides[routes.get_db] = lambda: session
	return TestClient(app)


def test_saved_search_collection_is_empty_without_database_rows():
	session = _MockSession()

	response = _client(session).get("/saved-searches")

	assert response.status_code == 200
	assert response.json() == []
	assert session.commits == 0


def test_saved_search_create_accepts_empty_filters_and_persists_through_mock():
	session = _MockSession()

	response = _client(session).post(
		"/saved-searches",
		json={"name": "Immigration appeals", "query": "inadmissibility"},
	)

	assert response.status_code == 201
	body = response.json()
	assert body["id"] == 1
	assert body["filters"] == {}
	assert body["search_mode"] == "semantic"
	assert body["alert_count"] == 0
	assert len(session.saved_searches) == 1
	assert session.commits == 1


def test_saved_search_ui_route_does_not_require_database():
	response = _client(_MockSession()).get("/saved-searches-ui")

	assert response.status_code == 200
	assert "Saved searches" in response.text
	assert "loadSavedSearches()" in response.text


def test_saved_search_create_accepts_filter_only_search():
	response = _client(_MockSession()).post(
		"/saved-searches",
		json={"name": "Recent FC matters", "filters": {"court": "FC"}},
	)

	assert response.status_code == 201
	assert response.json()["query"] == ""
	assert response.json()["filters"] == {"court": "FC"}


@pytest.mark.parametrize(
	("method", "path", "payload"),
	[
		("get", "/saved-searches/404", None),
		("put", "/saved-searches/404", {"name": "Missing"}),
		("delete", "/saved-searches/404", None),
		("post", "/saved-searches/404/check", None),
	],
)
def test_saved_search_item_routes_return_not_found_for_missing_search(
	method, path, payload
):
	response = getattr(_client(_MockSession()), method)(
		path, **({"json": payload} if payload is not None else {})
	)

	assert response.status_code == 404
	assert response.json()["detail"] == "Saved search not found"


@pytest.mark.parametrize("path", ["/saved-searches/digest", "/saved-searches/digest.html"])
def test_digest_static_routes_are_read_only_and_not_shadowed(path):
	session = _MockSession()
	response = _client(session).get(path)
	assert response.status_code == 200
	assert session.commits == 0
	if path.endswith(".html"):
		assert "No saved searches" in response.text
	else:
		assert response.json() == {"searches": [], "total_new_decisions": 0}


def test_digest_metadata_cohorts_counts_and_override():
	session = _MockSession()
	cutoff = datetime(2026, 10, 1, tzinfo=timezone.utc)
	session.saved_searches = [
		SimpleNamespace(id=1, name="<script>Saved</script>", last_alert_check=cutoff),
		SimpleNamespace(id=2, name="Empty", last_alert_check=None),
	]
	session.alerts = []
	session.cases = []
	for case_id in range(1, 11):
		new = case_id > 5
		session.alerts.append(SimpleNamespace(
			id=case_id, search_id=1, case_id=case_id,
			discovered_at=datetime(2026, 10, 2 if new else 1, tzinfo=timezone.utc),
		))
		session.cases.append(SimpleNamespace(
			id=case_id, title="Applicant v Canada (Citizenship and Immigration)",
			citation=f"2026 FC {case_id}", court="FC", date=cutoff.date(),
			metadata_json={"reader_extracted": {
				"government outcome": "lost" if case_id in (1, 6, 7) else "won",
				"decision outcome": "granted",
			}},
		))
	client = _client(session)
	body = client.get("/saved-searches/digest").json()
	group = body["searches"][0]
	assert group["possible_shift"] is True
	assert group["new_counts"]["minister_losses"] == 2
	assert group["earlier_counts"]["minister_losses"] == 1
	assert group["new_counts"]["decisions"] == 5
	assert group["new_matches"][0]["citation"] == "2026 FC 6"
	assert group["new_matches"][0]["court"] == "FC"
	assert body["searches"][1]["new_counts"]["decisions"] == 0
	html = client.get("/saved-searches/digest.html").text
	assert "<script>Saved</script>" not in html
	assert "&lt;script&gt;Saved&lt;/script&gt;" in html
	assert "Possible shift" in html
	override = client.get("/saved-searches/digest?since=2026-10-03T00:00:00Z").json()
	assert override["total_new_decisions"] == 0
	assert client.get("/saved-searches/digest?since=invalid").status_code == 422
	assert session.commits == 0
	assert session.saved_searches[0].last_alert_check == cutoff


def test_digest_uses_no_chunks_or_missing_case_in_denominator():
	session = _MockSession()
	session.saved_searches = [SimpleNamespace(id=1, name="Missing", last_alert_check=None)]
	session.alerts = [SimpleNamespace(id=1, search_id=1, case_id=99, discovered_at=datetime.now(timezone.utc))]
	session.cases = []
	body = _client(session).get("/saved-searches/digest").json()
	assert body["total_new_decisions"] == 0
	assert session.commits == 0
