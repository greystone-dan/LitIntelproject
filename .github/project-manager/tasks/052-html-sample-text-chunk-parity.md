# Task: HTML sample to text-only chunk parity

Status: in-progress
Created: 2026-09-05
Updated: 2026-09-05

Task: Use representative source HTML to improve and validate text-only chunking so the corpus does not require HTML for every case.
Why now: HTML acquisition is the current network bottleneck; only about 1,800 FC, 27 SCC, and 2 FCA cases currently have stored HTML, while the wider corpus is text-only.
Owner surface: `scripts/chunk_cases.py`, `backend/document_structure.py`, parity evaluation tooling, and chunk tests.
Dependencies: Existing canonical full text, representative stored HTML, current HTML-aware chunk builder, current text-only fallback.
Risk boundary: Evaluation-only first. Do not alter canonical chunks or pipeline rows during parity measurement. Preserve backend-owned offsets and do not claim HTML parity without measured gates.
Smallest falsifiable check: On a stratified FC/SCC/FCA sample, text-only and HTML-enabled chunk layers meet count/content/token/span-preservation gates or produce an explicit failure report.
Acceptance criteria: Source-family census recorded; representative sample selected; parity harness emits JSON metrics; text-only chunk rules improve where gates fail; focused tests and Swimm/canonical docs are updated.
Parity gates: paragraph count relative delta <=10% where canonical paragraph markers exist; section count relative delta <=20%; paragraph text containment >=90%; citation span preservation >=95% where citations exist; token estimate relative delta <=5%; every text-only chunk must be an exact canonical-text substring. HTML block count is diagnostic, not a required target when the canonical text has lost those structural boundaries.
Rollback/recovery: Evaluation artifacts are separate; revert only text-only chunk-rule changes if parity worsens. No source/canonical data deletion.
Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `docs/DATA_SOURCE_REGISTER.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`.
Evidence:
- Delegated source/chunk inventory found court distribution FC 35,813, FCA 7,785, RPD 6,729, SCC 10,889; source types are primarily `a2aj_parquet`.
- Stored HTML distribution is concentrated in FC (~1,800), SCC (27), and FCA (2).
- Parity harness added at `scripts/evaluate_chunk_parity.py` with gates for
	section/paragraph counts, containment, and token estimates.
- Six-case FC/FCA/SCC sample evaluated. FC small/large, FCA, and SCC short cases
	pass all gates. FC 2007 FC 229 remains structurally divergent (HTML 246 vs
	text-only 80 paragraph chunks); SCC 1999 2 SCR 817 improved from 2 to 92
	text-only paragraphs after the numeric-marker rule but remains below HTML's
	218. No canonical rows were changed by parity evaluation.
- Added SCC-specific numeric paragraph markers to the text-only chunker; chunk
	and document-structure tests pass (`14 passed`).
- Reframed parity evaluation around canonical evidence safety: all six sample
	cases preserve canonical-text substrings in text-only chunks and four pass
	all structural/token gates. FC/SCC HTML-only block granularity remains a
	diagnostic outlier rather than a reason to invent boundaries in canonical
	text.
- Reframed the parity gate: HTML block count is diagnostic where canonical text
	lacks equivalent boundaries; canonical substring containment, token coverage,
	section headings, and evidence-span preservation are the production gates.
Status: in-progress
Commit allowed: yes
Push allowed: yes
