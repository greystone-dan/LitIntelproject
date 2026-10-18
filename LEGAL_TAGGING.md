# Canadian Legal Tagging

## Design

Tag rows carry a case, category, normalized value, evidence, source, taxonomy
version, and (where supported by that version) confidence and offsets.
`case_tagging_status` records completion per case and taxonomy version.

### Taxonomy lifecycle

The repository contains three distinct taxonomy identifiers: `ca_legal_v2` in
`backend/legal_tagger.py`, `ca_legal_v2_core` for the separate V2 whitelist,
and the proposed `ca_legal_v3_core`. These identifiers and historical run
counts do not establish which tags are currently present in a live database;
use a fresh, authorized database/API inventory for live coverage.

**V3 activation status is unresolved in source.** The processing stage and
overnight job are wired to the V3 writer, and the overnight job description
calls it active. However, `backend/legal_tagger_v3.py` and
`scripts/tag_cases_v3.py` describe it as inactive, and the proposal file is
still marked `review_status: proposed`. Until that contradiction is resolved
and an owner confirms activation, treat V3 as a review-only proposal: do not
call it the approved production taxonomy or run its writer as a production
backfill. Keep stored rows separated by `taxonomy_version`; do not delete or
rewrite taxonomy rows based on this document.

The taxonomy does not treat a text match as a legal conclusion. For example, an
`organization=ipob` tag means the decision discusses IPOB, not that the Court made
any particular finding about that organization. Evidence must be shown with tags
in downstream interfaces.

## Source hierarchy

Use sources in this order when adding or changing legal concepts:

1. **Binding law:** the current [Immigration and Refugee Protection Act](https://laws-lois.justice.gc.ca/eng/acts/i-2.5/) and [Immigration and Refugee Protection Regulations](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/), the Constitution and Charter, other applicable statutes, regulations, and binding appellate decisions.
2. **Tribunal doctrine:** the IRB's [Interpretation of Convention Refugee and Person in Need of Protection in the Case Law](https://www.irb-cisr.gc.ca/en/legal-policy/legal-concepts/Pages/RefDef.aspx), Chairperson's Guidelines, policy instruments, rules, and country-of-origin National Documentation Packages.
3. **Court procedure:** Federal Court immigration practice guidelines, the Federal Courts Act and Rules, and reported FC/FCA/SCC decisions.
4. **Program operation:** IRCC [Program Delivery Instructions](https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/operational-bulletins-manuals.html) and CBSA enforcement manuals and public program descriptions. These explain administration; they do not override legislation or binding law.
5. **International law:** the 1951 Refugee Convention and 1967 Protocol, Convention against Torture, ICCPR, Convention on the Rights of the Child, CEDAW, Rome Statute, and relevant UNHCR Handbook and Guidelines on International Protection.
6. **Secondary sources:** current editions of `Canadian Immigration & Refugee Law Practice` (LexisNexis), `Immigration and Refugee Law: Cases, Materials, and Commentary` (Emond), practitioner works on Canadian inadmissibility and enforcement, and Hathaway and Foster's `The Law of Refugee Status` (Cambridge University Press). Confirm propositions against primary sources and verify the current edition before relying on a text.

## Coverage

Major independent dimensions include:

- legal area, proceeding, tribunal, agency, responsible minister, and outcome
- IRPA sections, IRPR provisions, Charter sections, and international instruments
- Convention grounds, section 96 and 97 risks, exclusion, cessation, vacation,
  state protection, IFA, credibility, evidence, country conditions, and non-refoulement
- Article 1F exclusion branches, section 97 torture and cruel-treatment risks,
  and IRB Chairperson guidance on detention, gender, accessibility, and SOGIESC
- countries and named political or armed organizations, including BNP and IPOB
- inadmissibility grounds, section 44 reports, admissibility hearings, detention,
  alternatives to detention, warrants, border examinations, and removal orders
- judicial, statutory, and administrative removal impediments
- CBSA program consequences such as removal delayed, removal resuming, and a
  redetermination required

CBSA and MPSEP are tagged separately from IRCC and the immigration minister because
their statutory roles and operational consequences differ. A judgment can therefore
be queried by decision-maker, enforcement action, impediment, and program effect.

## Commands

### Tagging V2 core layer (legacy comparison only)

Tagging V2 is an independent, legacy high-precision whitelist taxonomy defined in
`config/tagging_v2_core_whitelist.json`. It uses the separate version
`ca_legal_v2_core`, so it can be previewed or populated without changing
existing `ca_legal_v2` tags. The core layer contains canonical countries,
agencies, tribunals, statutes, acronyms, named external organizations, and
reviewed general legal/process terms with explicit aliases. The whitelist now
contains 146 canonical terms; reviewed country and organization inventories
expand the loaded matcher set without changing the taxonomy version.

The reviewed country and organization inventories are loaded into this layer as
additional canonical entities. V2 stores every matched occurrence, not only one
row per canonical value: each row retains the exact evidence and its
`offset_start`/`offset_end` location in `cases.full_text`. The main research
reader renders these evidence spans as green highlights. The `--recent` option
orders cases by decision date descending, then case ID descending, across all
decision types; use `--court` when a specific court cohort is intended.

Preview without writes:

```powershell
python scripts/tag_cases_v2.py --dry-run --limit 25
```

Run resumably in bounded batches. The default is 10 cases per batch and each
batch has a five-minute subprocess watchdog. A timed-out batch is terminated,
committed with `tags_count=-1`, and counted as skipped so the run advances
instead of retrying the same cases indefinitely:

```powershell
python scripts/tag_cases_v2.py --batch-size 10 --batch-timeout 300
```

The watchdog runs matching in a separate process, which allows it to terminate
work that is genuinely stuck on Windows. Successful batches commit their tags
and completion statuses independently. A later invocation resumes only cases
without a status row for `ca_legal_v2_core`:

```powershell
python scripts/tag_cases_v2.py --batch-size 10 --batch-timeout 300
```

For smaller batches or a shorter test timeout:

```powershell
python scripts/tag_cases_v2.py --batch-size 5 --batch-timeout 60 --limit 25
```

To inspect skipped batches:

```sql
SELECT case_id, tags_count, tagged_at
FROM case_tagging_status
WHERE taxonomy_version = 'ca_legal_v2_core' AND tags_count = -1
ORDER BY case_id;
```

Historical V2-core expansion checkpoint: one resumed run recorded 21,710 cases
and 2,051,241 occurrences, with no skipped batches reported at that time. This
is not a current resume cursor; inspect that run's state before considering
recovery.

### Tagging V3 core proposal (activation not established)

The V3 exact-match tagger, `tags_v3` processing stage, and bounded writer exist,
but their activation contract is contradictory as described above. The proposal
requires human review, negative examples, and exact-span fixtures before
activation. No canary, schema migration, or writer command is authorized by
this documentation. The V3 occurrence format includes evidence spans, rule ID,
language, evidence role, source, and taxonomy version; that implementation
detail is not evidence of production deployment.

Outcome intelligence is persisted separately in the versioned `case_outcomes`
table. The metadata payload retains a compatibility mirror, but outcome
analytics should use the dedicated table as its source of truth.

Citation extraction is resolution-free in the V2 Pipeline. It stores every raw
case-law occurrence, normalized form, span, and unresolved state without
looking up target cases. Target resolution runs later as a separate local pass,
after the canonical case corpus is populated, so extraction coverage and
resolution coverage remain independently measurable.
Short-form occurrences may retain a same-document anchor citation and its exact
anchor offsets; this is local extraction provenance, not target-case resolution.

For legacy V2 comparison only, rebuild the 100 most recent cases across the full database:

```powershell
python scripts/tag_cases_v2.py --retag --recent --limit 100
```

The AI proposal reports are discovery-only. A proposal becomes a reviewed core
term only after review, a canonical value and aliases are chosen, and a focused
test is added. The `ca_legal_v2_core` whitelist remains a distinct comparison
layer; more contextual phrases belong in a later advanced layer, not in the V3
proposal.

### Legacy `ca_legal_v2` text/metadata tagger

The following migration and `scripts/tag_cases.py` commands target the older
`ca_legal_v2` tagger, not the `ca_legal_v2_core` whitelist or proposed V3
taxonomy. Treat them as historical maintenance examples; verify the desired
taxonomy, current status, migration, and explicit database scope before use.

Apply the schema:

```powershell
python -m alembic upgrade head
```

Preview without writes:

```powershell
python scripts/tag_cases.py --dry-run --limit 25
```

Run resumably in bounded batches:

```powershell
python scripts/tag_cases.py --batch-size 100 --limit 1000
```

Use `--court`, `--source-type`, or `--retag` to scope or deliberately rebuild the
current version. Bulk tagging should not run concurrently with ingestion-heavy jobs.

The overnight `safe` and `enrich` profiles include the V3 writer. Do not start
either profile until the source-level activation contradiction is resolved and
the profile is reviewed. `--preflight` is not authorization to run its jobs.

## Revision rules

- Add a new taxonomy version for meaning-changing rule revisions.
- Keep categories orthogonal; do not encode several facts into one value.
- Require a matched span or structured metadata field for every tag.
- Test ambiguous acronyms, bilingual terms, line-wrapped PDF text, and negated or
  merely cited concepts before bulk execution.
- Named organizations and countries are mention tags, not findings of fact or law.
- Whitelist aliases may include an acronym/full-name pair, reviewed spelling or
  punctuation variants, and explicit hyphen/space variants when they preserve
  the same meaning. Plurals and adjectival forms are not generated automatically;
  add them only with a canonical-value decision, a false-positive check, and an
  exact-span regression fixture. Do not add substring fragments, generic nouns,
  or ambiguous two- or three-letter acronyms merely to increase coverage.
- Do not activate V3 contextual rules in the first release. Terms such as
  `application`, `decision`, `removal`, `detention`, and `hearing` require actor,
  proceeding, proximity, or evidence-role logic and are backlog work.
- Evaluate precision on a stratified FC, FCA, SCC, RPD, RAD, ID, and IAD sample.
