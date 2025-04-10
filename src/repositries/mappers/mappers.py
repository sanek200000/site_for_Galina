from models.services import ServicesORM
from repositries.mappers.base import DataMapper
from schemas.services import ServiceRead


class ServicesDataMapper(DataMapper):
    db_model = ServicesORM
    schema = ServiceRead
