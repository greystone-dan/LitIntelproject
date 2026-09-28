Task: Build a 10-case FC Activity audit report with summaries and source-backed findings.
Why now: The existing JSONL handoff preserves the layers but is cumbersome to inspect manually; a bounded readable report will make deterministic findings auditable.
Owner surface: Read-only FC Activity export and report presentation under `scripts/` and `data/copilot_exports/`.
Dependencies: Existing FC Activity source tables, persisted deterministic classifications, and the package exporter.
Risk boundary: Read-only database access; no canonical case, citation, statute, or Activity writes; report must preserve source evidence and distinguish derived findings from legal conclusions.
Smallest falsifiable check: Generate a package with exactly 10 Activity cases and a report whose case IDs, document counts, and classification joins match the manifest.
Acceptance criteria:
- Export exactly 10 real Activity case rows with linked documents and classifications where available.
- Present a concise summary and deterministic findings for each case.
- Include source document text and rule/evidence references for manual audit.
- Preserve explicit limitations and classifier version in the report.
- Run focused report tests and package/report generation checks.
Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.swm/fc-ingest-source-pipeline.sw.md`; generated package under `data/copilot_exports/`.
Rollback/recovery: Remove only the new report script, test, task record, documentation checkpoint, and generated 10-case package; do not alter source tables.
Evidence: Exported `data/copilot_exports/fc_activity_manual_audit_10_20260927/` with 10 cases, 83 documents, 7 classifications, 9 cases with documents, and 1 case without documents. Generated `audit_report.md` and `audit_report.json` with 27 evidence-linked findings across 7 classified cases and 47 explicit audit gaps. The report supports both persisted `fc_activity_v3` evidence fields and procedural-event arrays. Focused report tests passed 2; final Activity validation and `git diff --check` are recorded in the session.
Status: complete
Commit allowed: yes
Push allowed: yes