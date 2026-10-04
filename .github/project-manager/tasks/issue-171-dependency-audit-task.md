# Task: Add dependency update and audit automation

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #171 dependency update automation, non-blocking audit/SBOM workflow, and dependency security guidance.

Why now: Establish recurring dependency update and supply-chain review signals without changing application behavior or required test gates.

Owner surface: Dependency automation and security guidance (`.github/`, `docs/SECURITY_DEPENDENCIES.md`, and its existing CI-quality Swimm walkthrough).

Commit allowed: yes

Push allowed: yes

Dependencies: Issue #171 requirements supplied in the task; issue #112 Rules block; existing `quality.yml` conventions.

Risk boundary: Do not edit application code, requirements files, or the existing tests workflow. Audit is informational/non-blocking. Install CycloneDX tooling only inside the new workflow.

Smallest falsifiable check: Parse both new workflow configuration files as YAML, inspect triggers/action pins/commands/artifact paths, then run `git diff --check`.

Acceptance criteria:

- Dependabot configures pip and GitHub Actions weekly grouped updates with at most five open PRs per ecosystem.
- New workflow handles requirement-file PR changes, pushes to main, and a weekly schedule; audit runs `pip-audit -r requirements.txt` non-blocking, writes a summary, uploads its report, generates and uploads `sbom.cdx.json` using workflow-only `cyclonedx-py`, and pins actions by tag.
- Dependency guidance explains scan scope, interpretation, exact patch ownership `owner: Daniel, to be assigned`, and a suggested patch SLA proposal table.
- The related Swimm walkthrough and canonical dependency guidance are updated, and the PR note states workflows pushed by Copilot require human approval on first run.
- Focused config/documentation checks and a secret scan pass; no application or test-workflow files change.

Harness criteria:

The dependency automation and documentation match issue #171 and pass focused validation.

Docs/generated references: `docs/SECURITY_DEPENDENCIES.md` (canonical); `.swm/12.ci-quality-workflow.sw.md` (related Swimm walkthrough); no generated references.

Rollback/recovery: Revert only the new dependency config/workflow/guidance and the corresponding Swimm/task-record updates; no runtime or data changes occur.

Evidence: Issue #112 public-page Rules block read; it prohibits database/deploy-script/.env changes, feature deletion, added project dependencies, and enabling a password gate. These constraints are respected; CycloneDX is installed workflow-local only. The manager verified and corrected the worker's missing Dependabot groups, summary parsing, push trigger scope, and exact owner text. Passed: `yamllint .github/dependabot.yml .github/workflows/dependency-audit.yml`; inline PyYAML assertions for update groups, event filters, non-blocking audit, summary, artifacts, SBOM command, and action tags; local Markdown link/trailing-whitespace checks; changed-file credential-pattern scan (0 matches); `git diff --check`. Canonical documentation updated at `docs/SECURITY_DEPENDENCIES.md`; related Swimm walkthrough updated at `.swm/12.ci-quality-workflow.sw.md`. `python scripts/check_generated_docs.py` was attempted but failed because `fastapi` and `sqlalchemy` are not installed; no generated references were changed. No application tests were run because application code and test workflows were untouched.

Files changed: `.github/dependabot.yml`; `.github/workflows/dependency-audit.yml`; `docs/SECURITY_DEPENDENCIES.md`; `.swm/12.ci-quality-workflow.sw.md`; this task record.
Delegated work: `managed-worker` implemented the three requested files; structured response received. Worker reported YAML validation but did not provide executable command lines; manager will independently validate.
Focused validation: YAML lint, inline YAML behavior assertions, documentation link/whitespace checks, changed-file credential-pattern scan, and diff check passed; generated-document checker blocked by absent `fastapi` and `sqlalchemy`.
Residual risk: Workflow execution and GitHub first-run approval behavior cannot be exercised locally. The generated-document checker requires the missing project dependencies, though generated files are untouched.
Next bounded task: None.

## Hypothesis

If the new configuration matches the requested event filters, command behavior, report/SBOM artifacts, and ownership guidance, focused YAML and documentation checks will confirm a non-blocking, reproducible dependency-review signal without altering runtime dependencies.

## Plan

1. Implement the Dependabot configuration, dedicated workflow, and dependency guidance.
2. Update the existing CI quality walkthrough with links and boundaries for the new workflow.
3. Validate configuration, documentation links, diff scope, and secrets; record results.

## Execution Checkpoints

- Delegation: Managed worker completed implementation of the three requested files; manager corrected acceptance gaps.
- Implementation: `.github/dependabot.yml`, `.github/workflows/dependency-audit.yml`, and `docs/SECURITY_DEPENDENCIES.md`; focused YAML and behavior checks passed.
- Documentation: `docs/SECURITY_DEPENDENCIES.md` and `.swm/12.ci-quality-workflow.sw.md`.
- Recovery: Not applicable; no long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Reuse the CI quality walkthrough | It already documents the pip-audit workflow and is the closest mapped owner; no dedicated dependency-security walkthrough exists. | `.swm/12.ci-quality-workflow.sw.md` |

## Completion

Completion recorded: yes

Summary: Issue #171 dependency automation and advisory guidance implemented; the existing CI-quality Swimm walkthrough was extended.

Validation: `yamllint .github/dependabot.yml .github/workflows/dependency-audit.yml`, PyYAML semantic assertions, local link/trailing-whitespace checks, changed-file credential-pattern scan, and `git diff --check` passed. `python scripts/check_generated_docs.py` did not pass because `fastapi` and `sqlalchemy` are unavailable in the environment.

Residual risk: Workflow behavior and first-run approval require GitHub Actions; generated-reference validation needs the missing Python dependencies.

Next recommended task: None.
