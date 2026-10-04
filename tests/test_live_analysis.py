import asyncio
from io import BytesIO
from types import SimpleNamespace
from zipfile import ZIP_DEFLATED, ZipFile

from docx import Document
from fastapi import HTTPException
from fastapi.testclient import TestClient
from pypdf import PdfWriter
import pytest

from backend.live_analysis import _provision_excerpt, analyze_docx, validate_docx_upload
from backend.main import app
from backend import resource_limits, routes
from backend.pages.live_analysis import live_analysis_page_html


class FakeLegislationResolutionSession:
	def __init__(self, scalar_values=()):
		self.scalar_values = list(scalar_values)
		self.scalar_calls = []

	def scalar(self, statement):
		self.scalar_calls.append(str(statement))
		if self.scalar_values:
			return self.scalar_values.pop(0)
		return None


def make_docx(*paragraphs: str) -> bytes:
	document = Document()
	for paragraph in paragraphs:
		document.add_paragraph(paragraph)
	stream = BytesIO()
	document.save(stream)
	return stream.getvalue()


def make_text_pdf(*page_texts: str) -> bytes:
	objects = [
		b"<< /Type /Catalog /Pages 2 0 R >>",
		b"<< /Type /Pages /Kids [3 0 R 4 0 R] /Count 2 >>",
		b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 7 0 R >> >> /Contents 5 0 R >>",
		b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 7 0 R >> >> /Contents 6 0 R >>",
		None,
		None,
		b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
	]
	for index, page_text in enumerate(page_texts, start=5):
		encoded_text = page_text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)").encode("ascii")
		stream = b"BT /F1 12 Tf 72 720 Td (" + encoded_text + b") Tj ET"
		objects[index - 1] = b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"\nendstream"
	pdf = bytearray(b"%PDF-1.4\n")
	offsets = [0]
	for object_number, value in enumerate(objects, start=1):
		offsets.append(len(pdf))
		pdf.extend(f"{object_number} 0 obj\n".encode("ascii"))
		pdf.extend(value)
		pdf.extend(b"\nendobj\n")
	xref_offset = len(pdf)
	pdf.extend(f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode("ascii"))
	for offset in offsets[1:]:
		pdf.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
	pdf.extend(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("ascii"))
	return bytes(pdf)


def make_many_page_pdf(page_count: int) -> bytes:
	writer = PdfWriter()
	for _ in range(page_count):
		writer.add_blank_page(width=612, height=792)
	stream = BytesIO()
	writer.write(stream)
	return stream.getvalue()


def make_docx_with_expanded_entry(*paragraphs: str, expanded_bytes: int) -> bytes:
	base = make_docx(*paragraphs)
	stream = BytesIO()
	with ZipFile(BytesIO(base)) as source, ZipFile(stream, "w", ZIP_DEFLATED) as target:
		for entry in source.infolist():
			target.writestr(entry, source.read(entry.filename))
		target.writestr("word/expanded.xml", b"A" * expanded_bytes)
	return stream.getvalue()


def test_analyze_docx_preserves_source_offsets_and_nested_references() -> None:
	content = make_docx(
		"The provision is IRPA s. 34(1)(f) and IRPA s. 999.",
	)
	document = SimpleNamespace(id=101, instrument_key="canada.irpa", title="IRPA", source_url="https://example.test/irpa")
	section = SimpleNamespace(id=202, document_id=101, section_number="34", text="34 (1) This section text. (1)(f) Nested subsection text.")
	resolution_session = FakeLegislationResolutionSession([document, section, document, None])

	result = analyze_docx(content, "sample.docx", session=resolution_session)

	assert result["filename"] == "sample.docx"
	assert result["paragraph_count"] == 1
	assert result["text"] == "The provision is IRPA s. 34(1)(f) and IRPA s. 999."
	assert result["text_length"] == len(result["text"])
	assert result["case_citations"] == []
	statute = result["statute_references"][0]
	assert statute["instrument_key"] == "canada.irpa"
	assert statute["pinpoint"] == "34(1)(f)"
	assert statute["resolution_status"] == "resolved_provision"
	assert statute["source_title"] == "IRPA"
	assert statute["source_text"] == "34 (1) This section text. (1)(f) Nested subsection text."
	assert statute["source_url"] == "https://example.test/irpa"
	assert statute["authority_document_title"] == "IRPA"
	assert statute["authority_document_url"] == "https://example.test/irpa"
	assert statute["authority_section_number"] == "34"
	assert statute["authority_section_text"] == "34 (1) This section text. (1)(f) Nested subsection text."
	assert statute["section_number"] == "34"
	assert statute["legislation_url"].endswith("/acts/I-2.5/section-34.html")

	unresolved = result["statute_references"][1]
	assert unresolved["reference_text"] == "IRPA s. 999"
	assert unresolved["resolution_status"] == "section_not_indexed"
	assert unresolved["source_title"] == "IRPA"
	assert unresolved["source_text"] is None
	assert unresolved["authority_section_number"] is None
	assert unresolved["authority_section_text"] is None
	assert unresolved["section_number"] is None
	assert unresolved["offset_start"] < unresolved["offset_end"]


