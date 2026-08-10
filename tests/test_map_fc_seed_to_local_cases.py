from __future__ import annotations

from scripts.map_fc_seed_to_local_cases import _neutral_from_canlii_docid


def test_neutral_from_canlii_docid_fc() -> None:
    assert _neutral_from_canlii_docid("2024fc1268") == "2024 FC 1268"


def test_neutral_from_canlii_docid_fct_converts_to_fc() -> None:
    assert _neutral_from_canlii_docid("2012fct853") == "2012 FC 853"


def test_neutral_from_canlii_docid_unsupported_court_returns_none() -> None:
    assert _neutral_from_canlii_docid("2025onsc527") is None
