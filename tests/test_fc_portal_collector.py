from pathlib import Path

from scripts.fc_portal_collector import (
    CollectorConfig,
    parse_detail_page,
    parse_listing_entries,
    run_collection,
    select_prefixes_for_run,
)


def test_parse_listing_entries_uses_class_selector():
    html = """
    <html><body>
      <a class='court-file-number' href='/files/1'>IMM-1234-24</a>
      <a class='court-file-number' href='/files/2'>IMM-9999-23</a>
      <a class='court-file-number' href='/files/3'>T-111-20</a>
    </body></html>
    """

    rows = parse_listing_entries(html, prefix="IMM", base_url="https://example.com/list")

    assert len(rows) == 2
    assert rows[0]["file_number"] == "IMM-1234-24"
    assert rows[0]["detail_url"] == "https://example.com/files/1"


def test_parse_listing_entries_fallbacks_to_all_links():
    html = """
    <html><body>
      <a href='/x'>IMM-3333-22</a>
      <a href='/y'>A-101-21</a>
    </body></html>
    """

    rows = parse_listing_entries(html, prefix="A", base_url="https://example.com/list")

    assert len(rows) == 1
    assert rows[0]["file_number"] == "A-101-21"


def test_parse_detail_page_extracts_links_and_title():
    html = """
    <html>
      <head><title>Federal Court File IMM-1-24</title></head>
      <body>
        <h1>IMM-1-24</h1>
        <a href='/eng/decisions/abc'>Decision EN</a>
        <a href='/docs/judgment.pdf'>PDF</a>
      </body>
    </html>
    """

    result = parse_detail_page(html, "https://example.com/files/1")

    assert result["page_title"] == "Federal Court File IMM-1-24"
    assert "IMM-1-24" in result["headings"]
    assert any(link.endswith("/eng/decisions/abc") for link in result["decision_links"])
    assert any(link.endswith("/docs/judgment.pdf") for link in result["decision_links"])


def test_select_prefixes_for_run_rotates_checkpointed_window():
    config = CollectorConfig(
        prefixes=["IMM", "T", "A", "X"],
        delay_ms=0,
        max_pages=1,
        max_records=10,
        timeout=5.0,
        retries=1,
        backoff_seconds=0.0,
        output_jsonl=Path("out.jsonl"),
        checkpoint_json=Path("checkpoint.json"),
        expand_details=False,
        emit_import_ready=False,
        incremental_prefix_window=2,
        incremental_run_id=None,
        ignore_robots=True,
    )
    checkpoint: dict[str, object] = {}

    first = select_prefixes_for_run(config, checkpoint)
    second = select_prefixes_for_run(config, checkpoint)

    assert first == ["IMM", "T"]
    assert second == ["A", "X"]
    assert checkpoint["rotation_run"] == 2


def test_run_collection_emits_import_ready_with_mocked_http(monkeypatch, tmp_path: Path):
    listing_html = """
    <html><body>
      <a class='court-file-number' href='/files/1'>IMM-1234-24</a>
    </body></html>
    """
    detail_html = """
    <html>
      <head><title>Federal Court File IMM-1234-24</title></head>
      <body>
      <table>
        <tr><th>Style of Cause</th><td>Doe v Canada</td></tr>
        <tr><th>Neutral Citation</th><td>2025 FC 123</td></tr>
        <tr><th>Decision Date</th><td>2025-01-02</td></tr>
      </table>
      <p>Decision reasons paragraph one.</p>
      </body>
    </html>
    """

    class FakeResponse:
        def __init__(self, text: str):
            self.text = text

        def raise_for_status(self):
            return None

    def fake_request_with_retry(_client, url, *, params, retries, backoff_seconds):
        _ = retries, backoff_seconds
        if params and params.get("court-file-number") == "IMM":
            return FakeResponse(listing_html)
        if url.endswith("/files/1"):
            return FakeResponse(detail_html)
        return FakeResponse("<html><body></body></html>")

    emitted: list[dict] = []

    def fake_append_jsonl(_path, row):
        emitted.append(row)

    monkeypatch.setattr("scripts.fc_portal_collector.is_allowed_by_robots", lambda _client: True)
    monkeypatch.setattr("scripts.fc_portal_collector.request_with_retry", fake_request_with_retry)
    monkeypatch.setattr("scripts.fc_portal_collector.append_jsonl", fake_append_jsonl)

    config = CollectorConfig(
        prefixes=["IMM"],
        delay_ms=0,
        max_pages=1,
        max_records=1,
        timeout=5.0,
        retries=1,
        backoff_seconds=0.0,
        output_jsonl=tmp_path / "collector.jsonl",
        checkpoint_json=tmp_path / "checkpoint.json",
        expand_details=True,
        emit_import_ready=True,
        incremental_prefix_window=None,
        incremental_run_id=None,
        ignore_robots=True,
    )

    scanned, written = run_collection(config)

    assert scanned == 1
    assert written == 1
    import_ready = [row for row in emitted if row.get("stage") == "import_ready"]
    assert len(import_ready) == 1
    row = import_ready[0]
    assert row["style_of_cause"] == "Doe v Canada"
    assert row["neutral_citation"] == "2025 FC 123"
    assert row["decision_date"] == "2025-01-02"
    assert row["docket_number"] == "IMM-1234-24"
    assert row["url"].endswith("/files/1")
