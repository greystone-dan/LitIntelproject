"""Pure, offline saved-search digest construction and rendering."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from datetime import date, datetime, timezone
from html import escape
from typing import Any


def parse_timestamp(value: str | datetime) -> datetime:
	"""Normalize ISO timestamps to UTC; naive timestamps are treated as UTC."""
	if not isinstance(value, (str, datetime)):
		raise ValueError("Discovery/cutoff timestamp must be an ISO string or datetime")
	stamp = value if isinstance(value, datetime) else datetime.fromisoformat(value.replace("Z", "+00:00"))
	return stamp.replace(tzinfo=timezone.utc) if stamp.tzinfo is None else stamp.astimezone(timezone.utc)


def _iso(value: Any) -> Any:
	return value.isoformat() if isinstance(value, (date, datetime)) else value


def partition_matches(
	searches: Iterable[Mapping[str, Any]],
	matches: Iterable[Mapping[str, Any]],
	*,
	since: str | datetime | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
	"""Partition recorded alerts at --since or each search's last check.

	An alert exactly on the cutoff belongs to the earlier cohort. Never-checked
	searches treat all their recorded alerts as new. Missing discovery times are
	rejected rather than silently distorting the comparison.
	"""
	cutoffs = {
		search["id"]: (parse_timestamp(since or search["last_alert_check"])
			if since or search.get("last_alert_check") else None)
		for search in searches
	}
	new, earlier = [], []
	for match in matches:
		if match["search_id"] not in cutoffs:
			continue
		stamp = parse_timestamp(match["discovered_at"])
		cutoff = cutoffs[match["search_id"]]
		(new if cutoff is None or stamp > cutoff else earlier).append(dict(match))
	return new, earlier


def _decisions(matches: Iterable[Mapping[str, Any]], search_id: Any) -> list[dict[str, Any]]:
	# Several chunks/alerts can refer to one judgment; count decisions, not alerts.
	unique = {}
	for match in matches:
		if match["search_id"] != search_id:
			continue
		case_id = match["case_id"]
		if case_id in unique:
			continue
		minister = match.get("minister")
		loss = bool(minister) and match.get("government_outcome") == "lost"
		unique[case_id] = {
			"case_id": case_id,
			"title": match.get("title") or match.get("case_title"),
			"citation": match.get("citation") or match.get("case_citation"),
			"court": match.get("court"),
			"date": _iso(match.get("date") or match.get("case_date")),
			"outcome": match.get("decision_outcome"),
			"government_outcome": match.get("government_outcome"),
			"minister": minister,
			"minister_loss": loss,
			"discovered_at": _iso(match.get("discovered_at")),
		}
	return [unique[key] for key in sorted(unique)]


def _counts(decisions: list[dict[str, Any]]) -> dict[str, Any]:
	total = len(decisions)
	losses = sum(row["minister_loss"] for row in decisions)
	return {"decisions": total, "minister_losses": losses, "loss_share": losses / total if total else None}


def build_alert_digest(
	saved_searches: Iterable[Mapping[str, Any]],
	new_matches: Iterable[Mapping[str, Any]],
	earlier_matches: Iterable[Mapping[str, Any]],
) -> dict[str, Any]:
	"""Build JSON-compatible data without IO, clocks, mutation or dependencies.

	Inputs are enriched records, not ORM objects. Minister-loss flags require a
	named Minister and the existing explicit government outcome ``lost``.
	Unknown outcomes stay in the decision denominator; this is a descriptive
	research signal, not a statistical significance or legal conclusion.
	"""
	new_matches, earlier_matches = list(new_matches), list(earlier_matches)
	groups = []
	for search in saved_searches:
		new = _decisions(new_matches, search["id"])
		earlier = _decisions(earlier_matches, search["id"])
		# A decision already present earlier cannot be new because another chunk
		# matched later.
		earlier_ids = {row["case_id"] for row in earlier}
		new = [row for row in new if row["case_id"] not in earlier_ids]
		n, e = _counts(new), _counts(earlier)
		nt, et = n["decisions"], e["decisions"]
		# Integer comparison avoids floating-point errors at exactly +0.20.
		shift = nt >= 5 and et >= 5 and (
			5 * (n["minister_losses"] * et - e["minister_losses"] * nt) >= nt * et
		)
		groups.append({
			"search_id": search["id"],
			"search_name": search["name"],
			"last_alert_check": _iso(search.get("last_alert_check")),
			"new_matches": new,
			"earlier_matches": earlier,
			"new_counts": n,
			"earlier_counts": e,
			"possible_shift": shift,
		})
	return {"searches": groups, "total_new_decisions": sum(group["new_counts"]["decisions"] for group in groups)}


def _count_label(counts: Mapping[str, Any]) -> str:
	total, losses = counts["decisions"], counts["minister_losses"]
	share = f"{losses / total:.0%}" if total else "n/a"
	return f"{losses}/{total} Minister losses ({share}); {total} decisions"


def _decision_label(row: Mapping[str, Any]) -> str:
	return " | ".join(str(value) for value in (
		row["citation"] or "Citation unknown",
		row["title"] or f"Case {row['case_id']}",
		row["court"] or "Court unknown",
		row["date"] or "Date unknown",
		row["outcome"] or "Outcome unknown",
		"Minister loss" if row["minister_loss"] else "Minister loss not established",
	))


def render_digest_text(digest: Mapping[str, Any]) -> str:
	lines = ["Saved-search alert digest", ""]
	if not digest["searches"]:
		lines.append("No saved searches.")
	for group in digest["searches"]:
		lines.extend([
			group["search_name"],
			f"New: {_count_label(group['new_counts'])}",
			f"Earlier: {_count_label(group['earlier_counts'])}",
		])
		if group["possible_shift"]:
			lines.append("Possible shift: Minister-loss share increased by at least 20 percentage points.")
		lines.extend(f"- {_decision_label(row)}" for row in group["new_matches"])
		if not group["new_matches"]:
			lines.append("No new decisions.")
		lines.append("")
	lines.append("Descriptive signal only; unknown outcomes remain in counts. Verify against authoritative decisions.")
	return "\n".join(lines) + "\n"


def render_digest_html(digest: Mapping[str, Any]) -> str:
	"""Self-contained HTML; all styling is inline and record text is escaped."""
	parts = ['<!doctype html><html lang="en"><head><meta charset="utf-8">'
		'<meta name="viewport" content="width=device-width,initial-scale=1">'
		'<title>Saved-search alert digest</title></head>'
		'<body style="margin:0;padding:24px;background:#f5f7fb;color:#102038;font:15px/1.5 Arial,sans-serif">'
		'<main style="max-width:960px;margin:auto"><h1>Saved-search alert digest</h1>']
	if not digest["searches"]:
		parts.append("<p>No saved searches.</p>")
	for group in digest["searches"]:
		parts.append('<section style="margin:16px 0;padding:16px;background:white;border:1px solid #d8dee8">')
		parts.append(f"<h2>{escape(str(group['search_name']))}</h2>")
		for key, label in (("new_counts", "New"), ("earlier_counts", "Earlier")):
			parts.append(f"<p>{label}: {escape(_count_label(group[key]))}</p>")
		if group["possible_shift"]:
			parts.append('<p style="font-weight:bold;color:#92400e">Possible shift: Minister-loss share increased by at least 20 percentage points.</p>')
		parts.append("<ul>")
		parts.extend(f"<li>{escape(_decision_label(row))}</li>" for row in group["new_matches"])
		parts.append("</ul>" if group["new_matches"] else "</ul><p>No new decisions.</p>")
		parts.append("</section>")
	parts.append("<p>Descriptive signal only; unknown outcomes remain in counts. Verify against authoritative decisions.</p></main></body></html>")
	return "".join(parts)
