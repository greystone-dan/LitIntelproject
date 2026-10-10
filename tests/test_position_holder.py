import unittest

from backend.position_holder import (
	APPLICANT, AUTHORITY, COURT, EARLIER, RESPONDENT, WITNESS,
	parse_parties, sentence_cue, split_numbered_paragraphs, split_sentences, tag_decision, tag_paragraph,
)


def holder(sentence, title="Smith v. Canada (Citizenship and Immigration)"):
	cue = sentence_cue(sentence, parse_parties(title))
	return cue.holder if cue else None


class HeaderTests(unittest.TestCase):
	def test_individual_first(self):
		p = parse_parties("Lemay Co Inc. v. Canada (Attorney General)")
		self.assertFalse(p.minister_first)
		self.assertIn("Lemay", p.aliases_first)

	def test_minister_first(self):
		for t in ("Minister of Citizenship and Immigration v. Camayo", "Canada (Attorney General) v. Eakin",
				"Canada (Citizenship and Immigration) v. Camayo"):
			self.assertTrue(parse_parties(t).minister_first, t)

	def test_no_title(self):
		self.assertEqual(parse_parties("").first, "")


class CueTests(unittest.TestCase):
	def test_party_submissions(self):
		self.assertEqual(holder("The applicant submits that the Officer erred."), APPLICANT)
		self.assertEqual(holder("The Minister argues that the decision was reasonable."), RESPONDENT)
		self.assertEqual(holder("The respondent therefore brought this motion to strike, arguing that it is doomed."), RESPONDENT)
		self.assertEqual(holder("According to the applicant, the risk is personalized."), APPLICANT)
		self.assertEqual(holder("In the Minister's view, the evidence is insufficient."), RESPONDENT)

	def test_named_party_from_header(self):
		self.assertEqual(holder("Lemay submitted that subsection 152(3.4) applies.", "Lemay Co Inc. v. Canada (AG)"), APPLICANT)

	def test_filing_is_not_a_submission(self):
		self.assertIsNone(holder("The Applicant submitted an application for permanent residence in 2018."))

	def test_earlier_decision_maker(self):
		self.assertEqual(holder("The RPD found that the applicant was not credible."), EARLIER)
		self.assertEqual(holder("The Officer was not satisfied that the documents were genuine."), EARLIER)
		self.assertEqual(holder("The decision letter gives three reasons for the refusal."), EARLIER)

	def test_court_voice(self):
		self.assertEqual(holder("I am not persuaded by this argument."), COURT)
		self.assertEqual(holder("In my view, the decision was reasonable."), COURT)
		self.assertEqual(holder("The application for judicial review is dismissed."), COURT)

	def test_court_noting_a_party_view_stays_with_party(self):
		self.assertEqual(holder("I note that the applicant submits that the Officer ignored the letter."), APPLICANT)

	def test_authority(self):
		self.assertEqual(holder("In Vavilov, the Supreme Court held that reasonableness is the presumptive standard."), AUTHORITY)
		self.assertEqual(holder("Justice Crampton stated that the risk must be personalized."), AUTHORITY)
		self.assertEqual(holder("Section 25 of the Act provides that the Minister may grant relief."), AUTHORITY)

	def test_witness_and_document(self):
		self.assertEqual(holder("The affidavit states that the applicant was in Mexico in 2019."), WITNESS)
		self.assertEqual(holder("Dr. Lee opined that the applicant suffers from depression."), WITNESS)
		self.assertEqual(holder("The applicant testified that he was threatened."), APPLICANT)

	def test_no_cue(self):
		self.assertIsNone(holder("The hearing took place on May 4."))


class MinisterAsApplicantTests(unittest.TestCase):
	TITLE = "Minister of Citizenship and Immigration v. Camayo"

	def test_normalized_sides(self):
		# literal "the applicant" here is the Minister; normalised labels keep Minister = respondent
		self.assertEqual(holder("The applicant submits that the RPD erred.", self.TITLE), RESPONDENT)
		self.assertEqual(holder("The respondent says he fears the cartel.", self.TITLE), APPLICANT)
		self.assertEqual(holder("The Minister argues the finding was unreasonable.", self.TITLE), RESPONDENT)
		self.assertEqual(holder("Camayo submits that the RPD was correct.", self.TITLE), APPLICANT)

	def test_literal_sides(self):
		p = parse_parties(self.TITLE)
		p.normalize = False
		self.assertEqual(sentence_cue("The applicant submits that the RPD erred.", p).holder, APPLICANT)


