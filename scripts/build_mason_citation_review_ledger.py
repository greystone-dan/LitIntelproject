from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _load_fixture(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _parse_raw_labels(raw_response: str) -> tuple[list[dict[str, Any]], str | None]:
    try:
        payload = json.loads(raw_response)
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        return [], f"malformed_response: {exc}"
    labels = payload.get("labels") if isinstance(payload, dict) else None
    if not isinstance(labels, list):
        return [], "malformed_response: response has no labels array"
    return [label for label in labels if isinstance(label, dict)], None


def _error_by_label_index(errors: list[str]) -> dict[int, str]:
    mapped: dict[int, str] = {}
    for error in errors:
        prefix, separator, detail = error.partition(": ")
        if not separator or not prefix.startswith("label "):
            continue
        try:
            mapped[int(prefix.removeprefix("label "))] = detail
        except ValueError:
            continue
    return mapped


def build_ledger(fixture_path: Path, result_path: Path) -> dict[str, Any]:
    fixture = _load_fixture(fixture_path)
    by_id = {str(row["example_id"]): row for row in fixture}
    outcomes: dict[str, dict[str, Any]] = {}
    batches = json.loads(result_path.read_text(encoding="utf-8")).get("results", [])

    for batch in batches:
        raw_labels, batch_error = _parse_raw_labels(batch.get("raw_response", ""))
        valid_labels = {str(label["example_id"]): label for label in batch.get("labels", [])}
        errors = _error_by_label_index(batch.get("validation", {}).get("invalid_labels", []))
        for index, label in enumerate(raw_labels):
            example_id = str(label.get("example_id") or "")
            if example_id not in by_id:
                continue
            if example_id in valid_labels:
                continue
            outcomes[example_id] = {
                "status": "ai_label_rejected",
                "reason": errors.get(index, "label did not pass validation"),
                "raw_label": label,
                "batch_number": batch.get("batch_number"),
            }
        for example_id, label in valid_labels.items():
            outcomes[example_id] = {
                "status": "ai_label_accepted",
                "label": label,
                "batch_number": batch.get("batch_number"),
            }
        if batch_error:
            for example in fixture[
                int(batch.get("example_start", 0)) : int(batch.get("example_start", 0))
                + int(batch.get("example_count", 0))
            ]:
                example_id = str(example["example_id"])
                if example_id not in outcomes:
                    outcomes[example_id] = {
                        "status": "malformed_response",
                        "reason": batch_error,
                        "batch_number": batch.get("batch_number"),
                    }

    rows: list[dict[str, Any]] = []
    for example in fixture:
        example_id = str(example["example_id"])
        outcome = outcomes.get(
            example_id,
            {
                "status": "ai_label_omitted",
                "reason": "No label for this example was present in the saved response.",
            },
        )
        citation = example["citations"][0]
        rows.append(
            {
                "example_id": example_id,
                "citation": citation,
                "source_text": example["text"],
                "metadata": example.get("metadata", {}),
                "review_status": "needs_human_review",
                **outcome,
            }
        )
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    return {
        "artifact": "mason_citation_event_review_ledger",
        "fixture_source": str(fixture_path),
        "result_source": str(result_path),
        "example_count": len(rows),
        "coverage_complete": len(rows) == len(fixture),
        "status_counts": counts,
        "rows": rows,
    }


def render_markdown(ledger: dict[str, Any]) -> str:
    lines = [
        "# Mason Citation Event Review Ledger",
        "",
        "> Every deterministic citation event is included. AI labels are provisional and require human review.",
        "",
        f"- Events: **{ledger['example_count']}**",
        f"- Coverage complete: **{ledger['coverage_complete']}**",
        f"- Status counts: `{json.dumps(ledger['status_counts'], sort_keys=True)}`",
        "",
        "## Status meanings",
        "",
        "- `ai_label_accepted`: the returned label passed source-span validation.",
        "- `ai_label_rejected`: the AI returned a label, but validation rejected it.",
        "- `malformed_response`: the batch response could not be parsed as JSON.",
        "- `ai_label_omitted`: no label was found for this event in the saved response.",
        "",
        "## Events",
        "",
    ]
    for row in ledger["rows"]:
        citation = row["citation"]
        lines.extend(
            [
                f"### {row['example_id']} | `{row['status']}`",
                "",
                f"- Citation: `{citation['citation_text']}`",
                f"- Paragraph: `{row.get('metadata', {}).get('paragraph', {}).get('start', '?')}`",
            ]
        )
        if row.get("reason"):
            lines.append(f"- AI/validation note: `{row['reason']}`")
        label = row.get("label") or row.get("raw_label")
        if label:
            lines.append(f"- Proposed treatment: `{label.get('treatment', 'unavailable')}`")
            if label.get("phrase"):
                lines.append(f"- Proposed phrase: `{label['phrase']}`")
            if label.get("rationale"):
                lines.append(f"- Rationale: {label['rationale']}")
        lines.extend(["", "```text", row["source_text"], "```", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a complete Mason citation-event review ledger.")
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--output-json", required=True, type=Path)
    parser.add_argument("--output-markdown", required=True, type=Path)
    args = parser.parse_args()
    ledger = build_ledger(args.fixture, args.result)
    args.output_json.write_text(json.dumps(ledger, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    args.output_markdown.write_text(render_markdown(ledger), encoding="utf-8")
    print(json.dumps({key: ledger[key] for key in ("example_count", "coverage_complete", "status_counts")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())