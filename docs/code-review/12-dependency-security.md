# Dependency Security Review: Three Pinned Packages

**Issue:** #663
**Review date:** 2026-10-24
**Checkout:** issue branch `copilot/dependency-security-report`, based on
`origin/main` at `d2bcb41ea1e424024fabd3bc5c19028d75ebf6e2`
**Scope:** report only. No dependency, application, test, workflow, or other
documentation files were changed.

## Executive summary

The three direct pins are in `requirements.txt`. `requirements-dev.txt` includes
that manifest (`-r requirements.txt`), while `requirements-ml.txt` does not
repeat any of these pins. The repository's audit workflows scan
`requirements.txt`, but are informational and do not prove runtime reachability
or exploitability (`docs/SECURITY_DEPENDENCIES.md`; `.swm/12.ci-quality-workflow.sw.md`).

**Advisory verification is incomplete.** An exact-version OSV API lookup was
attempted for all three PyPI pins, but external DNS resolution failed
(`URLError: [Errno -5] No address associated with hostname`). The advisory,
release, and changelog links below are authoritative follow-up sources, but
were not fetched in this run. Consequently, no advisory ID, affected range,
severity, or fixed version is asserted as verified here. A lead is not a
confirmed finding; lack of a retrieved finding is not evidence of no
vulnerability.

Ranked below by reachable application surface and urgency to verify, not by
confirmed severity:

1. **`python-multipart==0.0.9` — highest verification priority.** FastAPI
   multipart form/file handling is used by upload and form endpoints. A
   parser-level issue could be reached before route-level document processing.
2. **`pypdf==4.2.0` — high verification priority.** PDF parsing is used by
   upload workflows, including live analysis and de-identification. Existing
   resource limits do not establish mitigation for an upstream parser defect.
3. **`sentence-transformers==3.0.0` — verify, but no package-specific advisory
   status is established.** It is used by local embedding/search code and
   scripts, although the default query-embedding provider is disabled.

These priorities are provisional exposure assessments, not verified
vulnerability ratings.

## Manifest inventory

| Manifest | Pin(s) / inclusion | Interpretation |
| --- | --- | --- |
| `requirements.txt:24` | `sentence-transformers==3.0.0` | Direct pin; base application/CI manifest. |
| `requirements.txt:45` | `python-multipart==0.0.9` | Direct pin; used indirectly by FastAPI multipart form/file parsing. |
| `requirements.txt:47` | `pypdf==4.2.0` | Direct pin; imported by PDF resource/parsing code. |
| `requirements-dev.txt:1` | `-r requirements.txt` | Inherits the three base pins; no duplicate direct pin. |
| `requirements-ml.txt:1-9` | Only `spacy` and its model are declared | Does not repeat these pins. The documented optional-ML install combines it with the base requirements. |

No other direct declaration of these three packages was found in
`requirements*.txt`. This inventory does not lock or establish the resolved
transitive dependency tree.

## Advisory and upgrade assessment

