from datetime import datetime, timezone
from typing import Annotated
from sqlalchemy import ForeignKey, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

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

    def __repr__(self):
        cols = [f"{col}={getattr(self, col)}" for col in self.__table__.columns.keys()]
        return f"{self.__class__.__name__}: {'|'.join(cols)}"


class WorkersORM(BaseORM):
    __tablename__ = "workers"
    id: Mapped[BaseORM.intpk]
    name: Mapped[str]

    resumes_col: Mapped[list["ResumesORM"]] = relationship(back_populates="worker_col")


class ResumesORM(BaseORM):
    __tablename__ = "resumes"
    id: Mapped[BaseORM.intpk]
    title: Mapped[str]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))

    worker_col: Mapped["WorkersORM"] = relationship(back_populates="resumes_col")

    vacancies_replied: Mapped[list["VacanciesORM"]] = relationship(
        back_populates="resumes_replied",
        secondary="m2m_vacancies_resumes",
    )


class VacanciesORM(BaseORM):
    __tablename__ = "vacancies"
    id: Mapped[BaseORM.intpk]
    title: Mapped[str]
    compinsation: Mapped[int | None]

    resumes_replied: Mapped[list["ResumesORM"]] = relationship(
        back_populates="vacancies_replied",
        secondary="m2m_vacancies_resumes",
    )


class VacanciesResumesORM(BaseORM):
    __tablename__ = "m2m_vacancies_resumes"
    id: Mapped[BaseORM.intpk]
    resume_id: Mapped[int] = mapped_column(ForeignKey("resumes.id", ondelete="CASCADE"))
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.id", ondelete="CASCADE")
    )
