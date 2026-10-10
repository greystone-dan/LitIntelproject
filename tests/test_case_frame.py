import unittest

from backend.case_frame import UNKNOWN, build_frame
from backend.position_holder import APPLICANT, EARLIER, RESPONDENT, parties_from_frame, tag_decision

FC_HEADER = """Ali v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2025-01-22
File numbers
IMM-8783-22
Decision Content
BETWEEN:
MOHAMMED ALI
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS"""
FC_BODY = ("[1] The Applicant seeks judicial review of a decision of a Senior Immigration Officer refusing his "
	"application. [2] The application for judicial review is dismissed.")


class FrameTests(unittest.TestCase):
	def test_fc_judicial_review_of_officer(self):
		f = build_frame(FC_HEADER, FC_BODY)
		self.assertEqual((f.court.value, f.proceeding.value, f.earlier_decision_maker.value), ("fc", "judicial_review", "officer"))
		self.assertEqual(f.applicant_is_minister.value, "no")
		self.assertTrue(f.confident)
		self.assertIn("officer", f.text())
		self.assertEqual(f.standard_of_review.source, "default")

	def test_minister_as_applicant_from_between_block(self):
		header = FC_HEADER.replace("MOHAMMED ALI", "THE MINISTER OF CITIZENSHIP AND IMMIGRATION", 1).replace(
			"THE MINISTER OF CITIZENSHIP AND IMMIGRATION\nRespondent", "MOHAMMED ALI\nRespondent")
		f = build_frame(header, FC_BODY)
		self.assertEqual(f.applicant_is_minister.value, "yes")
		self.assertEqual(parties_from_frame(f).minister_first, True)

	def test_crown_keeps_literal_roles(self):
		f = build_frame("R. v. G.F.\nCollection\nSupreme Court Judgments", "[1] This is an appeal.")
		self.assertEqual(f.applicant_is_minister.value, "crown")
		self.assertFalse(parties_from_frame(f).minister_first)

	def test_rpd_decision_has_no_earlier_decision(self):
		f = build_frame("RPD File No. / N° de dossier de la SPR : TB2-1\nPrivate Proceeding", "[1] The claimant alleges a fear.")
		self.assertEqual((f.court.value, f.proceeding.value), ("rpd", "direct"))
		self.assertEqual(f.earlier_decision_maker.value, UNKNOWN)
		self.assertTrue(f.confident)

	def test_rad_reviews_rpd(self):
		f = build_frame("RAD File / Dossier de la SAR : TB9-1", "[1] The Appellant appeals the decision of the Refugee Protection Division.")
		self.assertEqual(f.earlier_decision_maker.value, "rpd")

	def test_unknown_stays_unknown(self):
		f = build_frame("", "")
		self.assertEqual((f.court.value, f.proceeding.value), (UNKNOWN, UNKNOWN))
		self.assertFalse(f.confident)
		self.assertEqual(f.text(), "")


class FrameWiringTests(unittest.TestCase):
	def test_minister_applicant_sides_resolved_from_frame(self):
		header = FC_HEADER.replace("MOHAMMED ALI", "THE MINISTER OF CITIZENSHIP AND IMMIGRATION", 1).replace(
			"THE MINISTER OF CITIZENSHIP AND IMMIGRATION\nRespondent", "MOHAMMED ALI\nRespondent")
		f = build_frame(header, FC_BODY)
		out = tag_decision(["[1] The applicant submits that the RPD erred."], "", f)
		self.assertEqual(out[0].sentence_holders, [RESPONDENT])  # literal "applicant" is the Minister here

	def test_lead_in_list_belongs_to_the_party(self):
		out = tag_decision(["[1] The applicant raises two issues:", "[2] The Officer erred in assessing the evidence.", "[3] I disagree."],
			"Smith v. Canada (Citizenship and Immigration)")
		self.assertEqual([r.sentence_holders[0] for r in out], [APPLICANT, APPLICANT, "court"])

	def test_no_earlier_decision_folds_layers(self):
		f = build_frame("RPD File No. / N° de dossier de la SPR : TB2-1", "[1] x")
		out = tag_decision(["[1] The panel finds the claimant not credible."], "", f)
		self.assertEqual(out[0].layers, [1])


