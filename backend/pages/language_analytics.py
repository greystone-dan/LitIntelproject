"""HTML page for language analytics research interface."""

from typing import Any


def language_analytics_page_html(analysis: dict[str, Any] | None = None) -> str:
	"""Generate HTML page for language analytics research tool.

	The page displays phrases that appear more frequently in allowed
	(applicant win) vs. dismissed (minister win) decisions for a given tag.

	**Important**: Prominently cautions that phrase associations describe
	wording patterns observed in decisions, not causes of outcomes.
	"""
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Language Analytics | AI CaseLibrary</title>
	<style>
		:root{--ink:#14212b;--muted:#63707a;--paper:#f6f4ee;--panel:#fffdfa;--line:#d9d5ca;--allowed:#2d5016;--dismissed:#8b3a3a;--warning:#d4a574;}
		*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,"Times New Roman",serif}.shell{max-width:1280px;margin:auto;padding:32px 24px 56px}.masthead{display:flex;justify-content:space-between;gap:24px;align-items:end;border-bottom:3px solid var(--ink);padding-bottom:20px}.eyebrow{font:700 12px/1.2 Arial,sans-serif;letter-spacing:1.4px;text-transform:uppercase;color:var(--allowed)}h1{font-size:34px;font-weight:normal;margin:7px 0 0;letter-spacing:0}.subhead{max-width:620px;margin:0;color:var(--muted);font-size:16px;line-height:1.45}.warning{background:#fef5e8;border-left:4px solid var(--warning);padding:16px;margin:24px 0;border-radius:3px}.warning h3{margin:0 0 8px;font:700 14px Arial,sans-serif;color:var(--ink)}.warning p{margin:0;font-size:14px;line-height:1.45;color:var(--muted)}.search-form{display:flex;gap:12px;align-items:flex-end;margin:24px 0}.form-group{display:flex;flex-direction:column}.form-group label{font:700 11px Arial,sans-serif;letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin-bottom:6px}.form-group input{padding:10px;border:1px solid var(--line);border-radius:3px;font-family:inherit;font-size:14px}.submit{padding:10px 20px;background:var(--ink);color:var(--paper);border:0;border-radius:3px;cursor:pointer;font:700 12px Arial,sans-serif;letter-spacing:1px;text-transform:uppercase}.submit:hover{background:var(--allowed)}.results{margin:32px 0}.result-group h2{font-size:20px;margin:24px 0 12px;font:700 16px Arial,sans-serif;text-transform:uppercase;letter-spacing:.7px}.allowed h2{color:var(--allowed)}.dismissed h2{color:var(--dismissed)}.phrase-list{background:var(--panel);border:1px solid var(--line);border-radius:3px;overflow:auto}		.phrase-item{display:grid;grid-template-columns:1fr 100px 100px 100px;border-bottom:1px solid var(--line);padding:12px;align-items:center;gap:12px}.phrase-item:last-child{border-bottom:0}.phrase-header{font:700 10px Arial,sans-serif;letter-spacing:.5px;text-transform:uppercase;color:var(--muted);background:#f3f0e8}.phrase-text{font-family:"Courier New",monospace;font-size:13px}.count{text-align:right;font:700 13px Arial,sans-serif}.score{text-align:right;font-size:13px;color:var(--muted)}.metadata{display:flex;gap:20px;margin:16px 0;font-size:13px}.metadata strong{font:700 12px Arial,sans-serif;text-transform:uppercase;letter-spacing:.5px;color:var(--muted);display:block;margin-bottom:2px}.empty{padding:24px;text-align:center;color:var(--muted)}.error{background:#fce8e8;border-left:4px solid #8b3a3a;padding:16px;border-radius:3px;color:#5c2a2a}@media(max-width:680px){.shell{padding:22px 14px}.masthead{display:block}.subhead{margin-top:15px}.search-form{flex-direction:column}.form-group{width:100%}.phrase-item{grid-template-columns:1fr;grid-template-rows:auto auto auto;gap:8px}.phrase-header{display:none}.phrase-text{grid-column:1}.count{grid-column:1;text-align:left}.score{grid-column:1;text-align:left}.metadata{flex-direction:column;gap:10px}h1{font-size:29px}}
	</style>
</head>
<body>
	<main class="shell">
		<header class="masthead">
			<div>
				<div class="eyebrow">Legal Research</div>
				<h1>Language Analytics</h1>
			</div>
			<p class="subhead">Analyze word patterns in allowed (applicant win) versus dismissed (minister win) decisions by legal tag.</p>
		</header>

		<div class="warning">
			<h3>⚠ Important Caution</h3>
			<p><strong>This analysis describes word associations observed in decisions, not causes of outcomes.</strong> Phrases that appear more frequently in allowed decisions may reflect underlying legal arguments or facts, not necessarily characteristics of the judge or decision-maker. Correlation is not causation. Use this tool to explore wording patterns, not to draw conclusions about judicial bias or decision-making factors.</p>
		</div>

		<form class="search-form" id="analysisForm">
			<div class="form-group">
				<label for="tagInput">Tag (required)</label>
				<input type="text" id="tagInput" name="tag" placeholder="e.g., procedural fairness" required>
			</div>
			<div class="form-group">
				<label for="judgeInput">Judge (optional)</label>
				<input type="text" id="judgeInput" name="judge" placeholder="e.g., judge_slug">
			</div>
			<button type="submit" class="submit">Analyze</button>
		</form>

		<div id="results"></div>
	</main>

	<script>
		const escape = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[char]));

		document.getElementById('analysisForm').addEventListener('submit', async (e) => {
			e.preventDefault();
			const tag = document.getElementById('tagInput').value.trim();
			if (!tag) return;

			const judgeSlug = document.getElementById('judgeInput').value.trim();
			const params = new URLSearchParams({ tag });
			if (judgeSlug) params.append('judge', judgeSlug);

			try {
				document.getElementById('results').innerHTML = '<div class="empty">Loading...</div>';
				const response = await fetch(`/api/language-analytics?${params}`);
				if (!response.ok) {
					if (response.status === 404) {
						document.getElementById('results').innerHTML = `<div class="error">No results found for tag "${escape(tag)}"${judgeSlug ? ` and judge "${escape(judgeSlug)}"` : ''}. Try a different tag.</div>`;
					} else {
						throw new Error(`Request failed (${response.status})`);
					}
					return;
				}
				const data = await response.json();
				renderResults(data);
			} catch (error) {
				document.getElementById('results').innerHTML = `<div class="error">Error: ${escape(error.message)}</div>`;
			}
		});

		function renderResults(data) {
			let html = `
				<div class="metadata">
					<div><strong>Tag</strong>${escape(data.tag)}</div>
					<div><strong>Decisions Scanned</strong>${escape(data.decisions_scanned)}${data.decisions_capped ? ' (capped)' : ''}</div>
					<div><strong>Applicant Wins</strong>${escape(data.allowed_denominator)}</div>
					<div><strong>Minister Wins</strong>${escape(data.dismissed_denominator)}</div>
					<div><strong>Excluded (Unclassified)</strong>${escape(data.excluded_unclassified)}</div>
				</div>
				<div class="results">
					<div class="result-group allowed">
						<h2>Phrases more frequent in allowed decisions</h2>
						${renderPhraseList(data.allowed_phrases, data.allowed_denominator, data.dismissed_denominator)}
					</div>
					<div class="result-group dismissed">
						<h2>Phrases more frequent in dismissed decisions</h2>
						${renderPhraseList(data.dismissed_phrases, data.allowed_denominator, data.dismissed_denominator)}
					</div>
				</div>
			`;
			document.getElementById('results').innerHTML = html;
		}

		function renderPhraseList(phrases, allowedDenominator, dismissedDenominator) {
			if (!phrases || phrases.length === 0) {
				return '<div class="empty">No phrases found (minimum frequency: 5 documents)</div>';
			}
			return '<div class="phrase-list"><div class="phrase-item phrase-header"><div>Phrase</div><div>Allowed</div><div>Dismissed</div><div>Log₂ rate ratio</div></div>' + phrases.map((item, idx) => `
				<div class="phrase-item">
					<div class="phrase-text">${escape(item.phrase)}</div>
					<div class="count">${escape(item.allowed_count)}/${escape(allowedDenominator)}</div>
					<div class="count">${escape(item.dismissed_count)}/${escape(dismissedDenominator)}</div>
					<div class="score">score: ${escape(item.score ? item.score.toFixed(2) : '0')}</div>
				</div>
			`).join('') + '</div>';
		}

		// Try to load from URL query params if present
		const params = new URLSearchParams(window.location.search);
		if (params.has('tag')) {
			document.getElementById('tagInput').value = params.get('tag');
			if (params.has('judge')) {
				document.getElementById('judgeInput').value = params.get('judge');
			}
			document.getElementById('analysisForm').dispatchEvent(new Event('submit'));
		}
	</script>
</body>
</html>"""
