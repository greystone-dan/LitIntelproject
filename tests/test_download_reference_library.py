from __future__ import annotations

import hashlib
import json
from pathlib import Path

from scripts.download_reference_library import download_entry, run


class FakeResponse:
    def __init__(self, content: bytes, content_type: str, url: str = "https://example.test/final") -> None:
        self.content = content
        self.headers = {"Content-Type": content_type}
        self.url = url

    def raise_for_status(self) -> None:
        return None


class FakeSession:
    def __init__(self, response: FakeResponse) -> None:
        self.response = response
        self.calls = 0

    def get(self, *args, **kwargs) -> FakeResponse:
        self.calls += 1
        return self.response


def pdf_entry() -> dict:
    return {
        "id": "test-pdf",
        "source_url": "https://example.test/document.pdf",
        "source_type": "pdf",
        "local_path": "documents/test.pdf",
        "status": "pending",
    }


def xml_entry() -> dict:
    return {
        "id": "test-xml",
        "source_url": "https://example.test/act.xml",
        "source_type": "xml",
        "local_path": "documents/test.xml",
        "status": "pending",
    }


def test_download_pdf_records_provenance_and_checksum(tmp_path: Path) -> None:
    content = b"%PDF-1.7\nmock document\n%%EOF"
    session = FakeSession(FakeResponse(content, "application/pdf; charset=binary"))

    entry = download_entry(pdf_entry(), tmp_path, session, timeout=5)

    assert (tmp_path / "documents" / "test.pdf").read_bytes() == content
    assert entry["status"] == "downloaded"
    assert entry["mime_type"] == "application/pdf"
    assert entry["sha256"] == hashlib.sha256(content).hexdigest()
    assert entry["size_bytes"] == len(content)
    assert entry["final_url"] == "https://example.test/final"
    assert entry["retrieved_at"]


def test_download_xml_records_provenance_and_checksum(tmp_path: Path) -> None:
    content = b"<?xml version=\"1.0\"?><Statute><Section><Label>1</Label></Section></Statute>"
    session = FakeSession(FakeResponse(content, "text/xml"))

    entry = download_entry(xml_entry(), tmp_path, session, timeout=5)

    assert (tmp_path / "documents" / "test.xml").read_bytes() == content
    assert entry["status"] == "downloaded"
    assert entry["mime_type"] == "text/xml"
    assert entry["sha256"] == hashlib.sha256(content).hexdigest()


def test_pdf_entry_rejects_html_without_leaving_file(tmp_path: Path) -> None:
    session = FakeSession(FakeResponse(b"<!doctype html><title>Error</title>", "text/html"))
    entry = pdf_entry()

    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(
        json.dumps({"schema_version": "reference_library_v1", "documents": [entry]}),
        encoding="utf-8",
    )
    counts = run(manifest_path, session=session)

    saved = json.loads(manifest_path.read_text(encoding="utf-8"))["documents"][0]
    assert counts == {"downloaded": 0, "skipped": 0, "failed": 1}
    assert saved["status"] == "failed"
    assert "Expected PDF MIME type" in saved["error_reason"]
    assert not (tmp_path / "documents" / "test.pdf").exists()


def test_matching_checksum_skips_existing_download(tmp_path: Path) -> None:
    content = b"%PDF-1.7\nexisting\n%%EOF"
    destination = tmp_path / "documents" / "test.pdf"
    destination.parent.mkdir()
    destination.write_bytes(content)
    entry = pdf_entry()
    entry.update({"status": "downloaded", "sha256": hashlib.sha256(content).hexdigest()})
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(
        json.dumps({"schema_version": "reference_library_v1", "documents": [entry]}),
        encoding="utf-8",
    )
    session = FakeSession(FakeResponse(b"", "application/octet-stream"))

    counts = run(manifest_path, session=session)

    assert counts == {"downloaded": 0, "skipped": 1, "failed": 0}
    assert session.calls == 0
    inventory = (tmp_path / "inventory.csv").read_text(encoding="utf-8")
    assert "test-pdf" in inventory
    assert "documents/test.pdf" in inventory