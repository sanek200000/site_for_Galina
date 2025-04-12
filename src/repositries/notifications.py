from repositries.base import BaseRepository
from repositries.mappers.mappers import NotificationsDataMapper


class NotificationsRepository(BaseRepository):
    mapper = NotificationsDataMapper
    model = mapper.db_model
    schema = mapper.schema
