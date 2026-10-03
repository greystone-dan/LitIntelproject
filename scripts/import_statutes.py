#!/usr/bin/env python3
"""
Importer for Canadian federal statutes from Justice Laws XML (justice.gc.ca).

Imports statute text with versioning information (in-force dates) for:
- Immigration and Refugee Protection Act (IRPA)
- Immigration and Refugee Protection Regulations (IRPR)
- Citizenship Act
- Customs Act
- Federal Courts Act
- Federal Courts Rules
- Canadian Charter of Rights and Freedoms

Uses: justice.gc.ca REST API for statute versions and text.
License: Open Government License (Canada)
"""

import gzip
import json
import logging
import re
from datetime import date, datetime
from io import BytesIO
from pathlib import Path
from xml.etree import ElementTree as ET

import httpx
from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.database import SessionLocal, Statute, StatuteVersion, StatuteSection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# CBSA and immigration-relevant federal statutes with expansion phase
CBSA_IMMIGRATION_STATUTES = {
	# Phase 1: Core CBSA and immigration statutes (7)
	"IRPA": {
		"title": "Immigration and Refugee Protection Act",
		"short_title": "IRPA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/i-2.5/",
		"phase": 1,
	},
	"IRPR": {
		"title": "Immigration and Refugee Protection Regulations",
		"short_title": "IRPR",
		"jurisdiction": "Federal",
		"statute_type": "Regulation",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/",
		"phase": 1,
	},
	"CA": {
		"title": "Citizenship Act",
		"short_title": "CA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/c-29/",
		"phase": 1,
	},
	"CustA": {
		"title": "Customs Act",
		"short_title": "Customs Act",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/r-8.88/",
		"phase": 1,
	},
	"FCA": {
		"title": "Federal Courts Act",
		"short_title": "FCA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/f-7/",
		"phase": 1,
	},
	"FCR": {
		"title": "Federal Courts Rules",
		"short_title": "FCR",
		"jurisdiction": "Federal",
		"statute_type": "Rules",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-98-106/",
		"phase": 1,
	},
	"Charter": {
		"title": "Canadian Charter of Rights and Freedoms",
		"short_title": "Charter",
		"jurisdiction": "Federal",
		"statute_type": "Constitutional",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/const/page-12.html",
		"phase": 1,
	},
	# Phase 2: Additional CBSA-relevant acts and regulations (10)
	"CBSAA": {
		"title": "Canada Border Services Agency Act",
		"short_title": "CBSAA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/c-1.4/",
		"phase": 2,
	},
	"CReg": {
		"title": "Citizenship Regulations",
		"short_title": "CReg",
		"jurisdiction": "Federal",
		"statute_type": "Regulation",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-93-100/",
		"phase": 2,
	},
	"CustTariff": {
		"title": "Customs Tariff",
		"short_title": "Customs Tariff",
		"jurisdiction": "Federal",
		"statute_type": "Schedule",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/c-54.011/",
		"phase": 2,
	},
	"RPDIRR": {
		"title": "Refugee Protection Division Rules",
		"short_title": "RPD Rules",
		"jurisdiction": "Federal",
		"statute_type": "Rules",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-228/",
		"phase": 2,
	},
	"RADIRR": {
		"title": "Refugee Appeal Division Rules",
		"short_title": "RAD Rules",
		"jurisdiction": "Federal",
		"statute_type": "Rules",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-230/",
		"phase": 2,
	},
	"IDRR": {
		"title": "Immigrant Appeal Division Rules",
		"short_title": "IAD Rules",
		"jurisdiction": "Federal",
		"statute_type": "Rules",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-229/",
		"phase": 2,
	},
	"FCRR": {
		"title": "Federal Courts Citizenship and Immigration Rules",
		"short_title": "FCCIRules",
		"jurisdiction": "Federal",
		"statute_type": "Rules",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-98-106/",
		"phase": 2,
	},
	"PA": {
		"title": "Privacy Act",
		"short_title": "PA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/p-21/",
		"phase": 2,
	},
	"ATIA": {
		"title": "Access to Information Act",
		"short_title": "ATIA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/a-1/",
		"phase": 2,
	},
	"CEA": {
		"title": "Canada Evidence Act",
		"short_title": "CEA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/c-5/",
		"phase": 2,
	},
	"IA": {
		"title": "Interpretation Act",
		"short_title": "IA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/i-21/",
		"phase": 2,
	},
	# Criminal Code provisions referenced in inadmissibility (partial)
	"CC": {
		"title": "Criminal Code",
		"short_title": "CC",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/c-46/",
		"phase": 2,
	},
}

