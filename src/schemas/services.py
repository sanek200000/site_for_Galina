from pydantic import BaseModel, ConfigDict


class ServiceAdd(BaseModel):
    name: str
    description: str | None
    duration: int
    price: int


class ServiceRead(ServiceAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ServicePatch(BaseModel):
    name: str | None = None
    description: str | None = None
    duration: int | None = None
    price: int | None = None
