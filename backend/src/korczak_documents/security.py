from datetime import datetime, timedelta, timezone
from hashlib import sha256
import secrets
from uuid import uuid4

from ..database.connection import get_database
from ..errors import AppError, NotFoundError


SESSION_HOURS = 24


def hash_password(password: str) -> str:
    return sha256(password.encode("utf-8")).hexdigest()


def verify_password(password: str, password_hash: str) -> bool:
    return secrets.compare_digest(hash_password(password), password_hash)


def create_token() -> str:
    return secrets.token_urlsafe(48)


def token_hash(token: str) -> str:
    return sha256(token.encode("utf-8")).hexdigest()


async def create_session(user_id: str) -> tuple[str, datetime]:
    token = create_token()
    expires_at = datetime.now(timezone.utc) + timedelta(hours=SESSION_HOURS)
    await get_database()["sessoes"].insert_one({
        "id": str(uuid4()),
        "user_id": user_id,
        "token_hash": token_hash(token),
        "expires_at": expires_at,
        "created_at": datetime.now(timezone.utc),
    })
    return token, expires_at


async def require_user_from_token(token: str) -> dict:
    if not token:
        raise AppError("Autenticação obrigatória", "authentication_required", 401)
    session = await get_database()["sessoes"].find_one({
        "token_hash": token_hash(token),
        "expires_at": {"$gt": datetime.now(timezone.utc)},
    })
    if not session:
        raise AppError("Sessão inválida ou expirada", "invalid_session", 401)
    user = await get_database()["usuarios"].find_one({"id": session["user_id"]})
    if not user:
        raise NotFoundError("Usuário da sessão não encontrado")
    return user
