from sqlalchemy import func, select
from database import ENGINE
from models.services import ServicesORM
from repositries.base import BaseRepository
from repositries.mappers.mappers import ServicesDataMapper


class ServicesRepository(BaseRepository):
    mapper = ServicesDataMapper
    model = mapper.db_model
    schema = mapper.schema

    async def get_all(
        self,
        id: int,
        name: str,
        description: str,
        duration: int,
        price: int,
        limit: int,
        offset: int,
    ):
        query = select(self.model).limit(limit).offset(offset).order_by(self.model.id)
        if id:
            query = query.filter_by(id=id)
        if name:
            query = query.filter(
                func.lower(self.model.name).contains(name.lower().strip())
            )
        if description:
            query = query.filter(
                func.lower(self.model.description).contains(description.lower().strip())
            )
        if duration:
            query = query.filter_by(duration=duration)
        if price:
            query = query.filter_by(price=price)

        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        result = await self.session.scalars(query)
        return [self.mapper.map_to_domain_entity(row) for row in result.all()]
