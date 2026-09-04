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


def test_parse_document_page_extracts_intro_outro_metadata_blocks():
    document_url = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/350109/document.do"
    html = """
    <html>
      <body>
        <h1>Federal Court Decisions</h1>
        <div id="decision">
Date: 20250117
Docket: IMM-1234-24
Citation: 2025 FC 123
BETWEEN:
Jane Doe v. Canada (Citizenship and Immigration)
Applicant
and
The Minister of Citizenship and Immigration
Respondent
REASONS FOR JUDGMENT AND JUDGMENT BY: ROY J.
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: January 15, 2025
DATED: January 17, 2025
APPEARANCES:
John Lawyer
For the Applicant
SOLICITORS OF RECORD:
Law LLP
For the Applicant
        </div>
        <a href="/fc-cf/decisions/en/item/350109/decision.pdf">Download PDF</a>
      </body>
    </html>
    """

    parsed = parse_document_page(document_url, html)
    metadata = parsed.metadata

    assert metadata["date"] == "2025-01-17"
    assert metadata["docket"] == "IMM-1234-24"
    assert metadata["neutral citation"] == "2025 FC 123"
    assert metadata["judge"] == "ROY J."
    assert metadata["place of hearing"] == "Toronto, Ontario"
    assert metadata["place_of_hearing"] == "Toronto, Ontario"
    assert metadata["date of hearing"] == "January 15, 2025"
    assert metadata["date_of_hearing"] == "January 15, 2025"
    assert metadata["style of cause"] == "Jane Doe v. Canada (Citizenship and Immigration)"
    assert "John Lawyer" in metadata["counsel"]
    assert "Law LLP" in metadata["counsel"]


def test_parse_document_page_supports_french_labels_and_title_fallback():
    document_url = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/444/document.do"
    html = """
    <html>
      <body>
        <h1>Tayarah c. Canada (Citoyenneté et Immigration)</h1>
        <div id="decision">
Base de données – Cour (s)
Décisions de la Cour fédérale
Date
2026-02-02
Référence neutre
2026 CF 148
Numéro de dossier
T-1012-24
Contenu de la décision
Date : 20260202
Dossier : T-1012-24
Référence : 2026 CF 148
Ottawa (Ontario), le 2 février 2026
En présence de monsieur le juge McHaffie
ENTRE :
HASSAN TAYARAH
demandeur
et
MINISTRE DE LA CITOYENNETÉ ET DE L’IMMIGRATION
défenderesse
JUGEMENT ET MOTIFS
        </div>
      </body>
    </html>
    """

    parsed = parse_document_page(document_url, html)
    metadata = parsed.metadata

    assert metadata["neutral citation"] == "2026 CF 148"
    assert metadata["docket"] == "T-1012-24"
    assert metadata["judge"] == "McHaffie"
    assert metadata["style of cause"] == "Tayarah v. Canada (Citoyenneté et Immigration)"
    assert metadata["place of hearing"] == "Ottawa (Ontario)"


def test_parse_document_page_uses_reference_as_neutral_citation_fallback():
    document_url = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/999/document.do"
    html = """
    <html>
      <body>
        <div id="decision">
Reference: 2024 FC 987
Court file no: IMM-999-24
Before: SMITH J.
        </div>
      </body>
    </html>
    """

    parsed = parse_document_page(document_url, html)
    metadata = parsed.metadata

    assert metadata["neutral citation"] == "2024 FC 987"
    assert metadata["docket"] == "IMM-999-24"
    assert metadata["judge"] == "SMITH J."


def test_parse_document_page_preserves_multiline_decision_text():
    document_url = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/123/document.do"
    html = """
    <html>
      <body>
        <div class="decision">
BETWEEN:
A v. B

REASONS:
This is paragraph one.
This is paragraph two.
        </div>
      </body>
    </html>
    """

    parsed = parse_document_page(document_url, html)

    assert "\n" in parsed.full_text
    assert "This is paragraph one." in parsed.full_text
    assert "This is paragraph two." in parsed.full_text


def test_parse_document_page_derives_style_from_between_party_blocks():
    document_url = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/222/document.do"
    html = """
    <html>
      <body>
        <div id="decision">
BETWEEN:
MOHAMED HARKAT
Appellant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT BY: ROY J.
        </div>
      </body>
    </html>
    """

    parsed = parse_document_page(document_url, html)
    metadata = parsed.metadata

    assert metadata["style of cause"] == "MOHAMED HARKAT v. THE MINISTER OF CITIZENSHIP AND IMMIGRATION"
    assert metadata["judge"] == "ROY J."
