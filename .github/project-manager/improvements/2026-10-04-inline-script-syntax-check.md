# Inline generated-script syntax check

- Observed issue or missed opportunity: A `Citation Map` HTML string replacement
  placed ARIA state updates outside an arrow-function body, producing invalid
  inline JavaScript even though Python compilation and HTML assertions passed.
- Evidence: The first `node --check` of the generated inline script failed with
  `SyntaxError: missing ) after argument list`; bracing the callbacks repaired
  it, and the same check passed.
- Proposed change: For page-builder changes that emit inline JavaScript, extract
  generated `<script>` bodies in a focused test and run an available JS parser
  such as `node --check`, with a documented skip when the runtime is absent.
- Expected value and risk: Catches client-side parse errors cheaply before a
  browser is available. Risk is low; keep the check scoped to builders whose
  scripts changed rather than imposing Node on unrelated Python-only tests.
- Decision and date: Deferred for a separate test-infrastructure task,
  2026-10-04. This issue's generated Citation Map script was syntax-checked
  directly and passed after repair.
