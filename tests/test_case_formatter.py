from backend.case_formatter import format_decision

FC = "\n".join([
    "Doe v. Canada", "Court (s) Database", "Federal Court Decisions", "Decision Content",
    "Date: 20230515", "Docket: IMM-1-22", "Ottawa, Ontario, May 15, 2023", "PRESENT: Mr. Justice X",
    "BETWEEN:", "JANE DOE", "Applicant", "and", "THE MINISTER", "Respondent", "JUDGMENT AND REASONS",
    "I. Overview [1] The applicant seeks review.", "[2] She is a citizen.", "II. Analysis",
    "A. Standard of review", "[3] Reasonableness applies.", "(a) first limb", "“" + "x" * 210,
    "FEDERAL COURT", "SOLICITORS OF RECORD", "DOCKET:", "IMM-1-22", "SOLICITORS OF RECORD:", "Counsel", "For The Applicant",
])
SCC_MODERN = "\n".join([
    "Case", "Collection", "Decision Content", "Reasons for Judgment:", "2006: December 11; 2007: October 19.",
    "1 First paragraph.", "II. Facts", "2 Second paragraph.", "96 A statute line.", "Appeal allowed.",
    "Solicitors for the appellant: A.",
])
SCC_OLD = "\n".join([
    "Case", "Decision Content", "Held: appeal allowed.", "Some reasoning.", "Appeal allowed with costs.",
    "Solicitors for the appellant: A.", "[1] (1887), 56 L.J.Q.B. 621.", "[2] [1910] A.C. 614.",
])


def _kinds(text):
    return [(b["type"], text[b["start"]:b["end"]]) for b in format_decision(text)]


def test_blocks_are_ordered_in_range_and_never_alter_text():
    for text in (FC, SCC_MODERN, SCC_OLD):
        blocks = format_decision(text)
        assert all(0 <= b["start"] < b["end"] <= len(text) for b in blocks)
        assert all(a["end"] <= b["start"] for a, b in zip(blocks, blocks[1:]))


def test_fc_header_headings_paragraphs_and_footer():
    kinds = _kinds(FC)
    assert kinds[0][0] == "meta" and kinds[0][1].endswith("Decision Content")
    assert ("role", "Applicant") in kinds and ("doctitle", "JUDGMENT AND REASONS") in kinds
    assert ("heading", "I. Overview") in kinds
    para = next(b for b in format_decision(FC) if b["type"] == "para" and b["num"] == 1)
    assert FC[para["start"]:para["end"]].startswith("[1] The applicant") and FC[para["start"]:para["mark_end"]] == "[1]"
    assert ("heading", "A. Standard of review") in kinds
    assert [k for k, _ in kinds if k == "listitem"] and [k for k, _ in kinds if k == "quote"]
    footer = [t for k, t in kinds if k == "footer"]
    assert footer[0] == "FEDERAL COURT" and footer[-1] == "For The Applicant"


def test_modern_scc_bare_numbering_follows_sequence_only():
    nums = [b["num"] for b in format_decision(SCC_MODERN) if b["type"] == "para"]
    assert nums == [1, 2]
    assert ("text", "96 A statute line.") in _kinds(SCC_MODERN)


def test_old_scc_bracket_notes_after_counsel_are_footnotes_not_paragraphs():
    kinds = [k for k, _ in _kinds(SCC_OLD)]
    assert "para" not in kinds and kinds.count("footnote") == 2 and "footer" in kinds


def test_empty_text():
    assert format_decision(None) == [] and format_decision("") == []


FCA = "\n".join([
    "Doe v. Canada", "Decision Content", "Date: 20230101", "Docket: A-1-23", "CORAM:", "WEBB J.A.", "BETWEEN:",
    "JOHN DOE", "Appellant", "and", "HIS MAJESTY", "Respondent", "REASONS FOR JUDGMENT",
    "WEBB J.A.", "[1] First paragraph.", "“" + "q" * 90, "[…]", "[Emphasis added.]", "Analysis", "[2] Second.",
    "“I agree.", "“Jane Roe”", "Judge", "FEDERAL COURT OF APPEAL", "NAMES OF COUNSEL AND SOLICITORS OF RECORD", "DOCKET: A-1-23",
])


def test_fca_signature_quote_filler_and_plain_headings():
    kinds = _kinds(FCA)
    assert ("courtline", "WEBB J.A.") in kinds
    assert ("quote", "[…]") in kinds and ("quote", "[Emphasis added.]") in kinds
    assert ("heading", "Analysis") in kinds
    assert ("signature", "“Jane Roe”") in kinds and ("signature", "Judge") in kinds
    assert kinds[-1][0] == "footer"


def test_short_citation_shaped_bracket_lines_are_footnotes_even_without_counsel_footer():
    text = "\n".join(["Case", "Decision Content", "Reasoning here.", "[1] (1887), 56 L.J.Q.B. 621.", "[2] [1910] A.C. 614."])
    assert [k for k, _ in _kinds(text)].count("footnote") == 2
