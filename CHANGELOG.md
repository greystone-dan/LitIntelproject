- Reframed the forward roadmap around a demo-first product milestone: issue and
	case-type discovery, a coherent search-to-reader-to-authority journey,
	usability polish, and curated browser-validated demo scenarios. Corpus-wide
	quality and advanced intelligence work is now explicitly deferred except for
	demo-safety fixes.
# Unreleased

- Issue #281: added migration `0039_citation_refinement` and four standalone
  refinement-storage models, preserving base occurrence fields while adding
  version/step/confidence metadata, statute grouping, paragraph links and
  per-case status. Only absent tables are created; downgrade preserves them.
  No runtime refinement wiring or data migration. DB-free tests cover repeat
  upgrade, pre-existing preservation, model/field/index/FK parity and the new
  single migration head. Added an explicit disposable PostgreSQL-gated test for
  isolated fresh upgrade, reflected schema parity, actual repeated upgrade
  function calls, and no-op downgrade/re-upgrade preservation with final cleanup.
  Latest DB-free focused checks: 15 passed, 2 PostgreSQL-gated tests skipped,
  2 SQLite-writing tests deselected. Earlier CI-filtered full suite:
  2,856 passed, 5 skipped, 3 deselected, 1 xfailed, with 2 unrelated tokenizer
  tests failing because the external tiktoken download host could not resolve.
  External PostgreSQL access and dotenv reads were blocked during validation;
  generated-reference checking passed. No deployment or live migration was run.

- Live Analysis now opens your own memo, factum or decision (DOCX, text PDF, or pasted text) in the case reader's markup mode, in the site's own page and style. Case citations and statute references are marked in the text with margin notes, hover cards and the Peek panel; a cited case that is in the library shows the cited paragraph's stored text, and a statute reference shows the stored provision text. Case citations written as a case name followed by a neutral or SCR citation ("Vavilov, 2019 SCC 65 at paras 10-11") now match the library by that citation, where before only the case name could match. The document is read in memory, never stored, and no model is called. Headings and paragraph numbers in your own text are worked out from line shape (a heuristic). Outcome, judge, discussion units and tags are not shown for your own text. No schema or data change.
- Markup mode: the citation hover card and the Peek panel now show an "In this case" line ("Cited at ¶[14] and ¶[15] (pinpoint ¶7)"), read from where the citation sits in the open decision. No data or schema change.
- Markup: the Citations layer in the Margin layers panel is always selectable when the case has any citation, and its count includes citations whose case is not in the library (they stay out of the margin until clicked).
- Markup mode: citation notes, the hover card and the Peek panel now show the text of the pinpoint paragraph ("¶[34] of Strachn") from the stored text of the cited case, trimmed with a "Show full paragraph" toggle. They show it only when the stored text really is that paragraph; otherwise they say plainly that there is no pinpoint, that the pinpoint was not found in the stored text, or that the case is not in the library, and no text is invented. The reader data now picks the narrowest stored chunk for a pinpoint and, for coarsely chunked decisions (for example Dunsmuir), reads the paragraph from the stored decision text (at most 12 cited cases per request). No AI calls, schema or data writes.
- Markup mode: bare case names and short forms that are highlighted in the text but not matched to a stored case (for example "Horvath v. Canada") now respond to hover, click and Shift-click Peek like other citations; they show "Not in the library yet" and stay out of the margin and the Word export until opened. A render queued while switching cases no longer throws. Margin connector lines now start at the end of their own citation or statute text (a dot, then a leader under that line), so two references on one line no longer share a start point. The potential legal-development notice is hidden in markup and revealed by a "Legal-development notice" pill in the header row. No data or schema change.
- Added the opt-in `openai_compatible` `/research` chat provider using the
  OpenAI SDK custom base URL and `CHAT_BASE_URL`, optional `CHAT_API_KEY`,
  `CHAT_MODEL`, and `CHAT_TIMEOUT_SECONDS`. The provider contract exposes
  context, output-token, and JSON-mode capabilities; the route uses provider
  context/token limits. Enhanced local mode accepts only localhost/private
  compatible endpoints, hosted mode rejects local/private URLs, and off mode
  still stops before provider construction. OpenAI and native Ollama remain
  supported.
- Case pages: the unfinished reader tools are hidden by default. The Quick summary, Extracted case summary and selected-passages summary cards, the case structure and case summary buttons, paragraph assessments and the “Similar paragraphs” buttons only appear after switching on “Show experimental” (at the top of the reader, and in the Markup toolbar); the choice is remembered in this browser. When shown, the Quick and Extracted summary cards start closed (one line each, with an arrow) and keep their state while you switch between Formatted and Markup. No data or schema change.
- Added stored-data-only decision comparison at `GET /compare` and
  `GET /api/compare`, accepting case IDs or stored citations. It displays fact
  and outcome provenance, separate tags/statutes/authorities, shared and unique
  signals, stored authority pinpoints, and directional cross-citations; unknown
  decisions and self-comparison receive clear errors. Inputs above 512
  characters fail closed before ID or citation parsing. The reader adds a
  prefilled “Compare with…” link. The pre-existing `/case-compare` page and
  `/cases/compare` JSON endpoint remain separate and available. No AI, schema,
  or data writes. Also removed a redundant whitespace quantifier from reported
  citation-year parsing; parenthesized reporter-year citations retain their
  normalized form with repeated whitespace.
- Added an additive read-only `GET /api/cases/{case_id}/summary-card` projection
  and collapsed formatted-reader card. It shows stored case/outcome facts,
  separate statute and active-tag layers, and up to three exact numbered
  passages selected by disposition evidence, later stored pinpoint counts, and
  an explicit standard-of-review statement. Missing fields are omitted; long
  passages retain sentence boundaries and link to their source paragraph. No
  AI, writes, schema changes, or live-data access. Focused summary-card,
  reader-keyboard/print, JavaScript syntax, documentation-inventory, and
  generated-reference checks passed.
- Markup mode now follows the mockups more closely. New Acts / statutes layer (margin notes with the Act, pinpoint, stored provision text or an honest “not stored”, and a link to the Act); header pills for outcome, judge and file number; short margin pill names (“Vavilov 2019 SCC 65”); citation cards with a paragraph badge, “also cited at” and Open / Pin; judge card with Open judge profile; outcome card with Show paragraph; unit pills named from the section heading; Layers popup with counts, “N of M”, Show all layers and Reset; a By-topic grouped view (Reading order / By topic, Fold all / Unfold all); a right-edge minimap; annotated print with numbered markers and numbered margin comments. Read-only on data already loaded, no AI, no schema change.
- About page refresh and a Changelog view. The About overview was audited against the repository: counts at the top
  now read live from `/api/about/stats`, unverifiable figures (sample percentages, AI paragraph counts, test scores,
  old test and line counts) were removed or restated, the AI wording now says the site runs without AI, and a
  "What has been added recently" section was added. A new Overview / Changelog switch in the About tab shows a
  timeline (newest first, date headings, theme filter) built from `data/changelog/changelog.json`, which
  `scripts/build_changelog.py` generates from hand-written entries plus GitHub merged PRs and commits
  (`--refresh` pulls them; `--uncovered` lists merged PRs with no entry). No network or AI at view time.

