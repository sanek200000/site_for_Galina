from fastapi import APIRouter, Body, Query
from sqlalchemy import func, insert, select

from api.dependencies import PaginationDep
from database import ASYNC_SESSION_FACTORY, ENGINE
from models.services import ServicesORM
from repositries.services import ServicesRepository
from schemas.services import ServiceAdd, ServicePatch
from utils.openapi_examples import ServicesOE


router = APIRouter(prefix="/services", tags=["Услуги"])


## GET
@router.get("", description="Показать все услуги.")
async def get_all(
    pagination: PaginationDep,
    id: int | None = Query(None, description="id"),
    name: str | None = Query(None, description="Наименование услуги"),
    description: str | None = Query(None, description="Описание услуги"),
    duration: int | None = Query(
        None, description="Интервал времени на оказание услуги в минутах"
    ),
    price: int | None = Query(None, description="Цена услуги"),
):
    limit = pagination.per_page
    offset = pagination.per_page * (pagination.page - 1)

    async with ASYNC_SESSION_FACTORY() as session:
        return await ServicesRepository(session).get_all(
            id, name, description, duration, price, limit, offset
        )


## POST
@router.post("", description="Добавить услугу.")
async def create(data: ServiceAdd = Body(openapi_examples=ServicesOE.post)):
    async with ASYNC_SESSION_FACTORY() as session:
        result = await ServicesRepository(session).add(data)
        await session.commit()

    return {"status": "OK", "data": result}


## PUT
@router.put("/{service_id}", description="Редактировать услугу.")
async def put(service_id: int, data: ServiceAdd):
    data = {"id": service_id} | data.model_dump()
    return data


## PATCH
@router.patch("/{service_id}", description="Редактировать услугу (выборочно).")
async def patch(service_id: int, data: ServicePatch):
    data = {"id": service_id} | data.model_dump()
    return data


## DELETE
@router.delete("/{service_id}", description="Удалить услугу.")
async def delete(service_id: int): ...
