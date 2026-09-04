from io import BytesIO

from docx import Document
from fastapi.testclient import TestClient

from backend.live_analysis import _provision_excerpt, analyze_docx, validate_docx_upload
from backend.main import app


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


def test_analyze_docx_preserves_source_offsets_and_nested_references() -> None:
	content = make_docx(
		"Opening café paragraph.",
		"The decision is 2024 FC 100. The provision is IRPA s. 34(1)(f).",
	)

	result = analyze_docx(content, "sample.docx")

	assert result["filename"] == "sample.docx"
	assert result["paragraph_count"] == 2
	assert result["text"] == "Opening café paragraph.\n\nThe decision is 2024 FC 100. The provision is IRPA s. 34(1)(f)."
	assert result["text_length"] == len(result["text"])
	assert result["case_citations"][0]["reference_text"] == "2024 FC 100"
	assert result["case_citations"][0]["paragraph_index"] == 1
	statute = next(row for row in result["statute_references"] if row["reference_text"] == "IRPA s. 34(1)(f)")
	assert statute["instrument_key"] == "canada.irpa"
	assert statute["pinpoint"] == "34(1)(f)"
	assert statute["legislation_url"].endswith("/acts/I-2.5/section-34.html")


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
