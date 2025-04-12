from sqlalchemy.ext.asyncio import AsyncSession
from repositries.notifications import NotificationsRepository
from repositries.services import ServicesRepository
from repositries.users import UsersRepository


class DBManager:
    def __init__(self, session_factory: AsyncSession):
        self.__session_factory = session_factory

    async def __aenter__(self):
        self.__session = self.__session_factory()

        self.services_dbm = ServicesRepository(self.__session)
        self.users_dbm = UsersRepository(self.__session)
        self.notifications_dbm = NotificationsRepository(self.__session)

        return self

    async def __aexit__(self, *args):
        await self.__session.rollback()
        await self.__session.close()

    async def commit(self):
        await self.__session.commit()
