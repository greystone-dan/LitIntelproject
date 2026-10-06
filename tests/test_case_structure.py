import importlib.util
from pathlib import Path

import pytest

from backend.contextual_authority import case_structure as cs

_SPEC = importlib.util.spec_from_file_location(
    "evaluate_case_structure", Path(__file__).resolve().parents[1] / "scripts" / "evaluate_case_structure.py"
)
ev = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(ev)


MODERN_FC = [
    "Doe v. Canada\nCourt (s) Database\nFederal Court Decisions",
    "Date: 20230101\nDocket: IMM-1-23\nCitation: 2023 FC 1\nOttawa, Ontario",
    "[1] This is an application for judicial review of a decision of the Refugee Appeal Division.",
    "I. Background",
    "[2] The Applicant is a citizen of Nigeria. In March 2019, he arrived in Canada and claimed refugee protection.",
    "[3] The RPD found the Applicant not credible and the RAD dismissed his appeal.",
    "II. Issues and Standard of Review",
    "[4] The issue is whether the RAD's decision was reasonable.",
    "[5] The standard of review is reasonableness (Vavilov, 2019 SCC 65).",
    "III. Analysis",
    "[6] I agree with the Applicant that the RAD erred. In my view, the finding was unreasonable.",
    "[7] I am not persuaded by the Respondent's argument. Moreover, the evidence was ignored.",
    "IV. Conclusion",
    "[8] For these reasons, the application for judicial review is allowed.",
    "JUDGMENT in IMM-1-23",
    "THIS COURT'S JUDGMENT is that the application is allowed.",
    '"Jane Roe"',
    "Judge",
    "FEDERAL COURT",
    "SOLICITORS OF RECORD",
    "DOCKET: IMM-1-23",
    "STYLE OF CAUSE: DOE v MCI",
]


def test_split_decision_text_keeps_metadata_cover_and_lines():
    text = "Case\nCourt (s) Database\nDecision Content\nDate: 2020\nBETWEEN:\nA\nand\nB\n[1] First.\n[2] Second.\nSOLICITORS OF RECORD\n"
    paragraphs = cs.split_decision_text(text)
    assert paragraphs[0].endswith("Decision Content")
    assert paragraphs[1].startswith("Date: 2020") and paragraphs[1].endswith("B")
    assert paragraphs[2:] == ["[1] First.", "[2] Second.", "SOLICITORS OF RECORD"]


@pytest.mark.parametrize(
    "text, kind",
    [
        ("I. Background", "facts"),
        ("DECISION UNDER REVIEW", "facts"),
        ("II. Issues and Standard of Review", "issues"),
        ("Relevant statutory provisions", "issues"),
        ("VI. Analysis", "analysis"),
        ("VII. Conclusion", "disposition"),
        ("JUDGMENT", "disposition"),
        ("A. Services of exceptional value to Canada", "heading"),
        ("II. Background [4] In August 2012, the Applicant came to Canada.", "facts"),
        ("[3] The Board found the applicant to be not credible.", None),
        ("The application is allowed, and the matter is sent back for redetermination.", None),
    ],
)
def test_heading_kind(text, kind):
    assert cs.heading_kind(text) == kind


def test_modern_fc_roles_follow_the_skeleton():
    roles = cs.label_paragraph_roles(MODERN_FC)
    assert roles[:2] == ["metadata", "metadata"]
    assert roles[2] == "overview"
    assert roles[3:6] == ["facts"] * 3
    assert roles[6:9] == ["issues"] * 3
    assert roles[9:12] == ["analysis"] * 3
    assert roles[12:16] == ["disposition"] * 4
    assert roles[16:] == ["metadata"] * 6


def test_structural_unit_starts_follow_role_changes():
    assert cs.structural_unit_starts(MODERN_FC) == [0, 2, 3, 6, 9, 12, 16]


