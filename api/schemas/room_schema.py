#std
from typing import Optional
#ext
from pydantic import field_validator
#app
from api.model.base import BaseSchema
from api.model.room import Status


options = set(item.value for item in Status)

class CreateRoom(BaseSchema):
    room_number: str
    daily_rate: Optional[float] = 90

class UpdateRoomStatus(BaseSchema):
    status: str = f"Choices({', '.join(options)})"

    @field_validator("status")
    @classmethod
    def status_are_valid(cls, status):
        if status not in options or len(status) > 11:
            raise ValueError(
                "Status must be: ("
                "Free, Occupied, Maintenance or Dirty)"
            )
        return status

class UpdateRoomDailyRate(BaseSchema):
    daily_rate: float

class GetRoom(BaseSchema):
    id: int
    room_number: str
    daily_rate: float
    status: str
