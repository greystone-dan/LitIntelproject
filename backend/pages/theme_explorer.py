"""Theme Discovery explorer page - browse recurring legal themes across case library."""

from .accessibility import accessible_page


@accessible_page
def theme_explorer_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width,initial-scale=1">
	<title>Legal Themes Explorer</title>
	<style>
		* { margin: 0; padding: 0; box-sizing: border-box; }
		html { font-size: 15px; }
		body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f8f9fa; color: #202529; line-height: 1.5; }
		.header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 32px 24px; margin-bottom: 0; }
		.header h1 { font-size: 28px; margin-bottom: 8px; font-weight: 700; }
		.header p { font-size: 14px; opacity: 0.95; }

		.container { max-width: 1200px; margin: 0 auto; }
		.main { display: grid; grid-template-columns: 280px 1fr; gap: 24px; padding: 24px; }

		.sidebar { background: white; border-radius: 6px; padding: 20px; height: fit-content; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
		.sidebar h2 { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #666; margin-bottom: 16px; }
		.sidebar-section { margin-bottom: 20px; }
		.sidebar-label { font-size: 12px; font-weight: 600; color: #999; display: block; margin-bottom: 8px; }
		.filter-input { width: 100%; padding: 8px 12px; border: 1px solid #ddd; border-radius: 4px; font-size: 13px; }
		.theme-list { max-height: 600px; overflow-y: auto; }
		.theme-item { padding: 10px; margin-bottom: 6px; border-left: 3px solid #ccc; background: #f9f9f9; border-radius: 2px; cursor: pointer; font-size: 13px; transition: all 0.2s; }
		.theme-item:hover { background: #f0f0f0; border-left-color: #667eea; }
		.theme-item.active { background: #e8f0fe; border-left-color: #667eea; color: #1967d2; font-weight: 600; }
		.theme-item-count { font-size: 11px; color: #999; display: block; margin-top: 2px; }

		.content { background: white; border-radius: 6px; padding: 32px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
		.content-header { margin-bottom: 24px; border-bottom: 1px solid #eee; padding-bottom: 20px; }
		.theme-title { font-size: 24px; font-weight: 700; color: #1a1a1a; margin-bottom: 8px; }
		.theme-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-top: 16px; }
		.stat { }
		.stat-value { font-size: 22px; font-weight: 700; color: #667eea; }
		.stat-label { font-size: 11px; text-transform: uppercase; color: #999; letter-spacing: 0.5px; margin-top: 4px; }

		.content-section { margin-bottom: 28px; }
		.section-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #333; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid #eee; }

		.tags { display: flex; flex-wrap: wrap; gap: 8px; }
		.tag { background: #e8f0fe; color: #1967d2; padding: 6px 12px; border-radius: 14px; font-size: 12px; font-weight: 500; }
		.tag.role { background: #f0e8fe; color: #5b3a7d; }

		.occurrence-list { display: flex; flex-direction: column; gap: 12px; }
		.occurrence { background: #fafafa; padding: 14px; border-left: 3px solid #667eea; border-radius: 3px; cursor: pointer; transition: all 0.2s; }
		.occurrence:hover { background: #f0f0f0; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
		.occ-case { font-weight: 600; color: #1a1a1a; margin-bottom: 4px; }
		.occ-unit { font-size: 12px; color: #666; }
		.occ-case-link { color: #1967d2; text-decoration: none; }
		.occ-case-link:hover { text-decoration: underline; }

		.loading { text-align: center; padding: 40px; color: #5f6f7a; }
		.loading::after { content: " …"; animation: dots 1.5s steps(3, end) infinite; }
		@keyframes dots { 0%, 20% { content: " ."; } 40% { content: " .."; } 60% { content: " ..."; } }

		.empty { text-align: center; padding: 40px; color: #5f6f7a; }
	</style>
</head>
<body>
	<div class="header">
		<h1>Legal Themes Explorer</h1>
		<p>Discover recurring doctrinal themes and legal arguments across the case library</p>
	</div>

	<div class="container">
		<div style="background: white; margin: 24px 24px 0; padding: 20px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.08);">
			<h2 style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #666; margin-bottom: 12px;">Unit-Level Search</h2>
			<div style="display: grid; grid-template-columns: 1fr auto; gap: 8px;">
				<input type="text" id="unitSearchInput" aria-label="Search discussion units" placeholder="Search for specific legal topics within discussion units (e.g., credibility assessment, procedural fairness)" style="padding: 12px; border: 1px solid #ddd; border-radius: 4px; font-size: 13px;">
				<button id="unitSearchBtn" style="padding: 12px 24px; background: #667eea; color: white; border: none; border-radius: 4px; font-weight: 600; cursor: pointer;">Search Units</button>
			</div>
			<div id="unitSearchResults" style="margin-top: 12px; display: none;">
				<!-- Unit search results will be displayed here -->
			</div>
		</div>

		<div class="main">
			<div class="sidebar">
				<h2>Themes</h2>
				<div class="sidebar-section">
					<label class="sidebar-label" for="themeFilter">Search themes</label>
					<input type="text" id="themeFilter" class="filter-input" placeholder="e.g., credibility">
				</div>
				<div class="theme-list" id="themeList">
					<div class="loading">Loading themes</div>
				</div>
			</div>

			<div class="content">
				<div id="content" style="min-height: 400px;">
					<div class="empty">Select a theme from the list to view details</div>
				</div>
			</div>
		</div>
	</div>

	<script>
		let allThemes = [];
		let currentTheme = null;
		let unitSearchResults = [];

		async function loadThemes() {
			try {
				const response = await fetch('/themes/discovery');
				const data = await response.json();
				allThemes = data.themes || [];
				renderThemeList(allThemes);
			} catch (err) {
				console.error('Failed to load themes:', err);
				document.getElementById('themeList').innerHTML = '<div class="empty">Failed to load themes</div>';
			}
		}

		async function searchUnits(query) {
			if (query.length < 2) {
				document.getElementById('unitSearchResults').style.display = 'none';
				return;
			}

			try {
				const response = await fetch(\`/units/search?q=\${encodeURIComponent(query)}&limit=15\`);
				const data = await response.json();
				unitSearchResults = data.results || [];
				renderUnitSearchResults(data);
			} catch (err) {
				console.error('Failed to search units:', err);
				document.getElementById('unitSearchResults').innerHTML = '<div class="empty">Error searching units</div>';
				document.getElementById('unitSearchResults').style.display = 'block';
			}
		}

		function renderUnitSearchResults(data) {
			const container = document.getElementById('unitSearchResults');
			if (!data.results || !data.results.length) {
				container.innerHTML = '<div class="empty">No matching units found</div>';
				container.style.display = 'block';
				return;
			}

			const html = \`
				<div style="padding: 12px 0; border-top: 1px solid #eee;">
					<p style="font-size: 12px; color: #666; margin-bottom: 12px;"><strong>\${data.total_results}</strong> matching units found (\${data.results[0].match_type === 'semantic' ? 'semantic search' : 'keyword match'})</p>
					<div style="display: flex; flex-direction: column; gap: 8px; max-height: 400px; overflow-y: auto;">
						\${data.results.slice(0, 10).map(result => \`
							<div style="background: #f8f9fa; padding: 10px; border-left: 3px solid #667eea; border-radius: 3px; font-size: 12px;">
								<div style="font-weight: 600; margin-bottom: 4px;">Case \${result.case_id} · Unit \${result.unit_index}</div>
								<div style="color: #666; margin-bottom: 4px;">
									Judges: <strong>\${result.judges.join(', ') || 'Not recorded'}</strong>
									· Outcome: <strong>\${result.disposition || 'Unknown'}</strong>
								</div>
								<div style="color: #999; font-size: 11px;">
									Key terms: \${result.key_terms.join(', ')} · Score: \${(result.score * 100).toFixed(0)}%
								</div>
							</div>
						\`).join('')}
					</div>
				</div>
			\`;

			container.innerHTML = html;
			container.style.display = 'block';
		}

		function renderThemeList(themes) {
			const container = document.getElementById('themeList');
			if (!themes.length) {
				container.innerHTML = '<div class="empty">No themes found</div>';
				return;
			}

			container.innerHTML = themes.map((theme, idx) => `
				<div class="theme-item" onclick="selectTheme(${idx})">
					${theme.theme_name}
					<span class="theme-item-count">${theme.occurrence_count} occurrences</span>
				</div>
			`).join('');
		}

		function selectTheme(idx) {
			currentTheme = allThemes[idx];

			// Update sidebar selection
			document.querySelectorAll('.theme-item').forEach((item, i) => {
				item.classList.toggle('active', i === idx);
			});

			// Render theme details
			const html = `
				<div class="content-header">
					<div class="theme-title">${escapeHtml(currentTheme.theme_name)}</div>
					<div class="theme-stats">
						<div class="stat">
							<div class="stat-value">${currentTheme.occurrence_count}</div>
							<div class="stat-label">Occurrences</div>
						</div>
						<div class="stat">
							<div class="stat-value">${currentTheme.occurrences.length}</div>
							<div class="stat-label">Cases</div>
						</div>
						<div class="stat">
							<div class="stat-value">${currentTheme.top_key_terms.length}</div>
							<div class="stat-label">Key Terms</div>
						</div>
						<div class="stat">
							<div class="stat-value">${currentTheme.top_argument_roles.length}</div>
							<div class="stat-label">Roles</div>
						</div>
					</div>
				</div>

				<div class="content-section">
					<div class="section-title">Key Terms</div>
					<div class="tags">
						${currentTheme.top_key_terms.map(term =>
							\`<span class="tag">\${escapeHtml(term)}</span>\`
						).join('')}
					</div>
				</div>

				<div class="content-section">
					<div class="section-title">Argument Roles</div>
					<div class="tags">
						${currentTheme.top_argument_roles.map(role =>
							\`<span class="tag role">\${escapeHtml(role)}</span>\`
						).join('')}
					</div>
				</div>

				<div class="content-section">
					<div class="section-title">Case Occurrences</div>
					<div class="occurrence-list">
						${currentTheme.occurrences.slice(0, 20).map(occ => \`
							<div class="occurrence" onclick="openCase(\${occ.case_id})">
								<div class="occ-case">
									<a href="/data-explorer?case=\${occ.case_id}" class="occ-case-link">Case \${occ.case_id}</a>
									· Unit \${occ.unit_index}, \${escapeHtml(occ.subtheme_id)}
								</div>
								<div class="occ-unit">Click to view in case reader</div>
							</div>
						\`).join('')}
					</div>
				</div>
			`;

			document.getElementById('content').innerHTML = html;
		}

		function openCase(caseId) {
			window.location.href = \`/data-explorer?case=\${caseId}\`;
		}

		function escapeHtml(text) {
			const div = document.createElement('div');
			div.textContent = text;
			return div.innerHTML;
		}

		// Unit search
		document.getElementById('unitSearchBtn').addEventListener('click', (e) => {
			const query = document.getElementById('unitSearchInput').value.trim();
			if (query.length >= 2) {
				searchUnits(query);
			}
		});

		// Unit search on Enter key
		document.getElementById('unitSearchInput').addEventListener('keypress', (e) => {
			if (e.key === 'Enter') {
				const query = document.getElementById('unitSearchInput').value.trim();
				if (query.length >= 2) {
					searchUnits(query);
				}
			}
		});

		// Filter themes
		document.getElementById('themeFilter').addEventListener('input', (e) => {
			const query = e.target.value.toLowerCase();
			const filtered = allThemes.filter(theme =>
				theme.theme_name.toLowerCase().includes(query) ||
				theme.top_key_terms.some(term => term.toLowerCase().includes(query))
			);
			renderThemeList(filtered);
		});

		// Load themes on page load
		loadThemes();
	</script>
</body>
</html>"""
