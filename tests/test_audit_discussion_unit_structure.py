import json

from scripts.audit_discussion_unit_structure import audit_reports


def write_report(path, case_id, paragraph_count, units):
    path.write_text(
        json.dumps(
            {
                "case_id": case_id,
                "paragraph_count": paragraph_count,
                "discussion_units": units,
            }
        ),
        encoding="utf-8",
    )


def test_audit_flags_collapsed_and_oversized_structures(tmp_path):
    write_report(
        tmp_path / "case_126_deterministic.json",
        126,
        24,
        [{"paragraph_count": 24, "subthemes": [{"paragraph_indices": list(range(24))}]}],
    )
    write_report(
        tmp_path / "case_1540_deterministic.json",
        1540,
        20,
        [
            {"paragraph_count": 8, "subthemes": [{"paragraph_indices": list(range(4))}, {"paragraph_indices": list(range(4, 8))}]},
            {"paragraph_count": 12, "subthemes": [{"paragraph_indices": list(range(8, 14))}, {"paragraph_indices": list(range(14, 20))}]},
        ],
    )

    result = audit_reports(tmp_path)

    assert result["case_count"] == 2
    assert result["summary"]["collapsed_top_level_case_count"] == 1
    assert result["summary"]["collapsed_subthemes_case_count"] == 1
    assert result["summary"]["cases_with_oversized_units"] == 1
    assert result["summary"]["cases_with_oversized_subthemes"] == 1
    assert result["cases"][0]["flags"] == [
        "collapsed_top_level",
        "collapsed_subthemes",
        "oversized_unit",
        "oversized_subtheme",
    ]
    assert result["cases"][1]["flags"] == []