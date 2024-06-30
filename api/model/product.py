from .base import BaseModel

class Product(BaseModel, table=True):
    description: str
    price: float
