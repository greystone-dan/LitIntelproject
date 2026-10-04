from __future__ import annotations

import os
from typing import Dict, Literal

from fastapi import HTTPException, status

PUBLIC_ENV = "CASELIBRARY_PUBLIC_DATA_ONLY"

# New routes must be assigned a deployment profile rather than silently
# inheriting the analysis policy.
ROUTE_PATH_POLICY = {
    ("POST", "/ingest"): "analysis",
    ("POST", "/ingest/merge"): "analysis",
    ("POST", "/live-analysis/analyze"): "analysis",
    ("POST", "/live-analysis/resolve"): "analysis",
    ("POST", "/memo-citation-check"): "analysis",
    ("POST", "/api/deidentify"): "analysis",
    ("POST", "/api/reidentify"): "analysis",
    ("POST", "/api/deidentify/docx"): "analysis",
    ("POST", "/research"): "analysis",
    ("POST", "/access/login"): "public",
    ("POST", "/access/logout"): "public",
    ("POST", "/citation-metrics/recompute"): "public",
    ("POST", "/a2aj/citation-network/build-map"): "public",
    ("POST", "/a2aj/citation-network/convert"): "public",
    ("POST", "/search"): "public",
    ("POST", "/search/chunks"): "public",
    ("POST", "/search/chunks/paragraphs"): "public",
    ("POST", "/search/chunks/local"): "public",
    ("POST", "/search/chunks/grouped"): "public",
    ("POST", "/saved-searches"): "public",
    ("POST", "/saved-searches/{search_id}/check"): "public",
    ("GET", "/health"): "public-read",
    ("GET", "/api/deployment-profile"): "public-read",
    ("GET", "/data-explorer"): "public-read",
    ("GET", "/cases/{case_id}"): "public-read",
    ("GET", "/statutes"): "public-read",
}

ANALYSIS_POST_PATHS = frozenset(
    path for (method, path), profile in ROUTE_PATH_POLICY.items()
    if method == "POST" and profile == "analysis"
)

PathClassification = Literal["analysis", "public", "public-read", "unclassified"]


def is_public_data_only() -> bool:
    value = os.getenv(PUBLIC_ENV, "").strip().lower()
    return value not in ("", "0", "false", "off")


def get_deployment_profile() -> Dict[str, object]:
    return {
        "public_data_only": is_public_data_only(),
        "public_data_only_env": PUBLIC_ENV,
    }


async def require_analysis_allowed() -> None:
    """Dependency to use on analysis POST handlers.
    Raises HTTP 403 when public-data-only mode is enabled.
    """
    if is_public_data_only():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=(
                "Disabled: this deployment is public case law only"
            ),
        )


def classify_path(path: str, method: str = "GET") -> PathClassification:
    """Classify a route path and method for public-data-only policy."""
    normalized_method = method.upper()
    return ROUTE_PATH_POLICY.get((normalized_method, path), "unclassified")
