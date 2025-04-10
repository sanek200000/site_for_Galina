from fastapi import APIRouter, Body, Query

from api.dependencies import DB_Dep, PaginationDep
from database import ASYNC_SESSION_FACTORY
from repositries.services import ServicesRepository
from schemas.services import ServiceAdd, ServicePatch
from utils.openapi_examples import ServicesOE


router = APIRouter(prefix="/services", tags=["Услуги"])


## GET
@router.get("", description="Показать все услуги.")
async def get_all(
    pagination: PaginationDep,
    db: DB_Dep,
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

    return await db.services_dbm.get_all(
        id, name, description, duration, price, limit, offset
    )


@router.get("/{service_id}", description="Получить услугу по id.")
async def get_one_or_none(db: DB_Dep, service_id: int):
    result = await db.services_dbm.get_one_or_none(id=service_id)
    return {"status": "OK", "data": result}


## POST
@router.post("", description="Добавить услугу.")
async def create(db: DB_Dep, data: ServiceAdd = Body(openapi_examples=ServicesOE.post)):
    result = await db.services_dbm.add(data)
    await db.commit()
    return {"status": "OK", "data": result}


## PUT
@router.put("/{service_id}", description="Редактировать услугу.")
async def put(db: DB_Dep, service_id: int, data: ServiceAdd):
    result = await db.services_dbm.edit(data, id=service_id)
    await db.commit()
    return {"status": "OK", "data": result}


## PATCH
@router.patch("/{service_id}", description="Редактировать услугу (выборочно).")
async def patch(db: DB_Dep, service_id: int, data: ServicePatch):
    result = await db.services_dbm.edit(data, is_exclude=True, id=service_id)
    await db.commit()
    return {"status": "OK", "data": result}


## DELETE
@router.delete("/{service_id}", description="Удалить услугу.")
async def delete(db: DB_Dep, service_id: int):
    await db.services_dbm.delete(id=service_id)
    await db.commit()
    return {"status": "OK"}
