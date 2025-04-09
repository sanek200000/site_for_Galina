from pydantic import BaseModel
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import ENGINE


class BaseRepository:
    model = None

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def get_all(self):
        query = select(self.model).order_by(self.model.id)
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        result = await self.session.scalars(query)
        return result.all()

    async def get_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        result = await self.session.scalars(query)
        return result.one_or_none()

    async def add(self, data: BaseModel):
        query = insert(self.model).values(**data.model_dump()).returning(self.model)
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        result = await self.session.execute(query)
        return result.scalars().one()
