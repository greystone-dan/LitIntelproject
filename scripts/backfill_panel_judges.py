"""Create one judge profile per panel member for multi-judge cases (SCC) and link them (dry-run by default).

SCC cases store the whole panel in one field ("Wagner, Richard; Abella, Rosalie; ..."). The first profile
backfill turned each distinct panel string into a single fake judge. This script splits the panel, finds
or creates one profile per judge, and links each case to every panel member. Existing profiles and links
are never edited or deleted; reruns add nothing new.

  python scripts/backfill_panel_judges.py                 # dry run, SCC
  python scripts/backfill_panel_judges.py --apply         # write (needs Daniel's go)
  python scripts/backfill_panel_judges.py --courts SCC FCA
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import select

from backend.database import Case, CaseJudgeProfile, JudgeProfile, SessionLocal
from backend.judge_normalization import JudgeName, parse_panel
from scripts.backfill_judge_profiles import judge_slug, normalize_judge_name


def _panel_string(case: Case) -> str:
	metadata = case.metadata_json if isinstance(case.metadata_json, dict) else {}
	reader = metadata.get("reader_extracted")
	return str(reader.get("judge") or "").strip() if isinstance(reader, dict) else ""


def backfill_panels(session, courts: list[str], *, apply: bool = False) -> dict[str, int]:
	profiles = {p.normalized_name: p for p in session.scalars(select(JudgeProfile))}
	existing_links = {(c, p) for c, p in session.execute(select(CaseJudgeProfile.case_id, CaseJudgeProfile.judge_profile_id))}
	stats: Counter = Counter()
	new_profiles: dict[str, JudgeProfile] = {}
	for case in session.scalars(select(Case).where(Case.court.in_(courts)).order_by(Case.id)):
		raw = _panel_string(case)
		if ";" not in raw:
			stats["cases_without_panel_field"] += 1
			continue
		stats["panel_cases"] += 1
		for judge in parse_panel(raw):
			key = normalize_judge_name(judge.name_text)
			profile = profiles.get(key) or new_profiles.get(key)
			if profile is None:
				profile = JudgeProfile(slug=judge_slug(key), display_name=f"Justice {judge.name_text}",
					normalized_name=key, primary_court=case.court, aliases=[judge.raw])
				new_profiles[key] = profile
				stats["profiles_created"] += 1
				if apply:
					session.add(profile)
					session.flush()
			if apply and (case.id, profile.id) not in existing_links:
				session.add(CaseJudgeProfile(case_id=case.id, judge_profile_id=profile.id, raw_name=judge.raw))
				existing_links.add((case.id, profile.id))
				stats["links_created"] += 1
			elif not apply:
				stats["links_would_create"] += 1
	if apply:
		session.commit()
	else:
		session.rollback()
	stats["distinct_judges"] = len({*new_profiles})
	return dict(stats)


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write profiles and links.")
	parser.add_argument("--courts", nargs="+", default=["SCC"])
	args = parser.parse_args()
	with SessionLocal() as session:
		for key, value in backfill_panels(session, args.courts, apply=args.apply).items():
			print(f"{key}={value}")


if __name__ == "__main__":
	main()
