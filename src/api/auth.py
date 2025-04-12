from fastapi import APIRouter, Body, HTTPException, Query, Response

from api.dependencies import DB_Dep, PaginationDep, UserID_Dep
from models.users import RolesEnum
from schemas.users import UserLogin, UserRequestAdd
from utils.openapi_examples import AuthOE


router = APIRouter(prefix="/auth", tags=["Аутентификация"])


## GET
@router.get("", description="Показать всех пользователей")
async def get_all(
    pagination: PaginationDep,
    db: DB_Dep,
    id: int | None = Query(None, description="id"),
    phone: str | None = Query(None, description="Номер телефона"),
    telagram: str | None = Query(None, description="Никнейм в Telegram"),
    role: RolesEnum | None = Query(None, description="Роль"),
    name: str | None = Query(None, description="Имя/ник"),
    email: str | None = Query(None, description="Почта"),
):
    limit = pagination.per_page
    offset = pagination.per_page * (pagination.page - 1)

    return await db.users_dbm.get_all(
        id, phone, telagram, role, name, email, limit, offset
    )


@router.get("/me", description="Получить токен аутентификации")
async def only_auth(db: DB_Dep, user_id: UserID_Dep):
    result = await db.users_dbm.get_one_or_none(id=user_id)
    return {"status": "OK", "data": result}


## POST
@router.post("/sign_up", description="Регистрация.")
async def create(db: DB_Dep, data: UserRequestAdd = Body(openapi_examples=AuthOE.post)):
    result = await db.users_dbm.add(data)
    await db.commit()
    return {"status": "OK", "data": result}


@router.post("/login", description="Вход")
async def login(
    db: DB_Dep,
    response: Response,
    data: UserLogin = Body(openapi_examples=AuthOE.login),
):
    access_token = await db.users_dbm.login(data)
    if access_token:
        response.set_cookie("access_token", access_token)
        return {"status": "OK", "access_token": access_token}
    raise HTTPException(status_code=401, detail="Неверный логин или пароль")


@router.post("/logout", description="Выход")
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {"status": "OK"}
