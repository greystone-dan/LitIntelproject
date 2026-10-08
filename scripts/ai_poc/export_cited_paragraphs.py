"""Read-only: fetch the pinpointed paragraph text of cited decisions that are in our library. SELECTs only, no database writes, no OpenAI.

Input CSV columns: row_id, neutral_citation, para_start, para_end. Output JSON: one record per row with the library case id and the text of the
paragraphs para_start..para_end (the decision's own numbers as stored in case_chunks.paragraph_start/end), or found=false.
Run on the PC: python scripts\\ai_poc\\export_cited_paragraphs.py --in cited.csv --out cited_paragraphs.json
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import or_, select  # noqa: E402

from backend.database import Case, CaseChunk, SessionLocal  # noqa: E402


def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--in", dest="inp", type=Path, required=True)
	ap.add_argument("--out", type=Path, required=True)
	args = ap.parse_args()
	out = []
	with SessionLocal() as session:
		for row in csv.DictReader(args.inp.open(encoding="utf-8-sig")):
			cite = row["neutral_citation"].strip()
			lo, hi = int(row["para_start"]), int(row.get("para_end") or row["para_start"])
			case = session.execute(select(Case.id, Case.title).where(or_(Case.citation == cite, Case.secondary_citation == cite)).limit(1)).first()
			rec = {"row_id": row["row_id"], "citation": cite, "para_start": lo, "para_end": hi, "found": False}
			if case:
				chunks = session.execute(
					select(CaseChunk.paragraph_start, CaseChunk.paragraph_end, CaseChunk.text)
					.where(CaseChunk.case_id == case.id, CaseChunk.chunk_set == "paragraph", CaseChunk.paragraph_start <= hi, CaseChunk.paragraph_end >= lo)
					.order_by(CaseChunk.paragraph_start)).all()
				rec.update({"case_id": case.id, "title": case.title, "found": bool(chunks), "text": "\n\n".join(c.text for c in chunks)[:3000]})
			out.append(rec)
	args.out.write_text(json.dumps(out, indent=1), encoding="utf-8")
	print(json.dumps({"rows": len(out), "found": sum(r["found"] for r in out)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
