# Unresolved Citation Follow-ups

Status: deferred
Recorded: 2026-09-06
Owner surface: citation resolution, source coverage, and extraction QA

## Evidence

The 2026-09-06 conservative resolution checkpoint linked 1,405,281 of 2,152,332 citation rows. The remaining 747,051 rows include 697,037 short/name rows and 50,014 formal/neutral rows. Exact citation variants, parenthesized reporter years, unique canonical titles, preserved same-source anchors, and repeated globally resolved aliases were applied with self-case and collision gates.

## Deferred opportunities

1. Expand the canonical case inventory for authorities that are absent locally. This should start with a read-only frequency report grouped by normalized citation and source provenance, followed by bounded source acquisition with terms and provenance preserved.
2. Repair extraction for truncated and anonymized case names. Use exact source offsets and a gold set; do not replace the stored text or invent a target from a surname alone.
3. Build a reviewed alias table for recurring historical and alternate citation forms. Require citation-number or title evidence, reviewer provenance, and ambiguity retention.
4. Audit unresolved short/name families with a precision sample before adding any new rule. A proposed rule must show unique-target precision on a held-out set and preserve unresolved rows when evidence conflicts.

## Boundary

Do not add broad fuzzy matching, single-party surname matching, or external model adjudication to the production writer without a new collision analysis, a held-out precision check, and an explicit cost/benefit decision. The current local deterministic rules remain the production baseline.

## Next bounded experiment

Generate a read-only report of the top unresolved normalized authorities by frequency, source case count, citation kind, and candidate canonical-title coverage. No database writes or source downloads should occur in this experiment.
