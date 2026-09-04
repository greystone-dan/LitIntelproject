from types import SimpleNamespace

import pytest
from fastapi import HTTPException

from backend import citations
from backend import routes
from scripts.extract_irpa_irpr_references import extract_case_references


def test_parse_legislation_citation_returns_expandable_provision_identity():
	parsed = citations.parse_legislation_citation("paragraph 34(1)(f) of IRPA")

	assert parsed is not None
	assert parsed.instrument_key == "canada.irpa"
	assert parsed.pinpoint == "34(1)(f)"
	assert parsed.legislation_url.endswith("/section-34.html")


def test_parse_legislation_citation_distinguishes_irpr():
	parsed = citations.parse_legislation_citation("IRPR s. 12(1)")

	assert parsed is not None
	assert parsed.instrument_key == "canada.irpr"
	assert parsed.pinpoint == "12(1)"


def test_self_case_name_filter_rejects_source_surname_only():
	match = citations.RawCitationMatch("case_short", "Calixto", "Calixto, 2005 FC 1037", 0, 7)

	assert citations.is_self_case_name_match(
		"Calixto v. Canada (Minister of Citizenship and Immigration)", match
	)


def test_self_case_name_filter_keeps_other_case_short_form():
	match = citations.RawCitationMatch("case_short", "Vavilov", "Vavilov, 2019 SCC 65", 0, 7)

	assert not citations.is_self_case_name_match("Calixto v. Canada", match)


def test_self_case_citation_filter_rejects_source_neutral_citation():
	case = SimpleNamespace(citation="2005 FC 1037", secondary_citation=None)
	match = citations.RawCitationMatch("neutral", "2005 FC 1037", "2005 FC 1037", 0, 12)

	assert citations.is_self_case_citation(case, match)


def test_raw_citation_match_positional_constructor_keeps_optional_pinpoint_default():
	match = citations.RawCitationMatch("case", "2005 FC 1037", "2005 FC 1037", 0, 12)

	assert match.pinpoint is None
	assert match.anchor_citation_text is None
	assert match.anchor_offset_start is None
	assert match.anchor_offset_end is None


def test_raw_citation_match_positional_constructor_accepts_existing_sixth_argument():
	match = citations.RawCitationMatch("case", "2005 FC 1037", "2005 FC 1037", 0, 12, "at para. 4")

	assert match.pinpoint == "at para. 4"
	assert match.anchor_citation_text is None


class FakeDatabase:
	def __init__(self, rows=(), scalar_value=None):
		self.rows = list(rows)
		self.scalar_values = list(scalar_value) if isinstance(scalar_value, list) else [scalar_value]

	def execute(self, statement):
		self.statement = statement
		return self.rows

	def scalar(self, statement):
		self.statement = statement
		if self.scalar_values:
			return self.scalar_values.pop(0)
		return None


class FakeCitationSession:
	def __init__(self, target_case_id=7):
		self.target_case_id = target_case_id
		self.added = []

	def scalar(self, statement):
		return SimpleNamespace(id=self.target_case_id)

	def add_all(self, rows):
		self.added.extend(rows)


class QueuedScalarsSession:
	def __init__(self, scalar_batches):
		self.scalar_batches = iter(scalar_batches)
		self.commits = 0

	def scalars(self, statement):
		return next(self.scalar_batches)

	def commit(self):
		self.commits += 1


def test_extract_citations_from_text_normalizes_and_resolves(monkeypatch):
	monkeypatch.setattr(citations, "resolve_neutral_to_case_id", lambda session, neutral: 42 if neutral == "2024 FC 100" else None)
	session = FakeCitationSession()
	text = "See 2024 FC 100, Smith v. Jones, 2023 FCA 5, and IRPA s. 72(1)."

	rows = citations.extract_citations_from_text(session, source_case_id=11, text=text)

	# Case-law citations are a separate layer from statute references (see
	# test_extract_statute_reference_matches_returns_only_law_layer), so the
	# IRPA s. 72(1) reference in this text is intentionally excluded here.
	assert len(rows) == 2
	assert rows[0].target_case_id == 42
	assert rows[0].normalized_citation == "2024 FC 100"
	assert rows[1].target_case_id is None
	assert rows[1].normalized_citation == "Smith v. Jones, 2023 FCA 5"
	assert len(session.added) == 2


def test_extract_citations_from_text_resolves_short_form_alias_to_canonical_case():
	class AliasCaseSession:
		def __init__(self):
			self.added = []
			self.calls = []

		def execute(self, statement, params=None):
			self.calls.append((str(statement), params))
			pattern = (params or {}).get("pattern", "") if isinstance(params, dict) else ""
			if "oakes" in pattern.lower():
				return SimpleNamespace(scalar_one_or_none=lambda: 77)
			return SimpleNamespace(scalar_one_or_none=lambda: None)

		def scalar(self, statement, params=None):
			self.calls.append((str(statement), params))
			pattern = (params or {}).get("pattern", "") if isinstance(params, dict) else ""
			if "oakes" in pattern.lower():
				return 77
			return None

		def add_all(self, rows):
			self.added.extend(rows)

	session = AliasCaseSession()
	text = "The Court in R v Oakes at para 100 considered the issue. A second Oakes mention appears later."

	rows = citations.extract_citations_from_text(session, source_case_id=11, text=text)

	alias_rows = [row for row in rows if row.citation_text == "R v Oakes at para 100"]
	assert len(alias_rows) == 1
	assert alias_rows[0].target_case_id == 77
	assert alias_rows[0].unresolved is False
	assert alias_rows[0].offset_start != alias_rows[0].offset_end
	assert any(row.citation_text == "R v Oakes at para 100" for row in rows)


def test_resolve_case_alias_returns_none_for_duplicate_candidates():
	class DuplicateAliasSession:
		def __init__(self):
			self.patterns = []

		def execute(self, statement, params=None):
			pattern = (params or {}).get("pattern", "")
			self.patterns.append(pattern)
			if "oakes" in pattern.lower() and "r v oakes" in pattern.lower():
				return SimpleNamespace(scalars=lambda: SimpleNamespace(all=lambda: [77, 88, 77]))
			return SimpleNamespace(scalars=lambda: SimpleNamespace(all=lambda: []))

	raw_match = citations.RawCitationMatch(
		"case_short", "R v Oakes at para 100", "R v Oakes at para 100", 0, 21
	)
	session = DuplicateAliasSession()

	assert citations._resolve_case_alias_to_case_id(session, raw_match) is None
	assert len(session.patterns) == 1


def test_resolve_case_alias_returns_none_when_unresolved():
	class UnresolvedAliasSession:
		def execute(self, statement, params=None):
			return SimpleNamespace(scalars=lambda: SimpleNamespace(all=lambda: []))

	raw_match = citations.RawCitationMatch("case_short", "Unknown at para 10", "Unknown at para 10", 0, 18)

	assert citations._resolve_case_alias_to_case_id(UnresolvedAliasSession(), raw_match) is None


def test_rebuild_citations_for_case_keeps_alias_resolution_when_rerunning():
	class AliasRebuildSession:
		def __init__(self):
			self.added = []

		def execute(self, statement, params=None):
			return None

		def scalar(self, statement, params=None):
			pattern = str(statement).lower()
			if "oakes" in pattern:
				return SimpleNamespace(id=77)
			return None

		def add_all(self, rows):
			self.added.extend(rows)

	case = SimpleNamespace(
		id=11,
		title="Calixto v. Canada",
		full_text="The Court in R v Oakes at para 100 considered the issue.",
		summary="",
	)
	session = AliasRebuildSession()

	rows = citations.rebuild_citations_for_case(session, case)

	assert rows == 1
	assert session.added[0].target_case_id == 77
	assert session.added[0].unresolved is False
	assert session.added[0].citation_text == "R v Oakes at para 100"


def test_extract_raw_citation_matches_supports_canlii_and_section_keyword():
	text = "See 2023 CanLII 12345 (SCC) and IRPA section 34(1)."

	matches = citations.extract_raw_citation_matches(text)

	assert len(matches) == 2
	assert matches[0].kind == "neutral"
	assert matches[0].normalized_citation == "2023 CanLII 12345 (SCC)"
	assert matches[1].kind == "statute"
	assert matches[1].normalized_citation == "Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 34(1)"


def test_extract_raw_citation_matches_canonicalizes_comma_after_irpa():
	text = "The exclusion ground appears in IRPA, s. 34(1)(f)."

	matches = citations.extract_statute_reference_matches(text)

	assert any(
		match.kind == "statute"
		and match.normalized_citation == "Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 34(1)(f)"
		for match in matches
	)


def test_extract_raw_citation_matches_supports_long_form_law_citations():
	text = (
		"The Immigration and Refugee Protection Act, S.C. 2001, c. 27, section 98 applies, "
		"as does the Canadian Charter of Rights and Freedoms, section 7, and the Criminal Code, section 57. "
		"Article 1F(b) of the Refugee Convention, Can. T.S. 1969 No. 6 must also be considered."
	)

	matches = citations.extract_raw_citation_matches(text)

	assert any(m.kind == "statute" and m.normalized_citation.startswith("Immigration and Refugee Protection Act, S.C. 2001, c. 27") for m in matches)
	assert any(m.kind == "statute" and m.normalized_citation.startswith("Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982") for m in matches)
	assert any(m.kind == "statute" and m.normalized_citation.startswith("Criminal Code, R.S.C. 1985, c. C-46") for m in matches)
	assert any(m.kind == "instrument" and "Refugee Convention" in m.normalized_citation for m in matches)
	assert any(m.kind == "instrument" and "art. 1F(b)" in m.normalized_citation for m in matches)
	assert any(m.kind == "instrument" and "Can. T.S. 1969 No. 6" in m.normalized_citation for m in matches)


