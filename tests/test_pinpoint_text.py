from backend.reader_service import _starts_with_paragraph, paragraph_text_from_decision

DECISION = (
    "Some header\\n"
    "REASONS FOR JUDGMENT\\n"
    "[1] First paragraph text here.\\n"
    "[2] Second paragraph text.\\n"
    "[3] Third paragraph.\\n"
).replace("\\n", "\n")


def test_paragraph_text_comes_from_the_stored_decision():
    assert paragraph_text_from_decision(DECISION, 2) == "[2] Second paragraph text."
    assert paragraph_text_from_decision(DECISION, 3) == "[3] Third paragraph."


def test_missing_paragraph_or_text_gives_none_instead_of_invented_text():
    assert paragraph_text_from_decision(DECISION, 54) is None
    assert paragraph_text_from_decision(None, 2) is None
    assert paragraph_text_from_decision("", 2) is None


def test_chunk_must_start_with_the_pinpoint_number_to_count_as_that_paragraph():
    assert _starts_with_paragraph("[34] This has been interpreted", 34)
    assert _starts_with_paragraph("  [34] leading space", 34)
    assert not _starts_with_paragraph("SOLICITORS OF RECORD\nDOCKET: IMM-424-12", 54)
    assert not _starts_with_paragraph("[3] not thirty-four", 34)
    assert not _starts_with_paragraph(None, 34)
