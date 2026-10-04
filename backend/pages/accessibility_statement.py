"""Plain-language accessibility statement page."""

from .skip_link import with_skip_link


@with_skip_link
def accessibility_page_html() -> str:
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Accessibility | AI CaseLibrary</title>
  <style>
    :root{color-scheme:light;--ink:#202522;--muted:#59635e;--paper:#f1efe8;--surface:#fffef9;--line:#d8d5ca;--link:#145e5a}
    *{box-sizing:border-box}
    body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI",sans-serif}
    header,main,footer{max-width:54rem;margin:0 auto;padding:1.25rem}
    header,footer{border-bottom:1px solid var(--line)}
    footer{border-top:1px solid var(--line);border-bottom:0}
    main{margin-block:1rem 2rem;background:var(--surface);border:1px solid var(--line);border-radius:.35rem}
    h1,h2{line-height:1.2}h1{font-size:clamp(1.8rem,5vw,2.5rem);margin:.25rem 0 1rem}h2{font-size:1.25rem;margin-top:1.8rem}
    a{color:var(--link);text-underline-offset:.16em}a:focus-visible{outline:3px solid #315d8d;outline-offset:3px}
    .lede{font-size:1.15rem;max-width:65ch}.notice{padding:1rem;border-left:4px solid #8a6418;background:#f8f0dc}
    .contact{padding:1rem;border:1px solid var(--line);background:#f8f6ef}
  </style>
</head>
<body>
  <header><a href="/data-explorer?tab=about">About AI CaseLibrary</a></header>
  <main id="main-content" tabindex="-1">
    <h1>Accessibility</h1>
    <p class="lede">We aim to make AI CaseLibrary usable by as many people as possible. Our target is WCAG 2.1 Level AA.</p>
    <p class="notice"><strong>This is not a conformance statement.</strong> We have not established that the site conforms to WCAG 2.1 AA or any other accessibility standard.</p>

    <h2>What has been checked</h2>
    <p>Our static checks cover the declared language, title, viewport, and exactly one top-level heading in each standalone page builder. They also check for one skip-to-content link with a focusable target and an <code>alt</code> attribute on every image. Separate checks confirm that the Citation Map SVG has a title and description and that its text listing is present. These checks cover only those markup patterns; they do not assess whether image descriptions are useful, test every WCAG requirement, or show how the site works for people.</p>

    <h2>Known gaps</h2>
    <ul>
      <li>Automated checks only confirm that an image has an <code>alt</code> attribute; they do not assess the quality or usefulness of its description.</li>
      <li>We have not tested with a screen reader.</li>
      <li>We have not tested browser zoom at 200%.</li>
      <li>The Citation Map includes a visual graph. A text description and a “View as table” alternative are provided, but the graph itself remains visual and these alternatives still need user testing.</li>
      <li>Keyboard operation, contrast in every state, reflow, and assistive-technology behavior have not been comprehensively verified.</li>
    </ul>

    <h2>Contact</h2>
    <p class="contact">Accessibility feedback contact: <strong>[PLACEHOLDER — site owner must set this contact before publication]</strong></p>
    <p><a href="/data-explorer?tab=about">Return to About</a></p>
  </main>
  <footer><a href="/accessibility" aria-current="page">Accessibility</a></footer>
</body>
</html>"""
