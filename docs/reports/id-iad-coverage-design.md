# Design: ID/IAD decision coverage for CBSA-hearing research

**Status:** Design proposal only; no source acquisition, code, schema, or data
changes are included.
**Prepared:** 2026-10-03

## Product outcome and scope

The intended product outcome is a traceable, searchable collection of
Immigration Division (ID) and Immigration Appeal Division (IAD) decisions that
can support research relevant to CBSA hearings, without presenting discovered
records as official, complete, or legally classified unless that status is
evidenced.

This note scopes a future source-to-search path. It does not assert that any
source below contains a complete or reusable ID/IAD corpus, settle the legal
meaning of outcome categories, or authorize collection. No implementation is
proposed until source access and permitted use are checked.

### Evidence labels

- **Verified (repository):** confirmed in the local repository documentation,
  code inventory, or migration inventory reviewed for this design.
- **Unverified:** a source, licence, legal, coverage, data-quality, or other
  claim that was not directly confirmed from an authoritative accessible
  source. Unverified claims remain candidates, not facts.
- Recommendations are design proposals, not statements about current
  implementation.

## Possible sources and rights status

| Candidate | Possible role | What is verified | What remains unverified |
| --- | --- | --- | --- |
| [Immigration and Refugee Board (IRB) decisions](https://irb-cisr.gc.ca/en/decisions/Pages/index.aspx) | **Unverified candidate** for first-party discovery or acquisition of published tribunal decisions | Only the candidate URL was identified. | Whether this page publishes ID and IAD reasons; coverage, search/export features, stable IDs, historical range, formats, reuse permissions, and automated access conditions are all **unverified**. |
| [IRB Board/Tribunal information](https://irb-cisr.gc.ca/en/board/tribunal/Pages/index.aspx) | **Unverified candidate** authoritative orientation for tribunal names and roles | Only the candidate URL was identified. | Its current content and whether it resolves the proposed tribunal taxonomy are **unverified**. |
| [CanLII IRB collection](https://www.canlii.org/en/ca/irb/) | **Unverified candidate** secondary discovery or permitted source, potentially useful to identify published decisions | Only the candidate URL was identified. | ID/IAD coverage, completeness, bulk access, automated-use permissions, storage/republication rights, and applicable restrictions are **unverified**. Do not characterize CanLII decisions as open-licensed. |
| [CanLII terms](https://www.canlii.org/en/info/terms.html) | **Unverified candidate** terms page to review if CanLII is considered | Only the candidate terms URL was identified. | Current terms text, applicability to the proposed use, and any permission or restriction are **unverified**. |
| [Government of Canada Open Government Licence](https://open.canada.ca/en/open-government-licence-canada) | **Unverified candidate** general licence reference to check if a source explicitly invokes it | Only the candidate URL was identified. | Current text and, especially, whether it applies to any IRB decision or decision-site content are **unverified**. Do not infer applicability from a government domain. |
| [Federal Court decisions](https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/nav.do) | **Unverified candidate** separate source for later court proceedings that may cite or review tribunal matters | Only the candidate URL was identified. | Coverage and linkability to ID/IAD decisions are **unverified**. This is not a substitute for collecting original tribunal decisions. |

**Access and verification limit:** delegated read-only checks attempted bounded
requests to the IRB, CanLII, Canada.ca, and open.canada.ca hosts on 2026-10-03.
DNS resolution failed and `curl` returned HTTP status `000`; no page text,
licence, robots/access policy, or record was retrieved. Accordingly, every
external source and licence statement in this section is **unverified**. Links
are research leads, not evidence of access or permission. Before acquisition,
record the exact applicable terms, source URL, access date, allowed retrieval
method, storage/display rights, retention conditions, and any attribution
requirements in the source register. Escalate ambiguous rights for legal review;
do not bypass access controls or infer reuse permission.

## Repository touchpoints and proposed data contract

The following current-state statements are **verified (repository)** by the
reviewed local architecture references and bounded worker inspection:

- `backend/ingestion.py` owns canonical create/merge and source precedence;
  current ingest records have source/provenance support.
- `backend/models.py` owns request/response contracts, including ingestion and
  search requests.
- `backend/database.py` owns ORM models. The inspected canonical case model has
  no dedicated ID/IAD division code; the existing case `court` field should not
  be overloaded with a tribunal identity.
- `alembic/` owns deployable schema changes. `0008_case_provenance_tables.py`
  adds source provenance; `0022_case_outcomes.py` adds the versioned
  `case_outcomes` layer.
- `case_outcomes` is the outcome source of truth; the legacy
  `metadata_json.reader_extracted` fields remain a compatibility mirror.

These are the proposed additions to evaluate, not implemented behavior:

| Surface | Proposed contract |
| --- | --- |
| `backend/ingestion.py` | Accept and validate a controlled `tribunal_code` independently from `court`, with values initially proposed as `IRB_ID` and `IRB_IAD`. Preserve source-native tribunal name/identifier and original decision text as source evidence. Keep source identity, source URL, terms/licence reference, retrieval time, content hash, and parser/source version in the provenance path. Do not let a low-confidence text inference silently overwrite an explicit source value. |
| `backend/models.py` | Add the tribunal code to ingest and case-search contracts; validate only the controlled codes and permit existing callers to omit it. Add typed outcome filters only after agreeing their vocabulary. Keep source-record metadata and legal outcome signals separate. |
| `backend/database.py` | Add a nullable, indexed canonical tribunal code (or a normalized tribunal relation if a later source inventory proves multiple board/division hierarchies need it). Keep the existing court field for courts. Preserve provenance via `case_sources`; do not duplicate source licensing fields into unrelated citation/tag layers. Extend the dedicated outcome record only for versioned, evidence-backed fields demonstrated by the pilot. |
| `alembic/` | Use an additive, reversible migration with a nullable field and controlled values; preserve current cases and old API clients. Generate the schema reference from its generator after any eventual schema implementation. No migration is part of this task. |

Candidate record metadata to capture or map (each is a design proposal; exact
source fields and availability are **unverified**): source-native decision ID,
tribunal code, division label, decision date, case/reference number, title,
language, proceeding type, source URL, source family, retrieval timestamp,
terms/licence URL and review status, raw/normalized content hashes, and
publication/source status. Reuse existing case/source fields where appropriate
rather than storing competing copies. Distinguish a decision's tribunal from
the court that may later review it.

**Code value note:** `IRB_ID` and `IRB_IAD` are proposed internal values, not
verified source codes or externally standardized identifiers. Confirm source
labels and stable IDs before freezing the enum or migration.

## Outcome coding and Minister analytics

The requested analytical dimensions are **admissibility**, **detention**, and
**removal**. Whether these categories map cleanly to each division's
jurisdiction, what decision types belong in them, and which outcomes have
operational relevance are **unverified legal/domain claims** requiring review
against authoritative material and a labelled decision sample. Treat the
labels below as candidate dimensions, not legal conclusions.

Recommended design:

1. Preserve the tribunal's operative disposition text and source location.
   Keep it distinct from normalized analytics labels.
2. Store tribunal/division, proceeding type (candidate categories:
   admissibility, detention, removal), procedural event (candidate values to
   validate, such as hearing/review/appeal), and outcome action as separate
   axes. Do not encode these as tags, court names, or a single
   `decision_outcome`.
3. Retain the existing versioned `case_outcomes` evidence, confidence,
   disposition, and role boundaries. Add fields only after the pilot proves
   they are necessary and reproducibly extractable; ambiguous or missing
   outcomes must remain `unknown`/`undetermined`, not be inferred as a Minister
   win or loss.
4. Record the Minister's role (for example, applicant, respondent, other, or
   unknown) separately from the government/party outcome. The value list itself
   needs review. A Minister-related case or mention is not sufficient evidence
   that the Minister was a party or prevailed.
5. Scope analytics by tribunal and proceeding category before computing
   decision counts or outcome rates. Report denominator, unknown/mixed count,
   cohort dates, and source coverage. Do not combine ID and IAD rates or
   admissibility, detention, and removal results into one “Minister outcome”
   without an explicitly validated question and denominator.

Potential analytics include counts and reviewed outcome distributions for
admissibility, detention, and removal, partitioned by tribunal, date, and
verified Minister role. These are proposed measures; feasibility, legal
interpretation, and data completeness are **unverified** until measured on
source-linked records. Any eventual result must expose its cohort definition,
evidence, confidence, and unknowns.

## Filters and pages to consider

**Verified (repository):** `/data-explorer` is the active research interface;
Case Search already offers court/jurisdiction/date/source and outcome-related
filters. The court alias set currently documents FC, FCA, and SCC. Search opens
the inline reader; `/case-reader` is a compatibility route. Outcome and
Minister-related API/analytics touchpoints include
`/analytics/outcomes-by-year`, `/analytics/search/ministers`, and
`/api/citation-intelligence/{case_id}/outcomes`. Federal Court activity is a
separate workflow, not a tribunal-decision collection.

Proposed impact assessment (no page change in this task):

- Add a distinct **Tribunal** filter (ID/IAD), not ID/IAD values masquerading
  as court abbreviations. Add proceeding-category filters only after the
  controlled taxonomy is approved.
- Include tribunal and source/provenance context in Case Search result rows
  and the inline reader's canonical metadata, with explicit unknown/source
  status where relevant.
- Scope existing outcome panels/API aggregations by tribunal and validated
  proceeding categories; make Minister-role filtering explicit and preserve
  unknown/mixed cases.
- Review whether `/analytics/outcomes-by-year` and
  `/api/citation-intelligence/{case_id}/outcomes` need compatible optional
  filters. Keep `/analytics/search/ministers` as party-filter support unless
  evidence establishes a separate outcome use.
- Do not fold ID/IAD decisions into Federal Court activity charts or
  court/judge statistics by default. Assess judge filters only if source
  coverage and reliable judicial-member identification are established.

## Options and recommendation

| Option | Accuracy/provenance | Coverage and cost | Maintenance/explainability |
| --- | --- | --- | --- |
| Official IRB source only | Best first-party provenance if the candidate source and identity fields are confirmed; rights/access remain **unverified**. | Could have publication or acquisition gaps; those gaps are **unverified**. | Simplest source boundary; makes missing coverage visible rather than filling it with opaque records. |
| CanLII only | Secondary source; decision identity and permissible use need verification. | Could aid discovery; coverage, terms, and automated-access limits are **unverified**. | A single adapter is operationally simpler, but source limits could be mistaken for tribunal completeness. |
| Official-first source ledger, with an independently verified secondary source only as an attributed supplement | Preserves source identity and conflict review; does not assume sources or licences are interchangeable. | Potentially broader but adds rights review, reconciliation, and storage cost; actual gain is **unverified**. | More maintainable if all adapters enter the same provenance-aware staging/merge path; easiest to explain source conflicts and missing data. |

**Recommendation:** use the third pattern as a target, gated on source/terms
verification. Begin with the official-source candidate and a separate discovery
inventory; permit a secondary source only after its terms and record matching
are confirmed. Existing source precedence and `case_sources` are appropriate
integration boundaries; do not merge sources by title alone.

**Disconfirming experiment:** after access and rights review, compare a small
manually checked set of candidate decisions across the official source and one
permitted secondary source. If stable identifiers cannot distinguish records,
or permitted access/storage cannot be established, stop the adapter proposal
and revise the source plan before schema work.

## Phased plan and smallest first slice

1. **Source and legal gate (before implementation).** Review authoritative
   source pages and applicable terms; confirm publication/access method and
   whether use, storage, display, and indexing are permitted. Confirm the
   internal tribunal-code mapping and legal taxonomy with a domain reviewer.
   Record each result and unresolved item in `docs/DATA_SOURCE_REGISTER.md`.
   Stop if rights or reliable identity cannot be established.
2. **Smallest first slice — bounded, noncanonical pilot.** Only after phase 1
   passes, manually select a small (suggested: 10-record) single-division
   cohort from a permitted source. Create a read-only/staged manifest with
   source URL/ID, terms review reference, tribunal code, title, date, language,
   hashes, and parser notes. Have a reviewer verify identity, provenance, and
   candidate proceeding/outcome labels. Do not write canonical records or
   publish outcome analytics. The 10-record size is a proposed bounded pilot,
   not a claim about corpus representativeness.
3. **Additive contract and migration.** If the pilot supports stable source
   identity and metadata, add nullable tribunal code to ingestion/search and
   canonical schema, with backward-compatible validation, tests, migration,
   and generated-schema regeneration. Keep source-level attribution and merge
   conflicts intact.
4. **One outcome family at a time.** Validate label definitions and evidence
   extraction against a reviewed gold set for one requested category before
   enabling its analytics. Report unknowns and role-specific denominators.
   Expand across admissibility, detention, and removal only when separate
   quality gates pass.
5. **Research UI and coverage monitoring.** Add the tribunal filter and
   source-aware reader metadata; then expose validated outcome groupings.
   Measure source coverage, duplicate/conflict rates, unknown outcomes,
   Minister-role precision, and researcher retrieval success before expanding.

No source page was successfully accessed; no source acquisition, licence
interpretation, schema change, or code change was performed for this design.

## Evidence and references

Repository sources checked:

- [System Reference — source preservation and provenance](../../SYSTEM_REFERENCE.md)
- [System Reference — data model and ingestion lifecycle](../../SYSTEM_REFERENCE.md)
- [System Reference — metadata/outcome semantics and Data Explorer](../../SYSTEM_REFERENCE.md)
- `backend/ingestion.py`, `backend/models.py`, `backend/database.py`,
  `backend/metadata_outcomes.py`, `backend/intelligence.py`,
  `backend/analytics_service.py`, `backend/search_service.py`,
  `backend/routes.py`, selected `backend/pages/` modules, and migrations
  `0001`, `0008`, and `0022` (bounded read-only inspection reported by the
  delegated worker).
- [System Reference — active workflow and documentation authority](../../DOCS_INDEX.md)

External source/terms pointers and access limitations are listed above. They
were not successfully fetched in this run, so external legal, licensing,
availability, completeness, and access-method claims remain **unverified**.
