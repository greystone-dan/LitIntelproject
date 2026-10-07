"""Live Analysis in the reader's markup view: the reader-shaped payload built from a document in memory."""

import contextlib
from io import BytesIO
import types

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
	assert payload["readerData"]["evidence_summary"] is None and isinstance(payload["readerData"]["tags"], list)
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
		return _Rows()

	def begin_nested(self):
		return contextlib.nullcontext()

	def get_bind(self):
		return types.SimpleNamespace(dialect=types.SimpleNamespace(name="sqlite"))


class _BrokenLibrary(_NoLibrary):
	def execute(self, *args, **kwargs):
		raise RuntimeError("canceling statement due to statement timeout")


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


FC_MEMO = """REASONS FOR JUDGMENT

[1] Review under section 112 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].

[2] Reasonableness: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at paras 10-11, 23-25. See Baker v Canada (Minister of Citizenship and Immigration), [1999] 2 SCR 817 at paras 22-27; Khosa, 2009 SCC 12 at paras 59, 61 and 63.

[3] Under paragraph 97(1)(b) of the IRPA, and in Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93 at para 35, and Singh v. Canada (MCI), 2018 FC 456 at para. 12.
"""


def test_pasted_fc_style_text_finds_the_common_citation_forms() -> None:
	text, paragraphs = paragraphs_from_pasted_text(FC_MEMO)
	rows = build_live_reader_payload(text, paragraphs, "Pasted text", None)["citations"]
	found = {text[r["offset_start"] : r["offset_end"]] for r in rows}
	assert any(f.startswith("Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65") for f in found)
	assert any("[1999] 2 SCR 817" in f for f in found)
	assert any("2009 SCC 12" in f for f in found)
	assert any("2016 FCA 93" in f for f in found) and any("2018 FC 456" in f for f in found)
	assert any(r["citation_kind"] == "statute" and r.get("pinpoint") == "97(1)(b)" for r in rows)
	assert any(r["citation_kind"] == "statute" and r.get("pinpoint") == "112" for r in rows)
	# Known gaps of the shared extractor (not fixed here): semicolon-joined citations come back as one match
	# ("Baker ...; Khosa ...") and a lead-in such as "Under paragraph 97(1)(b) of the IRPA, and in" can be
	# swallowed into the next case's match.


def test_signal_words_are_not_part_of_the_marked_citation() -> None:
	text, paragraphs = paragraphs_from_pasted_text("[1] Compare Suresh v. Canada, 2002 SCC 1 at para 29, and the rest.")
	rows = build_live_reader_payload(text, paragraphs, "Pasted text", None)["citations"]
	row = next(r for r in rows if "Suresh" in r["citation_text"])
	assert row["citation_text"].startswith("Suresh v. Canada")
	assert text[row["offset_start"] : row["offset_end"]] == row["citation_text"]


def test_back_references_are_added_and_marked_as_heuristic() -> None:
	text, paragraphs = paragraphs_from_pasted_text(
		"[1] See Canada v Vavilov, 2019 SCC 65 at para 10. [2] Vavilov, above at para 99. Ibid at para 20."
	)
	rows = build_live_reader_payload(text, paragraphs, "Pasted text", None)["citations"]
	back = [r for r in rows if r.get("heuristic_note")]
	assert [text[r["offset_start"] : r["offset_end"]] for r in back] == ["Vavilov, above at para 99", "Ibid at para 20"]
	assert all(r["citation_kind"] == "case_short" and "heuristic" in r["heuristic_note"] for r in back)
	assert not any(r.get("heuristic_note") for r in rows if "2019 SCC 65" in r["citation_text"])


def test_a_library_that_cannot_be_checked_is_not_reported_as_missing() -> None:
	text = "See Canada v Vavilov, 2019 SCC 65 at para 99."
	text, paragraphs = paragraphs_from_pasted_text(text)
	broken = build_live_reader_payload(text, paragraphs, "memo", _BrokenLibrary())
	empty = build_live_reader_payload(text, paragraphs, "memo", _NoLibrary())
	assert {c["library_status"] for c in broken["citations"] if c["citation_kind"] != "statute"} == {"lookup_failed"}
	assert broken["summary"]["library_lookup_failed"] is True
	assert {c["library_status"] for c in empty["citations"] if c["citation_kind"] != "statute"} == {"not_found"}
	assert empty["summary"]["library_lookup_failed"] is False


def test_a_citation_matches_only_as_a_whole_stored_citation() -> None:
	from backend.live_analysis import _identifier_in

	assert _identifier_in("Vavilov, 2019 SCC 65 (CanLII)", "2019 SCC 65")
	assert _identifier_in("2019  scc 65", "2019 SCC 65")
	assert not _identifier_in("2019 SCC 650", "2019 SCC 65")
	assert not _identifier_in("12019 SCC 65", "2019 SCC 65")
	assert not _identifier_in(None, "2019 SCC 65")