- Paragraph cited-by batch job made safe to run next to the live site. It now lowers its own process
  priority (including on Windows), uses one database connection with server-side statement, lock and
  idle-in-transaction limits, commits one short transaction per small batch, rests at least four times as
  long as it worked, can watch the site (`--health-url`) and back off when it is slow, has a CPU budget, a
  stop file (`stop_cited_by.txt`) and a database-error cutoff, and no longer scans the whole citations table
  to find pending work. New `backend/batch_safety.py` and `backend/paragraph_cited_by_runner.py`; the script
  is a thin wrapper. No schema change, no AI.
- Markup mode: Export to Word and private notes. "Export to Word" downloads the
  decision with every margin note that is switched on (citations anchored on the
  citation itself, discussion units, outcome, judge, cited-by, my notes) as real
  Word comments, with highlighted paragraphs kept. Private notes and highlights:
  click a paragraph number to write a note or highlight the paragraph; they are
  saved in this browser only, show in the margin (inline under the paragraph on
  phones) and travel into the Word file. New route `POST /cases/{id}/markup-export`
  typesets what the browser sends and stores nothing. Also fixed: notes could sit
  hundreds of pixels from their paragraphs on first open because the reader adds
  content after first paint; they now re-place themselves when the text height
  changes. No AI, no schema change.
- Added Alembic revision `0037_cases_docket_number`, which idempotently adds
  nullable `cases.docket_number` (`String(255)`) and its model-declared index.
  Added mocked preservation/idempotency coverage and an explicitly gated
  PostgreSQL migration-from-zero schema comparison test.
- Phone layout, second pass: Site Architecture no longer overflows the screen, wide tables
  scroll inside their panel, the judge comparison form and the statute viewer form fit
  and stack on phones. CSS only.
- Phone layout fixes: the search page stacks its field and buttons with 16px text and
  scrolling filter chips; the case reader header no longer sits under its view
  buttons and the reader scrolls as one page; the yellow overruling-risk notice
  folds behind one tappable line on phones so it cannot push the decision off
  screen; Markup mode's toolbar is one row (Find, Topics and More open on tap),
  the Peek panel is a bottom sheet, and the hover card is off on touch screens.
  CSS and display logic only: no AI calls, new endpoints or schema changes.
- Paragraph "cited by" batch job (not run on production): `scripts/build_paragraph_cited_by.py`
  reads stored citation occurrences and, for each cited paragraph, stores which
  cases cite it, how often, and the signal phrase beside the citation (followed,
  distinguished, see, quoted, ...). Two additive tables (migration 0036). It is
  resumable, runs at low priority, and writes nothing without `--apply`. The
  Markup margin and Peek read the stored rows when they exist and fall back to
  the old counts otherwise. No AI. See `docs/PARAGRAPH_CITED_BY.md`.
- Markup mode second build, using only stored data: hover card on citations;
  Peek panel (floating or docked, stackable, shows the cited paragraph when the
  authority is in the library and says so when it is not); tag display modes
  (Off, Underline, Tint, Bubbles); topic chips from sub-theme key terms with a
  "show only selected" fold view; case-info drawer polish; keyboard use for
  citations and the toolbar; print re-layout; and a find-box focus fix. No AI,
  new endpoints or schema changes.
- Added **Markup mode**, a third case-reader view (button beside Formatted/Chunk
  breakdown). The decision runs full width with notes in a right margin: case
  citations with pinpoint text, discussion units and sub-themes, verified
  outcome (labelled unverified when no disposition passage is stored), judge,
  a cited-by gutter, soft tags, topic bands, outline, find-in-case, per-layer
  Off/Markers/Open controls with expand/collapse all, and annotated print. It
  only reads the already-loaded reader payload: no AI, no network calls, no
  schema changes. Existing readers are unchanged.
- Added a read-only `GET /api/overruling-risk/{case_id}` indicator using an
  editable, lawyer-review seed list, with direct matches and stored resolved
  citation links, source/rationale/assignment details, counts, and chronology
  dates. The active Data Explorer reader adds a cautious “may be affected”
  banner; no memo output or database schema changes. Extension guidance is in
  [`docs/reports/overruling-risk.md`](docs/reports/overruling-risk.md).
- Added a shared embedding-provider interface with a disabled default, lazy
  OpenAI client wrapper, and cached local SentenceTransformer implementation.
  Search/query and case-ingestion embeddings now respect `ENHANCED_AI_MODE`:
  off makes no model/client calls, local mode rejects hosted embeddings, and
  hosted mode uses the selected provider. Provider dimensions and the 503
  missing-key / 502 provider-failure API contracts are preserved. Added
  fake-client/model tests and updated the architecture inventory, configuration,
  system reference, and Swimm maps. Python compilation and `git diff --check`
  passed; seven provider tests and nine targeted API/search/ingestion tests passed
  in an isolated dependency environment. All three generated references were
  current. No model downloads or database operations were performed.
- Moved the experimental research, citation-intelligence, contextual-authority,
  and discussion-unit prompts into header-versioned text files loaded through a
  shared backend registry. Exact prompt wording is guarded by golden snapshots.
  `/research` now returns additive `prompt_version` metadata; the bounded
  discussion-unit scripts include their prompt versions in request/output
  artifacts without changing model-facing prompt text.
- Added the centralized `ENHANCED_AI_MODE` gate (`off` by default; `local` and
  `hosted` require explicit opt-in). API search defaults to lexical; off mode
  downgrades explicit semantic/hybrid requests without embedding calls and
  exposes effective-mode metadata at the response. `GET /api/ai-mode` reports
  the setting, while `/research` returns HTTP 503 when enhanced mode is off.
  Local mode uses Ollama for generation and allows only local query embeddings;
  hosted query embeddings additionally require `QUERY_EMBEDDING_PROVIDER=openai`.
  Query embeddings remain disabled by default (`none`). The analytics Case
  Search UI and its SQL-backed CSV/Word exports remain unchanged. Focused
  AI-mode/API tests passed (76 total), and generated-document checks passed. The
  full CI pytest command completed with 1,631 passed, 4 skipped, 3 deselected,
  1 xfailed, and 2 tokenizer-cache tests blocked by unavailable network access.
- Added public `GET /health/live` and `GET /health/ready` probes while preserving
  the legacy `GET /health` response. Readiness reports database, vector
  extension, required-table, and configured-model endpoint status, and returns
  HTTP 503 when a required check fails. Probe results omit endpoint addresses
  and credentials. The 12 focused mocked health tests and generated-document
  check passed; no database or `.env` was accessed.
