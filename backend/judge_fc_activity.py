"""Attach Federal Court docket activity (leave, JR, motions, stays) to a canonical judge profile.

FC Activity keys judges by a surname-style key and name ("S. Noël", "de Montigny"). Rows are matched
to a profile by the normalized surname and compatible initials; when another profile shares the
surname and the row names no given name, the row is left out rather than guessed.
"""

from __future__ import annotations

from typing import Any, Iterable

from .judge_normalization import JudgeName, parse_judge_name

_COUNT_FIELDS = (("leave_decisions", "leave_grant_rate"), ("jr_decisions", "jr_grant_rate"),
	("motion_decisions", "motion_grant_rate"), ("stay_decisions", "stay_grant_rate"))


def _initials_compatible(a: JudgeName, b: JudgeName) -> bool:
	return all(x[0] == y[0] for x, y in zip(a.given, b.given))


def match_fc_rows(
	rows: Iterable[dict[str, Any]],
	profile_names: Iterable[str],
	other_profile_names: Iterable[str] = (),
) -> list[dict[str, Any]]:
	"""Rows from fetch_fc_activity_judges that belong to the person behind `profile_names`."""
	mine = [p for p in (parse_judge_name(n) for n in profile_names) if p]
	if not mine:
		return []
	surnames = {p.surname for p in mine}
	rivals = [p for p in (parse_judge_name(n) for n in other_profile_names) if p and p.surname in surnames]
	matched = []
	for row in rows:
		parsed = parse_judge_name(str(row.get("name") or ""))
		if parsed is None or parsed.surname not in surnames:
			continue
		same = [p for p in mine if p.surname == parsed.surname and _initials_compatible(p, parsed)]
		if not same:
			continue
		if not parsed.given and any(r.surname == parsed.surname for r in rivals):
			continue  # surname-only row, another judge shares the surname: cannot tell who it is
		if parsed.given and any(
			r.surname == parsed.surname and r.given and _initials_compatible(r, parsed) for r in rivals
		) and not any(p.given and _initials_compatible(p, parsed) for p in mine):
			continue
		matched.append(row)
	return matched


def combine_rows(rows: list[dict[str, Any]]) -> dict[str, Any] | None:
	"""Merge matched rows into one summary using counts rebuilt from decisions x rate."""
	if not rows:
		return None
	result: dict[str, Any] = {"names": sorted({str(r["name"]) for r in rows})}
	for count_key, rate_key in _COUNT_FIELDS:
		total = sum(int(r.get(count_key) or 0) for r in rows)
		granted = sum(round(float(r.get(rate_key) or 0) * int(r.get(count_key) or 0)) for r in rows)
		result[count_key] = total
		result[rate_key] = round(granted / total, 4) if total else None
	days = [(int(r["median_days_hearing_to_judgment"]), int(r.get("jr_decisions") or 0)) for r in rows
		if r.get("median_days_hearing_to_judgment") is not None]
	result["median_days_hearing_to_judgment"] = (
		round(sum(d * w for d, w in days) / max(1, sum(w for _, w in days))) if days else None
	)
	return result
