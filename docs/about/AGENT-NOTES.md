# iLit About page: notes for a coding agent

This folder holds the iLit status overview, styled to match the ilit.ca explorer (`backend/pages/data_explorer.py`). It is meant to fill the empty **About** tab on `/data-explorer`.

## Files

| File | What it is |
|---|---|
| `ilit-about-fragment.html` | **The drop-in.** A `<style>` block plus `<div class="ilit-about">…</div>`. Paste it into the About tab's panel. All CSS is scoped under `.ilit-about`, so it won't touch the site's own `.tag`, `.eyebrow`, `.card` or `h1` rules. There is no JavaScript. It relies on the fonts the explorer already loads (IBM Plex Sans, Newsreader). |
| `ilit-overview.html` | A standalone preview of the same fragment on the site's cream grid background. Open it in a browser to see the target. |
| `src/brief.css` | The scoped stylesheet. |
| `src/brief_body.html` | Page text, with `{{FIG1}}`…`{{FIG9}}` placeholders for the diagrams. |
| `src/build_brief.py` | Python 3, no dependencies. It draws the nine SVG diagrams, fills the placeholders and writes both HTML files above. Run `python3 src/build_brief.py` after editing text or CSS. |

## Wiring it into the About tab

The About tab is currently empty, and "Site Architecture" says its content moved there. Suggested approach:

1. Store the fragment as a string or template file, for example `backend/pages/about_content.html`.
2. Inject it into the About tab's panel element in `data_explorer.py`.
3. Keep the fragment's `<h1>` as is, or change it to `<h2>` if the page header's `<h1>` ("Immigration Litigation Intelligence Tool") should stay the only one.
4. The in-page jump links (`#today`, `#how`, …) use plain anchors. If the explorer's tab switching intercepts hash changes, either turn them into `scrollIntoView` handlers or drop `nav.jump`.
5. Separately, fix the `#judgePanel` error in `selectTab`, so the About tab can open without the red error text above it.

## Design tokens (copied from the site)

These are defined on `.ilit-about`, not `:root`. The site is light-only, so there is no dark mode.

| Token | Value | Meaning in the page |
|---|---|---|
| `--bg` | `#f1efe8` | page ground (the preview adds the site's 26px grid) |
| `--surface` / `--surface-alt` | `#fffef9` / `#f8f6ef` | cards, tables, figure panels / table headers |
| `--border` | `#d8d5ca` | all borders; radius is 5px everywhere, with no shadows (same as the site's `.panel-card`) |
| `--text` / `--muted` | `#202522` / `#69726d` | body / secondary text |
| `--rust` / `--rust-soft` | `#a4412b` / `#f7e8e3` | brand accent: eyebrows, kickers, the active underline; also the colour for **Federal Court docket and internal material** in diagrams |
| `--blue` / `--blue-soft` | `#315d8d` / `#e7eef6` | **citations and case law** |
| `--teal` / `--teal-soft` | `#176c68` / `#edf5f3` | links, "Built", "Yes" |
| `--amber` / `--amber-soft` | `#8a6418` / `#f8f0dc` | limits and caveats (the site's `#c28e2d`, darkened so text passes contrast) |

Type:

- Headings are **Newsreader** 700.
- Body text is **IBM Plex Sans**.
- Kickers, table headers, tags and the jump nav use small uppercase letter-spaced labels, like the site's tabs.

## Components

All components are under `.ilit-about`:

- `.big` stat row (`.big.three` for 3 cells; `.d` / `.a` colour a number rust or blue)
- `.ask` callout with a rust left rule
- `.compare` scrollable table, with `span.yes` / `span.no`
- `.cards` / `.cards.two` / `.card`, with `.tag.ok` / `.tag.part` / `.tag.gap`
- `.ba` before/after grid
- `.status` rows
- `.note` caveat
- `details` FAQ
- `figure` > `.svgwrap` > `svg`

One column under 820px, and no horizontal page scroll at 390px. Wide figures and tables scroll inside their panel.

## Diagrams

The `Svg` helper in `build_brief.py` draws them:

- `box()` draws a box with a title and sub-lines.
- `line()` draws an arrow with an optional label.
- `text()` and `raw()` add free text and raw SVG.

Colour always comes from classes, never hard-coded fills:

- Boxes: `bx` plain, `bxh` blue, `bxd` rust, `bxm` dashed.
- Titles: `tt`, `tth`, `ttd`.
- Text: `ts` sub-text, `tl` italic label, `cap` rust caps heading.
- Arrows: `ln`, with `lnh` for blue and `dash` for dashed.

Keep that rule when adding figures.

| Figure | Shows |
|---|---|
| FIG1 | How it works: sources → collect → read → connect → answers |
| FIG2 | Three data layers joined (docket, decisions, authorities) |
| FIG3 | Docket outcome bar (65% leave refused / 16% granted / 19% unclear) |
| FIG4 | Life of a Federal Court file |
| FIG5 | How one citation becomes intelligence |
| FIG6 | AI paragraph meaning: "AI proposes, rules verify" |
| FIG7 | Today (public AI) vs dedicated hardware (local AI on internal documents) |
| FIG8 | Three funding tiers |
| FIG9 | New-case intake loop |

## Content notes

The text is a status overview written for the CBSA Hearings and Litigation Division, in the author's first person. It includes an unofficial funding section. Figures were checked against the repository on 28 Sept 2026. The site walkthrough of 29 Sept found issues that some claims depend on, such as the Vavilov outcome coding and the Baker citation mislink. Recheck those before relying on the related sentences.
