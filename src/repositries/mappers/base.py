from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase


class DataMapper:
    db_model: DeclarativeBase = None
    schema: BaseModel = None

    @classmethod
    def map_to_domain_entity(cls, model: DeclarativeBase):
        return cls.schema.model_validate(model, from_attributes=True)

    @classmethod
    def map_to_presistence_entity(cls, data: BaseModel):
        return cls.db_model(**data.model_dump())
