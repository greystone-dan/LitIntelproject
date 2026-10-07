"""Link refined citation rows (side table ``citations_refined``) to library cases.

Dry run by default: reports how many refined rows would link, by kind, and prints examples. ``--apply`` sets
``target_case_id`` on refined rows that resolve to exactly one case (never on the live ``citations`` table) and marks
unmatched formal citations ``unresolved``. Resumable: only rows still without a target are looked at. ``--revert --yes``
clears every link this script wrote for the refine version. Nothing on the site reads these rows unless
``CITATIONS_SOURCE=refined`` is set.
"""

from __future__ import annotations

import argparse
import random
import sys
from collections import Counter
from pathlib import Path

from sqlalchemy import select, update

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citation_refine.linking import LINKABLE_KINDS, build_case_key_index, resolve_refined_row
from backend.database import Case, CitationRefined, SessionLocal

REFINE_VERSION = 1


def main(argv: list[str] | None = None) -> None:
	parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
	parser.add_argument("--apply", action="store_true", help="Write links. Without it nothing is written.")
	parser.add_argument("--limit", type=int, default=None, help="Look at at most this many refined rows.")
	parser.add_argument("--refine-version", type=int, default=REFINE_VERSION)
	parser.add_argument("--batch-size", type=int, default=5_000)
	parser.add_argument("--examples", type=int, default=0, help="Print this many random linked examples.")
	parser.add_argument("--revert", action="store_true", help="Clear all links (and unresolved marks) for the version.")
	parser.add_argument("--yes", action="store_true", help="Confirm --revert.")
	args = parser.parse_args(argv)

	with SessionLocal() as session:
		if args.revert:
			if not args.yes:
				raise SystemExit("--revert needs --yes")
			cleared = session.execute(
				update(CitationRefined)
				.where(CitationRefined.refine_version == args.refine_version)
				.values(target_case_id=None, unresolved=True)
			).rowcount
			session.commit()
			print(f"REVERTED links on {cleared or 0} refined rows")
			return

		index = build_case_key_index(session.execute(select(Case.id, Case.citation, Case.secondary_citation)))
		print(f"case key index: {len(index)} keys")
		counts: Counter = Counter()
		examples: list[tuple] = []
		last_id = 0
		seen = 0
		while args.limit is None or seen < args.limit:
			take = args.batch_size if args.limit is None else min(args.batch_size, args.limit - seen)
			rows = session.execute(
				select(
					CitationRefined.id, CitationRefined.source_case_id, CitationRefined.citation_kind,
					CitationRefined.citation_text, CitationRefined.normalized_citation,
				)
				.where(CitationRefined.refine_version == args.refine_version, CitationRefined.target_case_id.is_(None), CitationRefined.id > last_id)
				.order_by(CitationRefined.id)
				.limit(take)
			).all()
			if not rows:
				break
			links: list[tuple[int, int]] = []
			unmatched: list[int] = []
			for row_id, source_id, kind, text, normalized in rows:
				last_id = row_id
				seen += 1
				if kind not in LINKABLE_KINDS:
					counts[f"{kind}: not linkable"] += 1
					continue
				target = resolve_refined_row(kind, text, normalized, source_id, index)
				if target is None:
					counts[f"{kind}: unmatched"] += 1
					unmatched.append(row_id)
				else:
					counts[f"{kind}: linked"] += 1
					links.append((row_id, target))
					if args.examples and len(examples) < 20_000:
						examples.append((row_id, kind, (text or "")[:80], target))
			if args.apply:
				for row_id, target in links:
					session.execute(update(CitationRefined).where(CitationRefined.id == row_id).values(target_case_id=target, unresolved=False))
				if unmatched:
					session.execute(update(CitationRefined).where(CitationRefined.id.in_(unmatched)).values(unresolved=True))
				session.commit()
		print(f"{'APPLIED' if args.apply else 'DRY RUN (nothing written)'} looked_at={seen} " + " ".join(f"[{k}={v}]" for k, v in sorted(counts.items())))
		for item in random.Random(1).sample(examples, min(args.examples, len(examples))):
			print(f"EXAMPLE refined_id={item[0]} kind={item[1]} text={item[2]!r} -> case {item[3]}")


if __name__ == "__main__":
	main()
