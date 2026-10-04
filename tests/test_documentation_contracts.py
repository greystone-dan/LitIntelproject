import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
API_REFERENCE = ROOT / "docs" / "API_REFERENCE.generated.md"
ARCHITECTURE = ROOT / "docs" / "ARCHITECTURE.md"


def test_readme_routes_exist_in_generated_api_reference():
    readme = README.read_text(encoding="utf-8")
    api_reference = API_REFERENCE.read_text(encoding="utf-8")

    documented_routes = set(
        re.findall(r"`(?:GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+(/[^`\s]+)`", readme)
    )
    documented_routes.update(re.findall(r"`(/[^`\s]+)`", readme))
    generated_routes = set(
        re.findall(
            r"^### `(?:GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+([^`]+)`$",
            api_reference,
            re.MULTILINE,
        )
    )

    assert documented_routes
    assert documented_routes <= generated_routes


def test_architecture_backend_inventory_matches_files_on_disk():
    architecture = ARCHITECTURE.read_text(encoding="utf-8")
    documented_modules = set(
        re.findall(r"^\| `(backend/[^`]+)` \|", architecture, re.MULTILINE)
    )
    backend_files = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "backend").rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }

    assert documented_modules == backend_files
    assert all((ROOT / module).is_file() for module in documented_modules)