- Added issue-first outcome patterns to Judge Profile through lazy-loaded
  `GET /api/judge-profiles/{slug}/issues`, with a matching Federal Court-wide
  baseline, four explicit outcome categories, full denominators including
  unclassified decisions, and a minimum of 10 judge-linked decisions per
  displayed issue; lower-count issue labels stay hidden and their count is
  disclosed. This descriptive view does not rank judges or infer harshness.
  Focused judge/profile/UI checks passed (83 passed, 1 skipped), and a
  fixture-only Chromium interaction check passed. The exact CI-deselected full
  suite ran 1,254 passed, 2 skipped, 1 xfailed, and 3 deselected; 3 unrelated
  tests failed because `sentence-transformers` and `tiktoken` were absent from
  the temporary test environment. No model/tokenizer assets were downloaded.
- Added a visible Data Explorer **Download Word** control and the
  `GET /search/export.docx` endpoint, which preserve active analytics search
  filters and export up to 200 cases with citation/title/court/date/outcome
  columns and query/filter/date/count context; the response is no-store.
- Added a bounded in-process TTL cache for the About statistics, Federal Court
  activity analytics, and Judge Profile list reads. The cache defaults to ten
  minutes, supports `ANALYTICS_CACHE_TTL_SECONDS` configuration or disablement,
  keys by all parsed filters, and reports `X-Cache: hit|miss`.
- Added an independent non-blocking pull-request and weekly workflow for
  pinned Ruff (`E,F401`) and pip-audit checks, with a separate artifact for each
  result. The first baseline is recorded in
  [`docs/reports/baseline-lint-and-audit.md`](docs/reports/baseline-lint-and-audit.md).
  The required CI pytest command ran 1,032 tests successfully; three other tests
  failed while attempting to download external Hugging Face/OpenAI tokenizer
  resources, one was skipped, one xfailed, and three configured tests were
  deselected.
- Added centralized, environment-configurable upload and parsing limits for
  memo citation checks, Live Analysis, and de-identification. Upload reads stop
  at the configured limit; DOCX expansion/entry count, PDF pages, extracted
  text, and de-identification pasted text are capped with HTTP 413 limit errors.
- Added read-only `/issue-brief?tag=category:value` analytics and a standalone
  printable `/issue-brief-ui` with yearly outcomes, courts, resolved cited
  authorities, and reader links. Outcome percentages disclose the unclassified
  count and all-decision denominator; empty tags return an explicit empty brief.
- Added saved-search persistence and CRUD/alert routes, a standalone saved
  searches page, a Case Search action to save the current query and filters,
  and a bounded read-only-by-default alert checker. The new schema revision is
  chained from the latest existing Alembic head; standard search behavior is
  unchanged when no saved searches exist. Focused checks passed (63); the full
  CI-deselected suite had 991 passes and 3 unrelated failures because uncached
  Hugging Face and OpenAI tokenizer assets could not be downloaded.
- Added **Download CSV** to Case Search and `GET /search/export.csv`, carrying
  the active query, filters, and sort order into a maximum 1,000-row export
  with stable columns, UTF-8 BOM, spreadsheet formula escaping, and active
  Data Explorer case links. Focused export tests (3) and feature-tab tests (51)
  passed; generated documentation is current. The configured CI command ran
  982 passed, 3 failed, and 3 intentionally deselected; the three failures
  require unavailable Hugging Face/OpenAI tokenizer downloads.
- Simplified chunk-mode reading with continuous compact sections, hidden chunk
	numbering and character metadata, and citation/statute highlights that retain
	the surrounding judgment typography.
- Upgraded Case Search with bounded title/citation suggestions, keyboard
	navigation, explicit loading/empty/error feedback, a clearer legal-result
	hierarchy, and browser-validated desktop/mobile behavior.
- Improved the active Case Search interface with a clearer primary query row,
  grouped collapsed advanced filters, active-filter feedback, reliable Clear
  behavior, and responsive desktop/mobile layout without changing search
  parameters or result semantics.
- Retired the standalone Judge Outcomes tab and dedicated routes while keeping
	Judge Profile as the active judge workflow; updated the current UI contract
	and focused feature-tab coverage.
- Added a read-only judge identity reconciliation report covering stored judge
	values, profile links, invalid candidates, and provenance mismatches without
	changing canonical rows.
- Added the deterministic `Show case summary` reader projection with stable
	issue, positions, facts, law, reasoning, limitations, and disposition
	sections backed by existing evidence.
- Added an optional deterministic `Show case structure` layer to the active
	Data Explorer reader, projecting source-linked Discussion Units and
	sub-theme evidence without canonical writes or AI-generated conclusions.
- Added a separate deterministic `Show case summary` projection with stable
	issue, positions, facts, law, reasoning, limitations, and disposition
	sections plus explicit unavailable states.
- Shaded numbered paragraphs with incoming pinpoint citations in the inline
	Case Search reader and added a distinct-citing-case tooltip without changing
	citation offsets; paragraphs without matching pinpoint evidence remain
	unmarked.

# Change History

Document role: milestone and implementation delta log.
For current operating picture, pair this with `SYSTEM_OVERVIEW.txt` and `OVERNIGHT.md`.

## 2026-09-18 - Discussion Unit V1.4 evidence review checkpoint

- Completed the bounded 16-case Discussion Unit cohort expansion and the
	four-case external review packet refresh for cases `677`, `1093`, `1171`,
	and `18674`.
- Added the deterministic V1.4 explanation diagnostic that identifies spans
	with no explicit argument evidence as metadata or cue-free text without
	inventing a role or changing source spans, offsets, hashes, or runtime
	behavior.
- Preserved the V1.3 procedural-claim filtering, explicit advocacy recall,
	governing-rule precision gates, and local contrast gating. All packet
	regeneration runs were dry runs with zero canonical or contextual
	writes.
- Updated the system reference, Swimm walkthrough, and project-manager task
	record with the external findings, residual uncertainty, and rollback
	boundary.
- Verification: focused Discussion Unit, sub-theme, and inspector tests passed
	(24); bounded assertions passed for all 16 cohort cases; and
	`git diff --check` passed.

## Unreleased - Optimized V2 text-only enrichment review

- Completed the optimized non-SCC V2 run: 50,327 records processed, 43,598
	completed, 6,729 excluded for missing parseable allowed hosts, and 0
	quarantined.
- Compared the completed cohort with the compact baseline: chunks increased
	12%, case citations 30%, statute references 65%, and V3 tag occurrences
	23.1x.
- Read-only evidence auditing found no malformed citation/statute offsets and
	no V3 tag rows missing offsets.
- Recorded the remaining boundary: citation rows are extraction-only and remain
	explicitly unresolved without chunk association until the separate local
	target-resolution pass; HTML coverage was intentionally not expanded by this
	run.
- Verification: focused V2/citation suite passed 116 tests; generated API,
	schema, and script references are current.

## 2026-09-03 - Thematic intelligence in Data Explorer

- Added the ninth Data Explorer tab, Legal Themes & Statutes, with live theme
	definitions and statute-tag affinity exploration for provisions such as
	`34(1)(f)`.
- Added inline reader Precedents support backed by composite thematic clustering
	across stored tags, statute references, and case citations.
