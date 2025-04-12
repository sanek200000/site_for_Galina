from datetime import datetime
from pydantic import BaseModel

from models.notifications import StatusEnum, TypeEnum


class NotificationAdd(BaseModel):
    user_id: int
    content: str
    type: TypeEnum
    status: StatusEnum
    scheduled_at: datetime
    sent_at: datetime


class NotificationRead(NotificationAdd):
    id: int
    created_at: datetime


class NotificationPatch(BaseModel):
    user_id: int | None = None
    content: str | None = None
    type: TypeEnum | None = None
    status: StatusEnum | None = None
    scheduled_at: datetime | None = None
    sent_at: datetime | None = None
