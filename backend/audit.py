import hmac
import json
import logging
import os
import time
from datetime import datetime, timezone
from hashlib import sha256
from logging.handlers import RotatingFileHandler
from uuid import uuid4

from starlette.types import ASGIApp, Message, Receive, Scope, Send


class _QuietRotatingFileHandler(RotatingFileHandler):
    def handleError(self, record: logging.LogRecord) -> None:
        # Logging's default error handler can print the record and a traceback.
        pass


class RequestAuditMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app
        self.handler = None
        self.address_key = b""
        self.raw_address = False
        path = os.getenv("CASELIBRARY_AUDIT_LOG")
        if path:
            try:
                self.address_key = os.urandom(32)
                self.raw_address = (
                    os.getenv("CASELIBRARY_AUDIT_LOG_RAW_ADDRESS", "").lower() == "true"
                )
                self.handler = _QuietRotatingFileHandler(
                    path,
                    maxBytes=5 * 1024 * 1024,
                    backupCount=3,
                    encoding="utf-8",
                    delay=True,
                )
                self.handler.setFormatter(logging.Formatter("%(message)s"))
            except Exception:
                self.handler = None

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or self.handler is None:
            await self.app(scope, receive, send)
            return

        started = time.perf_counter()
        timestamp = datetime.now(timezone.utc).isoformat()
        request_id = uuid4().hex
        status = 500

        async def capture_status(message: Message) -> None:
            nonlocal status
            if message["type"] == "http.response.start":
                status = message["status"]
            await send(message)

        try:
            await self.app(scope, receive, capture_status)
        finally:
            try:
                client = scope.get("client")
                address = client[0] if client else None
                route = scope.get("route")
                record = {
                    "time": timestamp,
                    "request_id": request_id,
                    "method": scope["method"],
                    "path": getattr(route, "path", "<unmatched>"),
                    "status": status,
                    "duration_ms": round((time.perf_counter() - started) * 1000, 3),
                    "client_address_hash": (
                        hmac.new(
                            self.address_key, address.encode("utf-8"), sha256
                        ).hexdigest()
                        if address is not None
                        else None
                    ),
                }
                if self.raw_address:
                    record["client_address"] = address
                self.handler.handle(
                    logging.LogRecord(
                        "caselibrary.audit",
                        logging.INFO,
                        "",
                        0,
                        json.dumps(record),
                        (),
                        None,
                    )
                )
            except Exception:
                pass
