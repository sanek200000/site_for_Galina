from pydantic import BaseModel


class ServiceAdd(BaseModel):
    name: str
    description: str | None
    duration: int
    price: int


class Service(ServiceAdd):
    id: int


class ServicePatch(BaseModel):
    name: str | None = None
    description: str | None = None
    duration: int | None = None
    price: int | None = None


class ServiceFiltred(ServicePatch):
    id: int | None = None
