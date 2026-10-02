from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from backend.analytics_service import _case_influence


def test_case_influence_counts_distinct_citing_cases_and_appeal_courts():
	engine = create_engine("sqlite://")
	with engine.begin() as connection:
		connection.execute(text("CREATE TABLE cases (id INTEGER PRIMARY KEY, court TEXT)"))
		connection.execute(
			text("CREATE TABLE citations (id INTEGER PRIMARY KEY, source_case_id INTEGER, target_case_id INTEGER)")
		)
		connection.execute(text("INSERT INTO cases VALUES (1, 'FC'), (2, 'FC'), (3, 'FCA'), (4, 'SCC')"))
		connection.execute(
			text(
				"INSERT INTO citations (source_case_id, target_case_id) VALUES "
				"(2, 1), (2, 1), (3, 1), (4, 1), (1, 1), (1, 2)"
			)
		)
	with Session(engine) as db:
		result = _case_influence([1, 2, 5], db)
	assert result == {1: (3, 2), 2: (1, 0)}
	assert _case_influence([], None) == {}
