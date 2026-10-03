# Outcome Classifier Test Plan

Issue #45 reviews `deterministic_outcome_v2` without changing behavior. This report records the current decision categories, the new synthetic fixture coverage, and the wording gaps that remain xfailed on purpose.

## Current coverage

- Supported today: allowed, dismissed, granted, set aside, remitted, and partial relief.
- Also covered today: withdrawn/discontinued wording, with outcome status derived from the current rule set.
- Not yet modeled as distinct final dispositions: conditional orders, questions certified, and matters returned for redetermination.

## Fixture plan

| Wording | Expected | Current | Risk |
| --- | --- | --- | --- |
| Allowed in part | `mixed` outcome / `mixed` winner state | Supported by partial-relief detection | Partial relief can blur Minister win-rate denominators if mixed cases are counted as clean wins/losses |
| Withdrawn / discontinued | Current deterministic record, but not a merits disposition | Classified today as `withdrawn` with outcome status `lost` | Minister win-rate can be overstated if withdrawals are treated like merits wins |
| Supreme Court wording like *Vavilov* | Final order still follows the operative verb | Supported when the dispositive wording is still explicit | Citations to *Vavilov* should not be read as an outcome signal by themselves |
| Conditional order | Separate conditional disposition label | Xfailed: no dedicated conditional disposition today | Current classifier can collapse conditions into plain allowed/granted wording |
| Questions certified | Separate certification disposition label | Xfailed: no final-disposition classification today | Non-merits certification should stay out of Minister win-rate numerators |
| Matter returned for redetermination | Separate remittal/redetermination disposition label | Xfailed: no dedicated redetermination label today | Treating remittals as undetermined undercounts Minister losses |

## Notes on Minister win-rate impact

- `mixed` outcomes should stay out of a pure win/loss count unless the reporting layer explicitly defines a partial-relief denominator.
- Withdrawn/discontinued matters can inflate Minister wins if they are counted as ordinary respondent wins instead of a separate non-merits bucket.
- Questions certified and redetermination orders should not be collapsed into final merits wins or losses.

## Validation used

- Focused pytest slice: `tests/test_metadata.py`
- Behavior constraint: no classifier code changes were made for this task