# Legacy alias for backward compatibility
PHASE1_STATUTES = {k: v for k, v in CBSA_IMMIGRATION_STATUTES.items() if v.get("phase") == 1}


class JusticeLawsXMLClient:
	"""Client for fetching statute text from justice.gc.ca."""

	BASE_URL = "https://laws-lois.justice.gc.ca"
	TIMEOUT = 30
	XML_SUFFIX = "FullText"  # Suffix for XML version of statute

	def __init__(self):
		self.client = httpx.Client(timeout=self.TIMEOUT, follow_redirects=True)

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.client.close()

	def fetch_statute_xml(self, instrument_key: str, xml_url: str) -> ET.Element | None:
		"""Fetch and parse statute XML from justice.gc.ca."""
		try:
			logger.info(f"Fetching XML for {instrument_key} from {xml_url}...")
			response = self.client.get(xml_url)
			if response.status_code == 200:
				root = ET.fromstring(response.content)
				return root
			else:
				logger.warning(f"Status {response.status_code} for {instrument_key} XML")
				return None
		except Exception as e:
			logger.error(f"Error fetching XML for {instrument_key}: {e}")
			return None

	def extract_statute_text_from_xml(self, root: ET.Element) -> str | None:
		"""Extract statute text from justice.gc.ca XML."""
		try:
			# Get all text elements from the statute
			text_parts = []
			for elem in root.iter():
				if elem.text and elem.text.strip():
					text_parts.append(elem.text.strip())
			return "\n".join(text_parts) if text_parts else None
		except Exception as e:
			logger.error(f"Error extracting text from XML: {e}")
			return None

	def extract_metadata_from_xml(self, root: ET.Element) -> dict:
		"""Extract metadata (dates, version info) from statute XML."""
		metadata = {}
		ns = {'lims': 'http://justice.gc.ca/lims'}

		# Extract point-in-time date
		pit_date = root.attrib.get('{http://justice.gc.ca/lims}pit-date')
		if pit_date:
			metadata['pit_date'] = pit_date

		# Extract in-force start date
		inforce_date = root.attrib.get('{http://justice.gc.ca/lims}inforce-start-date')
		if inforce_date:
			metadata['inforce_start_date'] = inforce_date

		# Check if there are previous versions
		has_prev = root.attrib.get('hasPreviousVersion', 'false') == 'true'
		metadata['has_previous_versions'] = has_prev

		return metadata

	def fetch_pitindex_versions(self, instrument_key: str, statute_url: str) -> list[dict]:
		"""
		Fetch historical versions from PITIndex.html.
		Returns list of dicts with pit_date, in_force_date, end_date, url.
		"""
		try:
			code = re.search(r'/(?:acts|regulations)/([^/]+)', statute_url)
			if not code:
				return []

			statute_type = "acts" if "/acts/" in statute_url else "regulations"
			pitindex_url = f"{self.BASE_URL}/eng/{statute_type}/{code.group(1)}/PITIndex.html"

			logger.info(f"Fetching PITIndex from {pitindex_url}...")
			response = self.client.get(pitindex_url)
			if response.status_code != 200:
				logger.warning(f"Could not fetch PITIndex (status {response.status_code})")
				return []

			versions = []
			# Pattern: <li><a href='20260326/P1TT3xt3.html'>From 2026-03-26 to 2026-09-21</a></li>
			pattern = r'<li><a href=[\'"](\d{8})/P1TT3xt3\.html[\'"]>From (\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})</a></li>'

			for match in re.finditer(pattern, response.text):
				pit_date_str = match.group(1)
				start_str = match.group(2)
				end_str = match.group(3)

				try:
					pit_date = datetime.strptime(pit_date_str, "%Y%m%d").date()
					start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
					end_date = datetime.strptime(end_str, "%Y-%m-%d").date()

					version_url = f"{self.BASE_URL}/eng/{statute_type}/{code.group(1)}/{pit_date_str}/P1TT3xt3.xml"

					versions.append({
						'pit_date': pit_date,
						'in_force_date': start_date,
						'end_date': end_date,
						'url': version_url,
					})
				except Exception as e:
					logger.warning(f"Could not parse version entry: {e}")

			logger.info(f"Found {len(versions)} historical versions for {instrument_key}")
			return versions

		except Exception as e:
			logger.error(f"Error fetching PITIndex: {e}")
			return []


