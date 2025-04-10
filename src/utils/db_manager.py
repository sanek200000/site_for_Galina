from sqlalchemy.ext.asyncio import AsyncSession
from repositries.services import ServicesRepository


class DBManager:
    def __init__(self, session_factory: AsyncSession):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.services_dbm = ServicesRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()
