"""Offline reader measurements; every invocation uses a cold Session.

The reader-data route delegates directly to build_case_reader_data. Statutes
are a separate /statute-references request, not part of reader-data JSON.
"""

from datetime import date, timedelta
from hashlib import sha256
import json

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, undefer

from backend import reader_service as reader
from backend.database import (
    Case, CaseChunk, CaseOutcome, CaseSource, CaseTag, Citation, CitationMetrics,
    LegislationDocument, LegislationSection, Statute, StatuteReference, StatuteVersion,
)
from performance_helpers import count_statements


@pytest.fixture
def engine():
    engine = create_engine("sqlite:///:memory:")
    for model in (
        Case, CaseChunk, CaseOutcome, CaseSource, CaseTag, Citation, CitationMetrics,
        LegislationDocument, LegislationSection, Statute, StatuteReference, StatuteVersion,
    ):
        model.__table__.create(engine)
    yield engine
    engine.dispose()


def seed(engine, size, repeated=False):
    labels = [
        f"2025 FC {2 if repeated else index + 2}, at para 7"
        for index in range(size)
    ]
    text = "[1] 😀 " + "; ".join(labels) + ". IRPA s. 25(1)(a)."
    with Session(engine) as db:
        db.add(Case(id=1, title="Applicant v Minister", court="Federal Court",
                    date=date(2025, 1, 2), citation="2025 FC 1", full_text=text))
        db.add(CaseChunk(id=1, case_id=1, chunk_set="paragraph", chunk_index=0,
                         paragraph_start=1, paragraph_end=1, text=text,
                         text_hash=sha256(text.encode()).hexdigest(), token_estimate=30))
        # Two layers exercise citation rebasing and span mapping.
        db.add(CaseChunk(id=1000, case_id=1, chunk_set="full_case", chunk_index=0,
                         text=text, text_hash=sha256(text.encode()).hexdigest(),
                         token_estimate=30))
        db.add(CaseSource(case_id=1, source_type="synthetic", is_primary=True))
        db.add(CaseTag(case_id=1, chunk_id=1, category="issue", value="fairness",
                       evidence="😀", offset_start=4, offset_end=5, score=1,
                       source="fixture", taxonomy_version=reader.ACTIVE_TAG_TAXONOMY_VERSION))
        db.add(CitationMetrics(case_id=1, in_degree=1, out_degree=size))
        targets = [2] if repeated else range(2, size + 2)
        for target in targets:
            target_text = "[7] Target authority."
            db.add(Case(id=target, title=f"Target {target}", court="FC",
                        date=date(2025, 1, 1), citation=f"2025 FC {target}"))
            db.add(CaseChunk(id=target, case_id=target, chunk_set="paragraph",
                             chunk_index=0, paragraph_start=7, paragraph_end=7,
                             text=target_text, text_hash=sha256(target_text.encode()).hexdigest(),
                             token_estimate=5, embedding=[0.1] * 1536))
        db.add(LegislationDocument(id=1, instrument_key="canada.irpa", title="Fixture Act",
                                   source_url="https://example.invalid/act"))
        for section in range(1, size + 1):
            db.add(LegislationSection(document_id=1, section_number=str(section),
                                      text=f"Provision {section} 😀", display_order=section))
        cursor = 0
        for index, label in enumerate(labels):
            start = text.index(label, cursor)
            cursor = start + len(label)
            db.add(Citation(source_case_id=1, target_case_id=2 if repeated else index + 2,
                            chunk_id=1000, citation_kind="neutral", citation_text=label,
                            normalized_citation=label, offset_start=start,
                            offset_end=cursor, provenance="local"))
            statute = f"IRPA s. {1 if repeated else index + 1}(1)(a)"
            db.add(StatuteReference(source_case_id=1, chunk_id=1,
                                   reference_kind="statute", reference_text=statute,
                                   normalized_reference=statute, offset_start=start,
                                   offset_end=cursor))
        db.commit()


