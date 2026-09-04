"""Quick search HTML page builder."""


def quick_search_page_html() -> str:
	return r"""<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<title>Quick Semantic Search</title>
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
			max-width: 1080px;
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
		.grid {
			display: grid;
			grid-template-columns: minmax(0, 1fr);
			gap: 14px;
		}
		.card {
			background: var(--card);
			border: 1px solid var(--border);
			border-radius: 14px;
			padding: 14px;
			box-shadow: 0 8px 24px rgba(13, 33, 48, 0.08);
		}
		.row {
			display: grid;
			grid-template-columns: 1fr 180px 170px;
			gap: 10px;
		}
		.filters {
			display: grid;
			grid-template-columns: 1fr 1fr 1fr;
			gap: 10px;
			margin-top: 10px;
		}
		label {
			display: block;
			margin: 4px 0;
			font-size: 0.85rem;
			color: var(--muted);
		}
		input, select, button {
			width: 100%;
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
		.status {
			margin-top: 10px;
			font-size: 0.88rem;
			color: var(--muted);
		}
		.result {
			border: 1px solid var(--border);
			border-radius: 12px;
			padding: 12px;
			margin-top: 12px;
			background: #fcfeff;
		}
		.result h3 {
			margin: 0;
			font-size: 1rem;
		}
		.meta {
			margin-top: 3px;
			font-size: 0.82rem;
			color: var(--muted);
		}
		.chunks {
			margin-top: 8px;
			display: grid;
			gap: 8px;
		}
		.chunk {
			padding: 10px;
			border: 1px solid var(--border);
			border-radius: 10px;
			background: #fff;
			font-size: 0.88rem;
			line-height: 1.45;
		}
		.chunk-head {
			font-size: 0.78rem;
			font-weight: 700;
			color: #2f4b5f;
			margin-bottom: 4px;
		}
		@media (max-width: 860px) {
			.row,
			.filters {
				grid-template-columns: 1fr;
			}
		}
	</style>
</head>
<body>
	<div class="wrap">
		<h1>Quick Semantic Search</h1>
		<p class="sub">Chunk-level semantic and hybrid retrieval over the current case library.</p>

		<section class="card">
			<div class="row">
				<div>
					<label for="query">Query</label>
					<input id="query" type="text" value="non-refoulement risk on return" />
				</div>
				<div>
					<label for="mode">Mode</label>
					<select id="mode">
						<option value="semantic" selected>semantic</option>
						<option value="hybrid">hybrid</option>
						<option value="lexical">lexical</option>
						<option value="metadata">metadata</option>
					</select>
				</div>
				<div>
					<label for="pageSize">Cases</label>
					<input id="pageSize" type="number" min="1" max="20" value="8" />
				</div>
			</div>

			<div class="filters">
				<div>
					<label for="court">Court contains</label>
					<input id="court" type="text" placeholder="Federal Court" />
				</div>
				<div>
					<label for="sourceType">Source type</label>
					<input id="sourceType" type="text" placeholder="a2aj_curated" />
				</div>
				<div>
					<label for="citationContains">Citation contains</label>
					<input id="citationContains" type="text" placeholder="FC" />
				</div>
			</div>

			<button id="searchBtn">Search</button>
			<div id="status" class="status">Ready.</div>
		</section>

		<section id="results"></section>
	</div>

	<script>
		function clip(text, maxLen) {
			const compact = (text || "").replace(/\s+/g, " ").trim();
			if (compact.length <= maxLen) return compact;
			return compact.slice(0, maxLen - 1) + "...";
		}

		function renderResults(payload) {
			const results = document.getElementById("results");
			results.innerHTML = "";
			const cases = payload.cases || [];
			if (!cases.length) {
				results.innerHTML = '<section class="card"><div class="status">No results found.</div></section>';
				return;
			}

			for (const item of cases) {
				const card = document.createElement("section");
				card.className = "card result";
				const citation = item.citation ? ` | ${item.citation}` : "";
				card.innerHTML = `
					<h3>${item.title}</h3>
					<div class="meta">score=${item.best_similarity.toFixed(4)} | ${item.court}${citation}</div>
					<div class="chunks"></div>
				`;
				const chunksEl = card.querySelector(".chunks");
				for (const chunk of item.chunks || []) {
					const node = document.createElement("div");
					node.className = "chunk";
					node.innerHTML = `
						<div class="chunk-head">chunk ${chunk.chunk_index} | score=${chunk.similarity.toFixed(4)}</div>
						<div>${clip(chunk.chunk_text, 420)}</div>
					`;
					chunksEl.appendChild(node);
				}
				results.appendChild(card);
			}
		}

		async function runSearch() {
			const statusEl = document.getElementById("status");
			const query = document.getElementById("query").value.trim();
			if (!query) {
				statusEl.textContent = "Enter a query first.";
				return;
			}

			const payload = {
				query,
				search_mode: document.getElementById("mode").value,
				page: 1,
				page_size: Number(document.getElementById("pageSize").value || 8),
				max_chunks_per_case: 2,
				candidate_pool: 150,
				court: document.getElementById("court").value || null,
				source_type: document.getElementById("sourceType").value || null,
				citation_contains: document.getElementById("citationContains").value || null,
			};

			statusEl.textContent = "Searching...";
			try {
				const response = await fetch("/search/chunks/grouped", {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(payload),
				});
				if (!response.ok) {
					const body = await response.text();
					throw new Error(`Search failed (${response.status}): ${body}`);
				}
				const result = await response.json();
				statusEl.textContent = `Found ${result.total_cases} case matches from ${result.total_chunks} candidate chunks.`;
				renderResults(result);
			} catch (error) {
				statusEl.textContent = String(error);
			}
		}

		document.getElementById("searchBtn").addEventListener("click", runSearch);
		document.getElementById("query").addEventListener("keydown", (event) => {
			if (event.key === "Enter") {
				event.preventDefault();
				runSearch();
			}
		});
	</script>
</body>
</html>
"""
