import enum
from datetime import date
from sqlalchemy import DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
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

    id: Mapped[BaseORM.intpk] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    content: Mapped[str]
    status: Mapped[StatusEnum]
    type: Mapped[TypeEnum]
    scheduled_at: Mapped[date] = mapped_column(DateTime)
    sent_at: Mapped[date] = mapped_column(DateTime)
    created_at: Mapped[date] = mapped_column(DateTime, server_default=func.now())

    user = relationship("UsersORM", back_populates="notifications")
