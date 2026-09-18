from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from typing import Any


def _load_fixture(path: Path) -> dict[str, dict[str, Any]]:
    examples: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                row = json.loads(line)
                examples[str(row["example_id"])] = row
    return examples


def _context_for_label(label: dict[str, Any], fixture: dict[str, dict[str, Any]]) -> dict[str, Any]:
    example = fixture.get(str(label["example_id"]))
    if example is None:
        raise ValueError(f"fixture is missing {label['example_id']}")
    text = str(example["text"])
    phrase_start = int(label["phrase_start"])
    phrase_end = int(label["phrase_end"])
    citation = example["citations"][int(label["citation_ordinal"])]
    citation_start = int(citation["start_offset"])
    citation_end = int(citation["end_offset"])
    anchor_start = min(phrase_start, citation_start)
    anchor_end = max(phrase_end, citation_end)
    start = max(0, anchor_start - 600)
    end = min(len(text), anchor_end + 1_200)
    return {
        "citation_text": citation["citation_text"],
        "citation_context_start": start,
        "citation_context_end": end,
        "decision_context": text[start:end],
        "citation_offset_in_context": [citation_start - start, citation_end - start],
        "treatment_offset_in_context": [phrase_start - start, phrase_end - start],
    }


def build_packet(source_path: Path, *, packet_id: str, fixture_path: Path) -> dict[str, Any]:
    source = json.loads(source_path.read_text(encoding="utf-8"))
    fixture = _load_fixture(fixture_path)
    rules = source.get("rules", [])
    eligible_labels = source.get("eligible_labels", [])
    priority_labels = [
        {
            **label,
            **_context_for_label(label, fixture),
            "review_status": "pending_review",
            "review_decision": None,
            "review_notes": "",
        }
        for label in eligible_labels
        if label.get("treatment") != "supportive" or label.get("offsets_repaired", False)
    ]
    compact_rules: list[dict[str, Any]] = []
    repaired_rule_count = 0
    single_evidence_rule_count = 0
    for rule in rules:
        evidence = rule.get("evidence", [])
        repaired = any(item.get("offsets_repaired", False) for item in evidence)
        repaired_rule_count += int(repaired)
        single_evidence_rule_count += int(len(evidence) == 1)
        compact_evidence = [{**item, **_context_for_label(item, fixture)} for item in evidence]
        compact_rules.append(
            {
                "rule_id": rule["rule_id"],
                "treatment": rule["treatment"],
                "phrase": rule["phrase"],
                "support_count": rule["support_count"],
                "mean_confidence": rule["mean_confidence"],
                "span_quality": "repaired" if repaired else "original",
                "evidence": compact_evidence,
                "review_status": "pending_review",
                "review_decision": None,
                "review_notes": "",
            }
        )
    treatment_counts = Counter(rule["treatment"] for rule in compact_rules)
    packet = {
        "artifact": "treatment_distillation_review_packet",
        "packet_id": packet_id,
        "status": "human_review_required",
        "runtime_publishable": False,
        "artifact_source": str(source_path),
        "fixture_source": str(fixture_path),
        "review_instructions": [
            "Review the treatment against the full evidence text, not the citation alone.",
            "Use the decision context to check what the judge says before and after the citation.",
            "Confirm the phrase expresses treatment or judicial reasoning about the cited authority.",
            "Reject generic nouns, citation text, party-only assertions, or unsupported conclusions.",
            "Record approve, reject, or needs_context in review_decision and explain uncertainty in review_notes.",
        ],
        "review_summary": {
            "total_rules": len(compact_rules),
            "pending_review": len(compact_rules),
            "approved": 0,
            "rejected": 0,
            "needs_context": 0,
            "treatment_distribution": dict(treatment_counts),
            "rules_with_repaired_spans": repaired_rule_count,
            "rules_with_single_evidence": single_evidence_rule_count,
            "rules_with_multiple_evidence": len(compact_rules) - single_evidence_rule_count,
            "priority_label_count": len(priority_labels),
            "priority_treatment_distribution": dict(Counter(label["treatment"] for label in priority_labels)),
        },
        "rules": compact_rules,
        "priority_labels": priority_labels,
        "source_summary": source.get("summary", {}),
    }
    return packet


