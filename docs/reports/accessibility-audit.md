# Accessibility audit: research and citation HTML builders

**Audit date:** 2026-10-03
**Target:** WCAG 2.1 AA
**Status:** Static review with surgical fixes; not a conformance certification.

## Scope and method

Reviewed the generated HTML and relevant source for:

- `backend/pages/data_explorer.py`: Case Search, inline case reader, Judge
  Profile, and citation-related views.
- `backend/pages/citation_map.py`: citation graph and case search.
- `backend/pages/citation_pass.py`, `backend/pages/live_analysis.py`, and
  `backend/pages/quick_search.py`: citation-oriented QA, temporary analysis, and
  supporting search builders.
- `backend/case_formatter.py` and `tests/test_case_formatter.py`.

The review inspected static builder output and the source templates, including
an HTML-parser inventory of exposed form controls in the standalone builders.
Dynamic JavaScript-rendered content was inspected selectively, not exhaustively.
No browser, keyboard-only, screen-reader, contrast-measurement, zoom, or
touch-target test was run.

## Findings and disposition

| Page | Issue / audit result | WCAG 2.1 AA item | File and line | Fix size |
| --- | --- | --- | --- | --- |
| Data Explorer — Case Search and Judge Profile | Search inputs already have programmatic labels; search and result controls now have explicit visible keyboard focus. | 1.3.1 Info and Relationships; 2.4.7 Focus Visible | `backend/pages/data_explorer.py:208-209, 440, 559` | Small — focus fixed; labels already present |
| Data Explorer — inline case reader | Information-view controls expose their active state with `aria-pressed`; keyboard focus is visible. Cited-paragraph shading pairs `#fff9e8` with `#202522` text (14.8:1); linked-case pinpoint shading pairs `#fff4c2` with `#202522` paragraph-number text (14.06:1). | 1.4.3 Contrast (Minimum); 2.1.1 Keyboard; 2.4.7 Focus Visible; 4.1.2 Name, Role, Value | `backend/pages/data_explorer.py:167, 209, 287, 722, 1057-1061` | Small — fixed |
| Citation Map — case search | Search previously relied on its placeholder for its accessible name; it now has an explicit `aria-label` and visible focus. | 2.4.7 Focus Visible; 4.1.2 Name, Role, Value | `backend/pages/citation_map.py:27, 34` | Small — fixed |
| Citation Map — mode and detail controls | Active state was conveyed only by a CSS class; controls now initialize and synchronize `aria-pressed`. Buttons, links, and selects have explicit focus styles. | 2.4.7 Focus Visible; 4.1.2 Name, Role, Value | `backend/pages/citation_map.py:28, 69-100` | Small — fixed |
| Citation Map — graph | SVG has a generic accessible name, but an equivalent description of the changing graph and its relationships was not verified. | 1.1.1 Non-text Content; 1.3.1 Info and Relationships | `backend/pages/citation_map.py:35` | Larger — defer pending browser/assistive-technology review |
| Search, reader, judge, and citation views | No clear static defect was identified for heading hierarchy, link text, or table headers. Narrow-screen CSS exists, but rendered reflow and usable keyboard order were not verified. Other shading and tag color combinations were not measured. | 1.3.1 Info and Relationships; 1.4.3 Contrast (Minimum); 1.4.10 Reflow; 2.4.3 Focus Order; 2.4.4 Link Purpose; 2.4.6 Headings and Labels | `backend/pages/data_explorer.py:1-1062`; `backend/pages/citation_map.py:4-101`; `backend/pages/citation_pass.py:1-195`; `backend/pages/live_analysis.py:4-48`; `backend/pages/quick_search.py:4-272` | Not sized — manual browser review needed |

The explicit control-name inventory found no unnamed exposed form controls in
the inspected standalone Citation Map, Citation Pass, Live Analysis, and Quick
Search builders. The two cited-paragraph text/shading pairs above exceed 4.5:1;
this does not verify all tag colors or rendered states.

## Positive observations

- Case Search and Citation Intelligence inputs have associated labels; Judge
  Profile search is labeled “Find a judge by name.” The primary case query
  exposes combobox semantics and its suggestion options expose selected state.
- The inline reader evidence tabs expose tab roles and `aria-selected`; the
  information-view buttons now expose pressed state.
- Citation Map mode and detail-view buttons now expose pressed state matching
  their active styling.
- The static control-name inventory found no unnamed exposed form controls in
  the inspected standalone Citation Map, Citation Pass, Live Analysis, and
  Quick Search builders. Citation Map's SVG already has `role="img"` and an
  accessible name.
- `backend/case_formatter.py` classifies source text into typed blocks and
  backend-owned offsets; it does not emit HTML or controls. No accessibility
  markup change was appropriate there.

## Validation and limitations

Passed:

- `python -m pytest -q tests/test_accessibility_builders.py tests/test_case_formatter.py`
  — 9 passed.
- `python -m compileall -q backend/pages/data_explorer.py backend/pages/citation_map.py backend/pages/citation_pass.py backend/pages/live_analysis.py backend/pages/quick_search.py backend/case_formatter.py tests/test_accessibility_builders.py`
  — passed (the existing invalid-escape `SyntaxWarning` in
  `backend/pages/data_explorer.py` remains).

Blocked environment checks:

- `python -m pytest -q tests/test_feature_tabs.py -k 'search_fields_have_keyboard_visible_focus_treatment or case_search_has_clear_primary_query_and_filter_state'`
  could not collect because `httpx` is not installed. The new isolated builder
  tests and formatter tests passed without importing the full API application.
- `python scripts/check_generated_docs.py` could not complete because its API
  and schema generators require unavailable `fastapi` and `sqlalchemy`
  packages. No API/schema/script-catalog references were changed.
- The `SYSTEM_REFERENCE.md` Research UI appendix was regenerated from
  `docs/RESEARCH_UI_GUIDE.md` using the existing `embedded_document` generator
  function; unrelated stale appendix sections were left untouched.

This review cannot establish full WCAG 2.1 AA conformance. Dynamic search
suggestions/results, live announcements, graph alternatives, keyboard behavior
across all views, color contrast in rendered states, zoom/reflow, mobile
touch-target sizes, and screen-reader behavior remain unverified. The next
bounded check is a browser keyboard and screen-reader review of Data Explorer
search/reader and Citation Map at desktop and narrow viewports.
