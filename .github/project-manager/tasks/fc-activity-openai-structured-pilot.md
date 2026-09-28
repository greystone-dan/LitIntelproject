# Task: 100-case OpenAI structured FC Activity pilot

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Send one structured extraction request per case for 100 cases selected from the fixed 1,000-case IMM-15 evaluation sample, including deterministic fields, judge observations, and motion details.
Why now: The user wants to measure whether a small OpenAI model can fill the complete FC Activity table accurately and cheaply enough to replace or complement deterministic extraction.
Owner surface: New review-only OpenAI FC Activity extraction runner and bounded evaluation artifact.
Dependencies: `data/eval/fc_activity_imm_suffix_15_judge_analysis_20260928.json`, OpenAI credentials, existing FC Activity source schema, and current deterministic classifier for later comparison.
Risk boundary: Exactly 100 requests, one case per request, model `gpt-4.1-nano`, hard budget USD 1.00, no database writes, no automatic fact promotion, no secrets in artifacts, resumable checkpoint required.
Smallest falsifiable check: Dry-run validates the selected 100 cases, projected cost, request count, schema, and checkpoint path before `--send`.
Acceptance criteria:
- The input is the current fixed 1,000-case IMM-15 report and the selected 100 case IDs are recorded.
- Each request contains one IMM number and its associated raw activity rows.
- Each response is structured JSON with deterministic fields, judge observations, and motion objects with source evidence.
- The run records actual token usage, spend, failures, and `database_written=false`.
- The output is review-only; no deterministic or canonical values are changed.
- Focused tests, dry-run, and bounded API execution pass or record exact failures.
Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; pilot artifacts under `data/eval/`.
Rollback/recovery: Delete only pilot artifacts and checkpoint; do not modify Activity or canonical tables. Resume from checkpoint or rerun with a new output path.
Commit allowed: yes
Push allowed: yes
Evidence: The initial compact pilot completed 100/100 requests at `$0.0393408`, but its loose format omitted requested objects and is retained only as a prompt-format baseline. The repaired strict-schema smoke completed one case with all required top-level objects, an empty missing-field list, and the correct IMM. The strict 100-case rerun used the same seed and selection, completed 99 cases initially, then retried the one response truncated at the 1,400-token ceiling; the final artifact has 100/100 successful records, `database_written=false`, 246,581 total tokens, and `$0.0355742` spend. Strict model coverage was filing date 83/100, decision type 85/100, decision date 86/100, any judge 76/100, and motion-bearing cases 32/100, versus deterministic 100/100, 37/100, 46/100, 72/100, and 33/100 on the same sample. The strict output artifact is `data/eval/fc_activity_openai_structured_pilot_100_schema_20260928.json`; its checkpoint is `data/eval/fc_activity_openai_structured_pilot_100_schema_checkpoint_20260928.json`; the smoke artifacts use the corresponding `schema_smoke` names.
Files changed: `scripts/run_fc_activity_openai_structured_pilot.py`, this task record, and bounded pilot artifacts under `data/eval/`.
Delegated work: Explore completed a read-only review of existing OpenAI runners and checkpoint/cost patterns.
Focused validation: `py_compile` passed; strict dry-run planned one request at `$0.0006797`; the strict smoke completed with all required keys and no missing fields; the strict 100-case run completed after one retry, with zero final failures and `$0.0355742` spend. The comparison shows the strict schema fixed structural omissions, but the model still underfilled filing dates relative to deterministic extraction and its motion arrays contained 76 rows versus 332 deterministic motion events.
Residual risk: This remains a coverage comparison, not an accuracy benchmark. Model judge and motion entries may include false positives, stage and outcome values are not yet normalized against deterministic evidence, one response required a retry after output truncation, and source document IDs were retained without copied evidence text. No model fact was promoted.
Next bounded task: Review a stratified sample of strict-schema disagreements for precision and field-level agreement before considering a larger or production-adjacent run.
