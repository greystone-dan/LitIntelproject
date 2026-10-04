from __future__ import annotations

import os
from typing import Dict, Literal

from fastapi import HTTPException, status

PUBLIC_ENV = "CASELIBRARY_PUBLIC_DATA_ONLY"

# Path policy is explicit so new POST routes must be assigned a deployment
# profile rather than silently inheriting the analysis policy.
ANALYSIS_POST_PATHS = frozenset({
    "/ingest",
    "/ingest/merge",
    "/live-analysis/analyze",
    "/live-analysis/resolve",
    "/memo-citation-check",
    "/api/deidentify",
    "/api/reidentify",
    "/api/deidentify/docx",
    "/research",
})

PUBLIC_POST_PATHS = frozenset({
    "/access/login",
    "/access/logout",
    "/citation-metrics/recompute",
    "/a2aj/citation-network/build-map",
    "/a2aj/citation-network/convert",
    "/search",
    "/search/chunks",
    "/search/chunks/paragraphs",
    "/search/chunks/local",
    "/search/chunks/grouped",
    "/saved-searches",
    "/saved-searches/{search_id}/check",
})

PUBLIC_READ_PATHS = frozenset({
    "/health",
    "/api/deployment-profile",
    "/data-explorer",
    "/cases/{case_id}",
    "/statutes",
})

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
                "This operation is disabled in public-data-only mode. "
                "Contact the operator to enable analysis or use a non-public deployment."
            ),
        )


def classify_path(path: str, method: str = "GET") -> PathClassification:
    """Classify a route path and method for public-data-only policy."""
    normalized_method = method.upper()
    if normalized_method == "POST":
        if path in ANALYSIS_POST_PATHS:
            return "analysis"
        if path in PUBLIC_POST_PATHS:
            return "public"
    elif normalized_method == "GET" and path in PUBLIC_READ_PATHS:
        return "public-read"
    return "unclassified"
