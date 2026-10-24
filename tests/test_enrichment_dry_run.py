import sys
from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session

from backend.database import Case
from scripts import chunk_cases, tag_cases, tag_cases_v2, tag_cases_v3


TAG_SCRIPTS = [tag_cases, tag_cases_v2, tag_cases_v3]


@pytest.fixture
def case():
    return Case(
        id=42,
        title="Example v Canada",
        court="FC",
        summary="IRCC considered the application.",
        full_text="[1] The application for judicial review is dismissed.",
        source_type="canlii",
    )


@pytest.fixture
def db(case):
    session = MagicMock(spec=Session)
    session.__enter__.return_value = session
    session.scalars.return_value.all.return_value = [case]
    session.scalars.return_value.__iter__.side_effect = lambda: iter([case])
    session.scalar.side_effect = [7, 3]
    return session


def run_main(monkeypatch, module, db, args):
    monkeypatch.setattr(module, "SessionLocal", lambda: db)
    monkeypatch.setattr(sys, "argv", [module.__file__, *args])
    module.main()


def assert_read_only(db):
    for method in ("execute", "add", "add_all", "delete", "flush", "commit", "merge", "bulk_save_objects"):
        getattr(db, method).assert_not_called()
    for call in [*db.scalars.call_args_list, *db.scalar.call_args_list]:
        assert call.args[0].is_select


@pytest.mark.parametrize("replace_existing", [False, True])
@pytest.mark.parametrize("scope", ["case-id", "csv", "both"])
def test_chunk_scoped_dry_run_is_read_only(
    monkeypatch, tmp_path, db, case, capsys, replace_existing, scope
):
    args = ["--dry-run"]
    if scope in ("case-id", "both"):
        args += ["--case-id", "42", "--case-id", "42"]
    if scope in ("csv", "both"):
        path = tmp_path / "cases.csv"
        path.write_text("case_id\n42\n42\n", encoding="utf-8")
        args += ["--case-ids-csv", str(path)]
    if replace_existing:
        args.append("--replace-existing")

    run_main(monkeypatch, chunk_cases, db, args)

    assert_read_only(db)
    statement = db.scalars.call_args.args[0]
    assert statement.compile().params == {"id_1": [42]}
    output = capsys.readouterr().out
    expected = len(chunk_cases.build_case_chunk_layers(case))
    assert f"pending_sample=1 estimated_chunks={expected}" in output
    if replace_existing:
        assert "chunks_to_delete=7" in output
        count_query = db.scalar.call_args.args[0]
        assert count_query.compile().params == {"case_id_1": [42]}
    else:
        db.scalar.assert_not_called()


@pytest.mark.parametrize("replace_existing", [False, True])
def test_chunk_real_run_honors_replace_existing(monkeypatch, db, case, capsys, replace_existing):
    args = ["--case-id", "42"]
    if replace_existing:
        args.append("--replace-existing")

    run_main(monkeypatch, chunk_cases, db, args)

    if replace_existing:
        db.execute.assert_called_once()
        statement = db.execute.call_args.args[0]
        assert statement.is_delete
        assert statement.compile().params == {"case_id_1": [42]}
    else:
        db.execute.assert_not_called()
    db.add_all.assert_called_once()
    rows = db.add_all.call_args.args[0]
    assert len(rows) == len(chunk_cases.build_case_chunk_layers(case))
    assert all(row.case_id == 42 for row in rows)
    db.commit.assert_called_once()
    assert f"cases_chunked=1 chunks_created={len(rows)}" in capsys.readouterr().out


def test_chunk_pending_dry_run_remains_read_only(monkeypatch, db, capsys):
    run_main(
        monkeypatch, chunk_cases, db,
        ["--dry-run", "--court", "FC", "--source-type", "canlii", "--limit", "2"],
    )

    assert_read_only(db)
    statement = db.scalars.call_args.args[0]
    assert "EXISTS" in str(statement)
    params = statement.compile().params
    assert params["court_1"] == "FC"
    assert params["source_type_1"] == "canlii"
    assert params["param_1"] == 2
    assert "pending_sample=1" in capsys.readouterr().out


@pytest.mark.parametrize("module", TAG_SCRIPTS, ids=lambda module: module.__name__)
@pytest.mark.parametrize("retag", [False, True])
def test_tag_dry_run_is_read_only(monkeypatch, db, capsys, module, retag):
    args = ["--dry-run", "--court", "FC", "--limit", "2"]
    if retag:
        args.append("--retag")
    if module is tag_cases:
        args += ["--source-type", "canlii"]

    run_main(monkeypatch, module, db, args)

    assert_read_only(db)
    statement = db.scalars.call_args.args[0]
    assert ("EXISTS" in str(statement)) is not retag
    params = statement.compile().params
    assert params["court_1"] == "FC"
    assert params["param_1"] == 2
    if module is tag_cases:
        assert params["source_type_1"] == "canlii"
    output = capsys.readouterr().out
    assert "pending_sample=1" in output
    assert f"taxonomy={module.TAXONOMY_VERSION}" in output
    if retag:
        assert "tags_to_delete=7 statuses_to_delete=3" in output
        assert db.scalar.call_count == 2
        for call, table in zip(db.scalar.call_args_list, ("case_tags", "case_tagging_status")):
            assert table in str(call.args[0])
            assert call.args[0].compile().params == {"taxonomy_version_1": module.TAXONOMY_VERSION}
    else:
        db.scalar.assert_not_called()


@pytest.mark.parametrize("module", TAG_SCRIPTS, ids=lambda module: module.__name__)
@pytest.mark.parametrize("retag", [False, True])
def test_tag_real_run_preserves_deletes_and_processing(monkeypatch, db, capsys, module, retag):
    events = []
    db.execute.side_effect = lambda statement: events.append(statement)
    db.commit.side_effect = lambda: events.append("commit")
    result = (1, 2) if module is tag_cases else (1, 2, 0)
    processor = MagicMock(side_effect=lambda *args, **kwargs: events.append("tag") or result)
    monkeypatch.setattr(module, "tag_pending_cases", processor)
    args = ["--court", "FC", "--limit", "2", "--batch-size", "1"]
    if retag:
        args.append("--retag")

    run_main(monkeypatch, module, db, args)

    if retag:
        assert len(events) == 4
        for statement, table in zip(events[:2], ("case_tags", "case_tagging_status")):
            assert statement.is_delete
            assert table in str(statement)
            assert statement.compile().params == {"taxonomy_version_1": module.TAXONOMY_VERSION}
        assert events[2:] == ["commit", "tag"]
    else:
        assert events == ["tag"]
        db.execute.assert_not_called()
        db.commit.assert_not_called()
    processor.assert_called_once()
    assert processor.call_args.args[0] is db
    assert processor.call_args.kwargs["court"] == "FC"
    assert processor.call_args.kwargs["limit"] == 2
    assert processor.call_args.kwargs["batch_size"] == 1
    assert "cases_tagged=1 tags_created=2" in capsys.readouterr().out


def test_chunk_pending_real_run_preserves_processing(monkeypatch, db):
    processor = MagicMock(return_value=(1, 3))
    monkeypatch.setattr(chunk_cases, "chunk_pending_cases", processor)

    run_main(
        monkeypatch, chunk_cases, db,
        ["--court", "FCA", "--source-type", "canlii", "--limit", "2", "--batch-size", "1"],
    )

    processor.assert_called_once_with(
        db, batch_size=1, limit=2, court="FCA", source_type="canlii"
    )
