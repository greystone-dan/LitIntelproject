"""Live Analysis in the reader's markup view: the reader-shaped payload built from a document in memory."""

from io import BytesIO

from docx import Document
from fastapi.testclient import TestClient

from backend.database import get_db
from backend.live_analysis import paragraphs_from_pasted_text
from backend.live_reader import build_live_reader_payload, format_blocks_for_text
from backend.main import app

MEMO = (
	"MEMORANDUM\n\n"
	"I. Standard of review\n\n"
	"1. Reasonableness applies: Dunsmuir v. New Brunswick, 2008 SCC 9 at para 47, and s. 96 of the "
	"Immigration and Refugee Protection Act.\n\n"
	"The officer relied on Doe v. Canada, 2021 FC 9999 at para 15.\n"
)


def test_blocks_are_offset_ranges_into_the_unchanged_text() -> None:
	blocks = format_blocks_for_text(MEMO)
	assert [b["type"] for b in blocks] == ["heading", "heading", "para", "para"]
	assert [b.get("num") for b in blocks if b["type"] == "para"] == [1, 2]
	assert MEMO[blocks[0]["start"] : blocks[0]["end"]] == "MEMORANDUM"
	assert MEMO[blocks[2]["start"] : blocks[2]["end"]].startswith("1. Reasonableness")
	# The last paragraph is kept even though the text ends with a newline.
	assert MEMO[blocks[3]["start"] : blocks[3]["end"]].endswith("para 15.")


def test_sentences_are_not_headings() -> None:
	blocks = format_blocks_for_text("The applicant arrived in 2019.\n\nBackground")
	assert [b["type"] for b in blocks] == ["para", "heading"]


def test_payload_has_the_shape_the_reader_and_markup_mode_read() -> None:
	text, paragraphs = paragraphs_from_pasted_text(MEMO)
	payload = build_live_reader_payload(text, paragraphs, "memo.docx", None)

	assert payload["item"]["full_text"] == text and payload["item"]["id"] is None
	assert payload["readerData"]["citations"] == payload["citations"]
	assert payload["readerData"]["format_blocks"]
	assert payload["readerData"]["evidence_summary"] is None and payload["readerData"]["tags"] == []
	kinds = {row["citation_kind"] for row in payload["citations"]}
	assert "statute" in kinds and kinds - {"statute"}
	for row in payload["citations"]:
		assert text[row["offset_start"] : row["offset_end"]] == row["citation_text"]
	assert len({row["id"] for row in payload["citations"]}) == len(payload["citations"])
	assert payload["summary"]["paragraphs"] == len(paragraphs)
	# Without a library nothing resolves and nothing is invented.
	assert all(row["target_case_id"] is None for row in payload["citations"])


def test_pasted_text_paragraphs_follow_blank_lines() -> None:
	text, paragraphs = paragraphs_from_pasted_text("one\ntwo\n\nthree\r\n\r\nfour")
	assert [p.text for p in paragraphs] == ["one\ntwo", "three", "four"]
	assert all(text[p.offset_start : p.offset_end] == p.text for p in paragraphs)


class _Rows(list):
	def all(self):
		return list(self)


class _NoLibrary:
	"""A session with an empty library: every lookup comes back empty."""

	def scalars(self, *args, **kwargs):
		return _Rows()

	def scalar(self, *args, **kwargs):
		return None

	def execute(self, *args, **kwargs):
		return []


def _client() -> TestClient:
	app.dependency_overrides[get_db] = lambda: _NoLibrary()
	return TestClient(app)


def test_reader_endpoint_reads_a_docx_without_storing_it() -> None:
	document = Document()
	for block in MEMO.strip().split("\n\n"):
		document.add_paragraph(block)
	stream = BytesIO()
	document.save(stream)
	try:
		response = _client().post(
			"/live-analysis/reader",
			files={"file": ("memo.docx", stream.getvalue(), "application/vnd.openxmlformats-officedocument.wordprocessingml.document")},
		)
	finally:
		app.dependency_overrides.pop(get_db, None)
	assert response.status_code == 200
	assert response.headers["cache-control"] == "no-store"
	body = response.json()
	assert body["filename"] == "memo.docx" and body["summary"]["case_citations"] == 2
	assert body["readerData"]["format_blocks"]


def test_reader_text_endpoint_and_rejections() -> None:
	try:
		client = _client()
		ok = client.post("/live-analysis/reader-text", json={"text": MEMO, "title": "My memo"})
		assert ok.status_code == 200 and ok.json()["filename"] == "My memo"
		assert client.post("/live-analysis/reader-text", json={"text": ""}).status_code == 422
		bad = client.post("/live-analysis/reader", files={"file": ("memo.txt", b"x", "text/plain")})
		assert bad.status_code == 422
	finally:
		app.dependency_overrides.pop(get_db, None)


def test_live_reader_makes_no_model_calls() -> None:
	from pathlib import Path

	source = (Path(__file__).resolve().parents[1] / "backend" / "live_reader.py").read_text(encoding="utf-8")
	for word in ("openai", "anthropic", "embedding", "ollama"):
		assert word not in source.lower()


def test_case_name_citation_finds_its_neutral_citation_without_the_pinpoint() -> None:
	from types import SimpleNamespace

	from backend.live_analysis import _embedded_identifiers

	match = SimpleNamespace(citation_text="Canada v. Vavilov, 2019 SCC 65 at paras 10-11, 23-25")
	assert _embedded_identifiers(match) == {"2019 SCC 65"}
	assert _embedded_identifiers(SimpleNamespace(citation_text="Baker, [1999] 2 SCR 817 at para 22")) == {"[1999] 2 SCR 817"}
	assert _embedded_identifiers(SimpleNamespace(citation_text="Doe v. Canada")) == set()
