"""Research experiment HTML page builder."""


def research_page_html() -> str:
	return r"""<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<title>Legal Research</title>
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
		.wrap { max-width: 980px; margin: 0 auto; padding: 22px; }
		nav { display: flex; gap: 14px; margin-bottom: 18px; font-size: 0.88rem; }
		nav a { color: var(--accent); text-decoration: none; }
		nav a:hover { text-decoration: underline; }
		h1 { margin: 0 0 6px; font-size: clamp(1.55rem, 2.4vw, 2.1rem); }
		.lead { margin: 0 0 18px; color: var(--muted); font-size: 0.93rem; }
		.card {
			background: var(--panel);
			border: 1px solid var(--line);
			border-radius: 12px;
			padding: 16px;
			margin-bottom: 14px;
		}
		.card h2 { margin: 0 0 10px; font-size: 1rem; }
		label { display: block; font-size: 0.82rem; color: var(--muted); margin-bottom: 4px; }
		textarea, input, select {
			width: 100%; border: 1px solid var(--line); border-radius: 8px;
			padding: 9px 10px; font-size: 0.92rem; background: #fff; font-family: inherit;
		}
		textarea { resize: vertical; min-height: 80px; }
		button {
			width: 100%; border: none; border-radius: 8px;
			padding: 10px; font-size: 0.94rem; font-weight: 600; cursor: pointer;
			background: linear-gradient(135deg, var(--accent), #14867a); color: #fff;
		}
		button:disabled { opacity: 0.55; cursor: not-allowed; }
		.grid2 { display: grid; gap: 12px; grid-template-columns: 1fr 1fr; }
		.grid3 { display: grid; gap: 12px; grid-template-columns: 1fr 1fr 1fr; }
		.answer-box {
			white-space: pre-wrap;
			background: #fff;
			border: 1px solid var(--line);
			border-radius: 8px;
			padding: 14px;
			font-size: 0.93rem;
			line-height: 1.65;
			min-height: 60px;
		}
		.source-card {
			background: #fff;
			border: 1px solid var(--line);
			border-radius: 8px;
			padding: 12px;
			margin-top: 10px;
		}
		.source-title { font-weight: 600; font-size: 0.95rem; }
		.source-meta { color: var(--muted); font-size: 0.81rem; margin: 3px 0 8px; }
		.excerpt {
			background: #f9f0e2;
			border-left: 3px solid var(--accent);
			padding: 8px 10px;
			font-size: 0.86rem;
			line-height: 1.55;
			margin-top: 6px;
			border-radius: 0 6px 6px 0;
			white-space: pre-wrap;
		}
		summary { cursor: pointer; font-size: 0.83rem; color: var(--accent); margin-top: 6px; }
		.disclaimer {
			font-size: 0.78rem;
			color: var(--muted);
			margin-top: 18px;
			padding: 10px 12px;
			border: 1px solid var(--line);
			border-radius: 8px;
			background: #f9f2e8;
		}
		.token-info { font-size: 0.78rem; color: var(--muted); margin-top: 6px; }
		@media (max-width: 640px) {
			.grid2, .grid3 { grid-template-columns: 1fr; }
		}
	</style>
</head>
<body>
	<div class="wrap">
		<nav>
			<a href="/prototype">Prototype Explorer</a>
			<a href="/testing">API Tester</a>
		</nav>
		<h1>Legal Research</h1>
		<p class="lead">Ask a research question. Answers are grounded in the prototype immigration cohort.</p>

		<div class="card">
			<h2>Research Question</h2>
			<div style="margin-bottom:10px;">
				<label for="question">Question</label>
				<textarea id="question" placeholder="e.g. What is the legal test for refugee protection under section 96 of the IRPA?"></textarea>
			</div>
			<div class="grid3" style="margin-bottom:12px;">
				<div>
					<label for="sourceType">Cohort (source_type)</label>
					<input id="sourceType" type="text" value="a2aj_immigration_core" />
				</div>
				<div>
					<label for="maxCases">Max source cases (1-10)</label>
					<input id="maxCases" type="number" min="1" max="10" value="5" />
				</div>
				<div>
					<label for="searchMode">Search mode</label>
					<select id="searchMode">
						<option value="semantic">Semantic</option>
						<option value="hybrid" selected>Hybrid</option>
						<option value="lexical">Lexical</option>
					</select>
				</div>
			</div>
			<button id="submitBtn" onclick="runResearch()">Run Research</button>
		</div>

		<div id="resultSection" style="display:none;">
			<div class="card">
				<h2>Answer</h2>
				<div id="answerBox" class="answer-box"></div>
				<div id="tokenInfo" class="token-info"></div>
			</div>
			<div class="card">
				<h2>Sources</h2>
				<div id="sourcesBox"></div>
			</div>
		</div>

		<div class="disclaimer">
			Research aid only - not legal advice. Sources are unofficial copies; verify against authoritative records.
		</div>
	</div>

	<script>
		function esc(value) {
			return String(value ?? "")
				.replace(/&/g, "&amp;")
				.replace(/</g, "&lt;")
				.replace(/>/g, "&gt;")
				.replace(/\"/g, "&quot;")
				.replace(/'/g, "&#39;");
		}

		function renderSources(sources) {
			if (!Array.isArray(sources) || sources.length === 0) {
				document.getElementById("sourcesBox").innerHTML = "<p style='color:var(--muted);'>No sources returned.</p>";
				return;
			}
			const cards = sources.map((src, i) => {
				const excerptHtml = (src.excerpts || []).map((ex, j) => `
					<div class="excerpt">${esc(ex)}</div>
				`).join("");
				const sourceLink = src.source_url
					? `<a href="${esc(src.source_url)}" target="_blank" rel="noopener noreferrer">${esc(src.source_url)}</a>`
					: "";
				return `
					<div class="source-card">
						<div class="source-title">${esc(src.title || "Untitled")}</div>
						<div class="source-meta">
							${esc(src.citation || "No citation")}
							${src.court ? ` &middot; ${esc(src.court)}` : ""}
							${src.date ? ` &middot; ${esc(src.date)}` : ""}
							${src.source_url ? ` &middot; ${sourceLink}` : ""}
							&middot; Case ID ${esc(src.case_id)}
						</div>
						<details>
							<summary>${(src.excerpts || []).length} excerpt(s) used in context</summary>
							${excerptHtml}
						</details>
					</div>
				`;
			}).join("");
			document.getElementById("sourcesBox").innerHTML = cards;
		}

		async function runResearch() {
			const question = document.getElementById("question").value.trim();
			if (!question) {
				alert("Please enter a research question.");
				return;
			}

			const btn = document.getElementById("submitBtn");
			btn.disabled = true;
			btn.textContent = "Researching...";
			document.getElementById("resultSection").style.display = "none";

			const payload = {
				query: question,
				max_cases: Math.max(1, Math.min(10, Number(document.getElementById("maxCases").value) || 5)),
				search_mode: document.getElementById("searchMode").value,
			};
			const sourceType = document.getElementById("sourceType").value.trim();
			if (sourceType) {
				payload.source_type = sourceType;
			}

			try {
				const response = await fetch("/research", {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(payload),
				});
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));

				if (!response.ok) {
					document.getElementById("answerBox").textContent =
						`Error ${response.status}: ${body.detail || response.statusText}`;
					document.getElementById("sourcesBox").innerHTML = "";
					document.getElementById("tokenInfo").textContent = "";
					document.getElementById("resultSection").style.display = "block";
					return;
				}

				document.getElementById("answerBox").textContent = body.answer || "(No answer returned)";
				document.getElementById("tokenInfo").textContent =
					`Model: ${body.model_used} - Prompt tokens: ${body.prompt_tokens} - Completion tokens: ${body.completion_tokens}`;
				renderSources(body.sources || []);
				document.getElementById("resultSection").style.display = "block";
			} catch (err) {
				document.getElementById("answerBox").textContent = `Request error: ${err.message}`;
				document.getElementById("sourcesBox").innerHTML = "";
				document.getElementById("resultSection").style.display = "block";
			} finally {
				btn.disabled = false;
				btn.textContent = "Run Research";
			}
		}

		document.addEventListener("keydown", (e) => {
			if (e.key === "Enter" && e.ctrlKey) {
				runResearch();
			}
		});
	</script>
</body>
</html>
"""
