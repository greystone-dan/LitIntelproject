"""Prepare and optionally run a bounded LLM Discussion Unit review."""

from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
from typing import Any

from openai import OpenAI

try:
    from scripts.discussion_units_ledger import record_case, should_skip
except ModuleNotFoundError:
    from discussion_units_ledger import record_case, should_skip


MODEL = "gpt-4.1-nano"
MAX_BUDGET_USD = 3.0


def _legal_paragraphs(paragraphs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    expanded: list[dict[str, Any]] = []
    seen_numbers: set[int] = set()
    numbered_text_exists = any(
        re.search(r"(?m)^\s*\[(\d{1,3})\](?=\s|$)", str(container["text"]))
        for container in paragraphs
    )
    for container in paragraphs:
        text = str(container["text"])
        matches = list(re.finditer(r"(?m)^\s*\[(\d{1,3})\](?=\s|$)", text))
        if not matches:
            if numbered_text_exists:
                continue
            expanded.append({**container, "paragraph_index": len(expanded), "container_paragraph_index": container["paragraph_index"]})
            continue
        for position, match in enumerate(matches):
            paragraph_number = int(match.group(1))
            if paragraph_number in seen_numbers:
                continue
            end = matches[position + 1].start() if position + 1 < len(matches) else len(text)
            segment = text[match.start():end].strip()
            seen_numbers.add(paragraph_number)
            expanded.append({
                **container,
                "paragraph_index": paragraph_number,
                "container_paragraph_index": container["paragraph_index"],
                "text": segment,
            })
    unique: dict[int, dict[str, Any]] = {}
    for item in expanded:
        unique.setdefault(item["paragraph_index"], item)
    return [unique[index] for index in sorted(unique)]


def build_request(
    report: dict[str, Any],
    *,
    model: str = MODEL,
    budget_usd: float = 1.0,
    text_only: bool = False,
    normalize_legal_paragraphs: bool = True,
) -> dict[str, Any]:
    paragraphs = report.get("paragraphs", [])
    if not paragraphs:
        raise ValueError("inspection report contains no paragraphs")
    expanded_paragraphs = _legal_paragraphs(paragraphs) if normalize_legal_paragraphs else paragraphs
    if text_only:
        compact_paragraphs = [
            {"paragraph_index": item["paragraph_index"], "text": item["text"]}
            for item in expanded_paragraphs
        ]
    else:
        compact_paragraphs = [
            {
                "paragraph_index": item["paragraph_index"],
                "container_paragraph_index": item["container_paragraph_index"],
                "source_paragraph_index": item.get("source_paragraph_index"),
                "text": item["text"],
                "citation_ids": item.get("citation_ids", []),
                "statute_ids": item.get("statute_ids", []),
                "tag_ids": item.get("tag_ids", []),
                "is_heading": item.get("is_heading", False),
            }
            for item in expanded_paragraphs
        ]
    system = (
        "You identify plain-language Discussion Units in a legal decision. "
        "Use only the supplied numbered paragraphs. Group contiguous paragraphs that "
        "perform one coherent task, such as procedural history, facts, party submissions, "
        "legal test, analysis/application, or disposition. Do not invent facts or citations. "
        "Return JSON with a units array. Each unit must contain start_paragraph, end_paragraph, "
        "label, explanation, transition_from_previous, and confidence. Use paragraph indices "
        "exactly as supplied; never output an index not present in the supplied list, and "
        "cover the supplied window from its first index through its last index exactly once. "
        "Before responding, verify that the first unit starts at the first_allowed index, "
        "the final unit ends at the last_allowed index, and there are no gaps or overlaps. "
        "Do not stop after summarizing only the most important paragraphs. "
        "Keep explanations short and readable for a legal researcher."
    )
    if text_only:
        system += " Do not rely on metadata or deterministic segmentation; infer the units from the paragraph text alone."
    payload = {
        "request_id": f"discussion-units-case-{report['case_id']}",
        "contract_version": "discussion_units_llm_v1",
        "case_id": report["case_id"],
        "paragraph_window": {
            "first_allowed": compact_paragraphs[0]["paragraph_index"],
            "last_allowed": compact_paragraphs[-1]["paragraph_index"],
        },
        "paragraphs": compact_paragraphs,
    }
    if not text_only:
        payload["deterministic_baseline"] = {
            "discussion_unit_count": report.get("discussion_unit_count", 0),
            "units": [
                {
                    "start_paragraph": unit["start_paragraph"],
                    "end_paragraph": unit["end_paragraph"],
                    "generation_method": unit.get("generation_method"),
                }
                for unit in report.get("discussion_units", [])
            ],
        }
    return {
        "model": model,
        "budget_usd": budget_usd,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=True, sort_keys=True)},
        ],
    }


