"""Central configuration and validation for uploaded document resource limits."""

from __future__ import annotations

from io import BytesIO
import os
from zipfile import BadZipFile, ZipFile

from pypdf import PdfReader


def _positive_int(name: str, default: int) -> int:
	raw = os.getenv(name)
	if raw is None:
		return default
	try:
		value = int(raw)
	except ValueError as exc:
		raise ValueError(f"{name} must be a positive integer") from exc
	if value <= 0:
		raise ValueError(f"{name} must be a positive integer")
	return value


# Defaults retain the existing 10 MiB upload contract while limiting expanded
# archive and parser work independently of the compressed upload size.
MAX_UPLOAD_BYTES = _positive_int("LITINTEL_MAX_UPLOAD_BYTES", 10 * 1024 * 1024)
MAX_DOCX_UNCOMPRESSED_BYTES = _positive_int(
	"LITINTEL_MAX_DOCX_UNCOMPRESSED_BYTES", 100 * 1024 * 1024
)
MAX_DOCX_ARCHIVE_ENTRIES = _positive_int("LITINTEL_MAX_DOCX_ARCHIVE_ENTRIES", 2_000)
MAX_PDF_PAGES = _positive_int("LITINTEL_MAX_PDF_PAGES", 500)
MAX_EXTRACTED_TEXT_CHARS = _positive_int(
	"LITINTEL_MAX_EXTRACTED_TEXT_CHARS", 5_000_000
)
MAX_PASTED_TEXT_CHARS = _positive_int("LITINTEL_MAX_PASTED_TEXT_CHARS", 1_000_000)


class ResourceLimitError(ValueError):
	"""An upload or parsed document exceeded a configured resource limit."""


def validate_extracted_text_length(char_count: int) -> None:
	if char_count > MAX_EXTRACTED_TEXT_CHARS:
		raise ResourceLimitError(
			"The extracted document text exceeds the "
			f"{MAX_EXTRACTED_TEXT_CHARS} character limit."
		)


def validate_pasted_text_length(char_count: int) -> None:
	if char_count > MAX_PASTED_TEXT_CHARS:
		raise ResourceLimitError(
			f"The pasted text exceeds the {MAX_PASTED_TEXT_CHARS} character limit."
		)


def upload_limit_message() -> str:
	limit_mb = MAX_UPLOAD_BYTES / (1024 * 1024)
	if limit_mb.is_integer():
		return f"The uploaded file exceeds the {int(limit_mb)} MB limit"
	return f"The uploaded file exceeds the {MAX_UPLOAD_BYTES} byte limit"


def validate_docx_archive(content: bytes) -> None:
	"""Reject DOCX archives with too many entries or excessive expanded size."""
	try:
		with ZipFile(BytesIO(content)) as archive:
			entries = archive.infolist()
	except BadZipFile as exc:
		raise ValueError("The DOCX archive is invalid.") from exc

	if len(entries) > MAX_DOCX_ARCHIVE_ENTRIES:
		raise ResourceLimitError(
			f"The DOCX archive exceeds the {MAX_DOCX_ARCHIVE_ENTRIES} entry limit."
		)
	uncompressed_bytes = sum(entry.file_size for entry in entries)
	if uncompressed_bytes > MAX_DOCX_UNCOMPRESSED_BYTES:
		raise ResourceLimitError(
			"The DOCX uncompressed content exceeds the "
			f"{MAX_DOCX_UNCOMPRESSED_BYTES} byte limit."
		)


def extract_pdf_pages(content: bytes) -> list[str]:
	"""Extract bounded PDF text, checking page and aggregate character limits."""
	reader = PdfReader(BytesIO(content))
	if len(reader.pages) > MAX_PDF_PAGES:
		raise ResourceLimitError(f"The PDF exceeds the {MAX_PDF_PAGES} page limit.")

	pages: list[str] = []
	total_chars = 0
	for page in reader.pages:
		text = page.extract_text() or ""
		total_chars += len(text)
		if len(pages):
			total_chars += 2
		validate_extracted_text_length(total_chars)
		pages.append(text)
	return pages
