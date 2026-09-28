"""Build a readable, source-backed audit report from an FC Activity package."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SUMMARY_FIELDS = (
    "application_filed",
    "application_perfected",
    "leave_decision",
    "hearing_status",
    "closing_status",
    "lifecycle_status",
)


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _status_value(value: Any) -> Any:
    if not isinstance(value, dict):
        return value
    return {key: value.get(key) for key in ("status", "date", "outcome", "judge_name", "rule") if value.get(key) is not None}


def _audit_gaps(classification: dict[str, Any]) -> list[str]:
    gaps: list[str] = []
    for field in SUMMARY_FIELDS:
        value = classification.get(field)
        if isinstance(value, dict) and value.get("status") in {None, "unknown"}:
            gaps.append(f"{field}: unknown")
        elif value is None:
            gaps.append(f"{field}: not emitted")
    if not classification.get("procedural_events"):
        gaps.append("procedural_events: no extracted events")
    return gaps


def _legacy_findings(classification: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for field, value in classification.items():
        if field in {"procedural_events", "challenged_decision", "history_profile"}:
            continue
        if not isinstance(value, dict) or value.get("status") not in {"yes", "active", "closed"}:
            continue
        if not any(value.get(key) is not None for key in ("text", "doc_id", "date", "rule")):
            continue
        findings.append(
            {
                "event_type": field,
                "subtype": None,
                "outcome": value.get("outcome") or value.get("result"),
                "event_date": value.get("date"),
                "date_kind": value.get("date_kind"),
                "judge_name": value.get("judge_name"),
                "doc_id": value.get("doc_id"),
                "rule": value.get("rule"),
                "text": value.get("text"),
                "source_recorded_entry": None,
            }
        )
    return findings


def build_report(package: Path) -> dict[str, Any]:
    manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
    cases = _load_jsonl(package / "cases.jsonl")
    documents = _load_jsonl(package / "documents.jsonl")
    classifications = _load_jsonl(package / "classifications.jsonl")
    documents_by_case: dict[int, list[dict[str, Any]]] = {}
    for document in documents:
        documents_by_case.setdefault(int(document["activity_case_id"]), []).append(document)
    classifications_by_case = {int(row["activity_case_id"]): row for row in classifications}

    report_cases: list[dict[str, Any]] = []
    for case in cases:
        case_id = int(case["activity_case_id"])
        classification_row = classifications_by_case.get(case_id, {})
        classification = classification_row.get("classification") or {}
        events = classification.get("procedural_events") or []
        source_by_id = {int(row["activity_document_id"]): row for row in documents_by_case.get(case_id, [])}
        findings = []
        for event in events:
            doc_id = event.get("doc_id")
            source = source_by_id.get(int(doc_id)) if doc_id is not None else None
            findings.append(
                {
                    "event_type": event.get("event_type"),
                    "subtype": event.get("subtype"),
                    "outcome": event.get("outcome"),
                    "event_date": event.get("event_date"),
                    "date_kind": event.get("date_kind"),
                    "judge_name": event.get("judge_name"),
                    "doc_id": doc_id,
                    "rule": event.get("rule"),
                    "text": event.get("text"),
                    "source_recorded_entry": source.get("recorded_entry") if source else None,
                }
            )
        if not findings:
            findings = _legacy_findings(classification)
        for finding in findings:
            if finding["source_recorded_entry"] is None and finding.get("doc_id") is not None:
                source = source_by_id.get(int(finding["doc_id"]))
                finding["source_recorded_entry"] = source.get("recorded_entry") if source else None
        report_cases.append(
            {
                "activity_case_id": case_id,
                "citation": case.get("citation"),
                "imm_number": case.get("imm_number"),
                "year": case.get("year"),
                "case_name": case.get("case_name"),
                "date_filed": case.get("date_filed"),
                "city_filed": case.get("city_filed"),
                "nature": case.get("nature"),
                "track": case.get("track"),
                "document_count": len(documents_by_case.get(case_id, [])),
                "classification_present": bool(classification_row),
                "classifier_version": classification_row.get("classifier_version"),
                "summary": {field: _status_value(classification.get(field)) for field in SUMMARY_FIELDS if field in classification},
                "findings": findings,
                "audit_gaps": _audit_gaps(classification),
            }
        )
    return {
        "report_version": "fc_activity_manual_audit_v1",
        "purpose": "Read-only manual audit of deterministic Federal Court Activity findings.",
        "manifest": manifest,
        "case_count": len(report_cases),
        "cases": report_cases,
        "limitations": manifest.get("known_limitations", []),
    }


def _md(value: Any) -> str:
    return str(value if value is not None else "unknown").replace("\n", " ").strip()


def render_markdown(report: dict[str, Any]) -> str:
    manifest = report["manifest"]
    lines = [
        "# Federal Court Activity: 10-Case Manual Audit",
        "> Read-only report. Derived findings are deterministic observations over Activity records, not canonical judgments or legal conclusions.",
        "",
        f"- Cases: {report['case_count']}",
        f"- Documents: {manifest.get('counts', {}).get('documents', 'unknown')}",
        f"- Classifications: {manifest.get('counts', {}).get('classifications', 'unknown')}",
        f"- Classifier version(s): {', '.join(manifest.get('classifier_versions', [])) or 'none'}",
        "",
        "## How To Audit",
        "For each finding, compare the extracted event with `source_recorded_entry`. Check the event date kind, outcome, judge, and rule. Treat entries under `Audit gaps` as review queues, not proof of missing procedural history.",
        "",
    ]
    for case in report["cases"]:
        lines.extend(
            [
                f"## {case['activity_case_id']}: {_md(case['case_name'])}",
                f"- Citation: {_md(case['citation'])}",
                f"- IMM: {_md(case['imm_number'])}",
                f"- Year / filed: {_md(case['year'])} / {_md(case['date_filed'])}",
                f"- Court location: {_md(case['city_filed'])}",
                f"- Nature: {_md(case['nature'])}",
                f"- Documents: {case['document_count']}",
                f"- Classification present: {case['classification_present']} ({_md(case['classifier_version'])})",
                "",
                "### Summary",
            ]
        )
        for field, value in case["summary"].items():
            lines.append(f"- `{field}`: `{json.dumps(value, ensure_ascii=False)}`")
        if not case["summary"]:
            lines.append("- No summary fields were persisted.")
        lines.extend(["", "### Findings", ""])
        if case["findings"]:
            for index, finding in enumerate(case["findings"], start=1):
                lines.extend(
                    [
                        f"#### {index}. {_md(finding['event_type'])} / {_md(finding['subtype'])}",
                        f"- Date: `{_md(finding['event_date'])}` ({_md(finding['date_kind'])})",
                        f"- Outcome: `{_md(finding['outcome'])}`; judge: `{_md(finding['judge_name'])}`",
                        f"- Source document: `{_md(finding['doc_id'])}`; rule: `{_md(finding['rule'])}`",
                        f"- Extracted text: {_md(finding['text'])}",
                        f"- Source entry: {_md(finding['source_recorded_entry'])}",
                        "",
                    ]
                )
        else:
            lines.append("No procedural events were extracted; inspect the package documents directly.")
            lines.append("")
        lines.append("### Audit gaps")
        if case["audit_gaps"]:
            lines.extend(f"- {gap}" for gap in case["audit_gaps"])
        else:
            lines.append("- No summary gap detected by this report; source review is still required.")
        lines.append("")
    lines.extend(["## Package Limitations", ""])
    lines.extend(f"- {item}" for item in report["limitations"])
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = build_report(args.package)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_markdown(report), encoding="utf-8")
    args.output.with_suffix(".json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"case_count": report["case_count"], "output": str(args.output), "json_output": str(args.output.with_suffix('.json'))}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())