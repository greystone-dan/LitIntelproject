"""Tests for the step-2 citation and statute refinement layers (backend.citation_refine)."""

import pytest

from backend.citation_refine import (
	ALL_STEPS,
	enabled_steps,
	identifier_keys,
	parse_pinpoint,
	refine_case_citations,
	refine_document,
	refine_statute_references,
	split_provision_list,
)
from backend.citation_refine.context import DocumentContext
from backend.citation_refine.pinpoints import parse_bare_page_pinpoint
from backend.citation_refine.resolution import (
	build_case_index,
	resolve_case_rows,
	resolve_statute_row,
	split_section_text,
)


def _cases(text, **kwargs):
	return refine_case_citations(text, current_year=2026, **kwargs).rows


def _one(rows, kind=None):
	matching = [row for row in rows if kind is None or row.kind == kind]
	assert len(matching) == 1, [(row.kind, row.citation_text) for row in rows]
	return matching[0]


# --------------------------------------------------------------------------- pinpoints


@pytest.mark.parametrize(
	("text", "kind", "values"),
	[
		("at paras 85-87 and 99", "paragraph", (85, 86, 87, 99)),
		("at para. 23", "paragraph", (23,)),
		("aux paragraphes 12 à 14", "paragraph", (12, 13, 14)),
		("au par. 5", "paragraph", (5,)),
		("at pp. 841-42", "page", (841, 842)),
		("paras 3, 5; 9", "paragraph", (3, 5, 9)),
	],
)
def test_parse_pinpoint_expands_lists_and_ranges(text, kind, values):
	pinpoint = parse_pinpoint(text)
	assert pinpoint is not None
	assert pinpoint.kind == kind
	assert pinpoint.values == values


def test_parse_pinpoint_ignores_words_ending_in_label_letters():
	assert parse_pinpoint("R.S.C. 1985 (5th Supp. 5)") is None


def test_pinpoint_stops_before_next_citation_volume():
	assert parse_pinpoint("at para 22, 131 ACWS (3d) 508").values == (22,)


def test_huge_pinpoint_range_is_capped():
	pinpoint = parse_pinpoint("at paras 1-5000")
	assert pinpoint.truncated
	assert len(pinpoint.values) == 200


def test_bare_page_pinpoint_after_reporter():
	pinpoint = parse_bare_page_pinpoint(" at 841.")
	assert pinpoint.kind == "page" and pinpoint.values == (841,)
	assert parse_bare_page_pinpoint(" at 2019 SCC 5") is None


# --------------------------------------------------------------------------- case layer: new formats


def test_french_neutral_citation_with_c_and_paragraph():
	row = _one(_cases("Dhillon c. Canada, 2020 CF 123, par. 12."))
	assert row.kind == "case"
	assert row.action == "added"
	assert row.language == "fr"
	assert row.normalized_citation == "Dhillon c. Canada, 2020 CF 123, at para. 12"
	assert "2020 FC 123" in row.identifiers
	assert row.pinpoints[0].values == (12,)


def test_csc_maps_to_scc_identifier():
	row = _one(_cases("Canada (Ministre de la Citoyenneté et de l'Immigration) c. Vavilov, 2019 CSC 65, au para 23."))
	assert row.identifiers == ("2019 SCC 65",)
	assert row.pinpoints[0].values == (23,)


def test_quicklaw_and_imm_lr_reporters():
	lee = _one(_cases("Lee v. Canada, [2003] F.C.J. No. 123 (QL)"))
	assert lee.normalized_citation == "Lee v. Canada, [2003] F.C.J. No. 123"
	assert lee.identifiers == ("2003 FCJ 123",)
	smith = _one(_cases("Smith v. Canada (1995), 30 Imm. L.R. (2d) 1 (F.C.T.D.)"))
	assert smith.normalized_citation == "Smith v. Canada (1995), 30 Imm. L.R. (2d) 1"
	assert smith.citation_text.endswith("(F.C.T.D.)")
	assert "30 IMMLR2D 1" in smith.identifiers


def test_r_v_and_re_style_names():
	rows = _cases("R v. Jordan, 2016 SCC 27; Re Singh, 2010 FC 5; Singh (Re), 2010 FC 6")
	assert [row.normalized_citation for row in rows] == [
		"R v. Jordan, 2016 SCC 27",
		"Singh (Re), 2010 FC 5",
		"Singh (Re), 2010 FC 6",
	]


