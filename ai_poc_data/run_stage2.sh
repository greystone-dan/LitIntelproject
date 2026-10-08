#!/bin/bash
cd C:/Users/danny/ilit_poc
export PYTHONIOENCODING=utf-8 PYTHONPATH=.
PY="C:/Users/danny/OneDrive/Desktop/AI CaseLibrary/venv/Scripts/python.exe"
O=C:/Users/danny/ilit_poc_out
L=$O/spend_ledger.jsonl
run() { "$PY" $O/run_with_key.py "$@"; }
total() { "$PY" -c "import json;print(round(sum(json.loads(l).get('usd',0) for l in open(r'$L',encoding='utf-8') if l.strip()),4))"; }
echo "[A] start $(date +%T) ledger=$(total)"
for pair in "gpt-4.1-nano v3_nano" "gpt-4.1-mini v3_mini" "gpt-4.1 v3_gpt41"; do
  set -- $pair
  echo "== A $2 ($1) $(date +%T)"
  run scripts/ai_poc/tag_paragraphs.py --send --prompt v3 --model $1 --run $2 --cases 126,1292,1540,1046,1147,62 --out-dir $O/$2 --ledger $L 2>&1 | tail -8
done
echo "== score_roles $(date +%T)"
"$PY" scripts/ai_poc/score_roles.py $O/nano_v2_slice $O/v3_nano $O/v3_mini $O/v3_gpt41 2>&1 | tee $O/score_roles.txt
echo "[B] start $(date +%T) ledger=$(total)"
for m in gpt-4.1-mini gpt-4.1 gpt-5-mini; do
  echo "== B themes_$m $(date +%T)"
  run scripts/ai_poc/extract_themes.py --send --model $m --run themes_$m --cases 126,1540,1147,1046,1292 --out-dir $O/themes --ledger $L 2>&1 | tail -10
done
T=$(total); echo "[C] ledger before C = $T"
"$PY" -c "import sys;sys.exit(0 if $T<=3 else 1)" || { echo "C SKIPPED: ledger above 3 USD"; echo STAGE2_DONE; exit 0; }
echo "== C nano_v3_all300 $(date +%T)"
run scripts/ai_poc/tag_paragraphs.py --send --prompt v3 --model gpt-4.1-nano --run nano_v3_all300 --out-dir $O/nano_v3_all300 --ledger $L --workers 4 2>&1 | tail -12
echo "ledger final = $(total)"; echo STAGE2_DONE
