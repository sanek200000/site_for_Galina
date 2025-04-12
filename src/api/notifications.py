from fastapi import APIRouter, Body, HTTPException

from api.dependencies import DB_Dep, PaginationDep, UserRole_Dep
from schemas.notifications import NotificationAdd, NotificationPatch
from utils.openapi_examples import NotificationsOE


router = APIRouter(prefix="/notifications", tags=["Уведомления"])


## GET
@router.get("", description="Показать все уведомления")
async def get_all(pagination: PaginationDep, db: DB_Dep):
    limit = pagination.per_page
    offset = pagination.per_page * (pagination.page - 1)

    return await db.notifications_dbm.get_all(limit, offset)


## POST
@router.post("", description="Добавить уведомление")
async def create(
    db: DB_Dep,
    data: NotificationAdd = Body(openapi_examples=NotificationsOE.post),
):
    result = await db.notifications_dbm.add(data)
    await db.commit()
    return {"status": "OK", "data": result}


## PUT
@router.put("/{notification_id}", description="Редактировать уведомление.")
async def put(db: DB_Dep, notification_id: int, data: NotificationAdd):
    result = await db.notifications_dbm.edit(data, id=notification_id)
    await db.commit()
    return {"status": "OK", "data": result}


## PATCH
@router.patch(
    "/{notification_id}",
    description="Редактировать уведомление (выборочно).",
)
async def patch(db: DB_Dep, notification_id: int, data: NotificationPatch):
    result = await db.notifications_dbm.edit(data, is_exclude=True, id=notification_id)
    await db.commit()
    return {"status": "OK", "data": result}


## DELETE
@router.delete("/{notification_id}", description="Удалить уведомление.")
async def delete(user_role: UserRole_Dep, db: DB_Dep, notification_id: int):
    if user_role in ["admin", "barber"]:
        await db.notifications_dbm.delete(id=notification_id)
        await db.commit()
        return {"status": "OK"}
    raise HTTPException(401, detail="Недостаточно прав")
