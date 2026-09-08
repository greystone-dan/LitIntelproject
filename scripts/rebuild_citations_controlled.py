"""Run a bounded, citation-only rebuild with baseline and recovery evidence."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.case_processing import process_case_in_five_layers
from backend.database import Case, Citation, SessionLocal
from scripts.run_overnight import RunLock, atomic_write_json


DEFAULT_RUN_DIR = PROJECT_ROOT / "data" / "overnight_runs" / "citation-only-rebuild"
STATE_FILENAME = "state.json"
BASELINE_FILENAME = "citation-baseline.jsonl"
COMPARISON_FILENAME = "citation-comparison.jsonl"
CHECKPOINT_FILENAME = "case-checkpoints.jsonl"
LOCK_FILENAME = "citation-rebuild.lock"


def now() -> str:
	return datetime.now(timezone.utc).isoformat()


def _citation_snapshot(citation: Citation) -> dict[str, Any]:
	return {
		"id": citation.id,
		"citation_kind": citation.citation_kind,
		"citation_text": citation.citation_text,
		"normalized_citation": citation.normalized_citation,
		"anchor_citation_text": citation.anchor_citation_text,
		"anchor_offset_start": citation.anchor_offset_start,
		"anchor_offset_end": citation.anchor_offset_end,
		"declared_alias": citation.declared_alias,
		"chunk_id": citation.chunk_id,
		"offset_start": citation.offset_start,
		"offset_end": citation.offset_end,
		"target_case_id": citation.target_case_id,
		"unresolved": citation.unresolved,
	}


def _append_baseline(path: Path, case_id: int, citations: list[Citation]) -> None:
	with path.open("a", encoding="utf-8") as handle:
		handle.write(
			json.dumps(
				{
					"case_id": case_id,
					"captured_at": now(),
					"citations": [_citation_snapshot(citation) for citation in citations],
				},
				ensure_ascii=True,
			)
			+ "\n"
		)


def _citation_summary(citations: list[Citation], source_text: str) -> dict[str, Any]:
	kinds: dict[str, int] = {}
	short_forms = 0
	invalid_short_anchors = 0
	for citation in citations:
		kinds[citation.citation_kind] = kinds.get(citation.citation_kind, 0) + 1
		if citation.citation_kind != "case_short":
			continue
		short_forms += 1
		anchor_start = citation.anchor_offset_start
		anchor_end = citation.anchor_offset_end
		anchor_text = citation.anchor_citation_text
		if not anchor_text or anchor_start is None or anchor_end is None or anchor_end <= anchor_start:
			invalid_short_anchors += 1
			continue
		if source_text and source_text[anchor_start:anchor_end] != anchor_text:
			invalid_short_anchors += 1
	return {
		"citation_count": len(citations),
		"citation_kinds": kinds,
		"short_form_count": short_forms,
		"invalid_short_anchor_count": invalid_short_anchors,
	}


def _append_comparison(path: Path, case_id: int, before: list[Citation], after: list[Citation], source_text: str) -> dict[str, Any]:
	comparison = {
		"case_id": case_id,
		"compared_at": now(),
		"before": _citation_summary(before, source_text),
		"after": _citation_summary(after, source_text),
	}
	comparison["citation_count_delta"] = comparison["after"]["citation_count"] - comparison["before"]["citation_count"]
	with path.open("a", encoding="utf-8") as handle:
		handle.write(json.dumps(comparison, ensure_ascii=True) + "\n")
	return comparison


def _append_case_checkpoint(path: Path, case_id: int, status: str, citation_count: int) -> None:
	with path.open("a", encoding="utf-8") as handle:
		handle.write(
			json.dumps(
				{
					"case_id": case_id,
					"status": status,
					"citation_count": citation_count,
					"recorded_at": now(),
				},
				ensure_ascii=True,
			)
			+ "\n"
		)


def _jsonl_rows(path: Path) -> list[dict[str, Any]]:
	if not path.exists():
		return []
	return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _restore_progress_from_evidence(
	state: dict[str, Any],
	checkpoint_path: Path,
	comparison_path: Path,
) -> tuple[int, int]:
	progress_rows = [
			{
				"case_id": row["case_id"],
				"status": "completed",
				"citation_count": row["after"]["citation_count"],
			}
			for row in _jsonl_rows(comparison_path)
	]
	progress_rows.extend(_jsonl_rows(checkpoint_path))

	latest_by_case = {int(row["case_id"]): row for row in progress_rows}
	processed_count = 0
	citation_total = 0
	for case_id in state["case_ids"]:
		row = latest_by_case.get(case_id)
		if row is not None:
			status = str(row["status"])
			if status not in {"completed", "planned", "missing"}:
				break
			case_state = state["cases"][str(case_id)]
			case_state.clear()
			case_state.update({"status": status, "baseline_written": True})
			processed_count += 1
			citation_total += int(row.get("citation_count") or 0)
			continue
		# No evidence row for this case; an operator-recorded terminal status
		# (e.g. an explicit skip) does not break recovery of later cases.
		if state["cases"][str(case_id)].get("status") in {"skipped", "missing"}:
			continue
		break
	return processed_count, citation_total


def _new_state(case_ids: list[int], limit: int, apply: bool) -> dict[str, Any]:
	return {
		"run_id": "",
		"created_at": now(),
		"updated_at": now(),
		"status": "running",
		"mode": "apply" if apply else "dry_run",
		"case_ids": case_ids,
		"limit": limit,
		"stage": "case_citations",
		"target_resolution": "deferred",
		"metrics": "deferred",
		"cases": {str(case_id): {"status": "pending", "baseline_written": False} for case_id in case_ids},
	}


def _write_state(path: Path, state: dict[str, Any]) -> None:
	state["updated_at"] = now()
	atomic_write_json(path, state)


def select_case_ids(*, case_ids: list[int], include_all: bool, limit: int) -> list[int]:
	"""Resolve a bounded explicit cohort before the runner creates run state."""
	selected_ids = sorted(set(case_ids))
	if include_all and selected_ids:
		raise ValueError("--all cannot be combined with --case-id")
	if include_all:
		with SessionLocal() as session:
			selected_ids = list(
				session.scalars(
					select(Case.id)
					.where(Case.full_text.is_not(None), Case.full_text != "")
					.order_by(Case.id)
					.limit(limit)
				)
			)
	return selected_ids


def run(
	*,
	case_ids: list[int],
	limit: int,
	run_dir: Path,
	apply: bool = False,
	confirm_citation_rebuild: bool = False,
	resume: bool = False,
	progress_every: int = 10,
) -> dict[str, Any]:
	"""Create evidence in dry-run mode or replace only selected citation rows."""
	selected_ids = sorted(set(case_ids))
	if not selected_ids:
		raise ValueError("At least one --case-id is required")
	if limit < 1:
		raise ValueError("--limit must be positive")
	if len(selected_ids) > limit:
		raise ValueError("The explicit case cohort exceeds --limit")
	if apply and not confirm_citation_rebuild:
		raise ValueError("Apply mode requires --confirm-citation-rebuild")
	if progress_every < 1:
		raise ValueError("--progress-every must be positive")

	run_dir.mkdir(parents=True, exist_ok=True)
	state_path = run_dir / STATE_FILENAME
	baseline_path = run_dir / BASELINE_FILENAME
	comparison_path = run_dir / COMPARISON_FILENAME
	checkpoint_path = run_dir / CHECKPOINT_FILENAME
	if state_path.exists():
		if not resume:
			raise ValueError(f"Run state already exists: {state_path}; use --resume")
		state = json.loads(state_path.read_text(encoding="utf-8"))
		if state.get("case_ids") != selected_ids or state.get("mode") != ("apply" if apply else "dry_run"):
			raise ValueError("Resume arguments do not match the existing run state")
		processed_count, citation_total = _restore_progress_from_evidence(
			state,
			checkpoint_path,
			comparison_path,
		)
		state["status"] = "running"
		state.pop("stop_reason", None)
		_write_state(state_path, state)
	else:
		state = _new_state(selected_ids, limit, apply)
		state["run_id"] = run_dir.name
		_write_state(state_path, state)
		processed_count = 0
		citation_total = 0

	with RunLock(run_dir / LOCK_FILENAME):
		with SessionLocal() as session:
			for case_id in selected_ids:
				case_state = state["cases"][str(case_id)]
				if resume and case_state["status"] in {"completed", "planned", "missing", "skipped"}:
					continue
				try:
					case = session.scalar(select(Case).where(Case.id == case_id))
					if case is None:
						case_state["status"] = "missing"
						_append_case_checkpoint(checkpoint_path, case_id, "missing", 0)
						processed_count += 1
						if processed_count % progress_every == 0:
							_write_state(state_path, state)
							print(
								f"Cases Processed [{processed_count}] - Citations Extracted [{citation_total}]",
								flush=True,
							)
						continue
					existing = list(
							session.scalars(
								select(Citation)
								.where(Citation.source_case_id == case_id)
								.order_by(Citation.id)
							)
						)
					if not case_state["baseline_written"]:
						_append_baseline(baseline_path, case_id, existing)
						case_state["baseline_written"] = True
					if apply:
						process_case_in_five_layers(
							session,
							case_id,
							stage_order=("case_citations",),
						)
						session.flush()
						after = list(
							session.scalars(
								select(Citation)
								.where(Citation.source_case_id == case_id)
								.order_by(Citation.id)
							)
						)
						comparison = _append_comparison(
							comparison_path,
							case_id,
							existing,
							after,
							getattr(case, "full_text", None) or getattr(case, "summary", None) or "",
						)
						if comparison["after"]["invalid_short_anchor_count"]:
							raise ValueError("Rebuilt short form has invalid direct anchor provenance")
						if comparison["before"]["citation_count"] and not comparison["after"]["citation_count"]:
							raise ValueError("Citation rebuild removed every existing citation; review baseline before retrying")
						citation_total += comparison["after"]["citation_count"]
						session.commit()
						case_state["status"] = "completed"
						_append_case_checkpoint(
							checkpoint_path,
							case_id,
							"completed",
							comparison["after"]["citation_count"],
						)
					else:
						case_state["status"] = "planned"
						citation_total += len(existing)
						_append_case_checkpoint(checkpoint_path, case_id, "planned", len(existing))
				except Exception as error:
					session.rollback()
					case_state["status"] = "failed"
					case_state["error"] = f"{type(error).__name__}: {error}"
					_write_state(state_path, state)
					raise
				processed_count += 1
				if processed_count % progress_every == 0:
					_write_state(state_path, state)
					print(
						f"Cases Processed [{processed_count}] - Citations Extracted [{citation_total}]",
						flush=True,
					)
			if processed_count % progress_every:
				_write_state(state_path, state)
				print(
					f"Cases Processed [{processed_count}] - Citations Extracted [{citation_total}]",
					flush=True,
				)

	state["status"] = "completed" if apply else "dry_run"
	_write_state(state_path, state)
	return state


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--case-id", type=int, action="append", default=[], help="Case ID to include; repeat for a bounded cohort.")
	parser.add_argument("--all", action="store_true", help="Select all text-bearing cases up to --limit and record the resulting IDs in state.")
	parser.add_argument("--limit", type=int, required=True, help="Maximum allowed selected cases; required in all modes.")
	parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN_DIR)
	parser.add_argument("--dry-run", action="store_true", help="Explicitly request the default non-mutating mode.")
	parser.add_argument("--apply", action="store_true", help="Replace citations only after reviewing a dry-run baseline.")
	parser.add_argument("--confirm-citation-rebuild", action="store_true", help="Required with --apply.")
	parser.add_argument("--resume", action="store_true", help="Resume matching state and skip completed/planned cases.")
	parser.add_argument("--progress-every", type=int, default=10, help="Print cumulative progress every N processed cases.")
	args = parser.parse_args()
	if args.dry_run and args.apply:
		raise SystemExit("--dry-run and --apply cannot be combined")
	if args.limit < 1:
		raise SystemExit("--limit must be positive")
	if args.progress_every < 1:
		raise SystemExit("--progress-every must be positive")
	case_ids = select_case_ids(case_ids=args.case_id, include_all=args.all, limit=args.limit)
	try:
		state = run(
			case_ids=case_ids,
			limit=args.limit,
			run_dir=args.run_dir,
			apply=args.apply,
			confirm_citation_rebuild=args.confirm_citation_rebuild,
			resume=args.resume,
			progress_every=args.progress_every,
		)
	except KeyboardInterrupt:
		state_path = args.run_dir / STATE_FILENAME
		if state_path.exists():
			state = json.loads(state_path.read_text(encoding="utf-8"))
			state["status"] = "stopped"
			state["stop_reason"] = "operator_interrupt"
			_write_state(state_path, state)
		print("status=stopped reason=operator_interrupt", flush=True)
		raise SystemExit(130) from None
	print(f"status={state['status']} cases={len(state['cases'])} stage=case_citations resolution=deferred metrics=deferred")


if __name__ == "__main__":
	main()