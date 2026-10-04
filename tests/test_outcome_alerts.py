import json
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

from backend.outcome_alerts import _date_windows, compute_alerts_from_fixture


def test_alert_windows_use_calendar_year_boundaries():
    as_of = datetime(2025, 3, 1, 0, 0)
    previous_start, previous_end, latest_start, latest_end = _date_windows(as_of)

    assert previous_start.isoformat() == "2023-03-01"
    assert previous_end.isoformat() == "2024-03-01"
    assert latest_start.isoformat() == "2024-03-01"
    assert latest_end.isoformat() == "2025-03-02"


def test_compute_alerts_from_fixture_uses_alerts_and_cited_decision_windows():
    now = datetime(2024, 1, 1, 0, 0)
    since = (now - timedelta(days=30)).isoformat()
    saved_search = {
        "id": 1,
        "name": "Test",
        "alerts": [
            {"case_id": 100, "match_type": "older", "discovered_at": (now - timedelta(days=20)).isoformat()},
            {"case_id": 100, "match_type": "semantic_tag", "relevance_score": 0.92, "discovered_at": (now - timedelta(days=10)).isoformat()},
            {"case_id": 101, "match_type": "too_old", "discovered_at": (now - timedelta(days=40)).isoformat()},
        ],
    }

    cases = [
        {
            "id": 100,
            "title": "Case A",
            "citation": "A v B",
            "date": (now - timedelta(days=10)).date().isoformat(),
            "summary": "Not the saved-search match reason.",
            "citations": [
                {"target_case_id": 200},
                {"target_case_id": 300},
                {"target_case_id": 400},
                {"target_case_id": 500},
                {"target_case_id": None},
                {"target_case_id": 999, "citation_kind": "statute"},
            ],
        },
        {
            "id": 101,
            "title": "Old match",
            "date": (now - timedelta(days=15)).date().isoformat(),
            "citations": [{"target_case_id": 600}],
        },
    ]

    outcomes = [
        {"case_id": 100, "government_outcome": "won", "disposition_evidence": "Minister won.", "source": "deterministic_outcome", "created_at": (now - timedelta(days=9)).isoformat()},
    ]

    # Ten recent decisions against authority 200, including result case 100.
    latest_cases = []
    for i in range(201, 211):
        d = (now - timedelta(days=30)).date().isoformat()
        gov = "lost" if i in (201, 202, 203, 204) else "won"
        latest_cases.append({
            "id": i,
            "title": f"Cite{i}",
            "date": d,
            "citations": [
                {"target_case_id": 200},
                {"target_case_id": 200},  # repeated occurrences count once per decision
                {"target_case_id": 999, "citation_kind": "statute"},
            ],
        })
        outcomes.append({"case_id": i, "government_outcome": gov, "disposition_evidence": None, "source": "deterministic_outcome", "created_at": (now - timedelta(days=29)).isoformat()})

    prev_cases = []
    for i in range(211, 220):
        d = (now - timedelta(days=400)).date().isoformat()
        gov = "lost" if i in (211, 212) else "won"
        prev_cases.append({"id": i, "title": f"Cite{i}", "date": d, "citations": [{"target_case_id": 200}]})
        outcomes.append({"case_id": i, "government_outcome": gov, "disposition_evidence": None, "source": "deterministic_outcome", "created_at": (now - timedelta(days=399)).isoformat()})

    # Authority 300 has too few recent decisions and no previous decisions.
    for i in range(220, 223):
        cases.append({"id": i, "title": f"CiteAuth300_{i}", "date": (now - timedelta(days=30)).date().isoformat(), "citations": [{"target_case_id": 300}]})
        outcomes.append({"case_id": i, "government_outcome": "won", "source": "deterministic_outcome"})

    # Authority 400 has enough recent decisions but fewer than 8 previous decisions.
    for i in range(230, 238):
        cases.append({"id": i, "title": f"CiteAuth400_{i}", "date": (now - timedelta(days=30)).date().isoformat(), "citations": [{"target_case_id": 400}]})
        outcomes.append({"case_id": i, "government_outcome": "lost" if i == 230 else "won", "source": "deterministic_outcome"})
    for i in range(238, 245):
        cases.append({"id": i, "title": f"CiteAuth400_{i}", "date": (now - timedelta(days=400)).date().isoformat(), "citations": [{"target_case_id": 400}]})
        outcomes.append({"case_id": i, "government_outcome": "won", "source": "deterministic_outcome"})

    # Authority 500 has fewer than 8 recent decisions but enough previous decisions.
    for i in range(250, 256):
        cases.append({"id": i, "title": f"CiteAuth500_{i}", "date": (now - timedelta(days=30)).date().isoformat(), "citations": [{"target_case_id": 500}]})
        outcomes.append({"case_id": i, "government_outcome": "won", "source": "deterministic_outcome"})
    for i in range(257, 265):
        cases.append({"id": i, "title": f"CiteAuth500_{i}", "date": (now - timedelta(days=400)).date().isoformat(), "citations": [{"target_case_id": 500}]})
        outcomes.append({"case_id": i, "government_outcome": "won", "source": "deterministic_outcome"})

    cases.extend(latest_cases)
    cases.extend(prev_cases)

    out = compute_alerts_from_fixture(saved_search, cases, outcomes, since=since, as_of=now.isoformat())

    assert out['search_id'] == 1
    assert len(out['new_case_matches']) == 1
    match = out['new_case_matches'][0]
    assert match['case_id'] == 100
    assert 'reason' in match and 'semantic_tag' in match['reason'] and 'score' in match['reason']
    assert "Not the saved-search match reason" not in match["reason"]
    assert match["outcome"]["government_outcome"] == "won"

    aw = out['authority_watch']
    assert '200' in aw
    a200 = aw['200']
    assert a200['latest']['denominator'] == 11
    assert a200['previous']['denominator'] == 9
    assert a200['latest']['numerator'] == 4
    assert a200['previous']['numerator'] == 2
    assert a200['latest']['proportion'] == 4 / 11
    assert a200["authority_id"] == 200

    assert '300' in aw
    assert aw['300']['comparison_suppressed'] is True
    assert aw["300"]["latest"]["denominator"] == 4
    assert "proportion" not in aw["300"]["latest"]
    assert "999" not in aw

    # Each suppression case proves either independent underpowered window suppresses.
    assert aw["400"]["latest"]["denominator"] == 9
    assert aw["400"]["previous"]["denominator"] == 7
    assert aw["400"]["comparison_suppressed"] is True
    assert aw["500"]["latest"]["denominator"] == 7
    assert aw["500"]["previous"]["denominator"] == 8
    assert aw["500"]["comparison_suppressed"] is True


def test_offline_builder_writes_json_without_database_import(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    input_path = tmp_path / "input.json"
    output_path = tmp_path / "output.json"
    input_path.write_text(
        json.dumps({
            "saved_search": {
                "id": 9,
                "alerts": [{
                    "case_id": 1,
                    "match_type": "lexical",
                    "discovered_at": "2025-01-02T00:00:00+00:00",
                }],
            },
            "cases": [{
                "id": 1,
                "title": "Fixture decision",
                "date": "2020-01-01",
                "citations": [],
            }],
            "outcomes": [{
                "case_id": 1,
                "government_outcome": "lost",
                "source": "deterministic_outcome",
            }],
            "since": "2025-01-01T00:00:00+00:00",
        }),
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(repo_root / "scripts" / "build_outcome_alerts.py"),
            str(input_path),
            "--output",
            str(output_path),
            "--as-of",
            "2025-01-03T00:00:00+00:00",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert payload["search_id"] == 9
    assert payload["new_case_matches"][0]["reason"] == "lexical"
