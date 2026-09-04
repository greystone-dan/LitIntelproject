# Task: Iterative citation extraction improvement loop

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Apply safe, evidence-backed case-citation extraction fixes, benchmark them
on increasing bounded samples, triage all emitted occurrences with suggestion-only
AI review, and iterate until gains flatten or evidence becomes ambiguous.

Why now: Human review of the full candidate is too large. AI triage identified
real extraction defects, but also produced noise. The loop must distinguish valid
case aliases such as Sosa from ordinary same-name mentions and preserve every
valid duplicate occurrence.

Owner surface: `backend/citations.py`, citation tests, bounded extraction/AI
triage reports, and this task documentation.

Dependencies: existing five-case candidate fixture, user inline comments,
AI triage script/report, citation tests, validated FC/FCA/SCC corpus.

Commit allowed: yes

Push allowed: yes

Risk boundary: Case-to-case citations only. Never suppress Sosa or other valid
aliases globally. Preserve duplicates. Do not touch statutes, tagging, metadata,
chunks, ORM schema, production citation rows, or confirmed gold labels. AI output
is advisory only. Preserve user edits in the candidate fixture.

Smallest falsifiable check: Focused fixtures prove each fix improves a confirmed
bad pattern while preserving valid Sosa/alias occurrences, exact spans, and
duplicate counts.

Acceptance criteria:

- Safe fixes are isolated and covered by focused tests.
- Iteration reports use increasing bounded samples and record occurrence, exact-span, kind, alias, and AI-flag metrics.
- AI triage processes all selected occurrences per iteration without an arbitrary flag-count cap; batching exists only for response-size safety.
- Each AI report remains suggestion-only and separate from candidate/gold data.
- At least three iterations run or a documented blocker/efficiency stop is reached.
- Full regression passes after the final code edit.
- User comments and candidate fixture remain uncommitted unless explicitly approved.

## Iteration Plan

1. Safe fixes: address confirmed malformed SCC party extraction and clearly invalid caption/header fragments; preserve valid Sosa references and ordinary-name ambiguity for review.
2. Sample 1: bounded 5-case extraction and AI triage.
3. Sample 2: bounded 20-case extraction and AI triage.
4. Sample 3: bounded 60-case extraction and AI triage.
5. Compare metrics, review repeated high-confidence flags, and stop when additional changes are not supported by evidence or cost.

## Cost Boundary

Use `OPENAI_AUDIT_MODEL` and configured audit rates. Each iteration has a hard
`OPENAI_AUDIT_BUDGET_USD` cap; default total loop budget is `$0.50` unless
explicitly increased. Prefer compact contexts and deterministic batch sizes.

## Evidence

Pending safe-fix review and iterative reports.

## Completion

Status: in-progress

Summary: Pending.

Validation: Pending.

Residual risk: AI suggestions can be wrong; user review remains authoritative.

Next recommended task: Pending.
