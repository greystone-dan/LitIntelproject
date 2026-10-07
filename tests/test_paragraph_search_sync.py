"""Catch-up sync of paragraph_search: dry run writes nothing, apply is batched, missing table is reported."""

from backend import paragraph_search_sync as sync


class Result:
	def __init__(self, value=0, rowcount=0):
		self.value, self.rowcount = value, rowcount

	def scalar(self):
		return self.value


class SyncDB:
	def __init__(self, table=True, waiting=12, orphans=0):
		self.table, self.waiting, self.orphans = table, waiting, orphans
		self.max_id, self.statements, self.commits = 100, [], 0

	def execute(self, statement, params=None):
		sql = str(statement)
		self.statements.append(sql)
		if "to_regclass" in sql:
			return Result(self.table)
		if "max(chunk_id)" in sql:
			return Result(self.max_id)
		if "INSERT INTO paragraph_search" in sql:
			added = min(params["batch"], self.waiting)
			self.waiting -= added
			self.max_id += added
			return Result(rowcount=added)
		if "id > :after_id" in sql:
			return Result(self.waiting)
		if "NOT EXISTS (SELECT 1 FROM paragraph_search" in sql:
			return Result(0)
		if sql.strip().startswith("SELECT count(*) FROM paragraph_search"):
			return Result(self.orphans)
		if sql.strip().startswith("DELETE"):
			return Result(rowcount=self.orphans)
		return Result(0)

	def commit(self):
		self.commits += 1


def test_missing_table_is_reported_not_created():
	db = SyncDB(table=False)
	assert sync.sync_paragraph_search(db) == {"table_exists": False, "added": 0}
	assert not any("CREATE" in sql for sql in db.statements)


def test_dry_run_counts_and_writes_nothing():
	db = SyncDB(waiting=12)
	report = sync.sync_paragraph_search(db, apply=False)
	assert report["new_paragraphs_waiting"] == 12 and report["added"] == 0
	assert not any("INSERT" in sql or "DELETE" in sql for sql in db.statements) and db.commits == 0


def test_apply_adds_in_committed_batches_and_stops_when_caught_up(monkeypatch):
	monkeypatch.setattr(sync, "BATCH_ROWS", 5)
	db = SyncDB(waiting=12)
	report = sync.sync_paragraph_search(db, pause_seconds=0)
	assert report["added"] == 12 and db.commits == 4  # 5 + 5 + 2, then the empty batch ends the loop


def test_max_rows_caps_the_run(monkeypatch):
	monkeypatch.setattr(sync, "BATCH_ROWS", 5)
	db = SyncDB(waiting=50)
	assert sync.sync_paragraph_search(db, max_rows=7, pause_seconds=0)["added"] == 7


def test_prune_only_when_asked():
	db = SyncDB(waiting=0, orphans=4)
	assert "pruned" not in sync.sync_paragraph_search(db, pause_seconds=0)
	assert sync.sync_paragraph_search(db, prune=True, pause_seconds=0)["pruned"] == 4
