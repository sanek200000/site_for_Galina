import enum
from datetime import date
from sqlalchemy import DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseORM


class StatusEnum(enum.Enum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"


class TypeEnum(enum.Enum):
    MASS = "mass_notification"
    REMINDER1 = "appointment_reminder_1h"
    REMINDER24 = "appointment_reminder_24h"
    OVERVIEW = "schedule_overview"


class NotificationsORM(BaseORM):
    """Таблица уведомлений"""

    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    content: Mapped[str]
    status: Mapped[StatusEnum] = mapped_column(Enum(StatusEnum), nullable=False)
    type: Mapped[TypeEnum] = mapped_column(Enum(TypeEnum), nullable=False)
    scheduled_at: Mapped[date] = mapped_column(DateTime, nullable=False)
    sent_at: Mapped[date] = mapped_column(DateTime, nullable=False)
    created_at: Mapped[date] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
