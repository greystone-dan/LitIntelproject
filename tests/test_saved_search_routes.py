from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from backend import routes
from backend.database import SavedSearch, SearchAlert


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

	def query(self, model):
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
