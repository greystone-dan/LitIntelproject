"""Deterministic source-HTML structure and plain-text mapping helpers."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from typing import Any

from bs4 import BeautifulSoup, NavigableString, Tag

BLOCK_TAGS = {
    "address",
    "article",
    "aside",
    "blockquote",
    "caption",
    "dd",
    "div",
    "dt",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "header",
    "li",
    "main",
    "p",
    "pre",
    "section",
    "td",
    "th",
    "tr",
}
REMOVED_TAGS = {"audio", "canvas", "embed", "iframe", "object", "script", "style", "video"}
_WHITESPACE_RE = re.compile(r"\s+")


@dataclass(frozen=True)
class DocumentBlock:
    """A structural source block mapped into canonical plain-text offsets."""

    block_index: int
    kind: str
    text: str
    plain_text_start: int
    plain_text_end: int
    html_tag: str
    html_path: str
    heading_level: int | None = None
    canonical_text_start: int | None = None
    canonical_text_end: int | None = None
    mapping_confidence: float = 0.0

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class StructuredDocument:
    """Sanitized source HTML, canonical text, and structural text blocks."""

    sanitized_html: str
    plain_text: str
    blocks: tuple[DocumentBlock, ...]
    parser_version: str = "html-structure-v1"
    canonical_text: str | None = None
    mapping_confidence: float | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
            "parser_version": self.parser_version,
            "plain_text": self.plain_text,
            "canonical_text": self.canonical_text,
            "mapping_confidence": self.mapping_confidence,
            "blocks": [block.as_dict() for block in self.blocks],
        }


@dataclass(frozen=True)
class LayerSpan:
    """A citation or evidence span expressed in one chunk layer."""

    layer: str
    chunk_id: int | None
    absolute_start: int
    absolute_end: int
    local_start: int
    local_end: int


def map_span_to_chunk_layers(
    case_text: str,
    span_start: int,
    span_end: int,
    chunks: list[Any] | tuple[Any, ...],
) -> dict[str, LayerSpan]:
    """Map a canonical case span into containing full, section, and paragraph chunks."""
    if span_start < 0 or span_end <= span_start or span_end > len(case_text):
        raise ValueError("span must be a positive range within case_text")
    layer_order = {"full_case": 0, "section": 1, "paragraph": 2, "legacy": 3}
    located: dict[str, LayerSpan] = {}
    search_cursors: dict[str, int] = {}
    for chunk in sorted(chunks, key=lambda item: (layer_order.get(getattr(item, "chunk_set", ""), 9), getattr(item, "chunk_index", 0))):
        layer = getattr(chunk, "chunk_set", None)
        chunk_text = getattr(chunk, "text", "") or ""
        if not layer or not chunk_text:
            continue
        cursor = search_cursors.get(layer, 0)
        absolute_start = case_text.find(chunk_text, cursor)
        if absolute_start < 0:
            absolute_start = case_text.find(chunk_text)
        if absolute_start < 0:
            continue
        absolute_end = absolute_start + len(chunk_text)
        search_cursors[layer] = absolute_end
        if layer in located or not (absolute_start <= span_start and span_end <= absolute_end):
            continue
        located[layer] = LayerSpan(
            layer=layer,
            chunk_id=getattr(chunk, "id", None),
            absolute_start=absolute_start,
            absolute_end=absolute_end,
            local_start=span_start - absolute_start,
            local_end=span_end - absolute_start,
        )
    return located


def _normalize_text(value: str) -> str:
    text = _WHITESPACE_RE.sub(" ", value or "").strip()
    return re.sub(r"\s+([,.;:!?%)\]])", r"\1", text)


def _html_path(node: Tag) -> str:
    parts: list[str] = []
    current: Tag | None = node
    while current is not None and current.name != "[document]":
        siblings = [item for item in current.parent.find_all(current.name, recursive=False)] if current.parent else []
        position = siblings.index(current) + 1 if current in siblings else 1
        parts.append(f"{current.name}[{position}]")
        parent = current.parent
        current = parent if isinstance(parent, Tag) else None
    return "/" + "/".join(reversed(parts))


def _sanitize(soup: BeautifulSoup) -> None:
    for node in soup.find_all(REMOVED_TAGS):
        node.decompose()
    for node in soup.find_all(True):
        for attribute in list(node.attrs):
            if attribute.lower().startswith("on") or attribute.lower() in {"srcdoc", "javascript"}:
                del node.attrs[attribute]


def _is_leaf_block(node: Tag) -> bool:
    return node.name in BLOCK_TAGS and not node.find(BLOCK_TAGS)


def _block_kind(node: Tag) -> str:
    if node.name.startswith("h") and len(node.name) == 2 and node.name[1].isdigit():
        return "heading"
    if node.name == "li":
        return "list_item"
    if node.name == "tr":
        return "table_row"
    if node.name == "blockquote":
        return "quote"
    if node.name == "pre":
        return "preformatted"
    return "paragraph"


def _scc_candidates(soup: BeautifulSoup) -> list[tuple[Tag, str, int | None]]:
    root = soup.select_one(".documentcontent") or soup.select_one("#document-content")
    if root is None:
        return []
    nodes = [node for node in root.find_all("div", recursive=False) if any(str(value).startswith("Section") for value in node.get("class", []))]
    start = next((index for index, node in enumerate(nodes) if node.find("p", class_=re.compile(r"^\d+$"))), None)
    if start is None:
        return []
    candidates: list[tuple[Tag, str, int | None]] = []
    for node in nodes[start:]:
        for paragraph in node.find_all("p"):
            text = _normalize_text(paragraph.get_text(" ", strip=True))
            if not text:
                continue
            paragraph_class = str((paragraph.get("class") or [""])[0])
            paragraph_match = re.match(r"^(\d+)\s+", text)
            kind = "heading" if re.match(r"^[IVXLC]+\.\s+", text) else "paragraph"
            paragraph_number = int(paragraph_match.group(1)) if paragraph_match else int(paragraph_class) if paragraph_class.isdigit() else None
            candidates.append((paragraph, kind, paragraph_number))
    return candidates


def structure_source_html(source_html: str | None, fallback_text: str | None = None, source_family: str | None = None) -> StructuredDocument:
    """Parse source HTML without mutating it and map structural blocks to text offsets."""
    original = source_html or ""
    soup = BeautifulSoup(original, "html.parser") if original.strip() else BeautifulSoup("", "html.parser")
    _sanitize(soup)
    scc_candidates = _scc_candidates(soup) if source_family == "scc" else []
    candidates = [node for node in soup.find_all(BLOCK_TAGS) if _is_leaf_block(node)] if not scc_candidates else [node for node, _kind, _paragraph_number in scc_candidates]
    if not candidates and fallback_text:
        text = _normalize_text(fallback_text)
        blocks = (
            DocumentBlock(0, "paragraph", text, 0, len(text), "text", "", None),
        ) if text else ()
        return StructuredDocument(sanitized_html="", plain_text=text, blocks=blocks)

    text_parts: list[str] = []
    blocks: list[DocumentBlock] = []
    cursor = 0
    for node in candidates:
        block_text = _normalize_text(node.get_text(" ", strip=True))
        if not block_text:
            continue
        if text_parts:
            text_parts.append("\n\n")
            cursor += 2
        start = cursor
        text_parts.append(block_text)
        cursor += len(block_text)
        scc_info = next(((kind, paragraph_number) for candidate, kind, paragraph_number in scc_candidates if candidate is node), None)
        heading_level = 1 if scc_info and scc_info[0] == "heading" else int(node.name[1]) if node.name.startswith("h") and node.name[1:].isdigit() else None
        blocks.append(
            DocumentBlock(
                block_index=len(blocks),
                kind=scc_info[0] if scc_info else _block_kind(node),
                text=block_text,
                plain_text_start=start,
                plain_text_end=cursor,
                html_tag=node.name,
                html_path=_html_path(node),
                heading_level=heading_level,
            )
        )
    plain_text = "".join(text_parts)
    return StructuredDocument(sanitized_html=soup.decode_contents(), plain_text=plain_text, blocks=tuple(blocks))


def map_to_canonical_text(document: StructuredDocument, canonical_text: str) -> StructuredDocument:
    """Map HTML block ranges onto canonical text without changing either text value."""
    if not canonical_text:
        return StructuredDocument(
            document.sanitized_html,
            document.plain_text,
            document.blocks,
            document.parser_version,
            canonical_text,
            0.0,
        )
    matcher = SequenceMatcher(None, document.plain_text, canonical_text, autojunk=True)
    opcodes = matcher.get_opcodes()
    block_matches: list[DocumentBlock] = []
    for block in document.blocks:
        mapped: list[tuple[int, int]] = []
        matched_length = 0
        for tag, source_start, source_end, target_start, target_end in opcodes:
            overlap_start = max(block.plain_text_start, source_start)
            overlap_end = min(block.plain_text_end, source_end)
            if overlap_start >= overlap_end or tag == "delete":
                continue
            source_length = max(1, source_end - source_start)
            target_length = target_end - target_start
            relative_start = overlap_start - source_start
            relative_end = overlap_end - source_start
            mapped_start = target_start + round(relative_start / source_length * target_length)
            mapped_end = target_start + round(relative_end / source_length * target_length)
            if mapped_end > mapped_start:
                mapped.append((mapped_start, mapped_end))
                if tag == "equal":
                    matched_length += overlap_end - overlap_start
        if mapped:
            canonical_start = min(start for start, _end in mapped)
            canonical_end = max(end for _start, end in mapped)
        else:
            canonical_start = canonical_end = None
        block_matches.append(
            DocumentBlock(
                **{
                    **block.as_dict(),
                    "canonical_text_start": canonical_start,
                    "canonical_text_end": canonical_end,
                    "mapping_confidence": round(matched_length / max(1, len(block.text)), 4),
                }
            )
        )
    matched_total = sum(end - start for tag, start, end, _target_start, _target_end in opcodes if tag == "equal")
    structural_length = sum(len(block.text) for block in document.blocks)
    return StructuredDocument(
        document.sanitized_html,
        document.plain_text,
        tuple(block_matches),
        document.parser_version,
        canonical_text,
        round(matched_total / max(1, structural_length), 4),
    )
