"""Index authoritative Justice Laws XML into section-addressable references."""

from __future__ import annotations

import argparse
import hashlib
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from sqlalchemy import delete, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import LEGISLATION_REGISTRY
from backend.database import LegislationDocument, LegislationSection, SessionLocal

XML_SOURCES = {
	"canada.irpa": ("Immigration and Refugee Protection Act", "I-2.5", "IRPA DATA/IRPA.xml"),
	"canada.irpr": ("Immigration and Refugee Protection Regulations", "SOR/2002-227", "IRPA DATA/IRPA-R.xml"),
	"canada.criminal_code": ("Criminal Code", "R.S.C. 1985, c. C-46", "legislation_xml/C-46.xml"),
	"canada.citizenship_act": ("Citizenship Act", "R.S.C. 1985, c. C-29", "legislation_xml/C-29.xml"),
	"canada.federal_courts_act": ("Federal Courts Act", "R.S.C. 1985, c. F-7", "legislation_xml/F-7.xml"),
	"canada.federal_courts_rules": ("Federal Courts Rules", "SOR/98-106", "legislation_xml/SOR-98-106.xml"),
	"canada.income_tax_act": ("Income Tax Act", "R.S.C. 1985, c. 1 (5th Supp.)", "legislation_xml/I-3.3.xml"),
	"canada.marine_liability_act": ("Marine Liability Act", "S.C. 2001, c. 6", "legislation_xml/M-0.7.xml"),
	"canada.commercial_arbitration_act": ("Commercial Arbitration Act", "R.S.C. 1985, c. C-34.6", "legislation_xml/C-34.6.xml"),
	"canada.coastal_fisheries_protection_act": ("Coastal Fisheries Protection Act", "R.S.C. 1985, c. C-33", "legislation_xml/C-33.xml"),
}


def parse_sections(path: Path) -> list[tuple[str, str | None, str]]:
	root = ET.parse(path).getroot()
	sections = []
	seen_numbers: set[str] = set()
	for section in root.iter("Section"):
		label = section.findtext("Label")
		if not label:
			continue
		number = label.strip()
		if number in seen_numbers:
			continue
		text = " ".join(" ".join(section.itertext()).split())
		seen_numbers.add(number)
		sections.append((number, section.findtext("MarginalNote"), text))
	return sections


def index_source(session, instrument_key: str, title: str, citation: str, path: Path) -> int:
	document = session.scalar(select(LegislationDocument).where(LegislationDocument.instrument_key == instrument_key))
	if document is None:
		document = LegislationDocument(instrument_key=instrument_key, title=title)
		session.add(document)
		session.flush()
	document.title = title
	document.citation = citation
	document.source_url = str(LEGISLATION_REGISTRY[instrument_key]["url"]).split("/section-")[0]
	document.local_path = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
	document.source_hash = hashlib.sha256(path.read_bytes()).hexdigest()
	session.execute(delete(LegislationSection).where(LegislationSection.document_id == document.id))
	rows = [
		LegislationSection(document_id=document.id, section_number=number, label=label, text=text, display_order=index)
		for index, (number, label, text) in enumerate(parse_sections(path))
	]
	session.add_all(rows)
	return len(rows)


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--instrument", choices=[*XML_SOURCES, "all"], default="all")
	args = parser.parse_args()
	with SessionLocal() as session:
		keys = XML_SOURCES if args.instrument == "all" else {args.instrument: XML_SOURCES[args.instrument]}
		for key, (title, citation, relative_path) in keys.items():
			count = index_source(session, key, title, citation, PROJECT_ROOT / "data" / "reference_library" / relative_path)
			print(f"{key}: sections={count}", flush=True)
		session.commit()


if __name__ == "__main__":
	main()