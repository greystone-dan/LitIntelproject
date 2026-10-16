from backend.case_formatter import format_decision
from backend.contextual_authority.heading_reader import heading_label, read_headings, resolved_labels
from backend.contextual_authority.outline_v2 import outline_v2


def _para(n: int, text: str = "The officer considered the evidence and the applicant's explanation in some detail here.") -> str:
	return f"[{n}] {text}"


def _decision(lines: list[str]) -> str:
	return "\n".join(["Smith v. Canada", "Date: 20200101", "REASONS FOR JUDGMENT AND JUDGMENT", *lines, "JUDGMENT", "THIS COURT'S JUDGMENT is that the application is dismissed.", "SOLICITORS OF RECORD"])


def test_labels_group_spellings_into_standard_names():
	assert heading_label("Factual background") == "background"
	assert heading_label("Issues and Standard of Review") == "issues_standard"
	assert heading_label("Impugned decision") == "decision_under_review"
	assert heading_label("Respondent's Submissions") == "submissions"
	assert heading_label("Conclusion and Disposition") == "conclusion"
	assert heading_label("Was the decision reasonable?") == "question"
	assert heading_label("Credibility") == "topic"


def test_reads_numbered_unnumbered_and_glued_headings():
	text = _decision(
		[
			_para(1),
			"II. Background",
			_para(2),
			"ANALYSIS",
			_para(3),
			"A. Was the decision reasonable?",
			_para(4),
			"V. Conclusion [5] The application is dismissed.",
		]
	)
	found = read_headings(text)
	assert [(h.kind, h.label) for h in found] == [("roman", "background"), ("plain", "analysis"), ("letter", "question"), ("roman", "conclusion")]
	assert found[-1].glued and not found[0].glued


def test_two_headings_run_together_on_one_line():
	text = _decision([_para(1), "IV. Analysis A. What is the standard of review? [2] The standard is reasonableness.", _para(3)])
	assert [h.title for h in read_headings(text)] == ["Analysis", "What is the standard of review?"]


def test_numbered_issue_list_lines_are_not_headings():
	text = _decision(
		[
			_para(1),
			"[2] There are two issues:",
			"1. What is the applicable standard of review?",
			"2. Did the officer err in assessing the evidence?",
			_para(3),
		]
	)
	assert read_headings(text) == []


def test_quoted_statute_notes_and_transcripts_are_not_headings():
	text = _decision(
		[
			_para(1),
			"[2] The Act provides:",
			"Convention refugee",
			"96. A Convention refugee is a person who, by reason of a well-founded fear of persecution, is outside their country.",
			_para(3),
			"Q. Did you leave the country in 2010?",
			"A. Yes.",
			_para(4),
		]
	)
	assert read_headings(text) == []


def test_bare_decision_heading_resolves_by_position():
	text = _decision([_para(1), "III. Decision", _para(2), "IV. Analysis", _para(3), "V. Decision", _para(4)])
	assert resolved_labels(read_headings(text)) == ["decision_under_review", "analysis", "conclusion"]


def _long_decision() -> str:
	lines = [_para(1), "BACKGROUND"]
	lines += [_para(n) for n in range(2, 5)]
	lines += ["ISSUES", _para(5), "APPLICANT'S SUBMISSIONS"]
	lines += [_para(n, "The applicant argues that the officer erred in several ways and asks the Court to intervene.") for n in range(6, 8)]
	lines += ["RESPONDENT'S SUBMISSIONS"]
	lines += [_para(n, "The respondent argues that the decision was reasonable and that the application should fail.") for n in range(8, 10)]
	lines += ["ANALYSIS"]
	lines += [_para(n, "I find that the officer's reasoning was transparent, intelligible and justified on this record.") for n in range(10, 15)]
	lines += ["CONCLUSION", _para(15, "The application for judicial review is dismissed. No question is certified.")]
	return _decision(lines)


def test_outline_starts_analysis_at_the_printed_heading(monkeypatch):
	text = _long_decision()
	monkeypatch.setenv("ILIT_OUTLINE_HEADINGS", "1")
	rows = outline_v2(text, format_decision(text, {}))
	sections = {r["section"]: r for r in rows if r["kind"] == "section"}
	assert sections["analysis"]["para"] == 10
	assert sections["disposition"]["para"] == 15
	assert sections["analysis"]["printed"] is True
	assert sections["disposition"]["printed"] is True


def test_headings_off_leaves_rows_without_the_printed_flag(monkeypatch):
	text = _long_decision()
	monkeypatch.delenv("ILIT_OUTLINE_HEADINGS", raising=False)
	rows = outline_v2(text, format_decision(text, {}))
	assert rows and all("printed" not in r for r in rows)


def test_short_decision_without_headings_keeps_only_the_disposition(monkeypatch):
	text = _decision([_para(n, "I find that the officer was reasonable and that the evidence supports the decision made.") for n in range(1, 8)] + [_para(8, "The application for judicial review is dismissed.")])
	monkeypatch.setenv("ILIT_OUTLINE_HEADINGS", "1")
	rows = outline_v2(text, format_decision(text, {}))
	assert all(r["section"] == "disposition" for r in rows)


def test_report_citation_line_is_not_a_paragraph_number():
	text = "\n".join(
		["Yugraneft Corp. v. Rexx", "[2010] 1 SCR 649", "Docket: 32738", "The judgment of the Court was delivered by", "Rothstein J. —", "I. Introduction", _para(1), "II. Facts", _para(2), "III. Analysis", _para(3), "Appeal dismissed.", "Solicitors for the appellant: Smith."]
	)
	assert [h.title for h in read_headings(text)] == ["Introduction", "Facts", "Analysis"]


def test_court_of_appeal_decision_of_ten_paragraphs_keeps_its_outline(monkeypatch):
	monkeypatch.setenv("ILIT_OUTLINE_HEADINGS", "1")
	body = [_para(n, "I find that the judge made no error and that the evidence supports the decision made below.") for n in range(1, 10)] + [_para(10, "The appeal is dismissed with costs.")]
	fc = _decision(body)
	fca = fc.replace("Smith v. Canada", "Smith v. Canada\nFederal Court of Appeal Decisions\nCitation: 2020 FCA 5", 1)
	assert all(r["section"] == "disposition" for r in outline_v2(fc, format_decision(fc, {})))
	assert any(r["section"] != "disposition" for r in outline_v2(fca, format_decision(fca, {})))
