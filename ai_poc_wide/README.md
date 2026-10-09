# Wide run: explicit layers, verbatim quotes and a case frame, on 100 new decisions

Public case law only. No database. Inputs were built from the public read-only case pages of www.ilit.ca (`build_inputs.py`).
`inputs/` holds 100 decisions (3,906 paragraphs) not used in any earlier batch, with a code-built `frame` per decision. `selection.csv` lists them.
`run_wide.py` has three arms: v4 (the existing propositions prompt unchanged), L (adds an explicit layer 1-6 and a verbatim quote per point), LF (arm L with the code-built frame instead of the old case header).
`gpt41_cases.txt` is the 20-decision subset for the second-model run (arm L on gpt-4.1).