def test_extract_statute_reference_matches_supports_french_provision_forms():
	text = (
		"L'article 112 de la Loi sur l'immigration et la protection des réfugiés, LC 2001, c 27, "
		"et le paragraphe 320.13(1) du Code criminel, LRC 1985, c C-46, s'appliquent."
	)

	matches = citations.extract_statute_reference_matches(text)

	assert any("Loi sur l'immigration" in match.normalized_citation for match in matches)
	assert any("Code criminel" in match.normalized_citation for match in matches)


def test_extract_statute_reference_matches_excludes_procedural_order_labels():
	matches = citations.extract_statute_reference_matches(
		"The Court issued a Preliminary Order and a Show Cause Order."
	)

	assert matches == []


def test_extract_statute_reference_matches_returns_only_law_layer():
	text = (
		"Vavilov v Canada, 2019 SCC 65 considered IRPA s. 72(1), the Canadian Charter "
		"of Rights and Freedoms, section 7, and Article 1F(b) of the Refugee Convention."
	)

	matches = citations.extract_statute_reference_matches(text)

	assert matches
	assert all(match.kind in {"statute", "instrument"} for match in matches)
	assert any("Immigration and Refugee Protection Act" in match.normalized_citation for match in matches)
	assert any("Canadian Charter of Rights and Freedoms" in match.normalized_citation for match in matches)
	assert any("Refugee Convention" in match.normalized_citation for match in matches)
	assert not any("Vavilov" in match.citation_text for match in matches)


def test_extract_statute_references_from_text_keeps_non_irpa_instruments():
	session = FakeCitationSession()
	rows = citations.extract_statute_references_from_text(
		session,
		source_case_id=11,
		text="Section 18.1 of the Federal Courts Act and Article 1F(b) of the Refugee Convention apply.",
	)

	assert {row.reference_kind for row in rows} == {"statute", "instrument"}
	assert any("Federal Courts Act" in (row.normalized_reference or "") for row in rows)
	assert any("Refugee Convention" in (row.normalized_reference or "") for row in rows)


def test_corpus_statute_extraction_keeps_non_irpa_references():
	case = SimpleNamespace(id=11, full_text="", summary="")
	chunk = SimpleNamespace(
		id=21,
		chunk_set="paragraph",
		chunk_index=0,
		text="IRPA section 34(1)(f), section 7 of the Charter, and Article 1F(b) of the Refugee Convention.",
	)

	rows = extract_case_references(case, [chunk])

	assert any(row.instrument_key == "canada.irpa" for row in rows)
	assert any("Charter" in (row.normalized_reference or "") for row in rows)
	assert any("Refugee Convention" in (row.normalized_reference or "") for row in rows)


def test_extract_statute_reference_matches_supports_orders_and_si_citations():
	text = "Section 2 of the Canadian Passport Order, SI/81-86, states the following."

	matches = citations.extract_statute_reference_matches(text)

	assert any(
		match.kind == "statute"
		and match.citation_text == "Section 2 of the Canadian Passport Order, SI/81-86"
		and match.normalized_citation == "Canadian Passport Order, SI/81-86 s. 2"
		for match in matches
	)


def test_extract_statute_reference_matches_propagates_anchored_article_subheadings():
	text = (
		"Articles 31 and 32 of the Vienna Convention on the Law of Treaties guide interpretation.\n"
		"Article 31. General rule of interpretation\n"
		"Article 32. Supplementary means of interpretation"
	)

	matches = citations.extract_statute_reference_matches(text)

	assert any(match.citation_text == "Article 31" for match in matches)
	assert any(match.citation_text == "Article 32" for match in matches)
	assert all(text[match.offset_start:match.offset_end] == match.citation_text for match in matches)
	assert all(
		"Vienna Convention on the Law of Treaties" in match.normalized_citation
		for match in matches
		if match.citation_text in {"Article 31", "Article 32"}
	)


def test_extract_statute_reference_matches_supports_short_vienna_convention_anchor():
	text = (
		"Articles 31 and 32 of the Vienna Convention guide interpretation.\n"
		"Article 31. General rule of interpretation"
	)

	matches = citations.extract_statute_reference_matches(text)

	assert any(
		match.citation_text == "Articles 31 and 32 of the Vienna Convention"
		and match.normalized_citation == "arts. 31, 32 of Vienna Convention on the Law of Treaties"
		for match in matches
	)
	assert any(
		match.citation_text == "Article 31"
		and match.normalized_citation == "art. 31 of Vienna Convention on the Law of Treaties"
		for match in matches
	)


def test_extract_statute_reference_matches_rejects_order_prose_and_judgment_paragraphs():
	text = (
		"The Immigration and Refugee Protection Act applies. In order to explain the result, "
		"paragraph 35 of these reasons addresses jurisdiction."
	)

	matches = citations.extract_statute_reference_matches(text)

	assert not any(match.citation_text == "In order" for match in matches)
	assert not any(match.citation_text == "paragraph 35" for match in matches)


def test_extract_statute_reference_matches_supports_named_refugee_instruments():
	text = (
		"Protocol relating to the Status of Refugees, 606 U.N.T.S. 267.\n"
		"Statute of the Office of the United Nations High Commissioner for Refugees, "
		"G.A. Res. 428(V) (1950), s. 7."
	)

	matches = citations.extract_statute_reference_matches(text)

	assert any("Protocol relating to the Status of Refugees" in match.citation_text for match in matches)
	assert any("Statute of the Office of the United Nations High Commissioner for Refugees" in match.citation_text for match in matches)
	assert all(match.kind == "instrument" for match in matches)


def test_extract_raw_citation_matches_supports_article_1fb_variant():
	text = "Article 1FB of the Refugee Convention, Can. T.S. 1969 No. 6 applies."

	matches = citations.extract_raw_citation_matches(text)

	assert any(
		m.kind == "instrument"
		and "art. 1F(b)" in m.normalized_citation
		and "Can. T.S. 1969 No. 6" in m.normalized_citation
		for m in matches
	)


def test_extract_raw_citation_matches_supports_section_of_statute_form():
	text = "Section 7 of the Charter and s. 34(1) of IRPA are engaged."

	matches = citations.extract_raw_citation_matches(text)
	normalized = [m.normalized_citation for m in matches if m.kind == "statute"]

	assert "Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982 s. 7" in normalized
	assert "Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 34(1)" in normalized


def test_extract_raw_citation_matches_preserves_nested_statute_subsections():
	text = "The decision turns on IRPA s. 3(2) (a) and the Charter section 7(1)(b)."

	matches = citations.extract_raw_citation_matches(text)
	normalized = [m.normalized_citation for m in matches if m.kind == "statute"]

	assert "Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 3(2) (a)" in normalized
	assert "Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982 s. 7(1)(b)" in normalized


def test_extract_raw_citation_matches_supports_generic_law_citations():
	text = (
		"Section 18.1 of the Federal Courts Act applies, and section 5(1) of the Citizenship Act, "
		"R.S.C. 1985, c. C-29 is also engaged."
	)

	matches = citations.extract_raw_citation_matches(text)
	normalized = [m.normalized_citation for m in matches if m.kind == "statute"]

	assert any("Federal Courts Act s. 18.1" in item for item in normalized)
	assert any("Citizenship Act, R.S.C. 1985, c. C-29" in item and "s. 5(1)" in item for item in normalized)


def test_extract_raw_citation_matches_supports_immigration_act_punctuation_variant():
	text = "Immigration Act, R.S.C., 1985, c. I-2"

	matches = citations.extract_raw_citation_matches(text)

	assert any(
		m.kind == "statute"
		and m.normalized_citation == "Immigration Act, R.S.C. 1985, c. I-2"
		for m in matches
	)


def test_extract_raw_citation_matches_supports_irpa_plural_section_ranges():
	text = "Under IRPA ss. 100 to 102, 101(1)(f), and 101(2)(b), the claim is ineligible."

	matches = citations.extract_raw_citation_matches(text)
	normalized = [m.normalized_citation for m in matches if m.kind == "statute"]

	assert any(
		item.startswith("Immigration and Refugee Protection Act, S.C. 2001, c. 27 ss. 100 to 102, 101(1)(f), 101(2)(b)")
		for item in normalized
	)


def test_extract_raw_citation_matches_supports_punctuated_irpa_section_variants():
	text = "The claim relies on IRPA, s. 34(1)(f), and IRPR s 245(1)(c)."

	matches = citations.extract_raw_citation_matches(text)
	statutes = [match for match in matches if match.kind == "statute"]

	assert [match.citation_text for match in statutes] == ["IRPA, s. 34(1)(f)", "IRPR s 245(1)(c)"]
	assert statutes[0].normalized_citation == "Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 34(1)(f)"
	assert statutes[1].normalized_citation == "Immigration and Refugee Protection Regulations, SOR/2002-227 s. 245(1)(c)"
	assert all(text[match.offset_start:match.offset_end] == match.citation_text for match in statutes)


def test_extract_raw_citation_matches_supports_irpa_irpr_word_and_undotted_lists():
	text = "IRPA, sections 34 and 37 apply; IRPR, ss 245(1)(c) and 246(1)(a) also apply."

	statutes = [match for match in citations.extract_raw_citation_matches(text) if match.kind == "statute"]

	assert [match.citation_text for match in statutes] == [
		"IRPA, sections 34 and 37",
		"IRPR, ss 245(1)(c) and 246(1)(a)",
	]
	assert statutes[0].normalized_citation.endswith("ss. 34, 37")
	assert statutes[1].normalized_citation.endswith("ss. 245(1)(c), 246(1)(a)")


