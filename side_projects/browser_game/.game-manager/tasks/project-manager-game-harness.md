# ProjectManagerGAME harness

Status: complete

Task: Create a separate manager harness and VS Code agent for the isolated browser game.
Why now: The game needs independent workflow state and hard execution boundaries before implementation begins.
Owner surface: `side_projects/browser_game/`.
Dependencies: Python standard library and the workspace custom-agent discovery path.
Risk boundary: The harness must not read, write, execute, or persist state outside the browser-game folder; it must not touch the main app, database, Git, network, or V2 extraction.
Smallest falsifiable check: A local harness run succeeds for an allowed command and rejects an outside path, shell syntax, and disallowed executable.
Acceptance criteria: Separate game harness, fail-closed policy, dedicated `ProjectManagerGAME` agent, local run state, and local task evidence.
Docs/generated references: `side_projects/browser_game/README.md`, `side_projects/browser_game/.game-manager/tasks/project-manager-game-harness.md`.
Rollback/recovery: Delete the new game-local `.game-manager/` and `tools/` files plus `.github/agents/project-manager-game.agent.md`; no main runtime data is changed.
Evidence: Created `tools/game_policy.py`, `tools/game_harness.py`, `tests/test_game_harness.py`, and `.github/agents/project-manager-game.agent.md`. Final run `final-policy-validation-20260906-055642-4fa0eee8` completed. Through the harness, `python -m compileall tools tests` passed and the hard-boundary unit tests passed. The harness stores state and command logs only under `.game-manager/`.
Commit allowed: yes
Push allowed: yes
