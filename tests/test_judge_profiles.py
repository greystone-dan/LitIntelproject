from types import SimpleNamespace
from datetime import date

from scripts.backfill_judge_profiles import is_profileable_judge, judge_slug, normalize_judge_name
from scripts.judge_reconciliation_report import build_report


def test_normalize_judge_name_removes_titles_and_accents():
	assert normalize_judge_name("The Honourable Justice Rene Cote") == "rene cote"
	assert judge_slug("rene cote") == "judge-rene-cote"


def test_rejects_malformed_oversized_judge_extraction():
	assert is_profileable_judge("Justice Smith") is True
	assert is_profileable_judge("Judge " + "x" * 300) is False


def test_rejects_location_and_document_labels():
	assert is_profileable_judge("Ottawa Ontario") is False
	assert is_profileable_judge("Ottawa, Ontario") is False
	assert is_profileable_judge("O T T A W A, Ontario") is False
	assert is_profileable_judge("Certified true translation") is False
	assert is_profileable_judge("FEDERAL COURT OF CANADA") is False
	assert is_profileable_judge("Ontario") is False
	assert is_profileable_judge("Quebec") is False


def test_reconciliation_report_separates_invalid_and_unlinked_judges():
	valid = SimpleNamespace(
		id=1,
		title="Valid v. Canada",
		citation="2020 FC 1",
		source_name="Federal Court",
		source_type="judgment",
		metadata_json={"reader_extracted": {"judge": "Justice Smith"}},
	)
	invalid = SimpleNamespace(
		id=2,
		title="Invalid v. Canada",
		citation="2020 FC 2",
		source_name="Federal Court",
		source_type="judgment",
		metadata_json={"reader_extracted": {"judge": "Ottawa Ontario"}},
	)
	linked_missing = SimpleNamespace(
		id=3,
		title="Missing v. Canada",
		citation="2020 FC 3",
		source_name="Federal Court",
		source_type="judgment",
		metadata_json={"reader_extracted": {}},
	)
	profile = SimpleNamespace(id=1, normalized_name="smith", display_name="Justice Smith")
	links = [
		SimpleNamespace(id=1, case_id=3, judge_profile_id=1, raw_name="Justice Smith"),
	]

	report = build_report([valid, invalid, linked_missing], links, [profile], sample_limit=2)

	assert report["read_only"] is True
	assert report["counts"]["total_cases"] == 3
	assert report["counts"]["cases_with_profileable_raw_judge"] == 1
	assert report["counts"]["cases_with_invalid_raw_judge"] == 1
	assert report["counts"]["cases_with_valid_raw_judge_without_profile_link"] == 1
	assert report["counts"]["linked_cases_without_valid_raw_judge"] == 1
	assert report["invalid_raw_judge_kinds"] == {"junk_pattern": 1}


def test_reconciliation_report_supports_post_2005_date_scope():
	old = SimpleNamespace(
		id=4,
		title="Old v. Canada",
		citation="2005 FC 1",
		date=date(2005, 12, 31),
		source_name="Federal Court",
		source_type="judgment",
		full_text="Old source",
		metadata_json={"reader_extracted": {"judge": "Justice Old"}},
	)
	new = SimpleNamespace(
		id=5,
		title="New v. Canada",
		citation="2006 FC 1",
		date=date(2006, 1, 1),
		source_name="Federal Court",
		source_type="judgment",
		full_text="New source",
		metadata_json={"reader_extracted": {"judge": "Justice New"}, "_field_confidence": {"judge": 0.94}},
	)

	report = build_report([], [], [], min_date=date(2006, 1, 1), sample_limit=2)
	assert report["counts"]["total_cases"] == 0

	report = build_report([old, new], [], [], min_date=date(2006, 1, 1), sample_limit=2)
	assert report["counts"]["total_cases"] == 1
	assert report["counts"]["cases_with_profileable_raw_judge"] == 1
	assert report["confidence_bins_for_profileable_judges"] == {"0.92-0.98": 1}


def test_reconciliation_report_can_compare_fresh_extraction(monkeypatch):
	case = SimpleNamespace(
		id=6,
		title="Fresh v. Canada",
		citation="2006 FC 2",
		date=date(2006, 1, 2),
		source_name="Federal Court",
		source_type="judgment",
		full_text="source",
		metadata_json={"reader_extracted": {"judge": "Justice Stored"}},
	)

	monkeypatch.setattr(
		"scripts.judge_reconciliation_report._fresh_judge_evidence",
		lambda _case: ("Justice Fresh", {"_field_confidence": {"judge": 0.94}}),
	)
	report = build_report([case], [], [], min_date=date(2006, 1, 1), fresh_extraction=True)

	assert report["fresh_extraction"]["counts"] == {"profileable": 1}
	assert report["fresh_extraction"]["cases_different_from_stored_judge"] == 1