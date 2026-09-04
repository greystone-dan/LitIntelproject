from pathlib import Path
from types import SimpleNamespace

from backend.document_structure import map_to_canonical_text, structure_source_html
from scripts.chunk_cases import build_case_chunk_layers


SNAPSHOT = Path("data/eval/scc_2002_scc_1_snapshot.html")


def test_scc_structure_starts_at_numbered_decision_blocks():
    source = SNAPSHOT.read_text(encoding="utf-8")
    document = structure_source_html(source, source_family="scc")

    assert document.blocks
    assert document.blocks[0].text.startswith("1 The Court")
    assert all(block.html_tag == "p" for block in document.blocks)
    assert any(block.text.startswith("II. Relevant Constitutional") for block in document.blocks)


def test_scc_chunk_builder_preserves_paragraph_blocks():
    source = SNAPSHOT.read_text(encoding="utf-8")
    source_document = structure_source_html(source, source_family="scc")
    case = SimpleNamespace(
        id=35860,
        court="SCC",
        source_html=source,
        full_text=source_document.plain_text,
        summary=None,
    )

    document = map_to_canonical_text(source_document, case.full_text)
    rows = build_case_chunk_layers(case)

    assert document.mapping_confidence > 0.98
    assert sum(row.chunk_set == "full_case" for row in rows) == 1
    assert sum(row.chunk_set == "paragraph" for row in rows) > 150
    assert all(row.text in case.full_text for row in rows)
