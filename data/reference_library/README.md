# Canadian Immigration Reference Library

This directory stores legislation, tribunal guidance, court procedure, and
immigration-program materials. These documents are references, not judicial or
administrative decisions, and must never be inserted into canonical case tables.

## Contents

- `manifest.json` is the authoritative provenance record.
- `inventory.csv` is a flat, filterable view generated from the manifest.
- `documents/` contains byte-for-byte snapshots grouped by publisher or function.

Each downloaded item records its publisher, title, original and final URL,
source type, document date when known, jurisdiction, topics, local path,
retrieval timestamp, MIME type, byte count, SHA-256 checksum, status, and failure
reason. HTML is retained as HTML; it is never renamed to look like a PDF.

Verified snapshot on 2026-08-01: `18/18` manifest entries are downloaded and
checksum-valid, comprising five PDFs and thirteen HTML snapshots.

## Refresh

```powershell
.\venv\Scripts\python.exe scripts\download_reference_library.py
```

Use `--source-id ID` to refresh selected records, `--limit N` for bounded runs,
or `--force` to replace checksum-valid snapshots. The downloader writes through
a temporary file and atomically renames only after the response passes strict
content validation. A PDF entry requires both a PDF MIME type and a `%PDF-`
signature; HTML and error responses are rejected for PDF entries.

The source pages are living publications. Refreshes intentionally update
retrieval metadata and checksums so changes remain detectable and attributable.