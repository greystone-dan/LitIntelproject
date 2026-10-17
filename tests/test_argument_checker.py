import os
import unittest
from unittest import mock

from backend.argument_checker import enabled, flag_lowest, normalise_side, own_side_reporting, score_arguments

PARAS = {
	1: "The applicant submits that the officer ignored the evidence.",
	2: "The respondent argues that the decision was reasonable.",
	3: "I find the officer erred.",
}


class ArgumentCheckerTests(unittest.TestCase):
	def test_side_roles_swap_when_minister_is_applicant(self):
		self.assertEqual(normalise_side("applicant", "no"), "individual")
		self.assertEqual(normalise_side("applicant", "yes"), "minister")
		self.assertEqual(normalise_side("respondent", "yes"), "individual")
		self.assertEqual(normalise_side("intervener", "no"), "other")

	def test_reporting_follows_the_side_label(self):
		self.assertGreater(own_side_reporting("applicant", 1, PARAS), 0)
		self.assertEqual(own_side_reporting("applicant", 3, {3: "I find the officer erred."}), 0)

	def test_minister_appellant_not_penalised(self):
		paras = {5: "The Minister submits that the Board misread the evidence.", 6: "The respondent argues the finding was open to the Board."}
		self.assertGreater(own_side_reporting("applicant", 5, paras, "yes"), 0)
		self.assertEqual(own_side_reporting("applicant", 5, paras, "no"), 0)

	def test_flag_lowest_keeps_items(self):
		scored = score_arguments([{"side": "applicant", "para": 1}, {"side": "respondent", "para": 2}, {"side": "applicant", "para": 3}], PARAS)
		out = flag_lowest(scored, 0.34)
		self.assertEqual(len(out), 3)
		self.assertEqual([m["flagged"] for m in out], [False, False, True])

	def test_off_by_default(self):
		with mock.patch.dict(os.environ, {}, clear=True):
			self.assertFalse(enabled())
		with mock.patch.dict(os.environ, {"ILIT_ARGUMENT_CHECKER": "1"}):
			self.assertTrue(enabled())


if __name__ == "__main__":
	unittest.main()
