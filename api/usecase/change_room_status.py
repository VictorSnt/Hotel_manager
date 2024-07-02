#std
from typing import Dict
#ext
from fastapi import HTTPException, status
#app
from api.schemas.room_schema import UpdateRoomStatus
from api.model.room import Room


class RoomStatusError(HTTPException):
    pass


def change_room_status(room: Room, updated_room_dict: Dict):
    new_status = updated_room_dict['status']
    valid_status = set(['Free', 'Maintenance', 'Dirty'])
    if room.status in valid_status and new_status in valid_status:
        updated_room = UpdateRoomStatus(**updated_room_dict)
        room.status = updated_room.status
        return room

    raise RoomStatusError(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail='the status occupied can\'t be changed, '
        'it must be (Free, Maintenance or Dirty) to (Free, Maintenance or Dirty)'
    )
        