def test_re_style_name_with_connectors():
	row = _one(_cases("Re Sheehan and Criminal Injuries Compensation Board (1974), 52 D.L.R. (3d) 728 (Ont. C.A.); Maple"))
	assert row.case_name == "Sheehan and Criminal Injuries Compensation Board (Re)"


def test_bare_provincial_neutral_citations():
	rows = _cases("Re X, 2019 QCCQ 44; 2018 BCCA 77")
	assert {row.normalized_citation for row in rows} >= {"2018 BCCA 77"}
	assert any("2019 QCCQ 44" in row.identifiers for row in rows)


def test_short_name_with_reporter_becomes_case():
	row = _one(_cases("Chieu, [2002] 1 FCR 113"))
	assert row.kind == "case"
	assert "short_name" in row.notes
	assert row.identifiers[0] == "2002 1 FCR 113"


def test_docket_numbers():
	rows = _cases("Docket: IMM-1234-22 and A-56-21")
	assert [row.normalized_citation for row in rows if row.kind == "docket"] == ["IMM-1234-22", "A-56-21"]


def test_dockets_can_be_excluded():
	assert refine_case_citations("Docket: IMM-1234-22", include_dockets=False).rows == []


def test_name_does_not_run_into_previous_citation():
	rows = _cases("Jones v. Great Western Railway Co. (1930),47 T.L.R. 39 at 45 (H.L.) See also Re Jaballah, 2016 FC 586, at para 5")
	jaballah = [row for row in rows if "2016 FC 586" in row.identifiers]
	assert jaballah[0].citation_text.startswith("Re Jaballah")


def test_sentence_boundary_stops_case_name():
	row = _one(_cases("The applicant relies on the Court. Baker v. Canada, [1999] 2 S.C.R. 817."))
	assert row.citation_text.startswith("Baker v. Canada")


# --------------------------------------------------------------------------- case layer: parallel citations


def test_parallel_citations_are_joined_with_all_identifiers():
	row = _one(_cases("Kane v. Board of Governors (UBC), [1980] 1 S.C.R. 1105, 110 D.L.R. (3d) 311"))
	assert row.step == "C3_parallel"
	assert row.action == "corrected"
	assert row.identifiers == ("1980 1 SCR 1105", "1 SCR 1105", "110 DLR3D 311")
	assert row.replaces


def test_pinpoint_between_parallel_citations():
	row = _one(_cases("Gjergo v Canada (Minister of Citizenship and Immigration), 2004 FC 303 at para 22, 131 ACWS (3d) 508."))
	assert row.citation_text.endswith("131 ACWS (3d) 508")
	assert "131 ACWS3D 508" in row.identifiers
	assert row.pinpoints[0].values == (22,)


def test_page_pinpoint_after_reporter():
	row = _one(_cases("Baker v Canada (MCI), [1999] 2 SCR 817 at 841."))
	assert row.citation_text.endswith("at 841")
	assert row.pinpoints[0].kind == "page"
	assert row.normalized_citation.endswith("at p. 841")


def test_parallel_step_off_keeps_first_citation_only():
	rows = refine_case_citations(
		"Kane v. Board of Governors (UBC), [1980] 1 S.C.R. 1105, 110 D.L.R. (3d) 311",
		steps=["C1_gap_scan"],
	).rows
	assert all("110 DLR3D 311" not in row.identifiers for row in rows)


# --------------------------------------------------------------------------- case layer: back-references


def test_ibid_and_id_point_to_previous_case():
	rows = _cases("Vavilov v. Canada, 2019 SCC 65 at para 23. Ibid at para 25. Id. at para 30.")
	short = [row for row in rows if row.kind == "case_short"]
	assert [row.citation_text for row in short] == ["Ibid at para 25", "Id. at para 30"]
	assert all(row.anchor_offset_start == 0 for row in short)
	assert [row.pinpoints[0].values for row in short] == [(25,), (30,)]
	assert short[0].normalized_citation == "Vavilov v. Canada, 2019 SCC 65, at para. 25"


def test_supra_with_pinpoint_and_note():
	text = "Canada v. Vavilov, 2019 SCC 65 [Vavilov]. Later: Vavilov, supra at para 99; See Vavilov, supra note 4."
	rows = _cases(text)
	short = [row for row in rows if row.kind == "case_short"]
	assert [row.citation_text for row in short] == ["Vavilov, supra at para 99", "Vavilov, supra note 4"]
	assert short[0].pinpoints[0].values == (99,)
	assert short[0].identifiers == ("2019 SCC 65",)


