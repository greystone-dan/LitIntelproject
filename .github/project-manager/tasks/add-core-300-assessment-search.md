# Task: Add Core 300 assessment search

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

Task: When users activate Core Cases, keep the existing 100-result case list and reveal a second search bar beneath the main search controls for assessment-aware searching strictly within the 300-case cohort.

Why now: The 300 paragraph assessments are now linked to citation evidence. Researchers need to find concepts such as standard-of-review issues and move from matching assessment paragraphs to their cases and linked citations.

Owner surface: Discussion Unit Core 300 search experience (`backend/discussion_units_sandbox.py`, its route contract, and the local Data Explorer control).

Dependencies: Existing `/analytics/search/cases` cohort scoping, paragraph assessment parser, citation evidence bridge artifact, current Core Cases button/result renderer.

Risk boundary: Read-only proof of concept. No canonical schema changes, no database writes, no citation-treatment inference, no external model calls, no changes to the general search contract outside optional parameters, and no expansion beyond the 300-case allowlist.

Commit allowed: yes
Push allowed: yes

Smallest falsifiable check: Submitting the second search bar with `standard of review` returns only cases from `discussion_units_core_300`, includes matched assessment paragraph metadata, and preserves the existing Core Cases 100-result behavior.

Acceptance criteria:
- Core Cases still loads up to 100 ordinary case results from the 300-case cohort.
- A second assessment-aware search control appears beneath the primary search bar after Core Cases is activated.
- Assessment search is strictly scoped to the 300-case cohort.
- Search matches topic, role, explanation, and linked paragraph text with transparent match metadata.
- Results include case ID, paragraph number, assessment fields, and linked citation IDs when available.
- Empty, malformed, and out-of-cohort requests fail safely.
- Focused route, parser/helper, and UI regression tests pass.
- Canonical documentation and relevant Swimm walkthrough are updated.
- No semantic model calls or citation-treatment classifications are introduced.

Hypothesis: A cached, read-only hybrid matcher over the 300 assessment artifacts can make concept searches useful without requiring a new database table or paid embedding run.

Focused validation: `venv\\Scripts\\python.exe -m pytest tests/test_discussion_units_sandbox.py tests/test_feature_tabs.py -q`.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`.

Rollback/recovery: Remove the optional endpoint/helper, second form, tests, and documentation; the existing Core Cases behavior remains unchanged.

Evidence:
- Delegated Explore inspection confirmed `displayCoreCases`, cohort filtering, assessment parser, and existing search/result contracts.
- Delegation found no current assessment search or assessment embedding index.
- Added cached report-only bridge loading and transparent assessment matching in `backend/discussion_units_sandbox.py`.
- Added `/analytics/search/cohort-assessments` with strict `discussion_units_core_300` validation.
- Added the second Core Cases search control and changed the initial Core Cases request to `limit: 100`.
- Updated `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/8.upryk5h6.sw.md`.
- Focused validation: `venv\\Scripts\\python.exe -m pytest tests/test_discussion_units_sandbox.py tests/test_feature_tabs.py tests/test_api.py -q` -> 73 passed, 1 warning.
- `get_errors` reported no errors in touched Python/UI files; `git diff --check` reported no whitespace errors.
- Browser validation was not run in this bounded pass.
