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
		.saved-searches-section {
			margin-top: 20px;
		}
		.saved-searches-header {
			display: flex;
			justify-content: space-between;
			align-items: center;
			margin-bottom: 10px;
		}
		.saved-searches-list {
			display: grid;
			grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
			gap: 10px;
		}
		.saved-search-card {
			background: var(--card);
			border: 1px solid var(--border);
			border-radius: 10px;
			padding: 12px;
			cursor: pointer;
			transition: all 0.2s;
		}
		.saved-search-card:hover {
			box-shadow: 0 2px 8px rgba(0,0,0,0.1);
			border-color: var(--accent);
		}
		.saved-search-card h4 {
			margin: 0 0 4px;
			font-size: 0.9rem;
		}
		.saved-search-card p {
			margin: 0 0 8px;
			font-size: 0.78rem;
			color: var(--muted);
		}
		.saved-search-card-actions {
			display: flex;
			gap: 6px;
			font-size: 0.78rem;
		}
		.saved-search-card-actions button {
			flex: 1;
			padding: 6px 10px;
		}
		.modal {
			display: none;
			position: fixed;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			background: rgba(0,0,0,0.5);
			z-index: 1000;
			align-items: center;
			justify-content: center;
		}
		.modal.open {
			display: flex;
		}
		.modal-content {
			background: var(--card);
			border-radius: 10px;
			padding: 20px;
			max-width: 400px;
			width: 90%;
		}
		.modal-header {
			font-size: 1rem;
			font-weight: 700;
			margin-bottom: 16px;
		}
		.form-group {
			margin-bottom: 12px;
		}
		.form-group label {
			display: block;
			font-weight: 600;
			font-size: 0.82rem;
			margin-bottom: 4px;
		}
		.form-group input,
		.form-group textarea {
			width: 100%;
			padding: 8px;
			border: 1px solid var(--border);
			border-radius: 6px;
			font-family: inherit;
			font-size: 0.85rem;
		}
		.form-group textarea {
			resize: vertical;
			min-height: 60px;
		}
		.form-group label input[type="checkbox"] {
			width: auto;
			margin-right: 6px;
		}
		.modal-actions {
			display: flex;
			gap: 8px;
			justify-content: flex-end;
			margin-top: 16px;
		}
		.modal-actions button {
			padding: 8px 14px;
			font-size: 0.85rem;
		}
		.modal-actions button.secondary {
			background: var(--card);
			color: var(--ink);
			border: 1px solid var(--border);
		}
		.save-btn-group {
			display: flex;
			gap: 10px;
		}
		.save-btn-group button {
			flex: 1;
		}
		@media (max-width: 860px) {
			.row,
			.filters {
				grid-template-columns: 1fr;
			}
			.save-btn-group {
				flex-direction: column;
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

			<div class="save-btn-group">
				<button id="searchBtn">Search</button>
				<button id="saveBtn" style="background: #666;">Save Search</button>
			</div>
			<div id="status" class="status">Ready.</div>
		</section>

		<section class="saved-searches-section card">
			<div class="saved-searches-header">
				<h2 style="margin: 0; font-size: 1rem;">Saved Searches</h2>
				<span id="savedCount" style="font-size: 0.85rem; color: var(--muted);">Loading...</span>
			</div>
			<div id="savedSearchesList" class="saved-searches-list" style="min-height: 40px;">Loading saved searches...</div>
		</section>

		<section id="results"></section>
	</div>

	<div id="saveModal" class="modal">
		<div class="modal-content">
			<div class="modal-header">Save This Search</div>
			<div class="form-group">
				<label for="saveName">Name</label>
				<input id="saveName" type="text" placeholder="e.g., Recent Procedural Fairness Cases" />
			</div>
			<div class="form-group">
				<label for="saveDesc">Description</label>
				<textarea id="saveDesc" placeholder="Optional description..."></textarea>
			</div>
			<div class="form-group">
				<label>
					<input id="saveAlert" type="checkbox" />
					Set up alert (notify me of new matching cases)
				</label>
			</div>
			<div class="modal-actions">
				<button class="secondary" onclick="closeModal()">Cancel</button>
				<button onclick="submitSave()" style="background: var(--accent);">Save</button>
			</div>
		</div>
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

		function getSearchParams() {
			return {
				query: document.getElementById("query").value.trim(),
				search_mode: document.getElementById("mode").value,
				page: 1,
				page_size: Number(document.getElementById("pageSize").value || 8),
				max_chunks_per_case: 2,
				candidate_pool: 150,
				court: document.getElementById("court").value || null,
				source_type: document.getElementById("sourceType").value || null,
				citation_contains: document.getElementById("citationContains").value || null,
			};
		}

		async function runSearch() {
			const statusEl = document.getElementById("status");
			const payload = getSearchParams();
			if (!payload.query) {
				statusEl.textContent = "Enter a query first.";
				return;
			}

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

		function openModal() {
			document.getElementById("saveModal").classList.add("open");
			document.getElementById("saveName").focus();
		}

		function closeModal() {
			document.getElementById("saveModal").classList.remove("open");
		}

		async function submitSave() {
			const name = document.getElementById("saveName").value.trim();
			if (!name) {
				alert("Please enter a name for this search.");
				return;
			}

			const params = getSearchParams();
			const payload = {
				name,
				description: document.getElementById("saveDesc").value.trim() || null,
				query: params.query,
				search_mode: params.search_mode,
				filters: {
					court: params.court,
					source_type: params.source_type,
					citation_contains: params.citation_contains,
					page_size: params.page_size,
					max_chunks_per_case: params.max_chunks_per_case,
					candidate_pool: params.candidate_pool,
				},
			};

			try {
				const response = await fetch("/saved-searches", {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(payload),
				});
				if (!response.ok) throw new Error("Failed to save search");
				closeModal();
				document.getElementById("saveName").value = "";
				document.getElementById("saveDesc").value = "";
				document.getElementById("saveAlert").checked = false;
				loadSavedSearches();
			} catch (error) {
				alert("Error saving search: " + error.message);
			}
		}

		async function loadSavedSearches() {
			try {
				const response = await fetch("/saved-searches");
				const searches = await response.ok ? await response.json() : [];
				const listEl = document.getElementById("savedSearchesList");
				const countEl = document.getElementById("savedCount");

				if (!searches.length) {
					listEl.innerHTML = '<p style="color: var(--muted); font-size: 0.85rem;">No saved searches yet. Create one after running a search.</p>';
					countEl.textContent = "0 saved";
					return;
				}

				countEl.textContent = `${searches.length} saved`;
				listEl.innerHTML = "";
				for (const search of searches) {
					const card = document.createElement("div");
					card.className = "saved-search-card";
					card.innerHTML = `
						<h4>${clip(search.name, 40)}</h4>
						<p>${clip(search.description || search.query, 60)}</p>
						<div class="saved-search-card-actions">
							<button onclick="loadSavedSearch(${search.id})" style="background: var(--accent); color: white; border: none;">Load</button>
							<button onclick="deleteSavedSearch(${search.id})" style="background: #c00; color: white; border: none;">Delete</button>
						</div>
					`;
					listEl.appendChild(card);
				}
			} catch (error) {
				console.error("Error loading saved searches:", error);
			}
		}

		async function loadSavedSearch(searchId) {
			try {
				const response = await fetch(`/saved-searches/${searchId}`);
				const search = await response.json();
				document.getElementById("query").value = search.query;
				document.getElementById("mode").value = search.search_mode;
				document.getElementById("court").value = search.filters.court || "";
				document.getElementById("sourceType").value = search.filters.source_type || "";
				document.getElementById("citationContains").value = search.filters.citation_contains || "";
				document.getElementById("pageSize").value = search.filters.page_size || 8;
				window.scrollTo(0, 0);
				runSearch();
			} catch (error) {
				alert("Error loading search: " + error.message);
			}
		}

		async function deleteSavedSearch(searchId) {
			if (!confirm("Delete this saved search?")) return;
			try {
				const response = await fetch(`/saved-searches/${searchId}`, { method: "DELETE" });
				if (!response.ok) throw new Error("Failed to delete");
				loadSavedSearches();
			} catch (error) {
				alert("Error deleting search: " + error.message);
			}
		}

		document.getElementById("searchBtn").addEventListener("click", runSearch);
		document.getElementById("saveBtn").addEventListener("click", openModal);
		document.getElementById("query").addEventListener("keydown", (event) => {
			if (event.key === "Enter") {
				event.preventDefault();
				runSearch();
			}
		});
		document.getElementById("saveName").addEventListener("keydown", (event) => {
			if (event.key === "Enter") {
				event.preventDefault();
				submitSave();
			}
		});

		loadSavedSearches();
	</script>
</body>
</html>
"""