def test_supra_pinpoint_does_not_swallow_following_words():
	text = "Baker v. Canada, [1999] 2 S.C.R. 817. As noted in Baker, supra, at para. 61, the duty applies."
	short = [row for row in _cases(text) if row.kind == "case_short"]
	assert short[0].citation_text == "Baker, supra, at para. 61"


def test_supra_without_known_case_is_ignored():
	assert [row for row in _cases("Unknown, supra at para 4.") if row.kind == "case_short"] == []


# --------------------------------------------------------------------------- case layer: validation


def test_implausible_years_are_flagged():
	rows = {row.normalized_citation: row for row in _cases("Also 2035 SCC 4 and 1995 SCC 3 and 2010 FCT 4")}
	assert rows["2035 SCC 4"].confidence <= 0.4
	assert "implausible_year:1995 SCC" in rows["1995 SCC 3"].notes
	assert "fct_after_2003" in rows["2010 FCT 4"].notes


def test_self_citation_is_dropped():
	result = refine_case_citations("Smith v. Canada, 2020 FC 5 at para 3.", source_citations=["2020 FC 5"])
	assert result.rows == []
	assert "self_citation" in result.dropped[0].notes


def test_to_raw_match_is_pass_one_compatible():
	row = _one(_cases("Dhillon c. Canada, 2020 CF 123, par. 12."))
	raw = row.to_raw_match()
	assert raw.kind == "case"
	assert raw.offset_start == row.offset_start
	assert raw.pinpoint == "at para. 12"


def test_identifier_keys_match_on_both_sides():
	assert identifier_keys("2019 SCC 65") == identifier_keys("2019 CSC 65")
	assert identifier_keys("[1999] 2 S.C.R. 817") == ("1999 2 SCR 817", "2 SCR 817")


# --------------------------------------------------------------------------- law layer


def _laws(text, **kwargs):
	return refine_statute_references(text, **kwargs)


def test_split_provision_list():
	assert split_provision_list("96, 97") == ["96", "97"]
	assert split_provision_list("112 to 114") == ["112", "113", "114"]
	assert split_provision_list("36(1)(a) and (b)") == ["36(1)(a)", "36(1)(b)"]
	assert split_provision_list("117(9)(a) to (d)") == ["117(9)(a)", "117(9)(b)", "117(9)(c)", "117(9)(d)"]
	assert split_provision_list("36(1)a) et b)") == ["36(1)(a)", "36(1)(b)"]
	assert split_provision_list("10-100") == ["10", "100"]


def test_section_lists_no_longer_lose_their_sections():
	rows = _laws("IRPA ss. 96, 97 apply.").rows
	assert [(row.instrument_key, row.section) for row in rows] == [("canada.irpa", "96"), ("canada.irpa", "97")]
	assert all(row.group_size == 2 for row in rows)
	assert [row.group_index for row in rows] == [0, 1]


def test_the_act_resolved_from_definition():
	text = "The Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] governs. Under section 25(1) of the Act the Minister may act."
	rows = [row for row in _laws(text).rows if row.provision]
	assert rows[0].instrument_key == "canada.irpa"
	assert rows[0].provision_path == ("25", "1")


def test_regulations_default_in_immigration_decision():
	result = _laws("Under the IRPA, section 216(1)(b) of the Regulations applies.")
	row = next(row for row in result.rows if row.provision == "216(1)(b)")
	assert row.instrument_key == "canada.irpr"
	assert "instrument_from_default_reading" in row.notes


def test_the_act_follows_the_only_act_named():
	text = "section 5 of the Citizenship Act, R.S.C. 1985, c. C-29. Under the Act, s. 5(1) applies."
	rows = [row for row in _laws(text).rows if row.provision == "5(1)"]
	assert rows[0].instrument_key == "canada.citizenship_act"


def test_rule_of_federal_courts_immigration_rules_is_identified():
	row = _one(_laws("Rule 9 of the Federal Courts Citizenship, Immigration and Refugee Protection Rules, SOR/93-22").rows)
	assert row.instrument_key == "canada.fc_cirp_rules"
	assert row.normalized_citation.endswith("r. 9")
	assert row.action == "corrected"


