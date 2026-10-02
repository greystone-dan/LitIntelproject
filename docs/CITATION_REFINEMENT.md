# Citation and statute refinement (step 2)

`backend/citation_refine/` is a second pass over citation extraction. It does not change
pass one (`backend/citations.py`). It takes pass one's rows and the full decision text,
then returns corrected rows. Each row records the step that produced it, what that step
did, and a confidence score. Nothing in the package writes to the database.

## Why

The goal is to link every citation to a **case paragraph** or a **statute provision** in
the database. Pass one loses links at four stages:

| Stage | Cases (before) | Laws (before) |
|---|---|---|
| Find | French cites, old reporters, Quicklaw numbers, Ibid/supra, `R v.`, `Re X` missed | "s. 112 of the Act" saved as "of the Act"; French references missed |
| Identify | parallel citations dropped | "IRPA ss. 96, 97" kept with **no section**; many instruments unknown |
| Match | one citation per case; short forms re-matched by name | lists and ranges never linked |
| Pinpoint | only the first paragraph of "paras 85-87 and 99"; pages never | section text only, no subsection or paragraph level |

## Layers and steps

Each step has a name and can be switched on or off by itself.

**Case layer** (`cases.py`)

| Step | What it does |
|---|---|
| `C1_gap_scan` | all Canadian neutral court codes, including French (CSC, CAF, CF); S.C.R./F.C./F.C.R./Imm. L.R./D.L.R./F.T.R./N.R. and more; `[2003] F.C.J. No. 123`; `R v.`, `Re X`, `X (Re)`, French `c.` names; docket numbers (IMM-1234-22). Also replaces malformed pass-one spans |
| `C2_backrefs` | Ibid, Id., "Name, supra (note 4)", "above", "précité", each linked to the case it points back to |
| `C3_parallel` | name + neutral + S.C.R. + D.L.R. + CanLII joined into one row; every citation becomes a lookup identifier |
| `C4_pinpoints` | structured pinpoints: paragraph lists and ranges, and pages (`at p. 841`, `at 841`) |
| `C5_validate` | year checked against the court's first neutral-citation year; out-of-range pinpoints flagged; self-citations dropped |

**Law layer** (`laws.py`, `instruments.py`, `context.py`)

| Step | What it does |
|---|---|
| `L1_definitions` | reads the whole decision for "the Act" / "[IRPA]" / "the Regulations" definitions; defaults to IRPA/IRPR in immigration decisions; drops pass-one junk such as "of the Act" |
| `L2_gap_scan` | "s. 112 of the Act", "r. 117(9)(d) IRPR", "Rule 9 of the … Rules", French "l'article 25 de la LIPR", "alinéa 36(1)a)", "art 1E" |
| `L3_expand` | "ss. 96, 97", "ss. 112 to 114", "36(1)(a) and (b)" become one row per provision. Rows from one list share `group_start`/`group_end` |
| `L4_registry` | extended registry: Federal Courts immigration Rules; RPD, RAD, ID and IAD Rules; Interpretation Act; Constitution Acts; CAT; ICCPR; Convention on the Rights of the Child; Protocol; French names |
| `L5_validate` | drops sentence fragments; keeps unknown law names at low confidence; flags provision numbers beyond the instrument's range |

**Linking** (`resolution.py`), run on the database machine:

- Cases: match on every identifier. Short forms and Ibid/supra take their anchor's target. A name-and-year match is used only when it is unique. Dockets match `cases.docket_number`.
- Paragraphs: every paragraph in the pinpoint is linked to its paragraph chunk. Results are `resolved`, `partial`, `beyond_target`, `page_unmapped` (pages are reported, never guessed) or `no_paragraph_index`.
- Statutes: `split_section_text` builds the subsection, paragraph, subparagraph and clause tree from stored section text, so `36(1)(b)` links to the exact clause (`resolved_provision`), or to the deepest level found (`partial_provision`).

## Trying it

```python
from backend.citation_refine import refine_document
result = refine_document(case.full_text, source_citations=[case.citation, case.secondary_citation])
result.cases.rows, result.laws.rows, result.summary()
```

Shadow report (read-only):

```
./venv/Scripts/python.exe scripts/evaluate_citation_refinement.py --text-file decision.html
./venv/Scripts/python.exe scripts/evaluate_citation_refinement.py --limit 200 --resolve
```

`--resolve` compares link rates for pass one and step 2 (cases, paragraphs, provisions).
Its output goes to `data/eval/reports/citation_refinement/`.

Limit steps with `steps=[...]` or `CASELIBRARY_CITATION_REFINE_STEPS` (`all`, `none`, or a
comma list such as `C1_gap_scan,L3_expand`).

## How to merge later

The layers are built so each merge step is small and can be reversed.

1. **Shadow run.** On Daniel's machine, run the evaluation script with `--resolve` on a sample.
   Compare against the gold sets (`scripts/evaluate_fc_citation_extraction.py`), then turn
   off any step that adds wrong rows.
2. **Case writer.** In `backend/citations.py`, `rebuild_citations_for_case` calls
   `extract_case_citation_matches(case_text)`. Replace that call with:

   ```python
   refined = refine_case_citations(case_text, source_citations=[case.citation, case.secondary_citation])
   matches = [row.to_raw_match() for row in refined.rows if row.kind in CASE_CITATION_KINDS]
   ```

   `to_raw_match()` returns the pass-one shape, so the rest of the writer is unchanged.
   Keep `docket` rows out until a column or table exists for them.
3. **Statute writer.** In `rebuild_statute_references_for_case`, run
   `refine_statute_references(case.full_text)` once on the whole text, not per chunk, so
   definitions are visible. Map each row to its chunk by offset, the same way case
   citations already are. Write `instrument_key`, `section`, `subsection` and `paragraph`
   from the refined row instead of re-parsing `normalized_citation`.
4. **Database columns.** Add these with an Alembic migration:
   - `citations`: `pinpoints` (JSON list), `pinpoint_kind`, `refine_step`, `confidence`, `identifiers` (JSON)
   - `statute_references`: `refine_step`, `confidence`, `group_start`, `group_end`, `group_index`
   - a `legislation_provisions` table filled from `split_section_text`

   `citations.provenance` can mark refined rows (`refine_v1`) during the switch-over.
5. **Linking.**
   - `scripts/resolve_citation_targets.py`: use `resolution.load_case_index` + `resolve_case_rows`.
   - `scripts/link_citation_pinpoints.py`: write one link per paragraph from `CaseResolution.paragraphs`. This may need a `citation_paragraph_links` table, because `target_paragraph` holds one number.
   - Statute rows: `resolve_statute_rows` with `statute_lookups_from_session`.
6. **Registry.** Move `instruments._EXTRA_INSTRUMENTS` and `_EXTRA_ALIASES` into
   `backend/statutes.LEGISLATION_REGISTRY` once the new instruments have been indexed.
7. **Retire duplicates.** Once step 2 is on everywhere, pass-one pieces it supersedes can be
   removed one at a time:
   - `_extract_anchored_provision_candidates`, which re-scans the text and is slow on whole decisions
   - the legacy path's broken `_extract_case_chain_candidates`

Run the case and law layers together through `refine_document`. It also stops a case row
and a law row from claiming the same words.