def parse_statute_sections_from_xml(root: ET.Element) -> list[dict]:
	"""
	Parse sections from statute XML.
	Extracts Section elements with their numbers, headings, and text.
	"""
	sections = []
	offset = 0
	ns = {'lims': 'http://justice.gc.ca/lims'}

	# Find all Section elements in the statute
	for section_elem in root.findall('.//Section', ns):
		section_num = section_elem.attrib.get('sid', '').split('/')[-1] if 'sid' in section_elem.attrib else None

		# Try to get section number from text content
		if not section_num:
			for child in section_elem:
				if 'sectionLabel' in child.tag.lower():
					section_num = child.text
					break

		# Extract heading
		heading = ''
		heading_elem = section_elem.find('.//Heading')
		if heading_elem is not None and heading_elem.text:
			heading = heading_elem.text

		# Extract full text by joining all text content
		text_parts = []
		for elem in section_elem.iter():
			if elem.text and elem.text.strip():
				text_parts.append(elem.text.strip())
		section_text = '\n'.join(text_parts)

		if section_num or section_text:
			section_dict = {
				'section_number': section_num or f'Section {len(sections) + 1}',
				'subsection': None,
				'paragraph': None,
				'heading': heading,
				'text': section_text[:5000],  # Limit to 5000 chars per section
				'offset_start': offset,
				'offset_end': offset + len(section_text),
			}
			sections.append(section_dict)
			offset += len(section_text)

	return sections if sections else []


def parse_statute_sections(statute_text: str) -> list[dict]:
	"""
	Fallback: parse statute text into sections.
	Returns list of section dicts with number, heading, text, and offsets.
	"""
	sections = []
	lines = statute_text.split("\n")
	current_section = None
	current_offset = 0

	for line_text in lines:
		# Match section headers: "1.", "2", "Section 1", "Schedule A", etc.
		section_match = re.match(
			r"^\s*(?:Section\s+)?([0-9]+(?:\.[0-9]+)?|Schedule\s+[A-Z]+)\.?\s*(?:\(([a-z])\))?\s*(.*)$",
			line_text.strip(),
		)

		if section_match and not current_section:
			# Start new section
			section_num = section_match.group(1)
			subsection = section_match.group(2)
			heading = section_match.group(3).strip()

			current_section = {
				"section_number": section_num,
				"subsection": subsection,
				"paragraph": None,
				"heading": heading,
				"text": "",
				"offset_start": current_offset,
				"offset_end": None,
			}
		elif current_section:
			current_section["text"] += line_text + "\n"

		current_offset += len(line_text) + 1

	# Save last section
	if current_section:
		current_section["offset_end"] = current_offset
		sections.append(current_section)

	return sections if sections else []


