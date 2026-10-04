# Schedule the offline outcome-alert builder on Windows

This procedure schedules an offline calculation on Daniel's PC. It does not
connect to CaseLibrary or export saved searches; it processes the JSON input
already placed on that PC. Prepare that input through an approved process before
enabling the task. Do not put passwords, database URLs, or other credentials in
the input or Task Scheduler arguments.

1. Confirm that Python can run the checked-out repository's
   `scripts/build_outcome_alerts.py`, and place a prepared input file at
   `C:\data\outcome_alerts_input.json`.
2. In Task Scheduler, create a task with **Start a program**:
   - Program/script: `C:\path\to\python.exe`
   - Add arguments:
     `"C:\path\to\repository\scripts\build_outcome_alerts.py" "C:\data\outcome_alerts_input.json" --output "C:\data\outcome_alerts.json"`
   - Start in: `C:\path\to\repository`
3. Choose the approved trigger (for example, daily at 07:00). Set the task to
   run only when the prepared input is available.
4. Configure Task Scheduler history and review the process exit code. Protect
   the input and output files according to their contents; rotate or archive
   outputs using the local retention policy.

The script is offline and has no database or credential options. Re-running it
with unchanged input recalculates the same snapshot (apart from the default
rolling-window reference time); use `--as-of ISO_DATETIME` when a reproducible
reference time is needed.
