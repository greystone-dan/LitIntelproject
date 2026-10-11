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


def _no_overlap(rows):
	sections = [r for r in rows if r["kind"] == "section"]
	for a, b in zip(sections, sections[1:]):
		assert a["end"] <= b["start"]
		if a.get("para_end") and b.get("para"):
			assert a["para_end"] < b["para"]


def test_rad_early_role_heading_does_not_swallow_the_decision():
	paras = []
	for n in range(1, 6):
		paras.append(f"[{n}] The Appellant appeals the decision of the Refugee Protection Division that rejected the claim for refugee protection, number {n}.")
	text = "REASONS FOR DECISION\nINTRODUCTION\n" + "\n".join(paras[:2]) + "\nROLE OF THE RAD\n" + "\n".join(paras[2:])
	n = 6
	body = []
	for _ in range(8):
		body.append(f"[{n}] I find that the RPD was correct to conclude the Appellant is not credible; I am not persuaded that the explanation is reasonable.")
		n += 1
	text += "\n" + "\n".join(body)
	text += f"\n[{n}] For these reasons, the appeal is dismissed and the decision of the RPD is confirmed.\nCONCLUSION\nThe appeal is dismissed.\n"
	rows = outline_v2(text, format_decision(text, {}))
	_no_overlap(rows)
	sections = [r["section"] for r in rows if r["kind"] == "section"]
	if rows:
		assert sections[-1] == "disposition"
		assert sections == sorted(sections, key=["background", "issues", "analysis", "disposition"].index)


def test_live_reader_and_case_reader_citations_carry_section_keys(monkeypatch):
	from backend.live_reader import build_live_reader_payload
	from backend.live_analysis import paragraphs_from_pasted_text
	from backend.models import CaseReaderCitationResponse

	monkeypatch.setenv("ILIT_OUTLINE_V2", "1")
	text = DECISION.replace(
		"[9] The applicant argues",
		"[9] See Baker v Canada (Minister of Citizenship and Immigration), [1999] 2 SCR 817 at para 22. The applicant argues",
	)
	text, paragraphs = paragraphs_from_pasted_text(text)
	rows = build_live_reader_payload(text, paragraphs, "Pasted text", None)["citations"]
	assert rows and all("section" in r for r in rows)
	assert any(r["section"] == "analysis" for r in rows)
	model = CaseReaderCitationResponse(id=1)
	tag_citation_sections([model], _outline(), lambda row: DECISION.index("ties to India"))
	assert model.section == "analysis" and model.section_point == "Ties to home country"


def test_appeal_headings_place_lower_decision_standard_of_review_and_disposition():
	lines = ["REASONS FOR JUDGMENT", "I. Introduction"]
	n = 1

	def add(count, sentence):
		nonlocal n
		for _ in range(count):
			lines.append(f"[{n}] {sentence} (paragraph {n}).")
			n += 1

	add(3, "The appellant bank appeals a judgment of the Tax Court about a payment system")
	lines.append("II. Reasons of the Tax Court judge")
	add(3, "The Tax Court judge found that the supply was a financial service")
	lines.append("III. Errors alleged and standard of review")
	add(2, "The standard of review is correctness for questions of law and the appeal raises two issues")
	lines.append("IV. Analysis")
	lines.append("Q. Okay, and why is that?")
	add(6, "I am not persuaded that the judge erred and I find that the conclusion was correct; however the argument fails")
	lines.append("V. Proposed disposition")
	add(1, "I would dismiss the appeal with costs")
	text = "\n".join(lines)
	rows = outline_v2(text, format_decision(text, {}))
	sections = {r["section"]: r for r in rows if r["kind"] == "section"}
	assert list(sections) == ["background", "issues", "analysis", "disposition"]
	assert sections["background"]["para_end"] == 6 and sections["issues"]["para"] == 7
	assert not any(r["title"].startswith("Q.") for r in rows)
	_no_overlap(rows)


def test_numbered_closing_paragraphs_become_the_disposition_before_a_bare_order_block():
	lines = ["REASONS FOR JUDGMENT"]
	for n in range(1, 8):
		lines.append(f"[{n}] The applicant argues that the officer erred; I do not agree and I find the decision reasonable, point {n}.")
	lines.append("[8] For these reasons the application for judicial review is dismissed.")
	lines.append("[9] No question of general importance is certified.")
	lines.append("JUDGMENT")
	lines.append("THIS COURT'S JUDGMENT is that the application is dismissed.")
	text = "\n".join(lines)
	rows = outline_v2(text, format_decision(text, {}))
	disposition = [r for r in rows if r["section"] == "disposition" and r["kind"] == "section"]
	assert disposition and disposition[0]["para"] == 8


def test_citation_offset_uses_the_citation_not_its_chunk_start():
	where = DECISION.index("ties to India")
	row = {
		"chunk_id": 7,
		"offset_start": 40,
		"layer_spans": {
			"full_case": {"absolute_start": 0, "local_start": where},
			"paragraph": {"absolute_start": DECISION.index("Background"), "local_start": where - DECISION.index("Background")},
		},
	}
	assert citation_offset(row) == where
	chunk_only = {"chunk_id": 7, "layer_spans": {"paragraph": {"absolute_start": DECISION.index("[10]"), "local_start": 5}}}
	assert citation_offset(chunk_only) == DECISION.index("[10]") + 5
