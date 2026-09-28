# Task: Prepare FC Activity package for Claude

Status: complete
Created: 2026-09-26
Updated: 2026-09-26

## Task Record

Task: Create a read-only, provenance-preserving export package that Claude can use to design and evaluate FC Activity data transformation.

Why now: The Activity inventory is large and currently distributed across database tables, raw payloads, deterministic classifications, evaluation artifacts, and collector logs. Claude needs a bounded, reproducible package rather than unrestricted database access.

Owner surface: scripts/export_fc_activity_package.py and its focused tests

Commit allowed: yes

Push allowed: yes

Dependencies: PostgreSQL Activity tables, existing deterministic classifier output, current evaluation artifacts

Risk boundary: No database writes, no canonical case writes, no network collection, no secrets, no fabricated legal conclusions, and raw Activity records remain separate from derived events.

Smallest falsifiable check: python scripts/export_fc_activity_package.py --help followed by a bounded --limit 3 export and manifest inspection.

Acceptance criteria:

- Export raw Activity case metadata, raw procedural documents, and deterministic classification as separate JSONL layers.
- Write a manifest with counts, classifier versions, source/provenance fields, omission notes, and schema descriptions.
- Support bounded export and full export without mutating PostgreSQL.
- Focused tests verify layer separation, evidence references, bounded limits, and manifest generation.
- Update canonical documentation and the relevant Swimm walkthrough.

Docs/generated references: SYSTEM_REFERENCE.md, docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md, .swm/fc-ingest-source-pipeline.sw.md

Rollback/recovery: Delete only the generated output directory; the exporter is read-only and leaves database state unchanged.

Evidence: Explore inspected the classifier, ORM, ingestion, and existing JSONL conventions and recommended stable ID joins with raw/derived layers. Focused tests passed: `pytest tests/test_export_fc_activity_package.py -q` (`2 passed`); `py_compile` passed; `get_errors` reported no errors; `git diff --check` passed with existing CRLF normalization warnings. Real database smoke export passed at `data/copilot_exports/fc_activity_claude_smoke_20260926` with 3 cases, 58 documents, 3 classifications, and classifier version `fc_activity_v3`. The complete export passed at `data/copilot_exports/fc_activity_claude_20260926` with 316,940 cases, 3,587,801 documents, 218,639 classifications, 315,850 cases with documents, and 1,090 cases without documents; package size is approximately 5.8 GB. `README.md` and `CLAUDE_BRIEFING.md` were added to the handoff. The canonical setup document `docs/CLAUDE_ACTIVITY_PROJECT_SETUP.md` and its `DOCS_INDEX.md` entry were added. Canonical Activity documentation remains in `SYSTEM_REFERENCE.md` and `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; Swimm walkthrough remains `.swm/fc-ingest-source-pipeline.sw.md`.

## Hypothesis

If the exporter reads each Activity table independently and emits stable identifiers linking derived rows back to source case/document rows, a bounded package inspection will show raw evidence and derived classification can be consumed separately without database access.

## Plan

1. Inspect existing Activity payload and classifier output contracts.
2. Implement a bounded read-only JSONL/manifest exporter.
3. Run focused tests and a three-case package smoke test.
4. Update canonical documentation and Swimm guidance with the package contract.

## Execution Checkpoints

- Delegation: Explore completed bounded Activity export contract inspection; no files changed.
- Implementation: `scripts/export_fc_activity_package.py` and `tests/test_export_fc_activity_package.py`; focused check passed.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`, and `.swm/fc-ingest-source-pipeline.sw.md` updated.
- Recovery: Generated package directory only; no long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-26 | Use layered JSONL plus manifest as first Claude handoff | Streams large enough for 316k cases and 3.5m documents while preserving raw/derived separation and avoiding a new dependency | Current Activity schema and runbook |

## Completion

Completion recorded: yes

Summary: Created the read-only layered JSONL and manifest exporter for Claude handoff, validated its contract, and documented source/derived boundaries.

Validation: Focused unit tests, Python compilation, diagnostics, diff check, and a real three-case database export all passed.

Residual risk: Classification coverage and semantic accuracy still require evaluation; this package does not make legal findings or infer missing procedural events. Full export requires an operator disk-space review.

Next recommended task: Add authenticated API or MCP access after the package contract is reviewed with Claude.
