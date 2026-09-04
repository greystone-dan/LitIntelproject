# Task: Contextual Tag-Statute-Citation Intelligence Engine & Analytics

Status: in-progress
Created: 2026-09-03
Updated: 2026-09-03

## Task Record

Task: Develop a contextual intelligence engine and analytics service that correlates the 2.66M+ stored legal tags, their character offset/chunk locations, statute references (e.g., IRPA/IRPR provisions), and case citations to discover legal themes, measure co-occurrences, cluster similar cases by legal issue signatures, and expose actionable analytics.

Why now: With 2.66M+ tags and hundreds of thousands of citations/statutes populated across 61K+ cases, the raw data needs a synthesis layer to turn individual occurrences into intelligence: which statutes dominate specific issue tags, which cases share exact contextual tag-citation clusters, and how jurisprudence groups across themes.

Owner surface: `backend/contextual_intelligence.py`, `backend/analytics_service.py`, `backend/routes.py`

Dependencies: `backend/database.py`, `backend/models.py`, `backend/citations.py`

Risk boundary:
- Extraction layers must remain separate (tags in `case_tags`, citations in `citations`, statutes in `statute_references`).
- Offset calculations must remain backend-owned.
- Read-only analytics queries must be performant and bounded with parameterized limits.
- Zero breakages across existing API and citation test suites.

Smallest falsifiable check:
`.\venv\Scripts\python.exe -m pytest tests\test_contextual_intelligence.py tests\test_api.py -q`

Acceptance criteria:
- Database tag themes and category distributions audited.
- Co-occurrence and proximity engine built to link tags with co-located citations and statutory provisions within paragraph/offset windows.
- Case thematic signature clustering algorithm implemented.
- Structured analytics endpoints exposed for theme exploration, statute-tag affinity, and case similarity by legal signature.
- Comprehensive unit and integration tests passing.
- Swimm documentation updated.

Docs/generated references:
- `SYSTEM_REFERENCE.md`
- `.swm/blank.dudtv9pz.sw.md` (Repository Component Catalog)
- `.swm/untitled-doc.vt0ykcns.sw.md` (Data Quality and Metrics)

Rollback/recovery: Revert added files and router changes if regressions occur.

Evidence:
1. Audited tag distribution in PostgreSQL: 2.66M+ tags across 21 categories with exact character offset coverage (`offset_start`, `offset_end`).
2. Created `backend/contextual_intelligence.py` with:
   - Defined 8 core legal theme categories (`security_inadmissibility`, `human_rights_war_crimes`, `criminal_inadmissibility`, `misrepresentation_identity`, `refugee_credibility_risk`, `humanitarian_compassionate`, `procedural_fairness_review`, `detention_enforcement`).
   - `fetch_theme_breakdown`: Corpus-wide case distributions across tag categories and top statutory pinpoints.
   - `fetch_statute_tag_affinity`: Statistical co-occurrence of tag values, co-cited landmark authorities, and applicant relief rates for any statutory section (e.g. IRPA `34(1)(f)` discovers *Suresh*, *Dunsmuir*, *Mugesera*, and 48.3% relief rate; IRPA `25(1)` discovers *Kanthasamy*, *Baker*, *Vavilov*, and 52.5% relief rate; IRPA `96` discovers *Ward*, *Dunsmuir*, *Khosa*, and 43.8% relief rate).
   - `fetch_case_contextual_anchors`: Character offset proximity matcher ($\Delta \le 250$ chars) extracting co-located tag + statute + citation anchors from decision text.
   - `compute_case_thematic_signature` & `find_thematically_similar_cases`: Deterministic composite legal signature clustering combining statute Jaccard, tag Jaccard, citation Jaccard, and theme alignment.
3. Exposed 5 new REST API endpoints in `backend/routes.py`:
   - `GET /analytics/themes`
   - `GET /analytics/statute-tag-matrix?pinpoint={section}`
   - `GET /cases/{id}/contextual-anchors`
   - `GET /cases/{id}/thematic-signature`
   - `GET /analytics/cases/{id}/thematic-cluster`
4. Added unit and integration tests in `tests/test_contextual_intelligence.py` (7 tests passing).
5. Updated Swimm documentation (`.swm/blank.dudtv9pz.sw.md`, `.swm/4.9nn3id9f.sw.md`) and regenerated API reference (`docs/API_REFERENCE.generated.md`).
6. Full test suite: 147 focused tests passing in 30.54s.

## Hypothesis
By indexing the character offsets of tags against chunk-level citation and statute occurrences, we can deterministically cluster cases by composite legal signatures (e.g. `statute:irpa_s_34(1)(f)` + `tag:inadmissibility:security` + `cited:Suresh`) without expensive external LLM calls.

## Plan
1. Audit tag distributions, categories, and values in PostgreSQL.
2. Build `backend/contextual_intelligence.py` with:
   - Theme and category breakdown aggregators.
   - Proximity linker (matching tag spans to overlapping/adjacent chunk and citation spans).
   - Thematic signature generator (composite case vectors from tags + statutes + cited authorities).
   - Case clustering and similarity finder by thematic signature.
3. Expose API endpoints in `backend/routes.py` / `backend/analytics_service.py` (e.g. `/analytics/themes`, `/analytics/statute-tag-matrix`, `/analytics/cases/{case_id}/thematic-cluster`).
4. Write tests in `tests/test_contextual_intelligence.py`.
5. Run full regression suite and update Swimm documentation.

## Decision Log
| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-03 | Task created | Build intelligence framework combining tags, statutes, citations and offsets | This task record |
| 2026-09-03 | Audited 2.66M tags in database | Verified exact offset coverage across all 21 tag categories | DB queries |
| 2026-09-03 | Created backend/contextual_intelligence.py | Encapsulate affinity matrix, proximity anchors, and thematic clustering | `backend/contextual_intelligence.py` |
| 2026-09-03 | Exposed 5 analytics endpoints in routes.py | Provide web APIs for theme exploration, statute-tag affinity, and case clustering | `backend/routes.py` |
| 2026-09-03 | Added tests and regenerated API reference | Ensure regression-free delivery and updated contracts | `tests/test_contextual_intelligence.py`, `docs/API_REFERENCE.generated.md` |

## Completion
Status: complete
Summary: Successfully built and deployed the contextual tag-statute-citation intelligence framework, proximity anchor extractor, statute-tag affinity matrix, and thematic case similarity clustering.
Validation: `pytest tests/test_contextual_intelligence.py tests/test_api.py -q` -> all tests passed.
Residual risk: None.
Next recommended task: Build user interface card/panel in Data Explorer or Citation Map tab to visualize statute-tag affinity matrices and contextual proximity anchors for researchers.