def test_extract_statute_reference_matches_supports_shared_parent_nested_range():
	text = "The Minister relies on subparagraphs 34(1)(a) to (f) of IRPA."

	matches = citations.extract_statute_reference_matches(text)

	assert any(
		match.citation_text == "subparagraphs 34(1)(a) to (f) of IRPA"
		and match.normalized_citation.endswith("ss. 34(1)(a) to (f)")
		for match in matches
	)


def test_extract_statute_reference_matches_rejects_unanchored_nested_numbers():
	text = "The reasons discuss subparagraphs 34(1)(a) to (f) without naming a statute."

	assert not citations.extract_statute_reference_matches(text)


def test_extract_statute_reference_matches_supports_irpa_paragraph_style_nested_provision():
	text = "The Minister relies on paragraph 34(1)(f) of IRPA."

	matches = citations.extract_statute_reference_matches(text)

	assert any(
		m.kind == "statute"
		and m.citation_text == "paragraph 34(1)(f) of IRPA"
		and m.normalized_citation == "Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 34(1)(f)"
		for m in matches
	)


def test_extract_statute_reference_matches_supports_irpa_prefix_paragraph_style_nested_provision():
	text = "The issue arises under IRPA paragraph 34(1)(f)."

	matches = citations.extract_statute_reference_matches(text)

	assert any(
		m.kind == "statute"
		and m.citation_text == "IRPA paragraph 34(1)(f)"
		and m.normalized_citation == "Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 34(1)(f)"
		for m in matches
	)


def test_extract_statute_reference_matches_supports_bare_nested_irpa_provision_of_form():
	text = "Inadmissibility under 34(1)(f) of IRPA is central to this appeal."

	matches = citations.extract_statute_reference_matches(text)

	assert any(
		m.kind == "statute"
		and m.citation_text == "34(1)(f) of IRPA"
		and m.normalized_citation == "Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 34(1)(f)"
		for m in matches
	)


def test_extract_statute_reference_matches_supports_nested_irpr_provisions_with_exact_spans():
	text = "The officer considered paragraph 245(1)(c) of the IRPR and IRPR s. 228(1)(a) during assessment."

	matches = citations.extract_statute_reference_matches(text)

	irpr_matches = [m for m in matches if "IRPR" in (m.citation_text or "")]
	assert len(irpr_matches) >= 2
	for m in irpr_matches:
		assert text[m.offset_start:m.offset_end] == m.citation_text
		assert m.offset_end > m.offset_start
		assert "245(1)(c)" in m.normalized_citation or "228(1)(a)" in m.normalized_citation


def test_extract_statute_reference_matches_nested_irpa_exact_offsets_and_slices():
	text = "[12] The applicant was found inadmissible pursuant to paragraph 34(1)(f) of IRPA and section 72(1) of the Immigration and Refugee Protection Act."

	matches = citations.extract_statute_reference_matches(text)
	irpa_matches = [m for m in matches if "34(1)(f)" in (m.normalized_citation or "") or "72(1)" in (m.normalized_citation or "")]

	assert len(irpa_matches) == 2
	for m in irpa_matches:
		assert text[m.offset_start:m.offset_end] == m.citation_text
		assert m.kind == "statute"


def test_extract_statute_reference_matches_rejects_non_statute_nested_patterns():
	negative_samples = [
		"The witness referenced paragraph 34(1)(f) of the transcript.",
		"Please refer to Exhibit 34(1)(f) in the affidavit.",
		"Rule 34(1)(f) of Court was discussed during the hearing.",
	]
	for sample in negative_samples:
		matches = citations.extract_statute_reference_matches(sample)
		assert not any("IRPA" in (m.normalized_citation or "") or "IRPR" in (m.normalized_citation or "") for m in matches)


def test_extract_raw_citation_matches_supports_vienna_convention_article_list():
	text = "Articles 31 and 32 of the Vienna Convention on the Law of Treaties guide interpretation."

	matches = citations.extract_raw_citation_matches(text)

	assert any(
		m.kind == "instrument"
		and m.normalized_citation == "arts. 31, 32 of Vienna Convention on the Law of Treaties"
		for m in matches
	)


def test_extract_raw_citation_matches_supports_scr_pinpoint_citation():
	text = "The Court relied on [1994] 3 S.C.R. 551, at pp. 577-78 for the test."

	matches = citations.extract_raw_citation_matches(text)

	assert any(
		m.kind == "secondary"
		and m.normalized_citation == "[1994] 3 S.C.R. 551, at pp. 577-78"
		for m in matches
	)


def test_extract_raw_citation_matches_supports_scr_paragraph_pinpoint_list():
	text = "[2013] 2 S.C.R. 678, at paras. 38 and 101, and Pushpanathan, at paras. 65-66 and 70."

	matches = citations.extract_raw_citation_matches(text)

	assert any(
		m.kind == "secondary"
		and m.normalized_citation == "[2013] 2 S.C.R. 678, at paras. 38 and 101"
		for m in matches
	)
	assert any(
		m.kind == "secondary"
		and m.normalized_citation == "Pushpanathan, at paras. 65-66 and 70"
		for m in matches
	)


def test_extract_raw_citation_matches_supports_pushpanathan_para_short_form():
	text = "Pushpanathan, at para. 57."

	matches = citations.extract_raw_citation_matches(text)

	assert any(
		m.kind == "secondary"
		and m.normalized_citation == "Pushpanathan, at para. 57"
		for m in matches
	)


def test_extract_raw_citation_matches_supports_refugee_convention_article_33_subsection():
	text = "The exception in Article 33(2) applies."

	matches = citations.extract_raw_citation_matches(text)

	assert any(
		m.kind == "instrument"
		and m.normalized_citation == "art. 33(2) of Refugee Convention"
		for m in matches
	)


def test_extract_raw_citation_matches_does_not_capture_bare_charter_term():
	text = "The Charter values at issue are discussed without a specific section."

	matches = citations.extract_raw_citation_matches(text)

	assert not any(m.kind == "statute" and m.normalized_citation == "Charter" for m in matches)


def test_extract_raw_citation_matches_supports_multiword_party_names():
	text = "Applied in R. v. Green Valley Holdings Ltd., 2018 FCA 12."

	matches = citations.extract_raw_citation_matches(text)

	assert len(matches) == 1
	assert matches[0].kind == "case"
	assert matches[0].normalized_citation == "R. v. Green Valley Holdings Ltd., 2018 FCA 12"


def test_extract_raw_citation_matches_supports_short_form_followups():
	text = (
		"See Suresh v. Canada (Minister of Citizenship and Immigration), 2002 SCC 1. "
		"Suresh, at para. 10, is applied."
	)

	matches = citations.extract_raw_citation_matches(text)

	assert len(matches) == 2
	assert matches[0].kind == "case"
	assert matches[0].normalized_citation == "Suresh v. Canada (Minister of Citizenship and Immigration), 2002 SCC 1"
	assert matches[0].pinpoint is None
	assert matches[1].kind == "case_short"
	assert matches[1].normalized_citation == "Suresh v. Canada (Minister of Citizenship and Immigration), 2002 SCC 1, at para. 10"
	assert matches[1].pinpoint == "at para. 10"


def test_extract_raw_citation_matches_preserves_full_case_trailing_pinpoint():
	text = "Suresh v. Canada (Minister of Citizenship and Immigration), 2002 SCC 1, at para. 10 was applied."

	matches = citations.extract_raw_citation_matches(text)
	case_matches = [match for match in matches if match.kind == "case"]

	assert len(case_matches) == 1
	assert case_matches[0].citation_text == "Suresh v. Canada (Minister of Citizenship and Immigration), 2002 SCC 1, at para. 10"
	assert case_matches[0].normalized_citation == "Suresh v. Canada (Minister of Citizenship and Immigration), 2002 SCC 1, at para. 10"
	assert case_matches[0].pinpoint == "at para. 10"


def test_extract_raw_citation_matches_populates_pinpoint_for_full_neutral_citation():
	text = "The Court applied 2019 SCC 65 at para 100."

	matches = citations.extract_raw_citation_matches(text)

	neutral_matches = [match for match in matches if match.kind == "neutral"]
	assert len(neutral_matches) == 1
	assert neutral_matches[0].citation_text == "2019 SCC 65 at para 100"
	assert neutral_matches[0].pinpoint == "at para. 100"


def test_extract_raw_citation_matches_populates_pinpoint_for_short_form_range():
	text = "Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65. Vavilov at paras 10-12."

	matches = citations.extract_raw_citation_matches(text)

	short_matches = [match for match in matches if match.kind == "case_short"]
	assert len(short_matches) == 1
	assert short_matches[0].citation_text == "Vavilov at paras 10-12"
	assert short_matches[0].pinpoint == "at paras. 10-12"


def test_extract_raw_citation_matches_preserves_case_trailing_reporter_and_pinpoint():
	text = (
		"Febles v. Canada (Citizenship and Immigration), 2014 SCC 68, [2014] 3 S.C.R. 431, at para. 94 "
		"was cited."
	)

	matches = citations.extract_raw_citation_matches(text)
	case_matches = [match for match in matches if match.kind == "case"]

	assert len(case_matches) == 1
	assert case_matches[0].citation_text == (
		"Febles v. Canada (Citizenship and Immigration), 2014 SCC 68, [2014] 3 S.C.R. 431, at para. 94"
	)
	assert case_matches[0].normalized_citation == (
		"Febles v. Canada (Citizenship and Immigration), 2014 SCC 68, [2014] 3 S.C.R. 431, at para. 94"
	)