def build_paragraph_assessment_request(
    report: dict[str, Any],
    paragraphs: list[dict[str, Any]],
    *,
    model: str = MODEL,
    budget_usd: float = 1.0,
) -> dict[str, Any]:
    system = (
        "Assess each supplied legal paragraph independently. Return JSON with an assessments "
        "array containing exactly one entry for every supplied paragraph, in the same order. "
        "Each entry must contain paragraph_index, topic, role, explanation, and confidence. "
        "Use the same topic for adjacent paragraphs when appropriate; do not merge entries "
        "or omit a paragraph. Use only the supplied paragraph text and do not invent facts, "
        "citations, or paragraph indices. Keep explanations short and readable for a legal "
        "researcher."
    )
    payload = {
        "request_id": f"discussion-paragraph-assessment-case-{report['case_id']}",
        "contract_version": "discussion_paragraph_assessment_v1",
        "case_id": report["case_id"],
        "paragraphs": [
            {"paragraph_index": item["paragraph_index"], "text": item["text"]}
            for item in paragraphs
        ],
    }
    return {
        "model": model,
        "budget_usd": budget_usd,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=True, sort_keys=True)},
        ],
    }


def _recover_assessments(content: str) -> tuple[list[Any], bool]:
    try:
        payload = json.loads(content)
    except json.JSONDecodeError:
        marker = content.find('"assessments"')
        array_start = content.find("[", marker)
        if marker < 0 or array_start < 0:
            raise
        decoder = json.JSONDecoder()
        position = array_start + 1
        assessments: list[Any] = []
        while position < len(content):
            while position < len(content) and content[position] in " \t\r\n,":
                position += 1
            if position >= len(content) or content[position] == "]":
                break
            try:
                assessment, position = decoder.raw_decode(content, position)
            except json.JSONDecodeError:
                break
            assessments.append(assessment)
        if not assessments:
            raise
        return assessments, False
    assessments = payload.get("assessments") if isinstance(payload, dict) else None
    if not isinstance(assessments, list):
        raise ValueError("response must contain an assessments array")
    return assessments, True


def _parse_paragraph_assessment(content: str, paragraphs: list[dict[str, Any]]) -> dict[str, Any]:
    assessments, complete_response = _recover_assessments(content)
    valid_indices = [item["paragraph_index"] for item in paragraphs]
    valid_index_set = set(valid_indices)
    by_index: dict[int, dict[str, Any]] = {}
    unmatched_count = 0
    for assessment in assessments:
        if not isinstance(assessment, dict):
            unmatched_count += 1
            continue
        try:
            paragraph_index = int(assessment.get("paragraph_index", -1))
        except (TypeError, ValueError):
            unmatched_count += 1
            continue
        if paragraph_index not in valid_index_set or paragraph_index in by_index:
            unmatched_count += 1
            continue
        by_index[paragraph_index] = {
                "paragraph_index": paragraph_index,
                "topic": str(assessment.get("topic") or "Unlabelled topic"),
                "role": str(assessment.get("role") or "Unspecified role"),
                "explanation": str(assessment.get("explanation") or "No explanation supplied."),
                "confidence": assessment.get("confidence"),
                "missing": False,
            }
    normalized = []
    missing_indices = []
    for paragraph_index in valid_indices:
        if paragraph_index in by_index:
            normalized.append(by_index[paragraph_index])
        else:
            missing_indices.append(paragraph_index)
            normalized.append(
                {
                    "paragraph_index": paragraph_index,
                    "topic": "Not found",
                    "role": "Not found",
                    "explanation": "No assessment was returned for this paragraph.",
                    "confidence": None,
                    "missing": True,
                }
            )
    return {
        "assessments": normalized,
        "returned_assessment_count": len(by_index),
        "missing_paragraph_indices": missing_indices,
        "unmatched_assessment_count": unmatched_count,
        "response_complete": complete_response,
    }


