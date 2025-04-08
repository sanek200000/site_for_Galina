import enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseORM


class RolesEnum(enum.Enum):
    admin = "admin"
    barber = "barber"
    client = "client"


class UsersORM(BaseORM):
    __tablename__ = "users"

    id: Mapped[BaseORM.intpk]
    phone: Mapped[str] = mapped_column(String(length=12), unique=True)
    telagram: Mapped[str] = mapped_column(String(length=50), unique=True)
    role: Mapped[RolesEnum]
    name: Mapped[str] = mapped_column(String(length=100))
    email: Mapped[str | None] = mapped_column(String(length=50))
    hashed_password: Mapped[str] = mapped_column(String(length=64))
    created_at: Mapped[BaseORM.created_at]

    notifications_rs: Mapped[list["NotificationsORM"]] = relationship(
        back_populates="user_rs"
    )
    records_rs: Mapped[list["RecordsORM"]] = relationship(back_populates="user_rs")