def import_statute_from_xml(
	db: Session,
	instrument_key: str,
	statute_info: dict,
	xml_root: ET.Element,
	metadata: dict,
	client: JusticeLawsXMLClient | None = None,
) -> Statute | None:
	"""
	Import a single statute version from XML into the database.
	"""
	try:
		# Extract statute text
		if client:
			statute_text = client.extract_statute_text_from_xml(xml_root)
		else:
			# Fallback: extract text directly
			text_parts = []
			for elem in xml_root.iter():
				if elem.text and elem.text.strip():
					text_parts.append(elem.text.strip())
			statute_text = "\n".join(text_parts) if text_parts else None

		if not statute_text or len(statute_text) < 100:
			logger.warning(f"Statute text too short for {instrument_key}, skipping")
			return None

		# Get version date from metadata
		version_date_str = metadata.get('pit_date') or metadata.get('inforce_start_date')
		if not version_date_str:
			version_date = date.today()
		else:
			try:
				version_date = datetime.strptime(version_date_str, '%Y-%m-%d').date()
			except:
				version_date = date.today()

		# Get or create statute record
		statute = db.query(Statute).filter(Statute.instrument_key == instrument_key).first()

		if not statute:
			statute = Statute(
				instrument_key=instrument_key,
				title=statute_info["title"],
				short_title=statute_info.get("short_title"),
				jurisdiction=statute_info["jurisdiction"],
				statute_type=statute_info["statute_type"],
				source=statute_info["source"],
				license=statute_info.get("license"),
				source_url=statute_info.get("url"),
			)
			db.add(statute)
			db.flush()
			logger.info(f"Created statute record for {instrument_key}")

		# Check if this version already exists
		existing_version = db.query(StatuteVersion).filter(
			StatuteVersion.statute_id == statute.id, StatuteVersion.in_force_date == version_date
		).first()

		if existing_version:
			logger.info(f"Version of {instrument_key} for {version_date} already exists, skipping")
			return statute

		# Compress text if larger than 1MB
		full_text = statute_text if len(statute_text) < 1024 * 1024 else None
		text_compressed = gzip.compress(statute_text.encode()) if len(statute_text) >= 1024 * 1024 else None

		# Create statute version
		statute_version = StatuteVersion(
			statute_id=statute.id,
			version_number='1.0',
			in_force_date=version_date,
			full_text=full_text,
			text_compressed=text_compressed,
			fetched_at=datetime.now(),
		)
		db.add(statute_version)
		db.flush()

		# Parse and store sections from XML
		sections = parse_statute_sections_from_xml(xml_root)
		if not sections:
			sections = parse_statute_sections(statute_text)

		for section_data in sections[:100]:  # Limit to first 100 sections to avoid DB bloat
			section = StatuteSection(
				statute_version_id=statute_version.id,
				section_number=section_data["section_number"],
				subsection=section_data["subsection"],
				paragraph=section_data["paragraph"],
				heading=section_data["heading"],
				text=section_data["text"],
				offset_start=section_data["offset_start"],
				offset_end=section_data["offset_end"],
			)
			db.add(section)

		db.commit()
		logger.info(f"Imported {min(len(sections), 100)} sections for {instrument_key} ({version_date})")
		return statute

	except Exception as e:
		logger.error(f"Error importing {instrument_key}: {e}")
		db.rollback()
		return None


def get_xml_url_for_statute(statute_url: str) -> str:
	"""Convert a statute HTML URL to its XML equivalent."""
	# Pattern: /eng/acts/i-2.5/ -> /eng/XML/I-2.5.xml
	# Pattern: /eng/regulations/SOR-2002-227/ -> /eng/XML/SOR-2002-227.xml
	import re
	match = re.search(r'/eng/(acts|regulations)/([^/]+)/?$', statute_url)
	if match:
		code = match.group(2)
		return f"https://laws-lois.justice.gc.ca/eng/XML/{code}.xml"
	return None


def analyze_statute_references(db: Session | None = None) -> dict[str, int]:
	"""
	Analyze existing statute references to determine citation frequency.
	Returns dict mapping instrument keys to citation counts.
	"""
	if db is None:
		db = SessionLocal()

	try:
		from backend.database import StatuteReference

		# Query references grouped by instrument_key
		result = db.query(
			StatuteReference.instrument_key,
			func.count(StatuteReference.id).label('count')
		).filter(
			StatuteReference.instrument_key.isnot(None)
		).group_by(
			StatuteReference.instrument_key
		).order_by(
			func.count(StatuteReference.id).desc()
		).all()

		citation_counts = {row[0]: row[1] for row in result}
		logger.info(f"\nStatute reference citation frequency (top 20):")
		for key, count in list(citation_counts.items())[:20]:
			logger.info(f"  {key}: {count} references")

		return citation_counts
	except Exception as e:
		logger.error(f"Error analyzing statute references: {e}")
		return {}
	finally:
		db.close()


