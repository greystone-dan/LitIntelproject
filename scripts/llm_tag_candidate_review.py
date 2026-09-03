"""Propose immigration research tags with an external OpenAI pass.

This script is read-only: it reads stored decision text and writes only a review report.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal


DEFAULT_MODEL = "gpt-4o-mini"
ALLOWED_CATEGORIES = {
    "inadmissibility_organization",
    "immigration_keyword",
    "proceeding",
    "remedy",
    "risk",
    "immigration_status",
    "immigration_program",
    "procedural_issue",
    "country_or_territory",
}
SYSTEM_PROMPT = """You identify useful search and tagging vocabulary in Canadian immigration decisions.
Return JSON only with this shape: {"tags": [{"category": "...", "canonical": "...", "variations": ["..."], "evidence": "...", "confidence": 0.0}]}

Rules:
- Find named external organizations, especially political, militant, insurgent, armed, or extremist groups relevant to inadmissibility analysis. Do not propose Canadian unions, agencies, courts, ministers, generic committees, or generic roles.
- Find immigration-specific concepts useful for search, such as asylum, refugee protection, stay of removal, removal, detention, security inadmissibility, misrepresentation, sponsorship, PRRA, H&C, and related variations.
- Find countries and territories only when the text clearly names a place. Preserve disputed or non-sovereign places when relevant; do not invent countries from ordinary nouns.
- Normalize each concept to a concise lower-case canonical value. Put spelling, acronym, French, and expanded-name forms in variations.
- Do not return case names, judge names, statutes, citations, generic words, or broad legal boilerplate as tags.
- Evidence must be a short verbatim quote from the supplied text. Confidence must be between 0 and 1.
- Use only the allowed categories supplied by the user prompt.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--max-text-chars", type=int, default=12000)
    parser.add_argument("--pause-seconds", type=float, default=0.2)
    parser.add_argument("--report-json", type=Path, default=Path("data/eval/reports/llm-tag-candidate-review.json"))
    return parser.parse_args()


def case_text(case: Case, maximum: int) -> str:
    text = "\n".join(value for value in (case.title, case.summary, case.full_text) if value)
    return text[:maximum]


def request_tags(client: OpenAI, model: str, text: str) -> list[dict]:
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Allowed categories: {', '.join(sorted(ALLOWED_CATEGORIES))}\n\n"
                    "Identify candidate tags and variations in this decision text:\n\n"
                    f"{text}"
                ),
            },
        ],
    )
    content = response.choices[0].message.content or "{}"
    payload = json.loads(content)
    return payload.get("tags", []) if isinstance(payload, dict) else []


def normalize(value: str) -> str:
    return " ".join(value.lower().split()).strip(" .,:;()[]")


def main() -> None:
    args = parse_args()
    if args.limit < 1 or args.batch_size < 1 or args.max_text_chars < 100:
        raise SystemExit("limit, batch-size, and max-text-chars must be positive")
    load_dotenv(PROJECT_ROOT / ".env")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is required in .env or the environment")
    os.environ.pop("OPENAI_ORG_ID", None)
    client = OpenAI(api_key=api_key)
    tags: dict[tuple[str, str], dict] = {}
    samples: defaultdict[tuple[str, str], list[dict]] = defaultdict(list)
    case_ids: defaultdict[tuple[str, str], set[int]] = defaultdict(set)
    processed = 0

    with SessionLocal() as session:
        cases = session.scalars(select(Case).order_by(Case.id).limit(args.limit)).all()
    for case in cases:
        text = case_text(case, args.max_text_chars)
        if not text:
            continue
        for attempt in range(3):
            try:
                proposed_tags = request_tags(client, args.model, text)
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)
        for proposed in proposed_tags:
            category = normalize(str(proposed.get("category", "")))
            canonical = normalize(str(proposed.get("canonical", "")))
            confidence = float(proposed.get("confidence", 0))
            if category not in ALLOWED_CATEGORIES or not canonical or not 0 <= confidence <= 1:
                continue
            key = (category, canonical)
            tags.setdefault(key, {
                "category": category,
                "canonical": canonical,
                "variations": sorted({normalize(str(value)) for value in proposed.get("variations", []) if value}),
                "confidence_max": confidence,
                "case_count": 0,
            })
            tags[key]["variations"] = sorted(set(tags[key]["variations"]) | {
                normalize(str(value)) for value in proposed.get("variations", []) if value
            })
            tags[key]["confidence_max"] = max(tags[key]["confidence_max"], confidence)
            case_ids[key].add(case.id)
            if len(samples[key]) < 3:
                samples[key].append({"case_id": case.id, "citation": case.citation, "evidence": proposed.get("evidence", "")})
        for key in tags:
            tags[key]["case_count"] = len(case_ids[key])
        processed += 1
        if processed % args.batch_size == 0:
            print(f"processed_cases={processed} tags={len(tags)}", flush=True)
        if args.pause_seconds:
            time.sleep(args.pause_seconds)

    report = {
        "processed_cases": processed,
        "model": args.model,
        "max_text_chars": args.max_text_chars,
        "read_only": True,
        "tags": [dict(value, samples=samples[key]) for key, value in sorted(tags.items())],
    }
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")
    print(f"processed_cases={processed}")
    print(f"tags={len(report['tags'])}")
    print(f"report_json={args.report_json}")


if __name__ == "__main__":
    main()