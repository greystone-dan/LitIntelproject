def prototype_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<title>Prototype Explorer</title>
	<style>
		:root {
			--bg: #f4efe6;
			--panel: #fffaf0;
			--ink: #1e1b16;
			--muted: #5d5547;
			--accent: #0d6a5f;
			--accent-2: #b65d2e;
			--line: #d8cebf;
		}
		* { box-sizing: border-box; }
		body {
			margin: 0;
			font-family: "Segoe UI", "Source Sans 3", sans-serif;
			color: var(--ink);
			background:
				radial-gradient(circle at 10% 8%, #f0e5d4 0, transparent 34%),
				radial-gradient(circle at 90% 88%, #d9ece8 0, transparent 35%),
				var(--bg);
		}
		.wrap { max-width: 1150px; margin: 0 auto; padding: 22px; }
		h1 { margin: 0 0 6px; font-size: clamp(1.55rem, 2.4vw, 2.2rem); }
		.lead { margin: 0 0 14px; color: var(--muted); }
		.grid { display: grid; gap: 14px; grid-template-columns: 1fr 1fr 1fr; }
		.card {
			background: var(--panel);
			border: 1px solid var(--line);
			border-radius: 12px;
			padding: 14px;
		}
		.card h2 { margin: 0 0 8px; font-size: 1rem; }
		.stat { font-size: 1.8rem; font-weight: 700; line-height: 1.1; }
		.stat-note { color: var(--muted); font-size: 0.86rem; }
		.controls { display: grid; gap: 10px; grid-template-columns: 1.2fr 0.8fr 0.6fr; margin-top: 12px; }
		label { display: block; font-size: 0.82rem; color: var(--muted); margin-bottom: 4px; }
		input, select, button {
			width: 100%; border: 1px solid var(--line); border-radius: 8px;
			padding: 9px 10px; font-size: 0.92rem; background: #fff;
		}
		button {
			background: linear-gradient(135deg, var(--accent), #14867a);
			color: #fff; font-weight: 600; border: none; cursor: pointer;
		}
		button.secondary { background: linear-gradient(135deg, var(--accent-2), #cf7d49); }
		.pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
		.pill {
			border: 1px solid var(--line); border-radius: 999px;
			padding: 3px 9px; font-size: 0.78rem; color: var(--muted);
		}
		.graph-canvas {
			width: 100%;
			height: 620px;
			border: 1px solid var(--line);
			border-radius: 10px;
			background:
				radial-gradient(circle at 20% 20%, #fffdf8 0, #f4ecdf 100%);
		}
		.graph-meta {
			display: flex;
			justify-content: space-between;
			gap: 10px;
			flex-wrap: wrap;
			margin-top: 8px;
		}
		table {
			width: 100%; border-collapse: collapse; margin-top: 12px; background: var(--panel);
			border: 1px solid var(--line); border-radius: 10px; overflow: hidden;
		}
		th, td { text-align: left; padding: 8px 9px; border-bottom: 1px solid #eee3d3; vertical-align: top; }
		th { background: #f9f0e2; font-size: 0.81rem; text-transform: uppercase; letter-spacing: 0.03em; color: #6d614f; }
		tr:last-child td { border-bottom: none; }
		.small { color: var(--muted); font-size: 0.82rem; }
		@media (max-width: 960px) {
			.grid { grid-template-columns: 1fr 1fr; }
			.controls { grid-template-columns: 1fr; }
		}
		@media (max-width: 620px) {
			.grid { grid-template-columns: 1fr; }
		}
	</style>
</head>
<body>
	<div class="wrap">
		<nav style="display:flex;gap:14px;margin-bottom:16px;font-size:0.88rem;">
			<a href="/research" style="color:#0d6a5f;text-decoration:none;">Research</a>
			<a href="/testing" style="color:#0d6a5f;text-decoration:none;">API Tester</a>
		</nav>
		<h1>Prototype Explorer</h1>
		<p class="lead">Inspect the immigration prototype cohort, topic tags, and citation-map readiness.</p>
		<div class="pills">
			<div class="pill">Prototype set: immigration_334_v1</div>
			<div class="pill">Scope: embedded + chunked cohort only</div>
		</div>

		<div class="grid" id="statsGrid">
			<div class="card"><h2>Total Cases</h2><div class="stat" id="statTotal">-</div><div class="stat-note">Cases in cohort</div></div>
			<div class="card"><h2>Embedded</h2><div class="stat" id="statEmbedded">-</div><div class="stat-note">Cases with vector</div></div>
			<div class="card"><h2>Chunked</h2><div class="stat" id="statChunked">-</div><div class="stat-note">Cases with chunks</div></div>
			<div class="card"><h2>Citation Nodes</h2><div class="stat" id="statNodes">-</div><div class="stat-note">Internal graph nodes</div></div>
			<div class="card"><h2>Citation Edges</h2><div class="stat" id="statEdges">-</div><div class="stat-note">Internal graph edges</div></div>
			<div class="card"><h2>Unique Topics</h2><div class="stat" id="statTopics">-</div><div class="stat-note">Keyword topic taxonomy</div></div>
		</div>

		<div class="card" style="margin-top:14px;">
			<h2>Citation Map</h2>
			<div class="controls" style="grid-template-columns: 1fr 0.8fr 0.6fr; margin-top: 0;">
				<div>
					<label for="graphTopic">Focus topic</label>
					<select id="graphTopic"><option value="">All topics</option></select>
				</div>
				<div>
					<label for="graphNodes">Max nodes</label>
					<input id="graphNodes" type="number" min="30" max="280" value="160" />
				</div>
				<div>
					<label>&nbsp;</label>
					<button onclick="loadGraph()">Render map</button>
				</div>
			</div>
			<svg id="graphSvg" class="graph-canvas" viewBox="0 0 980 620" preserveAspectRatio="xMidYMid meet"></svg>
			<div class="graph-meta">
				<div class="small" id="graphInfo">Graph not loaded.</div>
				<div class="small" id="graphHover">Hover a node for details.</div>
			</div>
		</div>

		<div class="card" style="margin-top:14px;">
			<h2>Browse Cases</h2>
			<div class="controls">
				<div>
					<label for="q">Query</label>
					<input id="q" type="text" placeholder="vavilov, irpa s.34, humanitarian and compassionate" />
				</div>
				<div>
					<label for="topic">Topic</label>
					<select id="topic"><option value="">All topics</option></select>
				</div>
				<div>
					<label for="pageSize">Per page</label>
					<input id="pageSize" type="number" min="5" max="100" value="20" />
				</div>
			</div>
			<div class="controls" style="grid-template-columns: 1fr 1fr 1fr; margin-top: 8px;">
				<button onclick="runSearch(1)">Search</button>
				<button class="secondary" onclick="prevPage()">Previous</button>
				<button onclick="nextPage()">Next</button>
			</div>
			<div class="small" id="pageInfo" style="margin-top:10px;">No search yet.</div>
			<div id="tableWrap"></div>
		</div>
	</div>

	<script>
		let currentPage = 1;
		let total = 0;

		function esc(value) {
			return String(value ?? "")
				.replace(/&/g, "&amp;")
				.replace(/</g, "&lt;")
				.replace(/>/g, "&gt;")
				.replace(/\"/g, "&quot;")
				.replace(/'/g, "&#39;");
		}

		function parseList(value) {
			if (!Array.isArray(value)) return "";
			return value.join(", ");
		}

		function topicColor(topic) {
			const palette = {
				refugee_protection: '#176f67',
				removal_detention: '#b65d2e',
				inadmissibility_security: '#8b3f62',
				family_hc: '#3f6db0',
				citizenship_status: '#8b6c10',
				judicial_review_procedure: '#4f4a9c',
			};
			return palette[topic] || '#6f6456';
		}

		async function loadSummary() {
			const res = await fetch('/prototype/summary');
			const body = await res.json();
			document.getElementById('statTotal').textContent = body.total_cases ?? 0;
			document.getElementById('statEmbedded').textContent = body.embedded_cases ?? 0;
			document.getElementById('statChunked').textContent = body.chunked_cases ?? 0;
			document.getElementById('statNodes').textContent = body.citation_nodes ?? 0;
			document.getElementById('statEdges').textContent = body.citation_edges ?? 0;
			document.getElementById('statTopics').textContent = Object.keys(body.topic_distribution || {}).length;

			const topicSelect = document.getElementById('topic');
			const graphTopicSelect = document.getElementById('graphTopic');
			for (const key of Object.keys(body.topic_distribution || {})) {
				const opt = document.createElement('option');
				opt.value = key;
				opt.textContent = `${key} (${body.topic_distribution[key]})`;
				topicSelect.appendChild(opt);
				graphTopicSelect.appendChild(opt.cloneNode(true));
			}
		}

		function createInitialLayout(nodes, width, height) {
			const centerX = width / 2;
			const centerY = height / 2;
			const radius = Math.min(width, height) * 0.36;
			return nodes.map((node, index) => {
				const angle = (Math.PI * 2 * index) / Math.max(nodes.length, 1);
				return {
					...node,
					x: centerX + (Math.cos(angle) * radius),
					y: centerY + (Math.sin(angle) * radius),
					vx: 0,
					vy: 0,
				};
			});
		}

		function forceLayout(nodes, edges, width, height) {
			const byId = new Map(nodes.map((n) => [n.id, n]));
			const edgePairs = edges
				.map((e) => [byId.get(e.source), byId.get(e.target)])
				.filter((pair) => pair[0] && pair[1]);
			const repulsion = 14000;
			const springLength = 85;
			const springStrength = 0.015;
			const damping = 0.86;
			const pad = 20;

			for (let step = 0; step < 170; step += 1) {
				for (let i = 0; i < nodes.length; i += 1) {
					for (let j = i + 1; j < nodes.length; j += 1) {
						const a = nodes[i];
						const b = nodes[j];
						let dx = a.x - b.x;
						let dy = a.y - b.y;
						const distSq = Math.max(20, (dx * dx) + (dy * dy));
						const force = repulsion / distSq;
						const dist = Math.sqrt(distSq);
						dx /= dist;
						dy /= dist;
						a.vx += dx * force;
						a.vy += dy * force;
						b.vx -= dx * force;
						b.vy -= dy * force;
					}
				}

				for (const [a, b] of edgePairs) {
					let dx = b.x - a.x;
					let dy = b.y - a.y;
					const dist = Math.max(1, Math.sqrt((dx * dx) + (dy * dy)));
					const stretch = dist - springLength;
					dx /= dist;
					dy /= dist;
					const fx = dx * stretch * springStrength;
					const fy = dy * stretch * springStrength;
					a.vx += fx;
					a.vy += fy;
					b.vx -= fx;
					b.vy -= fy;
				}

				for (const node of nodes) {
					node.vx *= damping;
					node.vy *= damping;
					node.x = Math.min(width - pad, Math.max(pad, node.x + node.vx));
					node.y = Math.min(height - pad, Math.max(pad, node.y + node.vy));
				}
			}
			return nodes;
		}

		function renderGraph(payload) {
			const svg = document.getElementById('graphSvg');
			svg.innerHTML = '';
			const width = 980;
			const height = 620;
			const nodes = forceLayout(createInitialLayout(payload.nodes || [], width, height), payload.edges || [], width, height);
			const byId = new Map(nodes.map((n) => [n.id, n]));

			const selectNode = (node) => {
				const citation = (node.citation || '').trim();
				if (!citation) {
					document.getElementById('graphHover').textContent = 'Selected node has no citation to filter.';
					return;
				}
				document.getElementById('q').value = citation;
				document.getElementById('graphHover').textContent = `Selected ${citation}; table filtered by citation.`;
				runSearch(1);
			};

			for (const edge of payload.edges || []) {
				const source = byId.get(edge.source);
				const target = byId.get(edge.target);
				if (!source || !target) continue;
				const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
				line.setAttribute('x1', String(source.x));
				line.setAttribute('y1', String(source.y));
				line.setAttribute('x2', String(target.x));
				line.setAttribute('y2', String(target.y));
				line.setAttribute('stroke', '#ccbca4');
				line.setAttribute('stroke-width', '1');
				line.setAttribute('stroke-opacity', '0.65');
				svg.appendChild(line);
			}

			for (const node of nodes) {
				const topic = Array.isArray(node.topics) && node.topics.length ? node.topics[0] : '';
				const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
				circle.setAttribute('cx', String(node.x));
				circle.setAttribute('cy', String(node.y));
				circle.setAttribute('r', String(Math.min(11, 3 + Math.sqrt(Math.max(1, Number(node.degree || 1))))));
				circle.setAttribute('fill', topicColor(topic));
				circle.setAttribute('fill-opacity', '0.88');
				circle.setAttribute('stroke', '#ffffff');
				circle.setAttribute('stroke-width', '1.3');
				circle.setAttribute('data-case-id', String(node.id || ''));
				circle.setAttribute('data-citation', String(node.citation || ''));
				circle.setAttribute('data-title', String(node.title || ''));
				circle.style.cursor = 'pointer';
				circle.addEventListener('mouseenter', () => {
					document.getElementById('graphHover').textContent = `${node.citation || 'No citation'} | ${node.title || 'Untitled'} | degree=${node.degree || 0}`;
				});
				circle.addEventListener('click', () => {
					selectNode(node);
				});
				svg.appendChild(circle);

				if ((node.degree || 0) >= 10) {
					const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
					text.setAttribute('x', String(node.x + 6));
					text.setAttribute('y', String(node.y - 6));
					text.setAttribute('font-size', '10');
					text.setAttribute('fill', '#3f362a');
					text.style.cursor = 'pointer';
					text.textContent = (node.citation || '').slice(0, 20);
					text.addEventListener('click', () => selectNode(node));
					svg.appendChild(text);
				}
			}

			const meta = payload.meta || {};
			document.getElementById('graphInfo').textContent = `Showing ${meta.returned_nodes || 0} of ${meta.total_nodes || 0} nodes and ${meta.returned_edges || 0} of ${meta.total_edges || 0} edges.`;
		}

		async function loadGraph() {
			const topic = document.getElementById('graphTopic').value.trim();
			const maxNodes = Math.max(30, Math.min(280, Number(document.getElementById('graphNodes').value || 160)));
			const params = new URLSearchParams({ max_nodes: String(maxNodes) });
			if (topic) params.set('topic', topic);
			document.getElementById('graphInfo').textContent = 'Rendering graph...';
			try {
				const response = await fetch(`/prototype/graph?${params.toString()}`);
				const payload = await response.json();
				renderGraph(payload);
			} catch (error) {
				document.getElementById('graphInfo').textContent = `Unable to load graph: ${error.message}`;
			}
		}

		function renderRows(items) {
			if (!Array.isArray(items) || items.length === 0) {
				document.getElementById('tableWrap').innerHTML = '<div class="small" style="margin-top:12px;">No cases matched.</div>';
				return;
			}
			const rows = items.map((item) => `
				<tr>
					<td>${esc(item.case_id)}</td>
					<td>${esc(item.citation || '')}</td>
					<td>${esc(item.title || '')}</td>
					<td>${esc(item.court || '')}</td>
					<td>${esc(item.date || '')}</td>
					<td>${esc(parseList(item.topic_keywords))}</td>
					<td>${esc(item.chunk_count)}</td>
				</tr>
			`).join('');
			document.getElementById('tableWrap').innerHTML = `
				<table>
					<thead>
						<tr>
							<th>ID</th><th>Citation</th><th>Title</th><th>Court</th><th>Date</th><th>Topics</th><th>Chunks</th>
						</tr>
					</thead>
					<tbody>${rows}</tbody>
				</table>
			`;
		}

		async function runSearch(page) {
			currentPage = page;
			const q = document.getElementById('q').value.trim();
			const topic = document.getElementById('topic').value.trim();
			const pageSize = Math.max(5, Math.min(100, Number(document.getElementById('pageSize').value || 20)));
			const params = new URLSearchParams({ page: String(currentPage), page_size: String(pageSize) });
			if (q) params.set('q', q);
			if (topic) params.set('topic', topic);
			const res = await fetch(`/prototype/cases?${params.toString()}`);
			const body = await res.json();
			total = Number(body.total || 0);
			renderRows(body.items || []);
			const shownFrom = total === 0 ? 0 : ((currentPage - 1) * pageSize) + 1;
			const shownTo = total === 0 ? 0 : Math.min(total, (currentPage - 1) * pageSize + (body.items || []).length);
			document.getElementById('pageInfo').textContent = `Showing ${shownFrom}-${shownTo} of ${total} (page ${currentPage})`;
		}

		function prevPage() { if (currentPage > 1) runSearch(currentPage - 1); }
		function nextPage() {
			const pageSize = Math.max(5, Math.min(100, Number(document.getElementById('pageSize').value || 20)));
			if (currentPage * pageSize < total) runSearch(currentPage + 1);
		}

		loadSummary().then(() => {
			runSearch(1);
			loadGraph();
		});
	</script>
</body>
</html>
"""
