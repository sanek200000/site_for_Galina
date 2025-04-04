import enum
from datetime import time
from sqlalchemy import Enum, ForeignKey, Time
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseORM
from models.services import ServicesORM


class StatusEnum(enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELED = "canceled"


class RecordsORM(BaseORM):
    """Таблица записей на прием"""

    __tablename__ = "records"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    workday_id: Mapped[int] = mapped_column(ForeignKey("workdays.id"))
    status: Mapped[StatusEnum] = mapped_column(Enum(StatusEnum), nullable=False)
    start_time: Mapped[time] = mapped_column(Time, nullable=False)

    service: Mapped[ServicesORM] = relationship("ServicesORM")

    @hybrid_property
    def end_time(self):
        return self.start_time + self.service.duration

    @end_time.expression
    def end_time(cls):
        return cls.start_time + cls.service.duration
