"""Word export of a case with the Markup margin notes as real Word comments.

Pure and offline: the decision text comes from the stored case, the comment text comes from what the
reader already shows (sent by the browser at click time), and the .docx is written directly as
OOXML with the standard library. No AI, no network, nothing stored.
"""

from __future__ import annotations

import io
import re
import zipfile
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from xml.sax.saxutils import escape

from backend.case_formatter import format_decision

MAX_COMMENTS = 3000
MAX_TEXT = 4000

_XML_BAD = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f￾￿]")
_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


@dataclass(frozen=True)
class Comment:
    block: int | None  # start offset of the decision block it belongs to; None = the case header
    label: str
    text: str
    quote: str | None = None  # words inside the block to anchor to; the whole block when absent
    author: str = "iLit Markup"


def _clean(value: object, limit: int) -> str:
    return _XML_BAD.sub("", str(value or ""))[:limit]


def _t(text: str) -> str:
    return f'<w:t xml:space="preserve">{escape(text)}</w:t>'


def _run(text: str, bold: bool = False, highlight: bool = False, size: int | None = None) -> str:
    props = ("<w:b/>" if bold else "") + ('<w:highlight w:val="yellow"/>' if highlight else "")
    if size:
        props += f'<w:sz w:val="{size}"/>'
    return f"<w:r>{f'<w:rPr>{props}</w:rPr>' if props else ''}{_t(text)}</w:r>"


def _anchor_span(text: str, quote: str | None) -> tuple[int, int]:
    """Character range a comment covers inside a block: the quote if found, else everything."""
    if quote:
        quote = quote.strip()
        at = text.find(quote)
        if at < 0:
            at = text.lower().find(quote.lower())
        if at >= 0:
            return at, at + len(quote)
    return 0, len(text)


def _paragraph_xml(text: str, comments: Sequence[tuple[int, Comment]], *, bold: bool, highlight: bool) -> str:
    """One Word paragraph; ``comments`` are (comment id, comment) pairs anchored inside ``text``."""
    events: list[tuple[int, int, int]] = []  # (position, order, comment id): 0 start, 1 end
    spans = {}
    for cid, comment in comments:
        start, end = _anchor_span(text, comment.quote)
        spans[cid] = (start, end)
        events.append((start, 0, cid))
        events.append((end, 1, cid))
    events.sort()
    out: list[str] = []
    pos = 0
    for at, kind, cid in events:
        if at > pos:
            out.append(_run(text[pos:at], bold, highlight))
            pos = at
        if kind == 0:
            out.append(f'<w:commentRangeStart w:id="{cid}"/>')
        else:
            out.append(f'<w:commentRangeEnd w:id="{cid}"/><w:r><w:commentReference w:id="{cid}"/></w:r>')
    if pos < len(text):
        out.append(_run(text[pos:], bold, highlight))
    style = '<w:pPr><w:spacing w:after="120"/></w:pPr>'
    return f"<w:p>{style}{''.join(out)}</w:p>"


def _comments_xml(comments: Sequence[Comment], when: str) -> str:
    parts = []
    for cid, comment in enumerate(comments):
        initials = "".join(word[0] for word in comment.author.split()[:2]).upper() or "iL"
        lines = ([comment.label] if comment.label else []) + [ln for ln in comment.text.split("\n")]
        body = "".join(
            f"<w:p>{_run(line, bold=(i == 0 and bool(comment.label)))}</w:p>" for i, line in enumerate(lines)
        ) or "<w:p/>"
        parts.append(
            f'<w:comment w:id="{cid}" w:author="{escape(comment.author, {chr(34): "&quot;"})}" '
            f'w:date="{when}" w:initials="{escape(initials)}">{body}</w:comment>'
        )
    return f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:comments xmlns:w="{_W}">{"".join(parts)}</w:comments>'


def build_markup_docx(
    *,
    title: str,
    subtitle: str,
    full_text: str,
    comments: Sequence[Comment],
    highlights: Sequence[int] = (),
    now: datetime | None = None,
) -> bytes:
    """The decision as a Word file with ``comments`` attached; ``highlights`` are block starts to mark yellow."""
    now = now or datetime.now(timezone.utc)
    when = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    comments = [
        Comment(c.block, _clean(c.label, 120), _clean(c.text, MAX_TEXT), _clean(c.quote, 400) or None, _clean(c.author, 40) or "iLit Markup")
        for c in comments[:MAX_COMMENTS]
    ]
    by_block: dict[int | None, list[tuple[int, Comment]]] = {}
    for cid, comment in enumerate(comments):
        by_block.setdefault(comment.block, []).append((cid, comment))
    marked = set(highlights)

    body: list[str] = [
        _paragraph_xml(_clean(title, 300), by_block.pop(None, []), bold=True, highlight=False),
        _paragraph_xml(_clean(subtitle, 300), [], bold=False, highlight=False),
        _paragraph_xml(
            f"Exported from the iLit Markup view on {now.strftime('%Y-%m-%d')}. Comments are the notes shown in the margin at the time of export.",
            [], bold=False, highlight=False,
        ),
    ]
    blocks = format_decision(full_text)
    known = {b["start"] for b in blocks}
    for block in blocks:
        text = _clean(full_text[block["start"]:block["end"]], 1_000_000)
        attached = by_block.pop(block["start"], [])
        body.append(
            _paragraph_xml(text, attached, bold=block["type"] == "heading", highlight=block["start"] in marked)
        )
    # Comments that point at a block that no longer exists still travel with the document.
    leftovers = [pair for block, pairs in by_block.items() if block not in known for pair in pairs]
    if leftovers:
        body.append(_paragraph_xml("Notes not attached to a paragraph", leftovers, bold=True, highlight=False))

    document = (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="{_W}" xmlns:r="{_R}">'
        f'<w:body>{"".join(body)}<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>'
        "</w:sectPr></w:body></w:document>"
    )
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/comments.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/>'
        "</Types>"
    )
    root_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        "</Relationships>"
    )
    doc_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments" Target="comments.xml"/>'
        "</Relationships>"
    )
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("_rels/.rels", root_rels)
        archive.writestr("word/document.xml", document)
        archive.writestr("word/_rels/document.xml.rels", doc_rels)
        archive.writestr("word/comments.xml", _comments_xml(comments, when))
    return buffer.getvalue()
