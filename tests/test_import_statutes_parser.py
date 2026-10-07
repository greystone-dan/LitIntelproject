"""Section numbers and headings come from the Justice Laws XML, not from an ordinal counter."""

import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "import_statutes", Path(__file__).resolve().parents[1] / "scripts" / "import_statutes.py"
)
import_statutes = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(import_statutes)

XML = """<Statute xmlns:lims="http://justice.gc.ca/lims">
<Body>
<Section><MarginalNote>Obligation on entry</MarginalNote><Label>20</Label>
<Subsection><Label>(1)</Label><Text>Every foreign national must establish that they hold the required visa.</Text></Subsection></Section>
<Section><MarginalNote>Document</MarginalNote><Label>20.01</Label><Text>A document may be cancelled by an officer.</Text></Section>
</Body></Statute>"""


def test_parse_uses_real_section_labels_and_marginal_notes():
    sections = import_statutes.parse_statute_sections_from_xml(ET.fromstring(XML))
    assert [s["section_number"] for s in sections] == ["20", "20.01"]
    assert [s["heading"] for s in sections] == ["Obligation on entry", "Document"]
    assert "required visa" in sections[0]["text"]


def test_parse_keeps_every_section():
    body = "".join(
        f"<Section><MarginalNote>n{i}</MarginalNote><Label>{i}</Label><Text>text {i} long enough</Text></Section>"
        for i in range(1, 251)
    )
    sections = import_statutes.parse_statute_sections_from_xml(ET.fromstring(f"<Statute><Body>{body}</Body></Statute>"))
    assert len(sections) == 250
    assert sections[-1]["section_number"] == "250"
