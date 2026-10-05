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


def _conflicts(a: JudgeName, b: JudgeName) -> bool:
	"""True when two same-surname names cannot be one person (gender clash or different initials)."""
	if a.gender and b.gender and a.gender != b.gender:
		return True
	return bool(a.given and b.given and not _initials_compatible(a, b))


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
	# Duplicate spellings of the same judge (e.g. "THE HONOURABLE MR. JUSTICE SHORE" and
	# "The Honorable Mr. Justice Shore") are not rivals; only a conflicting identity is.
	rivals = [
		p for p in (parse_judge_name(n) for n in other_profile_names)
		if p and p.surname in surnames and all(_conflicts(m, p) for m in mine if m.surname == p.surname)
	]
	matched = []
	for row in rows:
		parsed = parse_judge_name(str(row.get("name") or ""))
		if parsed is None or parsed.surname not in surnames:
			continue
		if not any(p.surname == parsed.surname and _initials_compatible(p, parsed) for p in mine):
			continue
		if any(r.surname == parsed.surname and not _conflicts(r, parsed) for r in rivals) and (
			not parsed.given or not any(p.given and _initials_compatible(p, parsed) for p in mine)
		):
			continue  # another judge with this surname could be the one named: do not guess
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
