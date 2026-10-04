# Generated Research UI Responsive Audit

Date: 2026-10-04
Scope: generated pages under `backend/pages/`, with a focus on usability at
360, 768, and 1280 CSS pixels. This is a static CSS/markup audit, not a live
application or browser-rendering certification.

## Method and acceptance evidence

`tests/test_responsive_generated_pages.py` renders the standalone Python page
builders, extracts inline CSS, and checks each page's viewport metadata,
width-based media rule for its main layout, non-table `min-width` declarations
above 360px, and table wrappers styled with `overflow-x: auto`. It also checks
table wrappers assembled dynamically in Data Explorer and its embedded
analytics. The existing page builders and their UI contracts were reviewed;
their data/API behavior was not changed.

The browser screenshot test is optional. This environment has neither
`/opt/pw-browsers` nor the Playwright Python package, so no screenshots were
produced; the optional test skipped cleanly. Responsive and documentation
contract tests passed (4 passed, 1 skipped). The CSS contract passes are
structural evidence at the requested target widths, not measurements of
rendered geometry or live content. The full suite passed 1,534 tests but had
three failures caused by unavailable DNS for Hugging Face and the OpenAI
tokenizer download; see the merge validation record for the exact test names.

## Page-by-page findings

| Page or embedded surface | Finding and disposition |
| --- | --- |
| Citation Map (`citation_map.py`) | The SVG canvas imposed a 620px minimum inside its own scrollable map. Reduced its minimum to 360px so the map does not force the page wider on phones; its internal pan/scroll affordance remains. |
| Citation Pass (`citation_pass.py`) | Corrected escaped viewport metadata in the generated HTML and added a horizontally scrollable wrapper around the reference table. |
| Data Explorer (`data_explorer.py`) | Added horizontal wrappers to the in-page citation/reference table. Existing responsive search, reader, and panel layouts remain intact; dynamic table surfaces are covered by wrapper assertions. |
| De-identification (`deidentify.py`) | Wrapped the generated review-key table in a horizontally scrollable container. |
| Discussion Units Sandbox (`discussion_units_sandbox.py`) | The rendered page met the static viewport, responsive-layout, minimum-width, and table-wrapper contract; no CSS change was needed. |
| Legal Issue Brief (`issue_brief.py`) | Wrapped its year, court, and authority tables for narrow screens. Kept the existing print stylesheet and explicitly restores visible table overflow for print. |
| Judge Outcomes (`judge_outcomes.py`) | Wrapped the wide outcome table in its own horizontal scroller; the table's 820px minimum remains intentional and isolated from page overflow. |
| Live Analysis (`live_analysis.py`) | The rendered page met the static responsive contract; no responsive CSS change was needed. |
| Memo Citation Check (`memo_citation_check.py`) | The rendered page met the static responsive contract; no responsive CSS change was needed. |
| Research Bench prototype (`prototype.py`) | Added a horizontal table wrapper to the generated table layout. |
| Quick Search (`quick_search.py`) | The existing narrow-screen layout rules passed the static contract; adjusted page-shell padding to retain usable content width. |
| Research (`research.py`) | The rendered page met the static responsive contract; no responsive CSS change was needed. |
| Saved Searches (`saved_searches.py`) | The rendered page met the static responsive contract; no responsive CSS change was needed. |
| Statute Viewer (`statute_viewer.py`) | The rendered page met the static responsive contract; no responsive CSS change was needed. |
| Tag Finder (`tag_finder.py`) | The rendered page met the static responsive contract; no responsive CSS change was needed. |
| Testing (`testing.py`) | The rendered page met the static responsive contract; no responsive CSS change was needed. |
| Legal Themes & Statutes (`theme_explorer.py`) | Added a breakpoint at 800px that stacks the main/sidebar layout and adjusts the statistics grid for narrow screens. |
| FC Analytics (`fc_analytics.py`, embedded partial) | The Data Explorer analytics table is DOM-built; it uses the existing `.fcx-scroll` horizontal container and was included in dynamic-wrapper assertions. It is not a standalone document. |
| Tag Analytics (`tag_analytics.py`, embedded partial) | DOM-built table renderers now place their tables in `.table-wrap` containers; it is not a standalone document. |
| About (`about_content.html`, embedded fragment) | The page is hosted inside Data Explorer. Its comparison table is wrapped by the host builder, and the graph retains its internal scroll wrapper. It is not a standalone document. |

`backend/pages/__init__.py` is a package marker, and
`explorer_snapshots.css` / `explorer_snapshots.js` are assets rather than
standalone pages.

## Deferred checks and residual risk

- No Chromium executable or Playwright package was available, so no browser
  screenshots or live geometry checks were run. Browser-generated screenshots
  belong under `docs/reports/responsive/` when that optional test is available.
- A CSS contract cannot prove that every dynamic state, translated label,
  touch target, or data-dependent chart fits without overlap at 360, 768, and
  1280px. Review those states in a browser before making a visual-conformance
  claim.
- Wide tables intentionally retain their readable intrinsic widths inside
  scroll wrappers. Keyboard and touch discoverability of those scrollers still
  warrants manual browser review.