def render_markdown(packet: dict[str, Any]) -> str:
    priority_limit = 10
    summary = packet["review_summary"]
    lines = [
        f"# Treatment Distillation Review: {packet['packet_id']}",
        "",
        "> Status: **human review required**. This packet is provisional and cannot publish runtime behavior.",
        "",
        "## How To Review",
        "",
        "For each item, answer one question: **Does the evidence phrase correctly describe how the judge treats the cited authority?**",
        "",
        "- `supportive`: the judge relies on, agrees with, or applies the authority.",
        "- `distinguishing`: the judge says the authority is different, limited, or does not control.",
        "- `negative`: the judge rejects or criticizes the authority.",
        "- `neutral`: the authority is discussed without a clear positive or negative treatment.",
        "- `absent`: the citation appears, but there is no treatment of it in the evidence.",
        "- `ambiguous`: the wording is too unclear to decide.",
        "",
        "Reply with item IDs using `approve`, `reject`, or `unclear`, plus a short reason. Example: `citation-context-1018: reject - this is the court's merits reasoning, not treatment of the cited case.`",
        "",
    ]
    lines.extend(f"- {instruction}" for instruction in packet["review_instructions"])
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Rules: **{summary['total_rules']}** pending review",
            f"- Treatment distribution: `{json.dumps(summary['treatment_distribution'], sort_keys=True)}`",
            f"- Rules with repaired spans: **{summary['rules_with_repaired_spans']}**",
            f"- Rules with one evidence item: **{summary['rules_with_single_evidence']}**",
            f"- Priority labels requiring direct review: **{summary['priority_label_count']}**",
            f"- Priority treatment distribution: `{json.dumps(summary['priority_treatment_distribution'], sort_keys=True)}`",
            f"- Full source artifact: `{packet['artifact_source']}`",
            "",
            "## Review Queue",
            "",
        ]
    )
    if packet["priority_labels"]:
        lines.extend(["## Priority Labels: Start Here", "", f"Review these first {min(priority_limit, len(packet['priority_labels']))} items. The JSON packet contains all {len(packet['priority_labels'])} priority labels.", ""])
        for label in packet["priority_labels"][:priority_limit]:
            lines.extend(
                [
                    f"- `{label['example_id']}`; proposed **{label['treatment']}**; confidence **{label['confidence']:.2f}**; citation: `{label['citation_text']}`",
                    f"  - Proposed evidence: `{label['evidence_text']}`",
                    f"  - Decision context: `{label['decision_context']}`",
                    f"  - Offsets repaired: `{label['offsets_repaired']}`; source hash: `{label['source_text_sha256']}`",
                    "",
                ]
            )
    lines.extend(["## Remaining Review Material", "", "After the starting batch, continue with the remaining priority labels and then the repeated-rule queue below.", ""])
    lines.extend(["## Repeated-Rule Queue", ""])
    for index, rule in enumerate(packet["rules"], 1):
        lines.extend(
            [
                f"### {index}. `{rule['rule_id']}`",
                "",
                f"- Proposed treatment: **{rule['treatment']}**",
                f"- Support: **{rule['support_count']}** examples; mean confidence **{rule['mean_confidence']:.2f}**",
                f"- Span quality: **{rule['span_quality']}**",
                f"- Phrase: `{rule['phrase']}`",
                "",
                "Evidence:",
            ]
        )
        for evidence in rule["evidence"]:
            lines.extend(
                [
                    f"- `{evidence['example_id']}`; citation: `{evidence['citation_text']}`; hash: `{evidence['source_text_sha256']}`",
                    f"  - Proposed evidence: `{evidence['evidence_text']}`",
                    f"  - Decision context: `{evidence['decision_context']}`",
                    f"  - Offsets repaired: `{evidence['offsets_repaired']}`; confidence: `{evidence['confidence']:.2f}`",
                ]
            )
        lines.extend(
            [
                "",
                "Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a human-readable treatment review packet.")
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--output-json", required=True, type=Path)
    parser.add_argument("--output-markdown", required=True, type=Path)
    parser.add_argument("--packet-id", required=True)
    args = parser.parse_args()
    packet = build_packet(args.source, packet_id=args.packet_id, fixture_path=args.fixture)
    args.output_json.write_text(json.dumps(packet, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    args.output_markdown.write_text(render_markdown(packet), encoding="utf-8")
    print(json.dumps(packet["review_summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())