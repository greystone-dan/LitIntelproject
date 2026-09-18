import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from backend.legal_tagger_v3 import CoreLegalTaggerV3, TAXONOMY_VERSION
from scripts import tag_cases_v3
from scripts.tag_cases_v3 import build_case_tag_rows


PROPOSAL_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "eval"
    / "reports"
    / "tagging-v3-core-whitelist-proposal.json"
)


def load_proposal() -> dict:
    return json.loads(PROPOSAL_PATH.read_text(encoding="utf-8"))


def all_aliases(proposal: dict) -> set[str]:
    return {
        alias
        for category in proposal["categories"].values()
        for aliases in category.values()
        for alias in aliases
    }


class _ScalarResult:
    def __init__(self, rows):
        self._rows = rows

    def all(self):
        return self._rows


class _FakePipe:
    def __init__(self, results=None):
        self._results = results

    def poll(self, _timeout):
        return self._results is not None

    def recv(self):
        if self._results is None:
            raise RuntimeError("no results available")
        return self._results

    def close(self):
        return None


class _FakeProcess:
    def __init__(self, should_return_results: bool, results=None):
        self.should_return_results = should_return_results
        self.results = results
        self.started = False
        self.terminated = False

    def start(self):
        self.started = True

    def is_alive(self):
        return self.should_return_results

    def terminate(self):
        self.terminated = True

    def join(self, _timeout):
        return None


class _FakeContext:
    def __init__(self, should_return_results: bool, results=None):
        self.should_return_results = should_return_results
        self.results = results

    def Pipe(self, duplex=False):
        return _FakePipe(), _FakePipe(self.results)

    def Process(self, target, args):
        return _FakeProcess(self.should_return_results, self.results)


class _FakeSession:
    def __init__(self, cases, statuses=None):
        self.cases = list(cases)
        self.statuses = dict(statuses or {})
        self.added = []
        self.added_all = []
        self.commits = 0
        self.rollbacks = 0

    def _complete_case_ids(self):
        return {case_id for case_id, tags_count in self.statuses.items() if tags_count >= 0}

    def scalars(self, statement):
        text = str(statement)
        if "FROM cases" in text or "FROM cases " in text:
            rows = [case for case in self.cases if case.id not in self._complete_case_ids()]
            return _ScalarResult(rows)
        raise AssertionError(f"Unexpected scalars statement: {statement!r}")

    def scalar(self, statement):
        text = str(statement)
        for case_id, tags_count in self.statuses.items():
            if f"case_id = {case_id}" in text and f"tags_count = {tags_count}" in text:
                return SimpleNamespace(case_id=case_id, taxonomy_version=TAXONOMY_VERSION, tags_count=tags_count)
        return None

    def add(self, row):
        self.added.append(row)
        if row.__class__.__name__ == "CaseTaggingStatus":
            self.statuses[row.case_id] = row.tags_count

    def add_all(self, rows):
        rows = list(rows)
        self.added_all.extend(rows)
        for row in rows:
            if row.__class__.__name__ == "CaseTaggingStatus":
                self.statuses[row.case_id] = row.tags_count

    def commit(self):
        self.commits += 1

    def rollback(self):
        self.rollbacks += 1


def _case(
    case_id: int,
    text: str | None = "IRCC and GCMS notes",
    summary: str | None = None,
) -> SimpleNamespace:
    return SimpleNamespace(id=case_id, full_text=text, summary=summary, court="FC", date=None)


def test_v3_proposal_is_inactive_and_versioned():
    proposal = load_proposal()

    assert proposal["taxonomy_version"] == "ca_legal_v3_core"
    assert proposal["review_status"] == "proposed"
    assert "required_evidence_for_alias" in proposal["alias_policy"]


def test_agency_core_signals_have_whitelist_aliases():
    proposal = load_proposal()
    aliases = all_aliases(proposal)

    for facet in proposal["agency_research_facets"].values():
        assert set(facet["core_signals"]).issubset(aliases)


def test_contextual_terms_are_not_core_signals():
    proposal = load_proposal()
    aliases = all_aliases(proposal)
    contextual_terms = set(proposal["contextual_only_until_review"])

    assert contextual_terms.isdisjoint(aliases)
    assert contextual_terms.isdisjoint(
        {
            signal
            for facet in proposal["agency_research_facets"].values()
            for signal in facet["core_signals"]
        }
    )


def test_reviewed_alias_variants_are_present():
    aliases = all_aliases(load_proposal())

    assert {"H&C", "H & C", "H and C"}.issubset(aliases)
    assert {"security screening", "security-screening"}.issubset(aliases)
    assert {"PGWP", "Post-Graduation Work Permit", "Post Graduation Work Permit"}.issubset(aliases)
    assert "Pre Removal Risk Assessment" in aliases


def test_known_generic_terms_remain_excluded():
    proposal = load_proposal()
    aliases = all_aliases(proposal)

    for term in ("Canada", "application", "decision", "removal", "detention", "hearing"):
        assert term not in aliases
        assert term in proposal["excluded_from_core"] or term in proposal["contextual_only_until_review"]


