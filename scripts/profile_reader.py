"""Time where a decision's reader payload spends its time (read-only).

Runs build_case_reader_data for one case with per-stage wall times, SQL statement
count and the slowest statements, then the real FastAPI route through TestClient
(validation, JSON encoding, middleware) so any gap between the function and the
HTTP response is visible. Only SELECTs are issued; the session is rolled back.

    python scripts/profile_reader.py 35874
    python scripts/profile_reader.py 35874 28926 --profile-file logs/profile_reader.txt
"""

from __future__ import annotations

import argparse
import cProfile
import functools
import io
import json
import pstats
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import event  # noqa: E402

from backend import reader_service  # noqa: E402
from backend.database import SessionLocal, engine  # noqa: E402

STAGE_FUNCTIONS = (
	"_cached_inspect_case",
	"_build_evidence_summary",
	"_build_reader_inferred_tags",
	"_incoming_cited_case_counts",
	"_match_pinpoint_chunks",
	"_build_reader_extracted_summary",
	"_build_reader_extracted_metadata",
	"_build_reader_outcome_metadata",
	"load_paragraph_cited_by",
	"load_target_cited_by",
	"format_decision",
	"locate_chunk_layers",
	"map_span_to_located_layers",
	"extract_metadata_observations",
)


class StageTimer:
	def __init__(self) -> None:
		self.totals: dict[str, float] = {}
		self.calls: dict[str, int] = {}

	def wrap(self, module, name: str) -> None:
		original = getattr(module, name, None)
		if original is None:
			return

		@functools.wraps(original)
		def timed(*args, **kwargs):
			start = time.perf_counter()
			try:
				return original(*args, **kwargs)
			finally:
				self.totals[name] = self.totals.get(name, 0.0) + time.perf_counter() - start
				self.calls[name] = self.calls.get(name, 0) + 1

		setattr(module, name, timed)

	def reset(self) -> None:
		self.totals.clear()
		self.calls.clear()


class SqlRecorder:
	def __init__(self) -> None:
		self.statements: list[tuple[float, str]] = []
		self._starts: list[float] = []

	def install(self) -> None:
		event.listen(engine, "before_cursor_execute", self._before)
		event.listen(engine, "after_cursor_execute", self._after)

	def _before(self, conn, cursor, statement, parameters, context, executemany) -> None:
		self._starts.append(time.perf_counter())

	def _after(self, conn, cursor, statement, parameters, context, executemany) -> None:
		elapsed = time.perf_counter() - self._starts.pop()
		self.statements.append((elapsed, " ".join(statement.split())[:160]))

	def reset(self) -> None:
		self.statements.clear()
		self._starts.clear()


def _report(label: str, wall: float, timer: StageTimer, sql: SqlRecorder) -> None:
	sql_total = sum(item[0] for item in sql.statements)
	print(f"\n== {label}: {wall:.3f}s total; SQL {len(sql.statements)} statements, {sql_total:.3f}s")
	for name, seconds in sorted(timer.totals.items(), key=lambda item: -item[1]):
		print(f"   stage {name:<36} {seconds:7.3f}s  x{timer.calls[name]}")
	for seconds, text in sorted(sql.statements, key=lambda item: -item[0])[:5]:
		print(f"   slow SQL {seconds:6.3f}s  {text}")


def _run_function(case_id: int, evidence: bool, timer: StageTimer, sql: SqlRecorder, profile: cProfile.Profile | None):
	timer.reset()
	sql.reset()
	with SessionLocal() as db:
		start = time.perf_counter()
		if profile is not None:
			profile.enable()
		try:
			payload = reader_service.build_case_reader_data(case_id, db, include_evidence=evidence)
		finally:
			if profile is not None:
				profile.disable()
		wall = time.perf_counter() - start
		db.rollback()
	return payload, wall


def _run_route(case_id: int, evidence: bool, timer: StageTimer, sql: SqlRecorder):
	from fastapi.testclient import TestClient

	from backend.main import app

	timer.reset()
	sql.reset()
	client = TestClient(app)
	start = time.perf_counter()
	response = client.get(f"/cases/{case_id}/reader-data", params={"evidence": "1" if evidence else "0"})
	wall = time.perf_counter() - start
	return response, wall


def profile_case(case_id: int, profile_path: Path, timer: StageTimer, sql: SqlRecorder) -> None:
	print(f"\n######## case {case_id}")
	for evidence in (False, True):
		mode = "evidence=on" if evidence else "evidence=off"
		profile = cProfile.Profile()
		payload, wall = _run_function(case_id, evidence, timer, sql, profile)
		_report(f"function {mode} (first run)", wall, timer, sql)
		_, warm = _run_function(case_id, evidence, timer, sql, None)
		_report(f"function {mode} (second run, caches warm)", warm, timer, sql)

		if not evidence:
			stream = io.StringIO()
			pstats.Stats(profile, stream=stream).sort_stats("cumulative").print_stats(15)
			with profile_path.open("a", encoding="utf-8") as handle:
				handle.write(f"\n##### case {case_id} {mode} cProfile top 15 cumulative\n{stream.getvalue()}\n")

			start = time.perf_counter()
			dumped = payload.model_dump(mode="json")
			dump_time = time.perf_counter() - start
			start = time.perf_counter()
			body = json.dumps(dumped)
			json_time = time.perf_counter() - start
			print(f"\n   payload: model_dump {dump_time:.3f}s, json.dumps {json_time:.3f}s, {len(body) / 1_000_000:.2f} MB")
			print(f"   citations in payload: {len(payload.citations)}")

		response, route_wall = _run_route(case_id, evidence, timer, sql)
		_report(
			f"ROUTE via TestClient {mode} (HTTP {response.status_code}, {len(response.content) / 1_000_000:.2f} MB)",
			route_wall,
			timer,
			sql,
		)
	print(f"\ncProfile tables appended to {profile_path}")


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("case_ids", nargs="+", type=int)
	parser.add_argument("--profile-file", default=str(PROJECT_ROOT / "logs" / "profile_reader.txt"))
	args = parser.parse_args()

	timer = StageTimer()
	for name in STAGE_FUNCTIONS:
		timer.wrap(reader_service, name)
	sql = SqlRecorder()
	sql.install()

	profile_path = Path(args.profile_file)
	profile_path.parent.mkdir(parents=True, exist_ok=True)
	for case_id in args.case_ids:
		profile_case(case_id, profile_path, timer, sql)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
