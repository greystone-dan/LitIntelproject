"""Tag the library's immigration decisions (2005 or later) with the rules + learned whose-position tagger.

READ-ONLY against the database (SELECT only, no commit). Writes one compact file per decision
(``<out>/case_<id>.json``, the shape ``backend/position_tags.py`` reads when ILIT_LEARNED_POSITIONS=1) and one summary
JSON. No model call, no network. Safe to stop and rerun: decisions already written are skipped unless --force.

    python scripts/run_position_tags_library.py --out data/position_learned --summary position-learned-summary.json
    python scripts/run_position_tags_library.py --out scratch_positions --summary scratch.json --sample 500   # dry run

Scope: courts FC, FCA, RAD, RPD, IAD; decision date 2005-01-01 or later; not French; immigration (the same test the
tagger was trained and measured on: title, tribunal, or the Immigration and Refugee Protection Act in the first 20,000
characters); at least one numbered paragraph.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
	sys.path.insert(0, str(REPO_ROOT))

from scripts.build_position_tags import tag_case  # noqa: E402
from scripts.train_learned_positions import is_immigration  # noqa: E402

COURTS = ("FC", "FCA", "RAD", "RPD", "IAD")
FIRST_DATE = date(2005, 1, 1)
BATCH = 200


def wanted(title: str, court: str, language: str | None, full_text: str | None) -> bool:
	return bool(full_text) and (language or "").lower() not in ("fr", "french") and is_immigration(title, court, full_text)


def run(session, out_dir: Path, limit: int = 0, sample: int = 0, force: bool = False, seed: int = 7) -> dict:
	from sqlalchemy import select

	from backend.database import Case

	ids = list(session.scalars(select(Case.id).where(Case.court.in_(COURTS), Case.date >= FIRST_DATE).order_by(Case.id)))
	if sample:
		random.Random(seed).shuffle(ids)
		ids = ids[:sample]
	out_dir.mkdir(parents=True, exist_ok=True)
	started = time.time()
	stats = {"candidates": len(ids), "written": 0, "skipped_existing": 0, "not_immigration_or_french": 0, "no_numbered_paragraphs": 0, "failed": 0}
	by_court: dict[str, Counter] = defaultdict(Counter)
	paragraphs_by_court: Counter = Counter()
	confidence_sum = 0.0
	confident = 0
	for start in range(0, len(ids), BATCH):
		if limit and stats["written"] >= limit:
			break
		rows = session.execute(select(Case.id, Case.title, Case.court, Case.language, Case.full_text).where(Case.id.in_(ids[start : start + BATCH])))
		for case_id, title, court, language, full_text in rows:
			path = out_dir / f"case_{case_id}.json"
			if path.exists() and not force:
				stats["skipped_existing"] += 1
				continue
			if not wanted(title or "", court or "", language, full_text):
				stats["not_immigration_or_french"] += 1
				continue
			try:
				tagged = tag_case({"id": case_id, "title": title, "full_text": full_text})
			except Exception:  # one bad decision must not stop the run
				stats["failed"] += 1
				continue
			if tagged is None:
				stats["no_numbered_paragraphs"] += 1
				continue
			path.write_text(json.dumps(tagged, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
			stats["written"] += 1
			for row in tagged["paragraphs"].values():
				by_court[court][row["h"]] += 1
				paragraphs_by_court[court] += 1
				confidence_sum += row["p"] or 0.0
				confident += (row["p"] or 0.0) >= 0.7
		print(f"{min(start + BATCH, len(ids))}/{len(ids)} candidates, {stats['written']} written, {time.time() - started:.0f}s", flush=True)
	total = sum(paragraphs_by_court.values()) or 1
	stats["paragraphs"] = sum(paragraphs_by_court.values())
	stats["share_at_least_0_7"] = round(confident / total, 3)
	stats["mean_probability"] = round(confidence_sum / total, 3)
	stats["holder_share_by_court"] = {c: {h: round(n / paragraphs_by_court[c], 3) for h, n in cnt.most_common()} for c, cnt in by_court.items()}
	stats["seconds"] = round(time.time() - started)
	return stats


def main(argv=None) -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--out", type=Path, required=True)
	parser.add_argument("--summary", type=Path, required=True)
	parser.add_argument("--limit", type=int, default=0, help="stop after this many files written")
	parser.add_argument("--sample", type=int, default=0, help="dry run on a random sample of this many candidates")
	parser.add_argument("--force", action="store_true")
	args = parser.parse_args(argv)
	from backend.database import SessionLocal

	with SessionLocal() as session:
		stats = run(session, args.out, args.limit, args.sample, args.force)
	args.summary.write_text(json.dumps(stats, indent=1) + "\n", encoding="utf-8")
	print(json.dumps({k: v for k, v in stats.items() if k != "holder_share_by_court"}, indent=1))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
