from types import SimpleNamespace

from scripts.inspect_discussion_units import _heading_match, _is_heading, _render_markdown


def test_heading_detection_reads_section_cues_inside_paragraph_text():
    assert _is_heading(SimpleNamespace(chunk_label="11", text="[11] The finding is set out. III. Issue"))
    assert _is_heading(SimpleNamespace(chunk_label="34", text="[34] Accordingly, the application is dismissed. JUDGMENT"))
    assert _heading_match("The order was dismissed") is None


def test_embedded_heading_match_preserves_source_offset():
    text = "The application is dismissed. II. Background"
    match = _heading_match(text)

    assert match is not None
    assert text[match.start():match.end()] == "II. Background"


def test_discussion_unit_markdown_is_reviewable_without_database():
    report = {
        "case_id": 7,
        "paragraph_count": 2,
        "continuity_count": 1,
        "discussion_unit_count": 1,
        "discussion_units": [
            {
                "discussion_unit_id": "7:1",
                "start_paragraph": 1,
                "end_paragraph": 2,
                "citation_counts": {"1": 2},
                "statute_counts": {},
                "tag_counts": {"issue:reasonableness": 2},
                "text_sha256": "a" * 64,
                "text": "The court applies the authority.\n\nThe court explains the rule.",
            }
        ],
    }

    markdown = _render_markdown(report)

    assert "Read-only inspection" in markdown
    assert "paragraphs 1-2" in markdown
    assert "The court applies the authority." in markdown
    assert "Source hash" in markdown


def test_markdown_renders_subthemes_and_argument_context():
    report = {
        "case_id": 7,
        "paragraph_count": 1,
        "continuity_count": 0,
        "discussion_unit_count": 1,
        "paragraphs": [{"text_sha256": "a" * 64}],
        "discussion_units": [
            {
                "discussion_unit_id": "7:1",
                "start_paragraph": 0,
                "end_paragraph": 0,
                "citation_counts": {},
                "statute_counts": {},
                "tag_counts": {},
                "text_sha256": "b" * 64,
                "text": "The applicants argue that the decision was unreasonable.",
                "subthemes": [
                    {
                        "subtheme_id": "7:1:subtheme:1",
                        "paragraph_indices": [0],
                        "key_terms": ["decision", "unreasonable"],
                        "display_key_terms": ["unreasonable"],
                        "argument_roles": ["party_position"],
                        "explanation": "Observed moves: party_position.",
                        "argument_evidence": [
                            {
                                "role": "party_position",
                                "text": "argue",
                                "chunk_id": 100,
                                "start_offset": 16,
                                "end_offset": 21,
                                "context_text": "The applicants argue that the decision was unreasonable.",
                            }
                        ],
                    }
                ],
            }
        ],
    }

    markdown = _render_markdown(report)

    assert "Sub-themes" in markdown
    assert "Raw key terms: `decision, unreasonable`" in markdown
    assert "Display key terms: `unreasonable`" in markdown
    assert "party_position" in markdown
    assert "The applicants argue" in markdown
    assert "Observed moves: party_position." in markdown


def test_markdown_bounds_large_section_text_without_losing_the_artifact():
    report = {
        "case_id": 7,
        "paragraph_count": 1,
        "continuity_count": 0,
        "discussion_unit_count": 1,
        "paragraphs": [],
        "discussion_units": [
            {
                "discussion_unit_id": "7:1",
                "start_paragraph": 0,
                "end_paragraph": 0,
                "citation_counts": {},
                "statute_counts": {},
                "tag_counts": {},
                "text_sha256": "b" * 64,
                "text": "x" * 100,
            }
        ],
    }

    markdown = _render_markdown(report, max_unit_text_chars=20)

    assert "Section text truncated at 20 characters" in markdown