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
		"url": "https://laws-lois.justice.gc.ca/eng/acts/i-2.5/",
	},
	"IRPR": {
		"title": "Immigration and Refugee Protection Regulations",
		"short_title": "IRPR",
		"jurisdiction": "Federal",
		"statute_type": "Regulation",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/",
	},
	"CA": {
		"title": "Citizenship Act",
		"short_title": "CA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/c-29/",
	},
	"CustA": {
		"title": "Customs Act",
		"short_title": "Customs Act",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/r-8.88/",
	},
	"FCA": {
		"title": "Federal Courts Act",
		"short_title": "FCA",
		"jurisdiction": "Federal",
		"statute_type": "Act",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/acts/f-7/",
	},
	"FCR": {
		"title": "Federal Courts Rules",
		"short_title": "FCR",
		"jurisdiction": "Federal",
		"statute_type": "Rules",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-98-106/",
	},
	"Charter": {
		"title": "Canadian Charter of Rights and Freedoms",
		"short_title": "Charter",
		"jurisdiction": "Federal",
		"statute_type": "Constitutional",
		"source": "justice_laws_xml",
		"license": "OGL",
		"url": "https://laws-lois.justice.gc.ca/eng/const/page-12.html",
	},
}


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

	def fetch_statute_html(self, instrument_key: str, statute_url: str) -> str | None:
		"""Fetch statute HTML from justice.gc.ca."""
		try:
			logger.info(f"Fetching {instrument_key} from {statute_url}...")
			response = self.client.get(statute_url)
			if response.status_code == 200:
				return response.text
			else:
				logger.warning(f"Status {response.status_code} for {instrument_key}")
				return None
		except Exception as e:
			logger.error(f"Error fetching {instrument_key}: {e}")
			return None

	def extract_statute_text_from_html(self, html: str) -> str | None:
		"""
		Extract statute text from justice.gc.ca HTML.
		Simple text extraction from the main content div.
		"""
		try:
			# Extract text from <main> tag or specific content divs
			# This is a simplified approach; production would parse HTML properly
			import re

			# Remove scripts and styles
			html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
			html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)

			# Extract main content
			match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
			if not match:
				match = re.search(r'<div[^>]*id=["\']content["\'][^>]*>(.*?)</div>', html, re.DOTALL)

			if match:
				content = match.group(1)
				# Remove HTML tags
				text = re.sub(r'<[^>]+>', '\n', content)
				# Clean up whitespace
				text = re.sub(r'\n\s*\n', '\n', text)
				return text.strip()

			return None
		except Exception as e:
			logger.error(f"Error extracting text: {e}")
			return None


def parse_statute_sections(statute_text: str) -> list[dict]:
	"""
	Parse statute text into sections with hierarchical structure.
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

	return sections if sections else [{"section_number": "1", "heading": "Full Text", "text": statute_text}]


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
		if not statute_text or len(statute_text) < 100:
			logger.warning(f"Statute text too short for {instrument_key}, skipping")
			return None

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

		# Compress text if larger than 1MB
		full_text = statute_text if len(statute_text) < 1024 * 1024 else None
		text_compressed = gzip.compress(statute_text.encode()) if len(statute_text) >= 1024 * 1024 else None

		# Create statute version
		statute_version = StatuteVersion(
			statute_id=statute.id,
			version_number=version_number,
			in_force_date=version_date,
			full_text=full_text,
			text_compressed=text_compressed,
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


def import_phase1_statutes(instruments: list[str] | None = None, db: Session | None = None) -> None:
	"""
	Import Phase 1 statutes from Justice Laws XML.

	Args:
		instruments: List of instrument keys to import (default: all Phase 1)
		db: Database session (creates new one if None)
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

			# Fetch statute HTML
			html = client.fetch_statute_html(instrument_key, statute_url)
			if not html:
				logger.warning(f"Could not fetch {instrument_key}")
				continue

			# Extract text
			statute_text = client.extract_statute_text_from_html(html)
			if not statute_text:
				logger.warning(f"Could not extract text for {instrument_key}")
				continue

			logger.info(f"Extracted {len(statute_text)} characters for {instrument_key}")

			# Import to database (using current date as version date for this simple test)
			import_statute_from_text(
				db, instrument_key, statute_info, statute_text, date.today(), version_number="current"
			)

	logger.info("Phase 1 import complete")
	db.close()


if __name__ == "__main__":
	import sys

	instruments = sys.argv[1:] if len(sys.argv) > 1 else ["IRPA", "IRPR"]
	import_phase1_statutes(instruments)
