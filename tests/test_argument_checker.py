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


def _jaccard(a, b):
	x, y = set(a.lower().split()), set(b.lower().split())
	return len(x & y) / len(x | y) if x | y else 0.0


class ListMergeTests(unittest.TestCase):
	FULL = [{"side": "respondent", "text": "the officer reasonably weighed the evidence", "para": 4}]
	NOTES = [
		{"side": "applicant", "text": "the officer reasonably weighed the evidence", "paras": [4]},
		{"side": "applicant", "text": "the delay breached fairness entirely", "paras": [9]},
	]

	def test_matching_notes_item_takes_full_text_side(self):
		from backend.argument_checker import adopt_full_text_sides

		out = adopt_full_text_sides(self.FULL, self.NOTES, _jaccard)
		self.assertEqual((out[0]["side"], out[0]["side_adopted"]), ("respondent", True))
		self.assertEqual((out[1]["side"], out[1]["side_adopted"]), ("applicant", False))

	def test_notes_item_kept_only_with_a_vote(self):
		from backend.argument_checker import merge_by_votes

		runs = [[{"text": "the delay breached fairness entirely"}], []]
		merged = merge_by_votes(self.FULL, self.NOTES, runs, _jaccard)
		self.assertEqual([m["src"] for m in merged], ["full_text", "notes"])
		self.assertEqual((merged[1]["votes"], merged[1]["paras"]), (1, [9]))
		self.assertEqual(len(merge_by_votes(self.FULL, self.NOTES, [[], []], _jaccard)), 1)


	def test_whole_decision_flip_for_unmatched_notes(self):
		from backend.argument_checker import adopt_full_text_sides

		full = [
			{"side": "respondent", "text": "alpha beta gamma delta"},
			{"side": "respondent", "text": "one two three four"},
		]
		notes = [
			{"side": "applicant", "text": "alpha beta gamma delta"},
			{"side": "applicant", "text": "one two three four"},
			{"side": "applicant", "text": "unrelated point about costs"},
		]
		out = adopt_full_text_sides(full, notes, _jaccard)
		self.assertEqual([o["side"] for o in out], ["respondent", "respondent", "respondent"])
		self.assertTrue(out[2]["side_flipped"] and not out[2]["side_adopted"])
		agree = adopt_full_text_sides(full, [{**n, "side": "respondent"} for n in notes[:2]] + [notes[2]], _jaccard)
		self.assertEqual(agree[2]["side"], "applicant")
