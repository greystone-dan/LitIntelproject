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