def test_provision_then_acronym():
	row = _one(_laws("r. 117(9)(d) IRPR").rows)
	assert row.instrument_key == "canada.irpr"
	assert row.provision_path == ("117", "9", "d")


def test_french_statute_references():
	rows = _laws("l'article 25 de la LIPR et l'alinéa 36(1)a) et b) du Règlement sur l'immigration et la protection des réfugiés").rows
	assert [(row.instrument_key, row.provision, row.language) for row in rows] == [
		("canada.irpa", "25", "fr"),
		("canada.irpr", "36(1)(a)", "fr"),
		("canada.irpr", "36(1)(b)", "fr"),
	]
	assert rows[0].normalized_citation.endswith("s. 25")


def test_refugee_convention_articles_keep_capital_letters():
	rows = _laws("Article 1F(b) of the Refugee Convention; art 1E applies").rows
	assert [row.normalized_citation for row in rows] == [
		"art. 1F(b) of Refugee Convention",
		"art. 1E of Refugee Convention",
	]


def test_new_treaty_in_registry():
	row = _one(_laws("Article 3 of the Convention Against Torture").rows)
	assert row.instrument_key == "international.cat"


def test_charter_needs_capital_letter():
	assert _laws("the charter flight left at 5").rows == []


def test_out_of_range_provision_is_flagged():
	row = _one(_laws("s. 900 of IRPA").rows)
	assert "provision_out_of_range" in row.notes
	assert row.confidence < 0.5


def test_junk_generic_rows_are_dropped():
	from backend.citations import RawCitationMatch

	junk = RawCitationMatch("statute", "of the Act", "of the Act", 0, 10)
	result = _laws("of the Act and more", pass_one_rows=[junk])
	assert result.rows == []
	assert result.dropped[0].action == "dropped"


def test_registry_step_off_ignores_new_instruments():
	assert _laws("Article 3 of the Convention Against Torture", steps=["L2_gap_scan"]).rows == []


def test_document_context_sentences_skip_abbreviations():
	context = DocumentContext.build("See s. 3 of the Act. Next sentence here.")
	assert context.sentence_start(len("See s. 3 of the Act. Next")) == len("See s. 3 of the Act. ")
	assert context.sentence_start(8) == 0


# --------------------------------------------------------------------------- combined


def test_refine_document_runs_both_layers_and_resolves_overlaps():
	text = "Baker v. Canada, [1999] 2 S.C.R. 817, at para. 5, applied s. 25(1) of IRPA. Ibid at para 7."
	result = refine_document(text, current_year=2026)
	assert [row.kind for row in result.cases.rows] == ["case", "case_short"]
	assert [row.provision for row in result.laws.rows] == ["25(1)"]
	assert "cases" in result.summary()


def test_enabled_steps_from_environment(monkeypatch):
	monkeypatch.setenv("CASELIBRARY_CITATION_REFINE_STEPS", "C1_gap_scan, L3_expand")
	assert enabled_steps() == frozenset({"C1_gap_scan", "L3_expand"})
	monkeypatch.setenv("CASELIBRARY_CITATION_REFINE_STEPS", "none")
	assert enabled_steps() == frozenset()
	monkeypatch.delenv("CASELIBRARY_CITATION_REFINE_STEPS")
	assert enabled_steps() == frozenset(ALL_STEPS)
	with pytest.raises(ValueError):
		enabled_steps(["C9_unknown"])


def test_no_steps_reproduces_pass_one_rows():
	from backend.citations import extract_case_citation_matches

	text = "Smith v. Canada, 2019 FC 12 at para 4. See also 2020 FCA 7."
	refined = refine_case_citations(text, steps=()).rows
	assert [(row.offset_start, row.offset_end) for row in refined] == [
		(row.offset_start, row.offset_end) for row in extract_case_citation_matches(text)
	]


# --------------------------------------------------------------------------- resolution


