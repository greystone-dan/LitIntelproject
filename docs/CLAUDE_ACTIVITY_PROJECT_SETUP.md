# Claude Activity Intelligence Project Setup

## Purpose

You are helping build a trustworthy program that turns Federal Court Activity records into useful research and management data.

The dataset contains Federal Court procedural Activity records for Canadian immigration matters. It is not a canonical judgment corpus. Activity records are procedural history, not citations, statutes, judgments, legal advice, or proof that a judgment was captured.

The project goals are to derive evidence-backed data for:

- motions and motion outcomes;
- stays of removal and removal cancellation signals;
- leave applications and leave outcomes;
- hearings;
- final decisions;
- settlements or discontinuances where explicitly recorded;
- filing and procedural dates;
- filing-to-removal, motion-to-removal, and other procedural delays.

Every derived value must remain traceable to its source Activity document.

## Repository

The source repository is the AI CaseLibrary project. Its relevant components are:

```text
backend/database.py                         Activity ORM schema
backend/fc_activity.py                      Activity normalization helpers
scripts/fetch_fc_procedural_history.py      Live Activity collector
scripts/classify_fc_activity.py             Deterministic classifier
scripts/evaluate_fc_activity_deterministic.py  Read-only evaluation
scripts/audit_fc_activity_openai.py         Bounded optional audit
scripts/export_fc_activity_package.py       Read-only handoff exporter
tests/test_classify_fc_activity.py          Classifier tests
tests/test_evaluate_fc_activity_deterministic.py  Evaluation tests
```

The Activity database tables are:

```text
fc_activity_cases
fc_activity_documents
fc_activity_classifications
```

The current full handoff package is:

```text
data/copilot_exports/fc_activity_claude_20260926/
```

## Package Files

Read these files in this order:

1. `manifest.json`
2. `README.md`
3. `cases.jsonl`
4. `documents.jsonl`
5. `classifications.jsonl`
6. this setup document

The full package currently contains approximately:

```text
316,940 cases
3,587,801 documents
218,639 deterministic classifications
315,850 cases with documents
1,090 cases with empty document lists
```

### `cases.jsonl`

One record per `fc_activity_cases` row. Important fields include:

```text
activity_case_id
source_key
citation
imm_number
year
case_name
date_filed
city_filed
nature
case_class
track
source_url
scraped_timestamp
raw_payload
```

### `documents.jsonl`

One record per `fc_activity_documents` row. Important fields include:

```text
activity_document_id
activity_case_id
re_no
docno
doc_dt
recorded_entry
entry_hash
raw_document
```

### `classifications.jsonl`

One deterministic derived record per persisted classification. Important fields include:

```text
classification_id
activity_case_id
source_key
classifier_version
classified_at
classification
```

The nested `classification` object contains evidence-backed statuses and event records. Evidence should retain document IDs, dates, registry identifiers, source text, and rule names where available.

Join documents and classifications to cases using `activity_case_id`. Use `source_key` as the stable source identity. Normalize a leading Unicode U+FEFF character from historical IMM values before matching identifiers.

## Non-Negotiable Evidence Rules

1. Treat `cases.jsonl` and `documents.jsonl` as source evidence.
2. Treat `classifications.jsonl` as derived observations, not authoritative legal conclusions.
3. Do not infer an event merely because a document is missing.
4. Do not infer that an empty `entries_json` means no procedural history exists outside the captured response.
5. Do not treat an Activity record as proof that a judgment, order, or legal outcome was captured.
6. Preserve raw source text and document IDs beside every derived event.
7. Keep filing dates, registry document dates, hearing dates, decision dates, and scheduled removal dates as distinct concepts.
8. Never replace an unknown or ambiguous value with zero, false, or a guessed date.
9. Preserve positive, negative, unknown, and ambiguous states.
10. Keep Activity data separate from canonical cases, citations, statutes, tags, embeddings, and judgment text.
11. Do not request, expose, or invent database credentials, API keys, or `.env` contents.
12. Do not write to the production database while designing or evaluating transformations.

## Claude Project Setup

Create a new Claude Project with a name such as:

```text
FC Activity Intelligence Design
```

Upload first:

```text
docs/CLAUDE_ACTIVITY_PROJECT_SETUP.md
data/copilot_exports/fc_activity_claude_smoke_20260926/manifest.json
data/copilot_exports/fc_activity_claude_smoke_20260926/cases.jsonl
data/copilot_exports/fc_activity_claude_smoke_20260926/documents.jsonl
data/copilot_exports/fc_activity_claude_smoke_20260926/classifications.jsonl
```

Do not upload the 5.8 GB full package to a normal web conversation. Use the smoke package for design and schema review first. Later provide targeted cohorts rather than the entire dataset.

Use this as the Claude Project instruction:

```text
You are the data architecture and research-intelligence partner for the AI
CaseLibrary Federal Court Activity project.

Your job is to help design a reproducible program that converts procedural
Activity records into evidence-backed structured data and management statistics.

Activity records are procedural history, not canonical judgments, citations,
statutes, legal advice, or proof that a judgment was captured.

Always preserve the separation between:
- source cases and raw payloads;
- source procedural documents and raw document payloads;
- deterministic classifications;
- later reviewed or adjudicated interpretations;
- aggregate statistics.

Every proposed derived field must identify its source document ID and preserve
source text or an exact evidence span. Keep filing dates, document dates,
hearing dates, decision dates, and scheduled removal dates distinct. Preserve
unknown, missing, negative, and ambiguous states. Never infer an event from an
empty response or from the absence of a classification row.

Do not write database code, migration code, or production mutation commands
until a schema, evidence policy, and validation plan have been reviewed. Do not
request secrets or database credentials. Do not make legal conclusions.

For each design recommendation provide:
1. source fields used;
2. derived fields created;
3. evidence linkage;
4. confidence or ambiguity handling;
5. validation tests;
6. likely failure modes.
```

## First Claude Conversation

After uploading the files, send:

```text
Read the project setup document, manifest, and sample layers first.

Do not write implementation code yet. Produce a design review covering:

1. the source data model and joins;
2. the distinction between raw evidence and derived classification;
3. classification coverage and missingness;
4. duplicate, BOM, empty-history, and provenance risks;
5. a proposed normalized schema for motions, stays, leave, hearings,
   decisions, settlements, filing dates, and procedural delays;
6. evidence requirements for every proposed field;
7. a staged transformation pipeline;
8. validation tests and a human-review workflow.

Use concrete examples from the sample documents. Flag anything that cannot be
supported by the source text. Do not treat deterministic classifications as
final legal outcomes.
```

## Local Commands

Run these from the repository root in PowerShell.

### Activate the project environment

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
. .\venv\Scripts\Activate.ps1
```

### Recreate a bounded sample

```powershell
$out = "data\copilot_exports\fc_activity_claude_smoke_20260926"
& ".\venv\Scripts\python.exe" scripts\export_fc_activity_package.py `
  --output $out --limit 3
```

The exporter refuses to overwrite an existing directory. Choose a new output
name or remove an intentionally disposable smoke directory first.

### Create the full package

Review disk space before running this command:

```powershell
Get-PSDrive C | Select-Object Name,@{Name="FreeGB";Expression={[math]::Round($_.Free/1GB,2)}}
```

Then run:

```powershell
$out = "data\copilot_exports\fc_activity_claude_$(Get-Date -Format yyyyMMdd)"
& ".\venv\Scripts\python.exe" scripts\export_fc_activity_package.py `
  --output $out
```

### Verify the package

```powershell
Get-Content "$out\manifest.json" -Raw
Get-ChildItem $out | Select-Object Name,@{Name="SizeGB";Expression={[math]::Round($_.Length/1GB,3)}}
```

### Run exporter tests

```powershell
& ".\venv\Scripts\python.exe" -m pytest tests\test_export_fc_activity_package.py -q
& ".\venv\Scripts\python.exe" -m py_compile scripts\export_fc_activity_package.py
```

## Targeted Cohorts

The full package should remain local. For Claude review, prepare focused
cohorts such as:

```text
cases with motion_filed
cases with motion_decision
cases with stay or stay_cancellation
cases with leave_decision
cases with hearing_held
cases with final_decision
cases with removal_scheduled_date
cases with ambiguous or missing dates
cases containing settlement, discontinuance, consent, or withdrawn language
```

The current exporter supports case limits but not semantic event filters. Do
not manually summarize these cohorts without retaining the source document ID
and text. The next implementation step should add reproducible event/year
filters to the exporter, then generate cohort packages for Claude.

## Required Deliverables From Claude

Claude's first design phase should produce:

1. a source-to-derived field mapping;
2. a normalized event schema;
3. an evidence-linkage policy;
4. a confidence and ambiguity model;
5. a transformation pipeline design;
6. cohort definitions for each requested statistic;
7. validation fixtures and negative cases;
8. a proposed API or analytical output contract;
9. a list of unsupported or unsafe inferences;
10. a bounded implementation plan.

No implementation should be considered ready until it can answer:

- Which source document supports this value?
- What exact text supports it?
- Is the value observed, classified, inferred, or reviewed?
- What happens when the source is missing or ambiguous?
- Can the result be reproduced from the raw Activity package?

## Completion Criteria

The project is ready for implementation when Claude and the operator agree on:

- the normalized event schema;
- source evidence and provenance requirements;
- positive, negative, unknown, and ambiguous states;
- cohort and denominator definitions for statistics;
- validation fixtures and acceptance thresholds;
- the boundary between deterministic extraction and human/AI review;
- a read-only prototype that does not mutate PostgreSQL.
