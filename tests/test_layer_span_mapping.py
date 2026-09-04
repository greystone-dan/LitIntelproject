from types import SimpleNamespace

import pytest

from backend.document_structure import map_span_to_chunk_layers


def test_map_span_to_full_section_and_paragraph_layers():
    case_text = "Title\n[1] First paragraph.\n[2] Second paragraph."
    citation_start = case_text.index("First")
    citation_end = citation_start + len("First")
    chunks = [
        SimpleNamespace(id=1, chunk_set="full_case", chunk_index=0, text=case_text),
        SimpleNamespace(id=2, chunk_set="section", chunk_index=0, text=case_text),
        SimpleNamespace(id=3, chunk_set="paragraph", chunk_index=0, text="[1] First paragraph."),
        SimpleNamespace(id=4, chunk_set="paragraph", chunk_index=1, text="[2] Second paragraph."),
    ]

    spans = map_span_to_chunk_layers(case_text, citation_start, citation_end, chunks)

    assert set(spans) == {"full_case", "section", "paragraph"}
    assert spans["full_case"].local_start == citation_start
    assert spans["section"].local_start == citation_start
    assert spans["paragraph"].local_start == len("[1] ")
    assert spans["paragraph"].local_end == len("[1] First")
    assert spans["paragraph"].chunk_id == 3


def test_map_span_rejects_invalid_case_range():
    with pytest.raises(ValueError, match="positive range"):
        map_span_to_chunk_layers("short", -1, 2, [])
