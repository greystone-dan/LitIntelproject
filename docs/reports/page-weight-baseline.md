# Page weight baseline

Generated: 2026-10-04T14:10:25.274297Z

All HTML is produced offline by calling the listed builder directly. Argument-taking builders use fixed, non-sensitive fixtures; no database, server, browser, or external network access is used. UTF-8 byte counts measure the complete returned HTML; gzip uses level 6 with a fixed timestamp. Inline byte columns count script/style text only (excluding tags, including style attributes). External requests count non-inline resource references declared by resource attributes and CSS `url()`/`@import`; duplicate references are counted individually. This is a template inventory, not a runtime waterfall.

| Page / fixture | Builder | Raw HTML (bytes) | Gzip (bytes) | Inline script (bytes) | Inline style (bytes) | External requests |
|---|---|---:|---:|---:|---:|---:|
| access_login | `backend.main._login_page` | 1216 | 682 | 0 | 628 | 0 |
| case_reader | `backend.case_reader_ui.case_reader_with_statutes_html` | 14162 | 3150 | 7158 | 4942 | 0 |
| citation_map | `backend.pages.citation_map.citation_map_html` | 35609 | 9827 | 23179 | 8447 | 2 |
| citation_pass | `backend.pages.citation_pass.citation_pass_page_html` | 26714 | 7724 | 15826 | 8335 | 0 |
| data_explorer | `backend.pages.data_explorer.data_explorer_page_html` | 582323 | 134683 | 300139 | 126670 | 3 |
| data_explorer_route_builder | `backend.routes._data_explorer_page_html` | 582323 | 134683 | 300139 | 126670 | 3 |
| deidentify | `backend.pages.deidentify.deidentify_page_html` | 20940 | 7122 | 8600 | 5306 | 1 |
| discussion_sandbox | `backend.discussion_units_sandbox.discussion_units_sandbox_page_html` | 584733 | 135324 | 302631 | 126670 | 3 |
| discussion_sandbox_standalone | `backend.pages.discussion_units_sandbox.discussion_units_sandbox_page_html` | 8352 | 2971 | 3784 | 3246 | 0 |
| issue_brief_empty_fixture | `backend.pages.issue_brief.issue_brief_page_html` | 1870 | 906 | 0 | 1399 | 0 |
| judge_outcomes | `backend.pages.judge_outcomes.judge_outcomes_page_html` | 5933 | 2305 | 2075 | 2480 | 0 |
| live_analysis | `backend.pages.live_analysis.live_analysis_page_html` | 23320 | 6436 | 13851 | 6714 | 1 |
| memo_citation_check | `backend.pages.memo_citation_check.memo_citation_check_page_html` | 12178 | 4241 | 5564 | 4150 | 1 |
| prototype | `backend.pages.prototype.prototype_page_html` | 16019 | 4930 | 9776 | 3091 | 0 |
| quick_search | `backend.pages.quick_search.quick_search_page_html` | 6808 | 2445 | 2858 | 2333 | 0 |
| quick_search_route_builder | `backend.routes._quick_search_page_html` | 6808 | 2445 | 2858 | 2333 | 0 |
| research | `backend.pages.research.research_page_html` | 10498 | 3478 | 4183 | 3925 | 0 |
| research_route_builder | `backend.routes._research_page_html` | 10498 | 3478 | 4183 | 3925 | 0 |
| saved_searches | `backend.pages.saved_searches.saved_searches_page_html` | 5189 | 2058 | 3300 | 1210 | 0 |
| statute_viewer_legacy | `backend.case_reader_ui.statute_viewer_page_html` | 5400 | 1545 | 2589 | 1910 | 0 |
| statute_viewer_page | `backend.pages.statute_viewer.statute_viewer_page_html` | 7810 | 2811 | 3023 | 3103 | 0 |
| tag_finder | `backend.pages.tag_finder.tag_finder_page_html` | 6805 | 2393 | 3228 | 2662 | 0 |
| testing | `backend.pages.testing.testing_page_html` | 38622 | 8442 | 22607 | 5778 | 0 |
| theme_explorer | `backend.pages.theme_explorer.theme_explorer_page_html` | 8292 | 2646 | 3765 | 3566 | 0 |

Measured builders: 24; skipped: 0.

## Static asset serving

Data Explorer's `explorer_snapshots.css` and `.js` are served from the `/static/` mount with `Cache-Control: public, max-age=3600`. Starlette `FileResponse` supplies ETag and Last-Modified validators. No-store and attachment responses remain excluded.
