# Task: Qwen3 paragraph summary baseline

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Generate a report-only baseline of 10 paragraph summaries using local Ollama `qwen3:4b`.

Why now: The local model is installed and callable; a small baseline is needed before designing persistent summary storage or broader enrichment.

Owner surface: bounded local summary evaluation under `data/eval/`

Commit allowed: yes

Push allowed: yes

Dependencies: Ollama `qwen3:4b`; canonical paragraph chunks; local provider; existing read-only evaluation patterns

Risk boundary: No database writes, no citation extraction/resolution changes, no canonical summary fields, no bulk case processing, and no hosted API calls.

Smallest falsifiable check: Ten paragraph inputs produce valid structured JSON with stable source paragraph IDs and non-empty summaries.

Acceptance criteria:

- Exactly 10 stored paragraphs are selected and recorded by case/chunk identity.
- Local `qwen3:4b` generates one summary per paragraph in a report-only artifact.
- Output parses as JSON and preserves source identifiers without inventing citation offsets.
- Runtime/model/error evidence is recorded.

Docs/generated references: SYSTEM_REFERENCE.md; docs/CONFIGURATION_REFERENCE.md; .swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md

Rollback/recovery: Delete only the new bounded evaluation artifact; no canonical or database rollback is needed.

Evidence: `scripts/run_local_paragraph_summary_baseline.py` ran 10 sequential local calls against Case 1093 paragraphs 0-9 and wrote `data/eval/qwen3_case_1093_paragraph_summary_baseline.json`. The artifact contains exactly 10 records and 10 source hashes with indices 0-9; 3 records are complete with non-empty summaries and 7 records explicitly failed structured-output validation. The raw failures show Qwen3 echoing the input payload (`case_id` and `paragraphs`) instead of returning `summaries`. Total elapsed time was 81.20 seconds, average 8.12 seconds per call, with 1,966 prompt tokens and 1,093 completion tokens. No database or canonical writes occurred.

## Hypothesis

If qwen3:4b is prompted for concise source-grounded JSON, each paragraph call will return parseable summaries within the local runtime limits. The baseline falsified the all-success expectation: 3/10 calls returned valid summaries.

## Plan

1. Identify a bounded real paragraph source and local output convention.
2. Run 10 sequential local calls with source IDs and prompt metadata.
3. Validate JSON coverage, non-empty summaries, and absence of canonical writes.

## Execution Checkpoints

- Delegation: Not used; this was a bounded manager-owned evaluation run.
- Implementation: Complete; added the report-only sequential runner with read-only CaseChunk reconstruction and hash checks.
- Validation: Complete; artifact coverage and provenance validation passed, with 7 explicit model-format failures retained.
- Documentation: Complete; updated SYSTEM_REFERENCE.md and the local-generation architecture walkthrough.

## Completion

Completion recorded: yes

Summary: Qwen3 is callable locally, but this prompt/model/limit combination produced only 3 valid paragraph summaries out of 10. Seven responses echoed the input payload rather than following the requested output schema. The report-only artifact preserves raw failures and per-paragraph timing for prompt/model tuning.

Validation: `venv\Scripts\python.exe -m py_compile scripts/run_local_paragraph_summary_baseline.py`; then the bounded baseline command with `--max-tokens 320`. Artifact inspection confirmed 10 records, exact indices 0-9, 10 source hashes, 3 non-empty successes, 7 explicit failures with raw responses, and timing for every call.

Residual risk: This baseline measures format and runtime, not legal-summary accuracy; human review remains required.

Next recommended task: Human-review the 10 summaries and define the provenance/schema gate for a larger pilot.
