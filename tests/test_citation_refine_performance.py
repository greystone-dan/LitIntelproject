"""Long lists of provisions (as in a Supreme Court "Statutes and Regulations Cited" block) must scan in linear time."""

from __future__ import annotations

import time

from backend import citations
from backend.citation_refine import laws, refine_document

LONG_LIST = (
    "Criminal Code, R.S.C. 1985, c. C-46, ss. 34 , 232 , 267 (b), 268 , 469 , 515(1) , (2) , (4) to (4.3) , (5) , (6) , (8) , "
    "(10) , 517(1) (b), 518 , 520 , 521 , 523(2) (b), 680 , 687 , 718.2 (d), 719(3) , (3.1) , 723 , 730 , 731 , 732.1(3) , 734 .\n"
)
LIMIT_SECONDS = 3.0


def _elapsed(pattern, text: str) -> float:
    started = time.perf_counter()
    list(pattern.finditer(text))
    return time.perf_counter() - started


def test_provision_patterns_do_not_backtrack_on_long_lists() -> None:
    text = "Statutes and Regulations Cited\n" + LONG_LIST * 6
    assert _elapsed(laws.PROVISION_THEN_ACRONYM_RE, text) < LIMIT_SECONDS
    assert _elapsed(laws.PROVISION_OF_INSTRUMENT_RE, text) < LIMIT_SECONDS
    assert _elapsed(citations.SECTIONS_OF_STATUTE_RE, text) < LIMIT_SECONDS


def test_refine_document_finishes_on_a_long_judgment_style_block() -> None:
    text = "[1] The appeal concerns the Immigration and Refugee Protection Act.\n" + LONG_LIST * 6 + "[2] Reasons follow. " * 50
    started = time.perf_counter()
    refine_document(text)
    assert time.perf_counter() - started < LIMIT_SECONDS * 3


def test_ordinary_provision_lists_still_match() -> None:
    match = citations.SECTIONS_OF_STATUTE_RE.search("see ss. 96, 97 and 98 of the IRPA for details")
    assert match and match.group(2) == "IRPA"
    assert "96" in match.group(1) and "98" in match.group(1)
    assert laws.PROVISION_OF_INSTRUMENT_RE.search("under paragraph 36(1)(a) of the IRPA")
    assert laws.PROVISION_THEN_ACRONYM_RE.search("r. 117(9)(d) IRPR")