def test_v3_tagger_matches_explicit_agency_and_process_aliases():
    tags = CoreLegalTaggerV3().tag(
        "IRCC reviewed the GCMS notes after a PFL. CBSA filed a section 44 report."
    )
    values = {(tag.category, tag.value) for tag in tags}

    assert ("agency", "ircc") in values
    assert ("procedure_or_record", "gcms") in values
    assert ("procedure_or_record", "procedural_fairness_letter") in values
    assert ("agency", "cbsa") in values
    assert ("procedure_or_record", "section_44_report") in values
    assert all(tag.taxonomy_version == TAXONOMY_VERSION for tag in tags)


def test_v3_tagger_preserves_exact_occurrence_offsets():
    text = "The applicant requested an H & C review and an Express Entry record."
    occurrences = CoreLegalTaggerV3().tag_occurrences(text)

    assert all(text[item.offset_start:item.offset_end] == item.evidence for item in occurrences)
    assert {item.value for item in occurrences} == {
        "humanitarian_and_compassionate",
        "express_entry",
    }


def test_v3_tagger_does_not_infer_contextual_terms_or_findings():
    tags = CoreLegalTaggerV3().tag(
        "The application decision discussed detention, removal, and credibility."
    )

    assert not tags


def test_v3_pipeline_preserves_repeated_occurrences_and_evidence_metadata():
    rows = build_case_tag_rows("IRCC contacted IRCC about GCMS notes.")
    ircc_rows = [row for row in rows if row["value"] == "ircc"]

    assert len(ircc_rows) == 2
    assert ircc_rows[0]["offset_start"] != ircc_rows[1]["offset_start"]
    for row in rows:
        assert row["rule_id"] == f"{row['category']}.{row['value']}"
        assert row["language"] == "unknown"
        assert row["evidence_role"] == "mention"
        assert row["taxonomy_version"] == TAXONOMY_VERSION
        assert row["source"] == "core_whitelist"


def test_successful_status_suppresses_pending_cases():
    session = _FakeSession([
        _case(1),
        _case(2),
    ], statuses={1: 3})

    pending = session.scalars(tag_cases_v3.pending_case_query()).all()

    assert [case.id for case in pending] == [2]


def test_failed_status_remains_pending():
    session = _FakeSession([
        _case(1),
    ], statuses={1: -1})

    pending = session.scalars(tag_cases_v3.pending_case_query()).all()

    assert [case.id for case in pending] == [1]


def test_timeout_or_crash_records_retryable_failure_without_raising_unsafe_state(monkeypatch):
    session = _FakeSession([
        _case(1),
    ])
    monkeypatch.setattr(tag_cases_v3.multiprocessing, "get_context", lambda _mode: _FakeContext(False))

    cases_tagged, tags_created, skipped_cases = tag_cases_v3.tag_pending_cases(
        session,
        batch_size=1,
        batch_timeout=0.01,
        limit=1,
    )

    assert (cases_tagged, tags_created, skipped_cases) == (1, 0, 1)
    assert session.rollbacks == 1
    assert session.commits == 1
    assert session.statuses[1] == -1
    assert [case.id for case in session.scalars(tag_cases_v3.pending_case_query()).all()] == [1]


def test_summary_only_cases_follow_the_active_v3_text_contract(monkeypatch):
    summary_only = _case(1, text=None, summary="IRCC and GCMS notes")
    empty_case = _case(2, text=None, summary=None)
    session = _FakeSession([
        summary_only,
        empty_case,
    ])
    captured_payloads = []

    class _PipeState:
        def __init__(self):
            self.results = None
            self.started = False

    class _PayloadAwarePipe:
        def __init__(self, state: _PipeState):
            self._state = state

        def poll(self, _timeout):
            return self._state.started

        def recv(self):
            if self._state.results is None:
                raise RuntimeError("no results available")
            return self._state.results

        def close(self):
            return None

    class _PayloadAwareProcess:
        def __init__(self, state: _PipeState, payloads):
            self._state = state
            self._payloads = payloads

        def start(self):
            self._state.started = True
            captured_payloads.extend(self._payloads)
            self._state.results = [
                (case_id, build_case_tag_rows(text))
                for case_id, text in self._payloads
            ]

        def is_alive(self):
            return False

        def terminate(self):
            return None

        def join(self, _timeout):
            return None

    class _PayloadAwareContext:
        def __init__(self):
            self.state = _PipeState()

        def Pipe(self, duplex=False):
            return _PayloadAwarePipe(self.state), _PayloadAwarePipe(self.state)

        def Process(self, target, args):
            return _PayloadAwareProcess(self.state, args[0])

    monkeypatch.setattr(tag_cases_v3.multiprocessing, "get_context", lambda _mode: _PayloadAwareContext())

    cases_tagged, tags_created, skipped_cases = tag_cases_v3.tag_pending_cases(
        session,
        batch_size=2,
        batch_timeout=0.01,
        limit=2,
    )

    assert captured_payloads == [(1, "IRCC and GCMS notes"), (2, "")]
    assert (cases_tagged, tags_created, skipped_cases) == (2, 2, 0)
    assert session.statuses[1] == 2
    assert session.statuses[2] == 0