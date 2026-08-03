"""Select and import 25 transparent A2AJ refugee-risk evaluation cases."""
import re
from datetime import date, datetime
from hashlib import sha256
from pathlib import Path

import pyarrow.parquet as pq
from sqlalchemy import select

from backend.database import Case, SessionLocal

SOURCE = Path("data/raw/a2aj/FC/train.parquet")
PATTERNS = {
    "refoulement": r"(?i)non[- ]?refoulement|refoulement",
    "torture": r"(?i)torture|cruel|unusual punishment|ill[- ]?treatment",
    "persecution": r"(?i)persecution|well[- ]?founded fear",
    "removal": r"(?i)removal|deportation|risk on return",
    "protection": r"(?i)state protection|internal flight|IFA|alternative refuge",
}


def select_candidates() -> list[dict]:
	rows = []
	for batch in pq.ParquetFile(SOURCE).iter_batches(
		batch_size=1024,
		columns=["dataset", "citation_en", "citation2_en", "name_en", "document_date_en", "url_en", "scraped_timestamp_en", "unofficial_text_en", "cases_cited_en", "cases_citing_en", "citing_cases_count", "upstream_license"],
	):
		for record in batch.to_pylist():
			title = record.get("name_en") or ""
			text = record.get("unofficial_text_en") or ""
			full = f"{title}\n{text}"
			scores = {name: len(re.findall(pattern, full)) for name, pattern in PATTERNS.items()}
			score = sum(min(value, 5) for value in scores.values())
			if score and ("citizenship and immigration" in title.lower() or scores["refoulement"] or scores["torture"]):
				record["_score"] = score
				record["_scores"] = scores
				rows.append(record)
	rows.sort(key=lambda record: (-record["_score"], record.get("citation_en") or ""))
	return rows[:25]


def main() -> None:
	selected = select_candidates()
	with SessionLocal() as session:
		existing = set(session.scalars(select(Case.citation)).all())
		imported = 0
		for record in selected:
			text = record["unofficial_text_en"]
			citation = record.get("citation_en")
			if citation in existing:
				continue
			scraped = record.get("scraped_timestamp_en")
			case = Case(
				title=record["name_en"], court="FC", jurisdiction="Canada",
				date=record["document_date_en"].date() if isinstance(record["document_date_en"], datetime) else date.fromisoformat(str(record["document_date_en"])[:10]),
				citation=citation, secondary_citation=record.get("citation2_en"), full_text=text,
				source_url=record.get("url_en"), source_name="A2AJ Canadian Legal Data",
				source_id=citation or sha256(text.encode()).hexdigest(), source_type="a2aj_curated",
				dataset_version=scraped.isoformat() if scraped else None, scraped_at=scraped,
				upstream_license=record.get("upstream_license"), language="en",
				full_text_hash=sha256(text.encode("utf-8")).hexdigest(), processing_status="raw",
				cases_cited=record.get("cases_cited_en"), cases_citing=record.get("cases_citing_en"),
				citing_cases_count=record.get("citing_cases_count"),
				metadata_json={"evaluation_group": "non_refoulement", "selection_method": "keyword_score", "keyword_scores": record["_scores"], "verification_status": "a2aj_unverified"},
			)
			session.add(case)
			existing.add(citation)
			imported += 1
		session.commit()
	print(f"selected={len(selected)} imported={imported}")
	for record in selected:
		print(f"{record.get('citation_en')} | {record.get('name_en')} | score={record['_score']}")


if __name__ == "__main__":
	main()