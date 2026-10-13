"""The single inventory of future features and tabs.

``feature_inventory.json`` adds, for every item in ``coming_soon_content.SECTIONS``, the workflow it belongs to, when
it is proposed to go live (now / next / later), whether it needs AI, who it helps, a one-line purpose and a link to its
evidence card. The Coming soon preview and the Lab status board both read it, so they cannot disagree.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

INVENTORY_FILE = Path(__file__).resolve().parent / "feature_inventory.json"


@lru_cache(maxsize=1)
def inventory() -> dict:
    return json.loads(INVENTORY_FILE.read_text(encoding="utf-8"))


def meta(slug: str) -> dict:
    return inventory()["items"].get(slug, {})


def label_of(kind: str, key: str) -> str:
    """Label for a workflow, horizon or ai key."""
    return next((entry["label"] for entry in inventory()[kind] if entry["key"] == key), key)
