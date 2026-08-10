# Legacy Code Staging Area

This folder contains modules moved out of the active runtime path while the project is focused on the master-300 stabilization phase.

Rules during focus mode:
- Do not import modules from this folder in active endpoints.
- Keep legacy code for reference, not execution.
- Re-enable only with an explicit migration plan and tests.
