from typing import Annotated

from fastapi import Depends, Query
from pydantic import BaseModel

from database import ASYNC_SESSION_FACTORY
from utils.db_manager import DBManager


class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(1, ge=1, description="Страница")]
    per_page: Annotated[
        int | None, Query(3, ge=1, lt=30, description="Элементов на странице")
    ]


async def get_db():
    async with DBManager(session_factory=ASYNC_SESSION_FACTORY) as db:
        yield db


PaginationDep = Annotated[PaginationParams, Depends()]
DB_Dep = Annotated[DBManager, Depends(get_db)]
