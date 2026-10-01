# Task: Acquire SCC HTML canary

Status: complete
Created: 2026-09-30
Updated: 2026-09-30

Task: Acquire and validate a bounded five-case SCC official HTML canary for cases missing stored source HTML.

Why now: SCC cases have official source URLs and extracted text, but only 27 of 10,893 canonical SCC records currently store HTML. The user authorized starting the HTML acquisition task.

Owner surface: `scripts/acquire_case_html.py` and canonical `Case.source_html` provenance updates.

Commit allowed: yes
Push allowed: yes

Dependencies: SCC official decision pages, canonical SCC source URLs, HTML validation/sanitization, and existing source provenance schema.

Risk boundary: SCC only; maximum five cases; missing-HTML cases only; official allowlisted host; no text replacement, no chunk rebuild, no embeddings, no non-SCC acquisition, and no deletion.

Smallest falsifiable check: A five-case dry-run must report validated HTML or explicit quarantine reasons before any write.

Acceptance criteria:

- The canary selects only SCC cases without stored HTML.
- Official HTML responses pass citation/content validation or are quarantined with reasons.
- If approved by the dry-run result, only validated snapshots are stored with hashes and provenance metadata.
- Existing canonical text and source identity remain unchanged.
- Validation and documentation record the exact result.

Docs/generated references: `OVERNIGHT.md`, `docs/DATA_SOURCE_REGISTER.md`, `.swm/4.9nn3id9f.sw.md`.

Rollback/recovery: Remove only canary HTML snapshots and their `source_html` provenance rows if the bounded result is invalid; preserve quarantine evidence. Do not delete case records or replace canonical text.

Evidence: SCC-only canary dry-run scanned 5 cases, validated 1, and quarantined 4 with `decision-content-not-found`; no dry-run writes occurred. The apply run stored 1 validated snapshot and quarantined the same 4 cases. Case `47505` (`[1992] 1 SCR 866`) now has stored sanitized HTML and a dedicated `source_html` provenance row. Structural mapping measured `0.6828` confidence across 100 blocks, below the SCC automatic mapping threshold of `0.85`.

Files changed: `.github/project-manager/tasks/scc-html-canary.md`, `scripts/acquire_case_html.py`, `docs/DATA_SOURCE_REGISTER.md`, `.swm/4.9nn3id9f.sw.md`.
Delegated work: None; bounded source acquisition is manager-owned.
Focused validation: `scripts/acquire_case_html.py --court SCC --missing-html-only --limit 5 --workers 1 --per-host-delay 2 --dry-run` returned `scanned=5 ready=1 applied=0 quarantined=4`; apply returned `scanned=5 ready=1 applied=1 quarantined=4`. Provenance repair restored the A2AJ text hash and created a separate HTML source row. HTML acquisition tests and `py_compile` passed.
Residual risk: Four older SCC pages failed citation-content validation, and the one validated page mapped below the SCC threshold. Existing SCC text remains authoritative; no broader acquisition or chunk rebuild was run.
Next bounded task: Review SCC page variants and improve/measure structural mapping before acquiring additional HTML.
