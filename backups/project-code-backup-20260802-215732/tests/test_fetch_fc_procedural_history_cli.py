from argparse import Namespace

from scripts import fetch_fc_procedural_history


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
            delay_ms=1000,
            limit=None,
            dry_run=False,
        ),
    )
    monkeypatch.setattr(fetch_fc_procedural_history, "load_imm_from_prototype", lambda: [])

    fetch_fc_procedural_history.main()

    assert "No prototype IMM numbers require" in capsys.readouterr().out