def invoke(engine, function):
    with Session(engine) as db, count_statements(engine) as counter:
        result = function(1, db)
        # Include serialization, which must not trigger additional lazy SQL.
        payload = (json.loads(result.model_dump_json()) if hasattr(result, "model_dump_json")
                   else [json.loads(row.model_dump_json()) for row in result])
    assert all(statement.lstrip().upper().startswith("SELECT") for statement in counter.statements)
    return payload, counter


@pytest.mark.parametrize("size", [5, 50])
@pytest.mark.parametrize("repeated", [False, True], ids=["distinct", "repeated"])
def test_reader_measurements(engine, size, repeated, monkeypatch):
    seed(engine, size, repeated)
    payload, reader_count = invoke(engine, reader.build_case_reader_data)
    statutes, statute_count = invoke(engine, reader.get_case_statute_references)
    print(f"size={size} repeated={repeated}: reader={reader_count.count} "
          f"statutes={statute_count.count}")
    assert len(payload["citations"]) == len(statutes) == size
    assert all(row["target_chunk_text"] == "[7] Target authority."
               for row in payload["citations"])
    assert all(row["resolution_status"] == "resolved_section" for row in statutes)
    assert reader_count.count <= 13
    assert statute_count.count <= 4
    # A full-projection query oracle for the only reader-data source change.
    # inspect_case remains real and included in both cold-session measurements.
    with monkeypatch.context() as patch:
        patch.setattr(reader, "defer", undefer)
        legacy_payload, _ = invoke(engine, reader.build_case_reader_data)
    assert payload == legacy_payload
    legacy_statutes, legacy_count = invoke(engine, legacy_statute_references)
    assert statutes == legacy_statutes  # entire JSON, including offsets and nulls
    assert legacy_count.count == 2 + 2 * size
    target_selects = [sql for sql in reader_count.statements
                      if "FROM case_chunks" in sql and "case_chunks.case_id IN" in sql]
    assert len(target_selects) == 1
    assert "case_chunks.embedding," not in target_selects[0]


def legacy_statute_references(case_id, db):
    """Frozen pre-optimization row-at-a-time response oracle."""
    assert db.scalar(select(Case.id).where(Case.id == case_id)) is not None
    rows = db.scalars(
        select(StatuteReference).where(StatuteReference.source_case_id == case_id)
        .order_by(StatuteReference.chunk_id, StatuteReference.offset_start, StatuteReference.id)
    )
    results = []
    for reference in rows:
        citation_text = reference.reference_text or reference.normalized_reference or ""
        start = reference.offset_start if reference.offset_start is not None else 0
        raw = reader.RawCitationMatch(
            reference.reference_kind, citation_text,
            reference.normalized_reference or citation_text, start,
            reference.offset_end if reference.offset_end is not None else start,
        )
        resolution = reader.resolve_legislation_reference(db, raw)
        document, section = resolution.document, resolution.section
        url = reference.legislation_url or (document.source_url if document is not None else None)
        results.append(reader.CaseReaderCitationResponse(
            id=-1000000 - reference.id, citation_kind=reference.reference_kind,
            chunk_id=reference.chunk_id, offset_start=reference.offset_start,
            offset_end=reference.offset_end, citation_text=reference.reference_text,
            normalized_citation=reference.normalized_reference,
            instrument_key=resolution.instrument_key or reference.instrument_key,
            pinpoint=resolution.pinpoint or reference.pinpoint, target_case_id=None,
            target_title=None, target_citation=None, provenance="statute_references",
            legislation_url=url,
            authority_document_title=document.title if document is not None else None,
            authority_document_url=document.source_url if document is not None else None,
            authority_section_number=section.section_number if section is not None else None,
            authority_section_text=section.text if section is not None else None,
            source_title=document.title if document is not None else None,
            source_text=section.text if section is not None else None, source_url=url,
            resolution_status=resolution.resolution_status,
            section_number=resolution.provision_section or reference.provision_section,
            provision_text=section.text if section is not None else None,
            provision_section=resolution.provision_section or reference.provision_section,
            provision_subsection=resolution.provision_subsection or reference.provision_subsection,
            provision_paragraph=resolution.provision_paragraph or reference.provision_paragraph,
            provision_nested_depth=resolution.provision_nested_depth,
            provision_is_range_or_list=resolution.is_range_or_list or reference.provision_is_range_or_list,
            unresolved=resolution.resolution_status != "resolved_section",
            statute_version_label=reader.get_statute_version_label(reference.statute_version),
        ))
    return results


