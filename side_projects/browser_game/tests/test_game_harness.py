import unittest
from pathlib import Path

from tools.game_policy import GAME_ROOT, validate_command, validate_write


class GamePolicyTests(unittest.TestCase):
    def test_allowed_local_command(self):
        self.assertEqual(validate_command(["python", "-m", "compileall", "tools"])[0], "python")

    def test_rejects_disallowed_executable(self):
        with self.assertRaises(PermissionError):
            validate_command(["powershell", "-Command", "Get-Date"])
        with self.assertRaises(PermissionError):
            validate_command(["npm", "install"])

    def test_rejects_shell_syntax(self):
        with self.assertRaises(PermissionError):
            validate_command(["python", "-c", "print(1); print(2)"])

    def test_rejects_path_escape(self):
        with self.assertRaises(PermissionError):
            validate_write(Path("..") / "backend")

    def test_game_root_is_the_policy_boundary(self):
        self.assertTrue(GAME_ROOT.name == "browser_game")


if __name__ == "__main__":
    unittest.main()