| Package and pin | Advisory status in this review | Candidate smallest issue-specific floor | Source links |
| --- | --- | --- | --- |
| `sentence-transformers==3.0.0` | **Unverified.** Exact-version advisory lookup could not reach OSV; no clean bill of health can be inferred. | **Unverified / not selected.** First establish any direct or transitive advisory and the resolved dependency set; do not choose a security bump from this report alone. | [PyPI 3.0.0](https://pypi.org/project/sentence-transformers/3.0.0/); [upstream releases](https://github.com/UKPLab/sentence-transformers/releases); [OSV PyPI search](https://osv.dev/list?ecosystem=PyPI&q=sentence-transformers); [GitHub Advisory search](https://github.com/advisories?query=sentence-transformers) |
| `python-multipart==0.0.9` | **Unverified lead:** CVE-2024-53981 / GHSA-59g5-xgcq-4qw3 are candidate records to check. Whether the advisory is authentic/current in the linked sources and whether this exact pin is in its affected range were not verified here. | **Unverified candidate only:** 0.0.18 is a lead for the minimum fix version associated with that advisory; it is not confirmed as a currently safe target. Recheck current advisories and all resolved dependencies before selecting any target. | [GitHub advisory lead](https://github.com/Kludex/python-multipart/security/advisories/GHSA-59g5-xgcq-4qw3); [NVD CVE record](https://nvd.nist.gov/vuln/detail/CVE-2024-53981); [PyPI 0.0.9](https://pypi.org/project/python-multipart/0.0.9/); [upstream releases](https://github.com/Kludex/python-multipart/releases); [OSV search](https://osv.dev/list?ecosystem=PyPI&q=python-multipart) |
| `pypdf==4.2.0` | **Unverified lead:** CVE-2024-41869 / GHSA-4xfr-9xv4-39c3 are candidate records to check. Whether the advisory is authentic/current in the linked sources and whether this exact pin is in its affected range were not verified here. | **Unverified candidate only:** 5.0.0 is a lead for the minimum fix version associated with that advisory; it is a major-version boundary, not a confirmed currently safe target. Recheck current advisories and compatibility before selecting any target. | [GitHub advisory lead](https://github.com/py-pdf/pypdf/security/advisories/GHSA-4xfr-9xv4-39c3); [NVD CVE record](https://nvd.nist.gov/vuln/detail/CVE-2024-41869); [PyPI 4.2.0](https://pypi.org/project/pypdf/4.2.0/); [upstream 5.0.0 release](https://github.com/py-pdf/pypdf/releases/tag/5.0.0); [upstream changelog](https://github.com/py-pdf/pypdf/blob/main/CHANGELOG.md); [OSV search](https://osv.dev/list?ecosystem=PyPI&q=pypdf) |

The two named CVE/GHSA pairs and candidate floors above are **unverified
research leads**, not findings. No source content was retrieved in this
environment, so the report cannot confirm advisory existence, affected
intervals, severities, or patch notes. Do not treat these candidate floors as
recommendations to apply. The authoritative records and upstream release notes
must be checked successfully before a dependency change is planned.

## Application use, reachability, and compatibility risks

### `sentence-transformers`

- `backend/embedding_providers.py` lazy-loads the sentence-transformers model
  provider. `backend/query_embedding_providers.py` supplies the opt-in local
  query-embedding provider; the default provider is `none`.
- `backend/search_service.py` can use local embeddings for relevant search
  paths. `backend/routes.py` exposes local semantic/search workflows.
- Scripts also use the package for local chunk embeddings and argument-list
  similarity (`scripts/embed_local_chunks.py`, `scripts/merge_argument_lists.py`,
  and `scripts/eval_models.py`).
- A change can affect model loading, dependency compatibility, embedding
  behavior, latency, memory use, or vectors produced for a given model. Those
  are compatibility risks to test; no specific break is verified for any
  candidate version.
- Existing focused coverage includes
  `tests/test_embedding_providers.py` and `tests/test_local_embeddings.py`.
  These tests exercise provider behavior but do not by themselves establish
  compatibility with every real model/artifact.

### `python-multipart`

- No direct package import was found. FastAPI `File`, `Form`, and `UploadFile`
  declarations rely on multipart handling for request parsing.
- Reachable examples include live document analysis, upload-based
  de-identification/re-identification, and other file/form routes in
  `backend/routes.py`; `backend/main.py` also declares a `Form` input.
- Existing request coverage includes multipart uploads/forms in
  `tests/test_live_analysis.py`, `tests/test_live_reader.py`, and
  `tests/test_deidentify.py`.
- A change may alter acceptance/rejection of malformed boundaries, form fields,
  or uploaded files, and may interact with FastAPI/Starlette versions. Preserve
  route status codes, validation, limits, and response contracts; no concrete
  API break is verified.

### `pypdf`

- `backend/resource_limits.py` imports `PdfReader` and provides bounded page/text
  extraction. PDF processing is reached through live analysis and upload-based
  de-identification/re-identification flows; there are also PDF-specific route
  paths.
- Existing coverage includes PDF extraction and live-analysis cases in
  `tests/test_live_analysis.py`, and upload/redaction paths in
  `tests/test_deidentify.py` and `tests/test_live_reader.py`.
- The `PdfReader` call surface appears localized, but the candidate fix crosses
  a major release boundary. Check parser defaults, malformed/encrypted-file
  behavior, page/text limits, and exception handling against the installed
  version. This is a compatibility test plan, not a claim that these APIs
  changed.

All reachability statements above describe checked-in call sites, not whether
the application is externally accessible, a malicious input is accepted, or an
advisory is exploitable in deployment.

## Ranked recommendation and test plan

1. **Verify `python-multipart` advisory lead and upload parser behavior first.**
   Retrieve the linked GHSA/NVD/OSV records and upstream release notes; establish
   the exact affected range and current patched release. If a future change is
   separately authorized, run the focused multipart route tests above and add
   malformed-boundary/form regression coverage for any confirmed issue.
2. **Verify `pypdf` advisory lead and PDF parser behavior.** Establish the
   affected range and fixed release from authoritative records/changelog. If a
   future change is separately authorized, test valid, malformed, encrypted,
   and over-limit PDF fixtures through the bounded parser and the live-analysis
   and de-identification routes. Pay particular attention to compatibility
   across the candidate major-version boundary.
3. **Resolve `sentence-transformers` and its transitive tree.** Check exact
   package and resolved dependency versions against current advisory sources.
   If a future change is separately authorized, run the provider/local-embedding
   tests and the local semantic-search API contract; include a real model smoke
   check only where model artifacts are already available and no external or
   paid operation is needed.
4. **After any separately approved dependency patch**, run the repository's
   `pip-audit -r requirements.txt` scan and normal focused tests in the patch
   branch, then broader CI as required. The current audit workflows are
   non-blocking; inspect their artifacts and do not treat a green run as proof
   of no risk. This report does not request or apply any upgrade.

## Validation and limitations

- The exact-version OSV API queries for all three pins failed before returning
  data because external DNS resolution was unavailable. Linked GHSA, NVD,
  PyPI, release, and changelog pages were not retrieved; advisory claims and
  candidate floors therefore remain **unverified**.
- A read-only repository inventory confirmed the three direct pins and relevant
  application, script, and test call sites. No tests, package installation,
  dependency audit, database operation, deployment, or upgrade was performed.
- `python scripts/check_generated_docs.py` was attempted and failed because
  `fastapi` and `sqlalchemy` are unavailable for the API/schema generators.
- `git diff --no-index --check /dev/null
  docs/code-review/12-dependency-security.md` passed after removing trailing
  whitespace. A local Markdown-link check found 15 links and no broken local
  links; external links were not reachable or checked.
- A high-confidence credential-pattern scan checked four common private-key,
  AWS, GitHub-token, and OpenAI-key patterns and found no matches. This was a
  targeted scan, not a full repository secret-scanner run.
- The `CodeQL` CLI was unavailable, no CodeQL workflow/configuration was found
  under `.github/workflows/`, and `gh auth status` reported that the CLI is not
  logged in. A remote CodeQL run could not be initiated from this environment.
- The only authorized file change for this report-only issue is this report.
  The canonical dependency guide and CI-quality Swimm walkthrough remain
  unchanged by design; no workflow or dependency behavior was changed.

**Disposition:** the report artifact is complete, but external advisory
verification is blocked. The package-specific advisory/fix-version assessment
should remain open until authoritative sources are retrievable and checked.

## Execution record

- **Task:** Produce the issue #663 dependency-security assessment.
- **Why now:** The three direct dependency pins need an evidence-backed,
  reachability-aware review; report only.
- **Owner surface:** Dependency-security review report.
- **Dependencies:** Authoritative advisory and upstream release/changelog
  records; external lookup was blocked.
- **Risk boundary:** No requirements, application, tests, workflow, database, or
  deployment changes. No upgrades are proposed for application.
- **Smallest falsifiable check:** Reconcile the exact pins across all
  `requirements*.txt` files and confirm source call sites/tests; separately
  verify exact versions against current authoritative advisory records.
- **Acceptance:** The manifest/use/reachability inventory is reported. The
  advisory-verification criterion remains blocked by unavailable external
  sources.
- **Docs/generated references:** This report is the only new file, as requested.
  No separate task record, canonical dependency-guide edit, or Swimm walkthrough
  update was made because the issue limits the change to exactly one file.
- **Rollback/recovery:** Remove this report; no runtime behavior or dependency
  state changed. Retry source verification when advisory sites are reachable.
- **Evidence:** Inventory was delegated read-only; OSV queries failed DNS
  resolution. Documentation, local-link, targeted secret-pattern, and CodeQL
  validation results and limitations are recorded above.
- **Commit allowed:** yes. **Push allowed:** yes. Neither was performed.
- **Status:** Report delivered; advisory verification and the documentation
  checkpoint are blocked by source/network and one-file scope constraints.
