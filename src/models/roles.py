from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseORM


class RolesORM(BaseORM):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=50), unique=True)