def test_provision_excerpt_extracts_current_subsection_from_indexed_section():
	section_text = "361 False pretence 361 (1) First subsection text. (2) Second subsection text."

	assert _provision_excerpt(section_text, "(1)") == "(1) First subsection text."
	assert _provision_excerpt(section_text, "") is None


def test_validate_docx_upload_rejects_unsupported_inputs() -> None:
	for filename, content_type, content, message in [
		("brief.txt", "text/plain", b"data", "Only .docx files are supported"),
		("brief.docx", "application/pdf", b"data", "The uploaded file must be a DOCX document"),
		("brief.docx", "application/octet-stream", b"", "The uploaded file is empty"),
	]:
		try:
			validate_docx_upload(filename, content_type, content)
		except ValueError as exc:
			assert str(exc) == message
		else:
			assert False, message


def test_live_analysis_api_is_ephemeral_and_returns_evidence() -> None:
	client = TestClient(app)
	content = make_docx("See 2024 FC 100 and IRPR s. 117.")

	response = client.post(
		"/live-analysis/analyze",
		files={
			"file": (
				"brief.docx",
				content,
				"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
			)
		},
	)

	assert response.status_code == 200
	payload = response.json()
	assert payload["filename"] == "brief.docx"
	assert payload["text"].startswith("See 2024 FC 100")
	assert payload["summary"]["case_citations"] == 1
	assert payload["summary"]["statute_references"] == 1
	assert client.get("/live-analysis").status_code == 200


def test_live_analysis_page_groups_ephemeral_evidence_in_layer_tabs() -> None:
	html = live_analysis_page_html()

	assert 'data-evidence-tab="cases"' in html
	assert 'data-evidence-tab="statutes"' in html
	assert 'function groupedEvidence(' in html
	assert 'authority_document_title||row.source_title||row.instrument_key' in html
	assert 'data-start="${row.offset_start}"' in html
	assert 'Evidence stays local to this uploaded document.' in html


def test_live_analysis_api_rejects_non_docx() -> None:
	client = TestClient(app)
	response = client.post(
		"/live-analysis/analyze",
		files={"file": ("brief.txt", b"not a document", "text/plain")},
	)

	assert response.status_code == 422
	assert response.json()["detail"] == "Only .docx and text-based .pdf files are supported"


def test_live_analysis_api_extracts_text_pdf_with_page_numbers() -> None:
	client = TestClient(app)
	content = make_text_pdf("See 2024 FC 100.", "IRPA s. 34(1)(f) applies.")

	response = client.post(
		"/live-analysis/analyze",
		files={"file": ("brief.pdf", content, "application/pdf")},
	)

	assert response.status_code == 200, response.text
	payload = response.json()
	assert payload["filename"] == "brief.pdf"
	assert payload["paragraph_count"] == 2
	assert payload["case_citations"][0]["page_number"] == 1
	assert payload["statute_references"][0]["page_number"] == 2
	assert payload["summary"] == {
		"case_citations": 1,
		"resolved_case_citations": 0,
		"unresolved_case_citations": 1,
		"statute_references": 1,
	}


@pytest.mark.parametrize("path", ["/live-analysis/analyze", "/live-analysis/resolve", "/memo-citation-check"])
def test_analysis_routes_reject_oversized_uploads_with_413(path: str, monkeypatch) -> None:
	monkeypatch.setattr(resource_limits, "MAX_UPLOAD_BYTES", 16)
	client = TestClient(app)
	response = client.post(
		path,
		files={"file": ("brief.docx", b"x" * 17, "application/octet-stream")},
	)

	assert response.status_code == 413
	assert response.json()["detail"] == "The uploaded file exceeds the 16 byte limit"


