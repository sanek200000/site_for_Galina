from sqlalchemy.ext.asyncio import AsyncSession
from repositries.services import ServicesRepository


class DBManager:
    def __init__(self, session_factory: AsyncSession):
        self.__session_factory = session_factory

    async def __aenter__(self):
        self.__session = self.__session_factory()

        self.services_dbm = ServicesRepository(self.__session)

        return self

    async def __aexit__(self, *args):
        await self.__session.rollback()
        await self.__session.close()

    async def commit(self):
        await self.__session.commit()
