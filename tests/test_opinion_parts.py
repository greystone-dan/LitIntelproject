import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "ai_poc"))

from opinion_parts import describe, opinion_parts, part_of  # noqa: E402

RANGED = """MediaQMI inc. v. Kamel
Held (Wagner C.J. and Rowe, Martin and Kasirer JJ. dissenting): The appeal should be dismissed.
Reasons for Judgment: (paras. 1 to 73)
Joint Dissenting Reasons: (paras. 74 to 143)
[1] Text. [73] Text. [74] Text. [143] Text."""

PLAIN = """Windsor (City) v. Canadian Transit Co.
Held (Abella, Moldaver, Côté and Brown JJ. dissenting): The appeal should be allowed.
Reasons for Judgment:
Joint Dissenting Reasons:
Dissenting Reasons:
The judgment of McLachlin C.J. and Cromwell, Karakatsanis, Wagner and Gascon JJ. was delivered by
[1] Text. [72] Text.
The reasons of Moldaver, Côté and Brown JJ. were delivered by
[73] Text. [121] Text.
The following are the reasons delivered by
[122] Text. [131] Text."""


class OpinionPartsTests(unittest.TestCase):
	def test_ranged_headings(self):
		info = opinion_parts(RANGED)
		self.assertEqual([(p["kind"], p["start"], p["end"]) for p in info["parts"]], [("majority", 1, 73), ("dissenting", 74, 143)])
		self.assertIn("appeal should be dismissed", info["held"])
		self.assertEqual(part_of(info["parts"], 80), "dissenting")
		self.assertIn("MAJORITY", describe(info))

	def test_plain_headings_with_delivered_by_lines(self):
		info = opinion_parts(PLAIN)
		self.assertEqual([(p["kind"], p["start"], p["end"]) for p in info["parts"]], [("majority", 1, 72), ("dissenting", 73, 121), ("dissenting", 122, 131)])

	def test_unanimous_decision_has_no_parts_line(self):
		info = opinion_parts("Ali v. Canada\n[1] The applicant seeks judicial review. [2] Dismissed.")
		self.assertEqual(info["parts"], [])
		self.assertEqual(part_of(info["parts"], 2), "majority")
		self.assertEqual(describe(info), "")


if __name__ == "__main__":
	unittest.main()
