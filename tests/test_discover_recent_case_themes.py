from datetime import date
from types import SimpleNamespace

from scripts.discover_recent_case_themes import (
    DEFAULT_END,
    DEFAULT_START,
    build_case_theme_record,
    build_report,
)


def make_case(case_id: int, decision_date: date):
    return SimpleNamespace(
        id=case_id,
        title="Procedural fairness judicial review",
        date=decision_date,
        court="Federal Court",
        citation=f"{decision_date.year} FC {case_id}",
        summary="The application concerns procedural fairness and reasonableness review.",
        full_text="",
        metadata_json={},
    )


def make_tag():
    return SimpleNamespace(
        value="procedural_fairness",
        category="issue",
        score=0.95,
        taxonomy_version="ca_legal_v3_core",
        evidence="procedural fairness",
        offset_start=10,
        offset_end=30,
    )


def test_recent_window_is_six_years_and_inclusive():
    assert DEFAULT_START == date(2020, 9, 22)
    assert DEFAULT_END == date(2026, 9, 22)
    record = build_case_theme_record(make_case(1, DEFAULT_START), tags=[make_tag()])
    assert record["date"] == "2020-09-22"


def test_theme_record_preserves_evidence_and_classifies_central_signal():
    discussion = {
        "discussion_units": [
            {
                "subthemes": [
                    {
                        "subtheme_id": "1:1",
                        "argument_roles": ["issue", "reasoning_application"],
                        "paragraph_indices": [4, 5],
                        "key_terms": ["procedural fairness"],
                        "text": "The issue is procedural fairness.",
                        "explanation": "The court applies procedural fairness.",
                    }
                ]
            }
        ]
    }
    record = build_case_theme_record(make_case(2, date(2024, 1, 1)), tags=[make_tag()], discussion=discussion)
    theme = next(theme for theme in record["themes"] if theme["theme_id"] == "procedural_fairness")

    assert theme["status"] == "central_issue"
    assert theme["classification_factors"] == {
        "role_score": 8,
        "independent_evidence_kinds": ["discussion_role", "phrase", "subject", "tag"],
        "threshold_met": "role_score >= 4",
    }
    assert "tag" in theme["evidence_kinds"]
    assert "discussion_role" in theme["evidence_kinds"]
    role = next(item for item in theme["evidence"] if item["kind"] == "discussion_role")
    assert role["paragraph_indices"] == [4, 5]
    assert role["subtheme_id"] == "1:1"


def test_report_is_read_only_and_records_date_window():
    case = make_case(3, date(2025, 6, 1))
    case.tags = [make_tag()]
    case.statute_references = []

    class Result:
        def __init__(self, values):
            self.values = values

        def all(self):
            return self.values

    class ReadOnlySession:
        def __init__(self):
            self.write_methods_called = []
            self.read_calls = 0

        def scalars(self, query):
            self.read_calls += 1
            return Result([case] if self.read_calls == 1 else [])

        def __getattr__(self, name):
            if name in {"add", "add_all", "commit", "flush", "delete", "execute_update"}:
                self.write_methods_called.append(name)
                raise AssertionError(f"write method called: {name}")
            raise AttributeError(name)

    session = ReadOnlySession()
    report = build_report(session, DEFAULT_START, DEFAULT_END, limit=1)

    assert report["date_window"] == {"start": "2020-09-22", "end": "2026-09-22"}
    assert report["case_count"] == 1
    assert report["cases_with_themes"] == 1
    assert session.write_methods_called == []
