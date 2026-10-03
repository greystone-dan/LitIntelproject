"""Saved Searches and Alerts UI page builder."""


def saved_searches_page_html() -> str:
	return r"""<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<title>Saved Searches & Alerts</title>
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
		.controls {
			display: flex;
			gap: 12px;
			margin-bottom: 24px;
			flex-wrap: wrap;
		}
		button {
			padding: 10px 16px;
			border: 1px solid var(--border);
			border-radius: 5px;
			background: var(--card);
			color: var(--ink);
			font-weight: 600;
			cursor: pointer;
			transition: all 0.2s;
		}
		button:hover {
			background: #f8f7f3;
		}
		button.primary {
			background: var(--accent);
			color: white;
			border-color: var(--accent);
		}
		button.primary:hover {
			background: #086664;
		}
		.grid {
			display: grid;
			grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
			gap: 14px;
			margin-bottom: 24px;
		}
		.card {
			background: var(--card);
			border: 1px solid var(--border);
			border-radius: 8px;
			padding: 16px;
			transition: all 0.2s;
		}
		.card:hover {
			box-shadow: 0 2px 8px rgba(0,0,0,0.1);
		}
		.card-title {
			font-weight: 700;
			margin: 0 0 6px;
			font-size: 15px;
		}
		.card-desc {
			font-size: 12px;
			color: var(--muted);
			margin: 0 0 12px;
			line-height: 1.4;
		}
		.card-meta {
			display: flex;
			gap: 12px;
			font-size: 11px;
			color: var(--muted);
			margin-bottom: 12px;
		}
		.badge {
			display: inline-block;
			padding: 4px 8px;
			background: #f0f0f0;
			border-radius: 3px;
			font-size: 11px;
			font-weight: 600;
		}
		.badge.alert-count {
			background: #fff3e0;
			color: #e65100;
		}
		.card-actions {
			display: flex;
			gap: 8px;
		}
		.card-actions button {
			flex: 1;
			padding: 8px 12px;
			font-size: 12px;
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
			border-radius: 8px;
			padding: 24px;
			max-width: 500px;
			width: 90%;
			max-height: 80vh;
			overflow-y: auto;
		}
		.modal-header {
			font-size: 18px;
			font-weight: 700;
			margin-bottom: 16px;
		}
		.form-group {
			margin-bottom: 16px;
		}
		.form-group label {
			display: block;
			font-weight: 600;
			font-size: 13px;
			margin-bottom: 6px;
		}
		.form-group input,
		.form-group textarea,
		.form-group select {
			width: 100%;
			padding: 10px;
			border: 1px solid var(--border);
			border-radius: 5px;
			font-family: inherit;
			font-size: 13px;
		}
		.form-group textarea {
			resize: vertical;
			min-height: 80px;
		}
		.modal-actions {
			display: flex;
			gap: 8px;
			justify-content: flex-end;
			margin-top: 20px;
		}
		.alert-list {
			background: var(--card);
			border: 1px solid var(--border);
			border-radius: 8px;
			overflow: hidden;
		}
		.alert-item {
			padding: 12px;
			border-bottom: 1px solid var(--border);
		}
		.alert-item:last-child {
			border-bottom: none;
		}
		.alert-item-title {
			font-weight: 600;
			margin: 0 0 4px;
			font-size: 13px;
		}
		.alert-item-meta {
			font-size: 11px;
			color: var(--muted);
		}
		.loading {
			text-align: center;
			color: var(--muted);
			padding: 20px;
		}
		.error {
			background: #ffebee;
			color: #c62828;
			padding: 12px;
			border-radius: 5px;
			margin-bottom: 12px;
		}
		.success {
			background: #e8f5e9;
			color: #2e7d32;
			padding: 12px;
			border-radius: 5px;
			margin-bottom: 12px;
		}
	</style>
</head>
<body>
<div class="wrap">
	<h1>Saved Searches & Alerts</h1>
	<p class="sub">Monitor case law and FC activity that matches your research interests.</p>

	<div id="message"></div>

	<div class="controls">
		<button class="primary" id="newSearchBtn">+ New Saved Search</button>
		<button id="refreshBtn">Refresh All</button>
		<button id="exportBtn">Export Digest</button>
	</div>

	<div id="searchesContainer" class="grid">
		<div class="loading">Loading saved searches...</div>
	</div>
</div>

<!-- New/Edit Search Modal -->
<div id="searchModal" class="modal">
	<div class="modal-content">
		<div class="modal-header" id="modalTitle">New Saved Search</div>
		<form id="searchForm">
			<div class="form-group">
				<label for="searchName">Search Name *</label>
				<input type="text" id="searchName" required placeholder="e.g., Immigration Appeals 2024">
			</div>
			<div class="form-group">
				<label for="searchDesc">Description</label>
				<textarea id="searchDesc" placeholder="Optional notes about this search..."></textarea>
			</div>
			<div class="form-group">
				<label for="searchQuery">Query *</label>
				<input type="text" id="searchQuery" required placeholder="e.g., procedural fairness">
			</div>
			<div class="form-group">
				<label for="searchMode">Search Mode</label>
				<select id="searchMode">
					<option value="semantic">Semantic (meaning-based)</option>
					<option value="lexical">Lexical (text-based)</option>
					<option value="hybrid">Hybrid</option>
					<option value="metadata">Metadata Only</option>
				</select>
			</div>
			<div class="form-group">
				<label for="filterCourt">Court</label>
				<input type="text" id="filterCourt" placeholder="e.g., Federal Court">
			</div>
			<div class="form-group">
				<label for="filterJudge">Judge Name</label>
				<input type="text" id="filterJudge" placeholder="Optional">
			</div>
			<div class="form-group">
				<label for="filterYearFrom">Year From</label>
				<input type="number" id="filterYearFrom" min="1900" max="2100" placeholder="e.g., 2020">
			</div>
			<div class="form-group">
				<label for="filterYearTo">Year To</label>
				<input type="number" id="filterYearTo" min="1900" max="2100" placeholder="e.g., 2024">
			</div>
			<div class="modal-actions">
				<button type="button" id="modalClose">Cancel</button>
				<button type="submit" class="primary">Save Search</button>
			</div>
		</form>
	</div>
</div>

<!-- Alert Details Modal -->
<div id="alertModal" class="modal">
	<div class="modal-content">
		<div class="modal-header" id="alertModalTitle">Recent Alerts</div>
		<div id="alertContent" class="alert-list"></div>
		<div class="modal-actions">
			<button id="alertModalClose">Close</button>
		</div>
	</div>
</div>

<script>
const API_BASE = '/';
const state = {
	searches: [],
	currentSearchId: null,
	isEditMode: false,
};

async function loadSearches() {
	try {
		const res = await fetch(API_BASE + 'saved-searches');
		if (!res.ok) throw new Error('Failed to load searches');
		state.searches = await res.json();
		renderSearches();
	} catch (err) {
		showMessage('Error loading searches: ' + err.message, 'error');
	}
}

function renderSearches() {
	const container = document.getElementById('searchesContainer');
	if (!state.searches.length) {
		container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--muted);">No saved searches yet. Create one to get started.</div>';
		return;
	}

	container.innerHTML = state.searches.map(search => `
		<div class="card">
			<div class="card-title">${escapeHtml(search.name)}</div>
			<div class="card-desc">${search.description ? escapeHtml(search.description) : '(No description)'}</div>
			<div class="card-meta">
				<span><strong>${search.alert_count}</strong> new alerts</span>
				<span class="badge">${search.search_mode}</span>
			</div>
			<div class="card-actions">
				<button onclick="viewAlerts(${search.id})">View Alerts</button>
				<button onclick="editSearch(${search.id})">Edit</button>
				<button onclick="deleteSearch(${search.id})">Delete</button>
			</div>
		</div>
	`).join('');
}

function showMessage(msg, type = 'success') {
	const el = document.getElementById('message');
	el.innerHTML = `<div class="${type}">${msg}</div>`;
	setTimeout(() => el.innerHTML = '', 4000);
}

async function viewAlerts(searchId) {
	try {
		const res = await fetch(API_BASE + 'saved-searches/' + searchId);
		if (!res.ok) throw new Error('Failed to load alerts');
		const search = await res.json();

		const content = document.getElementById('alertContent');
		if (!search.alerts.length) {
			content.innerHTML = '<div style="padding: 20px; text-align: center; color: var(--muted);">No new alerts yet.</div>';
		} else {
			content.innerHTML = search.alerts.map(alert => `
				<div class="alert-item">
					<div class="alert-item-title">${escapeHtml(alert.case_title || 'Unknown Case')}</div>
					<div class="alert-item-meta">
						<strong>${alert.case_citation || 'No citation'}</strong> · ${alert.case_date || 'Unknown date'}<br>
						Match type: ${alert.match_type} · Relevance: ${(alert.relevance_score * 100).toFixed(0)}%<br>
						Discovered: ${new Date(alert.discovered_at).toLocaleString()}
					</div>
					${alert.chunk_text ? `<div style="margin-top: 8px; font-size: 11px; color: var(--muted); line-height: 1.4;">...${escapeHtml(alert.chunk_text)}...</div>` : ''}
				</div>
			`).join('');
		}

		document.getElementById('alertModalTitle').textContent = 'Alerts for: ' + escapeHtml(search.name);
		document.getElementById('alertModal').classList.add('open');
	} catch (err) {
		showMessage('Error loading alerts: ' + err.message, 'error');
	}
}

function editSearch(searchId) {
	const search = state.searches.find(s => s.id === searchId);
	if (!search) return;

	state.currentSearchId = searchId;
	state.isEditMode = true;
	document.getElementById('modalTitle').textContent = 'Edit Saved Search';
	document.getElementById('searchName').value = search.name;
	document.getElementById('searchDesc').value = search.description || '';
	document.getElementById('searchQuery').value = search.query;
	document.getElementById('searchMode').value = search.search_mode;
	document.getElementById('filterCourt').value = search.filters.court || '';
	document.getElementById('filterJudge').value = search.filters.judge_name || '';
	document.getElementById('filterYearFrom').value = search.filters.date_from ? new Date(search.filters.date_from).getFullYear() : '';
	document.getElementById('filterYearTo').value = search.filters.date_to ? new Date(search.filters.date_to).getFullYear() : '';
	document.getElementById('searchModal').classList.add('open');
}

async function deleteSearch(searchId) {
	if (!confirm('Delete this saved search?')) return;
	try {
		const res = await fetch(API_BASE + 'saved-searches/' + searchId, { method: 'DELETE' });
		if (!res.ok) throw new Error('Failed to delete search');
		showMessage('Search deleted');
		loadSearches();
	} catch (err) {
		showMessage('Error deleting search: ' + err.message, 'error');
	}
}

async function submitSearch(e) {
	e.preventDefault();

	const filters = {};
	const court = document.getElementById('filterCourt').value.trim();
	const judge = document.getElementById('filterJudge').value.trim();
	const yearFrom = document.getElementById('filterYearFrom').value;
	const yearTo = document.getElementById('filterYearTo').value;

	if (court) filters.court = court;
	if (judge) filters.judge_name = judge;
	if (yearFrom) filters.date_from = yearFrom + '-01-01';
	if (yearTo) filters.date_to = yearTo + '-12-31';

	const payload = {
		name: document.getElementById('searchName').value,
		description: document.getElementById('searchDesc').value || null,
		query: document.getElementById('searchQuery').value,
		search_mode: document.getElementById('searchMode').value,
		filters: filters,
	};

	try {
		const url = API_BASE + 'saved-searches' + (state.isEditMode ? '/' + state.currentSearchId : '');
		const method = state.isEditMode ? 'PUT' : 'POST';
		const res = await fetch(url, {
			method: method,
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(payload),
		});

		if (!res.ok) throw new Error('Failed to save search');
		showMessage(state.isEditMode ? 'Search updated' : 'Search created');
		document.getElementById('searchModal').classList.remove('open');
		document.getElementById('searchForm').reset();
		state.currentSearchId = null;
		state.isEditMode = false;
		loadSearches();
	} catch (err) {
		showMessage('Error saving search: ' + err.message, 'error');
	}
}

function escapeHtml(text) {
	const div = document.createElement('div');
	div.textContent = text;
	return div.innerHTML;
}

// Event Listeners
document.getElementById('newSearchBtn').addEventListener('click', () => {
	state.isEditMode = false;
	state.currentSearchId = null;
	document.getElementById('modalTitle').textContent = 'New Saved Search';
	document.getElementById('searchForm').reset();
	document.getElementById('searchModal').classList.add('open');
});

document.getElementById('modalClose').addEventListener('click', () => {
	document.getElementById('searchModal').classList.remove('open');
});

document.getElementById('alertModalClose').addEventListener('click', () => {
	document.getElementById('alertModal').classList.remove('open');
});

document.getElementById('searchForm').addEventListener('submit', submitSearch);

document.getElementById('refreshBtn').addEventListener('click', loadSearches);

document.getElementById('exportBtn').addEventListener('click', () => {
	alert('Export feature coming soon - will generate CSV digest of all recent alerts');
});

// Load on startup
loadSearches();
</script>
</body>
</html>"""
