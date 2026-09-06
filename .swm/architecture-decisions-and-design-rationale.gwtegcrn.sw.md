---
title: Architecture Decisions and Design Rationale
---
# Architecture Decisions and Design Rationale

This walkthrough records why important product and architecture choices were
made. `SYSTEM_REFERENCE.md` remains the current-state authority; this document
preserves rationale, alternatives, consequences, and revisit triggers.

## Decision Record Format

```text
Decision:
Context:
Options considered:
Chosen approach:
Why:
Consequences:
Evidence:
Revisit trigger:
```

## Current Design Decisions

### Separate extraction from resolution

- **Decision:** Extract case citations and statute references first, then run
	case-to-case target resolution as a separate local pass.
- **Why:** An occurrence can be valid and useful even when no local target is
	resolved. Separation preserves QA precision and avoids conflating extraction
	coverage with library coverage.
- **Consequence:** `citations` and `statute_references` remain distinct layers;
	target links and graph metrics are derived afterward.
- **Revisit trigger:** A replacement resolution architecture demonstrates higher
	accuracy without changing stored occurrence evidence.

The V2 Pipeline benchmark confirmed the operational value of this boundary: the
pre-fix N+1 target lookups caused the slow run, while extraction-only citation
rebuild completed 50 cases in 23 seconds. Same-document short-form anchors are
stored as occurrence provenance; target resolution remains a later corpus pass.

The completed optimized text-only run processed 50,327 records, completed
43,598, excluded 6,729 malformed or hostless source links, and quarantined none.
Against the matching baseline cohort, chunks rose 12%, case citations 30%,
statutes 65%, and V3 tag occurrences 23.1x. Offset auditing found no malformed
citation/statute spans or missing V3 tag offsets. Because extraction-only rows
remain unresolved and unassociated with chunks, this evidence supports the
extraction contract but does not yet certify graph metrics or chunked reader
highlights; that requires the separate resolution/layer-association pass.

### Preserve backend-owned evidence locations

- **Decision:** Source/chunk offsets and provenance are authoritative; browser
	code renders them but does not invent replacement offsets.
- **Why:** Researchers need a reproducible path from a visible highlight back to
	stored source evidence.
- **Consequence:** Formatting changes must not silently redefine evidence spans.
- **Revisit trigger:** A new evidence representation supplies equivalent,
	testable source lineage.

### Prefer deterministic legal extraction as the baseline

- **Decision:** Keep deterministic citation, statute, metadata, and taxonomy
	extraction as the release baseline; evaluate embeddings or language models as
	additive signals.
- **Why:** Deterministic rules are inspectable, testable on exact spans, and
	suitable for bounded regression checks in legal research.
- **Consequence:** New model signals must preserve provenance and cannot silently
	replace established evidence layers.
- **Revisit trigger:** A benchmarked alternative improves accuracy and
	explainability at an acceptable operational cost.

### Use `/data-explorer` as the active research workflow

- **Decision:** Keep the inline reader and research navigation in Data Explorer.
- **Why:** One active workflow reduces duplicated UI behavior and makes browser
	validation meaningful.
- **Consequence:** `/case-reader` remains a compatibility redirect and
	`/citation-pass` remains a QA surface.
- **Revisit trigger:** A replacement workflow has equivalent coverage and a
	migration plan for existing links.

### Preserve source HTML and derive structure before chunking

- **Decision:** Preserve acquired source HTML separately and derive a sanitized
	display copy plus a structural document model and canonical plain text from
	it. Do not reconstruct structure from plain text after the fact.
- **Why:** HTML structure can identify headings, paragraphs, lists, tables, and
	captions for better chunk boundaries, while the sanitized copy can support a
	readable Case Reader.
- **Consequence:** `backend/document_structure.py` provides versioned blocks,
	HTML paths, canonical text ranges, and a safe display copy. Integration into
	chunking and evidence rendering must carry the plain-text-to-source mapping.
