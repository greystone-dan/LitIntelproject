from scripts.build_fc_activity_audit_report import build_report, render_markdown


def test_build_report_preserves_case_findings_and_source_evidence(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    (package / "manifest.json").write_text(
        '{"counts": {"cases": 1, "documents": 1, "classifications": 1}, "classifier_versions": ["test"], "known_limitations": []}',
        encoding="utf-8",
    )
    (package / "cases.jsonl").write_text('{"activity_case_id": 7, "case_name": "Example", "year": 2024}\n', encoding="utf-8")
    (package / "documents.jsonl").write_text('{"activity_document_id": 8, "activity_case_id": 7, "recorded_entry": "Order rendered."}\n', encoding="utf-8")
    (package / "classifications.jsonl").write_text(
        '{"activity_case_id": 7, "classifier_version": "test", "classification": {"procedural_events": [{"event_type": "decision", "doc_id": 8, "rule": "final", "text": "Order rendered."}]}}\n',
        encoding="utf-8",
    )

    report = build_report(package)
    markdown = render_markdown(report)

    assert report["case_count"] == 1
    assert report["cases"][0]["findings"][0]["source_recorded_entry"] == "Order rendered."
    assert "Order rendered." in markdown
    assert "final" in markdown


def test_build_report_renders_legacy_classifier_evidence(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    (package / "manifest.json").write_text('{"counts": {}, "known_limitations": []}', encoding="utf-8")
    (package / "cases.jsonl").write_text('{"activity_case_id": 7, "case_name": "Example"}\n', encoding="utf-8")
    (package / "documents.jsonl").write_text('{"activity_document_id": 8, "activity_case_id": 7, "recorded_entry": "Filed application."}\n', encoding="utf-8")
    (package / "classifications.jsonl").write_text(
        '{"activity_case_id": 7, "classification": {"application_filed": {"status": "yes", "date": "2024-01-01", "doc_id": 8, "text": "Filed application.", "rule": "application"}}}\n',
        encoding="utf-8",
    )

    report = build_report(package)

    assert report["cases"][0]["findings"][0]["event_type"] == "application_filed"
    assert report["cases"][0]["findings"][0]["source_recorded_entry"] == "Filed application."