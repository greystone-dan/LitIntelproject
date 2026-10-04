from backend.citation_refine.context import DocumentContext


def test_document_context_resolves_generic_terms_from_mentioned_instruments():
    context = DocumentContext.build("IRPA applies. IRPR governs the regulations.")

    assert context.is_immigration_context is True
    assert context.resolve_term("the Act", offset=20) == ("canada.irpa", False)
    assert context.resolve_term("regulations", offset=30) == ("canada.irpr", False)


def test_document_context_tracks_previous_sentence_without_splitting_abbreviations():
    text = "See s. 3 of IRPA. A second sentence follows. The regulations apply."
    context = DocumentContext.build(text)

    second_start = text.index("A second")
    third_start = text.index("The regulations")

    assert context.sentence_start(second_start + 3) == second_start
    assert context.previous_sentence_start(third_start + 4) == second_start
