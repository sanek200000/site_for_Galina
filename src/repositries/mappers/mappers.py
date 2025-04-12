from typing import Any
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase

from models.notifications import NotificationsORM
from models.services import ServicesORM
from models.users import UsersORM
from schemas.notifications import NotificationRead
from schemas.services import ServiceRead
from schemas.users import UserRead


class BaseDataMapper:
    db_model: DeclarativeBase = None  ## модель sqlalchemy
    schema: BaseModel = None  ## pydantic схема

    @classmethod
    def map_to_domain_entity(cls, model: DeclarativeBase) -> BaseModel:
        """Конвертирует `sqlalchemy` модель в `pydantic` схему

        Args:
            model (DeclarativeBase): данные в формате `sqlalchemy` модели. Например `<UsersORM: id=15, name=Sanek>`

        Returns:
            BaseModel: данные в формате `pydantic` схемы. Например `UserRead(id=15, name='Sanek')`
        """
        return cls.schema.model_validate(model, from_attributes=True)

    @classmethod
    def map_to_dict(cls, model: DeclarativeBase) -> dict[str, Any]:
        """Конвертирует `sqlalchemy` модель в `pydantic` схему, а затем в словарь

        Args:
            model (DeclarativeBase): данные в формате `sqlalchemy` модели. Например `<UsersORM: id=15, name=Sanek>`

        Returns:
            dict[str, Any]: словарь значений. Например `{'id': 15, 'name': 'Sanek'}`
        """
        return cls.schema.model_validate(model, from_attributes=True).model_dump()

    @classmethod
    def map_to_presistence_entity(cls, data: BaseModel) -> DeclarativeBase:
        """Конвертирует данные `pydantic` схемы в модель `sqlalchemy`

        Args:
            data (BaseModel): данные в формате `pydantic` схемы. Например `UserRead(id=15, name='Sanek')`

        Returns:
            DeclarativeBase: данные в формате `sqlalchemy` модели. Например `<UsersORM: id=15, name=Sanek>`
        """
        return cls.db_model(**data.model_dump())


class ServicesDataMapper(BaseDataMapper):
    db_model = ServicesORM
    schema = ServiceRead


class UsersDataMapper(BaseDataMapper):
    db_model = UsersORM
    schema = UserRead


class NotificationsDataMapper(BaseDataMapper):
    db_model = NotificationsORM
    schema = NotificationRead
