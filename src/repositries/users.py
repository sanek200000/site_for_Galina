from sqlalchemy import func, insert, select
from database import ENGINE
from models.users import RolesEnum
from repositries.base import BaseRepository
from repositries.mappers.mappers import UsersDataMapper
from schemas.users import UserAdd, UserLogin, UserRequestAdd
from services.auth import AuthService


class UsersRepository(BaseRepository):
    mapper = UsersDataMapper
    model = mapper.db_model
    schema = mapper.schema

    ##GET
    async def get_all(
        self,
        id: int,
        phone: str,
        telagram: str,
        role: RolesEnum,
        name: str,
        email: str,
        limit: int,
        offset: int,
    ):
        query = select(self.model).limit(limit).offset(offset).order_by(self.model.id)
        if id:
            query = query.filter_by(id=id)
        if phone:
            query = query.filter(
                func.lower(self.model.phone).contains(phone.lower().strip())
            )
        if telagram:
            query = query.filter(
                func.lower(self.model.telagram).contains(telagram.lower().strip())
            )
        if role:
            query = query.filter_by(role=role)
        if name:
            query = query.filter(
                func.lower(self.model.name).contains(name.lower().strip())
            )
        if email:
            query = query.filter(
                func.lower(self.model.email).contains(email.lower().strip())
            )

        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        result = await self.session.scalars(query)
        return [self.mapper.map_to_domain_entity(row) for row in result.all()]

    ## POST
    async def add(self, data: UserRequestAdd):
        new_data = UserAdd(
            phone=data.phone,
            telagram=data.telagram,
            role=data.role,
            name=data.name,
            email=data.email,
            hashed_password=AuthService().pwd_context.hash(data.password),
        )
        query = insert(self.model).values(**new_data.model_dump()).returning(self.model)
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        res = await self.session.execute(query)
        result = res.scalars().one()
        return self.mapper.map_to_domain_entity(result)

    async def login(self, data: UserLogin):
        query = select(self.model).filter_by(phone=data.phone)
        print(
            f"=====> {query.compile(bind=ENGINE, compile_kwargs={'literal_binds': True})}"
        )

        res = await self.session.scalars(query)
        user = res.one_or_none()
        if user and AuthService().verify_password(data.password, user.hashed_password):
            user_dump = self.mapper.map_to_dict(user)
            access_token = AuthService().create_access_token(user_dump)
            return access_token
