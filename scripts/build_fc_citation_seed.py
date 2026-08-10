"""Build a normalized Federal Court seed list for citation-system rebuild.

This script is intentionally extraction-only infrastructure. It normalizes a user-provided
case list into canonical FC item URLs and produces deterministic artifacts:
- accepted seeds
- rejects with reason codes
- summary stats

Supported input formats:
- .txt / .md: plain text with links
- .csv: scans common URL columns and any cell text
- .docx: extracts hyperlink targets and plain-text links
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import zipfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from fc_ingest.ingest_pipeline import _normalize_fc_item_url

URL_RE = re.compile(r"https?://[^\s<>()\[\]{}\"']+", re.IGNORECASE)
ITEM_ID_RE = re.compile(r"/item/(\d+)/", re.IGNORECASE)
CANLII_DOC_RE = re.compile(
    r"^/(?P<lang>en|fr)/(?P<jur>[a-z]{2})/(?P<court>[a-z0-9-]+)/doc/(?P<year>\d{4})/(?P<docid>[a-z0-9-]+)/(?P=docid)\.html$",
    re.IGNORECASE,
)
CSV_URL_COLUMNS = (
    "url",
    "link",
    "source_url",
    "raw_url",
    "item_url",
    "document_url",
    "pdf_url",
)


@dataclass(frozen=True)
class InputEntry:
    raw_value: str
    raw_url: str
    source_row: int


@dataclass(frozen=True)
class AcceptEntry:
    raw_value: str
    raw_url: str
    normalized_url: str
    source_system: str
    item_id: str
    source_row: int


@dataclass(frozen=True)
class RejectEntry:
    raw_value: str
    raw_url: str
    reason: str
    detail: str
    source_row: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Input file (.docx, .csv, .txt, .md)")
    parser.add_argument(
        "--accepted-csv",
        type=Path,
        default=Path("data/eval/fc_priority_seed_links.csv"),
    )
    parser.add_argument(
        "--rejects-csv",
        type=Path,
        default=Path("data/eval/fc_priority_seed_rejects.csv"),
    )
    parser.add_argument(
        "--summary-json",
        type=Path,
        default=Path("data/eval/fc_priority_seed_summary.json"),
    )
    parser.add_argument("--priority-group", default="fc_core")
    return parser.parse_args()


def _strip_trailing_url_noise(value: str) -> str:
    return value.rstrip(".,;:!?)\"]'")


def _extract_urls_from_text(text: str) -> list[str]:
    return [_strip_trailing_url_noise(match.group(0)) for match in URL_RE.finditer(text)]


def _iter_text_entries(path: Path) -> Iterable[InputEntry]:
    content = path.read_text(encoding="utf-8", errors="ignore")
    row = 1
    for url in _extract_urls_from_text(content):
        yield InputEntry(raw_value=url, raw_url=url, source_row=row)
        row += 1


def _iter_csv_entries(path: Path) -> Iterable[InputEntry]:
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as file_obj:
        reader = csv.DictReader(file_obj)
        row_num = 1
        for row in reader:
            row_num += 1
            if not row:
                continue

            value_candidates: list[str] = []
            lowered = {str(k).strip().lower(): v for k, v in row.items()}
            for column in CSV_URL_COLUMNS:
                value = lowered.get(column)
                if value and str(value).strip():
                    value_candidates.append(str(value).strip())

            if not value_candidates:
                for value in row.values():
                    if value and str(value).strip():
                        value_candidates.append(str(value).strip())

            seen: set[str] = set()
            for cell in value_candidates:
                for url in _extract_urls_from_text(cell):
                    if url in seen:
                        continue
                    seen.add(url)
                    yield InputEntry(raw_value=cell, raw_url=url, source_row=row_num)


def _iter_docx_entries(path: Path) -> Iterable[InputEntry]:
    with zipfile.ZipFile(path) as archive:
        rels_xml = archive.read("word/_rels/document.xml.rels")
        doc_xml = archive.read("word/document.xml")

    rels_root = ET.fromstring(rels_xml)
    relationship_map: dict[str, str] = {}
    for rel in rels_root.findall("{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"):
        rel_id = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rel_id and target:
            relationship_map[rel_id] = target

    doc_root = ET.fromstring(doc_xml)
    ns = {
        "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
        "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    }

    row = 1
    for node in doc_root.findall(".//w:hyperlink", ns):
        rel_id = node.attrib.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        if not rel_id:
            continue
        target = relationship_map.get(rel_id, "").strip()
        if not target:
            continue
        if target.startswith("/"):
            target = f"https://decisions.fct-cf.gc.ca{target}"
        target = _strip_trailing_url_noise(target)
        yield InputEntry(raw_value=target, raw_url=target, source_row=row)
        row += 1

    text_fragments: list[str] = []
    for tnode in doc_root.findall(".//w:t", ns):
        if tnode.text:
            text_fragments.append(tnode.text)
    plain_text = "\n".join(text_fragments)
    for url in _extract_urls_from_text(plain_text):
        yield InputEntry(raw_value=url, raw_url=url, source_row=row)
        row += 1


def _iter_input_entries(path: Path) -> Iterable[InputEntry]:
    suffix = path.suffix.lower()
    if suffix in {".txt", ".md"}:
        yield from _iter_text_entries(path)
        return
    if suffix == ".csv":
        yield from _iter_csv_entries(path)
        return
    if suffix == ".docx":
        yield from _iter_docx_entries(path)
        return
    raise SystemExit(f"Unsupported input format: {path.suffix}. Use .docx, .csv, .txt, or .md")


def _extract_item_id(normalized_url: str) -> str | None:
    match = ITEM_ID_RE.search(normalized_url)
    return match.group(1) if match else None


def _normalize_canlii_doc_url(url: str) -> tuple[str, str] | None:
    parsed = urlparse(url)
    host = (parsed.netloc or "").lower()
    if "canlii.org" not in host:
        return None

    normalized_path = re.sub(r"/{2,}", "/", parsed.path).rstrip("/")
    match = CANLII_DOC_RE.match(normalized_path)
    if not match:
        return None

    lang = match.group("lang").lower()
    jur = match.group("jur").lower()
    court = match.group("court").lower()
    year = match.group("year")
    docid = match.group("docid").lower()
    normalized_url = f"https://www.canlii.org/{lang}/{jur}/{court}/doc/{year}/{docid}/{docid}.html"
    return normalized_url, docid


def _normalize_entry(entry: InputEntry) -> tuple[AcceptEntry | None, RejectEntry | None]:
    parsed = urlparse(entry.raw_url)
    host = (parsed.netloc or "").lower()
    if not host:
        return None, RejectEntry(entry.raw_value, entry.raw_url, "invalid_url", "missing host", entry.source_row)

    if "decisions.fct-cf.gc.ca" in host:
        normalized = _normalize_fc_item_url(entry.raw_url)
        if not normalized:
            return None, RejectEntry(
                entry.raw_value,
                entry.raw_url,
                "not_item_url",
                "cannot derive /item/{id}/ URL",
                entry.source_row,
            )

        item_id = _extract_item_id(normalized)
        if not item_id:
            return None, RejectEntry(entry.raw_value, entry.raw_url, "missing_item_id", normalized, entry.source_row)

        return (
            AcceptEntry(
                raw_value=entry.raw_value,
                raw_url=entry.raw_url,
                normalized_url=normalized,
                source_system="fc_lexum",
                item_id=item_id,
                source_row=entry.source_row,
            ),
            None,
        )

    if "canlii.org" in host:
        normalized_canlii = _normalize_canlii_doc_url(entry.raw_url)
        if not normalized_canlii:
            return None, RejectEntry(
                entry.raw_value,
                entry.raw_url,
                "not_canlii_doc_url",
                "expected /<lang>/<jur>/<court>/doc/<year>/<docid>/<docid>.html",
                entry.source_row,
            )
        normalized_url, doc_id = normalized_canlii
        return (
            AcceptEntry(
                raw_value=entry.raw_value,
                raw_url=entry.raw_url,
                normalized_url=normalized_url,
                source_system="canlii",
                item_id=doc_id,
                source_row=entry.source_row,
            ),
            None,
        )

    return None, RejectEntry(entry.raw_value, entry.raw_url, "not_supported_domain", host, entry.source_row)


def build_seed(entries: Iterable[InputEntry]) -> tuple[list[AcceptEntry], list[RejectEntry], dict[str, int]]:
    accepts: list[AcceptEntry] = []
    rejects: list[RejectEntry] = []

    seen_keys: set[tuple[str, str]] = set()
    seen_urls: set[str] = set()
    reason_counts: Counter[str] = Counter()

    for entry in entries:
        accept, reject = _normalize_entry(entry)
        if reject is not None:
            rejects.append(reject)
            reason_counts[reject.reason] += 1
            continue
        assert accept is not None

        if accept.normalized_url in seen_urls:
            duplicate = RejectEntry(
                accept.raw_value,
                accept.raw_url,
                "duplicate_normalized_url",
                accept.normalized_url,
                accept.source_row,
            )
            rejects.append(duplicate)
            reason_counts[duplicate.reason] += 1
            continue

        key = (accept.source_system, accept.item_id)
        if key in seen_keys:
            duplicate = RejectEntry(
                accept.raw_value,
                accept.raw_url,
                "duplicate_item_id",
                f"{accept.source_system}:{accept.item_id}",
                accept.source_row,
            )
            rejects.append(duplicate)
            reason_counts[duplicate.reason] += 1
            continue

        seen_urls.add(accept.normalized_url)
        seen_keys.add(key)
        accepts.append(accept)

    stats = {
        "accepted": len(accepts),
        "rejected": len(rejects),
        "total": len(accepts) + len(rejects),
    }
    stats.update({f"rejected_{reason}": count for reason, count in sorted(reason_counts.items())})
    return accepts, rejects, stats


def _write_accepts(path: Path, source_file: Path, priority_group: str, rows: list[AcceptEntry]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(
            file_obj,
            fieldnames=[
                "source_file",
                "source_row",
                "priority_group",
                "source_system",
                "raw_value",
                "raw_url",
                "normalized_url",
                "item_id",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "source_file": str(source_file),
                    "source_row": row.source_row,
                    "priority_group": priority_group,
                    "source_system": row.source_system,
                    "raw_value": row.raw_value,
                    "raw_url": row.raw_url,
                    "normalized_url": row.normalized_url,
                    "item_id": row.item_id,
                }
            )


def _write_rejects(path: Path, source_file: Path, rows: list[RejectEntry]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(
            file_obj,
            fieldnames=["source_file", "source_row", "raw_value", "raw_url", "reason", "detail"],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "source_file": str(source_file),
                    "source_row": row.source_row,
                    "raw_value": row.raw_value,
                    "raw_url": row.raw_url,
                    "reason": row.reason,
                    "detail": row.detail,
                }
            )


def _write_summary(path: Path, source_file: Path, stats: dict[str, int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "source_file": str(source_file),
        "stats": stats,
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    args = parse_args()
    if not args.input.exists():
        raise SystemExit(f"Input file does not exist: {args.input}")

    entries = list(_iter_input_entries(args.input))
    accepts, rejects, stats = build_seed(entries)

    _write_accepts(args.accepted_csv, args.input, args.priority_group, accepts)
    _write_rejects(args.rejects_csv, args.input, rejects)
    _write_summary(args.summary_json, args.input, stats)

    print(f"input={args.input}")
    print(f"accepted={len(accepts)}")
    print(f"rejected={len(rejects)}")
    print(f"accepted_csv={args.accepted_csv}")
    print(f"rejects_csv={args.rejects_csv}")
    print(f"summary_json={args.summary_json}")


if __name__ == "__main__":
    main()
