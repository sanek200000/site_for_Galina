from datetime import date, time
from sqlalchemy import Date, ForeignKey, Time
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseORM


class WorkdaysORM(BaseORM):
    """Таблица рабочих дней в месяце"""

    __tablename__ = "workdays"

    id: Mapped[int] = mapped_column(primary_key=True)
    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedules.id"))
    day_date: Mapped[date] = mapped_column(Date, nullable=False)
    start_time: Mapped[time] = mapped_column(Time, nullable=False)
    end_time: Mapped[time] = mapped_column(Time, nullable=False)
