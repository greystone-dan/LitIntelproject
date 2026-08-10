from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
from typing import Any

from openai import OpenAI
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal
from fc_ingest.document_scraper import _extract_metadata_with_quality


DEFAULT_MODEL = os.getenv("OPENAI_METADATA_AUDIT_MODEL", "gpt-4.1-nano")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Adjudicate low-confidence FC metadata fields with constrained LLM fallback")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--min-confidence", type=float, default=0.9)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--apply", action="store_true", help="Write adjudicated metadata back to cases.metadata_json")
    parser.add_argument("--max-chars", type=int, default=16000)
    return parser.parse_args()


def _trim_text(full_text: str, max_chars: int) -> str:
    if len(full_text) <= max_chars:
        return full_text
    head = max_chars // 2
    tail = max_chars - head
    return full_text[:head] + "\n[...truncated...]\n" + full_text[-tail:]


def _adjudicate(client: OpenAI, model: str, text: str, current: dict[str, Any]) -> dict[str, str]:
    system = (
        "Extract legal case metadata from the provided decision text. "
        "Return strict JSON object only with keys: date, docket, neutral_citation, judge, style_of_cause, place_of_hearing, date_of_hearing, counsel. "
        "Use empty string for unknown values. Do not add extra keys."
    )
    user = json.dumps(
        {
            "current": {
                "date": current.get("date", ""),
                "docket": current.get("docket", ""),
                "neutral_citation": current.get("neutral citation", ""),
                "judge": current.get("judge", ""),
                "style_of_cause": current.get("style of cause", ""),
                "place_of_hearing": current.get("place of hearing", ""),
                "date_of_hearing": current.get("date of hearing", ""),
                "counsel": current.get("counsel", ""),
            },
            "text": text,
        },
        ensure_ascii=True,
    )

    completion = client.chat.completions.create(
        model=model,
        temperature=0,
        max_tokens=400,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    content = (completion.choices[0].message.content or "{}").strip()
    if content.startswith("```"):
        content = content.strip("`")
        if content.startswith("json"):
            content = content[4:].strip()
    start = content.find("{")
    end = content.rfind("}")
    if start != -1 and end != -1 and end > start:
        content = content[start : end + 1]

    parsed = json.loads(content)
    if not isinstance(parsed, dict):
        return {}

    out: dict[str, str] = {}
    for key in (
        "date",
        "docket",
        "neutral_citation",
        "judge",
        "style_of_cause",
        "place_of_hearing",
        "date_of_hearing",
        "counsel",
    ):
        value = parsed.get(key)
        if value is None:
            continue
        value_str = " ".join(str(value).split()).strip()
        if value_str:
            out[key] = value_str
    return out


def main() -> None:
    args = parse_args()
    if args.min_confidence <= 0 or args.min_confidence > 1:
        raise SystemExit("--min-confidence must be in (0, 1]")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is required for adjudication")

    client = OpenAI(api_key=api_key)

    updated = 0
    reviewed = 0

    with SessionLocal() as session:
        query = (
            select(Case)
            .where(Case.full_text.is_not(None))
            .where(Case.full_text != "")
            .where((Case.court == "FC") | (Case.citation.ilike("% FC %")) | (Case.citation.ilike("% FCA %")))
            .order_by(Case.id.desc())
            .limit(args.limit)
        )
        cases = list(session.scalars(query))

        for case in cases:
            metadata = _extract_metadata_with_quality(case.full_text or "")
            confidence = metadata.get("_field_confidence") or {}

            low_critical = [
                field for field in ("date", "docket", "neutral citation", "judge", "style of cause")
                if confidence.get(field, 0.0) < args.min_confidence
            ]
            if not low_critical:
                continue

            reviewed += 1
            adjudicated = _adjudicate(client, args.model, _trim_text(case.full_text or "", args.max_chars), metadata)
            if not adjudicated:
                continue

            mapped = {
                "date": adjudicated.get("date"),
                "docket": adjudicated.get("docket"),
                "neutral citation": adjudicated.get("neutral_citation"),
                "judge": adjudicated.get("judge"),
                "style of cause": adjudicated.get("style_of_cause"),
                "place of hearing": adjudicated.get("place_of_hearing"),
                "date of hearing": adjudicated.get("date_of_hearing"),
                "counsel": adjudicated.get("counsel"),
            }

            changed = False
            for key, value in mapped.items():
                if not value:
                    continue
                if not metadata.get(key):
                    metadata[key] = value
                    changed = True

            if not changed:
                continue

            if args.apply:
                existing = dict(case.metadata_json or {})
                existing.setdefault("reader_extracted", {})
                existing["reader_extracted"].update(metadata)
                case.metadata_json = existing
                updated += 1

        if args.apply and updated:
            session.commit()

    print(
        {
            "reviewed_low_confidence": reviewed,
            "updated_cases": updated,
            "applied": args.apply,
            "model": args.model,
        }
    )


if __name__ == "__main__":
    main()
