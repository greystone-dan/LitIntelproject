# Front-end code review

## Summary

Reviewed all 74 tracked text files under `backend/pages/` and `site_assets/`; excluded image and binary assets. No in-scope files were left unread. Findings below are limited to the Federal Court (FC), Federal Court of Appeal (FCA), and Supreme Court of Canada (SCC) workflow. Experimental reader styles are guarded by the Development view.

## Bugs

- `backend/pages/citation_pass.py:2-6,117-158` — **High**. The page is returned from a raw Python string, but its HTML attributes contain backslash-escaped quotes (`class=\"shell\"`, `id=\"liveCount\"`). Those backslashes are emitted literally, so expected attributes and DOM lookups may not work. Remove the backslashes from the HTML markup and verify the resulting page in a browser.
- `backend/pages/data_explorer.py:1409` — **Medium**. Switching to chunk mode builds a replacement citation list only from citations that fit wholly within a chunk; citations without a matching chunk are dropped from `readerState.payload.citations`. Preserve unmatched rows (or keep a separate mapped view) so changing display mode does not lose citations.
- `backend/pages/data_explorer.py:788,1532,1547,1550-1551` — **Medium**. The FC insights heading says the location filter applies, but `loadFcJudges()` removes `city`, and changing the city does not reload the judge table. Apply the location consistently or label the judge table as unfiltered.
- `backend/pages/reader_positions.js:81` — **Low**. The truthiness check on `words().court` changes “Judge” to “Member” whenever that object exists, including court decisions. Check the applicable case type/tribunal rather than object existence.
- `backend/pages/discussion_units_sandbox.py:22-23` — **Medium**. Concurrent searches or case selections can finish out of order and overwrite a newer result/reader with a stale response. Abort the prior request or use a request-generation/current-selection check before rendering.
- `backend/pages/markup_mode.js:52-56,65-76,100-104` — **Possible, Medium**. Each subtheme’s paragraph indices are collapsed to a min–max range, then every paragraph in that range is counted and shown. If a stored subtheme has nonconsecutive indices, unrelated paragraphs will be included. Retain the actual index set and iterate only those paragraphs.

## Security risks

- `backend/pages/data_explorer.py:1009`, `backend/pages/reader_v6.js:91,139` — **Possible, Medium**. Source URLs are HTML-escaped before being inserted into `href`, but their schemes are not restricted. If a stored URL can be controlled by an untrusted source, a `javascript:` URL could execute when clicked. Validate allowed schemes (for example, `https:`) before rendering.
- `backend/pages/live_analysis.py:172` — **Possible, Low**. `library_lookup_error` is concatenated into HTML without escaping, unlike the other dynamic text in this block. Escape it before interpolation; the risk depends on whether the backend error string can contain attacker-controlled text.
- `backend/pages/citation_map.py:12` — **Low**. Lucide is loaded from unpkg without Subresource Integrity. Pin the asset and add SRI/cross-origin attributes, or serve the vetted asset locally.

## Accessibility / UX

- `backend/pages/deidentify.py:35,119-123,167-174` — **Medium**. The `deidText` and `restoreText` textareas have no associated labels, and the file inputs use `display:none`, removing them from keyboard focus even though they are nested in labels. Associate visible labels with the textareas and use a visually hidden, focusable file input with a visible focus indicator.
- `backend/pages/citation_map.py:49-50` — **Medium**. SVG case-node groups respond to pointer clicks/double-clicks but are not focusable and have no keyboard activation. Give nodes accessible names, focusability, and Enter/Space handlers, or provide an equivalent keyboard-operable list.
- `backend/pages/data_explorer.py:1386-1388,1534,1546` — **Low**. Citation detail tooltips are triggered only by mouseover, and FC table sorting is attached to non-focusable `<th>` elements. Add focus/keyboard support for citation details and use buttons (with sort state announced) in sortable headers.
- `backend/pages/site_tour.js:293,331-345` — **Medium**. The tour card has `role="dialog"`, but the input guard explicitly allows Tab and there is no focus trap. Keyboard users can tab into the page behind the tour. Keep focus within the dialog/dock while it is open and restore focus when it closes.
- `backend/pages/tour_window.html:159` — **Medium**. The fixed 1440×900 stage is scaled to fit both viewport dimensions; on a narrow phone this can shrink the screenshot text to only a few pixels. Use a phone-specific layout or provide zoom/reflow and readable text outside the scaled screenshot.

## Performance

- `backend/pages/tour_window.html:232-236` — **Medium**. Tour startup eagerly creates an image request for every distinct screenshot (`tour_data.json` currently supplies about 145). Load the first/nearby steps initially and preload later images on demand or in small batches.

## Dead code / cleanup

- `backend/pages/data_explorer.py:977,1000-1001` — **Low**. The capture-phase submit listener calls `stopImmediatePropagation()` before the legacy form `onsubmit` handler can run, leaving `loadSearch()` and its `resultCard()` renderer unreachable through the form. Remove the obsolete path or reconnect it if still intended.

## Suggestions

- `backend/pages/data_explorer.py:1-1849` — **Low**. The page builder contains a very large inline UI implementation. Consider moving stable JavaScript/CSS blocks into static assets to make the active workflow easier to review and maintain.
- `backend/pages/about_how.html:80` — **Possible, Low**. “Every immigration file” is an absolute description of Federal Court docket coverage, but the page does not state a measured coverage boundary. Qualify it with the verified scope and an as-of date.
