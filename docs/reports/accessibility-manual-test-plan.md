# Accessibility manual test plan

**Purpose:** A repeatable manual follow-up for AI CaseLibrary's generated pages.
This plan is not evidence that the listed tests have been performed or that the
site conforms to WCAG 2.1 AA.

## Before testing

1. Start a local instance using the repository's normal development workflow;
   do not test against production without the owner's approval.
2. Open `/data-explorer`, `/citation-map`, `/case-compare`, `/accessibility`,
   and representative standalone tools such as `/live-analysis` and
   `/citation-pass`.
3. Use a small, known sample so results and map relationships are predictable.
   Record browser, operating system, screen-reader version, viewport, date, and
   outcome for each check. Do not put case text or personal information in notes.

## Keyboard-only pass

1. Reload each page, then use only `Tab`, `Shift+Tab`, `Enter`, `Space`, arrow
   keys, and `Escape` where appropriate.
2. Confirm the first `Tab` reveals “Skip to main content”; activate it and verify
   focus moves to the page's main content.
3. Follow the visible focus indicator through navigation, search suggestions,
   filters, buttons, tabs, dialogs/disclosures, result actions, the inline
   reader, and both case-comparison pickers. Check that focus order follows the
   visual reading order.
4. Operate Citation Map search, mode controls, node details, the “View as table”
   disclosure, and its table content without a pointer. Confirm no keyboard trap.
5. Confirm focus remains visible after actions and returns to a sensible place
   when a panel or disclosure is closed.

## NVDA (Windows)

1. Use a current NVDA release with Firefox or Chrome and enable browse mode.
2. Navigate headings and landmarks; verify each page has a useful page title,
   one primary heading, and a main landmark.
3. Read labels, instructions, validation errors, search suggestions, result
   counts, and state changes while using the page, including case-comparison
   picker results. Record missing or repeated announcements and confusing focus
   changes.
4. On Citation Map, inspect the SVG name/description, then use “View as table.”
   Confirm node names/citations and source-to-target citation links are
   understandable without the graph.

## VoiceOver (macOS/iOS)

1. On macOS, use VoiceOver with Safari; on iOS, optionally repeat the primary
   workflow with VoiceOver and touch exploration.
2. Navigate by headings, landmarks, form controls, and links. Confirm names,
   roles, current/expanded state, and focus changes are announced meaningfully.
3. Operate the skip link, Case Search, reader information tabs, and Citation Map
   table alternative. Record any gesture or rotor navigation that cannot reach
   an equivalent action.

## 200% zoom and reflow

1. Set browser zoom to 200% at a typical desktop viewport, then repeat at a
   narrow viewport without reducing browser text size.
2. Verify text and controls remain readable, headings and dialogs stay visible,
   focus is not clipped, and page actions remain reachable without two-
   dimensional scrolling except for content whose layout inherently requires
   it (such as a graph or wide data table).
3. Confirm the Citation Map can still reach “View as table” and use the text
   alternative when the visual graph requires horizontal scrolling.

## Contrast

1. Use a contrast analyzer on rendered foreground/background pairs for body
   text, links, buttons, focus indicators, error/success messages, inactive and
   active control states, and graph/table labels.
2. Check normal text against the applicable 4.5:1 target and large text against
   3:1; check non-text controls and meaningful graphical boundaries against 3:1
   where applicable.
3. Repeat for hover, focus, selected, disabled, and error states. Do not infer
   contrast compliance from source colors alone when opacity, gradients, or
   overlays change the rendered pair.

## Record and follow-up

For every failed or uncertain step, record the page, steps, expected result,
actual result, browser/assistive-technology version, and a privacy-safe
screenshot or short recording if useful. File a focused issue with the failing
workflow and reproduction details. Rerun the same check after a fix. Do not
describe the project as WCAG-conformant on the basis of this plan or a clean
automated scan.
