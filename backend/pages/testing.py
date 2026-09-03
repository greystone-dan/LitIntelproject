from __future__ import annotations

def testing_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<title>AI CaseLibrary API Tester</title>
	<style>
		:root {
			--bg: #f5f3ef;
			--panel: #fffdf9;
			--ink: #1f1d1a;
			--muted: #5d5952;
			--accent: #0f6e6a;
			--accent-2: #d7682f;
			--border: #d9d2c7;
		}
		* { box-sizing: border-box; }
		body {
			margin: 0;
			font-family: "Segoe UI", "Source Sans 3", sans-serif;
			background:
				radial-gradient(circle at 15% 10%, #ece3d7 0, transparent 32%),
				radial-gradient(circle at 85% 90%, #d6ebe8 0, transparent 35%),
				var(--bg);
			color: var(--ink);
			min-height: 100vh;
		}
		.wrap {
			max-width: 1100px;
			margin: 0 auto;
			padding: 24px;
		}
		h1 {
			margin: 0 0 12px;
			font-size: clamp(1.5rem, 2.5vw, 2.2rem);
			letter-spacing: 0.01em;
		}
		p.lead {
			margin: 0 0 20px;
			color: var(--muted);
		}
		.grid {
			display: grid;
			gap: 16px;
			grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
		}
		.search-card {
			grid-column: 1 / -1;
		}
		.search-layout {
			display: grid;
			gap: 14px;
			grid-template-columns: minmax(0, 1.45fr) minmax(300px, 0.85fr);
			align-items: start;
		}
		.search-panel,
		.preview-panel {
			border: 1px solid var(--border);
			border-radius: 14px;
			background: #fffefb;
			padding: 12px;
		}
		.section-head {
			display: flex;
			justify-content: space-between;
			gap: 10px;
			align-items: center;
			margin-bottom: 10px;
		}
		.section-head h2 {
			margin: 0;
		}
		.section-subtitle {
			margin: 0;
			color: var(--muted);
			font-size: 0.84rem;
		}
		.filter-group {
			border: 1px solid var(--border);
			border-radius: 12px;
			padding: 10px 10px 2px;
			margin-top: 12px;
			background: rgba(255, 255, 255, 0.72);
		}
		.filter-group summary {
			cursor: pointer;
			font-size: 0.9rem;
			font-weight: 600;
			color: var(--ink);
			margin-bottom: 8px;
		}
		.filter-group summary::marker {
			color: var(--accent);
		}
		.filter-grid {
			display: grid;
			gap: 8px;
		}
		.filter-actions {
			display: flex;
			flex-wrap: wrap;
			gap: 8px;
			margin-top: 12px;
		}
		.filter-actions button {
			width: auto;
			margin-top: 0;
			min-width: 144px;
		}
		.preview-panel textarea {
			min-height: 540px;
		}
		.helper-text {
			margin-top: 8px;
			font-size: 0.82rem;
			color: var(--muted);
			line-height: 1.45;
		}
		@media (max-width: 900px) {
			.search-layout {
				grid-template-columns: 1fr;
			}
			.preview-panel textarea {
				min-height: 260px;
			}
		}
		.card {
			background: var(--panel);
			border: 1px solid var(--border);
			border-radius: 14px;
			padding: 14px;
			box-shadow: 0 6px 20px rgba(35, 24, 13, 0.06);
		}
		h2 {
			margin: 0 0 8px;
			font-size: 1rem;
		}
		label {
			display: block;
			margin: 8px 0 4px;
			font-size: 0.86rem;
			color: var(--muted);
		}
		.controls {
			display: grid;
			grid-template-columns: 1fr 1fr;
			gap: 8px;
			align-items: end;
			margin-top: 8px;
		}
		.toggle {
			display: flex;
			align-items: center;
			gap: 8px;
			font-size: 0.86rem;
			color: var(--muted);
		}
		.toggle input {
			width: auto;
		}
		input, textarea, button {
			width: 100%;
			border-radius: 10px;
			border: 1px solid var(--border);
			padding: 9px 10px;
			font: inherit;
		}
		textarea {
			min-height: 130px;
			resize: vertical;
			font-family: Consolas, "Courier New", monospace;
			font-size: 0.86rem;
		}
		button {
			margin-top: 10px;
			background: linear-gradient(135deg, var(--accent), #0b5753);
			color: white;
			border: none;
			font-weight: 600;
			cursor: pointer;
			transition: transform 0.12s ease;
		}
		button:hover {
			transform: translateY(-1px);
		}
		.secondary {
			background: linear-gradient(135deg, var(--accent-2), #b95626);
		}
		.result {
			margin-top: 10px;
			background: #fffdf9;
			color: var(--ink);
			border-radius: 10px;
			padding: 10px;
			min-height: 120px;
			white-space: normal;
			overflow-x: auto;
			font-family: inherit;
			font-size: 0.9rem;
			line-height: 1.45;
			border: 1px solid var(--border);
		}
		.result pre {
			margin: 0;
			white-space: pre-wrap;
			font-family: Consolas, "Courier New", monospace;
			font-size: 0.82rem;
			line-height: 1.45;
			color: var(--ink);
		}
		.result .case-card {
			border: 1px solid var(--border);
			border-radius: 12px;
			padding: 10px 12px;
			margin-bottom: 10px;
			background: #ffffff;
		}
		.result .case-card.compact {
			padding: 8px 12px;
		}
		.result .hit-title {
			display: block;
			font-weight: 700;
			color: #0b5753;
			text-decoration: none;
			margin-bottom: 2px;
		}
		.result .hit-title:hover {
			text-decoration: underline;
		}
		.result .hit-meta {
			font-size: 0.78rem;
			color: var(--muted);
			margin-bottom: 4px;
		}
		.result .case-summary {
			margin-top: 6px;
			color: var(--muted);
			font-size: 0.84rem;
			line-height: 1.4;
		}
		.result .case-detail {
			display: none;
			margin-top: 8px;
			padding-top: 8px;
			border-top: 1px solid var(--border);
		}
		.result .case-detail.open {
			display: block;
		}
		.result .case-text {
			margin-top: 10px;
			white-space: pre-wrap;
			font-family: Consolas, "Courier New", monospace;
			font-size: 0.85rem;
			line-height: 1.5;
		}
		.pill {
			display: inline-block;
			padding: 2px 8px;
			border-radius: 999px;
			border: 1px solid var(--border);
			font-size: 0.78rem;
			color: var(--muted);
			margin-right: 6px;
		}
	</style>
</head>
<body>
	<div class="wrap">
		<h1>AI CaseLibrary API Tester</h1>
		<p class="lead">Manual testing interface for ingest and retrieval endpoints. Edit payloads, send requests, and inspect live JSON responses.</p>
		<div class="pill">Base URL: current host</div>
		<div class="pill">No auth required</div>
		<div class="grid">
			<section class="card">
				<h2>POST /ingest</h2>
				<label for="ingest">JSON payload</label>
				<textarea id="ingest">{
	"title": "Example v. Jones",
	"court": "Federal Court",
	"jurisdiction": "Canada",
	"date": "2026-07-31",
	"citation": "2026 FC 100",
	"summary": "The applicant challenges a removal order based on risk evidence.",
	"source_type": "manual_test"
}</textarea>
				<button onclick="sendJson('POST', '/ingest', 'ingest', 'ingestResult')">Run ingest</button>
				<div id="ingestResult" class="result"></div>
			</section>

			<section class="card search-card">
				<div class="section-head">
					<div>
						<h2>POST /search</h2>
						<p class="section-subtitle">Search A2AJ by query, citation, court, source metadata, scrape date, and relationship filters.</p>
					</div>
					<div class="pill">Metadata-first search</div>
				</div>
				<div class="search-layout">
					<div class="search-panel">
						<div class="controls" style="grid-template-columns: 1.2fr 1fr 1fr;">
							<div>
								<label for="searchQuery">Document text query</label>
								<input id="searchQuery" type="text" placeholder="non-refoulement risk review" />
							</div>
							<div>
								<label for="metaTitle">Case name / title (identifier)</label>
								<input id="metaTitle" type="text" placeholder="Doe v. Canada" />
							</div>
							<div>
								<label for="metaCaseNumber">File number / source ID (identifier)</label>
								<input id="metaCaseNumber" type="text" placeholder="IMM-1234-24" />
							</div>
						</div>
						<div class="controls" style="grid-template-columns: 1fr 1fr 1fr; margin-top: 8px;">
							<div>
								<label for="metaCitation">Citation (identifier)</label>
								<input id="metaCitation" type="text" placeholder="2024 FC 100" />
							</div>
							<div>
								<label for="secondaryCitationFilter">Secondary citation</label>
								<input id="secondaryCitationFilter" type="text" placeholder="2024 FCA 1" />
							</div>
							<div>
								<label for="sourceNameFilter">Source name</label>
								<input id="sourceNameFilter" type="text" placeholder="A2AJ Canadian Legal Data" />
							</div>
						</div>
						<div class="controls" style="grid-template-columns: 1fr 1fr 1fr; margin-top: 8px;">
							<div>
								<label for="sourceUrlFilter">Source URL contains</label>
								<input id="sourceUrlFilter" type="text" placeholder="canlii.org" />
							</div>
							<div>
								<label for="datasetVersionFilter">Dataset version contains</label>
								<input id="datasetVersionFilter" type="text" placeholder="2024-" />
							</div>
							<div>
								<label for="upstreamLicenseFilter">Upstream license contains</label>
								<input id="upstreamLicenseFilter" type="text" placeholder="Open Government" />
							</div>
						</div>
						<div class="controls" style="grid-template-columns: 1fr 1fr 1fr 1fr; margin-top: 8px;">
							<div>
								<label for="courtType">Court type</label>
								<select id="courtType">
									<option value="">All courts</option>
									<option value="FC">FC</option>
									<option value="Federal Court">Federal Court</option>
									<option value="Federal Court of Appeal">Federal Court of Appeal</option>
									<option value="Ontario Court of Appeal">Ontario Court of Appeal</option>
								</select>
							</div>
							<div>
								<label for="jurisdictionFilter">Jurisdiction</label>
								<input id="jurisdictionFilter" type="text" placeholder="Canada" />
							</div>
							<div>
								<label for="sourceTypeFilter">Source type</label>
								<input id="sourceTypeFilter" type="text" placeholder="a2aj_curated" list="sourceTypeOptions" />
								<datalist id="sourceTypeOptions">
									<option value="a2aj_curated"></option>
									<option value="a2aj_parquet"></option>
									<option value="federal_court"></option>
									<option value="manual_test"></option>
								</datalist>
							</div>
							<div>
								<label for="languageFilter">Language</label>
								<select id="languageFilter">
									<option value="">Any</option>
									<option value="en">English</option>
									<option value="fr">French</option>
								</select>
							</div>
						</div>
						<details class="filter-group" open>
							<summary>Advanced metadata filters</summary>
							<div class="filter-grid">
								<div class="controls" style="grid-template-columns: 1fr 1fr 1fr 1fr; margin-top: 0;">
									<div>
										<label class="toggle" for="yearToggle"><input id="yearToggle" type="checkbox" /> Year filter</label>
										<input id="decisionYear" type="number" min="1900" max="2100" placeholder="2020" disabled />
									</div>
									<div>
										<label for="scrapedFrom">Scraped from</label>
										<input id="scrapedFrom" type="date" />
									</div>
									<div>
										<label for="scrapedTo">Scraped to</label>
										<input id="scrapedTo" type="date" />
									</div>
									<div>
										<label for="processingStatusFilter">Processing status</label>
										<select id="processingStatusFilter">
											<option value="">Any</option>
											<option value="raw">raw</option>
											<option value="embedded">embedded</option>
										</select>
									</div>
								</div>
								<div class="controls" style="grid-template-columns: 1fr 1fr 1fr; margin-top: 8px;">
									<div>
										<label for="citedCaseFilter">Noteup cited case</label>
										<input id="citedCaseFilter" type="text" placeholder="2007 FC 1262" />
									</div>
									<div>
										<label for="casesCitedFilter">Cases cited contains</label>
										<input id="casesCitedFilter" type="text" placeholder="2007 FC 1262" />
									</div>
									<div>
										<label for="casesCitingFilter">Cases citing contains</label>
										<input id="casesCitingFilter" type="text" placeholder="2026 FC 1" />
									</div>
								</div>
								<div class="controls" style="grid-template-columns: 1fr 1fr; margin-top: 8px;">
									<div>
										<label for="citingCasesMin">Citing cases min</label>
										<input id="citingCasesMin" type="number" min="0" placeholder="0" />
									</div>
									<div>
										<label for="citingCasesMax">Citing cases max</label>
										<input id="citingCasesMax" type="number" min="0" placeholder="100" />
									</div>
								</div>
								<div class="controls" style="grid-template-columns: repeat(3, 1fr); margin-top: 8px;">
									<label class="toggle" for="partyMinister"><input id="partyMinister" type="checkbox" checked /> Minister</label>
									<label class="toggle" for="partyIRCC"><input id="partyIRCC" type="checkbox" /> IRCC</label>
									<label class="toggle" for="partyCBSA"><input id="partyCBSA" type="checkbox" /> CBSA</label>
								</div>
							</div>
						</details>
						<div class="filter-actions">
							<button class="secondary" onclick="applyAgencyPreset('minister')">Minister preset</button>
							<button class="secondary" onclick="applyAgencyPreset('ircc')">IRCC preset</button>
							<button class="secondary" onclick="applyAgencyPreset('cbsa')">CBSA preset</button>
							<button class="secondary" onclick="applyAgencyPreset('all')">All agencies</button>
							<button class="secondary" onclick="clearSearchFilters()">Reset your search</button>
							<button onclick="runCaseSearch()">Start a search</button>
						</div>
						<div id="searchPageInfo" class="pill" style="margin-top: 12px;">No search run yet.</div>
						<div id="activeFilterSummary" class="helper-text">Active filters: Minister party preset</div>
					</div>
					<div class="preview-panel">
						<label for="search">Payload preview / advanced override</label>
						<textarea id="search">{
	"query": "non-refoulement risk review",
	"search_mode": "metadata",
	"semantic_weight": 0.7,
	"lexical_weight": 0.3,
	"source_type": "a2aj_curated",
	"party_filters": ["Minister"],
	"cited_case": "2007 FC 1262",
	"page": 1,
	"page_size": 15
}</textarea>
						<div class="helper-text">The form drives the search. The JSON preview stays in sync so you can inspect or fine-tune the payload if needed.</div>
					</div>
				</div>
				<div class="controls" style="grid-template-columns: 120px 120px 1fr; align-items:end; margin-top: 12px;">
					<div>
						<label for="searchPage">Page</label>
						<input id="searchPage" type="number" min="1" value="1" />
					</div>
					<div>
						<label for="searchPageSize">Per page</label>
						<input id="searchPageSize" type="number" min="1" max="50" value="15" />
					</div>
					<div>
						<div class="pill">Use the filters above, then search.</div>
					</div>
				</div>
				<div class="controls" style="grid-template-columns: 1fr 1fr; margin-top:10px;">
					<button class="secondary" onclick="changeSearchPage(-1)">Previous page</button>
					<button onclick="changeSearchPage(1)">Next page</button>
				</div>
				<div id="searchResult" class="result"></div>
				<div id="caseTextResult" class="result"></div>
			</section>

			<section class="card">
				<h2>POST /search/chunks</h2>
				<label for="chunks">JSON payload</label>
				<textarea id="chunks">{
	"query": "torture evidence and internal flight alternative",
	"source_type": "a2aj_curated",
	"cited_case": "2007 FC 1262",
	"page": 1,
	"page_size": 5
}</textarea>
				<div class="controls">
					<label class="toggle" for="groupChunks"><input id="groupChunks" type="checkbox" checked /> Group by case</label>
					<div>
						<label for="maxChunksPerCase">Top chunks per case</label>
						<input id="maxChunksPerCase" type="number" min="1" max="10" value="2" />
					</div>
				</div>
				<button onclick="runChunkSearch()">Run grouped chunk search</button>
				<button class="secondary" onclick="sendJson('POST', '/search/chunks', 'chunks', 'chunksResult')">Run raw chunk search</button>
				<div id="chunksResult" class="result"></div>
			</section>

			<section class="card">
				<h2>GET /cases/{id}</h2>
				<label for="caseId">Case ID</label>
				<input id="caseId" type="number" value="1" min="1" />
				<button class="secondary" onclick="getCaseById()">Fetch case</button>
				<div id="caseResult" class="result"></div>
			</section>
		</div>
	</div>

	<script>
		function pretty(data) {
			return JSON.stringify(data, null, 2);
		}

		function escapeHtml(value) {
			return String(value ?? "")
				.replace(/&/g, "&amp;")
				.replace(/</g, "&lt;")
				.replace(/>/g, "&gt;")
				.replace(/\"/g, "&quot;")
				.replace(/'/g, "&#39;");
		}

		function previewText(value, maxLength = 180) {
			const normalized = String(value ?? "").replace(/\\s+/g, " ").trim();
			if (!normalized) {
				return "Click to open full text.";
			}
			if (normalized.length <= maxLength) {
				return normalized;
			}
			return `${normalized.slice(0, maxLength).trimEnd()}...`;
		}

		function renderCaseResultPane(caseRecord) {
			const output = document.getElementById("caseTextResult");
			const text = caseRecord.full_text || caseRecord.summary || "No text available.";
			output.innerHTML = `
				<strong>${escapeHtml(caseRecord.title || "Untitled case")}</strong><br />
				<span class="pill">${escapeHtml(caseRecord.citation || "No citation")}</span>
				<span class="pill">Case ID ${escapeHtml(caseRecord.id)}</span>
				<div class="case-text">${escapeHtml(text)}</div>
			`;
		}

		function updateSearchPageInfo(text) {
			const info = document.getElementById("searchPageInfo");
			if (info) {
				info.textContent = text;
			}
		}

		function updateActiveFilterSummary(payload) {
			const summary = document.getElementById("activeFilterSummary");
			if (!summary) {
				return;
			}
			const labels = [];
			if (payload.title_contains) labels.push(`title:${payload.title_contains}`);
			if (payload.citation_contains) labels.push(`citation:${payload.citation_contains}`);
			if (payload.secondary_citation_contains) labels.push(`secondary:${payload.secondary_citation_contains}`);
			if (payload.court) labels.push(`court:${payload.court}`);
			if (payload.jurisdiction) labels.push(`jurisdiction:${payload.jurisdiction}`);
			if (payload.source_type) labels.push(`source_type:${payload.source_type}`);
			if (payload.language) labels.push(`language:${payload.language}`);
			if (Array.isArray(payload.party_filters) && payload.party_filters.length) labels.push(`party:${payload.party_filters.join(",")}`);
			if (payload.date_from || payload.date_to) labels.push(`decision_date:${payload.date_from || "?"}..${payload.date_to || "?"}`);
			if (payload.scraped_from || payload.scraped_to) labels.push(`scraped:${payload.scraped_from || "?"}..${payload.scraped_to || "?"}`);
			if (payload.processing_status) labels.push(`status:${payload.processing_status}`);
			if (payload.cited_case) labels.push(`cited_case:${payload.cited_case}`);
			if (payload.cases_cited_contains) labels.push(`cases_cited:${payload.cases_cited_contains}`);
			if (payload.cases_citing_contains) labels.push(`cases_citing:${payload.cases_citing_contains}`);
			if (payload.citing_cases_min !== undefined || payload.citing_cases_max !== undefined) {
				labels.push(`citing_count:${payload.citing_cases_min ?? "?"}..${payload.citing_cases_max ?? "?"}`);
			}
			summary.textContent = labels.length ? `Active filters: ${labels.join(" | ")}` : "Active filters: none";
		}

		function getSearchPayload() {
			return JSON.parse(document.getElementById("search").value);
		}

		function setFieldValue(id, value) {
			const field = document.getElementById(id);
			if (field) {
				field.value = value ?? "";
			}
		}

		function setFieldChecked(id, value) {
			const field = document.getElementById(id);
			if (field) {
				field.checked = Boolean(value);
			}
		}

		function setSearchPayload(payload) {
			document.getElementById("search").value = JSON.stringify(payload, null, 2);
			document.getElementById("searchPage").value = String(payload.page ?? 1);
			document.getElementById("searchPageSize").value = String(payload.page_size ?? 15);
			setFieldValue("searchQuery", payload.query);
			setFieldValue("metaTitle", payload.title_contains);
			setFieldValue("metaCaseNumber", payload.source_id_contains);
			setFieldValue("metaCitation", payload.citation_contains);
			setFieldValue("secondaryCitationFilter", payload.secondary_citation_contains);
			setFieldValue("sourceNameFilter", payload.source_name_contains);
			setFieldValue("sourceUrlFilter", payload.source_url_contains);
			setFieldValue("datasetVersionFilter", payload.dataset_version_contains);
			setFieldValue("upstreamLicenseFilter", payload.upstream_license_contains);
			document.getElementById("courtType").value = payload.court ?? "";
			setFieldValue("jurisdictionFilter", payload.jurisdiction);
			setFieldValue("sourceTypeFilter", payload.source_type);
			document.getElementById("languageFilter").value = payload.language ?? "";
			const hasYearFilter = Boolean(payload.date_from || payload.date_to);
			document.getElementById("yearToggle").checked = hasYearFilter;
			document.getElementById("decisionYear").disabled = !hasYearFilter;
			document.getElementById("decisionYear").value = hasYearFilter && payload.date_from ? String(new Date(payload.date_from).getFullYear()) : "";
			setFieldValue("scrapedFrom", payload.scraped_from);
			setFieldValue("scrapedTo", payload.scraped_to);
			document.getElementById("processingStatusFilter").value = payload.processing_status ?? "";
			setFieldValue("citedCaseFilter", payload.cited_case);
			setFieldValue("casesCitedFilter", payload.cases_cited_contains);
			setFieldValue("casesCitingFilter", payload.cases_citing_contains);
			setFieldValue("citingCasesMin", payload.citing_cases_min);
			setFieldValue("citingCasesMax", payload.citing_cases_max);
			setFieldChecked("partyMinister", Array.isArray(payload.party_filters) ? payload.party_filters.includes("Minister") : false);
			setFieldChecked("partyIRCC", Array.isArray(payload.party_filters) ? payload.party_filters.includes("IRCC") : false);
			setFieldChecked("partyCBSA", Array.isArray(payload.party_filters) ? payload.party_filters.includes("CBSA") : false);
			updateActiveFilterSummary(payload);
		}

		function syncSearchControlsToPayload(payload) {
			payload.page = Math.max(1, Number(document.getElementById("searchPage").value || payload.page || 1));
			payload.page_size = Math.max(1, Math.min(50, Number(document.getElementById("searchPageSize").value || payload.page_size || 15)));
			const queryText = document.getElementById("searchQuery").value.trim();
			if (queryText) {
				payload.query = queryText;
			}
			const titleContains = document.getElementById("metaTitle").value.trim();
			if (titleContains) {
				payload.title_contains = titleContains;
			} else {
				delete payload.title_contains;
			}
			const sourceId = document.getElementById("metaCaseNumber").value.trim();
			if (sourceId) {
				payload.source_id_contains = sourceId;
			} else {
				delete payload.source_id_contains;
			}
			const citation = document.getElementById("metaCitation").value.trim();
			if (citation) {
				payload.citation_contains = citation;
			} else {
				delete payload.citation_contains;
			}
			const secondaryCitation = document.getElementById("secondaryCitationFilter").value.trim();
			if (secondaryCitation) {
				payload.secondary_citation_contains = secondaryCitation;
			} else {
				delete payload.secondary_citation_contains;
			}
			const sourceName = document.getElementById("sourceNameFilter").value.trim();
			if (sourceName) {
				payload.source_name_contains = sourceName;
			} else {
				delete payload.source_name_contains;
			}
			const sourceUrl = document.getElementById("sourceUrlFilter").value.trim();
			if (sourceUrl) {
				payload.source_url_contains = sourceUrl;
			} else {
				delete payload.source_url_contains;
			}
			const datasetVersion = document.getElementById("datasetVersionFilter").value.trim();
			if (datasetVersion) {
				payload.dataset_version_contains = datasetVersion;
			} else {
				delete payload.dataset_version_contains;
			}
			const upstreamLicense = document.getElementById("upstreamLicenseFilter").value.trim();
			if (upstreamLicense) {
				payload.upstream_license_contains = upstreamLicense;
			} else {
				delete payload.upstream_license_contains;
			}
			const courtType = document.getElementById("courtType").value.trim();
			if (courtType) {
				payload.court = courtType;
			} else {
				delete payload.court;
			}
			const jurisdiction = document.getElementById("jurisdictionFilter").value.trim();
			if (jurisdiction) {
				payload.jurisdiction = jurisdiction;
			} else {
				delete payload.jurisdiction;
			}
			const sourceType = document.getElementById("sourceTypeFilter").value.trim();
			if (sourceType) {
				payload.source_type = sourceType;
			} else {
				delete payload.source_type;
			}
			const language = document.getElementById("languageFilter").value.trim();
			if (language) {
				payload.language = language;
			} else {
				delete payload.language;
			}
			const yearToggle = document.getElementById("yearToggle").checked;
			document.getElementById("decisionYear").disabled = !yearToggle;
			const yearValue = Number(document.getElementById("decisionYear").value);
			if (yearToggle && Number.isFinite(yearValue) && yearValue >= 1900) {
				payload.date_from = `${yearValue}-01-01`;
				payload.date_to = `${yearValue}-12-31`;
			} else {
				delete payload.date_from;
				delete payload.date_to;
				if (!yearToggle) {
					document.getElementById("decisionYear").value = "";
				}
			}
			const scrapedFrom = document.getElementById("scrapedFrom").value;
			if (scrapedFrom) {
				payload.scraped_from = scrapedFrom;
			} else {
				delete payload.scraped_from;
			}
			const scrapedTo = document.getElementById("scrapedTo").value;
			if (scrapedTo) {
				payload.scraped_to = scrapedTo;
			} else {
				delete payload.scraped_to;
			}
			const processingStatus = document.getElementById("processingStatusFilter").value.trim();
			if (processingStatus) {
				payload.processing_status = processingStatus;
			} else {
				delete payload.processing_status;
			}
			const citedCase = document.getElementById("citedCaseFilter").value.trim();
			if (citedCase) {
				payload.cited_case = citedCase;
			} else {
				delete payload.cited_case;
			}
			const casesCited = document.getElementById("casesCitedFilter").value.trim();
			if (casesCited) {
				payload.cases_cited_contains = casesCited;
			} else {
				delete payload.cases_cited_contains;
			}
			const casesCiting = document.getElementById("casesCitingFilter").value.trim();
			if (casesCiting) {
				payload.cases_citing_contains = casesCiting;
			} else {
				delete payload.cases_citing_contains;
			}
			const citingCasesMin = document.getElementById("citingCasesMin").value.trim();
			if (citingCasesMin !== "") {
				payload.citing_cases_min = Math.max(0, Number(citingCasesMin));
			} else {
				delete payload.citing_cases_min;
			}
			const citingCasesMax = document.getElementById("citingCasesMax").value.trim();
			if (citingCasesMax !== "") {
				payload.citing_cases_max = Math.max(0, Number(citingCasesMax));
			} else {
				delete payload.citing_cases_max;
			}
			const partyFilters = [];
			if (document.getElementById("partyMinister").checked) {
				partyFilters.push("Minister");
			}
			if (document.getElementById("partyIRCC").checked) {
				partyFilters.push("IRCC");
			}
			if (document.getElementById("partyCBSA").checked) {
				partyFilters.push("CBSA");
			}
			if (partyFilters.length > 0) {
				payload.party_filters = partyFilters;
			} else {
				delete payload.party_filters;
			}
			setSearchPayload(payload);
			return payload;
		}

		function clearSearchFilters() {
			const payload = getSearchPayload();
			setSearchPayload({
				query: payload.query || document.getElementById("searchQuery").value.trim() || "",
				search_mode: payload.search_mode || "metadata",
				semantic_weight: payload.semantic_weight ?? 0.7,
				lexical_weight: payload.lexical_weight ?? 0.3,
				page: 1,
				page_size: Number(document.getElementById("searchPageSize").value || payload.page_size || 15),
			});
		}

		function applyAgencyPreset(preset) {
			const payload = getSearchPayload();
			if (preset === "minister") {
				payload.party_filters = ["Minister"];
			} else if (preset === "ircc") {
				payload.party_filters = ["IRCC"];
			} else if (preset === "cbsa") {
				payload.party_filters = ["CBSA"];
			} else {
				payload.party_filters = ["Minister", "IRCC", "CBSA"];
			}
			setSearchPayload(payload);
		}

		document.addEventListener("keydown", (event) => {
			if (event.key !== "Enter") {
				return;
			}
			if (event.target && event.target.tagName === "TEXTAREA") {
				return;
			}
			event.preventDefault();
			runCaseSearch();
		});

		function searchPageCount(total, pageSize) {
			if (!total || !pageSize) {
				return 0;
			}
			return Math.max(1, Math.ceil(total / pageSize));
		}

		function renderSearchPageInfo(total, page, pageSize, shown) {
			const totalPages = searchPageCount(total, pageSize);
			const start = total === 0 ? 0 : ((page - 1) * pageSize) + 1;
			const end = total === 0 ? 0 : Math.min(total, (page - 1) * pageSize + shown);
			updateSearchPageInfo(`Showing ${start}-${end} of ${total} results${totalPages ? ` Â· page ${page}/${totalPages}` : ""}`);
		}

		function getSearchHeaders(response) {
			return {
				total: Number(response.headers.get("x-search-total") || 0),
				page: Number(response.headers.get("x-search-page") || 1),
				pageSize: Number(response.headers.get("x-search-page-size") || 15),
			};
		}

		function getResultMatchSource(item) {
			if (item.match_source) {
				return item.match_source;
			}
			return "Unknown";
		}

		const caseTextCache = {};

		async function toggleCaseText(caseId) {
			const detail = document.getElementById(`case-detail-${caseId}`);
			if (!detail) {
				return;
			}
			if (detail.classList.contains("open")) {
				detail.classList.remove("open");
				return;
			}
			detail.classList.add("open");
			if (caseTextCache[caseId]) {
				detail.innerHTML = caseTextCache[caseId];
				return;
			}
			detail.innerHTML = "Loading case text...";
			try {
				const response = await fetch(`/cases/${caseId}`);
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				if (!response.ok) {
					detail.innerHTML = `<span style=\"color:#8c3b2f;\">${escapeHtml(body.detail || 'Failed to load case text.')}</span>`;
					return;
				}
				const text = body.full_text || body.summary || "No text available.";
				const html = `
					<strong>${escapeHtml(body.title || "Untitled case")}</strong><br />
					<span class="pill">${escapeHtml(body.citation || "No citation")}</span>
					<span class="pill">Case ID ${escapeHtml(body.id)}</span>
					<div class="case-text">${escapeHtml(text)}</div>
				`;
				caseTextCache[caseId] = html;
				detail.innerHTML = html;
			} catch (error) {
				detail.innerHTML = `<span style=\"color:#8c3b2f;\">Request error: ${escapeHtml(error.message)}</span>`;
			}
		}

		function renderSearchResults(results) {
			const output = document.getElementById("searchResult");
			if (!Array.isArray(results) || results.length === 0) {
				output.innerHTML = "No results.";
				return;
			}

			const rows = results.map((item) => `
				<div class="case-card compact">
					<a href="#" class="hit-title" onclick="toggleCaseText(${Number(item.id)}); return false;">
						${escapeHtml(item.title || "Untitled case")}
					</a>
					<div class="hit-meta">
						${escapeHtml(item.citation || "No citation")}${item.court ? ` Â· ${escapeHtml(item.court)}` : ""} Â· score ${Number(item.similarity ?? 0).toFixed(3)} Â· ${escapeHtml(getResultMatchSource(item))}
					</div>
					<div class="case-summary">${escapeHtml(previewText(item.summary || ""))}</div>
					<div style="margin-top:6px;">
						<button class="secondary" style="width:auto; margin-top:0; padding:6px 10px; font-size:0.82rem;" onclick="toggleCaseText(${Number(item.id)}); return false;">Open text</button>
					</div>
					<div id="case-detail-${Number(item.id)}" class="case-detail"></div>
				</div>
			`).join("");

			output.innerHTML = rows;
		}

		async function changeSearchPage(delta) {
			let payload;
			try {
				payload = getSearchPayload();
			} catch (error) {
				updateSearchPageInfo(`Invalid JSON: ${error.message}`);
				return;
			}
			payload = syncSearchControlsToPayload(payload);
			payload.page = Math.max(1, (Number(payload.page) || 1) + delta);
			setSearchPayload(payload);
			await runCaseSearch();
		}

		async function runCaseSearch() {
			const output = document.getElementById("searchResult");
			let payload;
			try {
				payload = syncSearchControlsToPayload(getSearchPayload());
			} catch (error) {
				output.textContent = `Invalid JSON: ${error.message}`;
				return;
			}

			output.textContent = "Sending request...";
			document.getElementById("caseTextResult").textContent = "";
			const start = performance.now();
			try {
				const response = await fetch("/search", {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(payload),
				});
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				const elapsed = (performance.now() - start).toFixed(0);
				output.innerHTML = `<div style="margin-bottom:10px;">[${response.status}] ${escapeHtml(response.statusText)} (${elapsed} ms)</div>`;
				if (Array.isArray(body)) {
					const headers = getSearchHeaders(response);
					renderSearchPageInfo(headers.total, headers.page, headers.pageSize, body.length);
					renderSearchResults(body);
				} else {
					output.innerHTML += `<pre style="margin:0; white-space:pre-wrap;">${escapeHtml(pretty(body))}</pre>`;
				}
			} catch (error) {
				output.textContent = `Request error: ${error.message}`;
			}
		}

		async function fetchCaseText(caseId) {
			const output = document.getElementById("caseTextResult");
			if (!caseId || caseId < 1) {
				output.textContent = "Enter a valid positive case ID.";
				return;
			}
			output.textContent = "Loading case text...";
			const start = performance.now();
			try {
				const response = await fetch(`/cases/${caseId}`);
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				const elapsed = (performance.now() - start).toFixed(0);
				output.innerHTML = `<div style="margin-bottom:10px;">[${response.status}] ${escapeHtml(response.statusText)} (${elapsed} ms)</div>`;
				if (response.ok) {
					renderCaseResultPane(body);
				} else {
					output.innerHTML += `<pre style="margin:0; white-space:pre-wrap;">${escapeHtml(pretty(body))}</pre>`;
				}
			} catch (error) {
				output.textContent = `Request error: ${error.message}`;
			}
		}

		function groupChunkResults(rows, maxChunksPerCase) {
			const grouped = new Map();
			for (const row of rows) {
				if (!grouped.has(row.id)) {
					grouped.set(row.id, {
						id: row.id,
						title: row.title,
						citation: row.citation,
						court: row.court,
						jurisdiction: row.jurisdiction,
						best_similarity: row.similarity,
						chunks: [],
					});
				}
				const entry = grouped.get(row.id);
				entry.best_similarity = Math.max(entry.best_similarity, row.similarity ?? 0);
				entry.chunks.push({
					chunk_index: row.chunk_index,
					similarity: row.similarity,
					chunk_text: row.chunk_text,
				});
			}

			const cases = Array.from(grouped.values());
			for (const item of cases) {
				item.chunks.sort((a, b) => (b.similarity ?? 0) - (a.similarity ?? 0));
				item.chunks = item.chunks.slice(0, maxChunksPerCase);
			}
			cases.sort((a, b) => (b.best_similarity ?? 0) - (a.best_similarity ?? 0));
			return {
				result_type: "grouped_by_case",
				total_cases: cases.length,
				total_chunks: rows.length,
				max_chunks_per_case: maxChunksPerCase,
				cases,
			};
		}

		async function sendJson(method, url, inputId, outputId) {
			const output = document.getElementById(outputId);
			let payload;
			try {
				payload = JSON.parse(document.getElementById(inputId).value);
			} catch (error) {
				output.textContent = `Invalid JSON: ${error.message}`;
				return;
			}

			output.textContent = "Sending request...";
			const start = performance.now();
			try {
				const response = await fetch(url, {
					method,
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(payload),
				});
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				const elapsed = (performance.now() - start).toFixed(0);
				output.textContent = `[${response.status}] ${response.statusText} (${elapsed} ms)\n\n${pretty(body)}`;
			} catch (error) {
				output.textContent = `Request error: ${error.message}`;
			}
		}

		async function runChunkSearch() {
			const output = document.getElementById("chunksResult");
			const groupByCase = document.getElementById("groupChunks").checked;
			const maxChunksValue = Number(document.getElementById("maxChunksPerCase").value);
			const maxChunksPerCase = Number.isFinite(maxChunksValue) && maxChunksValue > 0 ? maxChunksValue : 2;

			let payload;
			try {
				payload = JSON.parse(document.getElementById("chunks").value);
			} catch (error) {
				output.textContent = `Invalid JSON: ${error.message}`;
				return;
			}

			output.textContent = "Sending request...";
			const start = performance.now();
			try {
				const url = groupByCase ? "/search/chunks/grouped" : "/search/chunks";
				const groupedPayload = groupByCase ? { ...payload, max_chunks_per_case: maxChunksPerCase } : payload;
				const response = await fetch(url, {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(groupedPayload),
				});
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				const elapsed = (performance.now() - start).toFixed(0);
				output.textContent = `[${response.status}] ${response.statusText} (${elapsed} ms)\n\n${pretty(body)}`;
			} catch (error) {
				output.textContent = `Request error: ${error.message}`;
			}
		}

		async function getCaseById() {
			const caseId = Number(document.getElementById("caseId").value);
			const output = document.getElementById("caseResult");
			if (!caseId || caseId < 1) {
				output.textContent = "Enter a valid positive case ID.";
				return;
			}
			output.textContent = "Sending request...";
			const start = performance.now();
			try {
				const response = await fetch(`/cases/${caseId}`);
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				const elapsed = (performance.now() - start).toFixed(0);
				output.textContent = `[${response.status}] ${response.statusText} (${elapsed} ms)\n\n${pretty(body)}`;
			} catch (error) {
				output.textContent = `Request error: ${error.message}`;
			}
		}
	</script>
</body>
</html>
"""

