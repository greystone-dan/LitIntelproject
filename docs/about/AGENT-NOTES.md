# iLit About-page prototype: historical notes

This folder retains the standalone iLit overview and its packaged prototype. The
proposal below to wire that prototype into an empty **About** tab is superseded.
The active About panel is assembled by `backend/pages/data_explorer.py` using
`backend/pages/about_content.html`; the former About overview is now part of Site
Architecture. See the current-state description in
[`SYSTEM_REFERENCE.md`](../../SYSTEM_REFERENCE.md).

## Files

| File | What it is |
|---|---|
| `ilit-overview.html` | Standalone preview of the prototype; it is not the active Data Explorer page. |
| `ilit-web-page.zip` | Packaged prototype files, including the fragment, source text, stylesheet, and builder. |

## Current implementation

`backend/pages/data_explorer.py` assembles the active About panel from
`backend/pages/about_content.html`. It also places the moved overview content in
Site Architecture. The packaged prototype and standalone preview remain here as
design references; they are not wiring instructions for the current interface.

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
