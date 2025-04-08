from datetime import time, timedelta
from sqlalchemy import ForeignKey, Time
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseORM


class RecordsORM(BaseORM):
    """Таблица записей на прием"""

    __tablename__ = "records"

    id: Mapped[BaseORM.intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    workday_id: Mapped[int] = mapped_column(ForeignKey("workdays.id"))
    start_time: Mapped[time] = mapped_column(Time, nullable=False)

    @hybrid_property
    def end_time(self):
        return self.start_time + timedelta(minutes=self.service_rs.duration)

    @end_time.expression
    def end_time(cls):
        return cls.start_time + timedelta(minutes=cls.service_rs.duration)

    user_rs: Mapped["UsersORM"] = relationship(back_populates="records_rs")
    service_rs: Mapped["ServicesORM"] = relationship(back_populates="records_rs")
    workday_rs: Mapped["WorkdaysORM"] = relationship(back_populates="records_rs")