def test_all_statute_statuses_nulls_fallbacks_versions_and_duplicates(engine):
    labels = [
        "IRPA s. 1(2)(a)(i)", "Immigration and Refugee Protection Act s. 1(2)(b)",
        "IRPA s. 99", "IRPR s. 4", "IRPA", "IRPA ss. 1 and 2",
        "unidentified instrument", None, "IRPA s. 2",
    ]
    with Session(engine) as db:
        db.add(Case(id=1, title="Fixture", court="FC", date=date(2025, 1, 2)))
        db.add(LegislationDocument(id=1, instrument_key="canada.irpa",
                                   title="Fixture Act", source_url=None))
        db.add(Statute(id=1, instrument_key="canada.irpa", title="Fixture Act",
                       jurisdiction="Canada", statute_type="act", source="fixture"))
        db.add_all([
            LegislationSection(document_id=1, section_number="1", text="One", display_order=1),
            # Historical schema allows duplicates. Keep the old scalar choice.
            LegislationSection(document_id=1, section_number="2", text="First", display_order=2),
            LegislationSection(document_id=1, section_number="2", text="Second", display_order=3),
            StatuteVersion(id=1, statute_id=1, version_number="v1",
                           in_force_date=date(2020, 1, 1)),
            StatuteVersion(id=2, statute_id=1, version_number="v2",
                           in_force_date=date(2024, 1, 1)),
        ])
        for index, label in enumerate(labels):
            db.add(StatuteReference(
                source_case_id=1, reference_kind="instrument", reference_text=label,
                normalized_reference=label if index % 2 == 0 else None,
                offset_start=None if index % 2 else index,
                offset_end=None if index % 2 else index + 3,
                instrument_key="stored.fallback", pinpoint="stored pinpoint",
                provision_section="stored section", provision_subsection="stored subsection",
                provision_paragraph="stored paragraph", provision_is_range_or_list=True,
                legislation_url="https://example.invalid/override" if index % 2 else None,
                statute_version_id=(index % 2) + 1,
            ))
        db.commit()
    expected, _ = invoke(engine, legacy_statute_references)
    actual, counter = invoke(engine, reader.get_case_statute_references)
    assert actual == expected
    assert {row["resolution_status"] for row in actual} == {
        "resolved_section", "section_not_indexed", "document_not_indexed",
        "missing_section", "range_or_list_not_resolved", "instrument_unidentified",
    }
    assert counter.count <= 6  # version batch + duplicate-section scalar fallback
    assert {row["statute_version_label"] for row in actual} == {
        "In force 2020-01-01", "In force 2024-01-01",
    }


def test_empty_and_unknown_cases(engine):
    with Session(engine) as db:
        db.add(Case(id=1, title="Empty", court="FC", date=date(2025, 1, 2)))
        db.commit()
    statutes, counter = invoke(engine, reader.get_case_statute_references)
    assert statutes == []
    assert counter.count == 2
    payload, reader_counter = invoke(engine, reader.build_case_reader_data)
    assert payload["chunks"] == payload["citations"] == []
    assert reader_counter.count == 8
    for function in (reader.build_case_reader_data, reader.get_case_statute_references):
        with Session(engine) as db, pytest.raises(reader.HTTPException) as exc:
            function(999, db)
        assert exc.value.status_code == 404