def test_extract_raw_citation_matches_preserves_parenthesized_year_reporter():
	text = "In Baroud v. Canada (1998), 160 F.T.R. 91, the Court considered the delay."

	matches = citations.extract_raw_citation_matches(text)
	case_matches = [match for match in matches if match.kind == "case_name"]

	assert len(case_matches) == 1
	assert case_matches[0].citation_text == "Baroud v. Canada (1998), 160 F.T.R. 91"
	assert case_matches[0].normalized_citation == "Baroud v. Canada, (1998), 160 F.T.R. 91"


def test_extract_raw_citation_matches_supports_case_short_multi_para_lists():
	text = (
		"Canada (Citizenship and Immigration) v. Jayasekara, 2008 FCA 404. "
		"Febles v. Canada (Citizenship and Immigration), 2014 SCC 68. "
		"Jayasekara at paras 37 and 44. "
		"Febles at para 62. "
		"Jayasekara at para 55; and Febles at para 62."
	)

	matches = citations.extract_raw_citation_matches(text)
	short_matches = [m for m in matches if m.kind == "case_short"]

	assert any(m.citation_text == "Jayasekara at paras 37 and 44" for m in short_matches)
	assert any(m.citation_text == "Febles at para 62" for m in short_matches)
	assert any(m.citation_text == "Jayasekara at para 55" for m in short_matches)


def test_extract_case_citations_handles_chained_cases_with_bracket_aliases():
	text = (
		"The RAD relied on Jayasekara v Canada (Minister of Citizenship and Immigration), "
		"2008 FCA 404 [Jayasekara] and Febles v Canada (Citizenship and Immigration), "
		"2014 SCC 68 [Febles]. Jayasekara at paras 37 and 44. Febles at para 62."
	)

	matches = citations.extract_case_citation_matches(text)

	assert any(
		m.kind == "case"
		and m.citation_text
		== "Jayasekara v Canada (Minister of Citizenship and Immigration), 2008 FCA 404"
		for m in matches
	)
	assert any(
		m.kind == "case"
		and m.citation_text
		== "Febles v Canada (Citizenship and Immigration), 2014 SCC 68"
		for m in matches
	)
	assert any(
		m.kind == "case_short"
		and m.citation_text == "Jayasekara at paras 37 and 44"
		and m.normalized_citation
		== "Jayasekara v. Canada (Minister of Citizenship and Immigration), 2008 FCA 404, at paras. 37 and 44"
		for m in matches
	)


def test_extract_raw_citation_matches_supports_case_short_paragraph_wording():
	text = (
		"Canada (Citizenship and Immigration) v. Jayasekara, 2008 FCA 404. "
		"Jayasekara at paragraph 24. Jayasekara at paragraph 26."
	)

	matches = citations.extract_raw_citation_matches(text)
	short_matches = [m for m in matches if m.kind == "case_short"]

	assert any(m.citation_text == "Jayasekara at paragraph 24" for m in short_matches)
	assert any(m.citation_text == "Jayasekara at paragraph 26" for m in short_matches)


def test_extract_case_citations_captures_paragraph_ranges_and_page_pinpoints():
	text = (
		"Vavilov v Canada, 2019 SCC 65. "
		"Vavilov at para 100; Vavilov at para. 101; "
		"Vavilov at paragraph 102; Vavilov at paras 10-12; "
		"Vavilov at paragraphs 20 to 22; Vavilov at p. 100; "
		"Vavilov at pp. 100-102."
	)

	matches = citations.extract_case_citation_matches(text)
	short_matches = [match for match in matches if match.kind == "case_short"]

	assert [match.pinpoint for match in short_matches] == [
		"at para. 100",
		"at para. 101",
		"at para. 102",
		"at paras. 10-12",
		"at paras. 20 to 22",
		"at p. 100",
		"at pp. 100-102",
	]
	assert [match.citation_text for match in short_matches] == [
		"Vavilov at para 100",
		"Vavilov at para. 101",
		"Vavilov at paragraph 102",
		"Vavilov at paras 10-12",
		"Vavilov at paragraphs 20 to 22",
		"Vavilov at p. 100",
		"Vavilov at pp. 100-102",
	]


def test_extract_case_citations_preserves_anchor_provenance_for_duplicate_short_names():
	text = (
		"Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 "
		"sets the framework. Vavilov applies. Vavilov applies again."
	)
	anchor_start = text.index("Canada")
	anchor_end = text.index(" sets", anchor_start)
	anchor_text = text[anchor_start:anchor_end]

	matches = citations.extract_case_citation_matches(text)
	short_matches = [match for match in matches if match.kind == "case_short" and match.citation_text == "Vavilov"]

	assert len(short_matches) == 2
	assert [match.offset_start for match in short_matches] == [text.index("Vavilov", anchor_end), text.rindex("Vavilov")]
	assert all(match.anchor_citation_text == anchor_text for match in short_matches)
	assert all(match.anchor_offset_start == anchor_start for match in short_matches)
	assert all(match.anchor_offset_end == anchor_end for match in short_matches)


def test_extract_case_citations_leaves_unanchored_short_name_provenance_empty():
	matches = citations.extract_case_citation_matches("The tribunal discussed Vavilov without a full citation.")

	assert not any(match.kind == "case_short" and match.citation_text == "Vavilov" for match in matches)


def test_extract_raw_citation_matches_supports_standalone_case_name_without_neutral():
	text = "The panel relied on Nava AGUILAR v CANADA in its reasoning."

	matches = citations.extract_raw_citation_matches(text)

	assert any(
		m.kind == "case_name"
		and m.normalized_citation == "Nava AGUILAR v. CANADA"
		for m in matches
	)


def test_extract_raw_citation_matches_trims_narrative_prefix_from_case_name():
	text = "As noted by John Norris in Nava Aguilar v Canada (Citizenship and Immigration), 2024 FC 1714."

	matches = citations.extract_raw_citation_matches(text)

	assert any(
		m.kind == "case"
		and m.normalized_citation == "Nava Aguilar v. Canada (Citizenship and Immigration), 2024 FC 1714"
		for m in matches
	)


def test_extract_raw_citation_matches_ignores_narrative_prefix_before_case_name():
	text = (
		"The Court may disregard argumentative affidavit passages "
		"(Ray v Canada, 2003 FCA 317)."
	)

	matches = citations.extract_raw_citation_matches(text)

	assert len(matches) == 1
	assert matches[0].kind == "case"
	assert matches[0].normalized_citation == "Ray v. Canada, 2003 FCA 317"


def test_extract_raw_citation_matches_strips_judge_name_from_parenthetical_case():
	text = (
		"Justice Ahmed (Gnanapragasam v Canada (Public Safety and Emergency Preparedness), "
		"2023 FC 1735) explained the point."
	)

	matches = citations.extract_raw_citation_matches(text)

	assert any(
		m.kind == "case"
		and m.normalized_citation == "Gnanapragasam v. Canada (Public Safety and Emergency Preparedness), 2023 FC 1735"
		for m in matches
	)


def test_extract_raw_citation_matches_short_form_does_not_capture_trailing_prose():
	text = (
		"Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 was applied. "
		"Vavilov at para 10). The Minister adds that the outcome is unchanged."
	)

	matches = citations.extract_raw_citation_matches(text)
	short_matches = [m for m in matches if m.kind == "case_short"]

	assert len(short_matches) == 1
	assert short_matches[0].citation_text == "Vavilov at para 10"
	assert "The Minister" not in short_matches[0].citation_text


def test_extract_case_citations_highlights_bare_alias_after_full_citation():
	text = (
		"Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 "
		"sets the framework. The Court applied Vavilov. Vavilov also requires "
		"responsive reasons. Mr V gave evidence."
	)

	matches = citations.extract_case_citation_matches(text)
	bare_vavilov = [
		m
		for m in matches
		if m.kind == "case_short" and m.citation_text == "Vavilov"
	]

	assert len(bare_vavilov) == 2
	assert all(
		m.normalized_citation
		== "Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65"
		for m in bare_vavilov
	)
	assert not any(m.citation_text == "Mr V" for m in matches)


def test_extract_case_citations_does_not_promote_narrative_words_from_case_name_span():
	text = (
		"The claimant was excluded from the Refugee Convention on the basis of grave "
		"criminal conduct (X v Commissaire). The evidence came from another source, "
		"and the conduct was later discussed."
	)

	matches = citations.extract_case_citation_matches(text)

	assert any(
		m.kind == "case_name" and m.citation_text == "X v Commissaire"
		for m in matches
	)
	assert not any(
		m.kind == "case_short" and m.citation_text.lower() in {"from", "conduct"}
		for m in matches
	)


def test_extract_case_citations_captures_complete_parenthetical_short_citation():
	text = (
		"Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 "
		"sets the framework. The decision must be justified (Vavilov at para 100)."
	)

	matches = citations.extract_case_citation_matches(text)

	assert any(
		m.kind == "case_short"
		and m.citation_text == "(Vavilov at para 100)"
		and text[m.offset_start:m.offset_end] == "(Vavilov at para 100)"
		for m in matches
	)


