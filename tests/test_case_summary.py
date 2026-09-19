from backend.models import (
    CaseEvidenceSummaryResponse,
    CaseDiscussionUnitSummaryResponse,
    CaseSubThemeSummaryResponse,
)
from backend.reader_service import _build_case_summary


def _summary_with_roles(roles: list[str]) -> CaseEvidenceSummaryResponse:
    return CaseEvidenceSummaryResponse(
        method="discussion_unit_v1",
        version="1.4",
        total_units=1,
        total_subthemes=1,
        note="test",
        units=[
            CaseDiscussionUnitSummaryResponse(
                discussion_unit_id="1093:1",
                unit_index=1,
                start_paragraph=0,
                end_paragraph=2,
                paragraph_count=3,
                subthemes=[
                    CaseSubThemeSummaryResponse(
                        subtheme_id="1093:1:1",
                        paragraph_indices=[0, 1],
                        key_terms=["review"],
                        display_key_terms=["review"],
                        argument_roles=roles,
                        explanation="Deterministic source explanation.",
                        evidence=[],
                    )
                ],
            )
        ],
    )


def test_case_summary_uses_stable_section_order_and_role_mapping():
    summary = _build_case_summary(_summary_with_roles(["issue", "reasoning_application"]))

    assert summary is not None
    assert [section.section_id for section in summary.sections] == [
        "issue",
        "party_positions",
        "facts",
        "governing_law",
        "reasoning",
        "limitations",
        "disposition",
    ]
    assert summary.total_available_sections == 2
    assert summary.sections[0].items[0].paragraph_indices == [0, 1]
    assert summary.sections[4].items[0].text == "Deterministic source explanation."


def test_case_summary_marks_missing_roles_explicitly():
    summary = _build_case_summary(_summary_with_roles([]))

    assert summary is not None
    assert summary.total_available_sections == 0
    assert summary.total_unavailable_sections == 7
    assert all(
        section.unavailable_reason == "Not detected in available evidence."
        for section in summary.sections
    )
