# Task: Legal authority extraction and evidence roadmap

Status: in-progress
Created: 2026-09-15
Updated: 2026-09-15

## Task Record

Task: Review the legal law/statute extraction system end to end and produce an evidence-backed plan for reliable law and provision identification, section-level highlighting, and links to authoritative text.

Why now: The desired research workflow needs more than regex extraction: each legal reference must resolve to a stable authority identity, preserve the cited section/provision, and expose source text for verification. IRPA/IRPR work exists but the full authority-bank and evidence model need review.

Owner surface: legal authority extraction, statute persistence/resolution, and reader evidence contract

Commit allowed: yes

Push allowed: yes

Dependencies: backend/statutes.py, backend/citations.py, backend/database.py, backend/models.py, backend/routes.py, backend/reader_service.py, scripts/ and tests for statute extraction, source/provenance policy, authoritative legal-text inventory

Risk boundary: Review and planning only in this task. Do not run extraction rebuilds, bulk writers, external acquisition, paid APIs, or production/security changes. Preserve case-law/statute separation and backend-owned offsets.

Smallest falsifiable check: Read-only inventory of statute extraction, persistence, resolution, API/reader projection, existing IRPA/IRPR fixtures, and live schema counts; identify one concrete contract gap that prevents section-level evidence links.

Acceptance criteria:

- Current law/statute extraction and IRPA/IRPR coverage are mapped with evidence.
- The authority identity, provision identity, source text, provenance, and reader-link contracts are evaluated separately.
- At least three viable architecture approaches are compared where applicable.
- A phased implementation plan has owners, acceptance checks, data/provenance boundaries, and explicit approval gates.
- Canonical documentation and the relevant Swimm walkthrough are updated with the review outcome.

Docs/generated references: SYSTEM_REFERENCE.md; ROADMAP.md; .swm/4.9nn3id9f.sw.md; docs/DATA_SOURCE_REGISTER.md; docs/TESTING_MATRIX.md

Rollback/recovery: Documentation-only review; revert the roadmap checkpoint without changing extraction, schema, or database rows.

Evidence: Delegated read-only inventory completed. It confirmed nested IRPA/IRPR extraction and exact-span coverage in `backend/citations.py`, opaque `StatuteReference.pinpoint` persistence, existing but unpopulated `LegislationDocument`/`LegislationSection` tables, and reader/API surfaces that expose references but cannot consistently resolve authoritative section text. No files or database rows were changed by the worker. Focused validation: `tests/test_citations.py -q -k "statute or IRPA or IRPR"` -> `25 passed, 118 deselected, 1 warning`; `git diff --check` passed.

## Hypothesis

If statute extraction, legal authority identity, provision parsing, source acquisition, and reader evidence are separate contracts, then the current gap will be found at the identity/source-resolution boundary rather than in IRPA/IRPR regex matching alone.

## Plan

1. Delegate a bounded read-only inventory of extraction, schema, routes, reader, tests, and source register.
2. Synthesize findings and compare viable authority-bank/evidence architectures.
3. Update canonical roadmap/reference and Swimm documentation with an approval-gated plan.
4. Run documentation and focused read-only validation.

## Execution Checkpoints

- Delegation: Explore completed the bounded statute/schema/API/source-register inventory; no files changed.
- Implementation: Review synthesis only; no code writer or source acquisition authorized.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `ROADMAP.md`, and `.swm/4.9nn3id9f.sw.md` with the authority-layer plan.
- Recovery: No database or external acquisition operation authorized.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-15 | Task created | User requested a whole-system review and plan for section-linked legal authority evidence | Authority docs read; scope restricted to review/planning pending inventory |

## Completion

Completion recorded: yes

Summary: Completed the system review and selected a phased legal authority evidence plan. The recommended first slice is structured provision identity and deterministic read-only resolution reporting, followed by a provenance-aware authority bank and reader section links.

Validation: Read-only source inventory completed; `git diff --check` passed. No extraction rebuild, database writer, external acquisition, paid API, or production operation ran.

Residual risk: Authority-bank population requires decisions about authoritative source selection, versioning, licensing/terms, update cadence, and potentially external acquisition. Exact section links must not be presented as authoritative until those contracts are approved and validated.

Next recommended task: Implement a bounded structured-provision identity slice for IRPA/IRPR with fixture-backed extraction and read-only resolution metrics, after approving the schema and source-authority boundary.
