import hashlib

import pytest

from backend.prompt_registry import get_prompt


PROMPT_GOLDENS = {
    "research_system": "31cc7c9040b9dc825ff5f2319046e0ef28bf976fab571ea928f8798481970f9f",
    "citation_issue_focused_assessment": "dbf7137f6b07c01bafa59ff4baac474ec2e84b89228853d5ed8e41423e61144e",
    "citation_aware_assessment": "b79bb6aa9c35511d3bdb7f35037aeb3e38f537ef76dc918c95b8848457c0f52f",
    "citation_lightweight_issue_extraction": "69a256778292a3bcdc8d97b8406e85e851fbb2a2d7538fe0463e07deec1eb7e0",
    "contextual_authority_teacher": "5073a0d5ac0c4cfae224266f508002533468bfcd2d60c3831c48eb9f63226a01",
    "model_paragraph_segmentation": "483dc29d29928d862f36c4eae7624d95ca6ac8f9d8d04ba0464898f218ef0fc8",
    "discussion_units": "39ad09906d7e399297bc83e2241729b4338f0b37bcd7d3f6b348eedf6d40cd61",
    "discussion_paragraph_assessment": "2b0a5d7f0e889a9cf8a08337eb9f40a3008c1e69b1f006ff5a53dee55731abff",
}


@pytest.mark.parametrize(("name", "expected_sha256"), PROMPT_GOLDENS.items())
def test_prompt_text_matches_exact_baseline_snapshot(name, expected_sha256):
    text, version = get_prompt(name)

    assert hashlib.sha256(text.encode("utf-8")).hexdigest() == expected_sha256
    assert version == "v1"


def test_dynamic_citation_prompt_matches_exact_baseline_snapshot():
    from backend.citation_intelligence_prompts import build_unit_context_assessment_request

    request = build_unit_context_assessment_request(
        1,
        "UNIT",
        case_metadata={
            "case_name": "NAME",
            "court": "COURT",
            "year": 2025,
            "tags": ["TAG"],
            "statute_refs": ["STATUTE"],
            "cited_authorities": ["AUTHORITY"],
        },
        preceding_unit="PRECEDING",
        following_unit="FOLLOWING",
    )

    assert hashlib.sha256(request["messages"][0]["content"].encode("utf-8")).hexdigest() == (
        "f0a30b3ebebee0c47ef7f8422df861a066ad72aaa56fda8b4c9398d33593fd18"
    )
    assert request["prompt_version"] == "v1"


def test_prompt_registry_rejects_path_like_names():
    with pytest.raises(ValueError, match="invalid prompt name"):
        get_prompt("../research_system")
