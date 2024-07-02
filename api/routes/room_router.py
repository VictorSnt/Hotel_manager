#std
from typing import List
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

@room_router.get('/', response_model=List[GetRoom])
async def get_room():
    room_repo = RoomRepository(SessionMaker())
    rooms = await room_repo.find()
    return rooms


@room_router.get('/{room_id}', response_model=GetRoom)
async def get_room_by_id(room_id: int):
    room_repo = RoomRepository(SessionMaker())
    room = await room_repo.find(room_id)
    return room


@room_router.post('/', response_model=GetRoom)
async def create_room(room: CreateRoom):
    room_repo = RoomRepository(SessionMaker())
    new_room = await room_repo.create(room.model_dump())
    return new_room

@room_router.patch('/{room_id}/status', response_model=GetRoom)
async def find_and_update_room_status(updated_room: UpdateRoomStatus, room_id: int):
    room_repo = RoomRepository(SessionMaker())
    room = await room_repo.find_and_update(room_id, updated_room, change_room_status)
    return room

@room_router.put('/{room_id}', response_model=GetRoom)
async def find_and_update_room(room_id: int, updated_room: GetRoom):
    room_repo = RoomRepository(SessionMaker())
    room = await room_repo.find_and_update(room_id, updated_room)
    return room

@room_router.delete('/{room_id}', response_model=GetRoom)
async def find_and_delete_room(room_id: int):
    room_repo = RoomRepository(SessionMaker())
    reponse = await room_repo.find_and_delete(room_id)
    return reponse
