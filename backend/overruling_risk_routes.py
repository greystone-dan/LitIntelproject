"""Read-only API route for seed-based overruling-risk indicators."""

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Case, Citation, get_db
from .overruling_risk import build_overruling_risk_result

router = APIRouter(tags=["overruling-risk"])


@router.get("/api/overruling-risk/{case_id}", response_model=dict[str, Any])
def get_overruling_risk(case_id: int, db: Session = Depends(get_db)) -> dict[str, Any]:
    requested_case = db.scalar(select(Case).where(Case.id == case_id))
    if requested_case is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Case not found",
        )
    resolved_citations = list(
        db.execute(
            select(Citation, Case)
            .join(Case, Citation.target_case_id == Case.id)
            .where(
                Citation.source_case_id == case_id,
                Citation.target_case_id.is_not(None),
                Citation.unresolved.is_(False),
            )
            .order_by(Citation.id)
        )
    )
    return build_overruling_risk_result(requested_case, resolved_citations)