if __name__ == "__main__":
	unittest.main()


MOA_HEADER = """FEDERAL COURT
Court File No.: IMM-5590-25
BETWEEN:
KAVEH RAHIMI
Applicant
- and -
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
RESPONDENT’S MEMORANDUM OF ARGUMENT
(Prepared by counsel for the Minister)"""
MOA_BODY = ("1. The Respondent opposes the Applicant’s application for judicial review of the decision of the Refugee "
	"Protection Division (RPD) dated June 3, 2025. 2. The RPD’s decision is reasonable. The Court does not reweigh the "
	"evidence. 3. The Applicant’s argument is that the RPD ought to have weighed his motive differently. The RPD found "
	"that intention is presumed. 4. The Respondent asks that the application be dismissed, with no question for certification.")

ID_HEADER = """IMMIGRATION AND REFUGEE BOARD OF CANADA
IMMIGRATION DIVISION
File No. / No de dossier: VB5-04118
Detention review of: Teodor VALKANOV (Person Concerned)
REASONS FOR DECISION AND RELEASE ORDER"""
ID_BODY = "1. This is a detention review under subsection 57(2) of the Act. 2. The ID finds that the detainee is a flight risk. The Minister submits that he should remain detained."


class DocumentKindTests(unittest.TestCase):
	def test_decision_is_written_by_the_court(self):
		f = build_frame(FC_HEADER, FC_BODY)
		self.assertEqual((f.document_kind.value, f.author.value), ("decision", "court"))

	def test_ministers_memorandum_is_the_respondents_voice(self):
		f = build_frame(MOA_HEADER, MOA_BODY)
		self.assertEqual((f.document_kind.value, f.author.value), ("memorandum", "respondent"))
		self.assertEqual((f.court.value, f.proceeding.value, f.earlier_decision_maker.value), ("fc", "judicial_review", "rpd"))
		self.assertIn("written by the respondent", f.text())
		paras = [p for p in MOA_BODY.replace("1. ", "\n1. ").replace("2. ", "\n2. ").replace("3. ", "\n3. ").replace("4. ", "\n4. ").split("\n") if p]
		res = tag_decision(paras, frame=f)
		# untagged sentences are the respondent's position, not the Court's
		self.assertEqual(res[0].primary, RESPONDENT)
		self.assertEqual(res[0].cues[0].holder, RESPONDENT)
		# "The Court does not reweigh" is the author stating the law, not a holding
		self.assertNotIn("court", res[1].holders)
		# the other side's argument and the earlier decision maker are still seen
		self.assertIn(APPLICANT, res[2].holders)
		self.assertIn(EARLIER, res[2].holders)
		# "no question for certification" is a request, not the Court
		self.assertNotIn("court", res[3].holders)

	def test_memorandum_headings_and_issue_questions_are_the_authors(self):
		# lines copied from the fictional Word drafts 04 (study permit) and 05 (cessation)
		f = build_frame(MOA_HEADER.replace("RESPONDENT’S MEMORANDUM", "APPLICANT’S MEMORANDUM").replace("(Prepared by counsel for the Minister)", ""), MOA_BODY)
		paras = ["B. The officer’s conclusion on the study plan was unreasonable",
			"5.\t(a) Was the officer’s conclusion on the program of study unreasonable? (b) Did the officer’s failure to give adequate reasons breach procedural fairness?"]
		for r in tag_decision(paras, frame=f):
			self.assertEqual(set(r.sentence_holders), {APPLICANT})
			self.assertEqual(set(r.layers), {2})
		# a sentence that reports the officer's finding is still the earlier decision maker's
		r = tag_decision(["The officer found that the Applicant did not show a clear study plan, which was unreasonable."], frame=f)[0]
		self.assertIn(EARLIER, r.sentence_holders)

	def test_headings_do_not_change_a_decision(self):
		f = build_frame(FC_HEADER, FC_BODY)
		r = tag_decision(["The Officer found that Amara would adapt to life in Trinidad and Tobago"], frame=f)[0]
		self.assertEqual(f.author.value, "court")
		self.assertEqual(r.sentence_holders, [EARLIER])

	def test_applicants_memorandum(self):
		f = build_frame(MOA_HEADER.replace("RESPONDENT’S MEMORANDUM", "APPLICANT’S MEMORANDUM").replace("(Prepared by counsel for the Minister)", ""), MOA_BODY)
		self.assertEqual(f.author.value, "applicant")

	def test_immigration_division_decision_is_first_instance(self):
		f = build_frame(ID_HEADER, ID_BODY)
		self.assertEqual((f.court.value, f.proceeding.value, f.document_kind.value, f.author.value), ("id", "direct", "decision", "court"))
		self.assertFalse(f.earlier_decision_maker.known)
		res = tag_decision(["1. This is a detention review.", "2. The ID finds that the detainee is a flight risk. The Minister submits that he should remain detained."], frame=f)
		self.assertNotIn(EARLIER, res[1].holders)  # the ID is the author, not an earlier decision maker
		self.assertIn(RESPONDENT, res[1].holders)


