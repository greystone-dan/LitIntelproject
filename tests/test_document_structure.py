import backend.document_structure as document_structure
from backend.document_structure import DocumentBlock, StructuredDocument, map_to_canonical_text, structure_source_html


def test_structure_source_html_preserves_blocks_and_offsets():
    source = '<article><h1>Reasons</h1><p>[1] First paragraph.</p><p>Second <strong>paragraph</strong>.</p></article>'

    document = structure_source_html(source)

    assert document.parser_version == "html-structure-v1"
    assert document.plain_text == "Reasons\n\n[1] First paragraph.\n\nSecond paragraph."
    assert [block.kind for block in document.blocks] == ["heading", "paragraph", "paragraph"]
    assert document.plain_text[document.blocks[1].plain_text_start:document.blocks[1].plain_text_end] == "[1] First paragraph."
    assert document.blocks[0].heading_level == 1
    assert document.blocks[2].html_tag == "p"


def test_structure_source_html_sanitizes_display_copy_without_changing_input():
    source = '<p>Visible</p><script>alert("bad")</script><p onclick="bad()">Safe</p>'

    document = structure_source_html(source)

    assert document.plain_text == "Visible\n\nSafe"
    assert "script" not in document.sanitized_html
    assert "onclick" not in document.sanitized_html
    assert source == '<p>Visible</p><script>alert("bad")</script><p onclick="bad()">Safe</p>'


def test_structure_source_html_uses_fallback_text_when_html_is_missing():
    document = structure_source_html(None, "Plain text fallback")

    assert document.plain_text == "Plain text fallback"
    assert document.blocks[0].html_tag == "text"
    assert document.blocks[0].plain_text_end == len("Plain text fallback")


def test_map_to_canonical_text_handles_html_metadata_shift():
    document = structure_source_html("<article><h1>Reasons</h1><p>[1] First.</p></article>")

    mapped = map_to_canonical_text(document, "Title\nDate: 2026\nReasons\n[1] First.")

    assert mapped.canonical_text == "Title\nDate: 2026\nReasons\n[1] First."
    assert mapped.blocks[0].canonical_text_start == 17
    assert mapped.blocks[0].canonical_text_end == 24
    assert mapped.blocks[0].mapping_confidence == 1.0
    assert mapped.blocks[1].canonical_text_start == 25


def test_large_document_mapping_uses_bounded_block_lookup(monkeypatch):
    block_text = "[1] A mapped paragraph."
    document = StructuredDocument(
        sanitized_html="<p>mapped</p>",
        plain_text=block_text,
        blocks=(DocumentBlock(0, "paragraph", block_text, 0, len(block_text), "p", "/p[1]"),),
    )

    def fail_sequence_matcher(*args, **kwargs):
        raise AssertionError("global SequenceMatcher must not run for large documents")

    monkeypatch.setattr(document_structure, "SequenceMatcher", fail_sequence_matcher)
    canonical = "x" * 350_000 + block_text

    mapped = map_to_canonical_text(document, canonical)

    assert mapped.blocks[0].canonical_text_start == 350_000
    assert mapped.blocks[0].canonical_text_end == 350_000 + len(block_text)
    assert mapped.blocks[0].mapping_confidence == 1.0