- Verification: contextual intelligence tests passed (7), feature/API tests
	passed (55), and the full suite passed (311).

## Unreleased - Standalone Live Analysis prototype

- Added an ephemeral `.docx` analysis surface at `/live-analysis` with in-memory
	paragraph offsets, deterministic case-citation and statute-reference evidence,
	and optional read-only local case resolution.
- Added upload validation, focused API/service tests, and navigation links while
	keeping analysis results out of the canonical database and ingestion pipeline.
- Added text-based PDF support with page-aware evidence and `pypdf`; scanned-PDF
	OCR remains outside the prototype scope.
- Optimized optional local citation resolution into one batched database read and
	removed the external CanLII fallback from the Live Analysis path.
- Split citation resolution into a distinct second request and broadened local
	matching to named and short-form references using case metadata.
- Verification: `81 passed` for the focused Live Analysis/citation test slice;
	touched modules compile cleanly.

## 2026-08-19 - Docket Number Field Backfill and FC Activity Cross-Reference

- Added dedicated `docket_number` column to the canonical `cases` table to
	capture Federal Court docket and file identifiers separately from legal
	citation semantics.
- Backfilled docket numbers across 35,902 decisions by scanning title, summary,
	and first chunk text for T-XXXX and IMM-XXXX-YY patterns: 35,451 cases
	populated (98.74% coverage), with 22,140 IMM-pattern and 13,308 T-pattern
	docket numbers recovered.
- Updated schema in `backend/database.py`, `backend/models.py`,
	`backend/ingestion.py`, and `backend/routes.py` to persist the field through
	create and merge workflows.
- Cross-referenced canonical docket_number values against FC Activity dataset
	citations: 18,911 exact matches (53.85% of canonical dockets with activity
	correlation), confirming reliable linkage for immigration cases up to 2022.
- Documented root causes of 16,204 non-matches: 13,308 T-pattern cases
	(non-immigration; activity dataset is 100% immigration-focused), 2,838
	IMM-cases dated >2022 (activity dataset ends 2022), and 55 coverage gaps
	within date range.
- Verified backward compatibility: all Federal Court import tests pass (9
	passed), ingest/metadata tests pass (10 passed).
- Updated `AI_HANDOFF.md` with docket field documentation and coverage metrics.

## 2026-08-17 - Six-tab intelligence interface

- Restored the primary one-page product shell with About, Case Search,
	Citation Intelligence, Judge Outcomes, Judge Profile, and Data Explorer tabs.
- Restored database-backed About statistics and Citation Intelligence API
	surfaces without changing citation extraction or resolution behavior.
- Added Judge Profile list/detail APIs using the existing canonical profile
	schema and preserved compatibility redirects for `/about`,
	`/citation-intelligence`, and `/judges`.

Note: entries on the same date may be grouped by feature theme rather than
strict execution order.

## 2026-08-12 - Advanced search, citation resolution, and isolated LotD import

- Promoted `/data-explorer` into the main research-facing UI with three tabs:
	advanced search, judge outcomes, and case data explorer.
- Added advanced search filters for cited authority, government outcome,
	decision outcome, judge, court, year, and minister/government party.
- Added minister dropdown sourcing through `/analytics/search/ministers` and
	sort controls for relevance, newest, oldest, and minister A-Z.
- Added a full-decision modal reader backed by stored citation rows rather than
	live re-extraction, preserving highlight spans while reducing open time for
	heavily cited decisions.
- Added per-case citation metrics in search results and reader payloads:
	total citation mentions, unique cited authorities, and linked target cases.
- Added local batch target-resolution scripts:
	`scripts/resolve_citation_targets.py` and
	`scripts/resolve_short_citation_targets.py`.
- Completed local target resolution for the current citation inventory:
	`1,492,628` citation rows total, `760,197` linked rows, and `31,944` unique
	linked target cases.
- Added isolated side-project dataset utility under
	`side_projects/luck_of_the_draw_iii/`, including cached Hugging Face parquet
	download, import into schema `lotd`, and workbook export.
- Built the LotD dataset successfully: `218,639` cases, `2,610,399` dockets,
	and workbook output at
	`side_projects/luck_of_the_draw_iii/output/luck_of_the_draw_iii.xlsx`.
- Verification performed through live database counts, focused API timing, and
	targeted importer validation rather than a new full `pytest -q` baseline.

## 2026-08-10 - Workflow consolidation and explainer alignment

- Declared Citation Pass as the canonical day-to-day workflow for current
	extraction stabilization work.
- Updated `README.md` with a single operating sequence (run API, review
	`/citation-pass`, fix deterministic extraction, validate, then push).
- Updated `DOCS_INDEX.md` so explainer-document authority and update order are
	explicit for patch cycles.
- Updated `AI_HANDOFF.md` to foreground the same primary workflow and reduce
	context switching across parallel notes.
- Repository checkpoint prepared for push from `main` to keep all work up to
	this point synchronized on GitHub.

## 2026-08-10 - Legacy system folder consolidation

- Added a top-level `legacy/` archive zone to reduce root-level clutter and
	make active-vs-legacy boundaries explicit.
- Moved `Case Law Bookmarks - August 2026.docx` into
	`legacy/artifacts/Case Law Bookmarks - August 2026.docx`.
- Added `legacy/README.md` with rules for what belongs in legacy paths.
- Updated `README.md` and `DOCS_INDEX.md` to point active work to Citation Pass
	and classify legacy paths as reference-only.

## 2026-08-10 - Legacy helper script archive

- Moved non-runtime, non-test-bound helper scripts from `scripts/` to
	`legacy/scripts/` to keep the active scripts surface focused.
- Added `legacy/scripts/README.md` documenting archived script intent and scope.

## 2026-08-07 - Deterministic layered extraction review

- Hardened the case-only citation layer for full case anchors, grounded
	short-form aliases, complete parenthetical spans, and exact Unicode-safe
	source offsets.
- Added independent deterministic statute/instrument extraction through
	`extract_statute_reference_matches()`; statute rows no longer depend on case
	extraction or participate in case-layer overlap selection.
- Expanded law coverage for Canadian Acts, Codes, Regulations, Rules, Orders,
	SOR/SI citations, international instruments, plural provisions, and bounded
	short-form section/article propagation from a named authority.
- Added precision guards against ordinary prose such as `In order` and bare
	judgment paragraph numbers inheriting a statute anchor.
- Added a deterministic metadata span layer backed by the Federal Court
	metadata extractor. Canonical text-derived fields retain exact offsets,
	confidence, and source provenance.
- Extended `GET /cases/{case_id}/citation-pass` with separate
	`live_extracted`, `live_statutes`, and `live_metadata` arrays and independent
	counts. The review UI renders case citations in orange, laws in green, and
	metadata in blue without reparsing backend spans.
- Added focused extractor and API regressions. Verified live code-point span
	integrity with zero errors: Febles has `168` case citations and `442` law
	references; Hasani has `48` case citations, `62` law references, and `10`
	metadata fields.
