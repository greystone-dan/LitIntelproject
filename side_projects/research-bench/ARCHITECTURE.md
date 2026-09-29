# Research Bench: feature map and architecture (v0.2, 2026-09-29)

v0.2 changes (Daniel's feedback): three tabs instead of four (Library, Live case tracker, Live analysis); search lives in the header with recent searches in its dropdown; saved searches replaced by search alerts; FCA Activity renamed Live case tracker (tracks FCA and FC files); Live analysis added as a mockup.

Assumption: "the site" is a CanLII-style public case law site (FCA, FC, SCC and IRB decisions). The bench sits beside it as a personal and team workspace. Correct this if you meant a different site.

## 1. Feature map

| Area | What the analyst does | Module |
|---|---|---|
| My Bench | Save a decision, add private notes, tag it, file it in a folder | `LibraryService` (private scope) |
| Team Library | Publish a saved case to the shared library; others add notes, tags, "key paragraph" pins; edit history kept | `LibraryService` (team scope) |
| Annotations | Highlight a paragraph range, attach a comment, label it (supports / adverse / context / distinguish), reply in threads | `AnnotationService` |
| Search (header bar) | Search from any tab; recent searches (last 25) show in the search box dropdown; "Alert me to new decisions" turns a query into a search alert that flags newly released matches | `SearchService` |
| Live case tracker | Track a list of an analyst's own files by docket (FCA and FC); "Check for updates" queries the court source; new docket entries or a new decision raise an alert | `CaseTrackerService` |
| Live analysis | Pick a decision and a provision (and optionally a question); get key paragraphs, how the decision bears on the provision, and passages to watch; add any of them as annotations. Mockup only | `AnalysisService` (stub) |
| Sources | One adapter interface; CanLII, FCA docket, IRB adapters are stubs today | `adapters.py` |

## 2. Architecture

```
 UI (prototype page)            ──►  API layer (api.py, route outline only)
                                         │
      ┌──────────────┬──────────────┬────┴─────────┬───────────────┐
  LibraryService  AnnotationService  SearchService  CaseTrackerService  AnalysisService
      └──────────────┴──────┬───────┴──────────────┴───────────────┘
                        Repository (store.py: interface + in-memory impl)
                            │                              │
                     SQLite / Postgres later        SourceAdapter (adapters.py)
                                                    CanLII | FCA dockets | IRB  (stubs)
```

Design rules
- Services never talk to a court site directly; only adapters do. Swapping a stub for a real client changes no service code.
- Every record carries `owner` and `scope` (`private` or `team`). Team edits are appended to an audit log, not overwritten.
- Annotations anchor to paragraph numbers (the way decisions are cited), not character offsets, so they survive re-downloads.
- Update checks are idempotent: each tracked matter stores a `last_seen` fingerprint; a check reports only entries after it.

## 3. Data model (bench/models.py)

- `Decision`: citation, style of cause, court, date, url, source_id, summary
- `SavedCase`: decision, owner, scope, tags, folder, notes[]
- `Note`: author, body, created, paragraph refs
- `Annotation`: decision citation, para_from, para_to, label, comment, author, replies[]
- `SavedSearch` (used as a search alert): name, query, filters, owner, last_run, last_result_ids
- `RecentSearch`: query, filters, owner, ran_at, hit count
- `TrackedMatter`: docket, style of cause, analyst, court, status, last_seen, alerts[]
- `DocketEntry` / `Alert`: date, text, kind (new entry, decision released, hearing set)

## 4. Update query flow (Live case tracker)

1. Analyst adds a docket to their list.
2. "Check for updates" (or a scheduled job later) calls `CaseTrackerService.check(analyst)`.
3. For each matter, the adapter returns docket entries; entries newer than `last_seen` become Alerts.
4. If an entry is a decision, the adapter fetches it and offers "Save to bench".

## 5. Constraints and open items

- Court sites and CanLII are blocked from this cloud environment, so adapters are stubs returning sample data. A real deployment needs the CanLII API key (CanLII offers an API on request) and a docket source for the FCA.
- Protected B material, internal communications and private ID decisions must never be stored in the Team Library. `LibraryService.publish_to_team` has a hook (`_publish_guard`) for that check.
- Sample records use only public decisions already cited in this project: Wahab 2026 FCA 140, Mason 2023 SCC 21, Weldemariam 2024 FCA 69. Tracked matter dockets in the seed are marked as examples.

## 6. Files

- `bench/models.py` data classes
- `bench/store.py` repository interface and in-memory version
- `bench/adapters.py` source adapter interface and stubs
- `bench/services.py` library, annotations, searches, FCA activity
- `bench/api.py` route outline for a web API
- `bench/seed.py` sample data
- `demo.py` runs the whole flow end to end (`python3 demo.py`)
- `prototype.html` the clickable prototype page
