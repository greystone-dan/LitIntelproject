"""Additive router; application registration is owned by the integration slice."""

from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException

from .decision_timing import fetch_fc_activity_timing, fetch_judge_timing

router = APIRouter()


def get_timing_db():
    # Lazy dependency keeps importing the router safe for DB-free fixture tests.
    from .database import get_db
    yield from get_db()


@router.get("/api/fc-activity/timing", response_model=dict[str, Any])
def fc_activity_timing(
    db: Annotated[Any, Depends(get_timing_db)],
    city: str = "", year_from: int | None = None, year_to: int | None = None,
    decision_body: str = "", application_type: str = "", representation: str = "",
    language: str = "", office: str = "", resolution: str = "", judge: str = "",
    counsel: str = "",
) -> dict[str, Any]:
    """Recorded hearing-to-judgment days for filtered staged Activity files.

    Median/p25/p75 use linear interpolation and are null when n < 10.
    Tiny year/subject/category labels are omitted; hidden group and timed
    membership counts are disclosed. Missing, invalid/ambiguous and reversed
    endpoints are excluded and counted. Years are filing years. Issue/tag
    groups are stored challenge subjects/categories, not canonical issues or
    V3 tags. Descriptive coverage only, never predictions or rankings.
    """
    if year_from is not None and year_to is not None and year_from > year_to:
        raise HTTPException(status_code=422, detail={"code": "invalid_year_range"})
    return fetch_fc_activity_timing(
        db, city=city, year_from=year_from, year_to=year_to, decision_body=decision_body,
        application_type=application_type, representation=representation, language=language,
        office=office, resolution=resolution, judge=judge, counsel=counsel,
    )


@router.get("/api/judge-profiles/{slug}/timing", response_model=dict[str, Any],
            responses={404: {"description": "Unknown canonical judge slug"}})
def judge_timing(slug: str, db: Annotated[Any, Depends(get_timing_db)]) -> dict[str, Any]:
    """Canonical FC judge versus court hearing-to-judgment days, both n.

    Uses canonical profile links, stored reader hearing date and Case.date;
    never an Activity/docket join. Court baseline includes this judge.
    Statistics are null for n < 10; each cohort discloses date exclusions.
    Timing is independent of repeated profile Minister filters and describes
    recorded coverage, not judicial speed rankings or predictions.
    """
    result = fetch_judge_timing(db, slug)
    if result["status"] == "unknown_judge":
        raise HTTPException(status_code=404, detail={"code": "unknown_judge"})
    return result