def render_paragraph_assessment_markdown(
    report: dict[str, Any],
    result: dict[str, Any],
    *,
    model: str,
    usage: dict[str, Any] | None = None,
) -> str:
    usage = usage or {}
    lines = [
        f"# Paragraph-level Discussion Assessment: case {report['case_id']}",
        "",
        f"Model: `{model}`",
        f"Prompt tokens: `{usage.get('prompt_tokens', 'not available')}`",
        f"Completion tokens: `{usage.get('completion_tokens', 'not available')}`",
        f"Total tokens: `{usage.get('total_tokens', 'not available')}`",
        f"Estimated billing (USD): `${usage.get('estimated_cost_usd', 'not available')}`",
        "",
        f"Returned assessments: `{result.get('returned_assessment_count', len(result['assessments']))}`",
        f"Missing paragraphs: `{len(result.get('missing_paragraph_indices', []))}`",
        f"Response complete: `{result.get('response_complete', True)}`",
        "",
        "Each row represents one source paragraph; repeated topics are intentional.",
        "",
        "| Paragraph | Topic | Role | Confidence | Explanation |",
        "| ---: | --- | --- | ---: | --- |",
    ]
    for assessment in result["assessments"]:
        explanation = assessment["explanation"].replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {assessment['paragraph_index']} | {assessment['topic']} | {assessment['role']} | {assessment.get('confidence', 'not supplied')} | {explanation} |"
        )
    return "\n".join(lines) + "\n"


def select_paragraph_window(
    paragraphs: list[dict[str, Any]],
    start_paragraph: int | None,
    end_paragraph: int | None,
) -> list[dict[str, Any]]:
    if start_paragraph is None and end_paragraph is None:
        return paragraphs
    start = start_paragraph if start_paragraph is not None else paragraphs[0]["paragraph_index"]
    end = end_paragraph if end_paragraph is not None else paragraphs[-1]["paragraph_index"]
    selected = [item for item in paragraphs if start <= item["paragraph_index"] <= end]
    if not selected:
        raise ValueError("requested paragraph window is empty")
    return selected


def _parse_response(content: str, paragraphs: list[dict[str, Any]]) -> dict[str, Any]:
    content = content.strip()
    if content.startswith("```"):
        content = content.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    payload = json.loads(content)
    units = None
    if isinstance(payload, dict):
        units = payload.get("units") or payload.get("discussion_units")
    if not isinstance(units, list) or not units:
        raise ValueError("response must contain a non-empty units array")
    valid_indices = [item["paragraph_index"] for item in paragraphs]
    first_allowed = valid_indices[0]
    last_allowed = valid_indices[-1]
    units = [
        unit
        for unit in units
        if int(unit.get("end_paragraph", first_allowed - 1)) >= first_allowed
        and int(unit.get("start_paragraph", last_allowed + 1)) <= last_allowed
    ]
    if not units:
        raise ValueError("response contains no units within the requested paragraph window")
    expected_position = 0
    normalized: list[dict[str, Any]] = []
    for position, unit in enumerate(units, 1):
        start = int(unit["start_paragraph"])
        end = int(unit["end_paragraph"])
        if start != valid_indices[expected_position] or end not in valid_indices:
            raise ValueError(f"unit {position} does not provide contiguous paragraph coverage")
        try:
            end_position = valid_indices.index(end, expected_position)
        except ValueError as exc:
            raise ValueError(f"unit {position} ends outside the remaining paragraph sequence") from exc
        normalized.append(
            {
                "unit_number": position,
                "start_paragraph": start,
                "end_paragraph": end,
                "label": str(unit.get("label") or "Unlabelled discussion"),
                "explanation": str(unit.get("explanation") or "No explanation supplied."),
                "transition_from_previous": str(unit.get("transition_from_previous") or "start"),
                "confidence": unit.get("confidence"),
            }
        )
        expected_position = end_position + 1
    if expected_position != len(valid_indices):
        raise ValueError("response does not cover every paragraph exactly once")
    return {"units": normalized}


