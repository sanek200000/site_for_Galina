from fastapi import APIRouter, Body, Query

from api.dependencies import DB_Dep, PaginationDep
from schemas.users import UserRequestAdd
from utils.openapi_examples import AuthOE


router = APIRouter(prefix="/auth", tags=["Аутентификация"])


## GET
@router.get("", description="Показать всех пользователей.")
async def get_all(
    pagination: PaginationDep,
    db: DB_Dep,
    id: int | None = Query(None, description="id"),
    phone: str | None = Query(None, description="Номер телефона"),
    telagram: str | None = Query(None, description="Никнейм в Telegram"),
    role: str | None = Query(None, description="Роль"),
    name: str | None = Query(None, description="Имя/ник"),
    email: str | None = Query(None, description="Почта"),
):
    limit = pagination.per_page
    offset = pagination.per_page * (pagination.page - 1)

    return await db.users_dbm.get_all(id, phone, telagram, role, name, email)


@router.get("/{user_id}", description="Получить пользователя по id.")
async def get(db: DB_Dep, user_id: int):
    result = await db.users_dbm.get_one_or_none(id=user_id)
    return {"status": "OK", "data": result}


## POST
@router.post("/register", description="Добавить пользователя.")
async def create(db: DB_Dep, data: UserRequestAdd = Body(openapi_examples=AuthOE.post)):
    result = await db.users_dbm.add(data)
    await db.commit()
    return {"status": "OK", "data": result}
