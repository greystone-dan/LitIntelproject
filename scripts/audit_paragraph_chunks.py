"""Read-only audit of paragraph chunk rows: hanging headings, glued headings, missing numbering.

For a seeded random sample of decisions per court it checks two row sets and prints per-court rates:
  stored  - the "paragraph" rows now in the database
  fresh   - the rows the current chunker would build from the decision text (``reader_paragraph_layout``)
A row is flagged when:
  hang_end   its last line is a heading ("II. Analysis", "DETERMINATION") that belongs to the next paragraph;
  hang_start a numbered paragraph row begins with heading text before its "[n]" marker;
  glued      a heading and "[n]" share a row start ("I. Overview [1] The Applicant...");
  gap        paragraph numbers skip or repeat;
  unnumbered the decision has no usable numbered paragraphs at all.
Nothing is written to the database. Examples:
  python scripts/audit_paragraph_chunks.py --court SCC --court FC --court FCA --per-court 100 --report audit.csv
  python scripts/audit_paragraph_chunks.py --text-json case_10452.json
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.chunk_cases import reader_paragraph_layout  # noqa: E402

_HEAD_LABEL_RE = re.compile(r"^(?:[IVX]+|[A-Z]|\d{1,2})\.\s+\S")
_PLAIN_HEAD_RE = re.compile(
    r"^(?:Analysis|Conclusion|Background|Issues?|Facts|Overview|Introduction|Decision|Disposition|Costs?)\b[^.]{0,60}$",
    re.IGNORECASE,
)
_UPPER_HEAD_RE = re.compile(r"^[A-ZÀ-Ý][A-ZÀ-Ý0-9 ,;:&’'()/\-]{3,80}$")
_NUMBERED_RE = re.compile(r"^\s*(?:\[\d{1,3}\]|\d{1,3}[.)]?\s)")
_LEAD_HEAD_RE = re.compile(r"^(?P<head>[^\n\[]{3,160}?)\s*\n?\s*\[(?P<n>\d{1,3})\]\s")
_CASES_PER_COURT = {"FC", "FCA", "SCC"}
ROW_KINDS = ("paragraph", "intro", "heading", "tail")


def is_heading_line(line: str) -> bool:
    line = line.strip()
    if not line or len(line) > 160 or _NUMBERED_RE.match(line):
        return False
    if line.endswith((".", ",", ";", "?", "!")) and not _HEAD_LABEL_RE.match(line):
        return False
    if _HEAD_LABEL_RE.match(line) and len(line.split()) <= 25 and not line.endswith((",", ";")):
        return True
    return bool(_PLAIN_HEAD_RE.match(line) or _UPPER_HEAD_RE.match(line))


def last_line(text: str) -> str:
    lines = [part for part in text.strip().split("\n") if part.strip()]
    return lines[-1] if lines else ""


SHORT_DECISION_CHARS = 6000  # a stub or leave-to-appeal entry may have fewer than 3 numbered paragraphs


def audit_rows(rows: list[dict], text_length: int = SHORT_DECISION_CHARS) -> dict:
    """rows: dicts with label ('intro'/'heading'/'tail'/paragraph number), text. Returns flag counts."""
    flags = Counter()
    last_num = None
    numbered = 0
    for row in rows:
        label, text = str(row["label"]), row["text"] or ""
        if label == "heading":
            continue
        if label in {"intro", "tail"}:
            if label == "intro" and is_heading_line(last_line(text)) and _HEAD_LABEL_RE.match(last_line(text).strip()):
                flags["hang_end"] += 1
            continue
        numbered += 1
        if is_heading_line(last_line(text)) and "\n" in text.strip():
            flags["hang_end"] += 1
        stripped = text.lstrip()
        if not stripped.startswith("["):
            if _LEAD_HEAD_RE.match(stripped):
                flags["glued"] += 1
            elif "\n" in stripped and is_heading_line(stripped.split("\n", 1)[0]):
                flags["hang_start"] += 1
        try:
            num = int(label)
        except ValueError:
            continue
        if last_num is not None and num != last_num + 1:
            flags["gap"] += 1
        last_num = num
    if numbered == 0 and text_length >= SHORT_DECISION_CHARS:
        flags["unnumbered"] += 1
    flags["rows"] = len(rows)
    return dict(flags)


def fresh_rows(text: str) -> list[dict]:
    rows = []
    for entry in reader_paragraph_layout(text):
        value = text[entry["start"] : entry["end"]].strip()
        if value:
            rows.append({"label": str(entry.get("num")) if entry["kind"] == "paragraph" else entry["kind"], "text": value})
    return rows


def stored_rows(session, case_id: int) -> list[dict]:
    from sqlalchemy import select

    from backend.database import CaseChunk

    found = session.execute(
        select(CaseChunk.chunk_label, CaseChunk.text)
        .where(CaseChunk.case_id == case_id, CaseChunk.chunk_set == "paragraph")
        .order_by(CaseChunk.chunk_index)
    ).all()
    return [{"label": label, "text": text} for label, text in found]


def sample_cases(session, court: str, per_court: int, year_from: int, seed: int) -> list[tuple[int, str]]:
    from sqlalchemy import extract, select

    from backend.database import Case

    query = select(Case.id).where(Case.court == court, Case.full_text.is_not(None))
    query = query.where(extract("year", Case.date) >= year_from)
    ids = [row[0] for row in session.execute(query)]
    random.Random(f"{seed}-{court}").shuffle(ids)
    return [(case_id, court) for case_id in ids[:per_court]]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--court", action="append", choices=sorted(_CASES_PER_COURT))
    parser.add_argument("--per-court", type=int, default=100)
    parser.add_argument("--year-from", type=int, default=2005)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--report", help="CSV with one row per decision")
    parser.add_argument("--text-json", nargs="*", help="offline: decision JSON files with court/full_text/paragraphs")
    args = parser.parse_args()

    results: list[dict] = []
    if args.text_json:
        for path in args.text_json:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
            stored = [{"label": row.get("paragraph_start") if row["text"][:1] == "[" else "intro", "text": row["text"]} for row in data["paragraphs"]]
            for source, rows in (("stored", stored), ("fresh", fresh_rows(data["full_text"]))):
                results.append({"case_id": data["case_id"], "court": data["court"], "source": source, **audit_rows(rows, len(data["full_text"]))})
    else:
        from backend.database import SessionLocal, Case

        with SessionLocal() as session:
            for court in args.court or sorted(_CASES_PER_COURT):
                for case_id, _ in sample_cases(session, court, args.per_court, args.year_from, args.seed):
                    text = session.get(Case, case_id).full_text or ""
                    for source, rows in (("stored", stored_rows(session, case_id)), ("fresh", fresh_rows(text))):
                        results.append({"case_id": case_id, "court": court, "source": source, **audit_rows(rows, len(text))})

    flag_names = ("hang_end", "hang_start", "glued", "gap", "unnumbered")
    print("court source decisions " + " ".join(f"{name}%" for name in flag_names) + "  any%")
    for court in sorted({row["court"] for row in results}):
        for source in ("stored", "fresh"):
            group = [row for row in results if row["court"] == court and row["source"] == source]
            if not group:
                continue
            cells = [f"{100 * sum(1 for row in group if row.get(name)) / len(group):.1f}" for name in flag_names]
            anyflag = 100 * sum(1 for row in group if any(row.get(name) for name in flag_names)) / len(group)
            print(f"{court:4} {source:6} {len(group):5} " + " ".join(f"{cell:>8}" for cell in cells) + f"  {anyflag:.1f}")
    if args.report and results:
        with open(args.report, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=["case_id", "court", "source", "rows", *flag_names])
            writer.writeheader()
            for row in results:
                writer.writerow({key: row.get(key, 0) for key in writer.fieldnames})


if __name__ == "__main__":
    main()
