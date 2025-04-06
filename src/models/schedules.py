from datetime import date, datetime
from sqlalchemy import CheckConstraint, Date, ForeignKey, Time, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseORM


class MonthesORM(BaseORM):
    """Таблица расписания месяцев в году"""

    __tablename__ = "monthes"

    id: Mapped[int] = mapped_column(primary_key=True)
    month: Mapped[int] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[date]

    workdays = relationship(
        "WorkdaysORM",
        back_populates="monthes",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        CheckConstraint("year >= 2025 AND year <= 2100", name="valid_year"),
        CheckConstraint("month >= 1 AND month <= 12", name="valid_month"),
        UniqueConstraint("month", "year", name="_month_year_uc"),
    )


class WorkdaysORM(BaseORM):
    """Таблица рабочих дней в месяце"""

    __tablename__ = "workdays"

    id: Mapped[int] = mapped_column(primary_key=True)
    schedule_id: Mapped[int] = mapped_column(ForeignKey("monthes.id"))
    day_date: Mapped[date] = mapped_column(Date, nullable=False)
    start_time: Mapped[datetime] = mapped_column(Time, nullable=False)
    end_time: Mapped[datetime] = mapped_column(Time, nullable=False)

    month = relationship("MonthesORM", back_populates="workdays")
