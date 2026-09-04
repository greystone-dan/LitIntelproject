# Canadian Legal Tagging

## Design

`ca_legal_v2` is the legacy deterministic, additive taxonomy. Every stored tag includes its
case, category, normalized value, confidence score, matched evidence, derivation
source, and taxonomy version. `case_tagging_status` records completed cases even
when no tags were found, making batch runs resumable.

### Taxonomy lifecycle

V1 (`ca_legal_v2`) and V2 core (`ca_legal_v2_core`) are retained historical and
comparison layers. V3 core (`ca_legal_v3_core`) is now the active deterministic
runtime taxonomy after its regression, human-review, and bounded-canary gates.
V1 and V2 are not production runtime defaults and must not be treated as the
active taxonomy. Do
not delete either layer or rewrite its rows. New production tagging will move
to the separate `ca_legal_v3_core` version. Contextual tags remain deferred
until a separate contextual evidence contract is designed and validated.

As of 2026-08-04, the live corpus is tagged at scale: all 35,902 cases have
`case_tagging_status` rows and 770,395 tags are stored across the corpus.

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

The full-corpus expansion run was paused after 21,710 cases in its resumed
session, with 2,051,241 occurrences created and no skipped batches reported.
Completed work remains committed and can be resumed with the command above.

### Tagging V3 core layer (active deterministic pipeline)

The `ca_legal_v3_core` layer is implemented as an exact-match tagger in
`backend/legal_tagger_v3.py`, an ordered `tags_v3` stage in
`backend/case_processing.py`, and a bounded writer in
`scripts/tag_cases_v3.py`. It reads
`data/eval/reports/tagging-v3-core-whitelist-proposal.json`, preserves every
matched occurrence, and writes the taxonomy version separately from V1/V2.

Before any canary, apply the additive evidence-contract migration:

```powershell
python -m alembic upgrade head
```

Preview a bounded sample without writes:

```powershell
python scripts/tag_cases_v3.py --dry-run --limit 25
```

The V3 occurrence contract retains category, canonical value, score, exact
evidence, backend-owned offsets, rule ID, language, evidence role, optional
chunk ID, source, and taxonomy version. The writer does not convert matches to
a set or deduplicate repeated spans. The V3 stage is now part of ordered case
processing; the bounded writer remains available for resumable corpus work.
Contextual rules are not part of this first pipeline, and legacy V1 subject
derivation remains separate until the outcome/derived-intelligence pass.

For legacy V2 comparison only, rebuild the 100 most recent cases across the full database:

```powershell
python scripts/tag_cases_v2.py --retag --recent --limit 100
```

The AI proposal reports are discovery-only. A proposal becomes a reviewed core term
only after review, a canonical value and aliases are chosen, and a focused test
is added. V2 is retained for comparison and rollback; it is not the target
production taxonomy. More contextual phrases belong in a later advanced layer,
not in the first V3 core whitelist.

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

The overnight profile remains resumable and safe for ongoing ingestion or rebuilds;
it still runs tagging before chunking and embedding so new content stays consistent:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --continue-on-error
```

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
