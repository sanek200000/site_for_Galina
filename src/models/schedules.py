from datetime import date
from sqlalchemy import CheckConstraint, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseORM


class SchedulesORM(BaseORM):
    """Таблица расписания месяцев в году"""

    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(primary_key=True)
    month: Mapped[int] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[date]

    __table_args__ = (
        CheckConstraint("year >= 2025 AND year <= 2100", name="valid_year"),
        CheckConstraint("month >= 1 AND month <= 12", name="valid_month"),
        UniqueConstraint("month", "year", name="_month_year_uc"),
    )
