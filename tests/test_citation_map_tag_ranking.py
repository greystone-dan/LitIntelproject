from types import SimpleNamespace

from backend.citation_map import _rank_tags_by_rarity_and_frequency


class FakeQuery:
	def __init__(self, value):
		self.value = value

	def where(self, *_criteria):
		return self

	def scalar(self):
		return self.value


class FakeSession:
	def __init__(self, values):
		self.values = iter(values)

	def query(self, _statement):
		return FakeQuery(next(self.values))


def test_tag_ranking_counts_distinct_cases_without_name_error():
	tag = SimpleNamespace(category="issue", value="procedural_fairness")
	session = FakeSession([2, 1])

	assert _rank_tags_by_rarity_and_frequency(session, [tag], display_limit=10) == [tag]
