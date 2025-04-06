from datetime import datetime, timezone
from typing import Annotated
from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column

from conf import SETTINGS


ENGINE = create_async_engine(url=SETTINGS.DB_URL, echo=True)

ASYNC_SESSION_FACTORY = async_sessionmaker(bind=ENGINE, expire_on_commit=False)


class BaseORM(DeclarativeBase):
    intpk = Annotated[int, mapped_column(primary_key=True)]
    created_at = Annotated[
        datetime,
        mapped_column(server_default=text("TIMEZONE('utc', now())")),
    ]
    updated_at = Annotated[
        datetime,
        mapped_column(
            server_default=text("TIMEZONE('utc', now())"),
            onupdate=datetime.now(timezone.utc),
        ),
    ]


"""
    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"""
