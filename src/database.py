from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from conf import SETTINGS


engine = create_async_engine(SETTINGS.DB_URL)

async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


class BaseORM(DeclarativeBase):
    pass
