import re
import subprocess
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


def test_architecture_backend_inventory_matches_tracked_files():
    architecture = ARCHITECTURE.read_text(encoding="utf-8")
    inventory_rows = re.findall(
        r"^\| `(backend/[^`]+)` \|", architecture, re.MULTILINE
    )
    documented_modules = set(inventory_rows)
    tracked = subprocess.run(
        ["git", "ls-files", "-z", "--", "backend/"],
        cwd=ROOT, check=True, capture_output=True, text=True, timeout=10,
    )
    # Unmerged index stages can repeat a path; inventory paths still occur once.
    backend_files = set(tracked.stdout.split("\0")) - {""}

    assert backend_files, "No tracked backend files found"
    assert len(inventory_rows) == len(documented_modules), "Duplicate inventory rows"
    assert documented_modules == backend_files, (
        f"Missing: {sorted(backend_files - documented_modules)}; "
        f"Untracked inventory paths: {sorted(documented_modules - backend_files)}"
    )
    assert all((ROOT / module).is_file() for module in documented_modules)
