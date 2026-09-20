from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class TimestampedModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    created_at: datetime
    updated_at: datetime


class UserModel(TimestampedModel):
    id: str
    name: str = Field(min_length=1, max_length=160)
    email: str
    phone: str | None = None
    password_hash: str
    email_verified: bool = False
    phone_verified: bool = False
    role: str = "user"


class DocumentModel(TimestampedModel):
    id: str
    owner_id: str
    name: str = Field(min_length=1, max_length=255)
    document_type: str
    folder_id: str | None = None
    current_version_id: str | None = None
    status: str = "active"


class VersionModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    document_id: str
    version_number: int = Field(ge=1)
    author_id: str
    content: str | None = None
    created_at: datetime


class FolderModel(TimestampedModel):
    id: str
    owner_id: str
    parent_id: str | None = None
    name: str = Field(min_length=1, max_length=255)


class TagModel(TimestampedModel):
    id: str
    owner_id: str
    name: str = Field(min_length=1, max_length=100)


class SessionModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    user_id: str
    token_hash: str
    expires_at: datetime
    created_at: datetime


class EventModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    user_id: str | None = None
    type: str
    payload: dict = Field(default_factory=dict)
    created_at: datetime


class NotificationModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    user_id: str
    type: str
    message: str
    read: bool = False
    created_at: datetime
