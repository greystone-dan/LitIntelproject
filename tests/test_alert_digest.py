from copy import deepcopy
from datetime import datetime, timezone
import unittest

from backend.alert_digest import (
	build_alert_digest, partition_matches, render_digest_html, render_digest_text,
)


class DigestTests(unittest.TestCase):
	def setUp(self):
		self.searches = [{"id": 1, "name": "<script>alert('x')</script>", "last_alert_check": "2026-10-01T00:00:00Z"}]

	def matches(self, count, losses, start=1):
		return [{
			"search_id": 1, "case_id": start + i, "citation": f"2026 FC {start + i}",
			"court": "FC", "date": "2026-09-30", "decision_outcome": "granted",
			"minister": "Citizenship and Immigration",
			"government_outcome": "lost" if i < losses else "won",
			"discovered_at": "2026-10-02T00:00:00Z",
		} for i in range(count)]

	def test_exact_threshold_and_minimum_counts(self):
		for nt, nl, et, el, expected in [
			(5, 2, 5, 1, True), (5, 1, 5, 0, True),
			(10, 3, 10, 2, False), (4, 4, 5, 0, False),
			(5, 5, 4, 0, False), (5, 0, 5, 2, False),
			(0, 0, 5, 0, False), (5, 5, 0, 0, False),
		]:
			with self.subTest(nt=nt, nl=nl, et=et, el=el):
				result = build_alert_digest(self.searches, self.matches(nt, nl), self.matches(et, el, 101))
				self.assertEqual(result["searches"][0]["possible_shift"], expected)

	def test_rendering_fields_counts_and_escaping(self):
		result = build_alert_digest(self.searches, self.matches(5, 2), self.matches(5, 1, 101))
		html, text = render_digest_html(result), render_digest_text(result)
		self.assertNotIn("<script>", html)
		self.assertIn("&lt;script&gt;", html)
		self.assertIn('style="', html)
		self.assertNotIn("<link", html)
		for output in (html, text):
			for label in ("Possible shift", "2/5 Minister losses", "1/5 Minister losses", "2026 FC 1", "FC", "2026-09-30", "granted"):
				self.assertIn(label, output)

	def test_duplicates_overlap_unknowns_and_no_mutation(self):
		new = self.matches(6, 2)
		new.append(deepcopy(new[0]))
		new[1]["minister"] = None
		new[2]["government_outcome"] = None
		earlier = self.matches(1, 0, 6)
		before = deepcopy((self.searches, new, earlier))
		result = build_alert_digest(self.searches, new, earlier)["searches"][0]
		self.assertEqual(result["new_counts"]["decisions"], 5)
		self.assertEqual(result["new_counts"]["minister_losses"], 1)
		self.assertEqual((self.searches, new, earlier), before)

	def test_partition_boundary_timezones_and_never_checked(self):
		rows = self.matches(3, 0)
		rows[0]["discovered_at"] = "2026-09-30T20:00:00-04:00"
		rows[1]["discovered_at"] = datetime(2026, 10, 1, tzinfo=timezone.utc)
		new, earlier = partition_matches(self.searches, rows)
		self.assertEqual([row["case_id"] for row in new], [3])
		self.assertEqual(len(earlier), 2)
		new, earlier = partition_matches([{"id": 1}], rows)
		self.assertEqual(len(new), 3)
		self.assertEqual(earlier, [])
		new, earlier = partition_matches(self.searches, rows, since="2026-10-03")
		self.assertEqual(new, [])
		self.assertEqual(len(earlier), 3)

	def test_empty_and_search_isolation(self):
		self.assertIn("No saved searches", render_digest_text(build_alert_digest([], [], [])))
		other = self.matches(5, 5)
		for row in other:
			row["search_id"] = 2
		result = build_alert_digest(self.searches, other, [])
		self.assertEqual(result["total_new_decisions"], 0)
		self.assertIn("No new decisions", render_digest_html(result))

	def test_record_fields_are_escaped_and_search_counts_independent(self):
		rows = self.matches(5, 2)
		for key in ("citation", "title", "court", "date", "decision_outcome"):
			rows[0][key] = '<img src=x onerror="bad">'
		searches = self.searches + [{"id": 2, "name": "Other"}]
		other = self.matches(6, 3, 101)
		for row in other:
			row["search_id"] = 2
		result = build_alert_digest(searches, rows + other, [])
		self.assertEqual([g["new_counts"]["decisions"] for g in result["searches"]], [5, 6])
		self.assertEqual(result["total_new_decisions"], 11)
		self.assertNotIn("<img", render_digest_html(result))
		self.assertIn("&lt;img", render_digest_html(result))


if __name__ == "__main__":
	unittest.main()
