# Strengthen worker evidence for bounded analytics

## Observed issue

The first delegated issue #155 implementation claimed bounded database access
and log-odds scoring, but the returned code still loaded tag candidates with an
N+1 query and ranked raw count ratios. Its initial tests mostly inspected
function signatures or a duplicated arithmetic example rather than exercising
the pure analysis function. A follow-up worker reported the N+1 path as fixed,
while the code still retained it; manager review found and corrected these gaps.
The ordinary pytest command also loaded the root conftest, whose import-time
fixture attempts a PostgreSQL `SELECT 1` probe.

## Evidence

- `.github/project-manager/tasks/issue-155-language-analytics.md`
- `backend/language_analytics.py` before manager recovery: per-case issue loads
  followed an unbounded case query, and scoring ignored group denominators.
- Final `tests/test_language_analytics.py`: fixture-level phrase scoring,
  group counts, cap/filter behavior, and compiled bounded-query checks.

## Proposed change

For analytics work delegated to a managed worker, require at least one behavioral
fixture test for the exact pure-analysis contract and an offline query-shape
check for any claimed row cap. The manager should verify claimed fixes against
the returned files before accepting the structured report; a summary of claims
alone is not evidence.
For work that forbids database access or `.env` loading, run fixture-only pytest
with `--confcutdir` beyond the repository conftest and set
`PYTHON_DOTENV_DISABLED=1`; confirm that the repo-wide conftest does not enter
the test process.

## Expected value and risk

This lowers the chance that tests validate descriptions rather than behavior,
catches mismatches between delegated reports and actual code, and avoids an
unintended database probe in fixture-only work. The added review/test effort is
small; risk is unnecessary query-compile tests for simple helpers, so apply
query checks only when query bounds are an acceptance criterion.

## Decision

Deferred for prompt/workflow consideration. No agent instructions were changed
as a side effect of this task.
