from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseORM


class RolesORM(BaseORM):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)

    users: Mapped[list["UsersORM"]] = relationship(
        back_populates="roles",
        secondary="users_roles",
    )


class UsersORM(BaseORM):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    phone: Mapped[str] = mapped_column(String(length=12), unique=True)
    telagram: Mapped[str] = mapped_column(String(length=50), unique=True)
    email: Mapped[str | None] = mapped_column(String(length=50), nullable=True)
    name: Mapped[str] = mapped_column(String(length=100))
    hashed_password: Mapped[str] = mapped_column(String(length=64))
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )

    roles: Mapped[list["RolesORM"]] = relationship(
        back_populates="users",
        secondary="users_roles",
    )


class UsersRoomsORM(BaseORM):
    __tablename__ = "users_roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
