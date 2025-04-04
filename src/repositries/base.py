from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class BaseRepository:
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        query = select(self.model)
        result = await self.session.exequte(query)

        return result.scalars().all()
