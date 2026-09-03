"""Create canonical judge profiles from existing extracted case metadata."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseJudgeProfile, JudgeProfile, SessionLocal


def normalize_judge_name(value: str) -> str:
	text = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
	text = re.sub(r"\b(the\s+honourable|honourable|justice|judge|madam|mr\.?|mrs\.?)\b", " ", text, flags=re.IGNORECASE)
	return " ".join(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


def judge_slug(normalized_name: str) -> str:
	return f"judge-{normalized_name.replace(' ', '-')}"


def extracted_judge(case: Case) -> str:
	metadata = case.metadata_json or {}
	reader = metadata.get("reader_extracted") if isinstance(metadata, dict) else None
	value = reader.get("judge") if isinstance(reader, dict) else None
	return str(value or "").strip()


def is_profileable_judge(raw_name: str) -> bool:
	normalized_name = normalize_judge_name(raw_name)
	return bool(normalized_name) and len(raw_name) <= 255 and len(normalized_name) <= 230


def merge_duplicate_profiles(session, *, dry_run: bool = False) -> int:
	profiles = list(session.scalars(select(JudgeProfile).order_by(JudgeProfile.id)))
	groups: dict[str, list[JudgeProfile]] = {}
	for profile in profiles:
		groups.setdefault(profile.normalized_name, []).append(profile)
	merged = 0
	for normalized_name, duplicates in groups.items():
		if len(duplicates) < 2:
			continue
		canonical = next(
			(profile for profile in duplicates if profile.slug == judge_slug(normalized_name)),
			min(duplicates, key=lambda profile: profile.id),
		)
		for duplicate in duplicates:
			if duplicate is canonical:
				continue
			canonical.aliases = sorted({*(canonical.aliases or []), *(duplicate.aliases or []), duplicate.display_name})
			if canonical.primary_court is None:
				canonical.primary_court = duplicate.primary_court
			for link in list(duplicate.case_links):
				existing = session.scalar(
					select(CaseJudgeProfile).where(
						CaseJudgeProfile.case_id == link.case_id,
						CaseJudgeProfile.judge_profile_id == canonical.id,
					)
				)
				if existing is not None:
					session.delete(link)
				else:
					link.judge_profile_id = canonical.id
			session.delete(duplicate)
			merged += 1
	if dry_run:
		session.rollback()
	return merged


def backfill(dry_run: bool = False) -> dict[str, int]:
	with SessionLocal() as session:
		duplicate_profiles = merge_duplicate_profiles(session, dry_run=True)
		cases = list(session.scalars(select(Case).order_by(Case.id)))
		extracted = [(case, extracted_judge(case)) for case in cases]
		candidates = [(case, raw_name) for case, raw_name in extracted if is_profileable_judge(raw_name)]
		unresolved_values = [raw_name for _, raw_name in extracted if raw_name and not is_profileable_judge(raw_name)]
		profiles_by_name = {
			profile.normalized_name: profile
			for profile in session.scalars(select(JudgeProfile)).all()
		}
		existing_links = {
			(case_id, profile_id)
			for case_id, profile_id in session.execute(
				select(CaseJudgeProfile.case_id, CaseJudgeProfile.judge_profile_id)
			).all()
		}
		created_profiles = 0
		created_links = 0
		for case, raw_name in candidates:
			normalized_name = normalize_judge_name(raw_name)
			profile = profiles_by_name.get(normalized_name)
			if profile is None:
				profile = JudgeProfile(
					slug=judge_slug(normalized_name),
					display_name=raw_name,
					normalized_name=normalized_name,
					primary_court=case.court,
					aliases=[raw_name],
				)
				profiles_by_name[normalized_name] = profile
				created_profiles += 1
				if not dry_run:
					session.add(profile)
					session.flush()
			elif raw_name not in (profile.aliases or []):
				profile.aliases = sorted({*(profile.aliases or []), raw_name})
				if profile.primary_court is None:
					profile.primary_court = case.court
			if dry_run or (case.id, profile.id) in existing_links:
				continue
			session.add(CaseJudgeProfile(case_id=case.id, judge_profile_id=profile.id, raw_name=raw_name))
			existing_links.add((case.id, profile.id))
			created_links += 1
		if dry_run:
			session.rollback()
		else:
			session.commit()
		return {
			"cases_with_judges": len(candidates),
			"unresolved_extracted_values": len(unresolved_values),
			"judge_profiles_created": created_profiles,
			"case_links_created": created_links,
			"unique_raw_names": len(Counter(raw_name for _, raw_name in candidates)),
			"duplicate_profiles_found": duplicate_profiles,
		}


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--dry-run", action="store_true", help="Report changes without committing them.")
	parser.add_argument("--merge-duplicates", action="store_true", help="Relink and remove duplicate normalized profiles.")
	args = parser.parse_args()
	if args.merge_duplicates:
		with SessionLocal() as session:
			merged = merge_duplicate_profiles(session, dry_run=args.dry_run)
			if not args.dry_run:
				session.commit()
			print(f"duplicate_profiles_merged={merged}")
	for key, value in backfill(dry_run=args.dry_run).items():
		print(f"{key}={value}")


if __name__ == "__main__":
	main()