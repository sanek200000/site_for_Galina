from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseORM


class ServicesORM(BaseORM):
    """Таблица услуг оказываемых парекмахером"""

    __tablename__ = "services"

    id: Mapped[BaseORM.intpk]
    name: Mapped[str] = mapped_column(String(length=50), unique=True)
    description: Mapped[str | None]
    duration: Mapped[int]
    price: Mapped[int]

    records_rs: Mapped[list["RecordsORM"]] = relationship(back_populates="service_rs")
