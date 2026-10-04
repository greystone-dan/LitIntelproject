"""Standalone, read-only case comparison and existing-endpoint case pickers."""

from html import escape
import json


def case_compare_page_html(comparison: dict | None = None, a: str = "", b: str = "") -> str:
    def esc(value):
        return escape(str(value if value is not None else "Not recorded"), quote=True)

    if comparison:
        a, b = (str(comparison["cases"][side]["case_id"]) for side in ("a", "b"))
    pickers = "".join(
        f'<fieldset><legend>Case {side.upper()}</legend>'
        f'<label for="search-{side}">Search citation or case name</label>'
        f'<input id="search-{side}" type="search" autocomplete="off">'
        f'<div id="results-{side}" aria-live="polite"></div>'
        f'<label for="id-{side}">Selected case ID</label>'
        f'<input id="id-{side}" name="{side}" value="{esc(value)}" readonly required></fieldset>'
        for side, value in (("a", a), ("b", b))
    )
    content = '<p>Select two cases to compare stored research signals.</p>'
    if comparison:
        cards = []
        for side in ("a", "b"):
            case = comparison["cases"][side]
            outcome = case["outcome"]
            provenance = esc(json.dumps(outcome["provenance"], ensure_ascii=False, indent=2))
            cards.append(
                f'<article><h2>Case {side.upper()}: {esc(case["title"])}</h2>'
                f'<a href="{esc(case["url"])}">Open active reader</a><dl>'
                + "".join(f'<dt>{name}</dt><dd>{esc(case[key])}</dd>' for name, key in
                          (("Citation", "citation"), ("Court", "court"), ("Date", "date"), ("Judge", "judge")))
                + f'<dt>Judge source</dt><dd>{esc(case["judge_source"])}</dd>'
                f'<dt>Decision outcome</dt><dd>{esc(outcome["label"])}'
                f' (raw label: {esc(outcome["raw_label"])})</dd></dl>'
                f'<h3>Assignment provenance</h3><pre>{provenance}</pre></article>'
            )
        content = '<div class="pair">' + "".join(cards) + '</div>'
        for section, title in (("tags", "Legal tags"), ("statutes", "Statutes"), ("authorities", "Authorities")):
            data = comparison[section]
            counts = data["counts"]
            content += (
                f'<section id="signals-{section}"><h2>{title}</h2><p>Distinct counts: A {counts["a"]}; B {counts["b"]}; '
                f'shared {counts["shared"]}; unique A {counts["unique_a"]}; unique B {counts["unique_b"]}</p>'
                '<div class="pair">'
            )
            for side in ("a", "b"):
                items = [item for item in data["items"] if item[f"in_{side}"]]
                content += f'<div data-side="{side}"><h3>Case {side.upper()}</h3><ul class="signals">'
                for item in items:
                    flag = "Shared" if item["shared"] else f"Unique {side.upper()}"
                    highlight = "shared" if item["shared"] else f"unique-{side}"
                    label = esc(item["label"])
                    if item.get("url"):
                        label = f'<a href="{esc(item["url"])}">{label}</a>'
                    if section == "authorities" and not item["resolved"]:
                        label += " (unresolved)"
                    content += f'<li class="{highlight}">{label} — <span class="badge">{flag}</span></li>'
                content += '</ul>' + ('<p>No stored signals.</p>' if not items else '') + '</div>'
            content += '</div></section>'
        content += '<p>' + ' '.join(esc(value) for value in comparison["semantics"].values()) + '</p>'
    return """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Case comparison</title>
<style>
body{font:16px system-ui;max-width:1100px;margin:auto;padding:1rem;color:#202522;background:#fafaf7}
.pair,form{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem}
article,fieldset,section{border:1px solid #888;padding:1rem;min-width:0;overflow-wrap:anywhere}
label{display:block;margin-top:.5rem}input{box-sizing:border-box;width:100%;font:inherit}
button{font:inherit;margin:.3rem;padding:.4rem}form>button{grid-column:1/-1}
pre{white-space:pre-wrap;overflow-wrap:anywhere}dd{margin:0 0 .6rem}dt{font-weight:bold}
.signals{list-style:none;padding:0}.signals li{padding:.6rem;margin:.5rem 0;overflow-wrap:anywhere}
.signals .shared{background:#e5f2e8;border:2px solid #39714b}
.signals .unique-a{background:#e7effa;border:2px dashed #315d86}
.signals .unique-b{background:#fff0db;border:2px dotted #8a591b}
.badge{display:inline-block;font-weight:bold}
a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #315d86}
@media(max-width:760px){.pair,form{grid-template-columns:1fr}}@media print{form{display:none}}
</style></head><body><a href="/data-explorer">Back to case search</a><h1>Case comparison</h1>
<p>Research aid only. No records are changed.</p><form action="/case-compare" method="get">""" + pickers + """
<button type="submit">Compare cases</button></form><main>""" + content + """</main>
<script>
for (const side of ['a','b']) {
  const input = document.getElementById('search-' + side);
  const results = document.getElementById('results-' + side);
  const selected = document.getElementById('id-' + side);
  let timer, controller, sequence = 0;
  input.addEventListener('input', () => {
    clearTimeout(timer);
    if (controller) controller.abort();
    const current = ++sequence;
    results.replaceChildren();
    selected.value = '';
    const query = input.value.trim();
    if (query.length < 2) return;
    timer = setTimeout(async () => {
      controller = new AbortController();
      results.textContent = 'Searching…';
      try {
        const params = new URLSearchParams({query, limit:'8', offset:'0', search_full_text:'false'});
        const response = await fetch('/analytics/search/cases?' + params, {signal:controller.signal});
        if (!response.ok) throw new Error('Search failed');
        const data = await response.json();
        if (current !== sequence) return;
        results.replaceChildren();
        for (const row of data.results || []) {
          const button = document.createElement('button');
          button.type = 'button';
          button.textContent = [row.citation, row.title].filter(Boolean).join(' — ');
          button.addEventListener('click', () => {
            selected.value = String(row.case_id);
            input.value = button.textContent;
            results.replaceChildren();
          });
          results.append(button);
        }
        if (!results.childElementCount) results.textContent = 'No matching cases.';
      } catch (error) {
        if (current === sequence && error.name !== 'AbortError')
          results.textContent = 'Search unavailable. Please try again.';
      }
    }, 250);
  });
}
</script></body></html>"""
