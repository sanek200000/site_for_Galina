from datetime import date
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseORM


class UsersORM(BaseORM):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(String(length=12), unique=True)
    email: Mapped[str] = mapped_column(String(length=50), unique=True)
    telagramm: Mapped[str] = mapped_column(String(length=50), unique=True)
    name: Mapped[str] = mapped_column(String(length=100))
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    hashed_password: Mapped[str] = mapped_column(String(length=64))
    created_at: Mapped[date]