def import_statutes_bulk(
	statute_dict: dict | None = None,
	db: Session | None = None,
	with_history: bool = True,
	phase_filter: int | None = None,
) -> dict[str, int]:
	"""
	Bulk import statutes from Justice Laws XML with historical versions.

	Args:
		statute_dict: Dict of statutes to import (default: all CBSA/immigration statutes)
		db: Database session (creates new one if None)
		with_history: Fetch and import historical versions (default True)
		phase_filter: Only import statutes from this phase (default: all)

	Returns:
		Dict mapping instrument keys to counts of versions imported
	"""
	if db is None:
		db = SessionLocal()

	if statute_dict is None:
		statute_dict = CBSA_IMMIGRATION_STATUTES

	# Filter by phase if specified
	statutes_to_import = {}
	for key, info in statute_dict.items():
		if phase_filter is None or info.get("phase") == phase_filter:
			statutes_to_import[key] = info

	logger.info(f"\nStarting bulk statute import for {len(statutes_to_import)} instruments...")
	import_counts = {}

	with JusticeLawsXMLClient() as client:
		for instrument_key in sorted(statutes_to_import.keys()):
			statute_info = statutes_to_import[instrument_key]
			statute_url = statute_info.get("url")

			if not statute_url:
				logger.warning(f"No URL for {instrument_key}, skipping")
				continue

			logger.info(f"\n{'='*60}")
			logger.info(f"Importing {instrument_key} ({statute_info.get('title')})")
			logger.info("=" * 60)

			try:
				# Get XML URL for current version
				xml_url = get_xml_url_for_statute(statute_url)
				if not xml_url:
					logger.warning(f"Could not determine XML URL for {instrument_key}")
					continue

				version_count = 0

				# Fetch and import current statute XML
				xml_root = client.fetch_statute_xml(instrument_key, xml_url)
				if xml_root is None:
					logger.warning(f"Could not fetch XML for {instrument_key}")
					continue

				metadata = client.extract_metadata_from_xml(xml_root)
				logger.info(f"Fetched current version with metadata: {metadata}")
				if import_statute_from_xml(db, instrument_key, statute_info, xml_root, metadata, client):
					version_count += 1

				# Fetch and import historical versions
				if with_history:
					logger.info(f"Fetching historical versions for {instrument_key}...")
					historical_versions = client.fetch_pitindex_versions(instrument_key, statute_url)

					for version_info in historical_versions:
						try:
							# Only import if different from current version
							if version_info['in_force_date'] == metadata.get('pit_date'):
								logger.info(f"  Skipping current version (already imported)")
								continue

							version_xml = client.fetch_statute_xml(
								f"{instrument_key}@{version_info['in_force_date']}",
								version_info['url']
							)
							if version_xml:
								logger.info(f"  Importing version {version_info['in_force_date']}...")
								version_metadata = client.extract_metadata_from_xml(version_xml)
								if import_statute_from_xml(db, instrument_key, statute_info, version_xml, version_metadata, client):
									version_count += 1
						except Exception as e:
							logger.warning(f"  Error importing version {version_info['in_force_date']}: {e}")

				import_counts[instrument_key] = version_count
				logger.info(f"✓ {instrument_key}: imported {version_count} versions")
			except Exception as e:
				logger.error(f"Error importing {instrument_key}: {e}")
				import_counts[instrument_key] = 0

	db.close()

	# Summary report
	logger.info(f"\n{'='*60}")
	logger.info("Import Summary")
	logger.info("=" * 60)
	total_versions = 0
	for key, count in sorted(import_counts.items()):
		logger.info(f"{key:15} {count:5} versions")
		total_versions += count
	logger.info(f"{'TOTAL':15} {total_versions:5} versions imported")

	return import_counts


