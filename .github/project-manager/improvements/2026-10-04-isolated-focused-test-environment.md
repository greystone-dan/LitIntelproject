# Improvement: Probe an isolated test environment before blocking on dependencies

Observed issue: The default Python environment lacked pytest and runtime imports,
so the first focused test and generated-document attempts stopped before code
behavior could be checked.

Evidence: `requirements-dev.txt` inherits the pinned runtime requirements and
pins `pytest-cov==5.0.0`. In this issue, an isolated `/tmp` environment with
selected existing dependencies ran seven fake-provider tests, nine targeted
API/search/ingestion tests, and the generated-reference check successfully.
`PYTHON_DOTENV_DISABLED=1` was used; no database, `.env`, or model artifacts were
accessed. The user also confirmed the latest Actions run was `action_required`
with zero jobs and no failed logs.

Proposed change: Before treating missing local test packages as a blocker,
check the repository's pinned development requirements and CI deselection
policy, then try a temporary minimal environment for the narrow fake-only
validation. Exclude model packages and never relax DB/`.env`/deployment
boundaries.

Expected value and risk: Reduces avoidable blocked tasks and improves evidence
quality. External package installation is bounded to existing pins and a
temporary environment; it must not alter repository dependencies or trigger
model downloads.

Decision and date: Defer workflow automation until this pattern recurs. Use the
manual isolated-environment check for issue #203. 2026-10-04.
