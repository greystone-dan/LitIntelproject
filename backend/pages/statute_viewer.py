"""Simple navigable statute viewer page."""

from fastapi import APIRouter, Query, HTTPException
from sqlalchemy.orm import Session

from backend.database import SessionLocal, Statute, StatuteVersion, StatuteSection
import gzip

router = APIRouter(prefix="/api/statutes", tags=["statutes"])


def get_statute_text(statute_version: StatuteVersion) -> str:
	"""Decompress statute text if needed."""
	if statute_version.full_text:
		return statute_version.full_text
	elif statute_version.text_compressed:
		return gzip.decompress(statute_version.text_compressed).decode()
	return ""


@router.get("/")
def list_statutes(db: Session = None):
	"""List all statutes in the library."""
	if db is None:
		db = SessionLocal()

	statutes = db.query(Statute).order_by(Statute.instrument_key).all()

	result = []
	for statute in statutes:
		# Get latest version
		latest_version = (
			db.query(StatuteVersion)
			.filter(StatuteVersion.statute_id == statute.id)
			.order_by(StatuteVersion.in_force_date.desc())
			.first()
		)

		result.append({
			"key": statute.instrument_key,
			"title": statute.title,
			"short_title": statute.short_title,
			"statute_type": statute.statute_type,
			"jurisdiction": statute.jurisdiction,
			"license": statute.license,
			"source": statute.source,
			"latest_version": latest_version.in_force_date.isoformat() if latest_version else None,
		})

	return {"statutes": result}


@router.get("/{statute_key}")
def get_statute_view(statute_key: str, db: Session = None):
	"""Get statute with all its versions and sections."""
	if db is None:
		db = SessionLocal()

	statute = db.query(Statute).filter(Statute.instrument_key == statute_key).first()
	if not statute:
		raise HTTPException(status_code=404, detail=f"Statute {statute_key} not found")

	versions = (
		db.query(StatuteVersion)
		.filter(StatuteVersion.statute_id == statute.id)
		.order_by(StatuteVersion.in_force_date.desc())
		.all()
	)

	return {
		"statute": {
			"key": statute.instrument_key,
			"title": statute.title,
			"short_title": statute.short_title,
			"statute_type": statute.statute_type,
			"jurisdiction": statute.jurisdiction,
			"license": statute.license,
			"source": statute.source,
			"source_url": statute.source_url,
		},
		"versions": [
			{
				"id": v.id,
				"version_number": v.version_number,
				"in_force_date": v.in_force_date.isoformat(),
				"end_date": v.end_date.isoformat() if v.end_date else None,
				"section_count": db.query(StatuteSection).filter(StatuteSection.statute_version_id == v.id).count(),
			}
			for v in versions
		],
	}


@router.get("/{statute_key}/versions/{version_id}/sections")
def get_statute_sections(statute_key: str, version_id: int, db: Session = None):
	"""Get all sections of a statute version."""
	if db is None:
		db = SessionLocal()

	statute = db.query(Statute).filter(Statute.instrument_key == statute_key).first()
	if not statute:
		raise HTTPException(status_code=404, detail=f"Statute {statute_key} not found")

	version = db.query(StatuteVersion).filter(StatuteVersion.id == version_id).first()
	if not version:
		raise HTTPException(status_code=404, detail=f"Version {version_id} not found")

	sections = (
		db.query(StatuteSection)
		.filter(StatuteSection.statute_version_id == version_id)
		.order_by(StatuteSection.section_number)
		.all()
	)

	return {
		"statute_key": statute_key,
		"version_id": version_id,
		"in_force_date": version.in_force_date.isoformat(),
		"sections": [
			{
				"id": s.id,
				"section_number": s.section_number,
				"subsection": s.subsection,
				"paragraph": s.paragraph,
				"heading": s.heading,
				"text": s.text[:500] + "..." if s.text and len(s.text) > 500 else s.text,
			}
			for s in sections
		],
	}


@router.get("/{statute_key}/versions/{version_id}/sections/{section_id}")
def get_statute_section(statute_key: str, version_id: int, section_id: int, db: Session = None):
	"""Get a single section of a statute version."""
	if db is None:
		db = SessionLocal()

	section = db.query(StatuteSection).filter(StatuteSection.id == section_id).first()
	if not section:
		raise HTTPException(status_code=404, detail=f"Section {section_id} not found")

	return {
		"statute_key": statute_key,
		"section": {
			"id": section.id,
			"section_number": section.section_number,
			"subsection": section.subsection,
			"paragraph": section.paragraph,
			"heading": section.heading,
			"text": section.text,
			"offset_start": section.offset_start,
			"offset_end": section.offset_end,
		},
	}


@router.get("/{statute_key}/search")
def search_statute_sections(statute_key: str, query: str = Query(..., min_length=2), db: Session = None):
	"""Search statute sections by text."""
	if db is None:
		db = SessionLocal()

	statute = db.query(Statute).filter(Statute.instrument_key == statute_key).first()
	if not statute:
		raise HTTPException(status_code=404, detail=f"Statute {statute_key} not found")

	# Get latest version
	latest_version = (
		db.query(StatuteVersion)
		.filter(StatuteVersion.statute_id == statute.id)
		.order_by(StatuteVersion.in_force_date.desc())
		.first()
	)

	if not latest_version:
		raise HTTPException(status_code=404, detail="No versions found")

	# Simple full-text search
	sections = (
		db.query(StatuteSection)
		.filter(
			StatuteSection.statute_version_id == latest_version.id,
			(StatuteSection.heading.ilike(f"%{query}%")) | (StatuteSection.text.ilike(f"%{query}%")),
		)
		.limit(20)
		.all()
	)

	return {
		"statute_key": statute_key,
		"query": query,
		"results": [
			{
				"section_number": s.section_number,
				"heading": s.heading,
				"text": s.text[:200] + "..." if s.text and len(s.text) > 200 else s.text,
			}
			for s in sections
		],
	}
