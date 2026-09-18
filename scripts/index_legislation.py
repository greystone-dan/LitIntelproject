"""Index authoritative legal sources into section-addressable references."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

from bs4 import BeautifulSoup

from sqlalchemy import delete, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import LegislationDocument, LegislationSection, SessionLocal

@dataclass(frozen=True)
class SourceDefinition:
	title: str
	citation: str
	relative_path: str
	source_format: str
	source_url: str


XML_SOURCES = {
	"canada.irpa": SourceDefinition(
		title="Immigration and Refugee Protection Act",
		citation="I-2.5",
		relative_path="IRPA DATA/IRPA.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/I-2.5/",
	),
	"canada.irpr": SourceDefinition(
		title="Immigration and Refugee Protection Regulations",
		citation="SOR/2002-227",
		relative_path="IRPA DATA/IRPA-R.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/",
	),
	"canada.criminal_code": SourceDefinition(
		title="Criminal Code",
		citation="R.S.C. 1985, c. C-46",
		relative_path="legislation_xml/C-46.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/C-46/",
	),
	"canada.citizenship_act": SourceDefinition(
		title="Citizenship Act",
		citation="R.S.C. 1985, c. C-29",
		relative_path="legislation_xml/C-29.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/C-29/",
	),
	"canada.federal_courts_act": SourceDefinition(
		title="Federal Courts Act",
		citation="R.S.C. 1985, c. F-7",
		relative_path="legislation_xml/F-7.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/F-7/",
	),
	"canada.federal_courts_rules": SourceDefinition(
		title="Federal Courts Rules",
		citation="SOR/98-106",
		relative_path="legislation_xml/SOR-98-106.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/regulations/SOR-98-106/",
	),
	"canada.income_tax_act": SourceDefinition(
		title="Income Tax Act",
		citation="R.S.C. 1985, c. 1 (5th Supp.)",
		relative_path="legislation_xml/I-3.3.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/I-3.3/",
	),
	"canada.marine_liability_act": SourceDefinition(
		title="Marine Liability Act",
		citation="S.C. 2001, c. 6",
		relative_path="legislation_xml/M-0.7.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/M-0.7/",
	),
	"canada.commercial_arbitration_act": SourceDefinition(
		title="Commercial Arbitration Act",
		citation="R.S.C. 1985, c. C-34.6",
		relative_path="legislation_xml/C-34.6.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/C-34.6/",
	),
	"canada.coastal_fisheries_protection_act": SourceDefinition(
		title="Coastal Fisheries Protection Act",
		citation="R.S.C. 1985, c. C-33",
		relative_path="legislation_xml/C-33.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/C-33/",
	),
}

NON_XML_SOURCES = {
	"canada.charter": SourceDefinition(
		title="Canadian Charter of Rights and Freedoms",
		citation="Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982",
		relative_path="data/reference_library/non_xml_authorities/constitution_act_1982_page_12.html",
		source_format="html",
		source_url="https://laws-lois.justice.gc.ca/eng/const/page-12.html",
	),
	"international.refugee_convention": SourceDefinition(
		title="Convention Relating to the Status of Refugees",
		citation="Convention Relating to the Status of Refugees",
		relative_path="data/reference_library/non_xml_authorities/refugee_convention_1951_unts_189.txt",
		source_format="text",
		source_url="https://treaties.un.org/doc/Publication/UNTS/Volume%20189/volume-189-I-2545-English.pdf",
	),
	"international.refugee_protocol": SourceDefinition(
		title="Protocol Relating to the Status of Refugees",
		citation="Protocol Relating to the Status of Refugees",
		relative_path="data/reference_library/non_xml_authorities/refugee_protocol_1967_unts_606.txt",
		source_format="text",
		source_url="https://treaties.un.org/doc/Publication/UNTS/Volume%20606/volume-606-I-8791-English.pdf",
	),
}

SOURCE_DEFINITIONS = {**XML_SOURCES, **NON_XML_SOURCES}


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


def _heading_unit(text: str) -> tuple[str, str | None] | None:
	match = re.match(r"(?:Section|Article|Art\.)\s+([0-9]+[A-Za-z]?(?:\.[0-9]+)?|[IVXLCDM]+)(?:\s*[-:]?\s*(.*))?$", text)
	if match is None:
		return None
	return match.group(1), (match.group(2) or None)


def parse_html_sections(path: Path) -> list[tuple[str, str | None, str]]:
	soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
	charter_part = next(
		(
			element
			for element in soup.find_all("h2", class_="Part")
			if "Canadian Charter of Rights and Freedoms" in element.get_text(" ", strip=True)
		),
		None,
	)
	justice_sections = soup.select("p.Section, p.Subsection")
	if justice_sections and (charter_part is not None or soup.select_one("a.sectionLabel") is not None):
		sections: list[tuple[str, str | None, str]] = []
		seen_numbers: set[str] = set()
		current_label: str | None = None
		elements = soup.find_all(["h2", "h3", "p", "ul", "ol"])
		if charter_part is not None:
			start = elements.index(charter_part)
			elements = elements[start:]
		for element in elements:
			if element is not charter_part and element.name == "h2" and "Part" in (element.get("class") or []):
				break
			if element.name == "h3" and "Subheading" in (element.get("class") or []):
				current_label = element.get_text(" ", strip=True)
				continue
			if element.name == "p" and element.select_one("a.sectionLabel") is not None:
				anchor = element.select_one("a.sectionLabel")
				number = anchor.get_text(" ", strip=True)
				if not number or number in seen_numbers:
					continue
				body = element.get_text(" ", strip=True)
				body = re.sub(rf"^{re.escape(number)}\s*", "", body)
				sections.append((number, current_label, body))
				seen_numbers.add(number)
			elif sections and element.name in {"ul", "ol"}:
				text = element.get_text(" ", strip=True)
				if text:
					number, label, body = sections[-1]
					sections[-1] = (number, label, f"{body} {text}".strip())
		return sections
	blocks = [element.get_text(" ", strip=True) for element in soup.find_all(["h1", "h2", "h3", "h4", "p", "li"])]
	sections: list[tuple[str, str | None, str]] = []
	current: tuple[str, str | None, list[str]] | None = None
	seen_numbers: set[str] = set()
	for block in blocks:
		unit = _heading_unit(block)
		if unit is not None:
			if current is not None:
				number, label, text = current
				if number not in seen_numbers and text:
					sections.append((number, label, " ".join(text)))
					seen_numbers.add(number)
			number, label = unit
			current = (number, label, [])
		elif current is not None:
			current[2].append(block)
	if current is not None:
		number, label, text = current
		if number not in seen_numbers and text:
			sections.append((number, label, " ".join(text)))
	return sections


def parse_text_sections(path: Path) -> list[tuple[str, str | None, str]]:
	sections: list[tuple[str, str | None, str]] = []
	current: tuple[str, str | None, list[str]] | None = None
	seen_numbers: set[str] = set()
	for raw_line in path.read_text(encoding="utf-8").splitlines():
		line = " ".join(raw_line.split())
		if not line:
			continue
		unit = _heading_unit(line)
		if unit is not None:
			if current is not None:
				number, label, text = current
				if number not in seen_numbers and text:
					sections.append((number, label, " ".join(text)))
					seen_numbers.add(number)
			number, label = unit
			current = (number, label, [])
		elif current is not None:
			current[2].append(line)
	if current is not None:
		number, label, text = current
		if number not in seen_numbers and text:
			sections.append((number, label, " ".join(text)))
	return sections


def parse_source_sections(path: Path, source_format: str) -> list[tuple[str, str | None, str]]:
	if source_format == "xml":
		return parse_sections(path)
	if source_format == "html":
		return parse_html_sections(path)
	if source_format == "text":
		return parse_text_sections(path)
	raise ValueError(f"unsupported source format: {source_format}")


def index_source(session, instrument_key: str, source: SourceDefinition) -> int:
	path = PROJECT_ROOT / source.relative_path
	document = session.scalar(select(LegislationDocument).where(LegislationDocument.instrument_key == instrument_key))
	if document is None:
		document = LegislationDocument(instrument_key=instrument_key, title=source.title)
		session.add(document)
		session.flush()
	document.title = source.title
	document.citation = source.citation
	document.source_url = source.source_url
	document.local_path = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
	document.source_hash = hashlib.sha256(path.read_bytes()).hexdigest()
	session.execute(delete(LegislationSection).where(LegislationSection.document_id == document.id))
	rows = [
		LegislationSection(document_id=document.id, section_number=number, label=label, text=text, display_order=index)
		for index, (number, label, text) in enumerate(parse_source_sections(path, source.source_format))
	]
	session.add_all(rows)
	return len(rows)


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--instrument", choices=[*SOURCE_DEFINITIONS, "all"], default="all")
	args = parser.parse_args()
	with SessionLocal() as session:
		keys = SOURCE_DEFINITIONS if args.instrument == "all" else {args.instrument: SOURCE_DEFINITIONS[args.instrument]}
		for key, source in keys.items():
			count = index_source(session, key, source)
			print(f"{key}: sections={count}", flush=True)
		session.commit()


if __name__ == "__main__":
	main()