def test_extract_case_citations_captures_single_parenthetical_prefix_and_editorial_note():
	text = (
		"Febles v Canada (Citizenship and Immigration), 2014 SCC 68 applies. "
		"The exclusion is narrow (cf. Febles at para 62). "
		"The framework controls (Febles at para 84, internal quotation marks deleted)."
	)

	matches = citations.extract_case_citation_matches(text)
	short_texts = {m.citation_text for m in matches if m.kind == "case_short"}

	assert "(cf. Febles at para 62)" in short_texts
	assert "(Febles at para 84, internal quotation marks deleted)" in short_texts


def test_extract_case_citations_keeps_multi_authority_parenthetical_spans_separate():
	text = (
		"Jayasekara v Canada (Minister of Citizenship and Immigration), 2008 FCA 404 and "
		"Febles v Canada (Citizenship and Immigration), 2014 SCC 68 apply "
		"(Jayasekara at para 55; and Febles at para 62)."
	)

	matches = citations.extract_case_citation_matches(text)
	short_texts = {m.citation_text for m in matches if m.kind == "case_short"}

	assert "Jayasekara at para 55" in short_texts
	assert "Febles at para 62" in short_texts


def test_extract_raw_citation_matches_generic_short_form_prefers_anchor_and_rejects_fragments():
	text = (
		"Sharma v. Canada (Minister of Public Safety and Emergency Preparedness), 2016 FCA 319 sets the framework. "
		"The factors and, at para 70, are discussed. In Sharma, at para 34, the Court explained why. "
		"The assessment must be reasonable in the circumstances, at para 70."
	)

	matches = citations.extract_raw_citation_matches(text)
	short_matches = [m for m in matches if m.kind == "case_short"]

	assert any(m.citation_text == "Sharma, at para 34" for m in short_matches)
	assert any(
		m.normalized_citation
		== "Sharma v. Canada (Minister of Public Safety and Emergency Preparedness), 2016 FCA 319, at para. 34"
		for m in short_matches
	)
	assert not any("factors and" in m.citation_text for m in short_matches)
	assert not any("reasonable in the circumstances" in m.citation_text for m in short_matches)


def test_extract_raw_citation_matches_does_not_leak_bracket_alias_to_next_case():
	text = (
		"Penner v Niagara (Regional Police Services Board), 2013 SCC 19 [Penner], "
		"and Exeter v Canada (Attorney General), 2012 FCA 119 [Exeter]. "
		"Exeter at para 6 applies."
	)

	matches = citations.extract_raw_citation_matches(text)
	short_matches = [m for m in matches if m.kind == "case_short"]

	assert any(m.citation_text == "Exeter at para 6" for m in short_matches)
	assert any(
		m.citation_text == "Exeter at para 6"
		and m.normalized_citation == "Exeter v. Canada (Attorney General), 2012 FCA 119, at para. 6"
		for m in short_matches
	)


def test_extract_raw_citation_matches_binds_alias_to_immediately_preceding_case():
	text = (
		"Samuel v Canada (Citizenship and Immigration), 2019 FC 227 at para 17. "
		"The Respondent cites Shackleford v Canada (Citizenship and Immigration), "
		"2019 FC 1313 [Shackleford]. Shackleford at para 12 applies."
	)

	matches = citations.extract_case_citation_matches(text)
	short_matches = [m for m in matches if m.kind == "case_short"]

	assert any(
		m.citation_text == "Shackleford at para 12"
		and m.normalized_citation
		== "Shackleford v. Canada (Citizenship and Immigration), 2019 FC 1313, at para. 12"
		for m in short_matches
	)
	assert not any(
		m.citation_text == "Shackleford at para 12"
		and m.normalized_citation
		== "Samuel v. Canada (Citizenship and Immigration), 2019 FC 227"
		for m in short_matches
	)


def test_extract_raw_citation_matches_prefers_company_name_over_suffix_start():
	text = (
		"As described in Jennings-Clyde, Inc (Vivatas, Inc) v Canada (Attorney General), 2024 FC 1141 "
		"[Jennings-Clyde] at paragraph 39. Jennings-Clyde at para 40 follows."
	)

	matches = citations.extract_raw_citation_matches(text)
	full_cases = [m for m in matches if m.kind == "case"]
	short_matches = [m for m in matches if m.kind == "case_short"]

	assert any(
		m.normalized_citation == "Jennings-Clyde, Inc (Vivatas, Inc) v. Canada (Attorney General), 2024 FC 1141"
		for m in full_cases
	)
	assert any(
		m.citation_text == "Jennings-Clyde at para 40"
		and m.normalized_citation
		== "Jennings-Clyde, Inc (Vivatas, Inc) v. Canada (Attorney General), 2024 FC 1141, at para. 40"
		for m in short_matches
	)


def test_rebuild_stores_each_inline_case_name_with_chunk_location(monkeypatch):
	section_1 = "Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 sets the framework."
	section_2 = "Vavilov explains the first issue. Vavilov also controls the second issue."
	full_text = f"{section_1}\n{section_2}"
	case = SimpleNamespace(id=11, full_text=full_text, summary=None)
	chunks = [
		SimpleNamespace(id=101, chunk_set="section", chunk_index=0, text=section_1),
		SimpleNamespace(id=102, chunk_set="section", chunk_index=1, text=section_2),
	]

	class RebuildSession:
		def __init__(self):
			self.added = []

		def execute(self, statement):
			return None

		def add_all(self, rows):
			self.added.extend(rows)

	def fail_if_resolved(*_args, **_kwargs):
		raise AssertionError("extraction must not resolve targets")

	monkeypatch.setattr(citations, "resolve_neutral_to_case_id", fail_if_resolved)
	session = RebuildSession()

	inserted = citations.rebuild_citations_for_case(session, case, chunks)
	inline_rows = [row for row in session.added if row.citation_text == "Vavilov"]

	assert inserted == 3
	assert len(inline_rows) == 2
	assert all(row.citation_kind == "case_short" for row in inline_rows)
	assert all(row.target_case_id is None for row in inline_rows)
	assert all(row.unresolved for row in inline_rows)
	assert all(row.chunk_id == 102 for row in inline_rows)
	assert [section_2[row.offset_start:row.offset_end] for row in inline_rows] == ["Vavilov", "Vavilov"]
	assert inline_rows[0].offset_start != inline_rows[1].offset_start


def test_citation_endpoints_return_rows_and_metrics():
	case = SimpleNamespace(id=10)
	citation = SimpleNamespace(
		id=1,
		source_case_id=10,
		target_case_id=20,
		citation_text="2024 FC 100",
		normalized_citation="2024 FC 100",
		chunk_id=None,
		offset_start=4,
		offset_end=14,
		unresolved=False,
	)
	metrics = SimpleNamespace(case_id=10, in_degree=2, out_degree=3, pagerank=0.25)

	outgoing_db = FakeDatabase(rows=[(citation,)], scalar_value=[case])
	outgoing = routes.get_case_outgoing_citations(10, outgoing_db)

	assert outgoing[0].source_case_id == 10
	assert outgoing[0].target_case_id == 20
	assert outgoing[0].normalized_citation == "2024 FC 100"

	metrics_db = FakeDatabase(scalar_value=[case, metrics])
	result = routes.get_case_citation_metrics(10, metrics_db)

	assert result.case_id == 10
	assert result.in_degree == 2
	assert result.out_degree == 3
	assert result.pagerank == 0.25


def test_citation_map_endpoints_delegate_with_bounded_parameters(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case, case, case])
	calls = {}

	monkeypatch.setattr(routes, "_citation_map_summary", lambda db: {"database": db})
	monkeypatch.setattr(
		routes,
		"_top_authorities",
		lambda db, limit: calls.update(authorities=(db, limit)) or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_neighborhood",
		lambda db, focus, limit: calls.update(neighborhood=(db, focus.id, limit)) or {},
	)
	monkeypatch.setattr(
		routes,
		"_similar_cases_by_authority",
		lambda db, case_id, limit, min_shared: calls.update(
			similar=(db, case_id, limit, min_shared)
		) or [],
	)
	monkeypatch.setattr(
		routes,
		"_co_cited_authorities",
		lambda db, case_id, limit: calls.update(co_cited=(db, case_id, limit)) or [],
	)

	assert routes.get_citation_map_summary(database) == {"database": database}
	routes.get_citation_map_authorities(limit=999, db=database)
	routes.get_citation_map_neighborhood(10, limit=999, db=database)
	routes.get_citation_map_similar_cases(10, limit=999, min_shared=999, db=database)
	routes.get_citation_map_co_cited_authorities(10, limit=999, db=database)

	assert calls["authorities"] == (database, 200)
	assert calls["neighborhood"] == (database, 10, 500)
	assert calls["similar"] == (database, 10, 100, 50)
	assert calls["co_cited"] == (database, 10, 100)


def test_citation_map_case_search_and_authority_map_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case])
	calls = {}

	monkeypatch.setattr(
		routes,
		"_search_citation_cases",
		lambda db, query, limit: calls.update(search=(db, query, limit)) or [],
	)
	monkeypatch.setattr(
		routes,
		"_case_authority_map",
		lambda db, focus, limit: calls.update(authority_map=(db, focus.id, limit)) or {},
	)

	routes.search_citation_map_cases(q="Vavilov", limit=999, db=database)
	routes.get_case_authority_map(10, limit=999, db=database)

	assert calls["search"] == (database, "Vavilov", 30)
	assert calls["authority_map"] == (database, 10, 12)
	assert routes.case_reader_page().headers["location"] == "/data-explorer"
	assert routes.case_reader_page(6617).headers["location"] == "/data-explorer?case_id=6617"


