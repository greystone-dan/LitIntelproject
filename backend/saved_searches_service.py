from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import and_, desc, func
from . import database
from . import models
from .search_service import execute_search_cases
from .database import SavedSearch, SearchAlert, FCActivityAlert, CaseChunk


def create_saved_search(
	db: Session,
	name: str,
	description: str | None,
	query: str,
	search_mode: str,
	filters: dict,
) -> SavedSearch:
	saved_search = SavedSearch(
		name=name,
		description=description,
		query=query,
		search_mode=search_mode,
		filters=filters,
		last_alert_check=datetime.now(datetime.now().astimezone().tzinfo),
	)
	db.add(saved_search)
	db.commit()
	db.refresh(saved_search)
	return saved_search


def list_saved_searches(db: Session) -> list[SavedSearch]:
	return db.query(SavedSearch).order_by(desc(SavedSearch.created_at)).all()


def get_saved_search(db: Session, search_id: int) -> SavedSearch | None:
	return db.query(SavedSearch).filter(SavedSearch.id == search_id).first()


def update_saved_search(
	db: Session,
	search_id: int,
	name: str | None = None,
	description: str | None = None,
	query: str | None = None,
	search_mode: str | None = None,
	filters: dict | None = None,
) -> SavedSearch | None:
	saved_search = get_saved_search(db, search_id)
	if not saved_search:
		return None

	if name is not None:
		saved_search.name = name
	if description is not None:
		saved_search.description = description
	if query is not None:
		saved_search.query = query
	if search_mode is not None:
		saved_search.search_mode = search_mode
	if filters is not None:
		saved_search.filters = filters

	saved_search.updated_at = datetime.now(datetime.now().astimezone().tzinfo)
	db.commit()
	db.refresh(saved_search)
	return saved_search


def delete_saved_search(db: Session, search_id: int) -> bool:
	saved_search = get_saved_search(db, search_id)
	if not saved_search:
		return False

	db.delete(saved_search)
	db.commit()
	return True


def find_new_matches(
	db: Session,
	search_id: int,
	since: datetime | None = None,
) -> list:
	saved_search = get_saved_search(db, search_id)
	if not saved_search:
		return []

	if since is None:
		since = saved_search.last_alert_check or datetime.min

	# Construct search request from saved search
	search_req = models.CaseSearchRequest(
		query=saved_search.query,
		search_mode=saved_search.search_mode,
		page=1,
		page_size=100,
		**saved_search.filters,
	)

	# Perform the search
	search_result = execute_search_cases(db, search_req)

	# Filter results created after last check
	new_cases = [
		case
		for case in search_result.results
		if case.scraped_at and case.scraped_at > since
	]

	return new_cases


def record_alert(
	db: Session,
	search_id: int,
	case_id: int,
	chunk_id: int | None,
	match_type: str,
	relevance_score: float | None = None,
) -> SearchAlert:
	alert = SearchAlert(
		search_id=search_id,
		case_id=case_id,
		chunk_id=chunk_id,
		match_type=match_type,
		relevance_score=relevance_score,
	)
	db.add(alert)
	db.commit()
	db.refresh(alert)
	return alert


def get_alerts_since(
	db: Session,
	search_id: int,
	since: datetime,
) -> list[SearchAlert]:
	return (
		db.query(SearchAlert)
		.filter(
			and_(
				SearchAlert.search_id == search_id,
				SearchAlert.discovered_at >= since,
			)
		)
		.order_by(desc(SearchAlert.discovered_at))
		.all()
	)


def get_recent_alerts(
	db: Session,
	search_id: int,
	limit: int = 50,
) -> list[SearchAlert]:
	return (
		db.query(SearchAlert)
		.filter(SearchAlert.search_id == search_id)
		.order_by(desc(SearchAlert.discovered_at))
		.limit(limit)
		.all()
	)


def clear_alerts(db: Session, search_id: int) -> int:
	count = db.query(SearchAlert).filter(
		SearchAlert.search_id == search_id
	).delete()
	db.commit()
	return count


def update_last_check(db: Session, search_id: int) -> SavedSearch | None:
	saved_search = get_saved_search(db, search_id)
	if not saved_search:
		return None

	saved_search.last_alert_check = datetime.now(datetime.now().astimezone().tzinfo)
	db.commit()
	db.refresh(saved_search)
	return saved_search


def record_fc_activity_alert(
	db: Session,
	search_id: int,
	case_id: int,
	entry_type: str,
) -> FCActivityAlert:
	alert = FCActivityAlert(
		search_id=search_id,
		case_id=case_id,
		entry_type=entry_type,
	)
	db.add(alert)
	db.commit()
	db.refresh(alert)
	return alert


def get_fc_activity_alerts(
	db: Session,
	search_id: int,
	since: datetime | None = None,
	limit: int = 50,
) -> list[FCActivityAlert]:
	query = db.query(FCActivityAlert).filter(
		FCActivityAlert.search_id == search_id
	)

	if since:
		query = query.filter(FCActivityAlert.discovered_at >= since)

	return query.order_by(desc(FCActivityAlert.discovered_at)).limit(limit).all()
