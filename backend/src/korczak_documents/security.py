from datetime import datetime, timedelta, timezone
from hashlib import pbkdf2_hmac, sha256
import base64
import hmac
import secrets
from uuid import uuid4

from ..database.connection import get_database
from ..errors import AppError, NotFoundError


SESSION_HOURS = 24
_PASSWORD_ITERATIONS = 310_000


def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    digest = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _PASSWORD_ITERATIONS)
    return "pbkdf2_sha256$" + str(_PASSWORD_ITERATIONS) + "$" + base64.urlsafe_b64encode(salt).decode("ascii") + "$" + base64.urlsafe_b64encode(digest).decode("ascii")


def verify_password(password: str, encoded: str) -> bool:
    try:
        algorithm, iterations, salt_text, digest_text = encoded.split("$", 3)
        if algorithm != "pbkdf2_sha256":
            return False
        salt = base64.urlsafe_b64decode(salt_text.encode("ascii"))
        expected = base64.urlsafe_b64decode(digest_text.encode("ascii"))
        actual = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, int(iterations))
        return hmac.compare_digest(actual, expected)
    except (ValueError, TypeError):
        return False


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
