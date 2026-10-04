"""Shared primitives for read-only DOCX exports."""

from __future__ import annotations

from io import BytesIO
from typing import Any

from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.document import Document as DocumentType

from .deidentify import text_to_docx


def new_docx_document(title: str) -> DocumentType:
	"""Create a document using the established text-to-DOCX bootstrap."""
	return Document(BytesIO(text_to_docx(title)))


def add_docx_hyperlink(paragraph: Any, text: str, url: str) -> None:
	"""Add a clickable external hyperlink to a Word paragraph."""
	relationship_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
	hyperlink = OxmlElement("w:hyperlink")
	hyperlink.set(qn("r:id"), relationship_id)
	run = OxmlElement("w:r")
	properties = OxmlElement("w:rPr")
	color = OxmlElement("w:color")
	color.set(qn("w:val"), "164B73")
	properties.append(color)
	run.append(properties)
	text_element = OxmlElement("w:t")
	text_element.text = text
	run.append(text_element)
	hyperlink.append(run)
	paragraph._p.append(hyperlink)


def serialize_docx(document: DocumentType) -> bytes:
	"""Serialize a python-docx document to bytes."""
	buffer = BytesIO()
	document.save(buffer)
	return buffer.getvalue()
