# Dependency Security Review: Three Pinned Packages

**Issue:** #663
**Review date:** 2026-10-24
**Base:** `d2bcb41ea1e424024fabd3bc5c19028d75ebf6e2`
**Scope:** Report only. No dependency or application changes are proposed or
applied.

## Summary

The pins are `sentence-transformers==3.0.0`, `python-multipart==0.0.9`, and
`pypdf==4.2.0` in `requirements.txt`. The `requirements-dev.txt` manifest
includes that file; `requirements-ml.txt` does not repeat these packages.
The GitHub-reviewed advisory records below were retrieved on the review date.
They are package-level matches, not a scan of the complete resolved
environment.

All three pins fall in verified affected ranges. The smallest versions that
cover the package-specific advisories identified here are:

| Package | Assessment floor (not an instruction to upgrade) | Why |
| --- | --- | --- |
| `sentence-transformers` | `5.6.0` | Fixes the reviewed local-model code-execution advisory. |
| `python-multipart` | `0.0.31` | Fixes the reviewed issues with minimum patch floors of `0.0.27`, `0.0.30`, and `0.0.31`. PyPI reports `0.0.32` as current on the review date. |
| `pypdf` | `6.21.2` | Fixes the latest reviewed parser advisories identified, including records fixed in `6.21.2`. This crosses from 4.x to 6.x. |

These are issue-specific minimum floors, not guarantees against future or
transitive advisories. Owner approval is required before any upgrade.

## Advisories verified

### `sentence-transformers==3.0.0`

