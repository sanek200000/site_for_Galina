from passlib.context import CryptContext

from pydantic import BaseModel
from sqlalchemy import insert
from database import ENGINE
from models.users import UsersORM
from repositries.base import BaseRepository
from repositries.mappers.mappers import UsersDataMapper
from schemas.users import UserAdd, UserRead


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UsersRepository(BaseRepository):
    model = UsersORM
    schema = UserRead
    mapper = UsersDataMapper

    async def add(self, data: BaseModel):
        new_data = UserAdd(
            phone=data.phone,
            telagram=data.telagram,
            role=data.role,
            name=data.name,
            email=data.email,
            hashed_password=pwd_context.hash(data.password),
        )
        query = insert(self.model).values(**new_data.model_dump()).returning(self.model)
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        res = await self.session.execute(query)
        result = res.scalars().one()
        return self.mapper.map_to_domain_entity(result)
