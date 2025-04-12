from pydantic import BaseModel
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from database import ENGINE
from repositries.mappers.mappers import BaseDataMapper


class BaseRepository:
    mapper: BaseDataMapper = None
    model: DeclarativeBase = None
    schema: BaseModel = None

    def __init__(self, session: AsyncSession):
        self.session = session

    ## GET
    async def get_all(self, limit: int, offset: int):
        query = select(self.model).limit(limit).offset(offset).order_by(self.model.id)
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        result = await self.session.scalars(query)
        return [self.mapper.map_to_domain_entity(row) for row in result.all()]

    async def get_one_or_none(self, **filter_by) -> BaseModel | None:
        query = select(self.model).filter_by(**filter_by)
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        res = await self.session.scalars(query)
        result = res.one_or_none()
        if result:
            return self.mapper.map_to_domain_entity(result)

    ## POST
    async def add(self, data: BaseModel):
        query = insert(self.model).values(**data.model_dump()).returning(self.model)
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        res = await self.session.execute(query)
        result = res.scalars().one()
        return self.mapper.map_to_domain_entity(result)

    ## PUT/PATCH
    async def edit(self, data: BaseModel, is_exclude: bool = False, **filter_by):
        query = (
            update(self.model)
            .filter_by(**filter_by)
            .values(**data.model_dump(exclude_unset=is_exclude))
            .returning(self.model)
        )
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        res = await self.session.execute(query)
        result = res.scalars().one()
        return self.mapper.map_to_domain_entity(result)

    ## DELETE
    async def delete(self, **filter_by):
        query = delete(self.model).filter_by(**filter_by).returning(self.model)
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )
        await self.session.execute(query)
