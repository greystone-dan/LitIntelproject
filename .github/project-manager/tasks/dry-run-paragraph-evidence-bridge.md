# Task: Dry-run 300-case paragraph evidence bridge

Status: complete
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Produce a read-only mapping report that aligns paragraph assessment artifacts with canonical paragraph chunks, citations, and statute references for the 300-case cohort.

Why now: Establish match quality and ambiguity rates before any additive SQL linkage or schema change.

Owner surface: Read-only mapper under `scripts/` and its evidence report.

Commit allowed: yes

Push allowed: yes

Dependencies: PostgreSQL read access, the 300-case allowlist, report-only paragraph assessments, canonical paragraph chunks, citations, and statute references.

Risk boundary: No database writes, chunk rewrites, offset changes, migrations, or guessed mappings; preserve unmatched and ambiguous records.

Smallest falsifiable check: A bounded dry run over the 300-case allowlist reports exact, ambiguous, and unmatched paragraph mappings with source hashes and offset agreement.

Acceptance criteria:

- The dry run reads only the allowlisted 300 cases and does not mutate PostgreSQL or assessment artifacts.
- The report distinguishes exact, ambiguous, and unmatched assessment-to-paragraph mappings.
- Citation and statute assignments are derived from backend-owned offsets and remain separate evidence layers.
- Focused validation and artifact paths are recorded with known failures and residual risk.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`

Rollback/recovery: Delete the generated dry-run report and remove the mapper only if it is not retained; no database rollback is needed because the run is read-only.

Evidence: Explore inventory completed read-only. Focused mapper tests passed (`2 passed`). The 300-case read-only scan completed with 13,424 records: 11,657 exact, 798 ambiguous, and 969 missing assessment rows. Report: `data/eval/llm_discussion_units_pilot/paragraph_evidence_bridge_dry_run.json`. Evidence-layer check found 0 statute references attached to cohort paragraph chunks and 0 citations attached to those paragraph chunks, while 7,439 cohort citations had some chunk ID. Canonical documentation updated in `SYSTEM_REFERENCE.md`; Swimm walkthrough updated in `.swm/8.upryk5h6.sw.md`. On 2026-09-24, obsolete five-case, 20-case, single-case, and request-only paragraph pilots were removed; the active 300-case artifacts were preserved. `git diff --check` passed.

## Hypothesis

If canonical paragraph chunks preserve stable case-local paragraph numbers and offsets, then most assessment rows can be matched exactly while citation and statute evidence can be attached without rewriting existing records.

## Plan

1. Inspect the existing report loader, ORM models, cohort manifest, and nearby scripts.
2. Implement or adapt a bounded read-only mapper that emits match-quality evidence.
3. Run the mapper against the 300-case allowlist and validate that no writes occurred.
4. Update the canonical architecture document and relevant Swimm walkthrough with the measured result.

## Execution Checkpoints

- Delegation: Explore agent, bounded inventory of report/chunk/citation/statute paths and existing dry-run tooling; return the required structured result.
- Implementation: `scripts/dry_run_paragraph_evidence_bridge.py` and `tests/test_dry_run_paragraph_evidence_bridge.py`; focused tests passed.
- Documentation: `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` record the completed dry-run boundary and result.
- Recovery: Dry-run report is retained at `data/eval/llm_discussion_units_pilot/paragraph_evidence_bridge_dry_run.json`; no long-running writer was used.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-24 | Start with a read-only mapper | Mapping quality must be measured before additive persistence | Current architecture separates report files from SQL evidence layers |
| 2026-09-24 | Retain only 300-case assessment artifacts | Older paragraph pilots were superseded and no live route depends on them | Active `paragraph_level_300_run` and prepared `core_300_run` preserved |

## Completion

Completion recorded: yes

Summary: Completed the read-only 300-case paragraph assessment bridge scan. No SQL schema or canonical rows were changed.

Validation: `venv\\Scripts\\python.exe -m pytest tests/test_dry_run_paragraph_evidence_bridge.py -q` passed with 2 tests. `venv\\Scripts\\python.exe -m scripts.dry_run_paragraph_evidence_bridge --limit 300 --output data\\eval\\llm_discussion_units_pilot\\paragraph_evidence_bridge_dry_run.json` completed successfully. `git diff --check` passed.

Residual risk: Paragraph-number agreement does not prove text identity where reports are incomplete or source chunks differ. Citation/statute chunk-set reconciliation remains unresolved; no additive schema should be approved until that boundary is explained.

Next recommended task: Inspect why citation rows use non-paragraph chunk IDs and why the cohort has no statute rows before designing an additive staging schema.