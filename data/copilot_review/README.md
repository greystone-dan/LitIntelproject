# Copilot Review Handoffs

This folder is a file-based handoff queue for bounded external Copilot reviews.

## Protocol

1. Each task gets a unique numbered subfolder.
2. `REQUEST.md` defines the review question and constraints.
3. `SOURCES.md` identifies the read-only inputs.
4. The external reviewer writes only `RESPONSE.md`.
5. `STATUS.md` moves from `READY` to `IN_PROGRESS` to `RESPONSE_READY`.
6. The local agent validates the response and may add `ASSESSMENT.md`.

Do not edit source evaluation packets from a review folder. Do not place secrets,
production data, or database credentials here.
