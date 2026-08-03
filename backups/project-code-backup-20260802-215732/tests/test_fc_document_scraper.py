from fc_ingest.document_scraper import parse_document_page


def test_parse_document_page_extracts_pdf_url_and_table_metadata():
    document_url = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/350109/index.do?iframe=true"
    html = """
    <html><body>
      <h1>Federal Court Decisions</h1>
      <table>
        <tr><td>Date:</td><td>2018-11-07</td></tr>
        <tr><td>Neutral citation:</td><td>2018 FC 1123</td></tr>
        <tr><td>File numbers:</td><td>IMM-664-18</td></tr>
      </table>
      <a href="/fc-cf/decisions/en/350109/1/document.do">Download PDF</a>
      <div id="decision"><p>Reasons text</p></div>
    </body></html>
    """

    parsed = parse_document_page(document_url, html)

    assert parsed.metadata["date"] == "2018-11-07"
    assert parsed.metadata["neutral citation"] == "2018 FC 1123"
    assert parsed.metadata["file numbers"] == "IMM-664-18"
    assert parsed.metadata["pdf_url"] == "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/350109/1/document.do"
    assert "Reasons text" in parsed.full_text
