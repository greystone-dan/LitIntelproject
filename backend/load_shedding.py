"""Opt-in concurrency limits for resource-intensive request families."""

from __future__ import annotations

import asyncio
import math
import os
from dataclasses import dataclass, field
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

# Longest, more-specific prefixes come first; an explicit None keeps light
# request families unlimited while allowing route-classification tests to guard them.
ROUTE_BUCKET_PREFIXES: tuple[tuple[tuple[str, ...] | None, str, str | None], ...] = (
	(("POST",), "/live-analysis/analyze", "live_analysis"),
	(("POST",), "/live-analysis/resolve", "live_analysis"),
	(("POST",), "/memo-citation-check", "live_analysis"),
	(("POST",), "/api/deidentify/docx", "live_analysis"),
	(("POST",), "/api/deidentify", "live_analysis"),
	(("POST",), "/api/reidentify", "live_analysis"),
	(("POST",), "/cases/{case_id}/markup-export", "exports"),
	(("GET",), "/search/export.csv", "exports"),
	(("GET",), "/search/export.docx", "exports"),
	(None, "/api/citation-intelligence", "citation_map"),
	(None, "/citation-intelligence/search", "citation_map"),
	(None, "/citation-intelligence/cases", "citation_map"),
	(None, "/citation-map", "citation_map"),
	(None, "/api/fc-activity", "analytics"),
	(None, "/api/judge-profiles", "analytics"),
	(None, "/api/fc-history", "analytics"),
	(None, "/fc-history", "analytics"),
	(None, "/analytics", "analytics"),
	(None, "/judges", "analytics"),
	(("POST",), "/search/chunks", "bulk_search"),
	(("POST",), "/research", "bulk_search"),
	(("POST",), "/precedent-finder", "bulk_search"),
	(("GET",), "/discussion-units-sandbox/search", None),
	(("GET",), "/prototype/cases", None),
	(("GET",), "/search/tags/similar", None),
	(("POST",), "/saved-searches", None),
	(("PUT",), "/saved-searches", None),
	(("POST",), "/ingest", None),
	(("POST",), "/search", None),
)

BUCKET_NAMES = ("live_analysis", "exports", "citation_map", "analytics", "bulk_search")
BUSY_MESSAGE = "This service is busy handling similar requests. Please retry shortly."


def classify_route(path: str, method: str) -> tuple[bool, str | None]:
	"""Return whether a route is explicitly classified and its optional bucket."""
	method = method.upper()
	segments = path.strip("/").split("/") if path != "/" else []
	for methods, prefix, bucket in ROUTE_BUCKET_PREFIXES:
		if methods is not None and method not in methods:
			continue
		prefix_segments = prefix.strip("/").split("/")
		if len(segments) < len(prefix_segments):
			continue
		if all(
			segment.startswith("{") and segment.endswith("}") or segment == actual
			for segment, actual in zip(prefix_segments, segments)
		):
			return True, bucket
	return False, None


def _positive_int(name: str, default: int | None) -> int | None:
	raw = os.getenv(name)
	if raw is None:
		return default
	try:
		value = int(raw)
	except ValueError as exc:
		raise ValueError(f"{name} must be a positive integer") from exc
	if value <= 0:
		raise ValueError(f"{name} must be a positive integer")
	return value


def _queue_seconds() -> float:
	raw = os.getenv("HEAVY_ENDPOINT_QUEUE_SECONDS", "0")
	try:
		value = float(raw)
	except ValueError as exc:
		raise ValueError("HEAVY_ENDPOINT_QUEUE_SECONDS must be non-negative") from exc
	if value < 0 or not math.isfinite(value):
		raise ValueError("HEAVY_ENDPOINT_QUEUE_SECONDS must be non-negative")
	return value


@dataclass
class _Bucket:
	maximum: int
	semaphore: asyncio.Semaphore = field(init=False)
	active: int = 0
	waiting: int = 0

	def __post_init__(self) -> None:
		self.semaphore = asyncio.Semaphore(self.maximum)


class LoadSheddingState:
	def __init__(self) -> None:
		maximum = _positive_int("HEAVY_ENDPOINT_MAX_CONCURRENCY", None)
		self.enabled = maximum is not None
		self.queue_seconds = _queue_seconds()
		self.buckets: dict[str, _Bucket] = {}
		if maximum is not None:
			for name in BUCKET_NAMES:
				bucket_maximum = _positive_int(
					f"HEAVY_BUCKET_{name.upper()}_MAX", maximum
				)
				self.buckets[name] = _Bucket(bucket_maximum)

	def snapshot(self) -> dict[str, Any]:
		return {
			"enabled": self.enabled,
			"queue_seconds": self.queue_seconds,
			"buckets": {
				name: {
					"active": self.buckets[name].active if name in self.buckets else 0,
					"max_concurrency": (
						self.buckets[name].maximum if name in self.buckets else None
					),
					"waiting": self.buckets[name].waiting if name in self.buckets else 0,
				}
				for name in BUCKET_NAMES
			},
		}


class HeavyEndpointMiddleware:
	def __init__(self, app: Any, *, state: LoadSheddingState) -> None:
		self.app = app
		self.state = state

	async def __call__(self, scope: dict[str, Any], receive: Any, send: Any) -> None:
		if scope["type"] != "http" or not self.state.enabled:
			await self.app(scope, receive, send)
			return

		classified, bucket_name = classify_route(
			scope.get("path", "/"), scope.get("method", "GET")
		)
		bucket = self.state.buckets.get(bucket_name) if classified and bucket_name else None
		if bucket is None:
			await self.app(scope, receive, send)
			return

		semaphore = bucket.semaphore
		if semaphore.locked():
			if self.state.queue_seconds == 0:
				await self._busy(scope, send)
				return
			bucket.waiting += 1
			try:
				await asyncio.wait_for(
					semaphore.acquire(), timeout=self.state.queue_seconds
				)
			except TimeoutError:
				await self._busy(scope, send)
				return
			finally:
				bucket.waiting -= 1
		else:
			await semaphore.acquire()

		bucket.active += 1
		try:
			await self.app(scope, receive, send)
		finally:
			bucket.active -= 1
			semaphore.release()

	async def _busy(self, scope: dict[str, Any], send: Any) -> None:
		retry_after = max(1, math.ceil(self.state.queue_seconds))
		response = PlainTextResponse(
			BUSY_MESSAGE, status_code=503, headers={"Retry-After": str(retry_after)}
		)
		await response(scope, None, send)


async def health_limits(request: Request) -> JSONResponse:
	if os.getenv("CASELIBRARY_DEBUG_ENDPOINTS") != "1":
		return JSONResponse({"detail": "Not Found"}, status_code=404)
	state: LoadSheddingState = request.app.state.heavy_endpoint_limits
	return JSONResponse(state.snapshot())


def register(app: FastAPI) -> None:
	state = LoadSheddingState()
	app.state.heavy_endpoint_limits = state
	app.add_middleware(HeavyEndpointMiddleware, state=state)
	app.add_api_route("/health/limits", health_limits, methods=["GET"])