| Advisory | Affected / fixed | Weakness |
| --- | --- | --- |
| [GHSA-jhr6-gm9c-rqjv / CVE-2026-68770](https://github.com/advisories/GHSA-jhr6-gm9c-rqjv) | `< 5.6.0`; fixed in `5.6.0` | Critical (CVSS 9.8) code execution when an attacker can influence a local model directory: custom Python referenced by `modules.json` can load despite `trust_remote_code=False`. |

The app’s `POST /search/chunks/local` accepts a `model_name`
(`backend/models.py`, `backend/routes.py`) and passes it to
`SentenceTransformer(model_name, device=...)`
(`backend/search_service.py`, `backend/embedding_providers.py`). The rollout
flag defaults on, although configuration can disable it. Thus model loading is
reachable through a request-selected model name when that route is enabled.
The vulnerable condition still requires attacker-influenced model files to be
loaded; whether a deployed instance permits a requester to cause such a model
to be fetched or selected is **unverified**. The route does not accept an
uploaded model directory. The separate query-embedding provider defaults to
`none`, but that does not disable the local-chunk route.

**Compatibility:** The 5.6.0 release notes warn when loading local custom code
without `trust_remote_code=True` and say this will be required in v6.0. This
app does not pass that option. Ordinary `BAAI/bge-m3` loading is not custom
code in the checked-in code, but custom model behavior and the transitive
dependency resolution are **unverified**. The upgrade spans several major
versions; validate model loading, embeddings, dimensions, and installed
transformers/torch compatibility. The candidate release notes do not document
a change to this app's basic `SentenceTransformer(..., device=...)` call;
runtime compatibility is **unverified**.

**Existing tests:** `tests/test_embedding_providers.py`,
`tests/test_local_embeddings.py`, and
`test_local_chunk_search_respects_rollout_disable` in `tests/test_api.py`.
Provider tests use fakes, and the API test covers only the disabled-rollout
branch; they do not prove real model artifact compatibility or successful
model loading from the local-search route.

Sources: [GitHub advisory record](https://api.github.com/advisories/GHSA-jhr6-gm9c-rqjv);
[5.6.0 release notes](https://github.com/huggingface/sentence-transformers/releases/tag/v5.6.0).
The queried GitHub-reviewed package records returned this advisory; coverage
outside that source/query, including transitive dependencies, is **unverified**.

### `python-multipart==0.0.9`

| Advisory | Affected / fixed | Weakness |
| --- | --- | --- |
| [GHSA-59g5-xgcq-4qw3 / CVE-2024-53981](https://github.com/advisories/GHSA-59g5-xgcq-4qw3) | `< 0.0.18`; fixed in `0.0.18` | High (CVSS 7.5) CPU/logging denial of service from malformed multipart boundary preamble or epilogue. |
| [GHSA-pp6c-gr5w-3c5g / CVE-2026-42561](https://github.com/advisories/GHSA-pp6c-gr5w-3c5g) | `< 0.0.27`; fixed in `0.0.27` | High (CVSS 7.5) CPU denial of service from unbounded multipart part-header count/size. |
| [GHSA-vffw-93wf-4j4q / CVE-2026-53537](https://github.com/advisories/GHSA-vffw-93wf-4j4q) | `< 0.0.30`; fixed in `0.0.30` | Low (CVSS 3.7) `Content-Disposition` extended-parameter interpretation conflict can smuggle field names or filenames past an upstream inspector. |
| [GHSA-6jv3-5f52-599m / CVE-2026-53538](https://github.com/advisories/GHSA-6jv3-5f52-599m) | `< 0.0.30`; fixed in `0.0.30` | Low (CVSS 3.7) Semicolon handling in URL-encoded forms can create a parser differential and smuggle fields. |
| [GHSA-5rvq-cxj2-64vf / CVE-2026-53539](https://github.com/advisories/GHSA-5rvq-cxj2-64vf) | `< 0.0.30`; fixed in `0.0.30` | High (CVSS 7.5) Quadratic-time parsing of semicolon-separated URL-encoded forms can exhaust CPU. |
| [GHSA-v9pg-7xvm-68hf / CVE-2026-53540](https://github.com/advisories/GHSA-v9pg-7xvm-68hf) | `< 0.0.31`; fixed in `0.0.31` | Low (CVSS 3.7) Negative `Content-Length` makes direct `parse_form()` read to EOF. The advisory says Starlette/FastAPI do not use this helper; no direct `parse_form()` call was found in this repo, so this specific path is not shown reachable here. |

FastAPI route declarations use `File`, `Form`, and `UploadFile` in
`backend/routes.py` and `backend/main.py`. Multipart parsing therefore occurs
before upload handlers process request contents. The app accepts attacker-
provided document uploads on its live-analysis and de-identification routes.
Network exposure of those routes in a particular deployment is **unverified**.
The malformed-boundary and unbounded-header DoS advisories are directly
relevant to this parser surface. Form-field parser differences are relevant
where URL-encoded requests are accepted. The filename/field-name smuggling
impact depends on downstream use; checked-in upload names are validated or
passed into document analysis, and no claim of a confirmed authorization
bypass is made.

**Compatibility:** The `0.0.30` changelog changes URL-encoded parsing to use
only `&` and ignores RFC 2231/5987 `name*` and `filename*` parameters; `0.0.31`
validates negative `Content-Length` and changes multipart header handling and
performance. These can change behavior for malformed or non-standard forms;
ordinary FastAPI `File`/`Form` use is the intended path. Compare form values,
filenames, validation, status codes, and upload limits after an authorized
upgrade. No application code directly calls `python-multipart` APIs.

**Existing tests:** Multipart upload/form coverage includes
`tests/test_live_analysis.py`, `tests/test_live_reader.py`, and
`tests/test_deidentify.py`. No test specifically exercises malformed boundary
tails, oversized part headers, semicolon form ambiguity, or extended
`Content-Disposition` parameters.

Sources: [GitHub-reviewed package query](https://api.github.com/advisories?ecosystem=pip&affects=python-multipart&per_page=100);
[0.0.31 changelog](https://github.com/Kludex/python-multipart/blob/master/CHANGELOG.md);
[PyPI package metadata](https://pypi.org/pypi/python-multipart/json). The queried
records returned the six advisories listed above. Older
[CVE-2024-24762 / GHSA-2jv5-9r88-3w3p](https://github.com/advisories/GHSA-2jv5-9r88-3w3p)
is fixed in `0.0.7` and does **not** affect `0.0.9`; this advisory is included
to distinguish the earlier lead from the vulnerable findings.

### `pypdf==4.2.0`

GitHub-reviewed records below all include version ranges with a floor above
`4.2.0`; therefore the pin is in each affected range. Advisories are grouped
by the first fixed release; the short weakness descriptions summarize the
advisory titles and impacts.

| Fixed in | Verified advisories (GHSA / CVE) and weakness |
| --- | --- |
| `6.21.2` | [GHSA-6c7f-9265-g8fw / CVE-2026-115572](https://github.com/advisories/GHSA-6c7f-9265-g8fw), repeated references to a missing object cause long runtimes; [GHSA-jr96-gvgh-j3r4 / CVE-2026-115585](https://github.com/advisories/GHSA-jr96-gvgh-j3r4), repeated malformed cross-reference streams cause long runtimes; [GHSA-gmh7-3g9r-mjh5 / CVE-2026-115580](https://github.com/advisories/GHSA-gmh7-3g9r-mjh5), large cross-reference limits cause long runtimes. |
| `6.21.1` | [GHSA-5hx5-vpf9-5wcv / CVE-2026-113786](https://github.com/advisories/GHSA-5hx5-vpf9-5wcv), crafted `/DCTDecode` data can invoke arbitrary image parsers; advisory says optional Pillow must be installed for impact. |
| `6.21.0` | [GHSA-6vvc-x485-93v7 / CVE-2026-113789](https://github.com/advisories/GHSA-6vvc-x485-93v7), costly form-field retrieval; [GHSA-f54x-cmq8-qg57 / CVE-2026-113790](https://github.com/advisories/GHSA-f54x-cmq8-qg57), large arrays/dictionaries consume memory; [GHSA-cgf9-327m-v77c / CVE-2026-113791](https://github.com/advisories/GHSA-cgf9-327m-v77c), many small content-stream operations consume memory. |
| `6.20.1` | [GHSA-qfv9-64jg-mh7p / CVE-2026-113792](https://github.com/advisories/GHSA-qfv9-64jg-mh7p) and [GHSA-9mx8-4j7g-633p / CVE-2026-113793](https://github.com/advisories/GHSA-9mx8-4j7g-633p), crafted tree/outline structures can cause infinite loops. |
| `6.20.0` | [GHSA-39mj-jf6j-2qj3 / CVE-2026-113794](https://github.com/advisories/GHSA-39mj-jf6j-2qj3), truncated cross-reference table can loop; [GHSA-7mh2-4gg2-979f / CVE-2026-113795](https://github.com/advisories/GHSA-7mh2-4gg2-979f), multiple filters can consume excessive memory. |
| `6.19.0` | [GHSA-v247-6f48-mgcj / CVE-2026-102999](https://github.com/advisories/GHSA-v247-6f48-mgcj), many embedded files cause long runtimes; [GHSA-php9-fj8v-98fj / CVE-2026-102998](https://github.com/advisories/GHSA-php9-fj8v-98fj), form appearance generation can run long; [GHSA-w23x-9jrw-r45c / CVE-2026-103000](https://github.com/advisories/GHSA-w23x-9jrw-r45c), alphabetical page labels can consume memory. |
| `6.18.1` | [GHSA-fp3h-c4fm-7vvf / CVE-2026-102995](https://github.com/advisories/GHSA-fp3h-c4fm-7vvf), large `/ToUnicode` streams; [GHSA-jw7q-gvrg-4vj3 / CVE-2026-102997](https://github.com/advisories/GHSA-jw7q-gvrg-4vj3), malformed `/FlateDecode` streams; [GHSA-g9cg-prrw-2r8q / CVE-2026-102996](https://github.com/advisories/GHSA-g9cg-prrw-2r8q), large font widths; each can cause excessive resource use. |
| `6.18.0` | [GHSA-5jq2-8x83-x246 / CVE-2026-102994](https://github.com/advisories/GHSA-5jq2-8x83-x246), long indirect-object headers cause long runtimes. |
| `6.17.0` | [GHSA-qv6h-rv94-w285 / CVE-2026-102993](https://github.com/advisories/GHSA-qv6h-rv94-w285), large Roman page labels consume memory. |
| `6.16.1` | [GHSA-23w6-3w8w-8484 / CVE-2026-84310](https://github.com/advisories/GHSA-23w6-3w8w-8484) and [GHSA-763m-79hh-57f2 / CVE-2026-84311](https://github.com/advisories/GHSA-763m-79hh-57f2), expensive outline and XForm extraction. |
| `6.16.0` | [GHSA-jp53-mhqp-8xcg / CVE-2026-84309](https://github.com/advisories/GHSA-jp53-mhqp-8xcg), crafted tree insertion can loop. |
| `6.15.0` | [GHSA-fc8x-2rww-xw9m / CVE-2026-82398](https://github.com/advisories/GHSA-fc8x-2rww-xw9m), long non-whitespace input causes inefficient parsing; [GHSA-fp3f-mc75-235c / CVE-2026-71870](https://github.com/advisories/GHSA-fp3f-mc75-235c), large `/ToUnicode` streams consume memory; [GHSA-fwg2-594c-jp42 / CVE-2026-71852](https://github.com/advisories/GHSA-fwg2-594c-jp42), oversized CID font-width ranges cause long runtimes/memory use. |
| `6.14.2` | [GHSA-g867-7843-wf8q / CVE-2026-59935](https://github.com/advisories/GHSA-g867-7843-wf8q), unterminated ASCII85/ASCIIHex inline images can loop during text extraction. |
| `6.14.1` | [GHSA-5xf7-4p34-54qr / CVE-2026-59936](https://github.com/advisories/GHSA-5xf7-4p34-54qr), unterminated inline images can loop during text extraction. |
| `6.14.0` | [GHSA-55h5-xmcq-c37v / CVE-2026-59937](https://github.com/advisories/GHSA-55h5-xmcq-c37v), malformed xref entries cause long runtimes; [GHSA-5qjq-93h5-hrgp / CVE-2026-59938](https://github.com/advisories/GHSA-5qjq-93h5-hrgp), wrong image dimensions cause excessive memory use. |
| `6.13.3` | [GHSA-jm82-fx9c-mx94](https://github.com/advisories/GHSA-jm82-fx9c-mx94), missing stream lengths can bypass declared-length limits and exhaust memory. |
| `6.13.1` | [GHSA-g9xf-7f8q-9mcj / CVE-2026-54651](https://github.com/advisories/GHSA-g9xf-7f8q-9mcj), crafted article/thread structures can loop. |
| `6.13.0` | [GHSA-m2v9-299j-rv96 / CVE-2026-54531](https://github.com/advisories/GHSA-m2v9-299j-rv96) and [GHSA-52x6-gq3r-vpf4 / CVE-2026-54530](https://github.com/advisories/GHSA-52x6-gq3r-vpf4), writer outline/article or layout-mode font paths can loop. |
| `6.12.2` | [GHSA-j543-4vmf-qm7v / CVE-2026-49461](https://github.com/advisories/GHSA-j543-4vmf-qm7v), self-referencing form XObjects can consume memory; [GHSA-5hgr-hg42-57jg / CVE-2026-49460](https://github.com/advisories/GHSA-5hgr-hg42-57jg), PNG predictor streams can take long to decode. |
| `6.12.1` | [GHSA-wjqc-6w8f-h24c / CVE-2026-48735](https://github.com/advisories/GHSA-wjqc-6w8f-h24c), large XMP metadata can exhaust memory. |
| `6.12.0` | [GHSA-248m-82v9-q6g6 / CVE-2026-48156](https://github.com/advisories/GHSA-248m-82v9-q6g6), zero-only cross-reference stream widths with large `/Size` cause long runtimes. |
| `6.10.2` | [GHSA-x284-j5p8-9c5p / CVE-2026-41314](https://github.com/advisories/GHSA-x284-j5p8-9c5p), oversized FlateDecode image dimensions can exhaust memory; [GHSA-4pxv-j86v-mhcw / CVE-2026-41313](https://github.com/advisories/GHSA-4pxv-j86v-mhcw), large trailer size in incremental mode causes long runtimes. |
| `6.10.1` | [GHSA-jj6c-8h6c-hppx / CVE-2026-41168](https://github.com/advisories/GHSA-jj6c-8h6c-hppx), large cross-reference/object stream size values cause long runtimes. |
| `6.10.0` | [GHSA-3crg-w4f6-42mx / CVE-2026-40260](https://github.com/advisories/GHSA-3crg-w4f6-42mx), crafted XMP entity declarations can exhaust memory. |
| `6.9.2` | [GHSA-87mj-5ggw-8qc3 / CVE-2026-33699](https://github.com/advisories/GHSA-87mj-5ggw-8qc3), malformed dictionaries can loop during non-strict recovery. |

**Reachability:** `backend/resource_limits.py` constructs `PdfReader` over
uploaded PDF bytes and extracts text. The same helper is used in live analysis
and document workflows. Inputs are untrusted uploads; the app limits the
compressed upload size (10 MiB by default), extracted characters (5 million),
and pages (500). Those checks do not establish that parser work or memory use
is bounded before page extraction. The specific advisory paths are not all
confirmed to be invoked by this reader call; that per-advisory reachability is
**unverified**. Handling attacker-supplied PDFs makes the broader parser
hardening directly relevant.

**Compatibility:** The advisories and upstream changelog show resource limits,
parser robustness changes, and one `/DCTDecode` image-parser restriction in
`6.15.0`–`6.21.2`. `PdfReader(BytesIO(...))` and page text extraction remain the
call-site API, but moving from 4.x to 6.21.2 crosses multiple releases and may
alter malformed/encrypted PDF handling, extracted text, or exceptions. No
specific removed call-site API was identified; full compatibility is
**unverified** until the focused tests run.

**Existing tests:** PDF upload and extracted-text/page limits are covered by
`tests/test_live_analysis.py`; related upload flows are in
`tests/test_deidentify.py` and `tests/test_live_reader.py`. The existing tests
do not constitute regression tests for each advisory's specially crafted PDF.

Sources: [GitHub-reviewed package query](https://api.github.com/advisories?ecosystem=pip&affects=pypdf&per_page=100);
[upstream changelog](https://github.com/py-pdf/pypdf/blob/main/CHANGELOG.md);
[6.21.2 release](https://github.com/py-pdf/pypdf/releases/tag/6.21.2). This is
the set of affected records individually identified in that query during this
review; whether it is exhaustive across the entire database is **unverified**.
Other databases or later records are also **unverified**. The earlier lead
`CVE-2024-41869` is an Adobe Acrobat/Reader CVE, not a pypdf advisory, and
`GHSA-4xfr-9xv4-39c3` did not resolve in GitHub's advisory API; neither is
counted as a pypdf finding.

## Other aged pins

This is a version-freshness observation, not a security finding or a complete
audit. Pins from 2024 or earlier in the other manifests merit a routine
compatibility/advisory review; package age alone does not establish
vulnerability.

| Manifest | Other pins with 2024-or-earlier release lines |
| --- | --- |
| `requirements.txt` | `fastapi==0.111.0`, `uvicorn==0.29.0`, `psycopg2-binary==2.9.9`, `sqlalchemy==2.0.30`, `alembic==1.13.1`, `pgvector==0.2.5`, `openai==1.30.1`, `tiktoken==0.7.0`, `numpy==1.26.4`, `scipy==1.13.1`, `pandas==2.2.2`, `openpyxl==3.1.5`, `tqdm==4.67.1`, `pydantic==2.7.4`, `httpx==0.27.0`, `requests==2.32.3`, `cloudscraper==1.2.71`, `beautifulsoup4==4.12.3`, `python-docx==1.1.2`, `python-dotenv==1.0.1`, `pyyaml==6.0.1`, `pytest==8.2.2`, `black==24.4.2`. |
| `requirements-dev.txt` | Inherits `requirements.txt`; additionally `pytest-cov==5.0.0` and `pytest-xdist==3.6.1`. |
| `requirements-ml.txt` | `spacy==3.7.5`; the linked `en_core_web_md` wheel is version `3.7.1`. |

The other listed `requirements.txt` pins not in that age group include the
recent `datasets`, Hugging Face, `pyarrow`, and `pycountry` pins visible in the
manifest. A full current-version or transitive audit was not performed.

## Ranked recommendation and test plan

1. **`sentence-transformers`: assess/fix first if the local chunk-search route
   is enabled for untrusted callers.** It has the highest verified severity
   and a request-selected model name reaches model loading. Before an
   owner-approved update, test `tests/test_embedding_providers.py`,
   `tests/test_local_embeddings.py`, and the local-search tests in
   `tests/test_api.py`; then perform an offline smoke test with the configured
   trusted model. Do not test by loading an untrusted model. Whether the live
   route is externally exposed is **unverified**.
2. **`python-multipart`: next for parser-level availability and form
   interpretation issues.** After separate approval, run the upload/form tests
   above and add regression cases for malformed boundary tails, oversized part
   headers, `name*`/`filename*`, and URL-encoded semicolon bodies. Check ordinary
   FastAPI form values and upload behavior against the 0.0.31 changelog changes.
3. **`pypdf`: update planning should include a major-version compatibility
   checkpoint.** After separate approval, run the PDF/live-analysis and
   de-identification tests; exercise valid, malformed, encrypted, and
   over-limit PDFs through `extract_pdf_pages`. Add regression fixtures for
   advisory-specific parser paths only where safe fixtures are available.
4. **After any approved patch**, resolve and scan the full environment (the
   repo's `pip-audit -r requirements.txt` workflow scans the base manifest) and
   run the focused tests above before full CI. The audit workflows are
   informational/non-blocking and do not prove runtime exploitability.

## Validation and limitations

- Repository call sites, manifest pins, tests, and the cited GitHub advisory
  records/changelogs were checked on 2026-10-24. No package install, dependency
  audit, runtime test, database operation, deployment, or upgrade was done.
- Exact route exposure in the live deployment, all possible package advisories
  outside the cited GitHub-reviewed query results, and compatibility after
  upgrading are **unverified**.
- The report is the only changed path, as requested. No tests were added because
  this is report-only and runtime code is unchanged.
- `python scripts/check_generated_docs.py` was attempted and could not run
  because `fastapi` and `sqlalchemy` are unavailable in this environment.
- Local Markdown-link and whitespace checks passed; external sources were
  checked individually where cited. Secret scanning and CodeQL results are
  recorded in the PR checks, not asserted here.
