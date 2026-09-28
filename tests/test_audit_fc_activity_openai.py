import json

from scripts.audit_fc_activity_openai import build_messages, parse_audit_response, select_audit_cases


def test_openai_audit_selection_weights_recent_cases():
    cases = [{"activity_case_id": index, "year": 2000 + index // 10, "classification": {}} for index in range(100)]

    selected = select_audit_cases(cases, limit=12, recent_years=7, recent_share=0.75, seed=4)

    assert len(selected) == 12
    assert sum(case["year"] >= 2003 for case in selected) >= 9


def test_openai_messages_preserve_date_semantics_and_no_database_contract():
    messages = build_messages(
        [
            {
                "activity_case_id": 1,
                "year": 2024,
                "case_name": "Example v. Canada",
                "document_count": 2,
                "source_documents": [{"doc_id": 9, "source_document_date": "2024-01-01", "text": "Hearing held in Court."}],
                "classification": {
                    "procedural_events": [
                        {
                            "event_type": "leave_decision",
                            "outcome": "granted",
                            "source_document_date": "2024-01-01",
                            "doc_id": 9,
                            "rule": "leave_granted",
                            "text": "Application for leave granted.",
                        }
                    ]
                },
            }
        ]
    )

    assert "source_document_date" in messages[0]["content"]
    assert "database" in messages[0]["content"]
    assert "leave_decision" in messages[1]["content"]
    assert "Hearing held in Court" in messages[1]["content"]


def test_openai_audit_records_invalid_json_response():
    findings, error = parse_audit_response('{"findings": [}')

    assert findings == []
    assert error.startswith("JSONDecodeError:")