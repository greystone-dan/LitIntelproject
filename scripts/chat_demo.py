"""Throwaway local-model chat demo ("Under development"); separate from the iLit site.

Run by hand on the PC, never as part of the site or a scheduled task:

    ILIT_CHAT_DEMO=1 python scripts/chat_demo.py

It binds to 127.0.0.1:8765 only and talks only to the local Ollama on the same
machine. Messages are never stored or logged; only counters are kept in memory.
Without ILIT_CHAT_DEMO=1 it refuses to start. CHAT_DEMO_STUB=1 swaps the model
for a canned reply (used for tests and screenshots).
"""

from __future__ import annotations

import asyncio
import os
import sys
import time
from contextlib import asynccontextmanager
from collections import deque
from urllib.parse import urlsplit

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

HOST = "127.0.0.1"
PORT = int(os.getenv("CHAT_DEMO_PORT", "8765"))
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434/v1").rstrip("/").removesuffix("/v1")
MODEL = os.getenv("OLLAMA_MODEL", "qwen3:4b")

MAX_MESSAGE_CHARS = 1000
MAX_USER_TURNS = 10
MAX_MESSAGES = 2 * MAX_USER_TURNS + 1  # 10 questions, 10 answers, the new question
MAX_ANSWER_TOKENS = 400
REQUEST_TIMEOUT_SECONDS = 90.0
PER_VISITOR_PER_MINUTE = 10
GLOBAL_PER_MINUTE = 30

SYSTEM_PROMPT = (
	"You are a small demo assistant running on a private computer. You have no access to "
	"any database, files, websites or case law, so never claim to look anything up. "
	"Answer briefly and plainly. You are not a lawyer and this is not legal advice."
)

_busy = asyncio.Lock()
_visitor_hits: dict[str, deque[float]] = {}
_global_hits: deque[float] = deque()
counters = {"answered": 0, "busy": 0, "rate_limited": 0, "rejected": 0, "failed": 0}


def _stub_enabled() -> bool:
	return os.getenv("CHAT_DEMO_STUB") == "1"


def _allowed(visitor: str, now: float) -> bool:
	"""Sliding one-minute window per visitor and overall; memory only."""
	cutoff = now - 60.0
	while _global_hits and _global_hits[0] < cutoff:
		_global_hits.popleft()
	hits = _visitor_hits.get(visitor, deque())
	while hits and hits[0] < cutoff:
		hits.popleft()
	if len(hits) >= PER_VISITOR_PER_MINUTE or len(_global_hits) >= GLOBAL_PER_MINUTE:
		if not hits:
			_visitor_hits.pop(visitor, None)
		return False
	_visitor_hits[visitor] = hits
	hits.append(now)
	_global_hits.append(now)
	return True


def _clean_messages(payload: object) -> list[dict[str, str]] | None:
	"""Keep only plain user/assistant text within the caps; None if invalid."""
	raw = payload.get("messages") if isinstance(payload, dict) else None
	if not isinstance(raw, list) or not raw or len(raw) > MAX_MESSAGES:
		return None
	cleaned: list[dict[str, str]] = []
	for item in raw:
		if not isinstance(item, dict):
			return None
		role, content = item.get("role"), item.get("content")
		if role not in ("user", "assistant") or not isinstance(content, str):
			return None
		content = content.strip()
		if not content or len(content) > MAX_MESSAGE_CHARS:
			return None
		cleaned.append({"role": role, "content": content})
	if cleaned[-1]["role"] != "user":
		return None
	if sum(1 for m in cleaned if m["role"] == "user") > MAX_USER_TURNS:
		return None
	return cleaned


async def _ask_model(messages: list[dict[str, str]]) -> str:
	if _stub_enabled():
		await asyncio.sleep(0.2)
		return "This is a canned test reply. No model was called."
	payload = {
		"model": MODEL,
		"messages": [{"role": "system", "content": SYSTEM_PROMPT}, *messages],
		"stream": False,
		"think": False,
		"options": {"temperature": 0.3, "num_predict": MAX_ANSWER_TOKENS},
	}
	# trust_env=False: never route a visitor's text through a proxy set in the environment.
	async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT_SECONDS, trust_env=False) as client:
		response = await client.post(f"{OLLAMA_URL}/api/chat", json=payload)
		response.raise_for_status()
		return str(response.json().get("message", {}).get("content", "")).strip()


def check_config() -> None:
	"""Refuse to run unless switched on and pointed at a model on this same machine."""
	if os.getenv("ILIT_CHAT_DEMO") != "1":
		raise RuntimeError("Chat demo is off. Set ILIT_CHAT_DEMO=1 to run it.")
	if urlsplit(OLLAMA_URL).hostname not in ("127.0.0.1", "localhost", "::1"):
		raise RuntimeError("OLLAMA_BASE_URL must point at this machine (127.0.0.1 or localhost).")


@asynccontextmanager
async def _lifespan(_app: FastAPI):
	check_config()
	yield


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None, lifespan=_lifespan)


@app.middleware("http")
async def _private_headers(request: Request, call_next):
	response = await call_next(request)
	response.headers["X-Robots-Tag"] = "noindex, nofollow, noarchive"
	response.headers["Cache-Control"] = "no-store"
	return response


