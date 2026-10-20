"""Remove the redundant judge links the 2026-10-20 08:12 backfill_judge_profiles run added. Dry run by default.

That run wrote 28,584 case_judge_profiles rows (ids 158,683-187,266). On decisions that already had a link from
before the run (id <= 158,682) it added a second one because it only checks for the exact case + profile pair, not
for the same judge under another spelling. This script removes a new link only where its decision already had an
older link, Federal Court (FC) and Federal Court of Appeal (FCA) only. Supreme Court (SCC) is left alone: its extra
links belong to the panel-string profiles, which are a separate cleanup. New links on decisions with no older link
are never touched, and neither are older links or any judge profile.

  python scripts/remove_redundant_judge_links.py                              # dry run: pairs, counts, samples, checks
  python scripts/remove_redundant_judge_links.py --projected-csv out.csv      # also write every pair to a CSV
  python scripts/remove_redundant_judge_links.py --apply --expected-count N   # write the change log, then delete (needs Daniel's typed OK)
  python scripts/remove_redundant_judge_links.py --undo data/db_fix_backups/redundant_judge_links_<stamp>.jsonl

Junk guard: if an OLD link's profile name looks like junk (starts with and/order/judgment/reasons/schedule/annex/
appendix/between/style of cause, or holds a digit or U+FFFD, the K3 pattern), the decision is skipped and listed,
because the old link cannot be trusted as the keeper. The dry run then prints K7 (links per decision against the
ceilings FC 1, FCA 5), K10 (the same name twice on one decision) and K11 (two names sharing a surname) for the
database now and as it would be after the removal, plus before/after counts.

The change log (JSON lines) holds id, case_id, judge_profile_id, raw_name and created_at of every removed link.
--undo puts the rows back with the same ids and created_at, skipping any whose case or profile no longer exists.
Backup the table first. Orphaned backfill profiles (id > 1,694 with no links left) are a separate step.
"""

from __future__ import annotations

import argparse
import csv
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text

from backend.database import SessionLocal
from scripts.fix_common import default_undo_path, read_undo_file, write_undo_file

OLD_MAX_ID = 158682  # last link id that existed before the backfill run
RUN_MAX_ID = 187266  # last link id the backfill run wrote
COURTS = ("FC", "FCA")
CEILINGS = {"FC": 1, "FCA": 5}

# The K3 test from the step 2 known-answer checks, as Python.
JUNK_NAME_RE = re.compile(
	r"^\s*(and order|order|judgment|reasons|schedule|annex|appendix|between|style of cause)\b|[�0-9]", re.IGNORECASE
)
_TITLE_WORDS = {
	"the", "honourable", "hon", "justice", "juge", "chief", "mr", "mme", "madam", "madame", "mrs", "ms", "mister",
	"j", "ja", "jj", "cj", "pj", "ca", "de", "du", "la", "le", "of", "and", "et",
}

FETCH_SQL = text(
	"SELECT l.id, l.case_id, l.judge_profile_id, l.raw_name, l.created_at, c.court, c.citation, p.display_name "
	"FROM case_judge_profiles l JOIN cases c ON c.id = l.case_id JOIN judge_profiles p ON p.id = l.judge_profile_id "
	"WHERE c.court IN ('FC', 'FCA') "
	"AND l.case_id IN (SELECT case_id FROM case_judge_profiles WHERE id > :old_max AND id <= :run_max) "
	"AND l.case_id IN (SELECT case_id FROM case_judge_profiles WHERE id <= :old_max) "
	"ORDER BY l.case_id, l.id"
)
GLOBAL_COUNTS_SQL = text(
	"SELECT court, count(*) AS decisions, "
	"count(*) FILTER (WHERE n > CASE court WHEN 'FC' THEN 1 ELSE 5 END) AS over_ceiling "
	"FROM (SELECT c.court, l.case_id, count(*) AS n FROM case_judge_profiles l JOIN cases c ON c.id = l.case_id "
	"WHERE c.court IN ('FC', 'FCA') GROUP BY c.court, l.case_id) t GROUP BY court"
)
GLOBAL_K10_SQL = text(
	"SELECT court, count(*) AS decisions FROM (SELECT c.court, l.case_id FROM case_judge_profiles l "
	"JOIN cases c ON c.id = l.case_id JOIN judge_profiles p ON p.id = l.judge_profile_id "
	"WHERE c.court IN ('FC', 'FCA') GROUP BY c.court, l.case_id, lower(trim(p.display_name)) HAVING count(*) > 1) t "
	"GROUP BY court"
)
TOTAL_LINKS_SQL = text("SELECT count(*) FROM case_judge_profiles")


