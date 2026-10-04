"""Selective GZip compression for ordinary HTTP responses."""

from starlette.datastructures import Headers
from starlette.middleware.gzip import GZipMiddleware, GZipResponder
from starlette.types import ASGIApp, Message, Receive, Scope, Send


class SelectiveGZipMiddleware(GZipMiddleware):
    """Compress buffered responses, but pass downloads and streams through.

    Response headers are inspected before the GZip responder receives them so
    attachment and no-store responses are never compressed. Streaming responses
    are detected from their first body message and forwarded without buffering.
    """

    def __init__(
        self,
        app: ASGIApp,
        minimum_size: int = 500,
        compresslevel: int = 9,
    ) -> None:
        super().__init__(app, minimum_size=minimum_size, compresslevel=compresslevel)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        if not self._accepts_gzip(scope):
            await self.app(scope, receive, send)
            return

        responder = GZipResponder(
            self.app,
            self.minimum_size,
            compresslevel=self.compresslevel,
        )
        responder.send = send
        response_start: Message | None = None
        compress: bool | None = None

        async def send_wrapper(message: Message) -> None:
            nonlocal response_start, compress

            if message["type"] == "http.response.start":
                response_start = message
                return

            if message["type"] == "http.response.pathsend":
                # FileResponse can use this ASGI extension instead of a body.
                # Do not feed file-transfer messages to the GZip responder.
                if response_start is not None:
                    await send(response_start)
                await send(message)
                compress = False
                return

            if message["type"] == "http.response.body" and compress is None:
                headers = dict(response_start.get("headers", [])) if response_start else {}
                content_type = headers.get(b"content-type", b"").lower()
                disposition = headers.get(b"content-disposition", b"").lower()
                cache_control = headers.get(b"cache-control", b"").lower()
                first_body_is_streaming = bool(message.get("more_body", False))
                compress = not (
                    first_body_is_streaming
                    or disposition
                    or b"no-store" in cache_control
                    or content_type.startswith(b"text/event-stream")
                )

                if compress:
                    if response_start is not None:
                        await responder.send_with_gzip(response_start)
                    await responder.send_with_gzip(message)
                else:
                    if response_start is not None:
                        await send(response_start)
                    await send(message)
                return

            if compress:
                await responder.send_with_gzip(message)
            else:
                await send(message)

        await self.app(scope, receive, send_wrapper)

        # ASGI applications normally send a final body, including for empty
        # responses. Preserve a start-only response if an application does not.
        if response_start is not None and compress is None:
            await send(response_start)

    @staticmethod
    def _accepts_gzip(scope: Scope) -> bool:
        value = Headers(scope=scope).get("accept-encoding", "")
        for encoding in value.split(","):
            name, *parameters = encoding.strip().lower().split(";")
            if name.strip() != "gzip":
                continue
            quality = next(
                (
                    parameter.strip().partition("=")[2]
                    for parameter in parameters
                    if parameter.strip().startswith("q=")
                ),
                "1",
            )
            try:
                return float(quality) > 0
            except ValueError:
                return False
        return False
