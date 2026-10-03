# Privacy and security review: live analysis and de-identification

Reviewed: 2026-10-03  
Scope: `backend/live_analysis.py`, `backend/deidentify.py`,
`backend/deidentify_names.py`, the directly related handlers in
`backend/routes.py`, and their focused tests.

## Executive summary

Live Analysis and de-identification do not create canonical case records or
application-managed upload records. The reviewed service code processes upload
bytes per request, and local citation/de-identification work does not call an
external model or resolution service. Live Analysis does return the full
extracted source text and contextual snippets to the caller.

The two successful Live Analysis POST responses now set
`Cache-Control: no-store` and `Pragma: no-cache`, matching the de-identification
API. A focused API test covers both routes. This is a cache directive, not an
access-control mechanism.

The 10 MB upload check is not a complete hostile-file resource limit: both
upload paths read the multipart file before checking its length; DOCX expanded
ZIP size, PDF page count, extraction time, and pasted-text length are not
bounded in the reviewed application code. Large multipart uploads may also be
spooled by Starlette's multipart parser before the route handles them. No
application-managed persistence does not prove that request bytes never touch
temporary storage or that a deployment proxy does not retain request data.

Most importantly, `backend/main.py`'s `private_access_and_noindex` middleware
adds `X-Robots-Tag` but does not validate the access cookie or protect routes.
The existing configuration reference documents this gap. Unless a separately
verified reverse proxy or tunnel enforces access, reachable routes should be
treated as available to anyone who can reach the application. No-index headers
are not authentication.

## Findings

Line references point to the reviewed repository version. Severity reflects
the risk if the application is reachable by untrusted users; the access-control
finding is deployment-dependent.

| Severity | File and lines | Finding | Suggested fix / status |
| --- | --- | --- | --- |
| High (deployment-dependent) | `backend/main.py:78–82`; sensitive handlers in `backend/routes.py:931–1042` | The middleware only adds a search-engine exclusion header; it does not authenticate requests. The sensitive upload and de-identification routes therefore rely on an unverified external access boundary. | Verify and enforce authentication at the deployment gateway before exposure. The repository owner has deliberately left the optional password gate off; this review does not enable it. |
| Medium | `backend/routes.py:937,953,976`; `backend/live_analysis.py:79–87`; `backend/deidentify.py:467–479` | Each upload is fully read before the 10 MiB validation, so that check does not bound bytes read or multipart temporary spooling. Pasted text also has no application-level size check. | Enforce request-body limits before buffering and bound pasted text; retain the parser-level checks as defense in depth. |
| Medium | `backend/live_analysis.py:38–65,263–286`; `backend/deidentify.py:434–464` | DOCX/PDF parsing has no explicit expanded-ZIP, page-count, extracted-text, CPU, or memory budget. A small compressed DOCX or a PDF with many/complex pages could consume disproportionate resources. | Add bounded decompressed-size/page/output limits and time/resource controls with hostile-file tests before broadening parser support. |
| Low (fixed here) | `backend/routes.py:944–945,960–961` | Live Analysis responses contain the complete extracted document text and previously had no explicit cache directives. | Both successful POST routes now set `Cache-Control: no-store` and `Pragma: no-cache`; focused tests assert both headers. |
| Medium (coverage limitation) | `backend/deidentify.py:67–105,269–371,434–479`; `backend/deidentify_names.py:92–110,208–316` | Pattern and optional model-based name detection are heuristic and extraction is incomplete; identifiers, names, indirect identifiers, and text outside supported document parts can remain. | Keep the warning that output is not guaranteed anonymous; require human review and consider adversarial recall testing before relying on it for disclosure. |

## Routes and data flow

| Route | Input and processing | Response / persistence |
| --- | --- | --- |
| `POST /live-analysis/analyze` | Multipart `.docx` or text-based `.pdf`; extraction and deterministic case/statute citation analysis. The optional `resolve=true` invokes local read-only resolution. | Returns extracted source text, evidence rows, offsets, and summary. No canonical case, citation, chunk, embedding, or upload record is created. Successful responses set `no-store` / `no-cache`. |
| `POST /live-analysis/resolve` | Same supported file types; performs local read-only case/legislation matching. | Returns the source text and evidence plus resolution data; no upload record. Successful responses set `no-store` / `no-cache`. |
| `GET /deidentify` | Serves the de-identification page. | The page response also uses the existing no-store headers. |
| `POST /api/deidentify` | Accepts pasted text or `.docx`, `.pdf`, `.txt`, or `.md`; optional local spaCy-based name detection and deterministic patterns. | Returns redacted text, warnings, detected/kept names, and a key containing originals. No application database write. Response is no-store. |
| `POST /api/reidentify` | Accepts text or supported upload plus the user's key. | Returns restored text and warnings. The server does not retain the key or output in application storage; response is no-store. |
| `POST /api/deidentify/docx` | Accepts text already supplied to the endpoint and a filename. | Builds a DOCX in memory and returns it with a sanitized download filename and no-store headers. |

