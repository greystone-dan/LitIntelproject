# iLIT UI sweep: bug list

Scripted sweep of https://www.ilit.ca on 2026-09-29, no models. Six pages (/data-explorer, /about, /citation-intelligence, /discussion-units-sandbox, /citation-map, /live-analysis) at desktop (1366x850) and phone (iPhone 13) sizes. Every visible button, link and tab was clicked, each page and tab was scrolled, and console errors, dead clicks, covered controls, layout shift, overflow and load times were logged. Read-only: nothing was saved, uploaded or submitted. The only thing typed in was a case search for "Vavilov".

Screenshots are in `shots/`. Raw output is in `results/<run>/summary.md` and `findings.json`. To rerun: `bash run.sh` (or `PAGES=/citation-map bash run.sh` for one page).

## High

**1. The top tabs often don't switch the panel, and they break for the rest of the visit.**
Pages: /data-explorer and every page using the same tab bar (/about, /citation-intelligence, /discussion-units-sandbox), desktop and phone.
Steps: open /data-explorer, click RESEARCH BENCH, then click JUDGE PROFILE. The page still shows Research Bench, and the Research Bench tab stays underlined. On a fresh load, clicking JUDGE PROFILE first leaves "Find a decision" showing.
Cause (from the console): `Cannot set properties of null (setting 'hidden')` in `selectTab` (data-explorer, line 1069). The tab code looks for a panel element that isn't on the page, throws, and stops before hiding the old panel. Only a reload recovers.
Shots: `shots/judge-profile-phone.png`, `results/2026-09-29T12-11-08-119Z/shots/005-data-explorer-desktop-tab-judge-profile.png`

**2. Citation Map is frozen for about 5 to 10 seconds after it loads, with no sign why.**
Page: /citation-map, desktop and phone.
Steps: open /citation-map and click a starting point (e.g. Dunsmuir) or a detail tab (Context, Common) in the first few seconds. Nothing happens. The whole page is dimmed (`main.shell.loading`, opacity 0.55, pointer-events off) but there is no spinner or message, so it reads as broken. It becomes clickable after about 10 seconds.
Shots: `shots/citation-map-desktop.png` (the dimmed state)

**3. On phones, the header eats the top of the screen and the tab bar is cut off.**
Page: /data-explorer (and pages sharing its header), phone.
The logo and "Immigration Litigation Intelligence System" wrap to four lines, and the nav links wrap to two. Together they take about 20% of the screen. The top tab bar is cut off at "SITE ARCHITE", with no arrow or fade to show that it scrolls, so JUDGE PROFILE, FC HISTORY and LEGAL THEMES are hidden.
Shot: `shots/phone-header-and-tabs.png`

## Medium

**4. Citation Map shows "?" where a dash should be.** Examples: "Dunsmuir ? 2008 SCC 9", "Five influential authorities ? double-click a node to expand", "incoming ? 231". This is a character-encoding problem: an em dash or middle dot is being served as "?". Shot: `shots/citation-map-question-marks-phone.png`

**5. On phones, the Citation Map toolbar runs off the right edge.** The reset and refresh buttons are half off-screen, and the second starting-point card is clipped. Same shot as item 4.

**6. "Refresh map" does nothing when clicked** (desktop and phone): the page doesn't change and gives no feedback. It may need a selected case first, but then it should be disabled or explain why. Shot: `shots/citation-map-refresh-dead.png`

**7. The navigation is different on every page.**
- /data-explorer: Research, Sandbox, Citation Map, Live Analysis, Case Reader.
- /citation-map: Research, Citation Intel, Citation Map, Live Analysis, Case Reader, About, plus site stats.
- /live-analysis on phone: three unlabeled arrow icons.
- "Research" and "Case Reader" both go to /data-explorer.
- /discussion-units-sandbox shows two "Sandbox" links.

Shot: `shots/live-analysis-phone.png`

**8. On phones, the Live Analysis controls row is cramped.** The Analyze and Clear buttons, the checkbox and the status text are squeezed into one row. "Extraction runs first;" wraps to one word per line, and "No document" is cut off. The checkbox is 13x13px. Shot: `shots/live-analysis-phone.png`

**9. On phones, the "How it works" diagram in About is cut off at the right edge**, with no cue that it scrolls. Shot: `shots/about-after-anchor-phone.png`

**10. The Citation Map details panel scrolls inside the page (double scroll).** On desktop, the Related tab puts about 2,800px of content in a 550px inner scroll box. You have to aim the mouse at the panel to read it.

## Low

**11. Tap targets on phones are too small** (under the 32px guideline): top nav links are 29px tall, statute chips in Legal Themes are 25px, map detail tabs are 31px, "Find common citers" is 25px, the map's "Inspect" buttons are 34x13px, and the Live Analysis checkbox is 13x13px.

**12. Some clicks are slow and give no feedback.** Issue Map took 3.0s to respond on phone. Case Explorer and Links took about 1.6s. There's no loading indicator in between.

**13. Pages never go quiet on the network.** Something keeps polling after load. Pages paint in about 1 to 2s (DOMContentLoaded), so users won't notice much, but it wastes battery and data on phones.

## Not yet connected (behaviour only, per Daniel)

- **Research Bench** renders as a concept page. Its three sub-tabs (Library, Live case tracker, Live analysis) switch correctly. The grey chips (Private saves, Folders and tags, Supports, Adverse...) look like buttons but aren't clickable. Opening this tab is the easiest way to trigger bug 1. Shot: `shots/research-bench-desktop.png`
- **Judge Profile, FC History, Legal Themes, Citation Intelligence**: each panel's button (Find judge, Fetch history, Analyze statute, Find case, the statute chips) responded when clicked with the box empty. No errors came from these panels themselves; the errors were from bug 1. Their results weren't judged.
- **Site Architecture** opens but has no controls to test.

## What came back clean

- No page is wider than the screen at either size (item 9 is inside a clipped box).
- No scroll traps: mouse-wheel and touch scrolling reach the bottom of every page and tab.
- No layout shift over 0.1 on load. No broken images.
- Case search works: suggestions appear after typing "Vavilov", and Enter shows results.

## Sweep limits

- About's in-page section links were only partly tested, because each jump scrolls the rest out of reach.
- "Reset map" was skipped by the read-only guard.
- Forms were not filled beyond the one case search.
- Cloudflare's analytics beacon was blocked during the run.
