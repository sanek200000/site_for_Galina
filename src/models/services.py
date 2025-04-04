from datetime import timedelta
from sqlalchemy import Interval, String
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseORM


class ServicesORM(BaseORM):
    """Таблица услуг оказываемых парекмахером"""

    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=50), unique=True)
    description: Mapped[str | None]
    duration: Mapped[timedelta] = mapped_column(Interval, nullable=False)
    price: Mapped[int]
