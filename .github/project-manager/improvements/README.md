# Project Manager Improvements

Store evidence-backed recommendations for improving the project-manager prompt,
workflow, delegation, documentation, or validation here.

Each recommendation should state:

- Observed issue or missed opportunity
- Evidence
- Proposed change
- Expected value and risk
- Decision and date

Do not modify the agent instructions automatically as a side effect of ordinary
feature work. Adopt recommendations through an explicit, reviewed change.

## 2026-10-04 — Offline validation preflight

- Observed: issue #138 found dotenv/database access during test collection,
  raw-connection guard bypasses, and external tokenizer/model requirements.
- Evidence: [endpoint pass](../../../docs/reports/endpoint-performance-pass.md);
  guard rejection tests and full-suite results distinguish safe execution from
  green acceptance.
- Recommendation: preflight imports, direct/raw DBAPI paths and external resource
  caches before full-suite runs; preserve exact CI deselects and test offline
  guard failure paths. Do not substitute extra skips or fake providers for
  failed acceptance.
- Value/risk: prevents accidental application DB access and wasted validation
  cycles; isolation must still permit disposable fixtures/coverage files.
- Decision: guard/preflight improvements implemented; unrelated model/tokenizer
  test repair deferred to its owner. No agent instructions changed.
