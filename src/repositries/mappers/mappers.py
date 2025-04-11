from models.services import ServicesORM
from models.users import UsersORM
from repositries.mappers.base import DataMapper
from schemas.services import ServiceRead
from schemas.users import UserRead


class ServicesDataMapper(DataMapper):
    db_model = ServicesORM
    schema = ServiceRead


class UsersDataMapper(DataMapper):
    db_model = UsersORM
    schema = UserRead
