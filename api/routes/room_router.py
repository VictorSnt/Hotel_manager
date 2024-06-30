#ext
from fastapi import APIRouter
#app
from api.repository.room_repository import RoomRepository
from api.database.db_connector import SessionMaker
from api.schemas.room_schema import UpdateRoomStatus
from api.schemas.room_schema import CreateRoom
from api.schemas.room_schema import GetRoom
from api.usecase.change_room_status import change_room_status


room_router = APIRouter(prefix='/room')

@room_router.post('/', response_model=GetRoom)
async def create_room(room: CreateRoom):
    room_repo = RoomRepository(SessionMaker())
    new_room = await room_repo.create(room)
    return new_room

@room_router.patch('/{room_id}/status', response_model=GetRoom)
async def find_and_update_room_status(updated_room: UpdateRoomStatus, room_id: int):
    room_repo = RoomRepository(SessionMaker())
    room = await room_repo.find_and_update(room_id, updated_room, change_room_status)
    return room
