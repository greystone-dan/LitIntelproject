"""Canonical ingestion helpers for the Hugging Face A2AJ FC activity dataset.

This module defines the normalized shape used for the downloadable FC activity
source. It intentionally reflects the dataset schema first, rather than the
legacy FC procedural-history scrape format.
"""

from __future__ import annotations

import hashlib
import json
from collections import OrderedDict
from datetime import date, datetime
from typing import Any


def _clean(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = " ".join(value.strip().split())
        return cleaned or None
    return value


def _stable_key(*parts: Any) -> str:
    payload = "|".join("" if part is None else str(part) for part in parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _parse_date(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    text = str(value).strip()
    if not text:
        return None
    for candidate in (text, text[:10]):
        try:
            return datetime.fromisoformat(candidate.replace("Z", "+00:00")).date().isoformat()
        except ValueError:
            pass
    return text


def _document_entry_hash(*parts: Any) -> str:
    payload = "|".join("" if part is None else str(part) for part in parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def derive_case_source_key(record: dict[str, Any]) -> str:
    citation = _clean(record.get("citation"))
    case_name = _clean(record.get("name"))
    source_url = _clean(record.get("source_url"))
    date_filed = _parse_date(record.get("date_filed"))
    year = record.get("year")

    if citation:
        identity = {"citation": citation, "year": year}
    else:
        identity = {
            "case_name": case_name,
            "source_url": source_url,
            "date_filed": date_filed,
            "year": year,
        }

    if not any(value for value in identity.values() if value not in (None, "", [])):
        identity = {"raw_payload": json.dumps(record, sort_keys=True, separators=(",", ":"), default=str)}

    encoded = json.dumps(identity, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _normalize_document(document: Any) -> dict[str, Any] | None:
    if not isinstance(document, dict):
        return None

    re_no = _clean(document.get("RE_NO"))
    docno = _clean(document.get("DOCNO"))
    doc_dt = _parse_date(document.get("DOC_DT"))
    recorded_entry = _clean(document.get("RECORDED_ENTRY"))

    if recorded_entry is None and doc_dt is None and re_no is None and docno is None:
        return None

    entry_hash = _document_entry_hash(re_no, docno, doc_dt, recorded_entry)
    return {
        "re_no": re_no,
        "docno": docno,
        "doc_dt": doc_dt,
        "recorded_entry": recorded_entry,
        "entry_key": _stable_key(re_no, docno, doc_dt, recorded_entry),
        "entry_hash": entry_hash,
    }


def normalize_hf_case_record(record: dict[str, Any]) -> dict[str, Any]:
    """Normalize one row from the HF A2AJ FC activity dataset.

    The canonical form keeps the original case metadata and preserves each docket
    entry as an individual document record. The output is designed to be a stable
    staging structure before any downstream compatibility mapping to the app's
    legacy FC procedural-history fields.

    The source parquet may be either the planned document-list format or the
    cached A2AJ Federal Court parquet format used in this repository, so the
    normalizer supports both shapes.
    """
    documents = record.get("documents") or []
    normalized_documents: list[dict[str, Any]] = []

    if isinstance(documents, list) and documents:
        for document in documents:
            if not isinstance(document, dict):
                continue
            normalized = _normalize_document(document)
            if normalized is None:
                continue
            normalized_documents.append(
                {
                    "re_no": normalized["re_no"],
                    "docno": normalized["docno"],
                    "doc_dt": normalized["doc_dt"],
                    "recorded_entry": normalized["recorded_entry"],
                    "entry_key": normalized["entry_key"],
                    "entry_hash": normalized["entry_hash"],
                }
            )
    else:
        parquet_like = any(
            key in record
            for key in (
                "unofficial_text_en",
                "unofficial_text_fr",
                "document_date_en",
                "document_date_fr",
                "url_en",
                "url_fr",
                "scraped_timestamp_en",
                "scraped_timestamp_fr",
            )
        )
        if parquet_like:
            citation = _clean(record.get("citation") or record.get("citation_en") or record.get("citation_fr"))
            case_name = _clean(record.get("name") or record.get("name_en") or record.get("name_fr"))
            source_url = _clean(record.get("source_url") or record.get("url_en") or record.get("url_fr"))
            date_filed_value = record.get("date_filed") or record.get("document_date_en") or record.get("document_date_fr")
            date_filed = _parse_date(date_filed_value)
            full_text = _clean(
                record.get("recorded_entry")
                or record.get("unofficial_text_en")
                or record.get("unofficial_text_fr")
                or record.get("full_text")
            )
            if full_text or source_url or citation or case_name or date_filed:
                normalized_documents.append(
                    {
                        "re_no": "1",
                        "docno": "raw-row",
                        "doc_dt": date_filed,
                        "recorded_entry": full_text or "Imported from source parquet row.",
                        "entry_key": _stable_key("1", "raw-row", date_filed, full_text or "Imported from source parquet row."),
                        "entry_hash": _document_entry_hash("1", "raw-row", date_filed, full_text or "Imported from source parquet row."),
                    }
                )

    source_key = derive_case_source_key(record)

    raw_date_filed = record.get("date_filed")
    if isinstance(raw_date_filed, str) and "T" in raw_date_filed:
        normalized_date_filed = raw_date_filed
    else:
        normalized_date_filed = _parse_date(
            record.get("date_filed") or record.get("document_date_en") or record.get("document_date_fr")
        )

    return {
        "source_key": source_key,
        "citation": record.get("citation") or record.get("citation_en") or record.get("citation_fr"),
        "year": record.get("year") or (
            getattr(record.get("document_date_en"), "year", None)
            if isinstance(record.get("document_date_en"), datetime)
            else None
        ),
        "case_name": record.get("name") or record.get("name_en") or record.get("name_fr"),
        "date_filed": normalized_date_filed,
        "city_filed": record.get("city_filed") or record.get("city_en") or record.get("city_fr"),
        "nature": record.get("nature") or record.get("nature_en") or record.get("nature_fr"),
        "case_class": record.get("case_class") or record.get("class") or record.get("class_en"),
        "track": record.get("track") or record.get("track_en") or record.get("track_fr"),
        "source_url": record.get("source_url") or record.get("url_en") or record.get("url_fr"),
        "scraped_timestamp": record.get("scraped_timestamp") or record.get("scraped_timestamp_en") or record.get("scraped_timestamp_fr"),
        "documents": normalized_documents,
    }


def normalize_fc_activity(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Normalize a batch of HF FC activity rows into canonical case and document records.

    This keeps case metadata, preserves each docket fragment, and deduplicates both
    repeated case rows and repeated document entries using stable keys.
    """
    cases: OrderedDict[str, dict[str, Any]] = OrderedDict()
    documents: list[dict[str, Any]] = []
    duplicates_removed = 0

    for row in rows or []:
        if not isinstance(row, dict):
            continue

        citation = _clean(row.get("citation"))
        case_name = _clean(row.get("name"))
        source_url = _clean(row.get("source_url"))
        date_filed = _parse_date(row.get("date_filed"))
        year = row.get("year")
        city_filed = _clean(row.get("city_filed"))
        nature = _clean(row.get("nature"))
        case_class = _clean(row.get("class"))
        track = _clean(row.get("track"))
        scraped_timestamp = _parse_date(row.get("scraped_timestamp"))
        source_key = derive_case_source_key(row)

        if source_key in cases:
            duplicates_removed += 1
            case_record = cases[source_key]
        else:
            case_record = {
                "source_key": source_key,
                "citation": citation,
                "case_name": case_name,
                "year": year,
                "date_filed": date_filed,
                "city_filed": city_filed,
                "nature": nature,
                "case_class": case_class,
                "track": track,
                "source_url": source_url,
                "scraped_timestamp": scraped_timestamp,
                "documents": [],
                "case_key": source_key,
            }
            cases[source_key] = case_record

        for raw_document in row.get("documents") or []:
            normalized_document = _normalize_document(raw_document)
            if normalized_document is None:
                continue

            doc_key = normalized_document["entry_key"]
            seen_document = any(
                document.get("entry_key") == doc_key and document.get("case_key") == source_key
                for document in documents
            )
            if seen_document:
                duplicates_removed += 1
                continue

            document_record = {
                "case_key": source_key,
                "re_no": normalized_document["re_no"],
                "docno": normalized_document["docno"],
                "doc_dt": normalized_document["doc_dt"],
                "recorded_entry": normalized_document["recorded_entry"],
                "entry_key": doc_key,
                "entry_hash": normalized_document["entry_hash"],
            }
            documents.append(document_record)
            case_record["documents"].append(document_record)

    return {"cases": list(cases.values()), "documents": documents, "duplicates_removed": duplicates_removed}


def load_hf_fc_activity_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Convert raw dataset rows into the canonical FC activity shape."""
    normalized = normalize_fc_activity(rows)
    return [{
        "source_key": case["source_key"],
        "citation": case["citation"],
        "year": case["year"],
        "case_name": case["case_name"],
        "date_filed": case["date_filed"],
        "city_filed": case["city_filed"],
        "nature": case["nature"],
        "case_class": case["case_class"],
        "track": case["track"],
        "source_url": case["source_url"],
        "scraped_timestamp": case["scraped_timestamp"],
        "documents": [
            {
                "re_no": document["re_no"],
                "docno": document["docno"],
                "doc_dt": document["doc_dt"],
                "recorded_entry": document["recorded_entry"],
                "entry_key": document.get("entry_key"),
                "entry_hash": document.get("entry_hash"),
            }
            for document in case["documents"]
        ],
    } for case in normalized["cases"]]