def test_roles_never_go_back_to_the_header_or_out_of_the_footer():
    roles = cs.label_paragraph_roles(MODERN_FC)
    first_foot = roles.index("metadata", 2)
    assert set(roles[first_foot:]) == {"metadata"}
    assert "metadata" not in roles[2:first_foot]


def test_old_numbered_decision_without_headings():
    paragraphs = [
        "Smith v. Canada\nCourt (s) Database\nFederal Court Decisions\nDate\n2003-01-01",
        "BETWEEN: SMITH Applicant and THE MINISTER Respondent REASONS FOR ORDER",
        "[1] This is an application for judicial review of a decision of the Immigration and Refugee Board.",
        "[2] The applicant is a citizen of Albania. He arrived in Canada in 2001 and claimed refugee protection.",
        "[3] The Board found that the applicant was not credible and rejected his claim.",
        "[4] The standard of review is patent unreasonableness.",
        "[5] In my view, the Board did not err. I am not persuaded by the applicant's argument.",
        "[6] However, the Board's reasons were adequate. I agree with the respondent.",
        "[7] For all of these reasons, I dismiss this application for judicial review.",
        "SOLICITORS OF RECORD\nDOCKET: IMM-1-03\nSTYLE OF CAUSE: SMITH v MCI",
    ]
    roles = cs.label_paragraph_roles(paragraphs)
    assert roles[0] == "metadata" and roles[-1] == "metadata"
    assert roles[8] == "disposition"
    assert roles[6] == "analysis"
    assert roles[3] == "facts"


def test_empty_input():
    assert cs.label_paragraph_roles([]) == []
    assert cs.structural_unit_starts([]) == []


def test_issue_openers_split_long_analysis_only_when_asked():
    paragraphs = ["[%d] filler paragraph about the evidence. In my view it is reasonable." % i for i in range(1, 10)]
    paragraphs[5] = "[6] I turn first to the second ground, the alleged breach of fairness."
    roles = ["analysis"] * 9
    assert cs.structural_unit_starts(paragraphs, roles) == [0]
    assert cs.structural_unit_starts(paragraphs, roles, split_issue_openers=True) == [0, 5]


@pytest.fixture
def no_rpd(monkeypatch, tmp_path):
    monkeypatch.setenv("RPD_SAMPLE_CSV", str(tmp_path / "missing.csv"))


def test_gold_files_are_consistent(no_rpd):
    cases = ev.load_cases()
    assert len(cases) == 52  # 22 FC 2001-04 + 30 new FC / FCA / SCC / FC 2001-04 labelled by hand
    assert {c.split for c in cases} == {"dev", "holdout", "holdout2"}
    for case in cases:
        assert len(case.starts) == len(case.roles), case.key
        assert case.starts == sorted(case.starts) and case.starts[-1] < len(case.paragraphs), case.key
        assert set(case.roles) <= set(cs.ROLES), case.key


def test_rpd_cases_are_skipped_without_the_extract_and_when_the_text_differs(monkeypatch, tmp_path):
    monkeypatch.setenv("RPD_SAMPLE_CSV", str(tmp_path / "missing.csv"))
    assert ev.load_rpd_cases() == []
    wrong = tmp_path / "wrong.csv"
    wrong.write_text("case_id,chunk_index,text\n41876,0,not the decision\n")
    monkeypatch.setenv("RPD_SAMPLE_CSV", str(wrong))
    assert ev.load_rpd_cases() == []


def test_structure_labelling_scores_well_above_floor_on_every_split(no_rpd):
    """Regression floors, not targets (paragraph role accuracy when written: dev 85%, holdout 64%, holdout2 85%)."""
    cases = ev.load_cases()
    for split, floor in (("dev", 0.75), ("holdout", 0.6), ("holdout2", 0.75)):
        subset = [c for c in cases if c.split == split]
        boundary, (hits, total), _, _ = ev.evaluate(subset, ev.APPROACHES["structure+h"])
        assert hits / total >= floor, (split, hits, total)
        assert boundary.interior_hits / boundary.interior_gold >= 0.5, split
