from backend.case_formatter import format_decision
from backend.contextual_authority.case_structure import structure_outline
from backend.contextual_authority.outline_v2 import (
	citation_offset,
	outline_v2,
	section_for_offset,
	tag_citation_sections,
)

DECISION = "\n".join(
	[
		"Smith v. Canada (Citizenship and Immigration)",
		"Date: 20200101",
		"Docket: IMM-1-20",
		"BETWEEN:",
		"JOHN SMITH",
		"Applicant",
		"REASONS FOR JUDGMENT AND JUDGMENT",
		"[1] This is an application for judicial review of a decision of a visa officer refusing the applicant's work permit.",
		"[2] The applicant is a citizen of India who was born in 1980 and arrived in Canada in March 2015.",
		"I. Background",
		"[3] The applicant applied for a work permit in January 2019 and the officer refused it on February 3, 2019.",
		"[4] The officer found that the applicant had not shown he would leave Canada at the end of his stay.",
		"II. Issues",
		"[5] The application raises the following issues:",
		"1. Was the decision reasonable?",
		"III. Standard of Review",
		"[6] The standard of review is reasonableness as set out in Vavilov, 2019 SCC 65.",
		"IV. Analysis",
		"A. Credibility",
		"[7] I find that the officer's credibility finding was reasonable; the applicant's evidence was inconsistent.",
		"[8] In my view the inconsistencies in the applicant's account were material and the officer was entitled to rely on them.",
		"[9] The applicant argues that the officer ignored his explanation, but I do not agree with that submission.",
		"B. Ties to home country",
		"[10] The officer considered the applicant's ties to India and found them weak; that finding was open to the officer.",
		"[11] Moreover, the applicant's family is in Canada, which supports the officer's conclusion on dual intent.",
		"[12] I am not persuaded that the officer erred. However, the reasons could have been clearer.",
		"V. Conclusion",
		"[13] The application for judicial review is dismissed. No question is certified.",
		"JUDGMENT",
		"THIS COURT'S JUDGMENT is that the application is dismissed.",
		"SOLICITORS OF RECORD",
		"DOCKET: IMM-1-20",
	]
)


def _outline():
	return outline_v2(DECISION, format_decision(DECISION, {}))


def test_four_sections_in_order_with_sub_points():
	rows = _outline()
	sections = [r["section"] for r in rows if r["kind"] == "section"]
	assert sections == ["background", "issues", "analysis", "disposition"]
	titles = [r["title"] for r in rows if r["kind"] == "point" and r["section"] == "analysis"]
	assert "Credibility" in titles and "Ties to home country" in titles


def test_rows_keep_the_reader_fields_and_ranges():
	for row in _outline():
		assert {"title", "role", "start", "para", "count", "level"} <= set(row)
		assert row["end"] > row["start"]


def test_footer_is_not_outlined():
	rows = _outline()
	assert max(r["end"] for r in rows) < DECISION.index("SOLICITORS OF RECORD")


def test_section_for_offset_names_section_and_point():
	rows = _outline()
	found = section_for_offset(rows, DECISION.index("ties to India"))
	assert found == {"section": "analysis", "section_title": "Analysis", "point": "Ties to home country"}
	assert section_for_offset(rows, DECISION.index("Smith v.")) is None
	assert section_for_offset(rows, DECISION.index("Vavilov"))["section"] == "issues"


def test_tag_citation_sections_for_objects_and_dicts():
	rows = _outline()
	dict_row = {"offset_start": DECISION.index("Vavilov"), "chunk_id": None}
	mapped = {"layer_spans": {"paragraph": {"absolute_start": DECISION.index("credibility finding")}}, "chunk_id": 5, "offset_start": 3}
	tag_citation_sections([dict_row, mapped], rows, citation_offset)
	assert dict_row["section_title"] == "Issues"
	assert mapped["section_title"] == "Analysis" and mapped["section_point"] == "Credibility"


def test_unmapped_chunk_citation_has_no_section():
	rows = _outline()
	row = {"chunk_id": 9, "offset_start": 4}
	tag_citation_sections([row], rows, citation_offset)
	assert row["section"] is None


def test_too_short_text_gives_no_rows():
	text = "[1] One.\n[2] Two."
	assert outline_v2(text, format_decision(text, {})) == []


def test_flag_switches_structure_outline(monkeypatch):
	blocks = format_decision(DECISION, {})
	monkeypatch.delenv("ILIT_OUTLINE_V2", raising=False)
	assert not structure_outline(DECISION, blocks)[0].get("section")
	monkeypatch.setenv("ILIT_OUTLINE_V2", "1")
	assert structure_outline(DECISION, blocks)[0]["section"] == "background"


NOTED = "\n".join(
	[
		"Doe v. Canada",
		"Date: 20200101",
		"REASONS FOR DECISION",
		"[1] The appellant appeals a decision of the Refugee Protection Division refusing his claim for protection.",
		"[2] The appellant is a citizen of Nigeria who arrived in Canada in March 2016 and claimed protection.",
		"[3] The RPD rejected the claim on credibility and the appellant says it erred in doing so.",
		"ANALYSIS",
		"[4] I find that the RPD was correct that the appellant's account of events was inconsistent.1",
		"[5] In my view the appellant's explanation for the omission was not persuasive and the finding was open to the RPD.2",
		"[6] Moreover, the RPD was entitled to draw an adverse inference. However, the point is not determinative.",
		"[7] The appeal is dismissed and the decision of the RPD is confirmed.",
		"(signed) Jane Member",
		"1 Smith v. Canada, 2015 FC 100.",
		"2 Ibid.",
	]
)


def test_citation_in_an_endnote_takes_the_section_of_its_marker():
	blocks = format_decision(NOTED, {})
	rows = outline_v2(NOTED, blocks)
	assert max(r["end"] for r in rows) <= NOTED.index("1 Smith")
	citation = {"offset_start": NOTED.index("2015 FC 100"), "chunk_id": None}
	tag_citation_sections([citation], rows, citation_offset, NOTED)
	assert citation["section"] == "analysis"
