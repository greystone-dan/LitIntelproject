from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import HTMLResponse

from .database import get_db
from .outcome_alerts import compute_alerts_for_search

router = APIRouter()

@router.get("/saved-searches/{search_id}/alerts")
def saved_search_alerts_json(search_id: int, since: Optional[str] = Query(default=None), db=Depends(get_db)):
    # validate since param
    since_dt = None
    if since:
        try:
            since_dt = datetime.fromisoformat(since)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid since parameter")
    try:
        data = compute_alerts_for_search(db, search_id, since=since_dt)
    except ValueError:
        raise HTTPException(status_code=404, detail="Saved search not found")
    return data


@router.get("/saved-searches/{search_id}/alerts-ui", response_class=HTMLResponse)
def saved_search_alerts_ui(search_id: int) -> HTMLResponse:
    from .pages.saved_search_alerts import saved_search_alerts_page_html

    return HTMLResponse(content=saved_search_alerts_page_html(search_id))
