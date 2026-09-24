"""Run a bounded model-paragraph versus deterministic-paragraph experiment."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
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
from scripts.chunk_cases import case_text
from scripts.discussion_units_ledger import record_case, should_skip
from scripts.package_discussion_units_llm import _parse_response, build_request


MODEL = "gpt-4.1-nano"
MAX_BUDGET_USD = 3.0
REQUEST_TIMEOUT_SECONDS = 180.0


def build_segmentation_request(case_id: int, source_text: str, *, model: str, budget_usd: float) -> dict[str, Any]:
    system = (
        "Segment the supplied Canadian legal decision into source-faithful reading spans. "
        "Identify any introductory metadata, every numbered legal paragraph, and any outro "
        "or footer text. Return JSON with a segments array. Each segment must contain kind "
        "(intro, paragraph, or outro), paragraph_number when kind is paragraph, start_offset, "
        "and end_offset. Offsets are zero-based and end-exclusive. Do not return segment text: "
        "the caller will derive it from the source after validating offsets. Preserve source "
        "order. Do not summarize, normalize, omit, or invent text. Paragraph segments must "
        "cover the decision body in order; use intro/outro only for text outside that body. "
        "Before responding, verify offsets are within the source and segments do not overlap."
    )
    payload = {
        "request_id": f"model-paragraphs-case-{case_id}",
        "contract_version": "model_paragraphs_v1",
        "case_id": case_id,
        "source_text": source_text,
    }
    return {
        "model": model,
        "budget_usd": budget_usd,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=True)},
        ],
    }


def _usage(response: Any) -> dict[str, Any]:
    prompt_tokens = int(getattr(response.usage, "prompt_tokens", 0) or 0)
    completion_tokens = int(getattr(response.usage, "completion_tokens", 0) or 0)
    return {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": int(getattr(response.usage, "total_tokens", 0) or 0),
        "estimated_cost_usd": prompt_tokens * 0.10 / 1_000_000 + completion_tokens * 0.40 / 1_000_000,
    }


def parse_segments(content: str, source_text: str) -> list[dict[str, Any]]:
    payload = json.loads(content)
    segments = payload.get("segments") if isinstance(payload, dict) else None
    if not isinstance(segments, list) or not segments:
        raise ValueError("response must contain a non-empty segments array")
    normalized: list[dict[str, Any]] = []
    expected_start = 0
    paragraph_index = 0
    for position, segment in enumerate(segments, 1):
        if not isinstance(segment, dict):
            raise ValueError(f"segment {position} is not an object")
        start = int(segment["start_offset"])
        end = int(segment["end_offset"])
        if start != expected_start or end <= start or end > len(source_text):
            raise ValueError(f"segment {position} has a gap, overlap, or invalid offset")
        returned_text = segment.get("text")
        if returned_text is not None and str(returned_text) != source_text[start:end]:
            raise ValueError(f"segment {position} text does not match its source offsets")
        kind = str(segment.get("kind", "")).lower()
        if kind not in {"intro", "paragraph", "outro"}:
            raise ValueError(f"segment {position} has invalid kind {kind!r}")
        item = {"kind": kind, "start_offset": start, "end_offset": end, "text": source_text[start:end]}
        if kind == "paragraph":
            item["paragraph_number"] = segment.get("paragraph_number")
            item["paragraph_index"] = paragraph_index
            paragraph_index += 1
        normalized.append(item)
        expected_start = end
    if expected_start != len(source_text):
        raise ValueError("segments do not cover the complete source text")
    if not any(item["kind"] == "paragraph" for item in normalized):
        raise ValueError("response contains no paragraph segments")
    return normalized


def _call(client: OpenAI, request: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    response = client.chat.completions.create(
        model=request["model"],
        temperature=0,
        max_tokens=3000,
        response_format={"type": "json_object"},
        messages=request["messages"],
    )
    return response.choices[0].message.content or "{}", _usage(response)


def build_model_report(case_id: int, source_text: str, segments: list[dict[str, Any]]) -> dict[str, Any]:
    paragraphs = [
        {
            "paragraph_index": item["paragraph_index"],
            "source_paragraph_number": item.get("paragraph_number"),
            "start_offset": item["start_offset"],
            "end_offset": item["end_offset"],
            "text": item["text"],
            "citation_ids": [],
            "statute_ids": [],
            "tag_ids": [],
            "is_heading": False,
        }
        for item in segments
        if item["kind"] == "paragraph"
    ]
    return {
        "case_id": case_id,
        "paragraph_source": "model_segments_v1",
        "source_text_length": len(source_text),
        "segments": segments,
        "paragraph_count": len(paragraphs),
        "paragraphs": paragraphs,
        "discussion_unit_count": 0,
        "discussion_units": [],
        "canonical_writes": 0,
        "contextual_writes": 0,
    }


def render_experiment_markdown(report: dict[str, Any], result: dict[str, Any], *, usage: dict[str, Any], model: str) -> str:
    lines = [
        f"# Model-paragraph Discussion Units: case {report['case_id']}",
        "",
        f"Model: `{model}`",
        f"Model paragraphs: `{report['paragraph_count']}`",
        f"Source characters: `{report['source_text_length']}`",
        f"Paragraph-label prompt tokens: `{usage['segmentation']['prompt_tokens']}`",
        f"Discussion prompt tokens: `{usage['discussion']['prompt_tokens']}`",
        f"Total tokens: `{usage['total_tokens']}`",
        f"Estimated billing (USD): `${usage['estimated_cost_usd']}`",
        "",
        "This is a provisional, read-only comparison using model-identified paragraph spans.",
        "",
    ]
    for unit in result["units"]:
        lines.extend([
            f"## Paragraphs {unit['start_paragraph']}-{unit['end_paragraph']}: {unit['label']}",
            "",
            unit["explanation"],
            "",
            f"- Transition: {unit['transition_from_previous']}",
            f"- Confidence: {unit.get('confidence', 'not supplied')}",
            "",
        ])
    return "\n".join(lines)


def run_case(case_id: int, output_dir: Path, *, model: str, budget_usd: float, send: bool, ledger_path: Path) -> None:
    with SessionLocal() as session:
        case = session.scalar(select(Case).where(Case.id == case_id))
        if case is None:
            raise ValueError(f"case {case_id} was not found")
        source_text = case_text(case)
    if not source_text.strip():
        raise ValueError(f"case {case_id} has no source text")
    output_dir.mkdir(parents=True, exist_ok=True)
    request_path = output_dir / f"case_{case_id}_requests.json"
    report_path = output_dir / f"case_{case_id}_model_paragraphs.json"
    markdown_path = output_dir / f"case_{case_id}_discussion_units.md"
    segmentation_request = build_segmentation_request(case_id, source_text, model=model, budget_usd=budget_usd)
    if not send:
        request_path.write_text(json.dumps({"segmentation_request": segmentation_request}, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
        return
    os.environ.pop("OPENAI_ORG_ID", None)
    os.environ.pop("OPENAI_ORGANIZATION", None)
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        timeout=REQUEST_TIMEOUT_SECONDS,
        max_retries=0,
    )
    segmentation_content, segmentation_usage = _call(client, segmentation_request)
    segments = parse_segments(segmentation_content, source_text)
    report = build_model_report(case_id, source_text, segments)
    discussion_request = build_request(
        report,
        model=model,
        budget_usd=budget_usd,
        text_only=True,
        normalize_legal_paragraphs=False,
    )
    discussion_content, discussion_usage = _call(client, discussion_request)
    result = _parse_response(discussion_content, report["paragraphs"])
    usage = {
        "segmentation": segmentation_usage,
        "discussion": discussion_usage,
        "prompt_tokens": segmentation_usage["prompt_tokens"] + discussion_usage["prompt_tokens"],
        "completion_tokens": segmentation_usage["completion_tokens"] + discussion_usage["completion_tokens"],
        "total_tokens": segmentation_usage["total_tokens"] + discussion_usage["total_tokens"],
        "estimated_cost_usd": segmentation_usage["estimated_cost_usd"] + discussion_usage["estimated_cost_usd"],
    }
    report["discussion_result"] = result
    report["usage"] = usage
    report["created_at"] = datetime.now(timezone.utc).isoformat()
    request_path.write_text(json.dumps({"segmentation_request": segmentation_request, "discussion_request": discussion_request, "response": {"segments": segments, "result": result, "usage": usage}}, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    markdown_path.write_text(render_experiment_markdown(report, result, usage=usage, model=model), encoding="utf-8")
    record_case(ledger_path, case_id, "complete", mode="network", unit_count=len(result["units"]), usage=usage, spent_usd=usage["estimated_cost_usd"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-ids", required=True, help="Comma-separated approved case IDs")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--ledger-path", type=Path, required=True)
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--budget-usd", type=float, default=1.0)
    parser.add_argument("--send", action="store_true")
    parser.add_argument("--retry-failed", action="store_true")
    args = parser.parse_args()
    if args.budget_usd <= 0 or args.budget_usd > MAX_BUDGET_USD:
        parser.error(f"--budget-usd must be between 0 and {MAX_BUDGET_USD}")
    case_ids = [int(value.strip()) for value in args.case_ids.split(",") if value.strip()]
    if len(case_ids) != 20 or len(set(case_ids)) != 20:
        parser.error("--case-ids must contain exactly 20 unique IDs")
    summary = {"selected": len(case_ids), "completed": 0, "failed": 0, "skipped": 0, "network_called": args.send}
    for case_id in case_ids:
        if should_skip(args.ledger_path, case_id, retry_failed=args.retry_failed):
            summary["skipped"] += 1
            continue
        try:
            run_case(case_id, args.output_dir, model=args.model, budget_usd=args.budget_usd, send=args.send, ledger_path=args.ledger_path)
        except Exception as exc:
            record_case(args.ledger_path, case_id, "failed", error=str(exc))
            summary["failed"] += 1
            continue
        summary["completed"] += 1
    print(json.dumps(summary, sort_keys=True))
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())