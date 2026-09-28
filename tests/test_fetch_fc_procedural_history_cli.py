from argparse import Namespace

from scripts import fetch_fc_procedural_history


def test_activity_document_identity_requires_both_registry_keys():
    assert fetch_fc_procedural_history._activity_document_identity("10", "7") == ("10", "7")
    assert fetch_fc_procedural_history._activity_document_identity("10", None) is None
    assert fetch_fc_procedural_history._activity_document_identity(None, "7") is None


def test_empty_prototype_history_set_is_successful_noop(monkeypatch, capsys):
    monkeypatch.setattr(
        fetch_fc_procedural_history,
        "parse_args",
        lambda: Namespace(
            imm_numbers=None,
            imm_file=None,
            from_prototype=True,
            generate_years=None,
            max_imm=25000,
            update=False,
            reverse=False,
            delay_ms=2000,
            diagnostic_allow_sub_2000ms_delay=False,
            adaptive_delay=False,
            batch_size=20,
            issue_pause_ms=5000,
            backoff_factor=2.0,
            max_delay_ms=2000,
            jitter_ms=500,
            max_requests=100,
            limit=None,
            dry_run=False,
            write_activity=False,
            log_file=None,
        ),
    )
    monkeypatch.setattr(fetch_fc_procedural_history, "load_imm_from_prototype", lambda: [])

    fetch_fc_procedural_history.main()

    assert "No prototype IMM numbers require" in capsys.readouterr().out