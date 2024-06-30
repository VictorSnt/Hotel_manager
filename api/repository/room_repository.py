from typing import Callable, Dict, Union
from api.model.room import Room
from api.repository.base_repository import BaseRepository
from api.schemas.room_schema import CreateRoom
from api.database.db_connector import SessionMaker


class RoomRepository(BaseRepository):
    """
    Repository class for handling operations related to Room entities.
    """

    def __init__(self, session_maker: SessionMaker):
        super().__init__(session_maker, Room)

    async def create(self, created_room: CreateRoom) -> Room:
        new_room = Room(**created_room.model_dump())
        return await super().create(new_room.model_dump())

    async def find_and_update(
        self, room_id: int, update_room: Room,
        usecase: Union[Callable, None] = None,
        ) -> Room:
        updated_room_dict = update_room.model_dump()
        return await super().find_and_update(room_id, updated_room_dict, usecase)

    async def find_and_delete(self, room: Room) -> Dict:
        return await super().find_and_delete(room)
