# Task: Extract recurring unknown FC Activity motion patterns

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Produce a bounded, evidence-linked phrase-frequency report for unknown motion subtypes in the 1,000-record FC Activity artifact and define a reviewed fixture/gold-set candidate matrix.

Why now: Corpus measurement found 700 unknown motion subtypes. Before changing rules, the recurring source language and document-linkage opportunities must be independently measured.

Owner surface: FC Activity evaluation artifacts and review tooling

Commit allowed: yes

Push allowed: yes

Dependencies: `data/eval/fc_activity_motion_patterns_20260928.json`, `scripts/classify_fc_activity.py`, existing motion taxonomy tests, Beta comparison report, and FC ingestion Swimm walkthrough.

Risk boundary: Read-only artifact analysis and review-only output. Do not infer subtype labels from weak context, mutate classifier rules, write databases, call APIs, or promote OpenAI suggestions.

Smallest falsifiable check: A deterministic report generated from the existing artifact must show stable counts for unknown motion events grouped by explicit phrase families and preserve case/document IDs and bounded evidence text.

Acceptance criteria:

- A reproducible report groups unknown motion events into conservative phrase families, preserving unknown when no family is safe.
- The report includes event type, outcome, activity case ID, document ID, source date, and bounded source evidence for review candidates.
- A 20-30 candidate fixture/gold-set matrix is documented with explicit/inferred/unknown status and no automatic classifier changes.
- Canonical report and Swimm walkthrough record measured patterns, evidence paths, and residual uncertainty.
- Focused analysis/tests and evidence gate pass.

Harness criteria: The unknown-motion report passes; the fixture/gold-set candidate matrix is documented without rule promotion; focused validation passes; canonical report and Swimm walkthrough record evidence.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; no generated references expected.

Rollback/recovery: Delete the new review artifact and revert the task commit; no database or canonical recovery is required.

Evidence: Managed run `fc-activity-motion-unknown-patterns-20260928-072952-1a9fa2a1` recorded the 700-event report, 30-row matrix, 63 focused tests, documentation checks, and generated-catalog repair. Measured families were `motion_record_reference` 441, `unresolved_motion` 242, `motion_order_without_subject` 12, and `hearing_motion_reference` 5. All candidate rows remain unknown and `rules_promoted=false`.

Files changed: `scripts/report_fc_activity_motion_unknowns.py`; `tests/test_report_fc_activity_motion_unknowns.py`; `docs/SCRIPT_CATALOG.generated.md` (regenerated); `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; this task record. Artifact: `data/eval/fc_activity_motion_unknowns_20260928.json`.
Delegated work: Explore performed a bounded read-only pattern inventory; no files changed. Manager will independently verify the suggested phrase families.
Focused validation: `python -m pytest tests/test_report_fc_activity_motion_unknowns.py tests/test_evaluate_fc_activity_deterministic.py tests/test_audit_fc_activity_openai.py tests/test_classify_fc_activity.py -q` passed 63 tests; report generation passed; `git diff --check` and generated-doc validation passed after catalog regeneration.
Residual risk: Phrase families are triage labels, not legal or procedural truth; cross-document linkage and inferred subtype require human review. No classifier rule was changed.
Next bounded task: Build fixtures only from reviewed evidence IDs and explicit source text.

## Hypothesis

If unknown motion events are grouped only by explicit source-language markers, the resulting report will reveal recurring recoverable patterns while leaving ambiguous records visibly unknown.

## Plan

1. Add a pure phrase-family aggregation helper and focused tests.
2. Generate the bounded review artifact from the fixed 1,000-record report.
3. Document a 20-30 case fixture/gold-set candidate matrix and validate the evidence gate.

## Execution Checkpoints

- Delegation: Explore, bounded read-only inventory; structured return recorded in session.
- Implementation: Pending phrase-family aggregation and tests.
- Documentation: Pending canonical report and Swimm walkthrough updates.
- Recovery: Artifact under `data/eval/`; managed logs under `.github/project-manager/runs/`.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | Unknown subtype majority requires measured phrase evidence before classifier changes. | 1,000-record report; delegated inventory |

## Completion

Completion recorded: yes

Summary: Added a conservative evidence-linked unknown-motion report and 30-row review matrix without subtype inference or rule promotion.

Validation: Managed criteria 0, 1, 2, and 3 passed; `scripts/evidence_gate.py` passed with 6 recorded commands.

Residual risk: The matrix identifies review candidates but does not establish subtype accuracy; linked-document review remains.

Next recommended task: Review the 30 candidate rows and promote only source-supported fixtures into a gold set.
