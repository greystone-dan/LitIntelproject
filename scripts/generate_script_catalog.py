"""Generate an operational script catalog from active script modules."""

from __future__ import annotations

import argparse
import ast
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
DEFAULT_OUTPUT = PROJECT_ROOT / "docs" / "SCRIPT_CATALOG.generated.md"


def classify(name: str, text: str) -> tuple[str, str, str]:
	value = f"{name} {text}".lower()
	explicit = {
		"adjudicate_fc_metadata.py": ("Metadata adjudication", "OpenAI and database writer", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"),
		"download_reference_library.py": ("Reference acquisition", "network and filesystem writer", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"),
		"fc_portal_collector.py": ("Federal Court source acquisition", "network and filesystem writer", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"),
		"curate_a2aj_cases.py": ("A2AJ curation and canonical import", "database writer", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"),
		"curate_a2aj_immigration_cases.py": ("A2AJ curation and canonical import", "database writer", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"),
		"extract_a2aj_case_citations_resumable.py": ("Citation extraction maintenance", "database writer", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"),
		"populate_fc_gold_case_ids.py": ("Evaluation artifact maintenance", "filesystem writer", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"),
		"verify_fc_case_existence.py": ("Source verification", "network and filesystem output", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"),
	}
	if name in explicit:
		return explicit[name]
	if name.startswith("generate_"):
		return "Documentation generation", "read-only", f".\\venv\\Scripts\\python.exe scripts\\{name}"
	if name.startswith(("evaluate_", "audit_", "report_", "verify_", "extract_fc_citation_evidence", "cross_reference_", "map_", "build_", "quick_search_")):
		return "Evaluation, audit, or build artifact", "usually read-only/filesystem output", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"
	if name.startswith(("ingest_", "import_", "crawl_", "fetch_")):
		return "Source acquisition or canonical import", "network and/or database writer", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"
	if name.startswith(("chunk_", "embed_", "tag_", "resolve_", "backfill_", "remove_", "extract_citation_", "extract_irpa_", "classify_", "populate_")):
		return "Canonical enrichment or maintenance", "database writer unless dry-run is documented", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"
	if "overnight" in value:
		return "Orchestration", "database/network job runner", f".\\venv\\Scripts\\python.exe scripts\\{name} --list-jobs"
	return "Utility", "inspect implementation before execution", f".\\venv\\Scripts\\python.exe scripts\\{name} --help"


def script_info(path: Path) -> dict[str, str]:
	text = path.read_text(encoding="utf-8")
	tree = ast.parse(text, filename=str(path))
	docstring = ast.get_docstring(tree) or "No module docstring; inspect this script before use."
	category, risk, command = classify(path.name, text)
	return {"name": path.name, "docstring": " ".join(docstring.split()), "category": category, "risk": risk, "command": command}


def render_catalog(items: list[dict[str, str]]) -> str:
	lines = [
		"# Generated Script Catalog",
		"",
		"This file is generated from active `scripts/*.py` modules by "
		"`scripts/generate_script_catalog.py`. Do not edit it manually.",
		"",
		"Run every script from the repository root with the project virtual environment. "
		"For database/network writers, read `--help`, use dry-run/preflight/limit options "
		"where available, and confirm no other bulk PostgreSQL writer is active.",
		"",
		f"Active scripts documented: {len(items)}",
		"",
		"## Catalog",
		"",
		"| Script | Class | Risk | Safe first command |",
		"| --- | --- | --- | --- |",
	]
	for item in items:
		lines.append(f"| `{item['name']}` | {item['category']} | {item['risk']} | `{item['command']}` |")
	for item in items:
		lines.extend([
			"",
			f"## `scripts/{item['name']}`",
			"",
			f"**Purpose:** {item['docstring']}",
			"",
			f"**Operational class:** {item['category']}",
			"",
			f"**Write/network risk:** {item['risk']}",
			"",
			"**Safe first command**",
			"",
			"```powershell",
			item["command"],
			"```",
		])
	return "\n".join(lines).rstrip() + "\n"


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
	args = parser.parse_args()
	items = [script_info(path) for path in sorted(SCRIPTS_DIR.glob("*.py")) if path.name != "__init__.py"]
	output = args.output.resolve()
	output.parent.mkdir(parents=True, exist_ok=True)
	output.write_text(render_catalog(items), encoding="utf-8")
	print(f"generated={output}")


if __name__ == "__main__":
	main()