def test_a_failed_lookup_names_its_reason_in_the_summary() -> None:
	text, paragraphs = paragraphs_from_pasted_text("See Canada v Vavilov, 2019 SCC 65 at para 99.")
	summary = build_live_reader_payload(text, paragraphs, "memo", _BrokenLibrary())["summary"]
	assert "statement timeout" in summary["library_lookup_error"]
	assert isinstance(summary["library_lookup_ms"], int)


def test_statute_extraction_time_grows_gently_with_text_length() -> None:
	"""Statute extraction rescanned the whole text for every provision, so a long memo took many seconds."""
	import time

	from backend.citations import extract_statute_reference_matches

	paragraph = "The officer erred. Under section 96 of the IRPA and subsection 25(1) of the IRPA the test is met. See Smith J. at para 4. "
	text = paragraph * 400
	started = time.perf_counter()
	rows = extract_statute_reference_matches(text)
	assert rows
	assert time.perf_counter() - started < 5


def test_sentence_breaks_skip_single_letter_initials() -> None:
	from backend.citations import _sentence_break_ends

	text = "Smith J. said so. Done! Really? Yes"
	assert _sentence_break_ends(text) == [text.index("so.") + 3, text.index("Done!") + 5, text.index("Really?") + 7]
	assert _sentence_break_ends(".a. b") == [1]


def test_scr_citation_matches_with_or_without_dots() -> None:
	from backend.live_analysis import _citation_variants

	assert "[1999] 2 SCR 817" in _citation_variants("[1999] 2 S.C.R. 817")
	assert "[1999] 2 S.C.R. 817" in _citation_variants("[1999] 2 SCR 817")


def test_mock_documents_find_their_known_citations_without_a_library() -> None:
	"""The synthetic memos in tests/live_analysis_mocks: every case, back-reference and statute is still found."""
	from pathlib import Path

	from scripts.run_live_analysis_mocks import score

	report = score(Path(__file__).parent / "live_analysis_mocks", _NoLibrary())
	assert report
	# without a library nothing can be in it, so only check the extraction itself
	failed = [label for doc in report for label, ok in doc["results"] if not ok and not label.startswith(("case: Vavilov", "case: Baker", "case: Khosa", "case: Dunsmuir", "case: Smith"))]
	assert failed == []


_DECISION = """Citation: Canada (Citizenship and Immigration) v. Khosa, 2009 SCC 12, [2009] 1 S.C.R. 339
Date: 20090306
Docket: 31952

Reasons for Judgment:

[1] Binnie J. — This appeal concerns the standard of review of a decision of the Immigration Appeal Division.

[2] The respondent was found to be inadmissible. See Dunsmuir v. New Brunswick, 2008 SCC 9 at para 47.

[3] The appeal is allowed under section 18.1 of the Federal Courts Act.

[4] The first issue is the standard of review.

[5] The second issue is the remedy.

[6] The third issue is costs.

[7] Appeal allowed, without costs.
"""


def test_a_pasted_decision_gets_decision_formatting_and_header_details() -> None:
	text, paragraphs = paragraphs_from_pasted_text(_DECISION)
	payload = build_live_reader_payload(text, paragraphs, "Pasted text", _NoLibrary())
	assert payload["item"]["citation"] == "2009 SCC 12"
	assert payload["item"]["court"] == "Supreme Court of Canada"
	assert payload["item"]["date"] == "2009-03-06"
	assert payload["decision"]["outcome"] == "allowed"
	assert payload["summary"]["paragraphs"] == 7
	assert {b["type"] for b in payload["readerData"]["format_blocks"]} >= {"para"}


def test_a_memo_gets_no_decision_details() -> None:
	text, paragraphs = paragraphs_from_pasted_text("Overview\n\n1. The test is reasonableness. See Vavilov, 2019 SCC 65.\n\n2. Second point.")
	payload = build_live_reader_payload(text, paragraphs, "memo", _NoLibrary())
	assert payload["decision"] is None
	assert payload["item"]["citation"] is None


def test_a_document_gets_rule_based_tags_and_opens_formatted() -> None:
	text, paragraphs = paragraphs_from_pasted_text(
		"1. The Federal Court reviews the decision on a reasonableness standard under the Immigration and Refugee Protection Act.\n\n"
		"2. Procedural fairness was not breached. See section 96 of the Act."
	)
	payload = build_live_reader_payload(text, paragraphs, "memo", _NoLibrary())
	tags = payload["readerData"]["tags"]
	assert tags
	assert {"forum", "statute", "issue"} <= {tag["category"] for tag in tags}
	assert all(tag["offset_end"] > tag["offset_start"] for tag in tags)
	from backend.pages.live_analysis import live_analysis_page_html

	html = live_analysis_page_html()
	assert "toggle.getAttribute('aria-pressed')==='true')toggle.click()" in html


def test_live_analysis_goes_full_screen_inside_the_workbench() -> None:
	from backend.pages.live_analysis import live_analysis_page_html
	from backend.pages.workbench import workbench_page_html

	assert "ilitLive" in live_analysis_page_html()
	html = workbench_page_html()
	assert "reading-live" in html and "ilitLive" in html
