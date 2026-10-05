import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "government-readiness"
PATH_PATTERN = re.compile(
    r"(?<![\w])((?:\.\.?/)?(?:[\w.-]+/)+[\w.-]+\."
    r"(?:md|py|ps1|yml|yaml|json|html|toml)"
    r"(?::\d+(?:[-–]\d+)?)?)(?![\w])",
    re.IGNORECASE,
)
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CODE_PATTERN = re.compile(r"`([^`]+)`")


def test_government_readiness_file_references_exist():
    referenced_files = set()
    for document in DOCS.glob("*.md"):
        contents = document.read_text(encoding="utf-8")
        for destination in LINK_PATTERN.findall(contents):
            target = destination.split("#", 1)[0].strip()
            if target and not re.match(r"^[a-z][a-z0-9+.-]*://", target, re.IGNORECASE):
                referenced_files.add((document.parent / target).resolve())
        for code in CODE_PATTERN.findall(contents):
            for match in PATH_PATTERN.finditer(code):
                path = re.sub(r":\d+(?:[-–]\d+)?$", "", match.group(1))
                if path.startswith("../"):
                    continue
                referenced_files.add((ROOT / path).resolve())

    assert referenced_files
    missing = sorted(
        path.relative_to(ROOT).as_posix()
        if path.is_relative_to(ROOT)
        else str(path)
        for path in referenced_files
        if not path.is_file()
    )
    assert not missing, f"Government-readiness docs reference missing files: {missing}"
