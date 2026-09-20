from datetime import datetime, timezone
from uuid import uuid4

from ..errors import AppError, NotFoundError, ValidationError
from ..repositories import api as repo
from ..security import create_session, hash_password, validate_password_policy, verify_password, revoke_session
from ..database.connection import get_database


def clean_user(user: dict) -> dict:
    return {k: user[k] for k in (
        "id", "name", "email", "phone", "email_verified",
        "phone_verified", "role", "status", "created_at", "updated_at"
    )}


def normalize_email(email: str) -> str:
    return email.strip().casefold()


async def register(data):
    email = normalize_email(data.email)
    validate_password_policy(data.password, email, data.name)
    if await repo.find_user_by_email(email):
        raise AppError("E-mail já cadastrado", "email_already_exists", 409)
    user = await repo.create_user({
        "name": data.name.strip(), "email": email, "phone": data.phone,
        "password_hash": hash_password(data.password), "role": "user", "status": "active",
    })
    token, expires_at = await create_session(user["id"])
    await repo.log_event(user["id"], "auth.register", {"user_id": user["id"]})
    return token, expires_at, clean_user(user)


async def login(data):
    email = normalize_email(data.email)
    user = await repo.find_user_by_email(email)
    if not user or user.get("status", "active") != "active" or not verify_password(data.password, user["password_hash"]):
        raise AppError("Credenciais inválidas", "invalid_credentials", 401)
    token, expires_at = await create_session(user["id"])
    await repo.log_event(user["id"], "auth.login", {"user_id": user["id"]})
    return token, expires_at, clean_user(user)


async def logout(token: str):
    await revoke_session(token)


async def request_recovery(email: str):
    user = await repo.find_user_by_email(normalize_email(email))
    if user:
        await repo.log_event(user["id"], "auth.recovery_requested", {"user_id": user["id"]})
    return {"message": "Se a conta existir, as instruções de recuperação serão encaminhadas."}


async def document_or_404(document_id: str, user_id: str):
    document = await repo.get_document(document_id)
    if not document or document["owner_id"] != user_id:
        raise NotFoundError("Documento não encontrado")
    return document


async def folder_or_404(folder_id: str, user_id: str):
    folder = await repo.get_folder(folder_id)
    if not folder or folder["owner_id"] != user_id:
        raise NotFoundError("Pasta não encontrada")
    return folder


async def tag_or_404(tag_name: str, user_id: str):
    tag = await get_database()["etiquetas"].find_one({"name": tag_name, "owner_id": user_id})
    if not tag:
        raise NotFoundError("Etiqueta não encontrada")
    return tag


def page_values(page: int, page_size: int):
    if page < 1 or page_size < 1 or page_size > 100:
        raise ValidationError("Paginação inválida")
    return (page - 1) * page_size, page_size


async def version_number(document_id: str) -> int:
    last = await get_database()["versoes"].find_one({"document_id": document_id}, sort=[("version_number", -1)])
    return int(last["version_number"]) + 1 if last else 1