The re-identification key is sensitive: it contains the original strings mapped
to placeholders. It is returned to the caller, not saved by the reviewed
service. The caller must protect the downloaded/copied key and any original or
redacted document they retain.

The live-analysis frontend and API exchange the original extracted text so the
temporary reader can display it. The inspected handlers do not write uploaded
text to the application's case database or an application-managed file. This
does not rule out temporary multipart spooling, browser/proxy storage, or
deployment-level request logging.

## Storage, caching, logging, errors, and external services

- **Application persistence:** No upload/case/chunk/citation database write or
  application-owned upload file is performed by the reviewed flows. Local
  resolution reads existing case and legislation data only.
- **Temporary storage:** Routes call `UploadFile.read()`; multipart parsing is
  handled by Starlette and can use a spooled temporary file. The reviewed
  application code does not establish that all upload bytes remain exclusively
  in RAM from network receipt through cleanup. Proxy, server, container, and
  filesystem retention policies were not inspected.
- **Caching:** Live Analysis previously lacked explicit response cache
  directives despite returning the full source text. Both successful POST
  routes now set `Cache-Control: no-store` and `Pragma: no-cache`. The
  de-identification page and its API already use these headers. This cannot
  prevent a caller from saving data or replace transport/deployment controls.
- **Logging:** No reviewed handler or transformation explicitly logs uploaded
  document text, redacted text, names, or keys. The name-model loader logs a
  model-load exception, not document content. Web-server, reverse-proxy,
  hosting, crash-reporting, and request-body logging settings are outside this
  source review.
- **Errors:** Invalid filename/type, empty input, and over-limit input produce
  validation errors. Non-`ValueError` parse failures in Live Analysis return a
  generic 422 message; other `ValueError` messages can be returned as supplied
  by validation or the parser. De-identification wraps non-validation upload
  parse failures in a generic message; malformed keys return validation
  errors. No inspected error response intentionally includes document text,
  but runtime/framework logging configuration was not tested.
- **External services:** Citation/statute extraction, case resolution, and name
  detection use local code/data; the spaCy model is loaded locally when
  installed. The reviewed paths make no outbound model, OCR, or authority
  lookup request. Legislation/source URLs may be included in response data;
  the server does not fetch those URLs in these paths. A user may follow a
  displayed link in their own browser.

## Hostile files and resource limits

The application validates supported filename suffixes, selected MIME types,
empty content, and a maximum compressed/request file length of 10 MiB before
document parsing. The analysis parsers are `python-docx` and `pypdf`; DOCX uses
the OOXML package reader and PDFs are read from in-memory bytes.

The limit and parser behavior have important boundaries:

1. In both Live Analysis routes, `await file.read()` happens before
   `validate_live_analysis_upload` checks the 10 MiB length. De-identification
   similarly reads the whole file before `text_from_upload` checks its limit.
   Thus the application-level limit does not cap bytes read by the handler, and
   this review did not verify a proxy/server request-body cap.
2. The DOCX byte check limits the compressed upload, not the expanded ZIP
   member sizes, count, or total extracted text. No explicit zip-bomb
   expansion, nesting, or parser-time budget was found in the reviewed code.
3. No explicit PDF page-count, text-output, CPU, or memory budget was found.
   Live Analysis extracts selectable page text; scanned/image-only PDFs have
   no OCR and can yield little or no useful text. The de-identification PDF
   path rejects documents with very little selectable text per page.
4. The de-identification text-form input has no application-level character
   limit in the reviewed route. DOCX/PDF/TXT/MD upload bytes use the 10 MiB
   check, but that check also occurs after the file is read.
