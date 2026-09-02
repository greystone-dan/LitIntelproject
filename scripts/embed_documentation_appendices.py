"""Embed linked documentation appendices into the canonical system reference."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MASTER_PATH = PROJECT_ROOT / "SYSTEM_REFERENCE.md"
APPENDIX_FILES = (
    "WORK_HISTORY.md",
    "docs/API_REFERENCE.generated.md",
    "docs/SCHEMA_REFERENCE.generated.md",
    "docs/CONFIGURATION_REFERENCE.md",
    "docs/DATA_SOURCE_REGISTER.md",
    "docs/SCRIPT_CATALOG.generated.md",
    "docs/OPERATIONAL_RECOVERY_GUIDE.md",
    "docs/RESEARCH_UI_GUIDE.md",
    "docs/METRICS_DICTIONARY.md",
    "docs/TESTING_MATRIX.md",
    "docs/CHANGE_MANAGEMENT.md",
)
EMBEDDED_START = "## Embedded Appendices"


def embedded_document(text: str, relative_path: str) -> str:
    """Make one source document fit beneath the master document."""
    lines = text.rstrip().splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            lines[index] = f"### Appendix: {title}"
            break
    return "\n".join(
        [
            f"### Appendix Source: `{relative_path}`",
            "",
            "*The text below is synchronized from the companion file. Update the source file or its generator, then rerun `scripts/embed_documentation_appendices.py`.*",
            "",
            *lines,
        ]
    )


def build_master(master_text: str) -> str:
    """Replace the generated appendix section and return the complete master."""
    base = master_text.split(EMBEDDED_START, 1)[0].rstrip()
    sections = [
        EMBEDDED_START,
        "",
        "This section makes this file self-contained. The companion files remain the maintainable sources, and generated appendices must still be regenerated from their owning code before embedding.",
        "",
    ]
    for relative_path in APPENDIX_FILES:
        source_path = PROJECT_ROOT / relative_path
        if not source_path.is_file():
            raise FileNotFoundError(f"Missing appendix source: {relative_path}")
        sections.extend([embedded_document(source_path.read_text(encoding="utf-8"), relative_path), ""])
    return f"{base}\n\n{chr(10).join(sections).rstrip()}\n"


def main() -> None:
    MASTER_PATH.write_text(
        build_master(MASTER_PATH.read_text(encoding="utf-8")),
        encoding="utf-8",
        newline="\n",
    )
    print(f"Embedded {len(APPENDIX_FILES)} appendices into {MASTER_PATH.name}")


if __name__ == "__main__":
    main()