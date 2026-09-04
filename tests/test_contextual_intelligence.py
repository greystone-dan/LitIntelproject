"""Unit and integration tests for contextual tag, statute, and citation intelligence."""

from datetime import date
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from backend.contextual_intelligence import (
	THEME_CATEGORIES,
	compute_case_thematic_signature,
	fetch_case_contextual_anchors,
	fetch_statute_tag_affinity,
	fetch_theme_breakdown,
	fetch_theme_catalog,
	find_thematically_similar_cases,
)
from backend.main import app


def test_theme_catalog_has_all_defined_themes():
	catalog = fetch_theme_catalog()
	assert len(catalog) == len(THEME_CATEGORIES)
	theme_keys = {item["theme_key"] for item in catalog}
	assert "security_inadmissibility" in theme_keys
	assert "refugee_credibility_risk" in theme_keys
	assert "humanitarian_compassionate" in theme_keys
	assert "misrepresentation_identity" in theme_keys


def test_theme_breakdown_mock():
	class FakeBreakdownDB:
		def scalar(self, statement):
			return 100

		def execute(self, statement, params=None):
			sql = str(statement)
			class FakeResult:
				def mappings(self):
					class FakeMappings:
						def all(self):
							if "FROM case_tags" in sql:
								return [
									{"category": "security", "tag_count": 50, "case_count": 20},
								]
							elif "FROM statute_references" in sql:
								return [
									{"pinpoint": "34(1)(f)", "ref_count": 30, "case_count": 15},
								]
							return []

					return FakeMappings()

			return FakeResult()

	db = FakeBreakdownDB()
	breakdown = fetch_theme_breakdown(db)

	assert breakdown["total_cases"] == 100
	assert len(breakdown["themes"]) == len(THEME_CATEGORIES)
	assert len(breakdown["tag_categories"]) == 1
	assert breakdown["tag_categories"][0]["category"] == "security"
	assert len(breakdown["top_statutory_pinpoints"]) == 1
	assert breakdown["top_statutory_pinpoints"][0]["pinpoint"] == "34(1)(f)"


def test_statute_tag_affinity_requires_pinpoint():
	db = MagicMock()
	with pytest.raises(ValueError, match="pinpoint parameter is required"):
		fetch_statute_tag_affinity(db, "")


def test_statute_tag_affinity_empty_cases():
	class EmptyDB:
		def scalars(self, statement):
			return iter([])

	db = EmptyDB()
	affinity = fetch_statute_tag_affinity(db, "nonexistent_section")
	assert affinity["pinpoint"] == "nonexistent_section"
	assert affinity["citing_cases_count"] == 0
	assert affinity["top_tag_categories"] == []


def test_fetch_case_contextual_anchors_proximity():
	case = SimpleNamespace(
		id=1,
		title="Sample Case",
		summary=None,
		full_text="[1] The applicant committed misrepresentation under IRPA s. 40(1)(a) as established in Bellido, 2005 FC 452.",
	)
	tag = SimpleNamespace(
		case_id=1,
		category="misrepresentation_identity",
		value="misrepresentation",
		offset_start=24,
		offset_end=40,
	)
	statute = SimpleNamespace(
		source_case_id=1,
		normalized_reference="Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 40(1)(a)",
		pinpoint="40(1)(a)",
		offset_start=54,
		offset_end=67,
	)
	citation = SimpleNamespace(
		source_case_id=1,
		citation_text="Bellido, 2005 FC 452",
		normalized_citation="2005 FC 452",
		target_case_id=99,
		offset_start=87,
		offset_end=107,
	)

	class MockAnchorDB:
		def scalar(self, statement):
			return case

		def scalars(self, statement):
			stmt_str = str(statement)
			if "case_tags" in stmt_str:
				return iter([tag])
			elif "statute_references" in stmt_str:
				return iter([statute])
			elif "citations" in stmt_str:
				return iter([citation])
			return iter([])

	db = MockAnchorDB()
	anchors = fetch_case_contextual_anchors(db, 1, proximity_window=100)

	assert len(anchors) == 1
	anchor = anchors[0]
	assert anchor["statute"]["pinpoint"] == "40(1)(a)"
	assert len(anchor["co_occurring_tags"]) == 1
	assert anchor["co_occurring_tags"][0]["value"] == "misrepresentation"
	assert len(anchor["co_occurring_citations"]) == 1
	assert anchor["co_occurring_citations"][0]["citation_text"] == "Bellido, 2005 FC 452"


def test_compute_case_thematic_signature():
	case = SimpleNamespace(
		id=2,
		title="Security Sample",
		citation="2024 FC 999",
		court="Federal Court",
		date=date(2024, 1, 1),
		summary="Security matter",
		full_text="Full text of security decision",
		metadata_json={"reader_extracted": {"government outcome": "won", "decision outcome": "dismissed"}},
	)
	tag = SimpleNamespace(
		case_id=2,
		category="security",
		value="terrorism",
		offset_start=10,
		offset_end=20,
	)
	statute = SimpleNamespace(
		source_case_id=2,
		normalized_reference="IRPA s. 34(1)(f)",
		pinpoint="34(1)(f)",
		offset_start=30,
		offset_end=45,
	)
	citation = SimpleNamespace(
		source_case_id=2,
		citation_text="Suresh v. Canada",
		normalized_citation="2002 SCC 1",
		target_case_id=50,
		offset_start=50,
		offset_end=66,
	)

	class MockSigDB:
		def scalar(self, statement):
			return case

		def scalars(self, statement):
			stmt_str = str(statement)
			if "case_tags" in stmt_str:
				return iter([tag])
			elif "statute_references" in stmt_str:
				return iter([statute])
			elif "citations" in stmt_str:
				return iter([citation])
			return iter([])

	db = MockSigDB()
	sig = compute_case_thematic_signature(db, 2)

	assert sig.case_id == 2
	assert sig.primary_theme == "security_inadmissibility"
	assert sig.government_outcome == "won"
	assert "34(1)(f)" in sig.top_statutes
	assert "security:terrorism" in sig.top_tags


def test_api_endpoints_contextual_intelligence():
	client = TestClient(app)

	# 1. Themes endpoint
	resp_themes = client.get("/analytics/themes")
	assert resp_themes.status_code == 200
	data_themes = resp_themes.json()
	assert "themes" in data_themes
	assert "tag_categories" in data_themes
	assert "top_statutory_pinpoints" in data_themes

	# 2. Statute-tag matrix endpoint
	resp_matrix = client.get("/analytics/statute-tag-matrix?pinpoint=34(1)(f)")
	assert resp_matrix.status_code == 200
	data_matrix = resp_matrix.json()
	assert data_matrix["pinpoint"] == "34(1)(f)"
	assert "top_tag_categories" in data_matrix
	assert "top_cited_authorities" in data_matrix
	assert "outcomes" in data_matrix
