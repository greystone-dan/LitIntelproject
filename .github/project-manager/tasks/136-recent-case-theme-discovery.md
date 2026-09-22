# Task: Derive issue themes from recent cases

Status: in_progress
Created: 2026-09-22
Updated: 2026-09-22

Task: Implement a new read-only theme-discovery layer for cases dated 2020-09-22 through 2026-09-22, using existing evidence and Discussion Unit argument/issue work without changing canonical systems or data.
Why now: Issue themes are the natural demo entry point, but the product must first demonstrate that themes can be derived from recent cases in a traceable way.
Owner surface: `scripts/` recent-case theme discovery and its focused tests.
Dependencies: Existing legal tags, statute references, metadata subjects/types, citation signals, Discussion Unit/sub-theme evidence, and the canonical decision date.
Risk boundary: New report-only layer; no canonical database writes, migrations, changes to existing tags/statutes/metadata, external calls, embeddings, or UI changes in this slice. Exclude records outside the six-year window and report missing dates separately.
Smallest falsifiable check: A bounded report over the recent cohort produces per-case candidate themes with explicit evidence sources, central-versus-mentioned status, and no writes to existing tables.
Acceptance criteria:
- Date window is explicit and uses decision date: 2020-09-22 through 2026-09-22 inclusive.
- Existing Discussion Unit issue/reasoning roles are used when available.
- Existing tags, statutes, metadata, and citation signals are additive evidence only.
- Theme definitions are controlled and explainable, with exclusion/mention handling.
- Output is report-only and preserves case IDs, evidence references, and coverage counts.
- Focused tests cover date boundaries, centrality, evidence provenance, and non-write behavior.
- Canonical docs and relevant Swimm walkthrough are updated with the new layer and its limits.
Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`, and `ROADMAP.md` if implementation scope changes.
Rollback/recovery: Remove the new report script, tests, documentation additions, and generated report artifacts; existing data layers remain unchanged.
Evidence:
- Files: `scripts/discover_recent_case_themes.py`, `tests/test_discover_recent_case_themes.py`, `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, and bounded report `data/eval/reports/recent_case_themes_smoke.json`.
- Delegated work: `Explore` inspected the owning data model, existing metadata subject derivation, and `scripts/inspect_discussion_units.py`; it made no edits and reported no failures.
- Focused validation: `python -m pytest tests/test_discover_recent_case_themes.py -q` passed with 3 tests. `py_compile` passed before focused tests. A bounded read-only report over 25 cases dated within the explicit window produced 21 cases with themes, 25 cases with Discussion Units, and 84 Discussion Units total.
- Report contract: controlled ten-theme registry; explicit evidence kinds; ranked primary/secondary/mentioned projections; default `paragraph` chunk set; no canonical/contextual writes.
- Residual risk: phrase and deterministic subject/tag rules are candidate signals requiring legal-review precision checks. Primary themes can be multiple per case; the smoke cohort is not corpus-wide coverage. Citation counts are contextual only. No UI or persistence is included.
Status: complete
Delegated work:
Focused validation:
Residual risk:
Next bounded task:
Commit allowed: yes
Push allowed: yes
