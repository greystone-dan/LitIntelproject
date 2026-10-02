"""Shadow-mode comparison of pass-one citation extraction and the step-2 refinement layers.

Never writes to the database. Two input modes:

  --text-file PATH        a decision as .txt or .html (no database needed)
  --case-id N / --limit N decisions from the database (read-only)

With --resolve (database mode) it also links rows to cases, paragraphs and
statute provisions, and reports how many more reach each level than pass one.

Outputs go to --output-dir (default data/eval/reports/citation_refinement):
  rows.csv      every refined/dropped row with its step, action and notes
  summary.json  counts by step/action and, with --resolve, linking statuses
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from dataclasses import replace
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citation_refine import ALL_STEPS, refine_document  # noqa: E402
from backend.citation_refine.models import PINPOINT_PARAGRAPH, Pinpoint  # noqa: E402
from backend.citation_refine.resolution import resolve_case_rows, resolve_statute_rows  # noqa: E402

DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data" / "eval" / "reports" / "citation_refinement"
# The paragraph rule used today by scripts/link_citation_pinpoints.py: first number only.
CURRENT_PINPOINT_RE = re.compile(r"(?:at\s+)?(?:para(?:s|graph(?:s)?)?\.?|paragraph(?:s)?)\s+(\d+)", re.IGNORECASE)

ROW_FIELDS = [
	"source",
	"layer",
	"step",
	"action",
	"kind",
	"offset_start",
	"offset_end",
	"citation_text",
	"normalized_citation",
	"confidence",
	"notes",
	"identifiers_or_instrument",
	"provision_or_pinpoints",
	"replaces",
]


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	source = parser.add_mutually_exclusive_group(required=True)
	source.add_argument("--text-file", action="append", type=Path, help="Decision text (.txt or .html). Repeatable.")
	source.add_argument("--case-id", action="append", type=int, help="Case id from the database. Repeatable.")
	source.add_argument("--limit", type=int, help="First N cases with full text from the database.")
	parser.add_argument("--offset", type=int, default=0, help="Skip this many cases with --limit.")
	parser.add_argument("--resolve", action="store_true", help="Link rows to cases, paragraphs and provisions (database mode).")
	parser.add_argument("--steps", default="all", help='Comma list of steps, or "all". Known: ' + ", ".join(ALL_STEPS))
	parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
	return parser.parse_args()


def read_text_file(path: Path) -> str:
	raw = path.read_text(encoding="utf-8", errors="replace")
	if path.suffix.lower() in {".html", ".htm"}:
		from bs4 import BeautifulSoup

		return BeautifulSoup(raw, "html.parser").get_text("\n")
	return raw


def row_record(source: str, layer: str, row) -> dict[str, object]:
	if layer == "cases":
		identifiers = " | ".join(row.identifiers)
		detail = "; ".join(f"{pin.kind}:{','.join(map(str, pin.values))}" for pin in row.pinpoints)
	else:
		identifiers = row.instrument_key or ""
		detail = row.provision or ""
	return {
		"source": source,
		"layer": layer,
		"step": row.step,
		"action": row.action,
		"kind": row.kind,
		"offset_start": row.offset_start,
		"offset_end": row.offset_end,
		"citation_text": " ".join(row.citation_text.split()),
		"normalized_citation": row.normalized_citation,
		"confidence": row.confidence,
		"notes": "; ".join(row.notes),
		"identifiers_or_instrument": identifiers,
		"provision_or_pinpoints": detail,
		"replaces": "; ".join(f"{start}-{end}" for start, end, _text in row.replaces),
	}


def current_style_pinpoints(rows):
	"""Mimic today's linking: only the first paragraph number in the citation text."""
	adjusted = []
	for row in rows:
		match = CURRENT_PINPOINT_RE.search(row.citation_text)
		pins = (Pinpoint(PINPOINT_PARAGRAPH, match.group(0), (int(match.group(1)),)),) if match else ()
		adjusted.append(replace(row, pinpoints=pins))
	return adjusted


def main() -> int:
	args = parse_args()
	steps = None if args.steps.strip().lower() == "all" else [part.strip() for part in args.steps.split(",") if part.strip()]
	args.output_dir.mkdir(parents=True, exist_ok=True)
	records: list[dict[str, object]] = []
	counts: Counter[str] = Counter()
	resolution: dict[str, Counter[str]] = {name: Counter() for name in ("baseline_cases", "refined_cases", "baseline_pinpoints", "refined_pinpoints", "baseline_laws", "refined_laws")}

	documents: list[tuple[str, str, list[str | None]]] = []
	session = None
	if args.text_file:
		for path in args.text_file:
			documents.append((str(path), read_text_file(path), []))
		if args.resolve:
			print("--resolve needs the database; ignored for --text-file input.", file=sys.stderr)
	else:
		from sqlalchemy import select

		from backend.database import Case, SessionLocal

		session = SessionLocal()
		query = select(Case.id, Case.full_text, Case.citation, Case.secondary_citation).where(Case.full_text.is_not(None))
		if args.case_id:
			query = query.where(Case.id.in_(args.case_id))
		else:
			query = query.order_by(Case.id).offset(args.offset).limit(args.limit)
		for case_id, full_text, citation, secondary in session.execute(query):
			documents.append((f"case:{case_id}", full_text or "", [citation, secondary]))

	lookups = None
	if session is not None and args.resolve:
		from backend.citation_refine.resolution import load_case_index, paragraph_lookup_from_session, statute_lookups_from_session

		lookups = (load_case_index(session), paragraph_lookup_from_session(session), *statute_lookups_from_session(session))

	try:
		for source, text, own_citations in documents:
			refined = refine_document(text, steps=steps, source_citations=own_citations)
			for layer_name, layer in (("cases", refined.cases), ("laws", refined.laws)):
				for row in [*layer.rows, *layer.dropped]:
					records.append(row_record(source, layer_name, row))
					counts[f"{layer_name}:{row.step}:{row.action}"] += 1
			if lookups is None:
				continue
			case_index, paragraph_lookup, has_document, get_section = lookups
			baseline = refine_document(text, steps=(), source_citations=own_citations)
			for label, rows in (("baseline", current_style_pinpoints(baseline.cases.rows)), ("refined", refined.cases.rows)):
				for result in resolve_case_rows(rows, case_index, paragraph_lookup):
					resolution[f"{label}_cases"][result.status] += 1
					resolution[f"{label}_pinpoints"][result.pinpoint_status] += 1
			for label, rows in (("baseline", baseline.laws.rows), ("refined", refined.laws.rows)):
				for result in resolve_statute_rows(rows, has_document, get_section):
					resolution[f"{label}_laws"][result.status] += 1
	finally:
		if session is not None:
			session.close()

	rows_path = args.output_dir / "rows.csv"
	with rows_path.open("w", encoding="utf-8", newline="") as handle:
		writer = csv.DictWriter(handle, fieldnames=ROW_FIELDS)
		writer.writeheader()
		writer.writerows(records)
	summary = {
		"documents": len(documents),
		"steps": "all" if steps is None else steps,
		"counts": dict(sorted(counts.items())),
		"resolution": {name: dict(sorted(counter.items())) for name, counter in resolution.items() if counter},
	}
	summary_path = args.output_dir / "summary.json"
	summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
	print(json.dumps(summary, indent=2))
	print(f"rows={rows_path} summary={summary_path}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
