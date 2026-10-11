import unittest

from backend.case_frame_plus import build_frame_plus

HEADER = """Vuu v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2022-02-03
Docket: IMM-384-21
BETWEEN:
MICHAEL VUU
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS"""
PARAS = [
	"Mr. Vuu applied for permanent residence on humanitarian and compassionate grounds under s. 25(1) of the Immigration and Refugee Protection Act. He seeks judicial review of the refusal of this application by a Senior Officer.",
	"For the reasons that follow, I allow this application as I find the Officer made an unreasonable assessment of the Applicant's establishment.",
	"The Applicant argues that the Officer unreasonably discounted his establishment in Canada without explaining why ten years of residence was not enough.",
	"The Respondent submits that the Officer reviewed all the evidence and that an exemption was not warranted in the circumstances.",
	"The application for judicial review is allowed.",
]
NUMBERS = [1, 2, 3, 4, 5]


class FramePlusTests(unittest.TestCase):
	def setUp(self):
		self.f = build_frame_plus(HEADER, "\n".join(PARAS), PARAS, NUMBERS)

	def test_parties_and_roles(self):
		self.assertEqual((self.f.applicant_role, self.f.respondent_role), ("individual", "minister"))

	def test_levels_end_with_this_court_and_date(self):
		last = self.f.levels[-1]
		self.assertEqual((last.level, last.date), ("fc", "2022-02-03"))
		self.assertIn("allowed", last.outcome)

	def test_subject(self):
		self.assertEqual(self.f.subject, "humanitarian and compassionate application")

	def test_arguments_by_side(self):
		sides = {a.side: a.para for a in self.f.arguments}
		self.assertEqual(sides, {"applicant": 3, "respondent": 4})

	def test_courts_own_sentence_is_not_an_argument(self):
		self.assertNotIn(2, [a.para for a in self.f.arguments])

	def test_text_is_plain(self):
		self.assertIn("humanitarian", self.f.text())


if __name__ == "__main__":
	unittest.main()
