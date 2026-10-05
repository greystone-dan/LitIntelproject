"""Read-side helpers for the reversible judge alias layer.

`judge_profile_aliases` points duplicate profiles at a canonical profile. Nothing is
rewritten: with no alias rows every helper is a no-op, and deleting rows undoes a merge.
Requires alembic migration 0040 (deploy runs migrations before restarting the site).
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import JudgeProfileAlias


def alias_map(db: Session) -> dict[int, int]:
	"""alias profile id -> canonical profile id."""
	return {a: c for a, c in db.execute(select(JudgeProfileAlias.alias_profile_id, JudgeProfileAlias.canonical_profile_id))}


def member_ids(db: Session, profile_id: int) -> list[int]:
	"""The profile itself plus every profile aliased to it (resolves an alias to its canonical first)."""
	mapping = alias_map(db)
	canonical = mapping.get(profile_id, profile_id)
	return [canonical, *sorted(a for a, c in mapping.items() if c == canonical)]