- Focused validation passes: `6` statute-layer tests, `1` citation-pass API
	test, and `1` metadata-layer test. The full suite currently stops during test
	collection on a pre-existing syntax error in
	`tests/test_fc_document_scraper.py:58`; no full-suite pass count is claimed.
- No AI/API extraction calls or broad cohort reprocessing were performed.

## 2026-08-02 - Direct A2AJ FC PDF ingestion with metadata tagging

- Added direct Federal Court ingestion mode in `fc_ingest` (`--a2aj-direct`)
	that bypasses discovery windows and pulls known FC item URLs from the
	A2AJ-backed canonical corpus.
- Added FC URL normalization so `item`, `document`, and PDF links resolve to a
	canonical Lexum item URL before ingestion.
- Extended SQLite staging `fc_pdfs` records to store searchable metadata beside
	the PDF blob: case title, decision date, neutral citation, docket, and
	`metadata_json`.
- Added in-place schema upgrade logic for existing `fc_pdfs` tables so old
	databases gain new metadata columns automatically.
- Added regression tests for direct mode behavior and PDF metadata persistence;
	focused FC ingest test baseline is now `12 passed`.

## 2026-08-03 - Citation intelligence expansion

- Added a global citation surprise feed at `/citation-map/surprises` with
	optional tag and year filters, balancing local citation intensity against
	global authority ubiquity.
- Added doctrine-shift analytics at `/citation-map/issues/shifts` to surface
	likely authority replacement patterns within issue/statute/legal-area slices.
- Added CSV exports for high-value analytics surfaces:
	`/citation-map/cases/{case_id}/authority-signals.csv`,
	`/citation-map/surprises.csv`,
	`/citation-map/authorities/landmarks.csv`, and
	`/citation-map/issues/shifts.csv`.
- Added route-level regression tests for new endpoint bounds, validation rules,
	and export headers; full suite baseline is now `110 passed`.

## 2026-08-03 - Citation hidden paths and inheritance chains

- Added hidden-bridge analytics at `/citation-map/paths/hidden` to rank
	intermediate cases that repeatedly connect source-target citation paths.
- Added authority inheritance chain analytics at
	`/citation-map/authorities/{case_id}/inheritance` to trace downstream
	citation adoption depth and edge strength.
- Added CSV exports for both new surfaces:
	`/citation-map/paths/hidden.csv` and
	`/citation-map/authorities/{case_id}/inheritance.csv`.
- Expanded citation route tests and raised full regression baseline to
	`111 passed`.

## 2026-08-03 - Position profiles, completion suggestions, and shift dashboard

- Added citation position profiles at
	`/citation-map/cases/{case_id}/position-profiles` with early-vs-late
	citation placement features and CSV export.
- Added citation completion suggestions at
	`/citation-map/cases/{case_id}/completion-suggestions` to recommend likely
	missing authorities, plus CSV export.
- Added jurisprudential shift dashboard at `/citation-map/issues/dashboard`
	combining replacement candidates, lifecycle-stage signals, and surprise
	authorities into one issue-level intelligence payload, plus CSV export.
- Expanded route-level test coverage and raised full regression baseline to
	`113 passed`.

## 2026-08-03 - Missing authorities, lifecycle, and court flow

- Added missing-authority detection at
	`/citation-map/cases/{case_id}/missing-authorities` to surface authorities
	peer-similar cases cite that the focus case does not.
- Added authority lifecycle tracking at
	`/citation-map/authorities/lifecycle` with stage classification
	(emerging, dominant, declining, foundational, transitional).
- Added cross-court authority flow analytics at `/citation-map/courts/flow`
	to quantify citation movement between courts.
- Added CSV exports for all three new analytics surfaces.
- Saved the user master roadmap into `MASTER_IDEAS.md` for future staged
	implementation planning.
- Expanded citation route tests and raised full regression baseline to
	`112 passed`.

## 2026-08-03 - Case reader and branch-focused exploration

- Added `/case-reader`, a searchable, responsive decision reader backed by each
	case's canonical stored full text, with source and citation-map deep links.
- Changed map, search, comparison, and evidence surfaces to show case names as
	the primary visual label and neutral citations as secondary metadata.
- Kept first-level authorities radial while placing expanded descendants near
	their clicked parent and bringing off-screen branches into the map viewport.
- Added opt-in HTTP Basic authentication for temporary private deployments;
	local access remains unchanged unless private-access environment variables are
	set.

## 2026-08-03 - Case Explorer and Issue Map workbench

- Added a dual-mode citation workbench with focused case exploration and broad
	issue, statute, and legal-area maps.
- Added force-directed issue graphs with 20-150 case controls, all internal
	citation links, and node sizes scaled by distinct citing-case counts.
- Added two/three-authority common-citer comparison, exact chunk-backed citation
	contexts with CSV export, evidence-bearing legal tags, and branch expansion.
- Kept dynamic IRPA section tags visibly identified as machine-extracted
	evidence candidates rather than authoritative legal classifications.
- Validated dense desktop and narrow-screen rendering without page overflow.

## 2026-08-02 - Citation map baseline

- Added whole-corpus citation analytics for graph summary, leading authorities,
	weighted case neighborhoods, co-cited authorities, and explainable
	shared-authority similarity.
- Aggregated repeated citation occurrences into weighted case-to-case edges
	while retaining the underlying occurrence rows as evidence.
- Added typed read-only APIs under `/citation-map/*` with bounded result sizes.
- Redesigned `/citation-map` around arbitrary case search and a focused radial
	map of the five most influential authorities cited by the selected case.
- Added clickable node inspection, authority mention counts, one-click map
	recentering, related cases with shared-authority explanations, and co-citation
	drill-down.
- Excluded document self-citations from focused authority maps and verified
	responsive rendering without horizontal overflow in narrow and desktop views.
- Validated all analytics queries against the live `35,902`-case PostgreSQL
	corpus without starting embeddings or modifying Hugging Face staging.
- Full regression baseline: `104 passed`.

## 2026-08-02 - First overnight result and resume-path repair

- Executed overnight run `20260801-234642` with `--continue-on-error`.
- Completed `ca_legal_v2` tagging for all `35,902` cases, creating `770,357`
	tags in approximately 59 minutes.
- Chunked all `35,519` previously unchunked text-bearing cases into `165,600`
	new chunks in approximately 87 seconds. PostgreSQL now contains `168,282`
	chunks across all `35,902` cases.
- Verified the separate reference library without downloads (`18` skipped as
	checksum-valid). The FC portal completed with zero new rows.
- Diagnosed citation and local-embedding failures as direct-script Python import
	path errors. Changed both overnight commands to module-mode invocation and
	added regression coverage.
- Changed an empty prototype procedural-history candidate set into a successful
	no-op rather than a failed job.
- Isolated official FC discovery failures by monthly window while retaining a
	non-zero exit when every source window is unavailable.
- Verified the existing failed-job run can resume without repeating completed
	tagging or chunking. Local BGE-M3 dry run sees pending chunks.
- Current remaining backlog: zero extracted citations and zero local BGE-M3
	vectors across `168,282` chunks.
