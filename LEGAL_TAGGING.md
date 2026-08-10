# Canadian Legal Tagging

## Design

`ca_legal_v2` is a deterministic, additive taxonomy. Every stored tag includes its
case, category, normalized value, confidence score, matched evidence, derivation
source, and taxonomy version. `case_tagging_status` records completed cases even
when no tags were found, making batch runs resumable.

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
- Evaluate precision on a stratified FC, FCA, SCC, RPD, RAD, ID, and IAD sample.
