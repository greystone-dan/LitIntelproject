from backend.citation_pipeline import build_default_pipeline


def test_v2_pipeline_extracts_core_statute_and_instrument_patterns():
    pipeline = build_default_pipeline()
    text = (
        "Under IRPA ss. 100 to 102, 101(1)(f), and 101(2)(b), the claim is ineligible. "
        "Article 1F(b) and Article 33(2) apply."
    )

    matches = pipeline.extract(text)
    normalized = [m.normalized_citation for m in matches]

    assert any(item.startswith("Immigration and Refugee Protection Act, S.C. 2001, c. 27 ss. 100 to 102") for item in normalized)
    assert "art. 1F(b) of Refugee Convention" in normalized
    assert "art. 33(2) of Refugee Convention" in normalized


def test_v2_pipeline_extracts_reporter_and_short_authority_patterns():
    pipeline = build_default_pipeline()
    text = "[2013] 2 S.C.R. 678, at paras. 38 and 101, and Pushpanathan, at para. 57."

    matches = pipeline.extract(text)
    normalized = [m.normalized_citation for m in matches]

    assert "[2013] 2 S.C.R. 678, at paras. 38 and 101" in normalized
    assert "Pushpanathan, at para. 57" in normalized
