# Task: AI-assisted citation issue triage

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Send a bounded subset of proposed citation occurrences to an external AI
reviewer to flag likely extraction issues for human review, without treating AI
output as gold or modifying repository/database data.

Why now: The five-case candidate fixture is too large for efficient manual review
in one pass. AI can prioritize likely wrong kinds, spans, pinpoints, anchors,
and false positives while the user retains final adjudication.

Owner surface: new read-only triage script and separate AI suggestion report.

Dependencies: proposed five-case fixture, existing OpenAI audit conventions in
`scripts/verify_citation_extraction.py`, `OPENAI_API_KEY` environment variable.

Commit allowed: yes

Push allowed: yes

Risk boundary: External API receives only the bounded selected occurrence and
context excerpt, never full decisions or database credentials. AI output is
suggestion-only and must not alter `five_case_citation_gold_candidate.json`,
production rows, tests, or confirmed gold. No statutes/tagging work.

Smallest falsifiable check: Dry-run reports the selected subset, estimated
input/output tokens, and cost under the hard budget without making an API call.

Acceptance criteria:

- Deterministic subset selection with explicit limit and category filters.
- Hard budget cap and dry-run mode.
- Structured AI suggestions with issue type, confidence, rationale, and occurrence identity.
- Separate output file marked `ai_suggestion`, never confirmed gold.
- API call requires `OPENAI_API_KEY`; key is never printed or stored.
- No database writes and no mutation of the candidate fixture.

Evidence: Dry-run passed with 20 selected occurrences, approximately 3,699
input tokens, 400 output tokens, and estimated cost `$0.0005299`; no API call
or database write. API triage then completed using `gpt-4.1-nano` with the same
20-occurrence cap and wrote `data/eval/five_case_citation_ai_triage_suggestions.json`.
The report contains 5 suggestion flags, is marked `ai_suggestions_unconfirmed`,
has `database_writes=false` and `gold_fixture_modified=false`, and leaves the
candidate fixture separate. The first API response was non-strict JSON and was
discarded; the parser was hardened and the one bounded retry succeeded. No key
was printed or stored. User edits currently make the candidate fixture dirty;
those edits were preserved and not overwritten.

## Hypothesis

A small capped AI triage pass will reduce human review effort by surfacing the
highest-risk proposed occurrences while preserving human control over labels.

## Cost Envelope

Default model follows `OPENAI_AUDIT_MODEL` (currently the repository convention
is `gpt-4.1-nano`). Default cap is `$0.10`, 20 occurrences, 1,200 context chars
per occurrence, and 400 output tokens per batch. At the existing configured
rates (`$0.10/M` input, `$0.40/M` output), a typical pass should cost well under
one cent; the cap remains the enforcement boundary.

## Completion

Status: complete

Summary: Added and ran a bounded AI triage pass that prioritizes likely issues
for human review without labeling gold or modifying source/candidate data.

Validation: Dry-run cost/scope check passed; successful API report validated as
suggestion-only; script compile check and `git diff --check` passed.

Residual risk: External model suggestions may be wrong, incomplete, or biased;
all five flags require human confirmation. The API does not prove pinpoint
correctness; it only prioritizes review.

Next recommended task: Review the five flagged occurrences, then either annotate
them in the candidate fixture or run another small triage batch with a different
category filter. Preserve the user's existing inline comments.
