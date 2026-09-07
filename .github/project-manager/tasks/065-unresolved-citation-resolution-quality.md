# Unresolved citation resolution quality

Status: complete
Created: 2026-09-06
Updated: 2026-09-06

Task: Review unresolved stored case citations, identify recoverable naming and logic patterns, improve conservative case-to-case resolution, and validate that every citation with a confident local target is linked without creating false matches.
Why now: The whole local exact-citation pass linked 1,188,526 of 2,152,332 citation rows, leaving 963,806 unresolved; the SCC Ward check demonstrated that reported and CanLII citations can refer to the same local case under different citation families.
Owner surface: `backend/citations.py`, `scripts/resolve_citation_targets.py`, `scripts/resolve_short_citation_targets.py`, and focused citation-resolution tests.
Dependencies: Canonical `cases` citation/title fields, stored citation rows, existing extraction semantics, and PostgreSQL availability.
Risk boundary: Preserve source offsets, provenance, citation/statute separation, and conservative ambiguity handling; do not delete rows or invent target cases.
Smallest falsifiable check: Produce an unresolved-shape histogram and compare representative formal, reported, neutral, short, and named citations against canonical case aliases before changing resolver logic.
Acceptance criteria:
- Unresolved citation families and likely recoverable patterns are measured from the live database.
- Cross-citation normalization improves recall only where the target is unique and authoritative.
- Short/name resolution remains conservative and rejects ambiguous matches.
- Focused extraction and resolution tests cover each new normalization rule.
- A bounded rerun demonstrates added links and leaves unresolved rows intact for genuine misses.
Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/blank.dudtv9pz.sw.md`.
Rollback/recovery: Revert only newly written target links using the recorded run boundary and preserve all citation rows; rerun the resolver with its resume checkpoint after any fix.
Evidence: Live inventory, focused tests, bounded dry runs, two complete conservative short/name passes, one complete exact formal/neutral pass, final live counts, and documentation checkpoint recorded below.
Commit allowed: yes
Push allowed: yes

## Hypothesis

If unresolved citations are classified by formal citation family and matched against both neutral and reported citation aliases, then a measurable subset can be linked uniquely without broad fuzzy matching or false target assignments.

## Implemented Recovery Rules

- Reported citation variants now accept bracketed, bare, and parenthesized years, including reporter punctuation normalization.
- Formal and neutral rows use an exact canonical-title fallback after citation-variant lookup; source-case self matches and multi-target title collisions remain unresolved.
- Short/name rows use preserved composite anchor text when it uniquely identifies a canonical title.
- Short/name rows also use repeated, uniquely resolved full-name aliases only when the alias is observed from at least two source cases, maps to one target, and its leading party token agrees with the target title.
- Pure short-form normalization is cached for full-corpus execution; matching semantics are unchanged.

An external model or API was not used. The remaining unresolved population contains ambiguous authorities, anonymized or truncated text, missing local case records, and extraction-shape noise; no fuzzy or single-surname rule was applied.

## Evidence

- Initial live baseline: `2,152,332` citation rows, `1,188,526` linked, `963,806` unresolved.
- Same-source anchor pass: `56,454` source cases processed, `108,402` links added, `541,906` ambiguity decisions, exit code `0`.
- Exact formal/neutral recovery: `765,528` unresolved rows inspected, `8,984` links added, including `5,040` exact-title recoveries, exit code `0`.
- Repeated global-alias propagation pass: `56,454` source cases processed, `9,493` links added, `537,642` ambiguity decisions, exit code `0`.
- Final live state: `2,152,332` citation rows, `1,405,281` linked, `747,051` unresolved; unresolved short/name rows `697,037`, unresolved formal/neutral rows `50,014`.
- Ward spot check: `151` rows containing `1993 CANLII 105` link to case `35894`; `31` remain unresolved and are retained for future extraction/source review.
- Focused tests: `118 passed` in `tests\test_citations.py`; resolver modules compiled with `py_compile`; `git diff --check` passed.
- Rejected or deferred ideas: `CSC`/`SCC` connector equivalence had no live unresolved `CSC` rows; `vs`/`versus`/`c.` connector normalization had no meaningful live candidates; broad single-name and anonymized-name matching was collision-prone and was not applied.

Canonical documentation updated: `SYSTEM_REFERENCE.md` and `OVERNIGHT.md`.
Swimm walkthroughs updated: `.swm/blank.dudtv9pz.sw.md` and `.swm/system-map.ovnldklv.sw.md`.
Recovery command: rerun `scripts/resolve_short_citation_targets.py --batch-size 1000 --progress-every 2000` only after PostgreSQL preflight confirms no competing writer; all writes are target-link updates and leave citation rows intact.

## Plan

1. Audit unresolved citation structure and canonical alias coverage.
2. Implement the smallest evidence-backed normalization or alias-index fix.
3. Run focused citation tests immediately, then a bounded database rerun.
4. Update canonical and Swimm documentation with counts, precision safeguards, and residual risk.
