# Browser Game

An isolated browser-based game project inside the AI CaseLibrary repository.

## Boundary

This project is independent from the main CaseLibrary application. Keep game code, assets, tests, and dependencies inside this directory. Do not import from `backend/`, connect to the CaseLibrary database, or modify the main application routes.

## Structure

- `src/` game source code
- `assets/` images, audio, fonts, and other game media
- `tests/` game-specific tests
- `tools/` ProjectManagerGAME harness and fail-closed policy
- `.game-manager/` game-local runs, command logs, and task evidence
- `index.html` browser entry point
- `package.json` local game dependencies, when a framework is selected

## ProjectManagerGAME

The dedicated VS Code agent is discovered from the workspace `.github/agents`
folder, but its operating boundary is hard-coded to this directory. It must
use `tools/game_harness.py` for lifecycle commands. The harness rejects shell
syntax, path traversal, disallowed executables, and commands that would leave
the game folder. It does not access the main application, database, Git, or
network services.
