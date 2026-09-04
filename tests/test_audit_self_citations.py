from scripts.audit_self_citations import classify_self_citation


def test_classify_source_header_citation():
    result = classify_self_citation(
        "2005 FC 1037",
        "2005 FC 1037",
        "Neutral citation 2005 FC 1037 File numbers IMM-1-04",
        120,
    )

    assert result == "source_header_citation"


def test_classify_same_citation_outside_header_as_review_item():
    result = classify_self_citation(
        "2005 FC 1037",
        "2005 FC 1037",
        "The Court applied the reasoning in 2005 FC 1037 to this issue.",
        2400,
    )

    assert result == "same_citation_outside_header"


def test_classify_other_self_link():
    result = classify_self_citation(
        "Calixto",
        "2005 FC 1037",
        "The decision discussed Calixto in a later paragraph.",
        2400,
    )

    assert result == "other_self_link"