class EvaluationTests(unittest.TestCase):
	"""Sentences copied from the fictional Word drafts 01, 03, 04 and 05 (project folder live-analysis/test-docs-word)."""

	def _decision(self):
		return build_frame(FC_HEADER, FC_BODY)

	def _memo(self, author="applicant"):
		head = ("APPLICANT’S MEMORANDUM OF ARGUMENT\nFederal Court\nBETWEEN:\nMOHAMMED ALI\nApplicant\nand\n"
			"THE MINISTER OF CITIZENSHIP AND IMMIGRATION\nRespondent\n")
		if author == "respondent":
			head = head.replace("APPLICANT’S", "RESPONDENT’S")
		return build_frame(head, "[1] The Applicant seeks judicial review of a decision of an Officer.")

	def test_court_evaluation_of_the_officer_is_the_courts(self):
		f = self._decision()
		for s in ("The sole issue is whether the Officer’s decision is reasonable.",
				"Here the Officer’s conclusion that Amara “would adapt” rests on no evidence.",
				"Having rejected the report, the Officer did not consider the separate country evidence on mental health care.",
				"The Court is not reweighing; it is identifying that the Officer failed to consider evidence that bore on the key question.",
				"The Officer applied an unduly narrow hardship lens, contrary to Kanthasamy v Canada (Citizenship and Immigration), 2015 SCC 61."):
			self.assertEqual(tag_decision([s], frame=f)[0].sentence_holders[0], "court", s)

	def test_reporting_verbs_stay_with_the_officer(self):
		f = self._decision()
		for s in ("The Officer found the psychological report “of limited weight” because the author had met the Applicant only once.",
				"On the best interests of the child, the Officer wrote that Amara “would adapt” to life in Trinidad and Tobago."):
			self.assertEqual(tag_decision([s], frame=f)[0].sentence_holders[0], EARLIER, s)

	def test_memorandum_evaluation_and_relief_are_the_authors(self):
		m = self._memo("respondent")
		for s in ("The RPD’s decision is reasonable.", "The RPD’s decision is reviewed for reasonableness."):
			self.assertEqual(tag_decision([s], frame=m)[0].sentence_holders[0], RESPONDENT, s)
		a = self._memo("applicant")
		for s in ("The warrant post-dates the RAD decision.",
				"The Applicant asks that leave be granted, that the PRRA decision be set aside and that the matter be remitted to a different officer for redetermination, with an oral hearing if the Minister’s delegate considers it necessary."):
			self.assertEqual(tag_decision([s], frame=a)[0].sentence_holders[0], APPLICANT, s)
		# the officer's reported finding in the same memorandum is still the officer's
		r = tag_decision(["The Officer found the warrant to be of “little probative value” because it could not be authenticated."], frame=a)[0]
		self.assertEqual(r.sentence_holders[0], EARLIER)

	def test_ibid_takes_the_citation_before_it(self):
		for frame in (self._decision(), self._memo()):
			r = tag_decision(["Ibid."], frame=frame)[0]
			self.assertEqual((r.sentence_holders[0], r.layers[0]), ("prior_court_or_authority", 6))

	def test_reported_testimony_in_a_memorandum_keeps_its_layer(self):
		m = self._memo("respondent")
		r = tag_decision(["At the RPD hearing the Applicant testified that he returned to care for his ailing father."], frame=m)[0]
		self.assertEqual(r.layers[0], 4)