def is_junk_name(name: str | None) -> bool:
	return bool(name) and bool(JUNK_NAME_RE.search(name))


def surname_tokens(name: str | None) -> set[str]:
	"""Lowercase, accent-free name tokens without titles, initials and short particles (for the K11 diagnostic)."""
	folded = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()
	tokens = re.findall(r"[a-z]+", folded)
	return {t for t in tokens if len(t) >= 3 and t not in _TITLE_WORDS}


def group_by_case(rows: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
	cases: dict[int, list[dict[str, Any]]] = defaultdict(list)
	for row in rows:
		cases[row["case_id"]].append(row)
	return cases


def plan(rows: list[dict[str, Any]], old_max: int = OLD_MAX_ID, run_max: int = RUN_MAX_ID) -> dict[str, Any]:
	"""Pick the links to remove. Returns the removals (one dict per link, with the kept older links beside it) and skips."""
	removals: list[dict[str, Any]] = []
	skipped: list[dict[str, Any]] = []
	for case_id, links in group_by_case(rows).items():
		if links[0]["court"] not in COURTS:
			continue
		old = [l for l in links if l["id"] <= old_max]
		new = [l for l in links if old_max < l["id"] <= run_max]
		if not old or not new:
			continue
		junk_old = [l for l in old if is_junk_name(l["display_name"])]
		if junk_old:
			skipped.append({"case_id": case_id, "citation": links[0]["citation"], "court": links[0]["court"],
				"new_links": len(new), "junk_old_names": [l["display_name"] for l in junk_old]})
			continue
		for link in new:
			removals.append({**link, "kept": old})
	return {"removals": removals, "skipped": skipped}


def link_stats(links_by_case: dict[int, list[dict[str, Any]]]) -> dict[str, Counter]:
	"""K7 (over the FC/FCA ceiling), K10 (same name twice) and K11 (two names with a shared surname), counted by court."""
	stats = {"decisions": Counter(), "K7": Counter(), "K10": Counter(), "K11": Counter()}
	for links in links_by_case.values():
		if not links:
			continue
		court = links[0]["court"]
		stats["decisions"][court] += 1
		if len(links) > CEILINGS[court]:
			stats["K7"][court] += 1
		names = [(l["display_name"] or "").strip().lower() for l in links]
		if len(set(names)) < len(names):
			stats["K10"][court] += 1
		tokens = [surname_tokens(l["display_name"]) for l in links]
		if any(tokens[i] & tokens[j] for i in range(len(tokens)) for j in range(i + 1, len(tokens))):
			stats["K11"][court] += 1
	return stats


def projected_links(rows: list[dict[str, Any]], removals: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
	removed_ids = {r["id"] for r in removals}
	cases = group_by_case(rows)
	return {case_id: [l for l in links if l["id"] not in removed_ids] for case_id, links in cases.items()}


def csv_rows(removals: list[dict[str, Any]], after: dict[int, list[dict[str, Any]]], before: dict[int, list[dict[str, Any]]]):
	for r in removals:
		kept_tokens = [surname_tokens(k["display_name"]) for k in r["kept"]]
		yield {
			"case_id": r["case_id"], "citation": r["citation"], "court": r["court"],
			"removed_link_id": r["id"], "removed_profile_id": r["judge_profile_id"], "removed_name": r["display_name"],
			"removed_raw_name": r["raw_name"], "removed_is_junk": is_junk_name(r["display_name"]),
			"kept_profile_ids": " | ".join(str(k["judge_profile_id"]) for k in r["kept"]),
			"kept_names": " | ".join(k["display_name"] or "" for k in r["kept"]),
			"same_surname_as_a_kept_name": any(surname_tokens(r["display_name"]) & t for t in kept_tokens),
			"links_before": len(before[r["case_id"]]), "links_after": len(after[r["case_id"]]),
		}


def write_csv(path: Path, rows) -> int:
	fields = ["case_id", "citation", "court", "removed_link_id", "removed_profile_id", "removed_name", "removed_raw_name",
		"removed_is_junk", "kept_profile_ids", "kept_names", "same_surname_as_a_kept_name", "links_before", "links_after"]
	count = 0
	path.parent.mkdir(parents=True, exist_ok=True)
	with open(path, "x", encoding="utf-8", newline="") as handle:
		writer = csv.DictWriter(handle, fieldnames=fields)
		writer.writeheader()
		for row in rows:
			writer.writerow(row)
			count += 1
	return count


def format_pair(r: dict[str, Any]) -> str:
	kept = "; ".join(f"{k['display_name']!r} (profile {k['judge_profile_id']})" for k in r["kept"])
	return (f"  case {r['case_id']} {r['citation']} [{r['court']}] remove link {r['id']} -> {r['display_name']!r} "
		f"(profile {r['judge_profile_id']}, raw {r['raw_name']!r}); keep {kept}")


def global_counts(db) -> dict[str, dict[str, int]]:
	counts = {"decisions": {}, "K7": {}, "K10": {}}
	for row in db.execute(GLOBAL_COUNTS_SQL).mappings().all():
		counts["decisions"][row["court"]] = int(row["decisions"])
		counts["K7"][row["court"]] = int(row["over_ceiling"])
	for row in db.execute(GLOBAL_K10_SQL).mappings().all():
		counts["K10"][row["court"]] = int(row["decisions"])
	return counts


def print_report(db, rows, result, sample: int) -> None:
	removals, skipped = result["removals"], result["skipped"]
	before = group_by_case(rows)
	after = projected_links(rows, removals)
	by_court = Counter(r["court"] for r in removals)
	print(f"redundant_links_to_remove={len(removals)} (FC {by_court['FC']}, FCA {by_court['FCA']}) "
		f"decisions={len({r['case_id'] for r in removals})}")
	print(f"skipped_junk_old_link_decisions={len(skipped)} (new links not removed: {sum(s['new_links'] for s in skipped)})")
	for s in skipped[:20]:
		print(f"  skipped case {s['case_id']} {s['citation']} [{s['court']}] old junk names {s['junk_old_names']}")
	print(f"removed link is junk by the K3 pattern: {sum(is_junk_name(r['display_name']) for r in removals)}; "
		f"same surname as a kept name: {sum(row['same_surname_as_a_kept_name'] for row in csv_rows(removals, after, before))}")
	if removals:
		ordered = sorted(removals, key=lambda r: r["id"])
		print(f"link id range: {ordered[0]['id']} to {ordered[-1]['id']}")
		print("20 removals on decisions with the most links (largest):")
		for r in sorted(removals, key=lambda r: (-len(before[r["case_id"]]), r["id"]))[:sample]:
			print(format_pair(r))
		print(f"{sample} random removals (seed 0):")
		for r in random.Random(0).sample(removals, min(sample, len(removals))):
			print(format_pair(r))
		print("min and max link id:")
		print(format_pair(ordered[0]))
		print(format_pair(ordered[-1]))
	now_global = global_counts(db)
	touched = {r["case_id"] for r in removals}
	b = link_stats({c: l for c, l in before.items() if c in touched})
	a = link_stats({c: l for c, l in after.items() if c in touched})
	total = int(db.execute(TOTAL_LINKS_SQL).scalar() or 0)
	print(f"case_judge_profiles rows: before={total} after={total - len(removals)}")
	for check in ("K7", "K10"):
		for court in COURTS:
			now = now_global[check].get(court, 0)
			print(f"{check}{' (ceiling ' + str(CEILINGS[court]) + ')' if check == 'K7' else ''} {court}: "
				f"database now={now} projected={now - b[check][court] + a[check][court]}")
	for court in COURTS:
		print(f"K11 same-surname {court}: in affected decisions now={b['K11'][court]} projected={a['K11'][court]} "
			f"(diagnostic only: two judges can share a surname)")


def apply_removals(db, removals: list[dict[str, Any]], undo_path: Path) -> int:
	"""Write the change log first, then delete every listed link in one transaction; roll back on any mismatch."""
	ordered = sorted(removals, key=lambda r: r["id"])
	log = ({"id": r["id"], "case_id": r["case_id"], "judge_profile_id": r["judge_profile_id"],
		"raw_name": r["raw_name"], "created_at": r["created_at"]} for r in ordered)
	if write_undo_file(undo_path, log) != len(ordered):
		raise RuntimeError("change log is incomplete; nothing changed")
	deleted = 0
	try:
		for r in ordered:
			deleted += db.execute(
				text("DELETE FROM case_judge_profiles WHERE id = :id AND case_id = :case_id AND judge_profile_id = :profile_id"),
				{"id": r["id"], "case_id": r["case_id"], "profile_id": r["judge_profile_id"]},
			).rowcount or 0
		if deleted != len(ordered):
			raise RuntimeError(f"deleted {deleted} of {len(ordered)} listed links")
	except Exception:
		db.rollback()
		raise
	db.commit()
	return deleted


def restore(db, path: Path) -> tuple[int, int]:
	"""Re-insert the logged links with their original ids and created_at. Returns (inserted, listed)."""
	listed = inserted = 0
	for row in read_undo_file(path):
		listed += 1
		inserted += db.execute(
			text("INSERT INTO case_judge_profiles (id, case_id, judge_profile_id, raw_name, created_at) "
			"SELECT :id, :case_id, :judge_profile_id, :raw_name, CAST(:created_at AS timestamptz) "
			"WHERE EXISTS (SELECT 1 FROM cases WHERE id = :case_id) "
			"AND EXISTS (SELECT 1 FROM judge_profiles WHERE id = :judge_profile_id) ON CONFLICT DO NOTHING"),
			row,
		).rowcount or 0
	db.commit()
	return inserted, listed


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write the change log, then delete (default is a dry run).")
	parser.add_argument("--expected-count", type=int, help="With --apply: stop unless exactly this many links would be removed.")
	parser.add_argument("--undo", type=Path, help="Put back the links listed in this change log.")
	parser.add_argument("--undo-file", type=Path, help="Where --apply writes the change log (default data/db_fix_backups/).")
	parser.add_argument("--projected-csv", type=Path, help="Write every removal pair to this new CSV file.")
	parser.add_argument("--old-max-id", type=int, default=OLD_MAX_ID, help="Links with id up to this are the older ones to keep.")
	parser.add_argument("--run-max-id", type=int, default=RUN_MAX_ID, help="Last link id the backfill run wrote.")
	parser.add_argument("--sample", type=int, default=20, help="Rows in each dry-run sample.")
	args = parser.parse_args(argv)
	if args.apply and args.expected_count is None:
		parser.error("--apply needs --expected-count N (the redundant_links_to_remove number the dry run printed)")
	with SessionLocal() as db:
		if args.undo:
			inserted, listed = restore(db, args.undo)
			print(f"links_restored={inserted} of {listed} listed in {args.undo}")
			return 0
		rows = [dict(r) for r in db.execute(FETCH_SQL, {"old_max": args.old_max_id, "run_max": args.run_max_id}).mappings().all()]
		result = plan(rows, args.old_max_id, args.run_max_id)
		print_report(db, rows, result, args.sample)
		removals = result["removals"]
		if args.projected_csv:
			after = projected_links(rows, removals)
			print(f"projected_csv_rows={write_csv(args.projected_csv, csv_rows(removals, after, group_by_case(rows)))} file: {args.projected_csv}")
		if not args.apply:
			print("Dry run: nothing written. Add --apply --expected-count N to delete.")
			return 0
		if args.expected_count != len(removals):
			print(f"Expected {args.expected_count} but found {len(removals)}; nothing changed.")
			return 1
		undo_path = args.undo_file or default_undo_path("redundant_judge_links")
		print(f"links_removed={apply_removals(db, removals, undo_path)} change log: {undo_path}")
		print("Undo with: python scripts/remove_redundant_judge_links.py --undo", undo_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