- Full regression baseline after repair: `98 passed`.

## 2026-08-01 - Resumable overnight enrichment and local embeddings

- Added `scripts/run_overnight.py`, a sequential overnight orchestrator with an
	exclusive process lock, atomic JSON state, timestamped run directories,
	per-job logs, preflight checks, failure policy, and completed-job skipping on
	resume.
- Added official Federal Court-only acquisition jobs for IMM decision discovery,
	portal records, and procedural histories. CanLII and paid hosted-AI jobs are
	intentionally excluded from the overnight profiles.
- Added `scripts/chunk_cases.py` to create 6,000-character chunks with
	600-character overlap for canonical cases that do not already own chunks.
	Chunking uses keyset pagination and commits every 50 cases without changing
	`processing_status` or calling an AI service.
- Added resumable local BGE-M3 embedding through `scripts/embed_local_chunks.py`.
	It creates 1,024-dimensional vectors in `case_chunk_embeddings`, runs on CPU
	by default, commits every four chunks, and makes no OpenAI or Copilot calls.
- Hardened citation backfill with keyset pagination. Chunk citation extraction
	now processes all chunks for a case together so a later partial batch cannot
	erase earlier citations.
- Fixed Federal Court monthly ingestion windows across December/year boundaries.
- Added a separate 18-document reference library with strict content validation,
	source-native PDF/HTML storage, checksums, atomic writes, resume, and inventory.
- Advanced deterministic legal tagging to `ca_legal_v2`, including deeper PRRA,
	CBSA removal, inadmissibility, detention, and enforcement concepts.
- Verified pre-run PostgreSQL state: `35,902` cases, `35,498` raw cases, `2,682`
	chunks across `383` cases, `35,519` text-bearing cases pending chunking, zero
	local BGE-M3 embeddings, and zero `ca_legal_v2` completion records.
- Verified source state: `17,240` FC procedural histories, `830` discovered
	official FC decision IDs, and `18/18` reference documents downloaded.
- Added `OVERNIGHT.md` with launch, pull-only, preflight, resume, lock, state, and
	log operations. Full regression baseline: `94 passed`; workspace diagnostics
	are clean.

## 2026-08-01 - Versioned Canadian immigration and CBSA legal tags

- Added deterministic, evidence-bearing `ca_legal_v1` tagging across immigration,
	refugee protection, IRPA/IRPR, international law, countries, organizations,
	judicial review, remedies, and general legal concepts.
- Added first-class CBSA/MPSEP dimensions for section 44 reports, inadmissibility,
	detention, removal orders, stays/deferrals, warrants, and program consequences.
- Added indexed `case_tags` and resumable `case_tagging_status` tables in migration
	`0010_case_legal_tags` without changing source records or existing embeddings.
- Added `scripts/tag_cases.py` with dry-run, batching, limits, court/source filters,
	taxonomy-aware resume, and explicit retag support.
- Added `LEGAL_TAGGING.md` with authoritative source hierarchy, secondary reference
	works, interpretation cautions, taxonomy coverage, and operational commands.
- Verified focused taxonomy coverage (`5 passed`) and a five-case PostgreSQL dry-run
	(`38` preview tags).

## 2026-08-01 - Multi-court Hugging Face staging and project health review

- Downloaded and verified `61,217` A2AJ decisions in a local SQLite staging archive:
	- FC: `35,814`
	- RPD: `6,729`
	- FCA: `7,785`
	- SCC: `10,889`
- Preserved complete source rows in `raw_payload` plus query-friendly normalized columns and metadata-only JSON.
- Fixed bilingual citation normalization for `cases_cited_en/fr` and `cases_citing_en/fr`.
- Added stable source keys and compatibility matching so ingestion reruns do not duplicate pre-key staging rows.
- Added a bounded `repair_staging` command to backfill normalized citation columns and source keys after active data pulls finish.
- Added unique case/model embedding storage and bounded-memory embedding batches that skip completed vectors.
- Added `scripts/import_canlaw_staging.py`, a streaming, resumable, dry-run-capable bridge into the primary PostgreSQL ingestion API.
- Expanded `scripts/ingest_a2aj_parquet.py` to preserve all non-text A2AJ source metadata, including bilingual fields.
- Added Hugging Face/Xet dependencies, ignored the multi-gigabyte staging database, and removed duplicate dependency declarations.
- Added focused regression tests for multi-court ingestion, rich metadata, idempotency, embeddings, and the staging bridge.
- Verified the complete project suite: `60 passed`.
- Operational safety: left the active FC procedural-history pull running and did not execute the PostgreSQL bridge.

## 2026-07-31 - Prototype explorer, citation map, and topic-keyword visibility

- Added prototype cohort explorer endpoints:
	- `GET /prototype`
	- `GET /prototype/summary`
	- `GET /prototype/cases`
	- `GET /prototype/graph`
- Added an interactive citation map in the prototype UI:
	- topic-aware graph filtering
	- node-cap control for performance
	- degree-based node sizing and topic color encoding
	- hover metadata and node-click table filtering
- Added robust prototype pagination behavior:
	- out-of-range page requests now clamp to page `1` when filtered totals are non-zero
- Added cohort topic tagging workflow:
	- `scripts/tag_prototype_topics.py`
	- executed successfully for full cohort (`334` scanned/updated)
- Added prototype graph and pagination regression tests in `tests/test_api.py`.
- Updated health baseline:
	- `pytest -q` => `52 passed`

## 2026-07-31 - Merged local and A2AJ citation graph

- Extended the citation graph to carry a `provenance` flag so local regex extraction and A2AJ-derived edges can coexist in the unified `citations` table.
- Added A2AJ provenance tables and mappings:
	- `a2aj_cases`
	- `a2aj_citation_edges`
	- `a2aj_case_map`
- Added `scripts/ingest_a2aj_citation_network.py` to read the A2AJ parquet source, populate A2AJ citation tables, build the local case map, and convert A2AJ edges into local citations.
- Added FastAPI endpoints for A2AJ cases, A2AJ edges, A2AJ mapping, and A2AJ graph conversion.
- Kept local citation extraction and citation-metric recomputation in `backend/citations.py` and `scripts/extract_citation_network.py`.

## 2026-07-31 - Citation network scaffold added

- Added citation-graph ORM models and migration for `citations` and `citation_metrics`.
- Added reusable citation extraction helpers in `backend/citations.py` with Canadian neutral, case, and statute citation regexes.
- Added read-only backend endpoints for outgoing, incoming, and passage-level citations plus per-case citation metrics.
- Added `scripts/extract_citation_network.py` to backfill citations from cases or chunks and recompute graph metrics.
- Added a small citation-in-degree tie-breaker to case search so heavily cited cases can surface higher without changing the reported similarity score.

## 2026-07-31 - Immigration core dataset curation added

