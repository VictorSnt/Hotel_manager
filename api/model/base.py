#std
from datetime import datetime
from typing import Optional
#ext
from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    last_edited: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    active: bool = True

class BaseResponse(SQLModel):
    detail: str

class BaseSchema(SQLModel):
    pass
