from typing import Annotated

from fastapi import Depends, HTTPException, Query, Request
from pydantic import BaseModel

from database import ASYNC_SESSION_FACTORY
from utils.db_manager import DBManager
from services.auth import AuthService


## PaginationDep
class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(1, ge=1, description="Страница")]
    per_page: Annotated[
        int | None, Query(10, ge=1, lt=30, description="Элементов на странице")
    ]


## DB_Dep
async def get_db():
    async with DBManager(session_factory=ASYNC_SESSION_FACTORY) as db:
        yield db


## UserID_Dep
def get_token(request: Request):
    access_token = request.cookies.get("access_token", None)
    if access_token:
        return access_token
    raise HTTPException(status_code=401, detail="Вы не аутентифицированы")


def get_user_id(token: str = Depends(get_token)):
    data = AuthService().decode_access_token(token)
    return data.get("id")


def get_user_role(token: str = Depends(get_token)):
    data = AuthService().decode_access_token(token)
    return data.get("role")


## OUTPUT
PaginationDep = Annotated[PaginationParams, Depends()]
DB_Dep = Annotated[DBManager, Depends(get_db)]
UserID_Dep = Annotated[int, Depends(get_user_id)]
UserRole_Dep = Annotated[str, Depends(get_user_role)]
