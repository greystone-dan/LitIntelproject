from types import SimpleNamespace

from backend.reader_service import _build_reader_inferred_tags


def test_reader_inferred_tags_preserve_repeated_matches():
    case = SimpleNamespace(
        full_text="The ID reviewed the matter. " + ("Background evidence. " * 12) + "The ID issued reasons.",
        summary=None,
    )

    tags = _build_reader_inferred_tags(case, [])
    id_tags = [tag for tag in tags if tag.category == "forum" and tag.value == "id"]

    assert len(id_tags) == 2
    assert len({tag.evidence for tag in id_tags}) == 2