- Added `scripts/curate_a2aj_immigration_cases.py` to build a balanced immigration-focused seed set from the full A2AJ Federal Court parquet source.
- The selector now groups cases by immigration-relevant buckets:
	- refugee protection / non-refoulement
	- judicial review / procedure
	- removal / detention / inadmissibility
	- family status / citizenship / H&C
	- agency review and enforcement (`IMM`, `IRCC`, `CBSA`, `Minister`, `MPSEP`)
- Added balanced sampling controls:
	- default limit of 60 cases
	- per-bucket selection cap before fallback filling
- Stored the resulting records as `source_type="a2aj_immigration_core"` with bucket metadata in `metadata_json`.
- Added tests covering immigration signal scoring and bucket-balanced selection.

## 2026-07-31 - Metadata search UX overhaul, broader filters, and project health pass

- Expanded `CaseSearchRequest` metadata filters in `backend/models.py` with:
	- `title_contains`
	- `source_name_contains`, `source_url_contains`, `source_id_contains`
	- `citation_contains`, `secondary_citation_contains`
	- `dataset_version_contains`, `upstream_license_contains`
	- `cases_cited_contains`, `cases_citing_contains`
	- `language`, `processing_status`
	- `scraped_from`, `scraped_to`
	- `citing_cases_min`, `citing_cases_max`
- Extended `_apply_case_filters` in `backend/routes.py` so all of the above fields are enforced in SQL filtering.
- Added shared request validation guardrails for:
	- reversed decision date ranges
	- reversed scraped date ranges
	- invalid citing count bounds (`min > max`)
- Reworked the `/testing` UI into a metadata-first legal search interface:
	- core fields for document text, identifiers, citation, court, source, and language
	- advanced metadata panel for noteup/citation-network, scrape windows, status, and citing-count bounds
	- optional year toggle filter
	- agency presets (`Minister`, `IRCC`, `CBSA`, `All agencies`)
	- active-filter summary line and `Enter` key to run search
	- JSON payload moved to synchronized preview/advanced override mode
- Applied CanLII-style wording and flow cues (`Document text query`, identifier labels, `Start a search`, `Reset your search`).
- Confirmed runtime API behavior via live smoke check on `POST /search` (status `200` with pagination headers).
- Project health pass completed:
	- `python -m py_compile backend/routes.py backend/models.py tests/test_api.py`
	- `pytest -q` => `38 passed`
	- `get_errors` => no workspace diagnostics
- Added and updated regression coverage in `tests/test_api.py` for the new filter fields, UI labels, and validation behavior.

## 2026-07-31 - Retrieval foundation extended

- Added Alembic configuration and an initial migration for controlled schema evolution.
- Added jurisdiction, citation, full text, issues, flexible metadata, source URL, and source name fields.
- Added B-tree metadata indexes and an HNSW cosine vector index.
- Added search filters for court, jurisdiction, and date ranges.
- Added pagination and normalized similarity scores to search responses.
- Added four focused API tests covering ingestion, filtered search, date validation, and missing OpenAI configuration.

## 2026-07-31 - FC import adapter and low-noise evaluation controls

- Added `scripts/import_fc_decisions.py` to import Federal Court records from `.json`, `.jsonl`, or `.csv` through the existing `/ingest` API.
- Added field normalization for common FC dataset keys (`style_of_cause`, `neutral_citation`, `decision_date`, `docket_number`, `full_text`).
- Added lightweight deduplication and record-skipping rules for missing required content/date during batch import.
- Added evaluator controls in `scripts/evaluate_retrieval.py`:
	- `--limit` to run a bounded fixture subset for faster iteration.
	- `--verbose` to opt in to per-query output instead of printing it by default.
- Added unit tests for importer mapping/deduplication and evaluator summary/gate behavior.

## 2026-07-31 - Federal Court portal collector (stage 1 and optional stage 2)

- Added `scripts/fc_portal_collector.py` for polite FC portal collection with:
	- prefix-based paging (`IMM`, `T`, `A`, etc.)
	- retry/backoff and configurable request pacing
	- checkpoint/resume support
	- incremental JSONL output
	- deduplication across runs from existing output
	- optional detail-page expansion (`--expand-details`)
- Added parser tests for listing and detail extraction in `tests/test_fc_portal_collector.py`.
- Added `beautifulsoup4` dependency for robust HTML parsing.
- Added optional importer-contract emission (`--emit-import-ready`) that writes staged rows mapped to `style_of_cause`, `neutral_citation`, `decision_date`, `full_text`, `docket_number`, and `url`.
- Added incremental prefix-rotation mode (`--incremental-prefix-window`, checkpoint-backed `rotation_run`) for scheduled runs without crawling all prefixes each execution.
- Added importer normalization for staged collector output so `scripts/import_fc_decisions.py` ignores listing/detail rows and consumes `stage=import_ready` rows directly.

## 2026-07-31 - Multi-site case existence verifier (run-later ready)

- Added `scripts/verify_fc_case_existence.py` to verify whether docket/court numbers exist across configured sources.
- Supports `.txt`, `.json`, and `.jsonl` input formats and writes JSONL verification output.
- Added provider framework with:
	- `courtfiles` (definitive check via official `/CourtFilesAndDecisions/proceedingQueriesCourtNumberList` endpoint)
	- `decisions` (signal-only probe to decisions site search endpoint)
- Added focused unit tests in `tests/test_verify_fc_case_existence.py`.

## 2026-07-31 - Synthetic dataset imported

- Added a reusable importer for 20 clearly labeled synthetic Federal Court non-refoulement cases.
- Imported the dataset through the live `/ingest` API, generating and storing OpenAI embeddings for each record.
- Confirmed the database contains 20 synthetic cases plus the earlier demo case.
- Verified broad semantic search and jurisdiction-filtered search against the dataset.
- Made the importer skip existing citations so it can be rerun safely.

## 2026-07-31 - Raw A2AJ ingestion foundation

- Made summaries and embeddings optional so source documents can be preserved before enrichment.
- Added A2AJ provenance, licensing, source, hash, processing-status, and citation-network fields.
- Added migration `0002_raw_ingestion` and applied it to the local database.
- Added `scripts/ingest_a2aj_parquet.py` with dry-run, limit, Federal Court filtering, and duplicate detection.
- Added a regression test proving raw ingestion does not call OpenAI.
- Installed `pyarrow` for Parquet reading; no A2AJ data has been imported yet.

## 2026-07-31 - First A2AJ embedding test

- Added `case_chunks` storage and migration `0004_case_chunks`.
- Chunked the 25 A2AJ pilot cases into 82 overlapping chunks.
- Embedded the chunks with `text-embedding-3-small` at an estimated cost of $0.0021.
- Stored chunk embeddings and case-level average vectors, marking all 25 A2AJ records as `embedded`.
- Verified real A2AJ records appear in semantic search.
- Observed that synthetic records still rank highly, confirming the need for curated relevance benchmarks and chunk-level retrieval evaluation.

## 2026-07-31 - Curated evaluation and chunk search

- Added a transparent keyword-scored selector for 25 A2AJ refugee-risk cases.
- Imported the curated cases separately as `a2aj_curated` raw records, preserving the original pilot set.
- Embedded 471 curated text chunks at an estimated cost of $0.0138.
- Added `POST /search/chunks` to return source passages with parent-case citations.
- Verified chunk retrieval returns relevant passages about torture evidence, state protection, and refoulement.