def test_request_local_lookups_do_not_survive_updates(engine):
    seed(engine, 5, repeated=True)
    before, _ = invoke(engine, reader.get_case_statute_references)
    with Session(engine) as db:
        section = db.scalar(select(LegislationSection).where(
            LegislationSection.section_number == "1"))
        section.text = "Changed fixture provision"
        db.commit()
    after, _ = invoke(engine, reader.get_case_statute_references)
    assert before[0]["provision_text"] != after[0]["provision_text"]
    assert after[0]["provision_text"] == "Changed fixture provision"


def test_statute_batch_boundary_and_distinct_versions(engine):
    with Session(engine) as db:
        db.add(Case(id=1, title="Fixture", court="FC", date=date(2025, 1, 2)))
        db.add(LegislationDocument(id=1, instrument_key="canada.irpa", title="Fixture Act"))
        db.add(Statute(id=1, instrument_key="canada.irpa", title="Fixture Act",
                       jurisdiction="Canada", statute_type="act", source="fixture"))
        for index in range(1, 402):
            db.add(LegislationSection(document_id=1, section_number=str(index),
                                      text=f"Section {index}", display_order=index))
            db.add(StatuteVersion(id=index, statute_id=1, version_number=str(index),
                                 in_force_date=date(2020, 1, 1) + timedelta(days=index)))
            db.add(StatuteReference(source_case_id=1, reference_kind="statute",
                                   normalized_reference=f"IRPA s. {index}",
                                   statute_version_id=index))
        db.commit()
    actual, counter = invoke(engine, reader.get_case_statute_references)
    expected, _ = invoke(engine, legacy_statute_references)
    assert actual == expected
    # case + references + versions + documents + two <=400-pair section batches
    assert counter.count == 6


def test_missing_targets_and_null_offsets_preserve_complete_reader_json(engine, monkeypatch):
    seed(engine, 5)
    with Session(engine) as db:
        db.add_all([
            Citation(source_case_id=1, citation_kind="neutral",
                     citation_text="2020 FC 999", normalized_citation="2020 FC 999",
                     target_case_id=999, unresolved=True),
            Citation(source_case_id=1, citation_kind="neutral",
                     citation_text="2020 FC 998", normalized_citation="2020 FC 998",
                     target_case_id=None, offset_start=0, offset_end=1, unresolved=True),
        ])
        db.commit()
    actual, counter = invoke(engine, reader.build_case_reader_data)
    with monkeypatch.context() as patch:
        patch.setattr(reader, "defer", undefer)
        expected, _ = invoke(engine, reader.build_case_reader_data)
    assert actual == expected
    missing = [row for row in actual["citations"] if row["unresolved"]]
    assert len(missing) == 2
    assert all(row["target_title"] is row["target_case_id"] is None for row in missing)
    assert counter.count == 13


def test_prefetch_preserves_complete_resolver_objects(engine):
    seed(engine, 5)
    matches = [
        reader.RawCitationMatch("statute", text, normalized, index, index + 9)
        for index, (text, normalized) in enumerate([
            ("IRPA s. 1(2)(a)(i)", "IRPA s. 1(2)(a)(i)"),
            ("IRPA s. 1(3)(b)", ""),
            ("IRPR s. 99", "IRPA s. 1"),  # normalized text wins
            ("IRPA s. 99", ""),
            ("IRPR s. 1", ""),
            ("IRPA", ""),
            ("IRPA ss. 1 and 2", ""),
            ("", ""),
            ("unidentified", ""),
        ])
    ]
    with Session(engine) as db:
        lookup = reader._prefetch_legislation_resolver(db, matches)
        for raw in matches:
            # Dataclass equality covers every field, including original spelling,
            # offsets, provision nesting, document/section objects and statuses.
            assert reader.resolve_legislation_reference(lookup, raw) == (
                reader.resolve_legislation_reference(db, raw))
