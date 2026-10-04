# Dependency Security Scanning And SBOM

This guide explains recurring dependency updates, the informational
vulnerability scan, and the software bill of materials (SBOM) artifact.

## Overview

Dependency review uses three complementary signals:

1. **Dependabot**: Weekly grouped update pull requests for Python packages and
   GitHub Actions.
2. **pip-audit**: An advisory scan resolving packages from `requirements.txt`.
3. **CycloneDX**: An SBOM generated from `requirements.txt`.

## Automated Scanning Coverage

### Dependabot Configuration

Dependabot checks pip and GitHub Actions weekly. Updates in each ecosystem are
grouped, with a maximum of five open pull requests per ecosystem.

Configuration: `.github/dependabot.yml`

### Dependency Audit Workflow

**File**: `.github/workflows/dependency-audit.yml`

**Triggers**:
- Pull requests with changes to `requirements*.txt` files
- Every push to `main`
- Weekly schedule: Mondays at 02:00 UTC
- Manual workflow dispatch

**Jobs**:

#### pip-audit (non-blocking)

- Runs `pip-audit -r requirements.txt` and preserves its JSON report and exit
  status in the `pip-audit-results` artifact (30-day retention).
- Writes the scan status and artifact guidance to the job summary.
- Findings and scan failures do not block the workflow.

#### CycloneDX SBOM (non-blocking)

- Installs `cyclonedx-bom` in the workflow only to provide the `cyclonedx-py`
  CLI; neither is a project dependency.
- Generates `sbom.cdx.json` from `requirements.txt`, uploads it in the
  `sbom-results` artifact (30-day retention), and writes a job summary.
- Generation failures do not block the workflow.

These jobs are review signals, not merge gates. Review artifacts even when the
workflow is green; a green run does not by itself establish that dependencies
are safe.

## How to Interpret Findings

### pip-audit Output

The audit report includes:

- **Vulnerability ID**: Reference identifier from vulnerability databases (CVE, GHSA, etc.)
- **Package**: Name and version of affected dependency
- **Vulnerability Description**: What the vulnerability affects
- **Fixed Version**: Recommended patch version (if available)
- **Vulnerability Source**: Database reference (e.g., CVE, PyPI Security Advisory)

Treat an advisory as a lead to assess, not proof that the affected code path is
reachable or exploitable. Check the package and affected version range, advisory
details, available fixed versions, and whether the dependency is used in the
runtime or development environment.

| Finding | Suggested response |
|---------|--------------------|
| Direct dependency with an available fix | Update the declared requirement and review/test the resulting change. |
| Transitive dependency with an available fix | Identify the parent dependency; update it or apply an otherwise compatible resolution. |
| No fix is available | Record the finding, assess exposure, and monitor for an upstream fix or alternative. |
| Development-only dependency | Assess its actual use and exposure; keep the finding visible rather than assuming it is irrelevant. |

Use the SBOM as a component inventory to support review and incident response.
Package metadata such as licenses and hashes is present only when available;
the SBOM is not itself a vulnerability assessment.

## Limitations and Caveats

1. pip-audit can only report known advisories available to its data sources;
   undisclosed or unindexed vulnerabilities may be missed.
2. Resolving `requirements.txt` does not prove what is installed in production,
   whether vulnerable code is reachable, or whether an issue is exploitable.
3. A transitive dependency may not be independently updateable until its parent
   package changes.
4. Weekly scans can lag newly published advisories; rerun or assess urgently
   when new information warrants it.
5. Dependencies omitted from the requirements input or unsupported/private
   package sources may not be represented.

## Patch Ownership & Process

Dependency patch assessment owner: **owner: Daniel, to be assigned**

Patch changes should be reviewed and tested through the normal pull request
process. Production deployment remains a separate controlled operation.

### Suggested Patch SLA Proposal

The following suggested patch SLA is a proposal, not an approved service-level
policy:

| Severity | CVSS score | Suggested acknowledgement | Suggested patch/mitigation target |
|----------|------------|---------------------------|-----------------------------------|
| Critical | 9.0–10.0 | 2 business hours | 24 hours |
| High | 7.0–8.9 | 1 business day | 1 week |
| Medium | 4.0–6.9 | 5 business days | 2–4 weeks |
| Low | 0.1–3.9 | 30 days | Monthly review or next release |

## Workflow Approvals

**PR note:** Workflows pushed by Copilot require human approval for first run.
GitHub may also require first-run approval for automated or external
contributors, depending on repository settings. Review the workflow before
authorizing execution.

## Artifact Retention

Scan artifacts are retained for 30 days by default:
- `pip-audit-results`: Vulnerability scan output (JSON, logs)
- `sbom-results`: SBOM and generation logs

After retention expiration, artifacts are deleted. For compliance documentation, download and archive results as needed.

## Quick Links

- **Dependabot Configuration**: `.github/dependabot.yml`
- **Workflow Definition**: `.github/workflows/dependency-audit.yml`
- **Existing quality workflow**: `.github/workflows/quality.yml` (separate pip-audit signal)
- **Requirements Files**:
  - `requirements.txt` (production)
  - `requirements-dev.txt` (development)

## Feedback & Issues

- Report scanning issues: GitHub Issues (filter by `[security]` label)
- Suggest SLA adjustments: Team discussion
- Propose new scanning tools: RFC in project discussions