- **Revisit trigger:** A full mapped pipeline proves stable paragraph boundaries,
	exact citation/statute/tag spans, and source-preserving reader rendering.

The first implementation slice is intentionally pure and evaluation-only. It
does not change existing chunks, citations, statutes, tags, or database rows.

The canonical case-processing contract now defines three chunk layers: one
`full_case` row containing the complete normalized case text, heading-aware
`section` rows for larger legal units, and fine-grained `paragraph` rows for
evidence and retrieval. The former `legacy` fixed-size chunks remain a
compatibility format only.

A bounded sample rebuild confirmed that generated section and paragraph rows
remain exact substrings of canonical case text. The same sample showed that
preserved source HTML can have a different metadata/text representation than
`full_text`; HTML-to-canonical mapping must be explicitly aligned before
HTML-derived boundaries are used for evidence offsets or production chunking.

The mapper now performs deterministic sequence alignment and records per-block
confidence. On the Roghangar sample, all 115 HTML blocks mapped with document
confidence `0.991`. This supports future HTML-informed chunking, but production
evidence must require an explicit confidence threshold and fallback for unmapped
blocks.

The reader evidence contract exposes derived `layer_spans` so one citation can
be located in the full-case, section, and paragraph layers. The original stored
offset remains authoritative; layer spans are derived navigation metadata and
must be validated against the containing chunk text.

The operational chunk builder now uses the mapped HTML path when document
confidence is at least `0.98`: top-level headings define larger section chunks,
and mapped leaf blocks define paragraph-level chunks. It retains canonical text
as the chunk content and falls back to the existing text-based chunker when HTML
is absent or confidence is insufficient.

The cross-court canary confirms that FC, FCA, and SCC item pages use the same
iframe delivery pattern but have different wrappers and metadata. FCA mapped at
`0.9961`; FC varied from `0.957` to `0.9939`; SCC mapped at `0.8835` because of
substantial navigation and metadata structure, although 267 of 353 blocks mapped
strongly. The global gate remains unchanged until source-specific body scoping
and paragraph rules are tested.

SCC-specific rules are now tested: `.documentcontent` is flattened to numbered
paragraph elements after the first decision block, Roman-numeral divisions form
larger sections, and a `0.85` source-specific mapping gate admits the body while
the FC/FCA `0.98` gate remains unchanged. Suresh produced 1 full-case, 5
sections, and 176 paragraphs with exact canonical-text containment.

### Converge inventory and live-document processing

- **Decision:** Maintain separate source adapters for canonical inventory cases
	and user-provided live documents, but converge both paths on the same
	structural document model, canonical text mapping, three chunk layers, and
	citation/statute/tag extraction contracts.
- **Why:** Inventory sources commonly arrive as stored HTML, while live users
	may provide DOCX or PDF documents with different formatting structures. The
	product must preserve formatting-aware chunking and downstream evidence in
	both workflows without duplicating domain logic.
- **Consequence:** The live path must extract headings, paragraphs, lists,
	tables, page/section boundaries, and source mappings before downstream
	analysis. It must remain ephemeral by default and must not silently write to
	canonical case tables.
- **Revisit trigger:** A shared intermediate representation cannot preserve
	sufficient provenance or exact offsets for one supported input family.

## Open Decisions Requiring Evidence

1. How to improve citation truncation and partial-reference extraction without
	 reducing exact-span precision.
2. Whether a hybrid taxonomy-plus-embedding tagger outperforms deterministic
	 tagging on a labeled immigration-law set.
3. Which citation-context and purpose labels provide useful researcher signal
	 without implying unsupported legal conclusions.
4. What quality and performance thresholds should block a release.

## Governance Rule

Architectural decisions should be updated when the implementation, evidence, or
revisit trigger changes. A task record captures execution; this document
captures durable rationale.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBTGl0SW50ZWxwcm9qZWN0JTNBJTNBZ3JleXN0b25lLWRhbg==" repo-name="LitIntelproject"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
