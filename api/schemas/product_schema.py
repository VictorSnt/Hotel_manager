#std
from typing import Optional
#ext
from api.model.base import BaseSchema


class GetProduct(BaseSchema):
    id: int
    description: str
    price: float

class CreateProduct(BaseSchema):
    description: str
    price: float

class UpdateProduct(BaseSchema):
    description: Optional[str]
    price: Optional[float]
