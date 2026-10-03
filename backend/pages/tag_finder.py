"""Tag-based case similarity finder page."""


def tag_finder_page_html() -> str:
	return r"""<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<title>Tag-Based Case Finder</title>
	<style>
		:root {
			--bg: #f2f5f7;
			--card: #ffffff;
			--ink: #1e2a33;
			--muted: #5f6f7a;
			--accent: #0a7a73;
			--accent-2: #0c5eaf;
			--border: #d6e0e6;
		}
		* { box-sizing: border-box; }
		body {
			margin: 0;
			font-family: "Segoe UI", "Source Sans 3", sans-serif;
			color: var(--ink);
			background:
				radial-gradient(circle at 12% 10%, #e6f4f2 0, transparent 30%),
				radial-gradient(circle at 82% 88%, #e7eef8 0, transparent 34%),
				var(--bg);
			min-height: 100vh;
		}
		.wrap {
			max-width: 1200px;
			margin: 0 auto;
			padding: 22px;
		}
		h1 {
			margin: 0 0 8px;
			font-size: clamp(1.5rem, 2.4vw, 2.2rem);
		}
		.sub {
			margin: 0 0 18px;
			color: var(--muted);
		}
		.card {
			background: var(--card);
			border: 1px solid var(--border);
			border-radius: 14px;
			padding: 16px;
			box-shadow: 0 8px 24px rgba(13, 33, 48, 0.08);
			margin-bottom: 16px;
		}
		.input-row {
			display: grid;
			grid-template-columns: 1fr 140px;
			gap: 12px;
			margin-bottom: 12px;
		}
		label {
			display: block;
			margin: 0 0 6px;
			font-size: 0.85rem;
			color: var(--muted);
			font-weight: 600;
		}
		input, select, button {
			border: 1px solid var(--border);
			border-radius: 10px;
			padding: 10px;
			font: inherit;
		}
		button {
			cursor: pointer;
			border: none;
			color: #fff;
			font-weight: 700;
			background: linear-gradient(135deg, var(--accent), var(--accent-2));
		}
		button:hover {
			opacity: 0.9;
		}
		.status {
			margin-top: 12px;
			font-size: 0.88rem;
			color: var(--muted);
		}
		.source-case {
			background: #fcfeff;
			border: 1px solid var(--border);
			border-radius: 10px;
			padding: 14px;
			margin-bottom: 16px;
		}
		.source-case h3 {
			margin: 0 0 8px;
			font-size: 1rem;
		}
		.meta {
			font-size: 0.82rem;
			color: var(--muted);
			margin-bottom: 8px;
		}
		.tag-list {
			display: flex;
			flex-wrap: wrap;
			gap: 8px;
			margin-top: 10px;
		}
		.tag {
			background: #e8f4f1;
			border: 1px solid #a8d4cc;
			border-radius: 6px;
			padding: 4px 10px;
			font-size: 0.78rem;
			color: #0a5947;
		}
		.similar-case {
			background: #fcfeff;
			border: 1px solid var(--border);
			border-radius: 10px;
			padding: 14px;
			margin-bottom: 12px;
		}
		.similar-case h4 {
			margin: 0 0 6px;
			font-size: 0.95rem;
		}
		.similarity-score {
			display: inline-block;
			background: #e0f2f1;
			color: #00695c;
			padding: 2px 8px;
			border-radius: 4px;
			font-size: 0.78rem;
			font-weight: 600;
			margin-right: 8px;
		}
		.no-results {
			padding: 20px;
			text-align: center;
			color: var(--muted);
		}
		@media (max-width: 860px) {
			.input-row {
				grid-template-columns: 1fr;
			}
		}
	</style>
</head>
<body>
	<div class="wrap">
		<h1>Tag-Based Case Finder</h1>
		<p class="sub">Find cases with overlapping legal tags. Ranked by Jaccard similarity of tag profiles.</p>

		<section class="card">
			<div class="input-row">
				<div>
					<label for="caseId">Case ID</label>
					<input id="caseId" type="number" min="1" placeholder="e.g., 12345" />
				</div>
				<div>
					<label for="limit">Results</label>
					<input id="limit" type="number" min="1" max="50" value="10" />
				</div>
			</div>
			<button id="findBtn">Find Similar Cases</button>
			<div id="status" class="status">Enter a case ID and click Find.</div>
		</section>

		<section id="results"></section>
	</div>

	<script>
		function renderSource(data) {
			if (!data.source_case) return;
			const sc = data.source_case;
			const html = `
				<div class="source-case">
					<h3>${sc.title}</h3>
					<div class="meta">
						ID: ${sc.id}
						${sc.citation ? ` | ${sc.citation}` : ''}
						${sc.date ? ` | ${sc.date}` : ''}
						| ${sc.tag_count} tags
					</div>
					<div class="tag-list">
						${sc.tags ? sc.tags.slice(0, 15).map(t => `<span class="tag">${t.join(':')}</span>`).join('') : ''}
						${sc.tags && sc.tags.length > 15 ? `<span class="tag">+${sc.tags.length - 15} more</span>` : ''}
					</div>
				</div>
			`;
			document.getElementById("results").insertAdjacentHTML("afterbegin", html);
		}

		function renderResults(payload) {
			const container = document.getElementById("results");
			const cases = payload.similar_cases || [];

			if (!cases.length) {
				container.innerHTML = '<section class="card"><div class="no-results">No similar cases found (maybe all tags are unique to this case).</div></section>';
				return;
			}

			let resultsHtml = `<section class="card"><h2>Similar Cases (${cases.length} of ${payload.total_similar} found)</h2>`;
			for (const item of cases) {
				resultsHtml += `
					<div class="similar-case">
						<h4>${item.title}</h4>
						<div class="meta">
							<span class="similarity-score">Similarity: ${(item.jaccard_similarity * 100).toFixed(1)}%</span>
							${item.citation ? ` | ${item.citation}` : ''}
							${item.court ? ` | ${item.court}` : ''}
							${item.date ? ` | ${item.date}` : ''}
						</div>
						<div class="meta">Shared: ${item.shared_tag_count}/${item.total_tags} tags</div>
						<div class="tag-list">
							${item.shared_tags.slice(0, 10).map(t => `<span class="tag">${t.join(':')}</span>`).join('')}
							${item.shared_tags.length > 10 ? `<span class="tag">+${item.shared_tags.length - 10} more</span>` : ''}
						</div>
					</div>
				`;
			}
			resultsHtml += '</section>';
			container.innerHTML = resultsHtml;
		}

		async function findSimilar() {
			const statusEl = document.getElementById("status");
			const caseId = Number(document.getElementById("caseId").value || 0);
			const limit = Number(document.getElementById("limit").value || 10);

			if (!caseId) {
				statusEl.textContent = "Enter a case ID first.";
				return;
			}

			statusEl.textContent = "Searching...";
			document.getElementById("results").innerHTML = '';

			try {
				const response = await fetch(`/search/tags/similar?case_id=${caseId}&limit=${limit}`);
				if (!response.ok) {
					const body = await response.text();
					throw new Error(`Search failed (${response.status}): ${body}`);
				}
				const data = await response.json();
				renderSource(data);
				renderResults(data);
				statusEl.textContent = `Found ${data.similar_cases.length} similar cases out of ${data.total_similar} total.`;
			} catch (error) {
				statusEl.textContent = String(error);
				document.getElementById("results").innerHTML = '';
			}
		}

		document.getElementById("findBtn").addEventListener("click", findSimilar);
		document.getElementById("caseId").addEventListener("keydown", (event) => {
			if (event.key === "Enter") {
				event.preventDefault();
				findSimilar();
			}
		});
	</script>
</body>
</html>
"""
