import asyncio

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload


from database import ENGINE, ASYNC_SESSION_FACTORY, BaseORM
from models.services import ServicesORM
from models.users import UsersORM


"""async def create_tables():
    async with ENGINE.begin() as conn:
        await conn.run_sync(BaseORM.metadata.drop_all)
        # await conn.run_sync(BaseORM.metadata.create_all)


async def insert_services():
    async with ASYNC_SESSION_FACTORY() as session:
        service1 = ServicesORM(name="pool", duration=5, price=500)
        service2 = ServicesORM(name="mool", duration=10, price=600)
        session.add_all([service1, service2])
        await session.commit()


async def select_services():
    async with ASYNC_SESSION_FACTORY() as session:
        query = select(ServicesORM)
        result = await session.execute(query)
        services = result.all()
        print(f"==================== {services}")


async def update_services(id=1, new_name="new"):
    async with ASYNC_SESSION_FACTORY() as session:
        service = await session.get(ServicesORM, id)
        service.name = new_name
        await session.commit()


async def insert_workers_resumes():
    async with ASYNC_SESSION_FACTORY() as session:
        worker1 = WorkersORM(name="Sasha")
        worker2 = WorkersORM(name="Pasha")
        resume1 = ResumesORM(title="Python Developer", worker_id=1)
        resume2 = ResumesORM(title="JAVA Developer", worker_id=1)
        resume3 = ResumesORM(title="C++ Developer", worker_id=2)
        resume4 = ResumesORM(title="C# Developer", worker_id=2)
        session.add_all([worker1, worker2, resume1, resume2, resume3, resume4])
        await session.commit()


async def select_workers():
    async with ASYNC_SESSION_FACTORY() as session:
        query = select(WorkersORM).options(selectinload(WorkersORM.resumes_col))
        res = await session.execute(query)
        results = res.unique().scalars().all()
        print(f"==================== {results}")
        [
            print(f"{r.name}: {' | '.join(n.title for n in r.resumes_col)}")
            for r in results
        ]


async def select_resumes():
    async with ASYNC_SESSION_FACTORY() as session:
        query = select(ResumesORM).options(joinedload(ResumesORM.worker_col))
        res = await session.execute(query)
        results = res.unique().scalars().all()
        print(f"==================== {results}")
        [print(f"{r.title}: {r.worker_col.name}") for r in results]


async def insert_vacancies_replied():
    async with ASYNC_SESSION_FACTORY() as session:
        new_vacancy = VacanciesORM(title="Midle Python Developer", compinsation=300000)
        get_resume_1 = (
            select(ResumesORM)
            .filter_by(id=1)
            .options(selectinload(ResumesORM.vacancies_replied))
        )
        get_resume_2 = (
            select(ResumesORM)
            .filter_by(id=3)
            .options(selectinload(ResumesORM.vacancies_replied))
        )
        resume1 = (await session.execute(get_resume_1)).scalar_one()
        resume2 = (await session.execute(get_resume_2)).scalar_one()
        resume1.vacancies_replied.append(new_vacancy)
        resume2.vacancies_replied.append(new_vacancy)
        await session.commit()


async def select_resumes_with_all_relationships():
    async with ASYNC_SESSION_FACTORY() as session:
        query = (
            select(ResumesORM)
            .options(joinedload(ResumesORM.worker_col))
            .options(
                selectinload(ResumesORM.vacancies_replied).load_only(VacanciesORM.title)
            )
        )

        res = await session.execute(query)
        result = res.unique().scalars().all()
        print(f"{result = }")

"""


async def insert_users():
    async with ASYNC_SESSION_FACTORY() as session:
        admin = UsersORM(
            phone="+79522318888",
            telagram="@sdfsdf",
            role="admin",
            name="Sasha",
            email="dsfsda@dsfsdf",
            hashed_password="111",
        )
        barber = UsersORM(
            phone="+79522317777",
            telagram="@aaa",
            role="barber",
            name="Galina",
            email="sdfdffff@dsfsdf",
            hashed_password="222",
        )
        client = UsersORM(
            phone="+79522315555",
            telagram="@asdd",
            role="client",
            name="Vasya",
            email="ddd@dsfsdf",
            hashed_password="333",
        )
        session.add_all([admin, barber, client])
        await session.commit()


async def select_users():
    async with ASYNC_SESSION_FACTORY() as session:
        query = select(UsersORM).filter_by(id=1)
        res = await session.execute(query)
        result = res.scalars().all()
        print(f"==================== {result}")


async def main():
    await select_users()


if __name__ == "__main__":
    asyncio.run(main())
