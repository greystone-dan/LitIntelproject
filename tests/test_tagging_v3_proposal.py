import json
from pathlib import Path

from backend.legal_tagger_v3 import CoreLegalTaggerV3, TAXONOMY_VERSION
from scripts.tag_cases_v3 import build_case_tag_rows


PROPOSAL_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "eval"
    / "reports"
    / "tagging-v3-core-whitelist-proposal.json"
)


def load_proposal() -> dict:
    return json.loads(PROPOSAL_PATH.read_text(encoding="utf-8"))


def all_aliases(proposal: dict) -> set[str]:
    return {
        alias
        for category in proposal["categories"].values()
        for aliases in category.values()
        for alias in aliases
    }


def test_v3_proposal_is_inactive_and_versioned():
    proposal = load_proposal()

    assert proposal["taxonomy_version"] == "ca_legal_v3_core"
    assert proposal["review_status"] == "proposed"
    assert "required_evidence_for_alias" in proposal["alias_policy"]


def test_agency_core_signals_have_whitelist_aliases():
    proposal = load_proposal()
    aliases = all_aliases(proposal)

    for facet in proposal["agency_research_facets"].values():
        assert set(facet["core_signals"]).issubset(aliases)


def test_contextual_terms_are_not_core_signals():
    proposal = load_proposal()
    aliases = all_aliases(proposal)
    contextual_terms = set(proposal["contextual_only_until_review"])

    assert contextual_terms.isdisjoint(aliases)
    assert contextual_terms.isdisjoint(
        {
            signal
            for facet in proposal["agency_research_facets"].values()
            for signal in facet["core_signals"]
        }
    )


def test_reviewed_alias_variants_are_present():
    aliases = all_aliases(load_proposal())

    assert {"H&C", "H & C", "H and C"}.issubset(aliases)
    assert {"security screening", "security-screening"}.issubset(aliases)
    assert {"PGWP", "Post-Graduation Work Permit", "Post Graduation Work Permit"}.issubset(aliases)
    assert "Pre Removal Risk Assessment" in aliases


def test_known_generic_terms_remain_excluded():
    proposal = load_proposal()
    aliases = all_aliases(proposal)

    for term in ("Canada", "application", "decision", "removal", "detention", "hearing"):
        assert term not in aliases
        assert term in proposal["excluded_from_core"] or term in proposal["contextual_only_until_review"]


def test_v3_tagger_matches_explicit_agency_and_process_aliases():
    tags = CoreLegalTaggerV3().tag(
        "IRCC reviewed the GCMS notes after a PFL. CBSA filed a section 44 report."
    )
    values = {(tag.category, tag.value) for tag in tags}

    assert ("agency", "ircc") in values
    assert ("procedure_or_record", "gcms") in values
    assert ("procedure_or_record", "procedural_fairness_letter") in values
    assert ("agency", "cbsa") in values
    assert ("procedure_or_record", "section_44_report") in values
    assert all(tag.taxonomy_version == TAXONOMY_VERSION for tag in tags)


def test_v3_tagger_preserves_exact_occurrence_offsets():
    text = "The applicant requested an H & C review and an Express Entry record."
    occurrences = CoreLegalTaggerV3().tag_occurrences(text)

    assert all(text[item.offset_start:item.offset_end] == item.evidence for item in occurrences)
    assert {item.value for item in occurrences} == {
        "humanitarian_and_compassionate",
        "express_entry",
    }


def test_v3_tagger_does_not_infer_contextual_terms_or_findings():
    tags = CoreLegalTaggerV3().tag(
        "The application decision discussed detention, removal, and credibility."
    )

    assert not tags


def test_v3_pipeline_preserves_repeated_occurrences_and_evidence_metadata():
    rows = build_case_tag_rows("IRCC contacted IRCC about GCMS notes.")
    ircc_rows = [row for row in rows if row["value"] == "ircc"]

    assert len(ircc_rows) == 2
    assert ircc_rows[0]["offset_start"] != ircc_rows[1]["offset_start"]
    for row in rows:
        assert row["rule_id"] == f"{row['category']}.{row['value']}"
        assert row["language"] == "unknown"
        assert row["evidence_role"] == "mention"
        assert row["taxonomy_version"] == TAXONOMY_VERSION
        assert row["source"] == "core_whitelist"