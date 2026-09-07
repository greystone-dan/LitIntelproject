import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from scripts import rebuild_citations_controlled


class FakeSession:
	def __init__(self, case_id=41):
		self.case_id = case_id
		self.commits = 0
		self.rollbacks = 0
		self.flushes = 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		return False

	def scalar(self, statement):
		return SimpleNamespace(id=self.case_id)

	def scalars(self, statement):
		return [
			SimpleNamespace(
				id=9,
				citation_kind="case_short",
				citation_text="Albert at para. 40",
				normalized_citation="Albert v. Canada (MCI), 2020 FC 100, at para. 40",
				anchor_citation_text="Albert v. Canada (MCI), 2020 FC 100 [Albert] at para. 30",
				anchor_offset_start=0,
				anchor_offset_end=63,
				declared_alias=None,
				chunk_id=5,
				offset_start=12,
				offset_end=30,
				target_case_id=None,
				unresolved=True,
			)
		]

	def commit(self):
		self.commits += 1

	def flush(self):
		self.flushes += 1

	def rollback(self):
		self.rollbacks += 1


def test_dry_run_writes_baseline_and_never_rebuilds(tmp_path, monkeypatch):
	session = FakeSession()
	monkeypatch.setattr(rebuild_citations_controlled, "SessionLocal", lambda: session)
	monkeypatch.setattr(
		rebuild_citations_controlled,
		"process_case_in_five_layers",
		lambda *_args, **_kwargs: pytest.fail("dry run must not replace citations"),
	)

	state = rebuild_citations_controlled.run(case_ids=[41], limit=1, run_dir=tmp_path)

	assert state["status"] == "dry_run"
	assert state["target_resolution"] == "deferred"
	assert state["metrics"] == "deferred"
	assert state["cases"]["41"]["status"] == "planned"
	assert session.commits == 0
	baseline = [json.loads(line) for line in (tmp_path / "citation-baseline.jsonl").read_text(encoding="utf-8").splitlines()]
	assert baseline[0]["case_id"] == 41
	assert baseline[0]["citations"][0]["citation_text"] == "Albert at para. 40"


def test_apply_requires_confirmation_and_runs_only_citation_stage(tmp_path, monkeypatch):
	with pytest.raises(ValueError, match="confirm-citation-rebuild"):
		rebuild_citations_controlled.run(case_ids=[41], limit=1, run_dir=tmp_path, apply=True)

	session = FakeSession()
	calls = []
	monkeypatch.setattr(rebuild_citations_controlled, "SessionLocal", lambda: session)
	monkeypatch.setattr(
		rebuild_citations_controlled,
		"process_case_in_five_layers",
		lambda _session, case_id, *, stage_order: calls.append((case_id, stage_order)) or {"case_citations": 1},
	)

	state = rebuild_citations_controlled.run(
		case_ids=[41],
		limit=1,
		run_dir=tmp_path / "apply",
		apply=True,
		confirm_citation_rebuild=True,
	)

	assert state["status"] == "completed"
	assert calls == [(41, ("case_citations",))]
	assert session.commits == 1
	assert session.flushes == 1
	assert (tmp_path / "apply" / "citation-baseline.jsonl").exists()
	comparison = json.loads((tmp_path / "apply" / "citation-comparison.jsonl").read_text(encoding="utf-8"))
	assert comparison["after"]["invalid_short_anchor_count"] == 0


def test_apply_rolls_back_when_rebuild_removes_every_existing_citation(tmp_path, monkeypatch):
	class EmptyAfterSession(FakeSession):
		def __init__(self):
			super().__init__()
			self.batches = iter([super().scalars(None), []])

		def scalars(self, statement):
			return next(self.batches)

	session = EmptyAfterSession()
	monkeypatch.setattr(rebuild_citations_controlled, "SessionLocal", lambda: session)
	monkeypatch.setattr(
		rebuild_citations_controlled,
		"process_case_in_five_layers",
		lambda *_args, **_kwargs: {"case_citations": 0},
	)

	with pytest.raises(ValueError, match="removed every existing citation"):
		rebuild_citations_controlled.run(
			case_ids=[41],
			limit=1,
			run_dir=tmp_path,
			apply=True,
			confirm_citation_rebuild=True,
		)

	assert session.commits == 0
	assert session.rollbacks == 1


def test_run_rejects_unbounded_or_mismatched_cohort(tmp_path):
	with pytest.raises(ValueError, match="At least one"):
		rebuild_citations_controlled.run(case_ids=[], limit=1, run_dir=tmp_path)
	with pytest.raises(ValueError, match="exceeds"):
		rebuild_citations_controlled.run(case_ids=[1, 2], limit=1, run_dir=tmp_path)


def test_all_selection_is_bounded_and_cannot_mix_explicit_case_ids(monkeypatch):
	class SelectionSession:
		def __enter__(self):
			return self

		def __exit__(self, exc_type, exc_value, traceback):
			return False

		def scalars(self, statement):
			return [41, 42]

	monkeypatch.setattr(rebuild_citations_controlled, "SessionLocal", lambda: SelectionSession())

	assert rebuild_citations_controlled.select_case_ids(case_ids=[], include_all=True, limit=2) == [41, 42]
	with pytest.raises(ValueError, match="cannot be combined"):
		rebuild_citations_controlled.select_case_ids(case_ids=[41], include_all=True, limit=2)