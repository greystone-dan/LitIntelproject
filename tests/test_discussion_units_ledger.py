from pathlib import Path

from scripts.discussion_units_ledger import get_case, record_case, should_skip


def test_completed_case_is_skipped_and_failed_case_requires_explicit_retry(tmp_path: Path):
	ledger = tmp_path / "ledger.json"
	record_case(ledger, 7, "complete", output_markdown="case-7.md")
	assert should_skip(ledger, 7)

	record_case(ledger, 8, "failed", error="malformed")
	assert should_skip(ledger, 8)
	assert not should_skip(ledger, 8, retry_failed=True)
	assert get_case(ledger, 8)["error"] == "malformed"