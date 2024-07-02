from typing import Callable, Union
from api.model.room import Room
from api.repository.base_repository import BaseRepository
from api.database.db_connector import SessionMaker


class RoomRepository(BaseRepository):
    """
    Repository class for handling operations related to Room entities.
    """

    def __init__(self, session_maker: SessionMaker):
        super().__init__(session_maker, Room)

    async def find_and_update(
        self, room_id: int, update_room: Room,
        usecase: Union[Callable, None] = None,
        ) -> Room:
        updated_room_dict = update_room.model_dump(exclude_unset=True)
        return await super().find_and_update(room_id, updated_room_dict, usecase)
