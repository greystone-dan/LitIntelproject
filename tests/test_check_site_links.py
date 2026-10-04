from scripts.check_site_links import Route, audit_html_pages


def test_route_aware_links_accept_parameter_routes_and_intentional_urls():
    pages = {
        "/start": """
            <a href="/cases/42">case</a>
            <a href="https://example.test/path">external</a>
            <a href="#section">fragment</a>
            <link href="/assets/site.css">
            <form action="/api/cases/42"></form>
            <script>
              fetch('/api/cases/42');
              const xhr = new XMLHttpRequest();
              xhr.open('GET', '/cases/42');
              fetch(`/cases/${caseId}`);
              fetch('/cases/' + caseId);
            </script>
        """
    }
    routes = [
        Route("/cases/{case_id}", frozenset({"GET"})),
        Route("/api/cases/{case_id}", frozenset({"GET"})),
    ]

    assert audit_html_pages(pages, routes) == []


def test_reports_actionable_findings_for_broken_links_forms_and_api_calls():
    pages = {
        "/search": """
            <a href="/missing">broken link</a>
            <form action="/submit-misspelled"></form>
            <script>fetch('/api/missing');</script>
        """
    }
    routes = [Route("/submit", frozenset({"POST"}))]

    findings = audit_html_pages(pages, routes)

    assert [finding.source for finding in findings] == ["href", "action", "fetch"]
    assert all("does not match a registered route" in finding.reason for finding in findings)
    assert all("Correct the URL" in finding.suggestion for finding in findings)


def test_resolves_relative_urls_from_page_and_query_strings_do_not_affect_match():
    pages = {
        "/nested/page": '<a href="../cases/5?tab=summary">case</a>'
    }

    assert audit_html_pages(pages, [Route("/cases/{case_id}")]) == []


def test_checks_http_methods_for_forms_fetch_and_xhr_calls():
    pages = {
        "/start": """
            <form action="/submit" method="post"></form>
            <form action="/read" method="post"></form>
            <script>
              fetch('/read');
              fetch('/submit', {method: 'POST'});
              const xhr = new XMLHttpRequest();
              xhr.open('POST', '/submit');
            </script>
        """
    }
    routes = [
        Route("/submit", frozenset({"POST"})),
        Route("/read", frozenset({"GET"})),
    ]

    findings = audit_html_pages(pages, routes)

    assert [(finding.source, finding.url, finding.reason) for finding in findings] == [
        ("action", "/read", "local path '/read' has no registered POST route"),
    ]


def test_empty_form_action_targets_current_page_and_slash_redirect_is_valid():
    pages = {
        "/start": """
            <form method="post"></form>
            <a href="/reader/">reader</a>
        """
    }
    routes = [
        Route("/start", frozenset({"GET"})),
        Route("/reader", frozenset({"GET"})),
    ]

    findings = audit_html_pages(pages, routes)

    assert len(findings) == 1
    assert findings[0].source == "action"
    assert findings[0].url == ""
    assert "no registered POST route" in findings[0].reason
