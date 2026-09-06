from hashlib import sha256
from types import SimpleNamespace

import pytest

from scripts.chunk_cases import build_case_chunk_layers, build_case_chunks, chunk_pending_cases, split_text


class ScalarRows:
    def __init__(self, rows):
        self.rows = rows

    def all(self):
        return self.rows


class FakeSession:
    def __init__(self, batches):
        self.batches = iter(batches)
        self.added = []
        self.commits = 0

    def scalars(self, statement):
        return ScalarRows(next(self.batches))

    def add_all(self, rows):
        self.added.extend(rows)

    def commit(self):
        self.commits += 1


def test_split_text_uses_expected_overlap():
    chunks = split_text("abcdefghij", chunk_chars=6, overlap_chars=2)

    assert chunks == ["abcdef", "efghij"]


def test_split_text_rejects_nonadvancing_overlap():
    with pytest.raises(ValueError, match="overlap_chars"):
        split_text("text", chunk_chars=4, overlap_chars=4)


def test_build_case_chunks_falls_back_to_summary_and_hashes_text():
    case = SimpleNamespace(id=12, full_text="  ", summary="summary text")

    rows = build_case_chunks(case)

    assert len(rows) == 1
    assert rows[0].case_id == 12
    assert rows[0].chunk_set == "paragraph"
    assert rows[0].chunk_index == 0
    assert rows[0].text == "summary text"
    assert rows[0].text_hash == sha256(b"summary text").hexdigest()
    assert rows[0].token_estimate == 3
    assert rows[0].chunk_label == "document"


def test_build_case_chunk_layers_creates_full_section_and_paragraph_rows():
    case = SimpleNamespace(
        id=13,
        full_text="OVERVIEW\n[1] First paragraph.\n[2] Second paragraph.",
        summary=None,
    )

    rows = build_case_chunk_layers(case)

    assert [row.chunk_set for row in rows] == ["full_case", "section", "paragraph", "paragraph", "paragraph"]
    assert rows[0].chunk_label == "Full case"
    assert rows[0].text == case.full_text
    assert rows[1].chunk_label == "Overview"
    assert [row.chunk_label for row in rows[2:]] == ["intro", "1", "2"]


def test_build_case_chunk_layers_uses_confident_html_headings():
    case = SimpleNamespace(
        id=14,
        full_text="Title\nI. BACKGROUND\n[1] First paragraph.\nII. ANALYSIS\n[2] Second paragraph.",
        summary=None,
        source_html="<article><h1>I. BACKGROUND</h1><p>[1] First paragraph.</p><h1>II. ANALYSIS</h1><p>[2] Second paragraph.</p></article>",
    )

    rows = build_case_chunk_layers(case)

    assert [row.chunk_label for row in rows if row.chunk_set == "section"] == ["Intro Metadata", "Background", "Analysis"]
    assert all(row.text in case.full_text for row in rows)


def test_scc_text_fallback_handles_old_numbered_paragraphs_and_roman_sections():
    case = SimpleNamespace(
        id=15,
        court="SCC",
        full_text=(
            "Decision title\n2002 SCC 1\n"
            "I. Background\n1 The Court considered the appeal.\n"
            "II. Analysis\n2 The application was dismissed.\n"
            "APPEARANCES:\nCounsel"
        ),
        summary=None,
        source_html=None,
    )

    rows = build_case_chunk_layers(case)

    sections = [row for row in rows if row.chunk_set == "section"]
    paragraphs = [row for row in rows if row.chunk_set == "paragraph"]
    assert [row.chunk_label for row in sections] == ["Intro Metadata", "Background", "Analysis"]
    assert [row.chunk_label for row in paragraphs] == ["intro", "1", "2", "tail"]
    assert all(row.text in case.full_text for row in rows)
    assert all(row.chunk_label != "2002" for row in paragraphs)


def test_scc_text_fallback_handles_bracketed_modern_paragraphs():
    case = SimpleNamespace(
        id=16,
        court="SCC",
        full_text="Metadata\nII. Reasons\n[1] First reason.\n[2] Second reason.",
        summary=None,
        source_html=None,
    )

    paragraphs = [row for row in build_case_chunk_layers(case) if row.chunk_set == "paragraph"]

    assert [row.chunk_label for row in paragraphs] == ["intro", "1", "2"]
    assert [row.paragraph_start for row in paragraphs] == [0, 1, 2]


def test_scc_text_fallback_uses_body_lines_for_older_unnumbered_decisions():
    case = SimpleNamespace(
        id=17,
        court="SCC",
        full_text=(
            "Metadata\nCases Cited\nR v Example\n"
            "//The Court//\nThe following is the judgment delivered by\n"
            "The appeal is allowed.\nThe matter is remitted.\n"
            "Solicitor for the respondent: Justice Canada."
        ),
        summary=None,
        source_html=None,
    )

    paragraphs = [row for row in build_case_chunk_layers(case) if row.chunk_set == "paragraph"]

    assert [row.chunk_label for row in paragraphs] == ["body-1", "body-2", "body-3", "body-4", "tail"]
    assert paragraphs[0].text == "//The Court//"
    assert paragraphs[-2].text == "The matter is remitted."
    assert paragraphs[-1].text.startswith("Solicitor for")


def test_build_case_chunks_creates_only_intro_and_paragraph_chunks():
    case = SimpleNamespace(
        id=20,
        full_text="Header line\nOVERVIEW\n[1] First paragraph.\n[2] Second paragraph.\nCONCLUSION\nDone.",
        summary=None,
    )

    rows = build_case_chunks(case)

    assert [row.chunk_set for row in rows] == ["paragraph", "paragraph", "paragraph"]
    assert [row.chunk_label for row in rows] == ["intro", "1", "2"]
    assert rows[1].paragraph_start == 1
    assert rows[2].paragraph_end == 2


def test_build_case_chunks_paragraph_pass_has_intro_numbered_and_tail_chunks():
    case = SimpleNamespace(
        id=21,
        full_text=(
            "Header material before numbered reasons\n"
            "[1] First decision paragraph.\n"
            "[2] Second decision paragraph.\n"
            "APPEARANCES:\n"
            "Counsel names in footer."
        ),
        summary=None,
    )

    rows = build_case_chunks(case)

    assert [row.chunk_label for row in rows] == ["intro", "1", "2", "tail"]
    assert rows[0].text == "Header material before numbered reasons"
    assert rows[1].paragraph_start == 1
    assert rows[2].paragraph_end == 2
    assert rows[3].text.startswith("APPEARANCES:")


def test_build_case_chunks_does_not_treat_reporter_year_as_paragraph_marker():
    case = SimpleNamespace(
        id=22,
        full_text=(
            "Header material\n"
            "[1] The governing authority is Thomson v. Thomson, [1994] 3 S.C.R. 551.\n"
            "[2] The analysis follows that authority."
        ),
        summary=None,
    )

    rows = build_case_chunks(case)

    assert [row.chunk_label for row in rows] == ["intro", "1", "2"]
    assert rows[1].text == "[1] The governing authority is Thomson v. Thomson, [1994] 3 S.C.R. 551."


def test_chunk_pending_cases_commits_each_case_batch():
    cases = [
        SimpleNamespace(id=4, full_text="case four", summary=None),
        SimpleNamespace(id=9, full_text="case nine", summary=None),
    ]
    db = FakeSession([cases, []])

    cases_chunked, chunks_created = chunk_pending_cases(db, batch_size=2)

    assert cases_chunked == 2
    assert chunks_created == 6
    assert [row.case_id for row in db.added] == [4, 4, 4, 9, 9, 9]
    assert db.commits == 1