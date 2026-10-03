#!/usr/bin/env python3
"""
Importer for Canadian federal statutes from Justice Laws XML API.

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

import json
import logging
import re
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlencode
from xml.etree import ElementTree as ET

import httpx
from sqlalchemy.orm import Session

from backend.database import SessionLocal, Statute, StatuteVersion, StatuteSection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Phase 1 statutes: federal laws relevant to CBSA litigation
PHASE1_STATUTES = {
	"IRPA": {
		"title": "Immigration and Refugee Protection Act",
		"short_title": "IRPA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"description": "Core legislation governing immigration, refugees, and citizenship",
	},
	"IRPR": {
		"title": "Immigration and Refugee Protection Regulations",
		"short_title": "IRPR",
		"jurisdiction": "Federal",
		"statute_type": "Regulation",
		"source": "justice_laws_xml",
		"license": "OGL",
		"description": "Regulations under IRPA",
	},
	"CA": {
		"title": "Citizenship Act",
		"short_title": "CA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"description": "Federal citizenship law",
	},
	"CustA": {
		"title": "Customs Act",
		"short_title": "Customs Act",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"description": "CBSA authority for border control",
	},
	"FCA": {
		"title": "Federal Courts Act",
		"short_title": "FCA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"description": "Federal court jurisdiction and procedure",
	},
	"FCR": {
		"title": "Federal Courts Rules",
		"short_title": "FCR",
		"jurisdiction": "Federal",
		"statute_type": "Rules",
		"source": "justice_laws_xml",
		"license": "OGL",
		"description": "Procedural rules for Federal Court",
	},
	"Charter": {
		"title": "Canadian Charter of Rights and Freedoms",
		"short_title": "Charter",
		"jurisdiction": "Federal",
		"statute_type": "Constitutional",
		"source": "justice_laws_xml",
		"license": "OGL",
		"description": "Part of Constitution Act, 1982",
	},
}

# Mapping of instrument keys to justice.gc.ca API identifiers
# These are the official keys used by the Justice Laws XML service
JUSTICE_LAWS_KEYS = {
	"IRPA": "SOR-2002-227",  # SOR = Statutory Order and Regulation
	"IRPR": "SOR-2002-228",
	"CA": "SOR-1985-104",
	"CustA": "SOR-1985-127",
	"FCA": "SOR-2002-15",
	"FCR": "SOR-1998-106",
	"Charter": "Constitution Act, 1982",
}


class JusticeLabsXMLClient:
	"""Client for CanLII's Justice Laws XML API."""

	BASE_URL = "https://canlii.org/en/api"
	TIMEOUT = 30

	def __init__(self):
		self.client = httpx.Client(timeout=self.TIMEOUT, follow_redirects=True)

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.client.close()

	def get_statute_versions(self, instrument_key: str) -> dict | None:
		"""
		Fetch all versions of a statute from CanLII's API.
		Returns metadata about available versions and their in-force dates.
		"""
		# This would query CanLII's endpoint for statute versions
		# For now, a placeholder showing the API structure
		try:
			# Note: This is a simplified approach. Real implementation would use
			# the official justice.gc.ca API or CanLII's consolidated versions.
			logger.info(f"Fetching versions for {instrument_key} from CanLII API...")

			# Placeholder: would call actual API endpoint
			# response = self.client.get(f"{self.BASE_URL}/statute/{instrument_key}/versions")
			# return response.json() if response.status_code == 200 else None

			return None
		except Exception as e:
			logger.error(f"Error fetching {instrument_key}: {e}")
			return None

	def get_statute_text(self, instrument_key: str, version_date: date | None = None) -> str | None:
		"""
		Fetch the full text of a statute at a specific date.
		If version_date is None, fetches the current version.
		"""
		try:
			logger.info(f"Fetching text for {instrument_key} as of {version_date or 'current'}...")
			# Would fetch from justice.gc.ca or CanLII
			# response = self.client.get(f"{self.BASE_URL}/statute/{instrument_key}/text")
			# return response.text if response.status_code == 200 else None
			return None
		except Exception as e:
			logger.error(f"Error fetching statute text for {instrument_key}: {e}")
			return None


def parse_statute_sections(statute_text: str) -> list[dict]:
	"""
	Parse statute text into sections with hierarchical structure.
	Returns list of section dicts with number, heading, text, and offsets.
	"""
	sections = []

	# Simple regex-based parser for common statute structure
	# This is a basic implementation; production would use more robust parsing
	lines = statute_text.split("\n")
	current_section = None
	current_offset = 0

	for line in lines:
		# Match section headers like "1.", "2.", "Section 1", "Schedule A", etc.
		section_match = re.match(r"^([0-9]+(?:\.[0-9]+)?|Schedule\s+[A-Z])\s*(?:\(([a-z])\))?\s*(.*)$", line.strip())

		if section_match:
			# Save previous section
			if current_section:
				sections.append(current_section)

			# Start new section
			section_num = section_match.group(1)
			subsection = section_match.group(2)
			heading = section_match.group(3)

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
			current_section["text"] += line + "\n"

		current_offset += len(line) + 1

	# Save last section
	if current_section:
		current_section["offset_end"] = current_offset
		sections.append(current_section)

	return sections


def import_statute_from_text(
	db: Session,
	instrument_key: str,
	statute_info: dict,
	statute_text: str,
	version_date: date,
	version_number: str = "1.0",
) -> Statute | None:
	"""
	Import a single statute version into the database.
	"""
	try:
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
				source_url=statute_info.get("source_url"),
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

		# Create statute version
		statute_version = StatuteVersion(
			statute_id=statute.id,
			version_number=version_number,
			in_force_date=version_date,
			full_text=statute_text,
			fetched_at=datetime.now(),
		)
		db.add(statute_version)
		db.flush()

		# Parse and store sections
		sections = parse_statute_sections(statute_text)
		for section_data in sections:
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
		logger.info(f"Imported {len(sections)} sections for {instrument_key} v{version_number} ({version_date})")
		return statute

	except Exception as e:
		logger.error(f"Error importing {instrument_key}: {e}")
		db.rollback()
		return None


def import_phase1_statutes(db: Session | None = None) -> None:
	"""
	Import Phase 1 statutes from Justice Laws XML.
	This is a placeholder that shows the structure; actual API calls would go here.
	"""
	if db is None:
		db = SessionLocal()

	logger.info("Starting Phase 1 statute import...")

	# TODO: Implement actual API calls to justice.gc.ca or CanLII
	# For now, this is a structural placeholder

	logger.info("Phase 1 import complete. TODO: Implement API integration with justice.gc.ca or CanLII")


if __name__ == "__main__":
	import_phase1_statutes()
