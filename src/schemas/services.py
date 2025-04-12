from pydantic import BaseModel


class ServiceAdd(BaseModel):
    name: str
    description: str | None = None
    duration: int
    price: int


class ServiceRead(ServiceAdd):
    id: int


class ServicePatch(BaseModel):
    name: str | None = None
    description: str | None = None
    duration: int | None = None
    price: int | None = None