def test_case_resolution_uses_parallel_citations_and_anchors():
	index = build_case_index(
		[
			(1, None, "[1980] 1 S.C.R. 1105", "Kane v. Board of Governors (UBC)", 1980, None),
			(2, "2019 SCC 65", None, "Canada v. Vavilov", 2019, "IMM-1234-22"),
		]
	)
	text = (
		"Kane v. Board of Governors (UBC), 110 D.L.R. (3d) 311, [1980] 1 S.C.R. 1105. "
		"Vavilov v. Canada, 2019 CSC 65 at paras 3-4 and 99. Ibid at para 7. Docket IMM-1234-22."
	)
	rows = _cases(text)

	def paragraphs(case_id):
		return [(10, 1, 5), (11, 6, 50)] if case_id == 2 else []

	results = resolve_case_rows(rows, index, paragraphs)
	by_text = {result.row.citation_text: result for result in results}
	kane = next(result for result in results if result.row.citation_text.startswith("Kane"))
	assert kane.target_case_id == 1 and kane.method == "identifier"
	vavilov = next(result for result in results if result.row.citation_text.startswith("Vavilov"))
	assert vavilov.target_case_id == 2
	assert vavilov.pinpoint_status == "partial"
	assert [link.paragraph for link in vavilov.paragraphs] == [3, 4]
	assert vavilov.unmatched_paragraphs == (99,)
	ibid = by_text["Ibid at para 7"]
	assert ibid.method == "anchor" and ibid.target_case_id == 2
	assert ibid.paragraphs[0].chunk_id == 11
	assert by_text["IMM-1234-22"].target_case_id == 2


def test_case_resolution_statuses():
	index = build_case_index([(1, "2019 FC 1", None, "A v. B", 2019, None), (2, "2019 FC 1", None, "C v. D", 2019, None)])
	results = {result.row.normalized_citation: result for result in resolve_case_rows(_cases("2019 FC 1 and 2020 FC 2"), index)}
	assert results["2019 FC 1"].status == "ambiguous"
	assert results["2020 FC 2"].status == "not_in_database"


def test_page_pinpoints_are_reported_not_guessed():
	index = build_case_index([(1, None, "[1999] 2 S.C.R. 817", "Baker v. Canada", 1999, None)])
	result = resolve_case_rows(_cases("Baker v. Canada, [1999] 2 S.C.R. 817, at p. 841."), index, lambda _id: [(1, 1, 80)])[0]
	assert result.target_case_id == 1
	assert result.pinpoint_status == "page_unmapped"


def test_split_section_text_builds_provision_tree():
	text = (
		"36 (1) A permanent resident is inadmissible for (a) having been convicted of an offence under "
		"paragraph 36(1)(a); (b) having been convicted outside Canada (i) first, (ii) second; (h) eight; (i) ninth. "
		"(2) A foreign national is inadmissible under subsections (1) and (2): (a) other."
	)
	paths = [unit.path for unit in split_section_text("36", text)]
	assert paths == [
		("36", "1"),
		("36", "1", "a"),
		("36", "1", "b"),
		("36", "1", "b", "i"),
		("36", "1", "b", "ii"),
		("36", "1", "h"),
		("36", "1", "i"),
		("36", "2"),
		("36", "2", "a"),
	]


def test_statute_resolution_to_clause_level():
	section_text = "36 (1) A permanent resident is inadmissible for (a) having been convicted; (b) other. (2) Foreign nationals."
	row = next(row for row in _laws("paragraph 36(1)(b) of the IRPA").rows)

	def get_section(key, section):
		return (77, section_text) if (key, section) == ("canada.irpa", "36") else None

	result = resolve_statute_row(row, lambda key: key == "canada.irpa", get_section)
	assert result.status == "resolved_provision"
	assert result.section_id == 77
	assert result.matched_path == ("36", "1", "b")
	assert section_text[result.unit_start : result.unit_end].startswith("(b) other")

	partial_row = next(row for row in _laws("paragraph 36(1)(z) of the IRPA").rows)
	assert resolve_statute_row(partial_row, lambda key: True, get_section).status == "partial_provision"
	missing = next(row for row in _laws("section 40 of the IRPA").rows)
	assert resolve_statute_row(missing, lambda key: True, get_section).status == "section_not_indexed"
	assert resolve_statute_row(missing, lambda key: False, get_section).status == "document_not_indexed"


def test_unknown_law_names_are_kept_but_fragments_dropped():
	from backend.citations import RawCitationMatch

	rows = [
		RawCitationMatch("statute", "Motor Vehicle Act", "Motor Vehicle Act", 0, 17),
		RawCitationMatch("statute", "Does the Act", "Does the Act", 22, 34),
	]
	result = _laws("Motor Vehicle Act. Does the Act apply?", pass_one_rows=rows)
	assert [(row.normalized_citation, row.confidence) for row in result.rows] == [("Motor Vehicle Act", 0.4)]
	assert "sentence_fragment" in result.dropped[0].notes
