#std
from typing import Dict
#ext
from fastapi import HTTPException, status
#app
from api.schemas.room_schema import UpdateRoomStatus
from api.model.room import Room


def change_room_status(room: Room, updated_room_dict: Dict):
    if room.status and room.status != 'occupied':
        updated_room = UpdateRoomStatus(**updated_room_dict)
        room.status = updated_room.status
        return room

    raise HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail='the status occupied can\'t be changed'
    )
        