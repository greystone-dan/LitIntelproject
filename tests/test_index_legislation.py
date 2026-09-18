from scripts.index_legislation import NON_XML_SOURCES, SOURCE_DEFINITIONS, index_source, parse_source_sections


def test_non_xml_source_definitions_cover_reviewed_sources():
    assert set(NON_XML_SOURCES) == {
        "canada.charter",
        "international.refugee_convention",
        "international.refugee_protocol",
    }

    assert NON_XML_SOURCES["canada.charter"].source_format == "html"
    assert NON_XML_SOURCES["canada.charter"].relative_path == "data/reference_library/non_xml_authorities/constitution_act_1982_page_12.html"
    assert NON_XML_SOURCES["international.refugee_convention"].source_format == "text"
    assert NON_XML_SOURCES["international.refugee_convention"].relative_path == "data/reference_library/non_xml_authorities/refugee_convention_1951_unts_189.txt"
    assert NON_XML_SOURCES["international.refugee_protocol"].source_format == "text"
    assert NON_XML_SOURCES["international.refugee_protocol"].relative_path == "data/reference_library/non_xml_authorities/refugee_protocol_1967_unts_606.txt"


def test_index_source_routes_by_declared_format(monkeypatch, tmp_path):
    source = tmp_path / "data" / "reference_library" / "non_xml_authorities" / "refugee_protocol_1967_unts_606.txt"
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text("Article I\nThe States Parties undertake to apply articles 2 to 34 of the Convention.\n", encoding="utf-8")

    calls = []

    def fake_parse_source_sections(path, source_format):
        calls.append((path, source_format))
        return [("I", None, "The States Parties undertake to apply articles 2 to 34 of the Convention.")]

    monkeypatch.setattr("scripts.index_legislation.PROJECT_ROOT", tmp_path)
    monkeypatch.setattr("scripts.index_legislation.parse_source_sections", fake_parse_source_sections)

    class FakeSession:
        def __init__(self):
            self.document = None
            self.deleted = None
            self.rows = None

        def scalar(self, query):
            return self.document

        def add(self, document):
            self.document = document
            self.document.id = 7

        def flush(self):
            return None

        def execute(self, statement):
            self.deleted = statement

        def add_all(self, rows):
            self.rows = rows

    session = FakeSession()
    count = index_source(
        session,
        "international.refugee_protocol",
        SOURCE_DEFINITIONS["international.refugee_protocol"],
    )

    assert count == 1
    assert calls == [(source, "text")]
    assert session.document.title == "Protocol Relating to the Status of Refugees"
    assert session.document.citation == "Protocol Relating to the Status of Refugees"
    assert session.document.source_url == "https://treaties.un.org/doc/Publication/UNTS/Volume%20606/volume-606-I-8791-English.pdf"
    assert session.document.local_path == "data/reference_library/non_xml_authorities/refugee_protocol_1967_unts_606.txt"
    assert session.rows[0].section_number == "I"


def test_parse_html_sections(tmp_path):
    source = tmp_path / "charter.html"
    source.write_text(
        """
        <html><body>
        <h1>Canadian Charter</h1>
        <h2>Section 1 - Guarantee of Rights and Freedoms</h2>
        <p>The rights and freedoms set out in it are subject only to reasonable limits.</p>
        <h2>Section 2 - Fundamental Freedoms</h2>
        <p>Everyone has the following fundamental freedoms.</p>
        </body></html>
        """,
        encoding="utf-8",
    )

    assert parse_source_sections(source, "html") == [
        ("1", "Guarantee of Rights and Freedoms", "The rights and freedoms set out in it are subject only to reasonable limits."),
        ("2", "Fundamental Freedoms", "Everyone has the following fundamental freedoms."),
    ]


def test_parse_text_articles_and_deduplicates(tmp_path):
    source = tmp_path / "convention.txt"
    source.write_text(
        """
        Article 1 - Definition of the term refugee
        For the purposes of the present Convention, the term refugee shall apply.
        Article 33 - Prohibition of expulsion or return
        No Contracting State shall expel or return a refugee.
        Article 33 - Duplicate heading
        Ignored duplicate content.
        """,
        encoding="utf-8",
    )

    assert parse_source_sections(source, "text") == [
        ("1", "Definition of the term refugee", "For the purposes of the present Convention, the term refugee shall apply."),
        ("33", "Prohibition of expulsion or return", "No Contracting State shall expel or return a refugee."),
    ]


def test_parse_text_roman_article_numbers(tmp_path):
    source = tmp_path / "protocol.txt"
    source.write_text(
        """
        Article I
        The States Parties undertake to apply articles 2 to 34 of the Convention.
        Article II
        The States Parties undertake to co-operate with the Office.
        """,
        encoding="utf-8",
    )

    assert parse_source_sections(source, "text") == [
        ("I", None, "The States Parties undertake to apply articles 2 to 34 of the Convention."),
        ("II", None, "The States Parties undertake to co-operate with the Office."),
    ]


def test_parse_justice_html_section_anchors(tmp_path):
        source = tmp_path / "constitution.html"
        source.write_text(
                """
                <section>
                    <h3 class="Subheading">Guarantee of Rights and Freedoms</h3>
                    <p class="MarginalNote">Rights and freedoms in Canada</p>
                    <p class="Section"><strong><a class="sectionLabel" id="s-1">1</a></strong>
                        The Charter guarantees the rights and freedoms set out in it.
                    </p>
                    <ul class="ProvisionList">
                        <li><p class="Paragraph"><span class="lawlabel">(a)</span> freedom of conscience.</p></li>
                    </ul>
                </section>
                """,
                encoding="utf-8",
        )

        assert parse_source_sections(source, "html") == [
                (
                        "1",
                        "Guarantee of Rights and Freedoms",
                        "The Charter guarantees the rights and freedoms set out in it. (a) freedom of conscience.",
                )
        ]


def test_parse_source_sections_rejects_unknown_format(tmp_path):
    source = tmp_path / "source.bin"
    source.write_bytes(b"source")

    try:
        parse_source_sections(source, "pdf")
    except ValueError as error:
        assert str(error) == "unsupported source format: pdf"
    else:
        raise AssertionError("unsupported source format should fail")