class ParagraphTests(unittest.TestCase):
	def test_sentences_keep_abbreviations(self):
		s = split_sentences("[5] See Smith v. Canada, 2020 FC 1 at para. 4. The Court agrees.")
		self.assertEqual(len(s), 2)

	def test_tag_paragraph_default_and_holders(self):
		r = tag_paragraph("The hearing was held in Toronto. The applicant argues that the delay was unfair.")
		self.assertEqual(r.sentence_holders, [COURT, APPLICANT])
		self.assertEqual(r.primary, APPLICANT)

	def test_citation_adds_authority_at_paragraph_level(self):
		r = tag_paragraph("The standard is correctness (Mohr at para 52).")
		self.assertIn(AUTHORITY, r.holders)

	def test_submission_run_carries_only_on_continuation(self):
		r = tag_paragraph("The applicant submits that the Officer erred. Further, the reasons were thin.")
		self.assertEqual(r.sentence_holders, [APPLICANT, APPLICANT])
		r = tag_paragraph("The applicant submits that the Officer erred. The Officer's letter is dated June 1, 2020.")
		self.assertNotEqual(r.sentence_holders[1], APPLICANT)

	def test_tag_decision_runs_across_paragraphs(self):
		out = tag_decision(["[1] The applicant submits that the finding was unfair.", "[2] Also, the delay was long.",
			"[3] I disagree."], "Smith v. Canada (Citizenship and Immigration)")
		self.assertEqual([r.primary for r in out], [APPLICANT, APPLICANT, COURT])

	def test_numbered_paragraph_split_ignores_inline_brackets(self):
		d = split_numbered_paragraphs("Title\n[1] First one.\n[2] Second [5] quoted.\n[3] Third.")
		self.assertEqual(sorted(d), [1, 2, 3])


if __name__ == "__main__":
	unittest.main()


class LayerTests(unittest.TestCase):
	def layer(self, sentence, title="Smith v. Canada (Citizenship and Immigration)"):
		from backend.position_holder import assign_layer
		cue = sentence_cue(sentence, parse_parties(title))
		assign_layer(sentence, cue)
		return cue

	def test_court_layer(self):
		self.assertEqual(self.layer("I am not persuaded by this argument.").layer, 1)

	def test_jr_party_layer(self):
		c = self.layer("The applicant argues that the Officer erred.")
		self.assertEqual((c.holder, c.layer), (APPLICANT, 2))

	def test_earlier_decision_maker_layer(self):
		self.assertEqual(self.layer("The Officer was not satisfied that the documents were genuine.").layer, 3)

	def test_first_instance_party_reported_inside_decision(self):
		c = self.layer("The Board noted that the claimant said he feared the police.")
		self.assertEqual((c.holder, c.layer, c.inner_holder), ("earlier_decision_maker", 4, APPLICANT))
		c = self.layer("Before the RPD, the appellant alleged that he suffered from depression.")
		self.assertEqual((c.layer, c.inner_holder), (4, APPLICANT))

	def test_authority_layer(self):
		self.assertEqual(self.layer("In Vavilov, the Supreme Court held that reasonableness is presumptive.").layer, 6)

	def test_mixed_layers_flagged(self):
		r = tag_paragraph("The applicant argues that the Officer erred. The Officer found that the claimant lacked credibility.")
		self.assertTrue(r.mixed_layers)


class ForumTests(unittest.TestCase):
	def test_detect_forum(self):
		from backend.position_holder import detect_forum
		self.assertEqual(detect_forum("RAD File / Dossier de la SAR : TB9-1"), "rad")
		self.assertEqual(detect_forum("X v. Y\nCourt (s) Database\nFederal Court Decisions"), "fc")
		self.assertEqual(detect_forum("X v. Y\nFederal Court of Appeal Decisions"), "fca")

	def test_tribunal_is_author_of_its_own_decision(self):
		p = parse_parties("")
		p.forum = "rpd"
		self.assertEqual(tag_paragraph("The panel finds that the claimant is not credible.", p).sentence_holders, [COURT])
		p.forum = "fc"
		self.assertEqual(tag_paragraph("The panel finds that the claimant is not credible.", p).sentence_holders, [EARLIER])

	def test_rad_reviewing_rpd(self):
		p = parse_parties("")
		p.forum = "rad"
		self.assertEqual(tag_paragraph("The RPD found that the appellant was not credible.", p).sentence_holders, [EARLIER])


