from types import SimpleNamespace

from backend import citations


class FakeA2AJSession:
	def __init__(self, cases=None, mappings=None, edges=None, local_cases=None):
		self.added = []
		self.updated = []
		self.cases = list(cases or [])
		self.mappings = list(mappings or [])
		self.edges = list(edges or [])
		self.local_cases = list(local_cases or [])
		self.scalar_values = []
		self.commit_count = 0

	def add(self, value):
		self.added.append(value)

	def commit(self):
		self.commit_count += 1

	def scalar(self, statement):
		if self.scalar_values:
			return self.scalar_values.pop(0)
		return None

	def get(self, model, key):
		for mapping in self.mappings:
			if getattr(mapping, "a2aj_case_id", None) == key:
				return mapping
		return None

	def scalars(self, statement):
		if not hasattr(self, "_scalar_calls"):
			self._scalar_calls = 0
		self._scalar_calls += 1
		if self._scalar_calls == 1:
			return list(self.mappings)
		if self._scalar_calls == 2:
			return list(self.edges)
		if self._scalar_calls == 3:
			return list(self.local_cases)
		return list(self.cases)


def test_ingest_a2aj_cases_from_rows_stores_network_fields():
	session = FakeA2AJSession()
	rows = [
		{
			"id": "a1",
			"neutral_citation": "2024 FC 100",
			"court": "FC",
			"decision_date": "2024-01-01",
			"cases_cited": ["2023 FC 1"],
			"cases_citing": ["2024 FC 200"],
			"citing_cases_count": 4,
		},
	]

	inserted = citations.ingest_a2aj_cases_from_rows(session, rows)

	assert inserted == 1
	assert len(session.added) == 1
	stored = session.added[0]
	assert stored.a2aj_case_id == "a1"
	assert stored.neutral_citation == "2024 FC 100"
	assert stored.cases_cited == ["2023 FC 1"]
	assert stored.cases_citing == ["2024 FC 200"]
	assert stored.citing_cases_count == 4


def test_convert_a2aj_edges_to_local_creates_unified_a2aj_citations():
	mapping = SimpleNamespace(a2aj_case_id="a1", local_case_id=11)
	target_mapping = SimpleNamespace(a2aj_case_id="a2", local_case_id=22)
	edge = SimpleNamespace(
		id=1,
		source_a2aj_case_id="a1",
		target_a2aj_case_id="a2",
		normalized_citation="2024 FC 100",
	)
	session = FakeA2AJSession(mappings=[mapping, target_mapping], edges=[edge])
	session.scalar_values = [None]

	inserted = citations.convert_a2aj_edges_to_local(session)

	assert inserted == 1
	assert len(session.added) == 1
	created = session.added[0]
	assert created.source_case_id == 11
	assert created.target_case_id == 22
	assert created.provenance == "a2aj"
	assert created.unresolved is False