def test_upload_reader_stops_after_limit_plus_one_byte(monkeypatch) -> None:
	class TrackedUpload:
		def __init__(self) -> None:
			self.remaining = b"x" * 100
			self.read_sizes: list[int] = []

		async def read(self, size: int) -> bytes:
			self.read_sizes.append(size)
			chunk, self.remaining = self.remaining[:size], self.remaining[size:]
			return chunk

	upload = TrackedUpload()
	monkeypatch.setattr(resource_limits, "MAX_UPLOAD_BYTES", 10)

	with pytest.raises(HTTPException) as error:
		asyncio.run(routes._read_upload_bounded(upload))

	assert error.value.status_code == 413
	assert sum(upload.read_sizes) == 11


def test_docx_expanded_size_limit_is_enforced_by_live_analysis(monkeypatch) -> None:
	base = make_docx("ordinary content")
	with ZipFile(BytesIO(base)) as archive:
		base_uncompressed_bytes = sum(entry.file_size for entry in archive.infolist())
	monkeypatch.setattr(resource_limits, "MAX_DOCX_UNCOMPRESSED_BYTES", base_uncompressed_bytes + 32)
	content = make_docx_with_expanded_entry("ordinary content", expanded_bytes=4096)
	response = TestClient(app).post(
		"/live-analysis/analyze",
		files={"file": ("brief.docx", content, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")},
	)

	assert response.status_code == 413
	assert "DOCX uncompressed content" in response.json()["detail"]


def test_docx_archive_entry_limit_is_enforced(monkeypatch) -> None:
	monkeypatch.setattr(resource_limits, "MAX_DOCX_ARCHIVE_ENTRIES", 1)
	content = make_docx("ordinary content")

	with pytest.raises(resource_limits.ResourceLimitError, match="DOCX archive exceeds"):
		analyze_docx(content, "brief.docx")


def test_pdf_page_and_extracted_text_limits_are_enforced(monkeypatch) -> None:
	monkeypatch.setattr(resource_limits, "MAX_PDF_PAGES", 2)
	many_pages = make_many_page_pdf(3)
	page_response = TestClient(app).post(
		"/live-analysis/analyze",
		files={"file": ("brief.pdf", many_pages, "application/pdf")},
	)
	assert page_response.status_code == 413
	assert "PDF exceeds the 2 page limit" in page_response.json()["detail"]

	monkeypatch.setattr(resource_limits, "MAX_PDF_PAGES", 10)
	monkeypatch.setattr(resource_limits, "MAX_EXTRACTED_TEXT_CHARS", 5)
	text_response = TestClient(app).post(
		"/live-analysis/analyze",
		files={"file": ("brief.pdf", make_text_pdf("This text is too long.", "OK"), "application/pdf")},
	)
	assert text_response.status_code == 413
	assert "extracted document text" in text_response.json()["detail"]


def test_resource_limit_environment_overrides_are_positive_integers(monkeypatch) -> None:
	monkeypatch.setenv("LITINTEL_MAX_UPLOAD_BYTES", "1234")

	assert resource_limits._positive_int("LITINTEL_MAX_UPLOAD_BYTES", 99) == 1234

	monkeypatch.setenv("LITINTEL_MAX_UPLOAD_BYTES", "0")
	with pytest.raises(ValueError, match="must be a positive integer"):
		resource_limits._positive_int("LITINTEL_MAX_UPLOAD_BYTES", 99)


def test_live_analysis_responses_have_no_cache_headers() -> None:
	"""Both upload endpoints must prevent caching their sensitive payloads."""
	client = TestClient(app)
	content = make_docx("A temporary upload with no citations.")

	analyze_response = client.post(
		"/live-analysis/analyze",
		files={
			"file": (
				"brief.docx",
				content,
				"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
			)
		},
	)

	resolve_response = client.post(
		"/live-analysis/resolve",
		files={
			"file": (
				"brief.docx",
				content,
				"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
			)
		},
	)

	for response in (analyze_response, resolve_response):
		assert response.status_code == 200
		assert response.headers.get("Cache-Control") == "no-store"
		assert response.headers.get("Pragma") == "no-cache"
		assert response.json()["filename"] == "brief.docx"
