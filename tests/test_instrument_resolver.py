import pytest

from backend.instrument_resolver import normalize_act_name, resolve_instrument_key
from backend.statutes import LEGISLATION_REGISTRY


@pytest.mark.parametrize(
    "text, court, key",
    [
        ("Immigration and Refugee Protection Act, S.C. 2001, c. 27", None, "canada.irpa"),
        ("immigration and refugee protection act, sc 2001, c 27 (the act)", None, "canada.irpa"),
        ("Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the “Act”) s. 96", None, "canada.irpa"),
        ("IRPA s. 34(1)", None, "canada.irpa"),
        ("irp regulations", None, "canada.irpr"),
        ("Federal Court Rules", None, "canada.federal_courts_rules"),
        ("Federal Court Act", None, "canada.federal_courts_act"),
        ("Patent Act, R.S.C. 1985, c. P-4 s. 27(3)", None, "canada.patent_act"),
        ("NOC Regulations", None, "canada.noc_regulations"),
        ("Trade-marks Act, R.S.C. 1985, c. T-13", None, "canada.trademarks_act"),
        ("Income Tax Act, R.S.C. 1985, c. 1 (5th Supp.)", None, "canada.income_tax_act"),
        ("Criminal Code, R.S.C. 1970, c. C-34", None, "canada.criminal_code"),
        ("Corrections and Conditional Release Act, S.C. 1992, c. 20", None, "canada.corrections_conditional_release_act"),
        ("Controlled Drugs and Substances Act, S.C. 1996, c. 19", None, "canada.controlled_drugs_substances_act"),
        ("Privacy Act", "FC", "canada.privacy_act"),
        ("Supreme Court Act, R.S.C. 1985, c. S-26", "SCC", "canada.supreme_court_act"),
        ("Supreme Court Act", "SCC", "canada.supreme_court_act"),
        ("Supreme Court Act", "FCA", "canada.supreme_court_act"),
    ],
)
def test_names_resolve_to_registered_keys(text, court, key):
    assert resolve_instrument_key(text, court) == key
    assert key in LEGISLATION_REGISTRY


@pytest.mark.parametrize(
    "text, court",
    [
        ("Privacy Act", "SCC"),  # could be a provincial act
        ("Privacy Act", None),
        ("Ontario Privacy Act", "FC"),
        ("Motor Vehicle Act", "FC"),
        ("the Act", "FC"),
        ("under the act", "FC"),
        ("Part II of the Act", "FC"),
        ("Indian Act, R.S.C. 1952, c. 149", "FC"),  # an older consolidation is not the current text
        ("Immigration Act, R.S.C. 1970, c. I-2", "FC"),
        ("Civil Code", "SCC"),
        ("", "FC"),
        (None, "FC"),
    ],
)
def test_ambiguous_generic_or_old_names_stay_unresolved(text, court):
    assert resolve_instrument_key(text, court) is None


def test_normalization_strips_pinpoint_citation_and_filler():
    assert normalize_act_name("Statutes and Regulations Cited Criminal Code, R.S.C. 1985, c. C-46 s. 718") == "criminal code"
    assert normalize_act_name("Indian Act, R.S.C. 1985, c. I-5") == "indian act"
    assert normalize_act_name("In the Immigration Act s. 19") == "immigration act"


def test_every_alias_target_is_a_registered_instrument():
    from backend import instrument_resolver as r

    for key in [*r._ALIASES.values(), *r._FEDERAL_COURT_ONLY.values(), *r._FEDERAL_COURT_AND_SCC.values()]:
        assert key in LEGISLATION_REGISTRY, key
