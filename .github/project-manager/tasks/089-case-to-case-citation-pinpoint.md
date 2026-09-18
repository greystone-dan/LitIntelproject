Task:
Repair the case-to-case citation layer so act-like parentheticals and anchor phrases such as "the Citizenship Act" are not mistaken for a standalone case citation or a flattened authority label, and ensure nested section references remain attached to the correct case authority.

Why now:
The current report is not a statute-layer issue; it is a case-to-case extraction/anchor issue. We are seeing the citation layer dropping the precise legal anchor and collapsing to a bare act title or generic authority phrase. That creates false confidence in case-to-case intelligence and makes the reader appear to miss real authorities.

Owner surface:
backend/citations.py

Dependencies:
backend/citation_pipeline/, tests/test_citations.py, tests/test_api.py

Risk boundary:
Keep case citations and statute references strictly separate. Preserve exact offsets and source spans. Do not broaden into law parsing or target-resolution changes unless the failing case-citation anchor is isolated and proven.

Smallest falsifiable check:
.\venv\Scripts\python.exe -m pytest tests\test_citations.py -q

Acceptance criteria:
- A case-law reference that includes a generic act-like phrase or nested anchor does not collapse to only the act title.
- The extractor keeps the precise authority text and character span for the case citation.
- Existing citation extraction tests remain green, especially the nested IRPA/IRPR and anchor-preservation fixtures.

Docs/generated references:
- SYSTEM_REFERENCE.md
- docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md

Rollback/recovery:
Revert the local citation regex or anchor-selection change and rerun the same focused pytest target if overlap or false-positive regressions appear.

Evidence:
- The born-failing symptom is a bare act-title collapse, which is not a statute parsing bug but a case-citation anchor defect.
- The focused test slice will validate nested case-authority anchors without changing the statute layer.

Status:
in-progress

Commit allowed: yes
Push allowed: yes