def test_citation_map_issue_and_evidence_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case, case, case, case])
	calls = {}
	context = {
		"citation_id": 1,
		"source_case_id": 10,
		"source_title": "Source",
		"source_citation": "2024 FC 10",
		"target_case_id": 20,
		"target_title": "Target",
		"target_citation": "2019 SCC 65",
		"chunk_id": 3,
		"chunk_index": 0,
		"citation_text": "Vavilov",
		"normalized_citation": "2019 SCC 65",
		"offset_start": 4,
		"offset_end": 12,
		"context_start": 0,
		"context_end": 18,
		"context": "See Vavilov here.",
	}

	monkeypatch.setattr(routes, "_citation_map_topics", lambda db, query, limit: calls.update(topics=(db, query, limit)) or [])
	monkeypatch.setattr(routes, "_citation_issue_map", lambda db, category, value, limit: calls.update(issue=(db, category, value, limit)) or {})
	monkeypatch.setattr(routes, "_case_legal_tags", lambda db, case_id, limit: calls.update(tags=(db, case_id, limit)) or [])
	monkeypatch.setattr(routes, "_common_citing_cases", lambda db, case_ids, limit: calls.update(common=(db, case_ids, limit)) or [])
	monkeypatch.setattr(routes, "_citation_contexts", lambda db, source, target, limit: calls.update(context=(db, source, target, limit)) or [context])

	routes.get_citation_map_topics(q="fairness", limit=999, db=database)
	routes.get_citation_issue_map(category="issue", value="procedural_fairness", limit=999, db=database)
	routes.get_citation_map_case_tags(10, limit=999, db=database)
	routes.get_common_citing_cases(case_ids="10,20,10", limit=999, db=database)
	response = routes.export_citation_contexts(10, 20, db=database)

	assert calls["topics"] == (database, "fairness", 250)
	assert calls["issue"] == (database, "issue", "procedural_fairness", 200)
	assert calls["tags"] == (database, 10, 250)
	assert calls["common"] == (database, [10, 20], 200)
	assert calls["context"] == (database, 10, 20, 200)
	assert response.media_type == "text/csv; charset=utf-8"
	assert response.headers["content-disposition"] == 'attachment; filename="citation-context-10-to-20.csv"'
	assert b"See Vavilov here." in response.body

	with pytest.raises(HTTPException) as unsupported:
		routes.get_citation_issue_map(category="outcome", value="allowed", db=database)
	assert unsupported.value.status_code == 422

	with pytest.raises(HTTPException) as too_few:
		routes.get_common_citing_cases(case_ids="10", db=database)
	assert too_few.value.status_code == 422


def test_citation_paths_and_edge_summary_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case, case, case, case])
	calls = {}
	summary = {
		"source_case": {
			"case_id": 10,
			"title": "Source",
			"citation": "2024 FC 10",
			"court": "FC",
			"date": "2024-01-01",
			"in_degree": 1,
			"out_degree": 2,
			"pagerank": None,
		},
		"target_case": {
			"case_id": 20,
			"title": "Target",
			"citation": "2019 SCC 65",
			"court": "SCC",
			"date": "2019-01-01",
			"in_degree": 5,
			"out_degree": 0,
			"pagerank": None,
		},
		"occurrence_count": 3,
		"distinct_chunks": 2,
		"first_chunk_index": 1,
		"last_chunk_index": 4,
		"top_normalized_citations": [{"normalized_citation": "2019 SCC 65", "occurrences": 3}],
		"sample_contexts": [],
	}

	monkeypatch.setattr(
		routes,
		"_citation_paths",
		lambda db, source_case_id, target_case_id, max_hops, limit, per_node_limit: calls.update(
			paths=(db, source_case_id, target_case_id, max_hops, limit, per_node_limit)
		) or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_edge_summary",
		lambda db, source_case_id, target_case_id, context_limit, variant_limit: calls.update(
			summary=(db, source_case_id, target_case_id, context_limit, variant_limit)
		) or summary,
	)

	routes.get_citation_paths(source_case_id=10, target_case_id=20, max_hops=999, limit=999, per_node_limit=1, db=database)
	routes.get_citation_edge_summary(source_case_id=10, target_case_id=20, context_limit=999, variant_limit=0, db=database)

	assert calls["paths"] == (database, 10, 20, 6, 25, 5)
	assert calls["summary"] == (database, 10, 20, 20, 1)


def test_advanced_citation_analytics_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case, case, case, case, case])
	calls = {}

	replacement = {
		"old_authority": {
			"case_id": 10,
			"title": "Old",
			"citation": "2002 SCC 1",
			"court": "SCC",
			"date": "2002-01-01",
			"in_degree": 1,
			"out_degree": 1,
			"pagerank": None,
		},
		"new_authority": {
			"case_id": 20,
			"title": "New",
			"citation": "2019 SCC 65",
			"court": "SCC",
			"date": "2019-01-01",
			"in_degree": 5,
			"out_degree": 1,
			"pagerank": None,
		},
		"replacement_score": 1.1,
		"status": "replacement_likely",
		"series": [],
	}

	monkeypatch.setattr(
		routes,
		"_citation_contextual_paths",
		lambda db, source_case_id, target_case_id, max_hops, limit, per_node_limit, hop_context_limit: calls.update(
			contextual_paths=(db, source_case_id, target_case_id, max_hops, limit, per_node_limit, hop_context_limit)
		) or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_authority_signals",
		lambda db, case_id, limit, context_limit: calls.update(signals=(db, case_id, limit, context_limit)) or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_replacement_trend",
		lambda db, old_case_id, new_case_id, start_year, end_year: calls.update(
			replacement=(db, old_case_id, new_case_id, start_year, end_year)
		) or replacement,
	)
	monkeypatch.setattr(
		routes,
		"_citation_landmark_candidates",
		lambda db, limit, recent_years, baseline_years, min_recent: calls.update(
			landmarks=(db, limit, recent_years, baseline_years, min_recent)
		) or [],
	)

	routes.get_contextual_citation_paths(
		source_case_id=10,
		target_case_id=20,
		max_hops=999,
		limit=999,
		per_node_limit=1,
		hop_context_limit=99,
		db=database,
	)
	routes.get_citation_authority_signals(case_id=10, limit=999, context_limit=0, db=database)
	routes.get_citation_replacement_trend(old_case_id=10, new_case_id=20, start_year=2010, end_year=2020, db=database)
	routes.get_citation_landmark_candidates(limit=999, recent_years=99, baseline_years=99, min_recent=0, db=database)

	assert calls["contextual_paths"] == (database, 10, 20, 6, 25, 5, 5)
	assert calls["signals"] == (database, 10, 80, 1)
	assert calls["replacement"] == (database, 10, 20, 2010, 2020)
	assert calls["landmarks"] == (database, 100, 10, 20, 1)

	with pytest.raises(HTTPException) as same_case:
		routes.get_citation_replacement_trend(old_case_id=10, new_case_id=10, db=database)
	assert same_case.value.status_code == 422

	with pytest.raises(HTTPException) as bad_years:
		routes.get_citation_replacement_trend(old_case_id=10, new_case_id=20, start_year=2025, end_year=2020, db=database)
	assert bad_years.value.status_code == 422


def test_case_batch_extraction_advances_by_primary_key(monkeypatch):
	cases = [SimpleNamespace(id=4), SimpleNamespace(id=9)]
	session = QueuedScalarsSession([cases, []])
	processed = []
	monkeypatch.setattr(
		citations,
		"rebuild_citations_for_case",
		lambda _session, case, chunks=None: processed.append(case.id) or 1,
	)

	inserted = citations.batch_extract_citations_from_cases(session, batch_size=2)

	assert inserted == 2
	assert processed == [4, 9]
	assert session.commits == 1


def test_chunk_batch_rebuilds_each_case_with_all_chunks(monkeypatch):
	case_4 = SimpleNamespace(id=4)
	case_9 = SimpleNamespace(id=9)
	chunks = [
		SimpleNamespace(id=1, case_id=4, chunk_index=0),
		SimpleNamespace(id=2, case_id=4, chunk_index=1),
		SimpleNamespace(id=3, case_id=9, chunk_index=0),
	]
	session = QueuedScalarsSession([[4, 9], chunks, [case_4, case_9], []])
	processed = []
	monkeypatch.setattr(
		citations,
		"rebuild_citations_for_case",
		lambda _session, case, case_chunks=None: processed.append(
			(case.id, [chunk.id for chunk in case_chunks or []])
		) or len(case_chunks or []),
	)

	inserted = citations.batch_extract_citations_from_chunks(session, batch_size=2)

	assert inserted == 3
	assert processed == [(4, [1, 2]), (9, [3])]
	assert session.commits == 1


def test_surprise_feed_endpoints_are_bounded(monkeypatch):
	database = FakeDatabase()
	calls = {}

	monkeypatch.setattr(
		routes,
		"_citation_surprise_feed",
		lambda db, category, value, start_year, end_year, limit, min_occurrences: calls.update(
			surprises=(db, category, value, start_year, end_year, limit, min_occurrences)
		)
		or [],
	)

	routes.get_citation_surprises(
		category="issue",
		value="Detention",
		start_year=2010,
		end_year=2024,
		limit=999,
		min_occurrences=0,
		db=database,
	)

	assert calls["surprises"] == (database, "issue", "Detention", 2010, 2024, 250, 1)

	with pytest.raises(HTTPException) as missing_pair:
		routes.get_citation_surprises(category="issue", value=None, db=database)
	assert missing_pair.value.status_code == 422

	with pytest.raises(HTTPException) as unsupported:
		routes.get_citation_surprises(category="procedure", value="x", db=database)
	assert unsupported.value.status_code == 422

	with pytest.raises(HTTPException) as bad_years:
		routes.get_citation_surprises(start_year=2025, end_year=2020, db=database)
	assert bad_years.value.status_code == 422


