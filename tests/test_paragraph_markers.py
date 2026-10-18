from backend.case_formatter import format_decision
from backend.contextual_authority.case_structure import split_decision_text
from backend.paragraph_markers import find_marker


def _paras(text):
    return [(b["num"], text[b["start"] : b["end"]]) for b in format_decision(text) if b["type"] == "para"]


def test_heading_glued_marker_with_text():
    found = find_marker("Issue [19] The applicant argues", 18)
    assert found is not None and found.num == 19
    assert "Issue [19] The applicant argues"[: found.head_end] == "Issue"


def test_heading_glued_marker_variants():
    assert find_marker("(i) Textual Analysis [45] Text here", 44).num == 45
    assert find_marker("Internal Flight Alternative [IFA] [22] The RAD", 21).num == 22
    assert find_marker("Is the decision reasonable? [29] Other", 28).num == 29


def test_marker_alone_and_without_space():
    assert find_marker("[14]", 13).num == 14
    assert find_marker("[97]Dr. Grover suggests", 96).num == 97


def test_cross_references_are_not_markers():
    assert find_marker("see paragraph [5] of Dunsmuir", 4) is None
    assert find_marker("The Court said so in Smith [5] at length", 20) is None  # not the next number
    assert find_marker("Canada v Vavilov, [2019] 4 SCR 653", 0) is None  # bracketed year
    assert find_marker("Applicants relied on para [6] but", 5) is None  # cross-reference word
    assert find_marker("[5] normal paragraph", 4) is None  # handled by the usual pattern


def test_near_jump_accepted_far_jump_rejected():
    assert find_marker("Analysis [8] Text", 5).num == 8
    assert find_marker("Analysis [9] Text", 5) is None


def test_mistyped_number_does_not_stall_the_walk():
    assert find_marker("Issues [31] Text", 23, 30).num == 31


def test_format_decision_finds_glued_paragraphs():
    text = "Decision Content\n[1] First.\nIssue [2] The issue is this.\nBackground\n[3]\nThe facts.\n[4]No space.\n"
    assert [n for n, _ in _paras(text)] == [1, 2, 3, 4]
    heading = [text[b["start"] : b["end"]] for b in format_decision(text) if b["type"] == "heading"]
    assert "Issue" in heading


def test_format_decision_unchanged_for_plain_decision():
    text = "Decision Content\n[1] First.\n[2] Second.\nSee [5] elsewhere.\n[3] Third.\n"
    assert [n for n, _ in _paras(text)] == [1, 2, 3]


def test_split_decision_text_cuts_heading_off_marker_line():
    text = "Decision Content\n[1] First paragraph.\nAnalysis [2] Second paragraph.\n[3] Third.\n"
    paragraphs = split_decision_text(text)
    assert paragraphs[-4:] == ["[1] First paragraph.", "Analysis", "[2] Second paragraph.", "[3] Third."]
