# Improvement: Verify user-facing workflow labels against the active UI

Evidence: Issue #71 source review caught that `docs/RESEARCH_UI_GUIDE.md`
described the retired standalone Judge Outcomes view as active and that the
quick-start omitted the Judge Profile's explicit denominator and Minister
filter scope.

Recommendation: For future analyst-facing UI documentation, cross-check named
routes/views against `DOCS_INDEX.md` and verify metric labels, denominators, and
filter scope in the current page builder before publication.

Scope: Deferred process improvement; this task corrects the guide and its
canonical/Swimm pointers only.
