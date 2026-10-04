"""Focused checks for Docker build-context exclusions."""

from pathlib import Path
import unittest


class TestDockerignore(unittest.TestCase):
    def test_env_file_is_excluded(self):
        dockerignore = Path(__file__).resolve().parents[1] / ".dockerignore"
        patterns = {
            line.strip()
            for line in dockerignore.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        }

        self.assertIn(".env", patterns)


if __name__ == "__main__":
    unittest.main()
