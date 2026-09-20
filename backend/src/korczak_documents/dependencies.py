from fastapi import Header
from .security import require_user_from_token


async def current_user(authorization: str | None = Header(default=None)) -> dict:
    token = ""
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization[7:].strip()
    return await require_user_from_token(token)