def import_phase1_statutes(instruments: list[str] | None = None, db: Session | None = None, with_history: bool = True) -> None:
	"""
	Import Phase 1 statutes from Justice Laws XML with historical versions.

	Legacy function for backward compatibility. Use import_statutes_bulk instead.

	Args:
		instruments: List of instrument keys to import (default: all Phase 1)
		db: Database session (creates new one if None)
		with_history: Fetch and import historical versions (default True)
	"""
	if db is None:
		db = SessionLocal()

	if instruments is None:
		instruments = list(PHASE1_STATUTES.keys())

	logger.info(f"Starting Phase 1 statute import for {len(instruments)} instruments...")

	with JusticeLawsXMLClient() as client:
		for instrument_key in instruments:
			if instrument_key not in PHASE1_STATUTES:
				logger.warning(f"Unknown instrument: {instrument_key}")
				continue

			statute_info = PHASE1_STATUTES[instrument_key]
			statute_url = statute_info.get("url")

			if not statute_url:
				logger.warning(f"No URL for {instrument_key}, skipping")
				continue

			logger.info(f"\n{'='*60}")
			logger.info(f"Importing {instrument_key}")
			logger.info("=" * 60)

			# Get XML URL for current version
			xml_url = get_xml_url_for_statute(statute_url)
			if not xml_url:
				logger.warning(f"Could not determine XML URL for {instrument_key}")
				continue

			# Fetch and import current statute XML
			xml_root = client.fetch_statute_xml(instrument_key, xml_url)
			if xml_root is None:
				logger.warning(f"Could not fetch XML for {instrument_key}")
				continue

			metadata = client.extract_metadata_from_xml(xml_root)
			logger.info(f"Fetched current version with metadata: {metadata}")
			import_statute_from_xml(db, instrument_key, statute_info, xml_root, metadata, client)

			# Fetch and import historical versions
			if with_history:
				logger.info(f"Fetching historical versions for {instrument_key}...")
				historical_versions = client.fetch_pitindex_versions(instrument_key, statute_url)

				for version_info in historical_versions:
					try:
						# Only import if different from current version
						if version_info['in_force_date'] == metadata.get('pit_date'):
							logger.info(f"  Skipping current version (already imported)")
							continue

						version_xml = client.fetch_statute_xml(
							f"{instrument_key}@{version_info['in_force_date']}",
							version_info['url']
						)
						if version_xml:
							logger.info(f"  Importing version {version_info['in_force_date']}...")
							version_metadata = client.extract_metadata_from_xml(version_xml)
							import_statute_from_xml(db, instrument_key, statute_info, version_xml, version_metadata, client)
					except Exception as e:
						logger.warning(f"  Error importing version {version_info['in_force_date']}: {e}")

	logger.info("\nPhase 1 import complete")
	db.close()


if __name__ == "__main__":
	import sys
	from pathlib import Path

	usage = """
	Statute Importer - Import Canadian federal laws with historical versions

	Usage:
		python import_statutes.py [command] [options]

	Commands:
		analyze              Analyze existing statute references by citation count
		phase1               Import Phase 1 statutes only (7 laws)
		phase2               Import Phase 2 statutes only (14 laws)
		all                  Import all CBSA/immigration statutes (phases 1+2)
		[statute_codes...]   Import specific statutes (e.g., IRPA IRPR CA)

	Examples:
		python import_statutes.py analyze
		python import_statutes.py phase1
		python import_statutes.py all
		python import_statutes.py IRPA IRPR CA
	"""

	if len(sys.argv) < 2:
		print(usage)
		sys.exit(1)

	command = sys.argv[1]

	if command == "analyze":
		analyze_statute_references()
	elif command == "phase1":
		import_statutes_bulk(phase_filter=1, with_history=True)
	elif command == "phase2":
		import_statutes_bulk(phase_filter=2, with_history=True)
	elif command == "all":
		import_statutes_bulk(with_history=True)
	elif command in ("-h", "--help"):
		print(usage)
	else:
		# Assume it's a list of statute codes
		codes = [command] + sys.argv[2:]
		filtered = {k: v for k, v in CBSA_IMMIGRATION_STATUTES.items() if k in codes}
		if filtered:
			import_statutes_bulk(statute_dict=filtered, with_history=True)
		else:
			logger.error(f"Unknown command or statute codes: {codes}")
			print(usage)
			sys.exit(1)