class FrameworkTests(unittest.TestCase):
	def test_law_statement_without_citation(self):
		r = tag_paragraph("The test is whether the decision is justified, transparent and intelligible.")
		self.assertEqual(r.layers, [6])
		self.assertTrue(r.has_framework)

	def test_leading_case_commentary(self):
		r = tag_paragraph("The leading case on this point is Baker, which held that the duty of fairness is flexible.")
		self.assertIn(6, r.layers)

	def test_finding_on_these_facts_is_not_framework(self):
		r = tag_paragraph("I find that the Officer's reasons on this record were adequate.")
		self.assertEqual(r.layers, [1])

	def test_party_argument_stays_with_party(self):
		r = tag_paragraph("The applicant argues that the test is not met.")
		self.assertEqual(r.layers, [2])


class AppealCourtTests(unittest.TestCase):
	"""Rules added after scoring against reader grades and AI tags (see docs/position-rules-evaluation.md)."""

	def _forum(self, forum):
		p = parse_parties("Smith v. Canada")
		p.forum = forum
		return p

	def test_scc_courts_below_are_earlier_decision_makers(self):
		p = self._forum("scc")
		self.assertEqual(sentence_cue("The Federal Court of Appeal found that s. 23 grants jurisdiction.", p).holder, EARLIER)
		self.assertEqual(sentence_cue("Gagnon J.A. concluded that the onus was on Mr. Rosati.", p).holder, EARLIER)
		self.assertEqual(sentence_cue("The trial judge accepted the complainant's evidence.", p).holder, EARLIER)

	def test_scc_other_case_stays_authority(self):
		p = self._forum("scc")
		cue = sentence_cue("In R. v. Handy, 2002 SCC 56, the Court of Appeal held that the evidence was admissible.", p)
		self.assertNotEqual(cue.holder, EARLIER)

	def test_fc_forum_unchanged(self):
		p = self._forum("fc")
		self.assertNotEqual(sentence_cue("The Federal Court of Appeal found that the test is met.", p).holder, EARLIER)

	def test_capitalised_officer_is_earlier_decision_maker(self):
		p = self._forum("fc")
		self.assertEqual(sentence_cue("The Officer scheduled an interview with the applicant.", p).holder, EARLIER)
		self.assertEqual(sentence_cue("The Commission informed the appellant of its concerns.", p).holder, EARLIER)

	def test_agree_with_party_adds_the_party(self):
		p = parse_parties("Smith v. Canada (Citizenship and Immigration)")
		res = tag_paragraph("I agree with the Respondent that the decision was reasonable.", p)
		self.assertIn(COURT, res.holders)
		self.assertIn(RESPONDENT, res.holders)

	def test_citation_in_party_sentence_is_not_authority(self):
		p = parse_parties("Smith v. Canada (Citizenship and Immigration)")
		res = tag_paragraph("Mr. Smith asserts that the Officer erred (Sosi v Canada, 2008 FC 1300 at para 24).", p)
		self.assertNotIn(AUTHORITY, res.holders)
		res = tag_paragraph("The test is well established. See Sosi v Canada, 2008 FC 1300 at para 24.", p)
		self.assertIn(AUTHORITY, res.holders)

	def test_more_argument_verbs(self):
		self.assertEqual(holder("The applicant takes issue with the Officer's reasons."), APPLICANT)
		self.assertEqual(holder("The respondent challenges the standing of the applicant."), RESPONDENT)


class ForumAndNumberingTests(unittest.TestCase):
	def test_court_named_first_in_header_wins(self):
		from backend.position_holder import detect_forum
		header = "Smith v. Canada\nCourt (s) Database\nSupreme Court Judgments\nOn appeal from the Federal Court of Appeal\n"
		self.assertEqual(detect_forum(header), "scc")
		self.assertEqual(detect_forum("Smith v. Canada\nFederal Court of Appeal Decisions\n"), "fca")

	def test_line_start_numbers_when_no_brackets(self):
		text = "MEMORANDUM\n\n1. First paragraph about the facts.\n\n2. Second paragraph, with a list:\n1. restarts inside\n\n3. Third.\n\n4. Fourth."
		paras = split_numbered_paragraphs(text)
		self.assertEqual(sorted(paras), [1, 2, 3, 4])
		self.assertTrue(paras[3].startswith("3. Third"))

	def test_brackets_win_over_line_numbers(self):
		paras = split_numbered_paragraphs("[1] One.\n[2] Two.\n[3] Three.\n1. a list item\n")
		self.assertEqual(sorted(paras), [1, 2, 3])


class EvalSplitTests(unittest.TestCase):
	def test_split_is_stable_and_by_decision(self):
		from scripts.eval_position_rules import split_of
		self.assertEqual(split_of(28105), split_of("28105"))
		share = sum(split_of(i) == "test" for i in range(2000)) / 2000
		self.assertTrue(0.25 < share < 0.35)