def test_doctrine_shift_endpoints_are_bounded(monkeypatch):
	database = FakeDatabase()
	calls = {}

	monkeypatch.setattr(
		routes,
		"_citation_doctrine_shifts",
		lambda db, category, value, limit, candidate_limit, start_year, end_year: calls.update(
			shifts=(db, category, value, limit, candidate_limit, start_year, end_year)
		)
		or [],
	)

	routes.get_citation_doctrine_shifts(
		category="issue",
		value="Detention",
		limit=999,
		candidate_limit=1,
		start_year=2005,
		end_year=2024,
		db=database,
	)

	assert calls["shifts"] == (database, "issue", "Detention", 50, 4, 2005, 2024)

	with pytest.raises(HTTPException) as unsupported:
		routes.get_citation_doctrine_shifts(category="outcome", value="Allowed", db=database)
	assert unsupported.value.status_code == 422

	with pytest.raises(HTTPException) as bad_years:
		routes.get_citation_doctrine_shifts(category="issue", value="Detention", start_year=2024, end_year=2020, db=database)
	assert bad_years.value.status_code == 422


def test_hidden_bridge_and_inheritance_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	other_case = SimpleNamespace(id=20)
	database = FakeDatabase(scalar_value=[case, other_case, case])
	calls = {}

	monkeypatch.setattr(
		routes,
		"_citation_hidden_bridges",
		lambda db, source_case_id, target_case_id, max_hops, path_limit, per_node_limit, bridge_limit: calls.update(
			hidden=(db, source_case_id, target_case_id, max_hops, path_limit, per_node_limit, bridge_limit)
		)
		or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_inheritance_chains",
		lambda db, case_id, max_depth, limit, per_node_limit, min_occurrences: calls.update(
			inheritance=(db, case_id, max_depth, limit, per_node_limit, min_occurrences)
		)
		or [],
	)

	routes.get_hidden_citation_bridges(
		source_case_id=10,
		target_case_id=20,
		max_hops=999,
		path_limit=999,
		per_node_limit=1,
		limit=999,
		db=database,
	)
	routes.get_citation_inheritance_chains(
		case_id=10,
		max_depth=99,
		limit=999,
		per_node_limit=0,
		min_occurrences=0,
		db=database,
	)

	assert calls["hidden"] == (database, 10, 20, 8, 40, 5, 60)
	assert calls["inheritance"] == (database, 10, 6, 60, 1, 1)

	with pytest.raises(HTTPException) as same_case:
		routes.get_hidden_citation_bridges(source_case_id=10, target_case_id=10, db=database)
	assert same_case.value.status_code == 422


def test_missing_authority_lifecycle_and_court_flow_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	database = FakeDatabase(scalar_value=[case])
	calls = {}

	monkeypatch.setattr(
		routes,
		"_citation_missing_authorities",
		lambda db, case_id, peer_limit, result_limit, min_peer_share, min_peer_citations: calls.update(
			missing=(db, case_id, peer_limit, result_limit, min_peer_share, min_peer_citations)
		)
		or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_authority_lifecycle",
		lambda db, category, value, start_year, end_year, limit, recent_years, prior_years: calls.update(
			lifecycle=(db, category, value, start_year, end_year, limit, recent_years, prior_years)
		)
		or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_cross_court_flow",
		lambda db, start_year, end_year, limit: calls.update(flow=(db, start_year, end_year, limit)) or [],
	)

	routes.get_citation_missing_authorities(
		case_id=10,
		peer_limit=999,
		limit=999,
		min_peer_share=0.25,
		min_peer_citations=0,
		db=database,
	)
	routes.get_citation_authority_lifecycle(
		category="issue",
		value="Detention",
		start_year=2001,
		end_year=2024,
		limit=999,
		recent_years=99,
		prior_years=99,
		db=database,
	)
	routes.get_citation_cross_court_flow(start_year=2010, end_year=2024, limit=999, db=database)

	assert calls["missing"] == (database, 10, 200, 100, 0.25, 1)
	assert calls["lifecycle"] == (database, "issue", "Detention", 2001, 2024, 120, 10, 10)
	assert calls["flow"] == (database, 2010, 2024, 200)

	with pytest.raises(HTTPException) as invalid_share:
		routes.get_citation_missing_authorities(case_id=10, min_peer_share=1.2, db=database)
	assert invalid_share.value.status_code == 422

	with pytest.raises(HTTPException) as invalid_pair:
		routes.get_citation_authority_lifecycle(category="issue", value=None, db=database)
	assert invalid_pair.value.status_code == 422

	with pytest.raises(HTTPException) as invalid_flow_years:
		routes.get_citation_cross_court_flow(start_year=2025, end_year=2020, db=database)
	assert invalid_flow_years.value.status_code == 422


def test_position_completion_and_shift_dashboard_endpoints_are_bounded(monkeypatch):
	case = SimpleNamespace(id=10)
	other_case = SimpleNamespace(id=20)
	database = FakeDatabase(scalar_value=[case, case, other_case])
	calls = {}

	monkeypatch.setattr(
		routes,
		"_citation_position_profiles",
		lambda db, case_id, limit, min_occurrences: calls.update(
			positions=(db, case_id, limit, min_occurrences)
		)
		or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_completion_suggestions",
		lambda db, case_id, peer_limit, limit, min_peer_share, min_peer_citations: calls.update(
			completion=(db, case_id, peer_limit, limit, min_peer_share, min_peer_citations)
		)
		or [],
	)
	monkeypatch.setattr(
		routes,
		"_citation_shift_dashboard",
		lambda db, category, value, start_year, end_year, replacement_limit, lifecycle_limit, surprise_limit: calls.update(
			dashboard=(db, category, value, start_year, end_year, replacement_limit, lifecycle_limit, surprise_limit)
		)
		or {
			"category": category,
			"value": value,
			"replacement_candidates": [],
			"emerging_authorities": [],
			"declining_authorities": [],
			"surprises": [],
		},
	)

	routes.get_citation_position_profiles(case_id=10, limit=999, min_occurrences=0, db=database)
	routes.get_citation_completion_suggestions(case_id=10, peer_limit=999, limit=999, min_peer_share=0.4, min_peer_citations=0, db=database)
	routes.get_citation_shift_dashboard(
		category="issue",
		value="Detention",
		start_year=2001,
		end_year=2024,
		replacement_limit=999,
		lifecycle_limit=1,
		surprise_limit=999,
		db=database,
	)

	assert calls["positions"] == (database, 10, 120, 1)
	assert calls["completion"] == (database, 10, 200, 100, 0.4, 1)
	assert calls["dashboard"] == (database, "issue", "Detention", 2001, 2024, 30, 5, 200)

	with pytest.raises(HTTPException) as invalid_share:
		routes.get_citation_completion_suggestions(case_id=10, min_peer_share=-0.2, db=database)
	assert invalid_share.value.status_code == 422

	with pytest.raises(HTTPException) as bad_category:
		routes.get_citation_shift_dashboard(category="outcome", value="Allowed", db=database)
	assert bad_category.value.status_code == 422

	with pytest.raises(HTTPException) as bad_years:
		routes.get_citation_shift_dashboard(category="issue", value="Detention", start_year=2025, end_year=2020, db=database)
	assert bad_years.value.status_code == 422


