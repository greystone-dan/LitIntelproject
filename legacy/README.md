# Legacy System Area

This folder is the archive zone for non-primary workflows, deprecated UI surfaces, and historical artifacts.

Active work should default to the Citation Pass workflow documented in README.md.

What belongs here:
- Historical artifacts and one-off exports that are not required for runtime
- Deprecated or superseded UI/workbench modules
- Notes that document prior workflow states

Current references:
- Runtime legacy modules: backend/legacy/
- Historical implementation notes: docs/history/
- Archived artifact files: legacy/artifacts/

Rules:
- Do not import from legacy paths in new runtime code unless explicitly reactivated.
- Keep active docs in root docs and keep this folder as reference/archive.
