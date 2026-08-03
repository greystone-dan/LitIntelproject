from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ItemData:
    fc_id: str
    title: str
    metadata: dict[str, Any]
    document_url: str
    pdf_url: str


@dataclass
class DocumentData:
    title: str
    full_text: str
    metadata: dict[str, Any]
