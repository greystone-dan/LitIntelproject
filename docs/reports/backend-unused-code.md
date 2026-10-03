# Backend Unused-Code and Duplicate-Logic Inventory

Read-only inventory of `backend/` for issue #46. No code was changed or removed.

## Method and limits

I listed Python files under `backend/`, collected their top-level declarations,
and traced imports and calls from `backend/main.py`, router declarations in
`backend/routes.py`, page builders, scripts, and tests. Repository-wide symbol
and path searches also covered documentation, generated references, embedded
HTML/JavaScript, and `.swm/` walkthroughs. In particular, the search checked
references that would make a seemingly unused item unsafe to remove.

Static searches cannot prove the absence of dynamic imports, external consumers,
or runtime behavior not represented in the repository. “Safe-to-remove” below
means only that the repository search found no reference; it is not permission
to delete code as part of this inventory.

## Unused or potentially unserved code

| Path and symbol | Evidence | Verdict |
| --- | --- | --- |
| `backend/routes.py::_normalize_whitespace` (line 454) | A repository-wide exact-name search found only its definition. There are similarly named helpers in `backend/reader_service.py`, `backend/citations.py`, and outside `backend/`; none calls this route-local symbol. It has no route decorator, page/template, script, test, or documentation reference. | **safe-to-remove** — only this private helper; do not infer that the other whitespace helpers are unused. |
| `backend/pages/judge_outcomes.py::judge_outcomes_page_html` | No route calls this builder. `backend/pages/__init__.py` imports and exports it, however, and the page’s embedded JavaScript requests `/analytics/judge-outcomes`. `SYSTEM_REFERENCE.md` lists the page module, and `.github/project-manager/tasks/141-remove-judge-outcomes-tab.md` records related route retirement. The active Data Explorer also contains its own judge-outcomes UI. | **unsure** — likely an unserved duplicate page, but the export, embedded endpoint reference, and documentation prevent a safe-to-remove verdict. |

No other complete `backend/` module met the strict “no repository reference”
criterion in this pass. Apparent non-route modules were checked for consumers
from other backend modules, scripts, tests, templates, and docs before
classification; an absence of a route import alone is not treated as unused.

## Duplicate or overlapping logic

| Paths | Evidence and distinction | Verdict |
| --- | --- | --- |
| `backend/legal_tagger.py`, `backend/legal_tagger_v2.py`, `backend/legal_tagger_v3.py` | These are three related deterministic legal-tagging implementations. V1 supplies `LegalTagger` to `backend/metadata_subjects.py` and is also referenced by tagging scripts, tests, and documentation. V2 is used by `scripts/tag_cases_v2.py`, report-cleaning scripts, and `tests/test_legal_tagger_v2.py`. V3 is the active ordered tag stage (`backend/case_processing.py`) and is imported by search, analytics, reader, and citation-map services; V3 also has scripts and tests. V2/V3 share core-tag and exact-match scaffolding, but they load separate taxonomies and expose different metadata/evidence contracts. | **keep** — overlapping taxonomy machinery, but each version has code, test, operational, or documentation references. |
| `backend/routes.py::_normalize_whitespace`, `backend/reader_service.py::_normalize_whitespace`, `backend/citations.py::_normalize_whitespace` | The route and reader helpers both collapse whitespace with `" ".join((value or "").split()).strip()`. The citations helper uses the same operation for non-null strings but does not accept `None`. The route copy has no callers; the reader and citations copies are called within their respective modules. | **safe-to-remove** for the route-local helper only; **keep** the called helpers. |
| `backend/citations.py::_citation_variants`, `backend/live_analysis.py::_citation_variants` | Both create citation lookup variants and include the Federal Court `FC`/`FCT` alias. The citations helper parses formal and reported citation forms for local resolution and is also imported by resolution scripts. The Live Analysis helper normalizes an already-extracted neutral citation and is used only by its local-case resolver. | **keep** — overlapping alias behavior, but the accepted inputs and outputs differ. |
| `backend/metadata_outcomes.py::_sentence_bounds`, `backend/contextual_authority/subthemes.py::_sentence_bounds` | Both locate text boundaries around a match, but the outcome helper uses `.?!` and an explicit start/end span, while the subtheme helper uses `.?!` and whitespace around the match position. Each is called by its own subsystem. | **keep** — similar purpose, different boundary rules and callers. |

## Search evidence

- `find backend -type f` established the backend file inventory; Python AST
  inspection listed top-level functions and classes.
- Repository-wide searches for page-builder imports, route decorators, exact
  candidate symbols, and the `legal_tagger`, `_normalize_whitespace`,
  `_citation_variants`, and `_sentence_bounds` names traced references across
  backend code, scripts, tests, docs, generated API references, and Swimm files.
- Targeted reads of `backend/routes.py`, `backend/pages/__init__.py`,
  `backend/pages/judge_outcomes.py`, the three taggers, `backend/citations.py`,
  `backend/live_analysis.py`, `backend/reader_service.py`,
  `backend/metadata_outcomes.py`, and
  `backend/contextual_authority/subthemes.py` checked the relevant call paths
  and compared the implementations.