def render_markdown(
    report: dict[str, Any],
    result: dict[str, Any],
    *,
    model: str,
    usage: dict[str, Any] | None = None,
) -> str:
    usage = usage or {}
    prompt_tokens = usage.get("prompt_tokens", "not available")
    completion_tokens = usage.get("completion_tokens", "not available")
    total_tokens = usage.get("total_tokens", "not available")
    estimated_cost = usage.get("estimated_cost_usd", "not available")
    lines = [
        f"# Plain-language Discussion Units: case {report['case_id']}",
        "",
        f"Model: `{model}`",
        f"Prompt tokens: `{prompt_tokens}`",
        f"Completion tokens: `{completion_tokens}`",
        f"Total tokens: `{total_tokens}`",
        f"Estimated billing (USD): `${estimated_cost}`",
        "",
        "This is a provisional, read-only interpretation; source paragraphs remain authoritative.",
        "",
    ]
    for unit in result["units"]:
        lines.extend(
            [
                f"## Paragraphs {unit['start_paragraph']}-{unit['end_paragraph']}: {unit['label']}",
                "",
                unit["explanation"],
                "",
                f"- Transition: {unit['transition_from_previous']}",
                f"- Confidence: {unit.get('confidence', 'not supplied')}",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-json", type=Path, required=True)
    parser.add_argument("--output-request", type=Path, required=True)
    parser.add_argument("--output-markdown", type=Path, required=True)
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--budget-usd", type=float, default=1.0)
    parser.add_argument("--send", action="store_true", help="Call the model; otherwise prepare only")
    parser.add_argument("--response-file", type=Path, help="Replay a saved model JSON response without network access")
    parser.add_argument("--ledger-path", type=Path, help="Durable per-case run ledger")
    parser.add_argument("--retry-failed", action="store_true", help="Retry a previously failed ledger row")
    parser.add_argument("--text-only", action="store_true", help="Send only paragraph indices and source text")
    parser.add_argument("--paragraph-level", action="store_true", help="Assess every paragraph separately instead of grouping spans")
    parser.add_argument("--start-paragraph", type=int)
    parser.add_argument("--end-paragraph", type=int)
    args = parser.parse_args()
    if args.budget_usd <= 0 or args.budget_usd > MAX_BUDGET_USD:
        parser.error(f"--budget-usd must be between 0 and {MAX_BUDGET_USD}")
    report = json.loads(args.input_json.read_text(encoding="utf-8"))
    if args.ledger_path and should_skip(args.ledger_path, int(report["case_id"]), retry_failed=args.retry_failed):
        print(json.dumps({"status": "skipped", "case_id": report["case_id"]}))
        return 0
    if args.ledger_path:
        record_case(
            args.ledger_path,
            int(report["case_id"]),
            "started",
            input_json=str(args.input_json),
            output_request=str(args.output_request),
            output_markdown=str(args.output_markdown),
            network_requested=bool(args.send),
        )
    model_paragraphs = select_paragraph_window(
        _legal_paragraphs(report.get("paragraphs", [])),
        args.start_paragraph,
        args.end_paragraph,
    )
    result_key = "assessments" if args.paragraph_level else "units"
    report_for_request = {**report, "paragraphs": model_paragraphs}
    request = (
        build_paragraph_assessment_request(
            report_for_request,
            model_paragraphs,
            model=args.model,
            budget_usd=args.budget_usd,
        )
        if args.paragraph_level
        else build_request(
            report_for_request,
            model=args.model,
            budget_usd=args.budget_usd,
            text_only=args.text_only,
        )
    )
    args.output_request.parent.mkdir(parents=True, exist_ok=True)
    args.output_request.write_text(json.dumps(request, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    if args.response_file:
        try:
            result = (
                _parse_paragraph_assessment(args.response_file.read_text(encoding="utf-8"), model_paragraphs)
                if args.paragraph_level
                else _parse_response(args.response_file.read_text(encoding="utf-8"), model_paragraphs)
            )
        except (IndexError, TypeError, ValueError, json.JSONDecodeError) as exc:
            if args.ledger_path:
                record_case(args.ledger_path, int(report["case_id"]), "failed", error=str(exc), response_file=str(args.response_file))
            raise
        args.output_markdown.parent.mkdir(parents=True, exist_ok=True)
        args.output_markdown.write_text(
            render_paragraph_assessment_markdown(report, result, model=args.model)
            if args.paragraph_level
            else render_markdown(report, result, model=args.model),
            encoding="utf-8",
        )
        if args.ledger_path:
            record_case(args.ledger_path, int(report["case_id"]), "complete", mode="replayed", unit_count=len(result[result_key]))
        print(json.dumps({"status": "replayed", "case_id": report["case_id"], "unit_count": len(result[result_key])}))
        return 0
    if not args.send:
        print(json.dumps({"status": "prepared", "case_id": report["case_id"], "paragraph_count": len(report["paragraphs"])}))
        return 0
    try:
        os.environ.pop("OPENAI_ORG_ID", None)
        os.environ.pop("OPENAI_ORGANIZATION", None)
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            timeout=180.0,
            max_retries=0,
        )
        response = client.chat.completions.create(
            model=args.model,
            temperature=0,
            max_tokens=6000,
            response_format={"type": "json_object"},
            messages=request["messages"],
        )
    except Exception as exc:
        if args.ledger_path:
            record_case(args.ledger_path, int(report["case_id"]), "failed", error=str(exc))
        raise
    content = response.choices[0].message.content or "{}"
    try:
        result = _parse_paragraph_assessment(content, model_paragraphs) if args.paragraph_level else _parse_response(content, model_paragraphs)
    except (IndexError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raw_path = args.output_markdown.with_suffix(".raw_response.txt")
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        usage = {
            "prompt_tokens": int(getattr(response.usage, "prompt_tokens", 0) or 0),
            "completion_tokens": int(getattr(response.usage, "completion_tokens", 0) or 0),
            "total_tokens": int(getattr(response.usage, "total_tokens", 0) or 0),
            "estimated_cost_usd": (
                (int(getattr(response.usage, "prompt_tokens", 0) or 0) * 0.10 / 1_000_000)
                + (int(getattr(response.usage, "completion_tokens", 0) or 0) * 0.40 / 1_000_000)
            ),
        }
        raw_path.write_text(
            (
                render_paragraph_assessment_markdown(report, {"assessments": []}, model=args.model, usage=usage)
                if args.paragraph_level
                else render_markdown(report, {"units": []}, model=args.model, usage=usage)
            )
            + "\n--- Raw model response ---\n"
            + content,
            encoding="utf-8",
        )
        if args.ledger_path:
            record_case(
                args.ledger_path,
                int(report["case_id"]),
                "failed",
                error=str(exc),
                raw_response=str(raw_path),
                usage=usage,
                spent_usd=usage["estimated_cost_usd"],
            )
        raise ValueError(f"model response rejected: {exc}; raw response saved to {raw_path}") from exc
    output = {
        "status": "complete",
        "network_called": True,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model,
        "case_id": report["case_id"],
        "source_report": str(args.input_json),
        "usage": {
            "prompt_tokens": int(getattr(response.usage, "prompt_tokens", 0) or 0),
            "completion_tokens": int(getattr(response.usage, "completion_tokens", 0) or 0),
            "total_tokens": int(getattr(response.usage, "total_tokens", 0) or 0),
            "estimated_cost_usd": (
                (int(getattr(response.usage, "prompt_tokens", 0) or 0) * 0.10 / 1_000_000)
                + (int(getattr(response.usage, "completion_tokens", 0) or 0) * 0.40 / 1_000_000)
            ),
        },
        "result": result,
    }
    args.output_markdown.parent.mkdir(parents=True, exist_ok=True)
    args.output_markdown.write_text(
        render_paragraph_assessment_markdown(report, result, model=args.model, usage=output["usage"])
        if args.paragraph_level
        else render_markdown(report, result, model=args.model, usage=output["usage"]),
        encoding="utf-8",
    )
    args.output_request.write_text(json.dumps({"request": request, "response": output}, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    if args.ledger_path:
        record_case(
            args.ledger_path,
            int(report["case_id"]),
            "complete",
            mode="network",
            unit_count=len(result[result_key]),
            spent_usd=output["usage"]["estimated_cost_usd"],
            usage=output["usage"],
        )
    print(json.dumps({"status": "complete", "case_id": report["case_id"], "unit_count": len(result[result_key])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())