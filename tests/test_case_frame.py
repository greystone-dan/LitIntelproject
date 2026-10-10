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
