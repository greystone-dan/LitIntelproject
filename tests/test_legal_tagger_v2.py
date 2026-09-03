from backend.legal_tagger_v2 import CoreLegalTagger, TAXONOMY_VERSION


def test_core_tagger_matches_whitelist_aliases_and_canonical_values():
    tags = CoreLegalTagger().tag(
        "The CBSA referred the PRRA to the RAD. The claimant was from Nigeria and mentioned IPOB."
    )
    values = {(tag.category, tag.value) for tag in tags}

    assert ("agency", "cbsa") in values
    assert ("immigration_term", "prra") in values
    assert ("tribunal", "rad") in values
    assert ("country", "nigeria") in values
    assert ("organization", "ipob") in values
    assert all(tag.taxonomy_version == TAXONOMY_VERSION for tag in tags)
    assert all(tag.source == "core_whitelist" for tag in tags)


def test_core_tagger_does_not_match_partial_words():
    tags = CoreLegalTagger().tag("The applicant was irreplaceable and visited Nigerian restaurant staff.")

    assert not tags


def test_core_tagger_keeps_exact_evidence():
    text = "IRCC considered H&C and the Immigration and Refugee Protection Act."
    occurrences = CoreLegalTagger().tag_occurrences(text)

    assert all(text.find(item.evidence) >= 0 for item in occurrences)
    assert {item.value for item in occurrences} == {"ircc", "h_and_c", "irpa"}
    assert all(text[item.offset_start:item.offset_end] == item.evidence for item in occurrences)