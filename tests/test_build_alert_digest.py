import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts import build_alert_digest


class DigestCLITests(unittest.TestCase):
	def payload(self):
		return {"saved_searches": [{"id": 1, "name": "FC", "last_alert_check": "2026-10-01"}], "matches": [{
			"search_id": 1, "case_id": 9, "citation": "2026 FC 9", "court": "FC",
			"date": "2026-10-01", "decision_outcome": "granted", "minister": "Immigration",
			"government_outcome": "lost", "discovered_at": "2026-10-02T00:00:00Z",
		}]}

	def test_stdin_formats_and_since(self):
		for fmt, marker in (("html", "<!doctype html>"), ("text", "2026 FC 9"), ("json", '"minister_loss": true')):
			with patch("sys.stdin", io.StringIO(json.dumps(self.payload()))), redirect_stdout(io.StringIO()) as output:
				self.assertEqual(build_alert_digest.main(["--format", fmt]), 0)
				self.assertIn(marker, output.getvalue())
		with patch("sys.stdin", io.StringIO(json.dumps(self.payload()))), redirect_stdout(io.StringIO()) as output:
			build_alert_digest.main(["--format", "json", "--since", "2026-10-03"])
			self.assertEqual(json.loads(output.getvalue())["total_new_decisions"], 0)

	def test_offline_subprocess_input_and_output(self):
		with tempfile.TemporaryDirectory() as directory:
			source, target = Path(directory) / "input.json", Path(directory) / "digest.html"
			source.write_text(json.dumps(self.payload()), encoding="utf-8")
			# Fail if the CLI imports any DB, settings, dotenv, or network module.
			code = (
				"import sys,runpy; "
				"blocked={'backend.database','dotenv','requests','httpx','sqlalchemy','socket'}; "
				"sys.addaudithook(lambda event,args: (_ for _ in ()).throw(RuntimeError('Forbidden import')) "
				"if event=='import' and args[0] in blocked else None); "
				"runpy.run_path('scripts/build_alert_digest.py',run_name='__main__')"
			)
			result = subprocess.run([
				sys.executable, "-c", code, "--input", str(source), "--out", str(target),
				"--since", "2026-10-01", "--format", "html",
			], capture_output=True, text=True)
			self.assertEqual(result.returncode, 0, result.stderr)
			self.assertEqual(result.stdout, "")
			self.assertIn("Minister loss", target.read_text(encoding="utf-8"))

	def test_invalid_input_and_timestamp_fail_cleanly(self):
		null_timestamp = self.payload()
		null_timestamp["matches"][0]["discovered_at"] = None
		for data, args in (
			("{}", []), ("not json", []),
			(json.dumps(self.payload()), ["--since", "bad"]),
			(json.dumps(null_timestamp), []),
		):
			with patch("sys.stdin", io.StringIO(data)), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
				build_alert_digest.main(args)
			self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
	unittest.main()
