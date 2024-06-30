from enum import Enum

from api.model.base import BaseModel


class Status(str, Enum):
    FREE = "Free"
    OCCUPIED = "Occupied"
    MAINTENANCE = "Maintenance"
    DIRTY = "Dirty"

class Room(BaseModel, table=True):
    room_number: str
    status: str = "Free"
    daily_rate: float = 90
