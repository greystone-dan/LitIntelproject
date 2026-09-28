"""Generate a bounded, report-only local paragraph-summary baseline."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from typing import Any

from sqlalchemy import select

from backend.database import CaseChunk, SessionLocal
from backend.text_generation_providers import get_text_generation_provider


def build_request(case_id: int, paragraphs: list[dict[str, Any]]) -> list[dict[str, str]]:
    payload = {
        "case_id": case_id,
        "paragraphs": [
            {"paragraph_index": item["paragraph_index"], "text": item["text"]}
            for item in paragraphs
        ],
    }
    system = (
        "Summarize the supplied Canadian legal decision paragraph. Use only its text. "
        "Return JSON with a summaries array containing exactly one entry. The entry must contain "
        "paragraph_index, summary, topic, role, and confidence. Do not merge paragraphs, "
        "invent facts or citations, or add paragraph indices. Keep each summary to one "
        "or two sentences and distinguish facts, party submissions, findings, reasoning, "
        "and disposition when possible."
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": json.dumps(payload, ensure_ascii=True, sort_keys=True)},
    ]


def load_paragraphs(report: dict[str, Any]) -> list[dict[str, Any]]:
    paragraphs = report["paragraphs"]
    if all("text" in item for item in paragraphs):
        return paragraphs
    chunk_ids = {item["chunk_id"] for item in paragraphs}
    with SessionLocal() as session:
        chunks = session.scalars(select(CaseChunk).where(CaseChunk.id.in_(chunk_ids))).all()
    chunks_by_id = {chunk.id: chunk for chunk in chunks}
    loaded: list[dict[str, Any]] = []
    for item in paragraphs:
        chunk = chunks_by_id.get(item["chunk_id"])
        if chunk is None:
            raise ValueError(f"missing source chunk {item['chunk_id']}")
        text = (chunk.text or "")[item["start_offset"] : item["end_offset"]]
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if text_hash != item["text_sha256"]:
            raise ValueError(f"text hash mismatch for paragraph {item['paragraph_index']}")
        loaded.append({**item, "text": text, "container_paragraph_index": item["source_paragraph_index"]})
    return loaded


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--start-paragraph", type=int, default=0)
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--max-tokens", type=int, default=1600)
    args = parser.parse_args()
    if args.count < 1 or args.count > 10:
        parser.error("--count must be between 1 and 10")

    report = json.loads(args.input.read_text(encoding="utf-8"))
    paragraphs = load_paragraphs(report)
    selected = [
        item
        for item in paragraphs
        if args.start_paragraph <= item["paragraph_index"] < args.start_paragraph + args.count
    ]
    if len(selected) != args.count:
        raise SystemExit(f"requested {args.count} paragraphs, found {len(selected)}")

    provider = get_text_generation_provider()
    records: list[dict[str, Any]] = []
    prompt_tokens = 0
    completion_tokens = 0
    for paragraph in selected:
        started = time.perf_counter()
        content = ""
        failure_type = None
        try:
            completion = provider.create_chat_completion(
                model=provider.model_name,
                temperature=0,
                max_tokens=args.max_tokens,
                response_format={"type": "json_object"},
                messages=build_request(int(report["case_id"]), [paragraph]),
            )
            prompt_tokens += int(getattr(completion.usage, "prompt_tokens", 0) or 0)
            completion_tokens += int(getattr(completion.usage, "completion_tokens", 0) or 0)
            content = completion.choices[0].message.content or ""
            parsed = json.loads(content)
            summaries = parsed.get("summaries")
            if not isinstance(summaries, list) or len(summaries) != 1:
                failure_type = "wrong_summary_count_or_shape"
                raise ValueError("response did not contain exactly one summary")
            summary = summaries[0]
            if summary.get("paragraph_index") != paragraph["paragraph_index"]:
                failure_type = "paragraph_index_mismatch"
                raise ValueError("response paragraph index mismatch")
            if not str(summary.get("summary", "")).strip():
                failure_type = "empty_summary"
                raise ValueError("summary was empty")
            records.append({"status": "complete", "elapsed_seconds": time.perf_counter() - started, **summary})
        except Exception as exc:
            if failure_type is None:
                failure_type = "empty_response" if not content else type(exc).__name__
            records.append({
                "status": "failed",
                "paragraph_index": paragraph["paragraph_index"],
                "elapsed_seconds": time.perf_counter() - started,
                "failure_type": failure_type,
                "error": str(exc),
                "raw_response": content,
            })

    output = {
        "status": "local_paragraph_summary_baseline_complete",
        "network_called": True,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "model": provider.model_name,
        "provider": type(provider).__name__,
        "case_id": int(report["case_id"]),
        "source_file": str(args.input),
        "paragraph_range": {"start": selected[0]["paragraph_index"], "end": selected[-1]["paragraph_index"]},
        "source_paragraphs": [
            {
                "paragraph_index": item["paragraph_index"],
                "container_paragraph_index": item.get("container_paragraph_index"),
                "text_sha256": hashlib.sha256(item["text"].encode("utf-8")).hexdigest(),
            }
            for item in selected
        ],
        "usage": {"prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens},
        "summaries": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": output["status"], "model": output["model"], "paragraphs": len(records), "output": str(args.output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
