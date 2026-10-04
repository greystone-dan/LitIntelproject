"""HTML UI for case reader with statute reference integration."""

from .pages.skip_link import with_skip_link


@with_skip_link
def case_reader_with_statutes_html(
    case_id: int,
    case_title: str,
    case_citation: str,
    case_date: str,
    case_court: str,
    case_summary: str,
) -> str:
    """Generate HTML for case reader with statute references and decision-date matching."""

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Case Reader: {case_citation}</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                background-color: #f5f5f5;
                color: #333;
            }}

            .container {{
                max-width: 1200px;
                margin: 0 auto;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
                padding: 20px;
            }}

            .case-panel, .statute-panel {{
                background: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                overflow: hidden;
            }}

            .panel-header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 20px;
                border-bottom: 1px solid #ddd;
            }}

            .panel-header h2 {{
                font-size: 18px;
                margin-bottom: 8px;
            }}

            .panel-header .metadata {{
                font-size: 12px;
                opacity: 0.9;
            }}

            .panel-content {{
                padding: 20px;
                height: 600px;
                overflow-y: auto;
            }}

            .case-text {{
                line-height: 1.8;
                color: #444;
            }}

            .statute-ref {{
                background-color: #fff3cd;
                padding: 2px 6px;
                border-radius: 3px;
                cursor: pointer;
                font-weight: 500;
                border-bottom: 2px solid #ffc107;
                transition: all 0.2s ease;
                display: inline;
            }}

            .statute-ref:hover {{
                background-color: #ffe69c;
                transform: translateY(-1px);
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}

            .statute-content {{
                background: white;
                padding: 15px;
                border-radius: 4px;
                margin-bottom: 15px;
                border-left: 4px solid #667eea;
            }}

            .statute-title {{
                font-weight: bold;
                color: #667eea;
                margin-bottom: 8px;
                font-size: 14px;
            }}

            .statute-section {{
                margin: 12px 0;
                padding: 10px;
                background: #f8f9fa;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
                font-size: 13px;
                line-height: 1.6;
            }}

            .statute-section-num {{
                font-weight: bold;
                color: #667eea;
                margin-right: 8px;
            }}

            .statute-note {{
                background: #e8f4f8;
                padding: 8px 12px;
                border-left: 3px solid #17a2b8;
                margin-top: 10px;
                font-size: 12px;
                color: #004085;
                border-radius: 3px;
            }}

            .loading {{
                text-align: center;
                padding: 40px;
                color: #999;
            }}

            .error {{
                background: #f8d7da;
                border: 1px solid #f5c6cb;
                color: #721c24;
                padding: 12px;
                border-radius: 4px;
                margin: 10px 0;
            }}

            .empty {{
                text-align: center;
                padding: 60px 20px;
                color: #999;
            }}

            .statute-changed {{
                background: #fff3cd;
                padding: 8px 12px;
                border-left: 3px solid #ffc107;
                margin-top: 8px;
                font-size: 12px;
                color: #856404;
                border-radius: 3px;
            }}

            .statute-unchanged {{
                background: #d4edda;
                padding: 8px 12px;
                border-left: 3px solid #28a745;
                margin-top: 8px;
                font-size: 12px;
                color: #155724;
                border-radius: 3px;
            }}

            .case-summary {{
                background: #f0f4ff;
                padding: 12px;
                border-radius: 4px;
                margin: 15px 0;
                font-size: 13px;
                line-height: 1.6;
            }}

            .statute-meta {{
                font-size: 11px;
                color: #999;
                margin-top: 8px;
                padding-top: 8px;
                border-top: 1px solid #eee;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Case Panel -->
            <div class="case-panel">
                <div class="panel-header">
                    <h2>Case Information</h2>
                    <div class="metadata">
                        <div>{case_citation}</div>
                        <div>{case_court} • {case_date}</div>
                    </div>
                </div>
                <div class="panel-content">
                    <div style="margin-bottom: 20px;">
                        <h1 style="font-size: 16px; margin-top: 1em; margin-bottom: 8px;">{case_title}</h1>
                    </div>

                    <div class="case-summary">
                        <strong>Summary:</strong><br>
                        {case_summary}
                    </div>

                    <div style="margin-top: 20px;">
                        <strong style="display: block; margin-bottom: 12px;">Statute References:</strong>
                        <div id="statute-refs-list" style="font-size: 13px; line-height: 1.8;">
                            <div class="loading">Loading statute references...</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Statute Panel -->
            <div class="statute-panel">
                <div class="panel-header">
                    <h2>Statute Content</h2>
                    <div class="metadata">
                        <div id="statute-info">Select a statute reference to view</div>
                    </div>
                </div>
                <div class="panel-content">
                    <div id="statute-content" class="empty">
                        Click on a statute reference in the left panel to view its content as it was on the decision date.
                    </div>
                </div>
            </div>
        </div>

        <script>
            const CASE_ID = {case_id};
            const CASE_DATE = '{case_date}';

            // Load statute references for this case
            async function loadStatuteReferences() {{
                try {{
                    const response = await fetch(`/cases/${{CASE_ID}}/statute-references`);
                    if (!response.ok) throw new Error('Failed to load statute references');

                    const references = await response.json();
                    displayReferences(references);
                }} catch (error) {{
                    document.getElementById('statute-refs-list').innerHTML =
                        '<div class="error">Failed to load statute references: ' + error.message + '</div>';
                }}
            }}

            function displayReferences(references) {{
                const container = document.getElementById('statute-refs-list');
                if (!references || references.length === 0) {{
                    container.innerHTML = '<div class="empty">No statute references found</div>';
                    return;
                }}

                // Group by statute
                const byStatute = {{}};
                references.forEach(ref => {{
                    const key = ref.instrument_key || 'unknown';
                    if (!byStatute[key]) byStatute[key] = [];
                    byStatute[key].push(ref);
                }});

                let html = '';
                Object.entries(byStatute).forEach(([statute, refs]) => {{
                    const sections = refs
                        .filter(r => r.pinpoint)
                        .map(r => r.pinpoint)
                        .join(', ')
                        .split(',')
                        .map(s => s.trim())
                        .filter((v, i, a) => a.indexOf(v) === i)
                        .join(', ');

                    if (sections) {{
                        html += `
                            <div style="margin-bottom: 8px;">
                                <span class="statute-ref"
                                      onclick="viewStatute('${{statute}}', '${{sections}}')"
                                      title="Click to view sections: ${{sections}}">
                                    ${{statute}} s. ${{sections}}
                                </span>
                            </div>
                        `;
                    }}
                }});

                container.innerHTML = html || '<div class="empty">No statute sections found</div>';
            }}

            async function viewStatute(statuteCode, sections) {{
                const container = document.getElementById('statute-content');
                const infoDiv = document.getElementById('statute-info');

                container.innerHTML = '<div class="loading">Loading statute...</div>';
                infoDiv.textContent = `Loading ${{statuteCode}}...`;

                try {{
                    // Get statute metadata with decision-date matching
                    const metaResponse = await fetch(
                        `/api/statutes/${{statuteCode}}?as_of=${{CASE_DATE}}`
                    );
                    if (!metaResponse.ok) throw new Error('Statute not found');
                    const metadata = await metaResponse.json();

                    // Get statute sections
                    const sectionsResponse = await fetch(
                        `/api/statutes/${{statuteCode}}/versions/${{metadata.version_id}}/sections`
                    );
                    if (!sectionsResponse.ok) throw new Error('Sections not found');
                    const sectionData = await sectionsResponse.json();

                    let html = `
                        <div class="statute-content">
                            <div class="statute-title">${{metadata.title}}</div>
                            <div class="statute-meta">
                                In force: ${{metadata.in_force_date}}<br>
                                Version ID: ${{metadata.version_id}}
                            </div>
                    `;

                    // Parse requested sections
                    const requestedSections = sections
                        .split(',')
                        .map(s => s.trim())
                        .filter(s => s);

                    // Filter and display relevant sections
                    const relevantSections = sectionData.filter(section => {{
                        const secNum = section.section_number;
                        return requestedSections.some(req => {{
                            const base = req.split('.')[0].trim();
                            return secNum === req || secNum === base ||
                                   secNum.startsWith(base + '.') ||
                                   secNum.startsWith(base + '(');
                        }});
                    }});

                    if (relevantSections.length === 0) {{
                        html += '<div class="statute-section">No matching sections found</div>';
                    }} else {{
                        relevantSections.forEach(section => {{
                            const sectionText = (section.heading || '') +
                                               (section.text ? '\\n' + section.text : '');
                            html += `
                                <div class="statute-section">
                                    <span class="statute-section-num">${{section.section_number}}</span>
                                    <span>${{sectionText.substring(0, 500)}}${{sectionText.length > 500 ? '...' : ''}}</span>
                                </div>
                            `;
                        }});
                    }}

                    // Check if statute has changed since decision date
                    const currentDate = new Date().toISOString().split('T')[0];
                    if (currentDate !== metadata.in_force_date) {{
                        html += `
                            <div class="statute-changed">
                                ⚠️ This statute text is as it was in force on ${{metadata.in_force_date}}.
                                It may have been amended since then.
                            </div>
                        `;
                    }} else {{
                        html += `
                            <div class="statute-unchanged">
                                ✓ This is the current statute text.
                            </div>
                        `;
                    }}

                    html += '</div>';
                    container.innerHTML = html;
                    infoDiv.textContent = `${{metadata.title}} (as of ${{metadata.in_force_date}})`;

                }} catch (error) {{
                    container.innerHTML = '<div class="error">Error loading statute: ' + error.message + '</div>';
                    infoDiv.textContent = 'Error loading statute';
                }}
            }}

            // Load references on page load
            window.addEventListener('load', loadStatuteReferences);
        </script>
    </body>
    </html>
    """


@with_skip_link
def statute_viewer_page_html() -> str:
    """Standalone statute viewer page."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Statute Viewer</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                max-width: 900px;
                margin: 0 auto;
                padding: 20px;
                background: #f5f5f5;
            }

            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 30px;
                border-radius: 8px;
                margin-bottom: 30px;
            }

            h1 {
                margin: 0 0 10px 0;
            }

            .search-form {
                display: flex;
                gap: 10px;
                margin-top: 20px;
            }

            .search-form input {
                flex: 1;
                padding: 10px;
                border: none;
                border-radius: 4px;
            }

            .search-form button {
                padding: 10px 20px;
                background: white;
                color: #667eea;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-weight: bold;
            }

            .content {
                background: white;
                padding: 30px;
                border-radius: 8px;
                min-height: 400px;
            }

            .statute {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 4px;
                margin-bottom: 20px;
                border-left: 4px solid #667eea;
            }

            .statute-title {
                font-weight: bold;
                color: #667eea;
                margin-bottom: 10px;
            }

            .statute-section {
                margin: 15px 0;
                padding: 10px;
                background: white;
                border-radius: 3px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Canadian Statute Viewer</h1>
            <p>View federal statutes and regulations with point-in-time versioning</p>
            <div class="search-form">
                <input type="text" id="statute-code" placeholder="E.g., IRPA, IRPR, CA..." />
                <input type="date" id="statute-date" />
                <button onclick="searchStatute()">View Statute</button>
            </div>
        </div>

        <div class="content" id="content">
            <p>Enter a statute code and optional date to view the statute text.</p>
        </div>

        <script>
            const contentDiv = document.getElementById('content');

            function searchStatute() {
                const code = document.getElementById('statute-code').value.toUpperCase();
                const date = document.getElementById('statute-date').value;

                if (!code) {
                    contentDiv.innerHTML = '<p style="color: red;">Please enter a statute code</p>';
                    return;
                }

                fetchStatute(code, date);
            }

            async function fetchStatute(code, date) {
                contentDiv.innerHTML = '<p>Loading...</p>';

                try {
                    const url = date
                        ? `/api/statutes/${code}?as_of=${date}`
                        : `/api/statutes/${code}`;

                    const metaResp = await fetch(url);
                    if (!metaResp.ok) throw new Error('Statute not found');
                    const metadata = await metaResp.json();

                    const sectionsResp = await fetch(
                        `/api/statutes/${code}/versions/${metadata.version_id}/sections`
                    );
                    if (!sectionsResp.ok) throw new Error('Sections not found');
                    const sections = await sectionsResp.json();

                    let html = `
                        <div class="statute">
                            <div class="statute-title">${metadata.title}</div>
                            <p><strong>In force:</strong> ${metadata.in_force_date}</p>
                    `;

                    sections.slice(0, 20).forEach(sec => {
                        html += `
                            <div class="statute-section">
                                <strong>${sec.section_number}</strong>
                                <p>${(sec.text || '').substring(0, 200)}...</p>
                            </div>
                        `;
                    });

                    if (sections.length > 20) {
                        html += `<p><em>Showing 20 of ${sections.length} sections</em></p>`;
                    }

                    html += '</div>';
                    contentDiv.innerHTML = html;

                } catch (error) {
                    contentDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
                }
            }

            // Allow Enter key to search
            document.getElementById('statute-code').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') searchStatute();
            });
        </script>
    </body>
    </html>
    """
