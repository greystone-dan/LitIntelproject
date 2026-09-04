"""Download a provenance-preserving reference corpus kept separate from cases."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = PROJECT_ROOT / "data" / "reference_library" / "manifest.json"
USER_AGENT = "AI-CaseLibrary-ReferenceLibrary/1.0"
PDF_MIME_TYPES = {"application/pdf", "application/x-pdf"}
HTML_MIME_TYPES = {"text/html", "application/xhtml+xml"}
XML_MIME_TYPES = {"application/xml", "text/xml", "application/octet-stream"}
INVENTORY_FIELDS = (
    "id",
    "publisher",
    "title",
    "source_type",
    "document_date",
    "jurisdiction",
    "topics",
    "status",
    "retrieved_at",
    "source_url",
    "final_url",
    "local_path",
    "mime_type",
    "size_bytes",
    "sha256",
    "error_reason",
)


class ValidationError(ValueError):
    """Raised when a response does not match its declared source type."""


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def normalized_mime(content_type: str | None) -> str:
    return (content_type or "").split(";", 1)[0].strip().lower()


def validate_content(content: bytes, content_type: str | None, source_type: str) -> str:
    mime_type = normalized_mime(content_type)
    prefix = content.lstrip()[:1024].lower()

    if source_type == "pdf":
        if mime_type not in PDF_MIME_TYPES:
            raise ValidationError(f"Expected PDF MIME type, received {mime_type or 'missing'}")
        if not content.startswith(b"%PDF-"):
            raise ValidationError("Response does not begin with the PDF signature")
        return mime_type

    if source_type == "html":
        if mime_type not in HTML_MIME_TYPES:
            raise ValidationError(f"Expected HTML MIME type, received {mime_type or 'missing'}")
        if not re.search(br"<(?:!doctype\s+html|html|head|body)(?:\s|>)", prefix):
            raise ValidationError("Response does not contain recognizable HTML markup")
        return mime_type

    if source_type == "xml":
        if mime_type not in XML_MIME_TYPES:
            raise ValidationError(f"Expected XML MIME type, received {mime_type or 'missing'}")
        if not re.search(br"<\?xml\b|<Statute\b", content.lstrip()[:2048], re.IGNORECASE):
            raise ValidationError("Response does not contain recognizable XML markup")
        return mime_type

    raise ValidationError(f"Unsupported source_type: {source_type}")


def safe_local_path(library_root: Path, relative_path: str) -> Path:
    destination = (library_root / relative_path).resolve()
    root = library_root.resolve()
    if destination != root and root not in destination.parents:
        raise ValueError(f"local_path escapes reference library: {relative_path}")
    return destination


def atomic_write_bytes(destination: Path, content: bytes) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(f".{destination.name}.{os.getpid()}.tmp")
    try:
        temporary.write_bytes(content)
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


def atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    content = (json.dumps(payload, indent=2, ensure_ascii=True) + "\n").encode("utf-8")
    atomic_write_bytes(path, content)


def write_inventory_csv(path: Path, documents: list[dict[str, Any]]) -> None:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=INVENTORY_FIELDS, extrasaction="ignore")
    writer.writeheader()
    for document in documents:
        row = dict(document)
        row["topics"] = ";".join(document.get("topics", []))
        writer.writerow(row)
    atomic_write_bytes(path, buffer.getvalue().encode("utf-8"))


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file_obj:
        manifest = json.load(file_obj)
    if manifest.get("schema_version") != "reference_library_v1":
        raise ValueError("Manifest schema_version must be reference_library_v1")
    if not isinstance(manifest.get("documents"), list):
        raise ValueError("Manifest documents must be a list")
    return manifest


def download_entry(
    entry: dict[str, Any],
    library_root: Path,
    session: requests.Session,
    timeout: float,
) -> dict[str, Any]:
    destination = safe_local_path(library_root, entry["local_path"])
    response = session.get(
        entry["source_url"],
        headers={"User-Agent": USER_AGENT, "Accept": "application/pdf,text/html,application/xml;q=0.9"},
        timeout=timeout,
        allow_redirects=True,
    )
    response.raise_for_status()
    content = response.content
    mime_type = validate_content(content, response.headers.get("Content-Type"), entry["source_type"])
    atomic_write_bytes(destination, content)

    entry.update(
        {
            "retrieved_at": utc_now_iso(),
            "final_url": response.url,
            "mime_type": mime_type,
            "sha256": sha256_bytes(content),
            "size_bytes": len(content),
            "status": "downloaded",
            "error_reason": None,
        }
    )
    return entry


def existing_download_is_valid(entry: dict[str, Any], library_root: Path) -> bool:
    if entry.get("status") != "downloaded" or not entry.get("sha256"):
        return False
    destination = safe_local_path(library_root, entry["local_path"])
    if not destination.is_file():
        return False
    return sha256_bytes(destination.read_bytes()) == entry["sha256"]


def run(
    manifest_path: Path,
    timeout: float = 60.0,
    limit: int | None = None,
    force: bool = False,
    source_ids: set[str] | None = None,
    session: requests.Session | None = None,
) -> dict[str, int]:
    manifest = load_manifest(manifest_path)
    library_root = manifest_path.parent
    http = session or requests.Session()
    counts = {"downloaded": 0, "skipped": 0, "failed": 0}
    attempted = 0

    for entry in manifest["documents"]:
        if source_ids and entry.get("id") not in source_ids:
            continue
        if not force and existing_download_is_valid(entry, library_root):
            counts["skipped"] += 1
            continue
        if limit is not None and attempted >= limit:
            break
        attempted += 1

        try:
            download_entry(entry, library_root, http, timeout)
            counts["downloaded"] += 1
        except Exception as exc:
            entry.update(
                {
                    "retrieved_at": utc_now_iso(),
                    "status": "failed",
                    "error_reason": f"{type(exc).__name__}: {exc}",
                }
            )
            counts["failed"] += 1
        manifest["updated_at"] = utc_now_iso()
        atomic_write_json(manifest_path, manifest)

    write_inventory_csv(library_root / "inventory.csv", manifest["documents"])
    return counts


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--source-id", action="append", default=[])
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be at least 1")
    counts = run(
        manifest_path=args.manifest.resolve(),
        timeout=args.timeout,
        limit=args.limit,
        force=args.force,
        source_ids=set(args.source_id) or None,
    )
    print(json.dumps(counts, sort_keys=True))
    if counts["failed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()