@app.get("/", response_class=HTMLResponse)
async def page() -> str:
	return PAGE


@app.get("/health")
async def health() -> dict[str, object]:
	return {"ok": True, "stub": _stub_enabled(), "counters": counters}


@app.post("/api/chat")
async def chat(request: Request) -> JSONResponse:
	# Behind the Cloudflare tunnel the real visitor address is in this header.
	visitor = request.headers.get("cf-connecting-ip") or (request.client.host if request.client else "?")
	if not _allowed(visitor, time.monotonic()):
		counters["rate_limited"] += 1
		return JSONResponse({"error": "Too many messages. Please wait a minute."}, status_code=429)
	try:
		messages = _clean_messages(await request.json())
	except ValueError:
		messages = None
	if messages is None:
		counters["rejected"] += 1
		return JSONResponse(
			{"error": f"Message not accepted (max {MAX_MESSAGE_CHARS} characters, {MAX_USER_TURNS} questions per chat)."},
			status_code=400,
		)
	if _busy.locked():
		counters["busy"] += 1
		return JSONResponse({"error": "The demo is busy with someone else. Try again shortly."}, status_code=503)
	async with _busy:
		try:
			answer = await _ask_model(messages)
		except (httpx.HTTPError, ValueError):
			counters["failed"] += 1
			return JSONResponse({"error": "The local model did not answer in time."}, status_code=502)
	counters["answered"] += 1
	return JSONResponse({"answer": answer or "(no answer)"})


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Local AI chat demo</title>
<style>
:root{--bg:#f6f5f1;--fg:#1d1d1b;--mut:#5d5d58;--card:#fff;--line:#d9d6cc;--warn:#fff4d6;--warnl:#e2c46a;--me:#e8eef7;--acc:#1f4e8c}
@media (prefers-color-scheme:dark){:root{--bg:#161614;--fg:#ecebe6;--mut:#a3a29a;--card:#201f1d;--line:#3a3935;--warn:#3a3014;--warnl:#7a6420;--me:#1d2a3d;--acc:#7fb0ee}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif}
main{max-width:720px;margin:0 auto;padding:16px}
.tag{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;background:var(--warn);border:1px solid var(--warnl);border-radius:4px;padding:2px 8px}
h1{font-size:22px;margin:8px 0}
.warn{background:var(--warn);border:1px solid var(--warnl);border-radius:8px;padding:12px 14px;margin:12px 0;font-size:15px}
#log{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px;min-height:240px;max-height:55vh;overflow:auto}
.m{margin:0 0 10px;padding:8px 10px;border-radius:8px;white-space:pre-wrap;overflow-wrap:anywhere}
.u{background:var(--me)}.a{border:1px solid var(--line)}.e{color:#b3261e;font-size:14px}
.hint{color:var(--mut)}
form{display:flex;gap:8px;margin-top:12px}
textarea{flex:1;font:inherit;color:inherit;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px;resize:vertical;min-height:48px}
button{font:inherit;font-weight:600;background:var(--acc);color:#fff;border:0;border-radius:8px;padding:0 18px;min-height:44px;cursor:pointer}
button:disabled{opacity:.5;cursor:default}
.foot{color:var(--mut);font-size:13px;margin-top:8px}
</style></head><body><main>
<span class="tag">Under development &middot; demo</span>
<h1>Local AI chat demo</h1>
<div class="warn"><strong>This is a test, not part of iLit.</strong> Your messages are sent to an AI model running on Daniel&rsquo;s own computer, and to no outside service. This page does not save your messages. It cannot look up case law, answers can be wrong or slow, and it is not legal advice. Please do not type anything confidential. One person can chat at a time.</div>
<div id="log" aria-live="polite"><p class="m hint">Ask a short question. The model is small, so answers may take 10 to 60 seconds.</p></div>
<form id="f"><textarea id="t" maxlength="1000" placeholder="Type a question (up to 1,000 characters)" aria-label="Your message"></textarea><button id="b">Send</button></form>
<p class="foot">Up to 10 questions per chat. Reloading the page clears the chat.</p>
</main><script>
const log=document.getElementById('log'),t=document.getElementById('t'),b=document.getElementById('b');
let hist=[];
function add(c,x){const p=document.createElement('p');p.className='m '+c;p.textContent=x;log.appendChild(p);log.scrollTop=log.scrollHeight;return p}
document.getElementById('f').addEventListener('submit',async e=>{
 e.preventDefault();const q=t.value.trim();if(!q)return;
 t.value='';add('u',q);hist.push({role:'user',content:q});b.disabled=true;
 const w=add('a hint','Thinking\\u2026');
 try{const r=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({messages:hist})});
  const d=await r.json();w.remove();
  if(r.ok){add('a',d.answer);hist.push({role:'assistant',content:d.answer})}
  else{add('e',d.error||'Something went wrong.');hist.pop()}
 }catch(_){w.remove();add('e','Could not reach the demo.');hist.pop()}
 b.disabled=false;t.focus()});
</script></body></html>"""


if __name__ == "__main__":
	try:
		check_config()
	except RuntimeError as exc:
		sys.exit(str(exc))
	import uvicorn

	uvicorn.run(app, host=HOST, port=PORT, log_level="warning", access_log=False)
