# Discussion Unit core 300 preflight

Status: in_progress
Created: 2026-09-24
Updated: 2026-09-24

Task: Prepare the 300-case core Discussion Unit manifest and requests, then execute exactly the first 10 hybrid API cases for validation. Stop before the remaining 290 API calls pending explicit user approval.

Why now: The resumable runner is hardened; this bounded preflight verifies deterministic reports, request preparation, ledger behavior, visual Markdown output, and API response handling before scaling.

Owner surface: `scripts/prepare_discussion_units_cohort.py`, the resumable cohort runner, and the dedicated run artifact directory.

Dependencies: core 300 CSV, local database `CaseChunk` paragraph data, `OPENAI_API_KEY` for the explicitly approved first 10 calls, and the existing `gpt-4.1-nano` hybrid request contract.

Risk boundary: Preparation for all 300 is read-only and no-network. Network execution is limited to the first 10 cases with a bounded per-case budget. Do not run the remaining 290 without a new user approval. No canonical database writes or model-output publication.

Smallest falsifiable check: The manifest has 300 unique cases with existing input/request/Markdown paths; the first 10 complete or fail with ledger/raw-response evidence; a second invocation skips terminal cases.

Acceptance criteria: one dedicated run directory; deterministic reports and Markdown for 300; prepared request payloads for 300; manifest and ledger; exactly 10 network attempts maximum; visual outputs retained; status/cost/error summary recorded; database-layer persistence deferred as a separate next task.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, `docs/NEXT_STEPS.md`, and this task record.

Rollback/recovery: Delete only the dedicated run directory and ledger; no database rollback is needed. Resume by rerunning the same manifest with the same ledger.

Commit allowed: yes

Push allowed: yes

Evidence: Preparation completed for all 300 core cases in
`data/eval/llm_discussion_units_pilot/core_300_run`: 300 deterministic input
reports and 300 request payloads were created, with a manifest and empty
ledger initialized. The approved first-10 API validation selected exactly 10
rows and completed 9 cases (`62`, `126`, `356`, `853`, `1046`, `1147`, `1292`,
`1439`, `1540`); case `677` failed and retained one raw response artifact.
Nine hybrid Markdown reviews and nine request/result JSON responses were
written. No cases after the first 10 were attempted. The output-directory
regression tests passed (`8 passed`). The remaining 290 API calls and database
persistence layer are deferred pending explicit approval and a separate
design task.

The next approved 10-case slice (`1748`, `1866`, `1901`, `1978`, `2044`,
`2220`, `2517`, `2660`, `2788`, `2828`) ran after the billing-header change:
8 cases completed and 2 were rejected for incomplete paragraph coverage. Their
artifacts record prompt/completion/total tokens and estimated billing at the
top of each Markdown or raw-response text file. The slice cost was
`$0.0076567` total, or `$0.0009570875` per completed case; the two failed API
responses also incurred recorded costs. The durable ledger now retains the
full usage object for subsequent cost reporting.

Status: in_progress