## 2026-07-31 - A2AJ source and retrieval state

- Downloaded the A2AJ Federal Court Parquet source locally at `data/raw/a2aj/FC/train.parquet`.
- Verified the file contains 35,814 records and completed a 25-record dry run with zero invalid records or duplicates.
- Imported 25 A2AJ pilot records as raw full-text records, then chunked and embedded them into 82 chunks.
- Added `GET /cases/{id}` for direct case retrieval with a clear `404` response for missing IDs.
- Added migration `0003_backfill_processing_status` so existing vector records are labeled `embedded` instead of `raw`.

## 2026-07-31 - Paused evaluation checkpoint

Current database state:

- 21 synthetic/demo prototype cases, embedded.
- 25 A2AJ pilot cases, embedded in 82 chunks.
- 25 curated A2AJ refugee-risk evaluation cases, embedded in 471 chunks.
- 71 total case records and 553 total stored chunks.
- Alembic revision `0004_case_chunks` is at head.
- Seven automated tests pass.

The project is intentionally paused before larger ingestion. The current retrieval result is a technical success, not yet a validated legal-relevance benchmark: synthetic cases can rank highly, and chunk results can repeat the same parent case. No summaries or RAG generation have been added.

Recommended next path:

1. Add a relevance evaluation fixture with research questions and expected case citations.
2. Group chunk results by parent case and return the best passages per case.
3. Add source-type filters so evaluation can exclude synthetic records.
4. Review curated results manually and adjust selection rules.
5. Run the benchmark before importing more records or generating summaries.
6. Add RAG only after retrieval quality is measurable.

## 2026-07-31 - Long-term guidance added

- Added `GUIDANCE.md` as the project north star for litigation-focused ingestion, retrieval, RAG, data modeling, operations, and future product decisions.
- Kept current implementation notes, historical changes, and future direction in separate documents.

## Earlier project history - Accounts, setup, and resolution

This section records the supplied project history without storing passwords, API keys, or other secret values.

### Phase 1 - Accounts and API setup

- An OpenAI account was created.
- OpenAI billing was funded with $25 in credits.
- A new OpenAI API key was generated, verified in the OpenAI dashboard, and saved locally in the project environment file.
- Secret values are intentionally omitted from this history.

### Phase 2 - Local development environment

- Python 3.12 and pip were installed and verified.
- The project was created at `C:\Users\danny\OneDrive\Desktop\AI CaseLibrary`.
- A project virtual environment was created in `venv`.
- PowerShell activation required:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

- Backend dependencies were installed, including FastAPI, Uvicorn, SQLAlchemy, psycopg2, pgvector, Pydantic, and the OpenAI client.

### Phase 3 - PostgreSQL and pgvector

- PostgreSQL and pgAdmin were installed.
- pgvector was enabled and verified.
- The working local database is `caselibrary`.
- The `cases` table contains `id`, `title`, `court`, `date`, `summary`, `embedding`, and `created_at`.

### Phase 4 - FastAPI backend

- `main.py` provides the FastAPI application, startup hook, router registration, and health check.
- `database.py` provides SQLAlchemy configuration, sessions, the ORM `Case` model, pgvector setup, and table creation.
- `models.py` provides the Pydantic request and response models.
- `routes.py` provides embedding calls, ingestion, and vector similarity search.
- The current implementation keeps these responsibilities in the four modules above rather than separate `schemas.py`, `openai_client.py`, or `search.py` files.

### Phase 5 - Project-local environment

- A local `.env` file was created under `backend/.env`.
- It contains local OpenAI and PostgreSQL configuration, but its secret values are not recorded here.
- The application loads `.env` from the project root or `backend/.env` using `python-dotenv`.
- It supports either `DATABASE_URL` or separate `POSTGRES_*` variables.

### Phase 6 - Debugging and resolution

- Initial startup failed because the environment file was missing or empty and the fallback PostgreSQL credentials were incorrect.
- PostgreSQL was reachable, but authentication initially failed for the `postgres` user.
- After the correct local environment values were saved, the remaining error showed that `ai_caselibrary` did not exist.
- The configuration was corrected to use the existing `caselibrary` database.
- Database initialization then succeeded, including pgvector setup and table creation.
- Uvicorn completed startup with `Application startup complete.`

### Phase 7 - Current system state

- The health endpoint has been verified successfully.
- The `/ingest` and `/search` routes are registered and ready for live OpenAI testing.
- API documentation is available at `/docs`.
- Full live ingestion and semantic-search requests still require a valid OpenAI API key and should be tested with non-sensitive sample cases.

## 2026-07-31 - Backend foundation completed

### Added

- FastAPI application wiring in `backend/main.py`.
- SQLAlchemy PostgreSQL engine and session management.
- ORM `Case` model with title, court, date, summary, timestamp, and a 1536-dimensional pgvector embedding.
- Automatic `vector` extension setup and table creation at application startup.
- Pydantic request and response schemas.
- `POST /ingest` for OpenAI summary embeddings and case storage.
- `POST /search` for OpenAI query embeddings and cosine similarity search.
- Environment loading from the project root `.env` or `backend/.env`.
- Support for either `DATABASE_URL` or separate `POSTGRES_*` settings.
- Safe SQLAlchemy URL construction for passwords containing special characters.

### Configuration fixes

- Identified that PostgreSQL was running on port 5432.
- Corrected the database name from `ai_caselibrary` to `caselibrary`.
- Confirmed PostgreSQL authentication and pgvector initialization.

### Verification

- Backend modules compile successfully.
- Pylance reports no errors in the database module.
- Database initialization succeeded.
- FastAPI startup completed successfully.
- `GET /` returned `AI CaseLibrary backend is running`.

### Remaining work

- Add Alembic migrations.
- Add automated API and database tests.
- Test `/ingest` and `/search` with a valid OpenAI API key.
- Add the AI chat/RAG endpoint.
- Add authentication, CORS configuration, logging, and production deployment settings.

## 2026-07-31 - Code review and pause checkpoint

- Reviewed backend, migrations, importers, tests, and live database state.
- Added source-type filtering to case and chunk search so synthetic data can be excluded from evaluation.
- Made ingestion derive `processing_status` from actual behavior instead of trusting caller input.
- Made the server compute full-text hashes instead of accepting a potentially false client-provided hash.
- Added regression coverage for source filtering, hash integrity, and derived processing status; the suite now has 8 passing tests.
- Added `AI_HANDOFF.md`, a detailed technical continuation brief for another AI or developer.
- Confirmed the paused database state: 71 cases, 553 chunks, migration `0004_case_chunks` at head.
- Documented remaining risks: unbenchmarked retrieval quality, repeated parent cases in chunk results, no CanLII adapter, no canonical multi-source table, and no RAG layer.

The recommended next step is retrieval evaluation with expected citations, not full-corpus ingestion or RAG generation.
