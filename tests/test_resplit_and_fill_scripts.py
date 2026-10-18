from types import SimpleNamespace

from scripts.fill_fca_headline_outcomes import classify, summarise
from scripts.resplit_paragraph_chunks import carry_over_embeddings, locate_rows, row_for_paragraph, row_for_position, row_signature


def _row(label, start, end, text, text_hash="h"):
    return SimpleNamespace(id=None, chunk_label=label, paragraph_start=start, paragraph_end=end, text=text, text_hash=text_hash)


def test_locate_rows_and_position_lookup_follow_the_text():
    text = "intro\n[1] first\n[2] second"
    rows = [_row("intro", None, None, "intro"), _row("1", 1, 1, "[1] first"), _row("2", 2, 2, "[2] second")]
    located = locate_rows(text, rows)

    row, start = row_for_position(located, text.index("second"))

    assert row.chunk_label == "2"
    assert start == text.index("[2]")
    assert row_for_position(located, len(text) + 5) == (None, 0)


def test_row_for_paragraph_needs_exactly_one_match():
    rows = [_row("1", 1, 1, "a"), _row("2", 2, 3, "b"), _row("3", 3, 3, "c")]

    assert row_for_paragraph(rows, 1).chunk_label == "1"
    assert row_for_paragraph(rows, 2).chunk_label == "2"
    assert row_for_paragraph(rows, 3) is None
    assert row_for_paragraph(rows, None) is None


def test_row_signature_detects_identical_splits():
    a = [_row("1", 1, 1, "x", "h1")]
    assert row_signature(a) == row_signature([_row("1", 1, 1, "x", "h1")])
    assert row_signature(a) != row_signature([_row("1", 1, 1, "x", "h2")])


def test_fca_fill_only_touches_blank_headlines_with_clear_v2_results():
    assert classify("", "allowed") == "fill"
    assert classify(None, "mixed") == "fill"
    assert classify(None, "dismissed") == "fill"
    assert classify(None, "unclear") == "left_blank"
    assert classify(None, "procedural") == "left_blank"
    assert classify(None, None) == "left_blank"
    assert classify("dismissed", "allowed") == "kept_existing"


def test_fca_fill_summary_counts_before_and_after():
    rows = [(1, None, "allowed"), (2, "", "unclear"), (3, "dismissed", "allowed"), (4, None, "dismissed")]

    summary = summarise(rows)

    assert summary["blank_before"] == 3
    assert summary["blank_after"] == 1
    assert summary["fill"] == 2
    assert summary["kept_existing"] == 1
    assert summary["filled_by_value"] == {"allowed": 1, "dismissed": 1}


def _embedded(label, text, text_hash, embedding):
    row = _row(label, None, None, text, text_hash)
    row.embedding = embedding
    row.embedding_model = "m" if embedding is not None else None
    return row


def test_embeddings_carry_to_new_rows_with_identical_text_only():
    old = [_embedded("1", "same", "a", [0.1]), _embedded("2", "old split", "b", [0.2]), _embedded("3", "plain", "c", None)]
    new = [_embedded("1", "same", "a", None), _embedded("2", "new split", "d", None)]

    carried, lost = carry_over_embeddings(old, new)

    assert (carried, lost) == (1, 1)
    assert new[0].embedding == [0.1]
    assert new[0].embedding_model == "m"
    assert new[1].embedding is None
