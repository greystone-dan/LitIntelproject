import base64
import binascii
import hmac
import os

from fastapi import FastAPI, Request
from fastapi.responses import Response

from .database import init_db
from .routes import router

app = FastAPI()


@app.middleware("http")
async def optional_private_access(request: Request, call_next):
    username = os.getenv("CASELIBRARY_PRIVATE_USER")
    password = os.getenv("CASELIBRARY_PRIVATE_PASSWORD")
    if not username or not password:
        return await call_next(request)

    authorization = request.headers.get("Authorization", "")
    try:
        scheme, encoded = authorization.split(" ", 1)
        supplied = base64.b64decode(encoded).decode("utf-8")
        supplied_username, supplied_password = supplied.split(":", 1)
    except (ValueError, UnicodeDecodeError, binascii.Error):
        supplied_username = supplied_password = ""

    valid = scheme.lower() == "basic" if "scheme" in locals() else False
    valid = valid and hmac.compare_digest(supplied_username, username)
    valid = valid and hmac.compare_digest(supplied_password, password)
    if not valid:
        return Response(status_code=401, headers={"WWW-Authenticate": 'Basic realm="AI CaseLibrary"'})
    return await call_next(request)


@app.on_event("startup")
def startup() -> None:
    init_db()


app.include_router(router)


@app.get("/")
def root():
    return {"message": "AI CaseLibrary backend is running"}
