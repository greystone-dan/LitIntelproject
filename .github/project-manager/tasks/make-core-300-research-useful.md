# Task: Make Core 300 research workflow useful

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

Task: Define and implement the highest-value next workflow for using Core 300 paragraph assessments and linked citation evidence in legal research.

Why now: The current proof of concept can find assessment paragraphs, but usefulness depends on helping a researcher move from a research question to comparable cases, source paragraphs, and citation evidence without overclaiming semantic meaning.

Owner surface: Active Data Explorer Core 300 workflow and its report-only assessment/evidence layer.

Dependencies: Existing 300-case allowlist, paragraph assessments, citation bridge artifact, Core Cases UI, inline reader, and cohort assessment search endpoint.

Risk boundary: Read-only research assistance. Preserve provenance and backend-owned offsets; do not infer citation treatment, alter canonical records, expand beyond the cohort, or launch paid/unbounded model operations without approval.

Commit allowed: yes
Push allowed: yes

Smallest falsifiable check: Given one research question, a researcher can retrieve a short ranked set of Core 300 assessment hits, inspect the source paragraph, see linked citation evidence, and compare at least two cases without losing cohort/provenance context.

Acceptance criteria:
- Identify one primary researcher workflow and one measurable success signal.
- Rank candidate improvements by research value, implementation cost, explainability, and risk.
- Select the smallest next implementation slice with a focused validation command.
- Record deferred opportunities separately rather than expanding scope.
- Update the relevant canonical documentation and Swimm walkthrough when implementation begins.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`.

Rollback/recovery: Keep the current Core 300 search as the fallback; revert only the selected additive workflow slice if its focused check fails.

Evidence:
- Current Core 300 search loads 100 ordinary results and provides an experimental assessment search over 300 report-only records.
- Current assessment result rendering opens a case but does not yet provide a comparison/evidence review workflow.
- Added `/analytics/search/cohort-assessments/compare` for deterministic topic/role comparison across the Core 300 cohort.
- Preserved `(case_id, paragraph, chunk_id, citation_id)` citation identity and exposed paragraph-anchored citation chips.
- Focused validation: `venv\\Scripts\\python.exe -m pytest tests/test_discussion_units_sandbox.py tests/test_api.py -k 'cohort_assessment' -q` -> 4 passed, 2 warnings.
- Documentation checkpoint updated in `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/8.upryk5h6.sw.md`.
- Citation target-case resolution and paragraph-local citation offsets remain deferred because the bridge artifact does not provide those fields.