def test_new_csv_exports_include_expected_headers(monkeypatch):
	database = FakeDatabase(scalar_value=[SimpleNamespace(id=1), SimpleNamespace(id=1), SimpleNamespace(id=2), SimpleNamespace(id=1), SimpleNamespace(id=1), SimpleNamespace(id=1), SimpleNamespace(id=1), SimpleNamespace(id=1), SimpleNamespace(id=1)])

	monkeypatch.setattr(
		routes,
		"_citation_authority_signals",
		lambda db, case_id, limit, context_limit: [
			{
				"authority": {
					"case_id": 2,
					"title": "Authority",
					"citation": "2019 SCC 65",
					"court": "SCC",
					"date": "2019-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"occurrence_count": 3,
				"distinct_chunks": 2,
				"gravity_share": 0.2,
				"global_citing_cases": 4,
				"surprise_score": 0.3,
				"originality_score": 0.4,
				"boilerplate_hits": 1,
				"first_chunk_index": 0,
				"last_chunk_index": 2,
				"sample_contexts": [],
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_surprise_feed",
		lambda db, category, value, start_year, end_year, limit, min_occurrences: [
			{
				"source_case": {
					"case_id": 1,
					"title": "Source",
					"citation": "2024 FC 10",
					"court": "FC",
					"date": "2024-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"authority": {
					"case_id": 2,
					"title": "Authority",
					"citation": "2019 SCC 65",
					"court": "SCC",
					"date": "2019-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"occurrence_count": 2,
				"global_citing_cases": 3,
				"gravity_share": 0.5,
				"surprise_score": 0.2,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_landmark_candidates",
		lambda db, limit, recent_years, baseline_years, min_recent: [
			{
				"case": {
					"case_id": 3,
					"title": "Landmark",
					"citation": "2020 SCC 1",
					"court": "SCC",
					"date": "2020-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"recent_citing_cases": 5,
				"baseline_citing_cases": 1,
				"emergence_score": 4.0,
				"lift_ratio": 5.0,
				"recent_window": {"start_year": 2022, "end_year": 2024},
				"baseline_window": {"start_year": 2017, "end_year": 2021},
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_doctrine_shifts",
		lambda db, category, value, limit, candidate_limit, start_year, end_year: [
			{
				"old_authority": {
					"case_id": 4,
					"title": "Old",
					"citation": "2001 SCC 1",
					"court": "SCC",
					"date": "2001-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"new_authority": {
					"case_id": 5,
					"title": "New",
					"citation": "2019 SCC 65",
					"court": "SCC",
					"date": "2019-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"replacement_score": 1.2,
				"status": "replacement_likely",
				"series": [],
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_hidden_bridges",
		lambda db, source_case_id, target_case_id, max_hops, path_limit, per_node_limit, bridge_limit: [
			{
				"bridge_case": {
					"case_id": 6,
					"title": "Bridge",
					"citation": "2017 FC 22",
					"court": "FC",
					"date": "2017-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"path_count": 2,
				"weighted_support": 6.5,
				"average_relative_position": 0.5,
				"average_path_hops": 3.0,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_inheritance_chains",
		lambda db, case_id, max_depth, limit, per_node_limit, min_occurrences: [
			{
				"chain_case_ids": [1, 2, 3],
				"depth": 2,
				"total_occurrences": 7,
				"nodes": [],
				"edge_occurrences": [4, 3],
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_missing_authorities",
		lambda db, case_id, peer_limit, result_limit, min_peer_share, min_peer_citations: [
			{
				"authority": {
					"case_id": 7,
					"title": "Missing",
					"citation": "2018 SCC 9",
					"court": "SCC",
					"date": "2018-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"peer_citing_cases": 9,
				"peer_coverage": 0.45,
				"peer_occurrences": 13,
				"rarity_boost": 0.33,
				"priority_score": 1.7,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_authority_lifecycle",
		lambda db, category, value, start_year, end_year, limit, recent_years, prior_years: [
			{
				"authority": {
					"case_id": 8,
					"title": "Lifecycle",
					"citation": "2015 FC 100",
					"court": "FC",
					"date": "2015-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"recent_citing_cases": 15,
				"prior_citing_cases": 10,
				"total_citing_cases": 40,
				"velocity": 5.0,
				"decay": 0.0,
				"lifecycle_stage": "emerging",
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_cross_court_flow",
		lambda db, start_year, end_year, limit: [
			{
				"source_court": "FC",
				"target_court": "SCC",
				"citing_case_count": 20,
				"citation_occurrences": 45,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_position_profiles",
		lambda db, case_id, limit, min_occurrences: [
			{
				"authority": {
					"case_id": 9,
					"title": "Positioned",
					"citation": "2014 FC 99",
					"court": "FC",
					"date": "2014-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"occurrence_count": 4,
				"avg_chunk_index": 2.5,
				"first_chunk_index": 1,
				"last_chunk_index": 4,
				"first_half_hits": 2,
				"second_half_hits": 2,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_completion_suggestions",
		lambda db, case_id, peer_limit, limit, min_peer_share, min_peer_citations: [
			{
				"authority": {
					"case_id": 10,
					"title": "Suggested",
					"citation": "2016 SCC 3",
					"court": "SCC",
					"date": "2016-01-01",
					"in_degree": 0,
					"out_degree": 0,
					"pagerank": None,
				},
				"peer_citing_cases": 8,
				"peer_coverage": 0.4,
				"rarity_boost": 0.3,
				"expected_occurrences": 12,
				"recommendation_score": 1.5,
			}
		],
	)
	monkeypatch.setattr(
		routes,
		"_citation_shift_dashboard",
		lambda db, category, value, start_year, end_year, replacement_limit, lifecycle_limit, surprise_limit: {
			"category": category,
			"value": value,
			"replacement_candidates": [
				{
					"old_authority": {
						"case_id": 4,
						"title": "Old",
						"citation": "2001 SCC 1",
						"court": "SCC",
						"date": "2001-01-01",
						"in_degree": 0,
						"out_degree": 0,
						"pagerank": None,
					},
					"new_authority": {
						"case_id": 5,
						"title": "New",
						"citation": "2019 SCC 65",
						"court": "SCC",
						"date": "2019-01-01",
						"in_degree": 0,
						"out_degree": 0,
						"pagerank": None,
					},
					"replacement_score": 1.2,
					"status": "replacement_likely",
					"series": [],
				}
			],
			"emerging_authorities": [
				{
					"authority": {
						"case_id": 8,
						"title": "Lifecycle",
						"citation": "2015 FC 100",
						"court": "FC",
						"date": "2015-01-01",
						"in_degree": 0,
						"out_degree": 0,
						"pagerank": None,
					},
					"recent_citing_cases": 15,
					"prior_citing_cases": 10,
					"total_citing_cases": 40,
					"velocity": 5.0,
					"decay": 0.0,
					"lifecycle_stage": "emerging",
				}
			],
			"declining_authorities": [],
			"surprises": [
				{
					"source_case": {
						"case_id": 1,
						"title": "Source",
						"citation": "2024 FC 10",
						"court": "FC",
						"date": "2024-01-01",
						"in_degree": 0,
						"out_degree": 0,
						"pagerank": None,
					},
					"authority": {
						"case_id": 2,
						"title": "Authority",
						"citation": "2019 SCC 65",
						"court": "SCC",
						"date": "2019-01-01",
						"in_degree": 0,
						"out_degree": 0,
						"pagerank": None,
					},
					"occurrence_count": 2,
					"global_citing_cases": 3,
					"gravity_share": 0.5,
					"surprise_score": 0.2,
				}
			],
		},
	)

	authority_csv = routes.export_citation_authority_signals(case_id=1, db=database)
	assert authority_csv.media_type == "text/csv; charset=utf-8"
	assert authority_csv.headers["content-disposition"] == 'attachment; filename="authority-signals-1.csv"'
	assert b"originality_score" in authority_csv.body

	surprises_csv = routes.export_citation_surprises(category="issue", value="Detention", db=database)
	assert surprises_csv.media_type == "text/csv; charset=utf-8"
	assert surprises_csv.headers["content-disposition"] == 'attachment; filename="citation-surprises.csv"'
	assert b"surprise_score" in surprises_csv.body

	landmarks_csv = routes.export_citation_landmark_candidates(db=database)
	assert landmarks_csv.media_type == "text/csv; charset=utf-8"
	assert landmarks_csv.headers["content-disposition"] == 'attachment; filename="landmark-candidates.csv"'
	assert b"emergence_score" in landmarks_csv.body

	shifts_csv = routes.export_citation_doctrine_shifts(category="issue", value="Detention", db=database)
	assert shifts_csv.media_type == "text/csv; charset=utf-8"
	assert shifts_csv.headers["content-disposition"] == 'attachment; filename="doctrine-shifts.csv"'
	assert b"replacement_score" in shifts_csv.body

	hidden_csv = routes.export_hidden_citation_bridges(source_case_id=1, target_case_id=2, db=database)
	assert hidden_csv.media_type == "text/csv; charset=utf-8"
	assert hidden_csv.headers["content-disposition"] == 'attachment; filename="hidden-bridges-1-to-2.csv"'
	assert b"weighted_support" in hidden_csv.body

	inheritance_csv = routes.export_citation_inheritance_chains(case_id=1, db=database)
	assert inheritance_csv.media_type == "text/csv; charset=utf-8"
	assert inheritance_csv.headers["content-disposition"] == 'attachment; filename="inheritance-chains-1.csv"'
	assert b"chain_case_ids" in inheritance_csv.body

	missing_csv = routes.export_citation_missing_authorities(case_id=1, db=database)
	assert missing_csv.media_type == "text/csv; charset=utf-8"
	assert missing_csv.headers["content-disposition"] == 'attachment; filename="missing-authorities-1.csv"'
	assert b"priority_score" in missing_csv.body

	lifecycle_csv = routes.export_citation_authority_lifecycle(db=database)
	assert lifecycle_csv.media_type == "text/csv; charset=utf-8"
	assert lifecycle_csv.headers["content-disposition"] == 'attachment; filename="authority-lifecycle.csv"'
	assert b"lifecycle_stage" in lifecycle_csv.body

	flow_csv = routes.export_citation_cross_court_flow(db=database)
	assert flow_csv.media_type == "text/csv; charset=utf-8"
	assert flow_csv.headers["content-disposition"] == 'attachment; filename="cross-court-flow.csv"'
	assert b"source_court" in flow_csv.body

	position_csv = routes.export_citation_position_profiles(case_id=1, db=database)
	assert position_csv.media_type == "text/csv; charset=utf-8"
	assert position_csv.headers["content-disposition"] == 'attachment; filename="position-profiles-1.csv"'
	assert b"avg_chunk_index" in position_csv.body

	completion_csv = routes.export_citation_completion_suggestions(case_id=1, db=database)
	assert completion_csv.media_type == "text/csv; charset=utf-8"
	assert completion_csv.headers["content-disposition"] == 'attachment; filename="completion-suggestions-1.csv"'
	assert b"recommendation_score" in completion_csv.body

	dashboard_csv = routes.export_citation_shift_dashboard(category="issue", value="Detention", db=database)
	assert dashboard_csv.media_type == "text/csv; charset=utf-8"
	assert dashboard_csv.headers["content-disposition"] == 'attachment; filename="shift-dashboard.csv"'
	assert b"replacement_candidate" in dashboard_csv.body