5. Malformed or unsupported inputs are rejected or mapped to 422 responses;
   hostile malformed/oversized/zip-bomb fixture testing was not part of the
   focused suite and no claim of comprehensive parser hardening is made.
6. The parsers extract document text, not arbitrary embedded content.
   Live-analysis DOCX extraction iterates document paragraphs; it does not
   enumerate every Word table, header/footer, text box, comment, attachment, or
   embedded object. The de-identification DOCX extractor includes body
   paragraphs/tables and selected headers/footers, but is not a complete
   extractor for every OOXML part. PDF extraction uses page text and does not
   fetch embedded links or attachments. External hyperlink targets are not
   followed by the reviewed server code.

These limits mean the byte threshold is a useful input check, not a promise
against memory/CPU exhaustion. Enforcing streaming request limits and
decompressed/page/output budgets should be a separate, tested hardening task;
no parser or limit redesign was included here.

## De-identification coverage and known misses

De-identification is a review aid, not a guarantee that a document is anonymous
or safe to disclose. `deidentify_text` combines caller-supplied names/details,
pattern matches for common identifiers and personal details, and optionally
local spaCy name detection. It reports unmatched typed names and some residual
occurrences; the person reviewing the document remains responsible for
checking the output.

Known coverage boundaries visible in the implementation:

- Automatic name detection is optional and model-dependent. If the spaCy model
  is unavailable, the response warns that only user-entered names are hidden.
  Name recognition is heuristic and can miss spelling, casing, transliteration,
  uncommon-name, single-word, OCR, or layout variations.
- Person names are not guaranteed to be found when they appear outside the
  extraction scope of the uploaded format (for example, some DOCX text boxes or
  embedded content). PDF extraction only sees selectable page text.
- Pattern rules cover specified common forms (email, phone, several Canadian
  identifiers, address/postal formats, dates, and ages); unusual formatting,
  unlabelled identifiers, indirect identifiers, and facts that identify a
  person by combination can remain.
- Countries, employment details, and place names are intentionally retained to
  preserve claim context. Names of parties in cited cases and decision-makers
  may also be retained; a caller can type names to hide and use the
  never-hide option to control the automatic detector.
- The tool produces placeholders and a restoration key. Re-identification
  restores originals by design; sharing the key or restored text defeats the
  redaction.

The tests cover representative identity patterns, exact restoration, warning
behavior, selected name-detection cases, and extraction examples. They do not
establish complete PII recall or provide an exhaustive adversarial name,
address, identifier, OCR, or layout benchmark.

## Changed issue and evidence

The clear, small issue fixed for this review was missing cache-control headers
on the two Live Analysis success responses. They now use the same
`Cache-Control: no-store` and `Pragma: no-cache` values as de-identification
responses, while retaining `LiveAnalysisResponse` validation and response
payload shape.

Focused validation:

```text
python -m pytest -q tests/test_live_analysis.py tests/test_deidentify.py
22 passed, 1 warning
```

The warning is an upstream Starlette `BlockingPortal` deprecation. This review
did not run hostile-file fuzzing, a browser/proxy retention audit, a deployment
access-control test, or the full test suite.

## Follow-up boundaries

1. Treat Live Analysis and de-identification routes as sensitive: ensure
   deployment-level authentication/access control before exposing the app. The
   current app middleware's no-index behavior is not route authentication; see
   `docs/CONFIGURATION_REFERENCE.md`.
2. Consider a separate bounded upload-hardening task for request-body limits
   before full reads, DOCX expanded-size limits, PDF page/output limits, and
   adversarial parser fixtures.
3. Continue manual review of de-identified output and keep the restoration key
   separate from any redacted document intended for sharing.

## Evidence sources

- `backend/live_analysis.py`: accepted types, 10 MiB check, DOCX/PDF extraction,
  returned full text, and local resolution.
- `backend/deidentify.py`: redaction patterns, overlap handling, warnings,
  restoration key, supported formats, and upload byte check.
- `backend/deidentify_names.py`: local spaCy loading, heuristic detection, and
  fallback warning.
- `backend/routes.py`: Live Analysis and de-identification route behavior,
  response headers, error handling, and upload reads.
- `backend/main.py` and `docs/CONFIGURATION_REFERENCE.md`: no-index middleware
  and documented access-control limitation.
- `tests/test_live_analysis.py` and `tests/test_deidentify.py`: focused route,
  extraction, redaction, and restoration evidence.
